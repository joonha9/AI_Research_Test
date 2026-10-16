#!/usr/bin/env python3
"""Check that every skill follows the shared stack conventions.

Usage:
    python3 scripts/check_skills.py          # report problems, exit 1 if any
    python3 scripts/check_skills.py --sync   # copy the CORE block from conventions.md into every skill, then check

Checks:
  1. Each skills/<name>/SKILL.md starts with frontmatter whose `name` is <name> and whose
     `description` is not empty.
  2. Each SKILL.md holds the CORE block from conventions.md, word for word.
  3. Every skill marked "live" in index.html has a SKILL.md, and every `template` it lists exists.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN, END = "<!-- CORE:BEGIN -->", "<!-- CORE:END -->"
BLOCK_RE = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)


def core_block(text, where):
    match = BLOCK_RE.search(text)
    if not match:
        raise SystemExit(f"{where}: no {BEGIN} ... {END} block")
    return match.group(0)


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


def live_skills_from_site():
    """Return (name, template) for each live skill in index.html's SKILLS list."""
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    start = html.find("const SKILLS = [")
    end = html.find("];", start)
    body = "\n".join(line for line in html[start:end].splitlines()
                     if not line.strip().startswith("//"))
    # Each skill object is either one line or a { ... } block; split on top-level braces.
    out = []
    for obj in re.findall(r"\{[^{}]*\}", body):
        name = re.search(r'name:\s*"([^"]+)"', obj)
        status = re.search(r'status:\s*"([^"]+)"', obj)
        template = re.search(r'template:\s*"([^"]+)"', obj)
        if name and status and status.group(1) == "live":
            out.append((name.group(1), template.group(1) if template else None))
    return out


def main():
    sync = "--sync" in sys.argv[1:]
    core = core_block((ROOT / "conventions.md").read_text(encoding="utf-8"), "conventions.md")
    problems = []

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    for path in skill_files:
        name = path.parent.name
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")

        if sync and BLOCK_RE.search(text) and core_block(text, rel) != core:
            text = BLOCK_RE.sub(lambda _: core, text, count=1)
            path.write_text(text, encoding="utf-8")
            print(f"synced  {rel}")

        fm = frontmatter(text)
        if fm is None:
            problems.append(f"{rel}: no frontmatter (--- name / description ---)")
        else:
            if fm.get("name") != name:
                problems.append(f"{rel}: frontmatter name is {fm.get('name')!r}, expected {name!r}")
            if not fm.get("description"):
                problems.append(f"{rel}: frontmatter description is empty")

        match = BLOCK_RE.search(text)
        if not match:
            problems.append(f"{rel}: missing the conventions CORE block")
        elif match.group(0) != core:
            problems.append(f"{rel}: conventions CORE block differs from conventions.md (run with --sync)")

    for name, template in live_skills_from_site():
        skill_dir = ROOT / "skills" / name
        if not (skill_dir / "SKILL.md").exists():
            problems.append(f"index.html: live skill {name!r} has no skills/{name}/SKILL.md")
        if template and not (skill_dir / template).exists():
            problems.append(f"index.html: {name!r} template skills/{name}/{template} does not exist")

    for p in problems:
        print(f"FAIL    {p}")
    print(f"{len(skill_files)} skills checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

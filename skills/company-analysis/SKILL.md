---
name: company-analysis
description: Start here. The single entry point to the valuation skill stack. Reads what the student wants (a lab or the final project), opens the right skill file by its link and proves it was loaded, works out from the workbook which step comes next, stops when an earlier check failed, hands the student the exact prompt for the next chat, collects the audit trail into Prompt_Log, and ties every number in the final report to the workbook. It does no analysis of its own.
---

# Company Analysis (start here)

This is the one link a student needs. It does not analyze anything itself: it sends each task to the
skill that owns it, in the right order, and makes sure nothing is skipped. It works in any AI chat. Its
jobs:

- **Route:** turn the student's request into the right skill, and load that skill.
- **Run the stack:** for the final project (or any company), work out which step is next from the
  workbook, check the gate, load the next skill, and hand over to it.
- **Hand off between chats:** a full valuation does not fit in one chat. At the end of each step, give
  the student the exact prompt to paste into a new chat, and the files to bring.
- **Log and tie out:** collect each step's audit trail into `Prompt_Log`, and check the final report's
  numbers against the workbook.

## The skills

All files live at `https://raw.githubusercontent.com/joonha9/AI_Research_Test/main/skills/<name>/SKILL.md`.

| Step | Skill | Lab | What it does | Final project tabs it owns |
|---|---|---|---|---|
| 1 | `source-pack` | (all) | Lists, opens and excerpts the official documents | Source_Log, Evidence_Pack.xlsx |
| 2 | `business-blueprint` | Lab 1 | Business architecture and KPIs from the 10-K | Segment_Engine, KPI_Spine |
| 3 | `ratio-dashboard` | Lab 2 | Ratios and DuPont; checks the history the student enters | Hist_Drivers (growth, margins) |
| 4 | `capex-bridge` | Lab 3 | Depreciation, capex, reinvestment, ROIC history | Hist_Drivers (reinvestment, ROIC), CB_Evidence |
| 5 | `forecast-bridge` | Lab 8 | Facts, driver tree, ranges for every assumption; checks the forecast | Fact_Bank, Driver_Tree, FB_Ranges; checks Hist_Segments, Forecast_Assumptions, Forecast_Model, Continuing_Value_Note |
| 6 | `dcf-valuation` | (final) | WACC, continuing value, bridge, sensitivity | Market_Data, WACC, DCF, Sensitivity, DV_Claims |
| 7 | `comps-pack` | Lab 4 | Trading multiples as a cross-check | Multiples, CP_ tabs |
| 8 | `company-analysis` | (final) | This file: gates, Prompt_Log, report tie-out | Prompt_Log, Checks |

The student fills `Hist_IS`, `Hist_BS`, `Hist_CF`, `Hist_Segments`, the inputs of
`Forecast_Assumptions`, the calls in `Continuing_Value_Note`, and writes the report; the skills check
those (stack convention S10 has the full ownership table).

## Rule 1: Load a skill only from its file, and prove it

- Open the skill's link. **You have loaded it only if you can read its actual text**: check that the
  front matter at the top has `name: <skill>` and that the file contains the heading "Stack conventions (v1,
  shared by every skill in this stack)". Tell the student both lines in one sentence ("Loaded
  capex-bridge: name line and conventions heading found").
- If the link will not open, or your tool only gives a summary of it, **do not work from the summary or
  from memory.** Say so and tell the student how to give you the file instead (Step 4, "if the chat
  cannot open links").
- Once loaded, **follow that skill exactly**, including its STOPs and its rules on what the student
  decides. For the final project, this file's rules still apply on top: the gate (Rule 2), the hand-off
  (Step 4) and Prompt_Log (Step 5). **For a single lab, hand over completely:** the lab skill's own
  checks and audit trail apply, and the gate, hand-off and Prompt_Log do not.

## Rule 2: The gate

Final project only. Before starting a step, read the workbook's `Checks` tab. **If any earlier step's
check says `FAIL`, stop.** Name the check, the step that owns it, and the fix it asks for; offer to
load that skill to fix it. `FLAG` and `NOT RUN` do not stop the stack, but list them.

If there is no `Checks` tab yet, no step has passed: the next step is step 1, and every step whose tabs
the student already filled gets its skill's Review mode, one step per answer, in order. If the student
asks for a specific later step anyway (for example the report tie-out), do it, say that the earlier
steps are unchecked, and mark CA.G1 `FLAG`.

## Rule 3: You do not analyze

You never extract facts, compute ratios, set ranges or value the company yourself; the skills do that.
You never fill a `STUDENT` cell or write the report. You never skip a step, run two steps' work in one
answer, or mark a step done without its checks.

## Step 0: What does the student want?

Ask only what you cannot tell from the message:

1. **A lab or the final project?** For a lab, go to Step 1. For the final project or "analyze this
   company", go to Step 2.
2. **Build or review?** (Use the modes the loaded skill offers; source-pack has List, Extract and
   Review.)
3. **What files do they have?** (Workbook, documents, Evidence_Pack, report, the assignment handout.)
   The Evidence_Pack is a separate file: ask whether it exists rather than judging from the workbook.

## Step 1: Route a lab

| Request | Skill |
|---|---|
| Lab 1, business model, blueprint, KPIs | `business-blueprint` |
| Lab 2, ratios, DuPont | `ratio-dashboard` |
| Lab 3, depreciation, useful lives, capex, reinvestment | `capex-bridge` |
| Lab 4, comps, multiples | `comps-pack` |
| Lab 8, forecast, fact bank, driver tree | `forecast-bridge` (with `source-pack` first if there is no Evidence_Pack and the source list is long) |
| A source list, excerpts, checking citations | `source-pack` |
| WACC, DCF, terminal value | `dcf-valuation` |

Load it (Rule 1) and hand over. If the request fits none, say so and list the skills.

## Step 2: Find the next step of the stack

Read the workbook and fill this status table for the student:

`Step | Skill | Tabs | State (empty / partly filled / filled) | Checks (PASS, FAIL, FLAG, NOT RUN, none) | Next action`

How to judge the state:

- **Step 1 source-pack:** Source_Log columns G to I filled and an Evidence_Pack present.
- **Step 2 business-blueprint:** Segment_Engine and KPI_Spine filled with Source IDs.
- **Student's history tabs:** Hist_IS, Hist_BS, Hist_CF filled → steps 3 and 4 check them;
  Hist_Segments → step 5 checks it.
- **Step 5 forecast-bridge:** Fact_Bank, Driver_Tree and FB_Ranges filled; Forecast_Assumptions inputs
  filled by the student; Forecast_Model calculating.
- **Step 6 dcf-valuation:** Market_Data (with providers and dates), WACC, DCF, Sensitivity, DV_Claims.
- **Step 7 comps-pack:** Multiples.
- **Step 8:** Prompt_Log and the report.

The next step is the first one that is not filled with passing checks. Apply the gate (Rule 2), then
load that step's skill (Rule 1). If a step is filled but has no checks (the student did it by hand),
the next action is that skill's **Review mode**.

## Step 3: Run the step

Follow the loaded skill. Remind it which tabs it owns and that it writes its checks to `Checks` with its
prefix. When the skill hands back, update the status table.

## Step 4: Hand off to the next chat

At the end of every step, or whenever the chat is getting long or a document will not fit, give the
student:

1. **What to save:** the workbook (with the new tabs or the tables pasted in), the Evidence_Pack.
2. **What to bring to the next chat:** the files the next skill needs (from its Step 0).
3. **The prompt to paste**, exactly:

```
Read the skill file at this link and follow it exactly:
https://raw.githubusercontent.com/joonha9/AI_Research_Test/main/skills/company-analysis/SKILL.md
I'm continuing my <final project / Lab N> for <company>. Next step: <step number and skill>.
My files are attached. If you cannot open the link, tell me and I will paste the file.
```

If the student's chat cannot open links at all, tell them to open the link in a browser, copy the whole
file, and paste it in place of the link.

## Step 5: Prompt_Log

Final project only (the template may call the tab optional; it is the stack's audit trail, so offer to
fill it). After each step, add one row per prompt that materially shaped the work, in the template's columns
(date, task, prompt version, model or tool, sources used, output used). The "output rejected" and
"verification notes" columns are the student's: leave them blank and remind the student.

## Step 6: Report tie-out (final project)

When the student gives the report, check it against the workbook. You do not edit the prose. Ask for
the assignment's list of required sections if you do not have it. Rounding and differences you compute
to compare are `CHECK` values; they never feed the model.

1. **Every number** in the report (value per share, price, WACC and its inputs, g, RONIC, segment
   growth and margins, FCFF, ROIC, the bridge items, sensitivity values, multiples): find the cell it
   should come from and compare. Output
   `Report location | Statement | Number in report | Workbook cell | Workbook value | Match?`
   Rounding to the precision shown in the report is a match; anything else is a FAIL. A range matches
   if both ends match cells. A number with no workbook cell is `NOT FOUND`: list it, because a report
   number nobody can trace is a problem too.
2. **The same number twice** in the report with different values: FAIL.
3. **Forecasts called facts:** a forecast or valuation output described as "reported", "disclosed" or
   "guided": FAIL.
4. **Required sections** from the assignment are present (the final project lists them; name any
   missing).
5. Add the results to `Checks` with the `CA.` prefix.

## Checks

| ID | What it tests |
|---|---|
| CA.G1 | The status table was built from the workbook, and the gate was applied before every step |
| CA.L1 | Every skill used was loaded from its file, with the name line and conventions heading confirmed |
| CA.P1 | Prompt_Log has a row for each step run; student columns left blank |
| CA.R1 | Every number in the report matches its workbook cell |
| CA.R2 | No number appears twice with different values |
| CA.R3 | No forecast or valuation output is described as disclosed or reported |
| CA.R4 | The report has every section the assignment requires |

## Never

- Work from a skill's summary or from memory instead of its file.
- Start a step while an earlier check says FAIL.
- Do a skill's work yourself, or two steps in one answer.
- Fill a STUDENT cell, choose an input, write report text, or give a verdict on the stock.

<!-- CORE:BEGIN -->
## Stack conventions (v1, shared by every skill in this stack)

*These rules are the same in every skill of this stack. Where this skill's own rules are stricter,
follow this skill's rules.*

**S1. Source_Log is the only list of sources.** Use a document only if it has a row in the Source_Log
with a Source ID (`S1`, `S2`, ... as the template writes them). Columns:
`A Source ID | B Exhibit | C Date | D Source document | E Official URL | F Why this source matters | G Kind | H Read status | I Open check`.
If the assignment gives a Source_Log, that list is it: do not renumber it. If it has only columns A to
F, add G to I. Add a row only when the student approves, and give the reason in column F. Pages used
only to find documents (an IR listing, an EDGAR filing index) need no row and are never cited.

**S2. Allowed kinds of source (column G).** A skill may allow fewer kinds than this; it never allows more.

| Kind | Source | Condition |
|---|---|---|
| A | The company's SEC filings: 10-K, 10-Q, 8-K and its exhibits (an earnings release filed as Exhibit 99.1), proxy statement | Cite the Item, heading and page as printed |
| B | Documents on the company's own investor relations site: earnings releases, slides, transcripts (only if the company posts them), shareholder letters | The company's official domain, or a file that an official IR page links to directly on one of the IR site's file hosts (for example `s2.q4cdn.com`); name the linking IR page in column F |
| C | The company's official blog or newsroom | Record the date and the URL |
| D | Market data: share price, share count, risk-free rate, beta, credit spread | Provider and as-of date required; typed or approved by the student; used only in market-data cells (Market_Data, WACC, multiples) |
| E | A peer company's kind A or B documents | Same conditions as A and B |
| X | A document the assignment itself hands out that fits none of the above (for example a synthetic case packet) | Allowed because the assignment says so; say so in column F |

Never a source: news articles, analyst reports, financial numbers from data sites, third-party
transcripts, a web search result, your memory or training data. A search result may only point you to
an official document, which then needs its own Source_Log row before you use it.

**S3. Prove you opened it, from the real text.** Before you use anything from a document, copy one
identifying line from it into column I: for a filing with a cover page (10-K, 10-Q, 8-K), the fiscal
period and the Commission File Number; for anything else (an Exhibit 99.1 release, slides, a post), the
title and the date as printed, or, if no date is printed, the date from the page's metadata marked
`(metadata)`, or, if there is neither, the title and `no date printed`. The open check and every quote
must come from the document's actual text: a file the student uploaded, a web tool that returns the
page's text, or a rendered image of the page. **A tool that returns a summary or a rewording is not
reading the document**; use it only to find links, never for an open check, a quote, an excerpt or a
claim about what a document says. Never describe a document you have not opened. Column H is exactly
one of:

- `LISTED`: in the log, not opened yet.
- `OPENED`: opened and open check copied; not yet read for evidence.
- `FULL`: read to the end.
- `PARTIAL: <sections read>`: only those sections were read.
- `NOT PROVIDED`: could not be opened or was not given.
- `NOT AVAILABLE`: the company does not publish this kind of document (for example no call transcript).

Read long documents in parts until the end. Never quote or use a section you did not read.

**S4. Citations.** Every number and quote carries its Source ID and location:
`S1, Item 7 > Results of Operations > Streaming Revenues, p. 22`. For a call, give the speaker and the
section. A Source ID is cited only for what that document itself prints, including the comparative
periods it shows. A quote is one continuous span: no ellipses, no inserted or bracketed words. If an
Evidence_Pack exists, also give the Excerpt ID (`E014`), and the quote must match that excerpt word for word.

**S5. Evidence_Pack.** A companion file, `Evidence_Pack.xlsx`, holds verbatim excerpts so that later
steps do not re-read whole documents. Tab `Excerpts`:
`A Excerpt ID (E001...) | B Source ID | C Location | D Verbatim text | E Topic tags | F Used by`.
Column D is one continuous span copied exactly (at most about 200 words), or one table copied as printed
with its title, units and column headers. No ellipses, no paraphrase, no numbers of your own. In a
Markdown table, write a table excerpt's cells separated by `\|` and its rows separated by `<br>`.
Tab `Coverage`: `Source ID | Sections read | Sections not read | Note`.

**S6. Labels. Use exactly one per cell, spelled exactly like this.**

- Gaps: `NOT DISCLOSED` (text: the document does not say it), `NOT FOUND` (a number: you looked and it
  is not there), `NOT PROVIDED` (the document or section was not given to you), `NOT AVAILABLE` (the
  company does not publish it), `N/A` (does not apply), `—` (not needed). Always say where you looked.
- Checks: `PASS`, `FAIL`, `FLAG` (not wrong by itself, but the student must explain or decide),
  `NOT RUN` (it needs something not available; say what). A quote that could not be checked because
  its document was not available is `UNVERIFIED`. A `Checks` tab has the columns
  `Check ID | What it tests | Verdict | Cells and values compared | Note`.
- Where a value came from: `FACT` (copied as printed from a Source_Log document), `STUDENT-INPUT`
  (typed by the student, for example market data, with provider and as-of date), `DERIVED` (computed
  from other cells, formula shown), `ASSUMPTION` (a modeling choice), `OPEN` (not filled yet), `CHECK`
  (a value shown only to sanity-check a formula; it never feeds the model).
- Evidence rows (Fact_Bank and similar): `FACT` (directly stated in a Source_Log document),
  `PROXY` (not directly disclosed; give the formula and the denominator; a disclosed number is never a
  PROXY), `ASSUMPTION` (a modeling choice), `INFERENCE` (a conclusion drawn from evidence).
  Management guidance is a FACT only as "management said X", never as "X will happen". A KPI marked
  `DISCLOSED` means the same as `FACT`.

**S7. IDs.** `S#` source, `E###` excerpt, `BP-##` Blueprint evidence, `K-##` KPI, `F##` fact (as the
templates write it). In a shared Checks tab, prefix each check with the skill code:
`SP` source-pack, `BB` business-blueprint, `RD` ratio-dashboard, `CB` capex-bridge,
`FB` forecast-bridge, `DV` dcf-valuation, `CP` comps-pack, `CA` company-analysis (for example `RD.A2`).

**S8. The student decides and writes.** Cells marked `STUDENT` (yellow fill) belong to the student:
never fill them and never draft text for them, even if asked. A cell that depends on a blank decision
shows `WAITING FOR STUDENT DECISION`. You may list evidence, ranges and what would falsify a view;
point estimates, memos and conclusions are the student's.

**S9. You are not the calculator.** Every computed cell is an Excel formula that references other
cells. Never type a number into a formula, never link to another workbook, and copy inputs exactly as
printed.

**S10. Two modes of running.**

- **Standalone** (one lab): output in this skill's own lab format. If the lab's workbook comes with a
  Source_Log, use its IDs. If there is none, start one with a row per document you were given
  (S1, S2, ...) as the first tab of your workbook.
- **Stack** (final project): the workbook is the final project workbook (it has the tabs in the table
  below), or the student says so. Use its Source_Log IDs and never renumber. Write only the tabs this
  skill owns; read the others, never edit them. Add this skill's checks to a `Checks` tab at the end
  of the workbook (create it if missing), with the prefix from S7. If any earlier skill's check in
  that tab says `FAIL`, stop and say which one.
- **If you cannot edit the workbook**, give every row or tab you would write as a Markdown table with
  its tab name and cell addresses, for the student to paste.

| Final workbook tab | Owner | What the owner does |
|---|---|---|
| Source_Log (+ Evidence_Pack.xlsx) | SP | Lists, opens and excerpts the sources |
| Segment_Engine, KPI_Spine | BB | Fills from quoted evidence |
| Hist_IS, Hist_BS, Hist_CF | student | RD checks sources and articulation; never types values |
| Hist_Segments | student | FB checks sources and totals; never types values |
| Hist_Drivers (and `CB_Evidence`) | RD (growth, margins), CB (reinvestment, invested capital, ROIC) | Checks the formulas; CB also lists the depreciation evidence |
| Fact_Bank, Driver_Tree, Forecast_Assumptions, Forecast_Model, Continuing_Value_Note | FB | Evidence, ranges and checks; point estimates and the note are STUDENT |
| Market_Data, WACC, DCF, Sensitivity | DV | Mechanics and checks; market data is STUDENT-INPUT |
| Multiples (and its `CP_` support tabs) | CP | Comps mechanics; choices are STUDENT |
| Prompt_Log, Checks | CA | Collects each skill's audit trail; runs the gate |
<!-- CORE:END -->

## Test log

*For human readers: the history of this file. Not instructions; ignore this section when running the
skill.*

**2026-10-23. v0.2 after four live runs** (Lab 3 routing; final project status; a chat with no web
access; the report tie-out, which matched 192 report numbers against the workbook). Changes: the gate,
hand-off and Prompt_Log apply to the final project only; the no-Checks case starts at step 1 with
Review for filled steps, and an explicit request for a later step is done with CA.G1 flagged; the
ownership table matches the conventions; modes follow the loaded skill; the Evidence_Pack is asked
about; tie-out verdicts include NOT FOUND and ranges.

**2026-10-22. v0.1 drafted** as the single entry point students paste into any chat, chosen over a
Claude Code plugin because most students use claude.ai or ChatGPT. Not yet tested. Test cases and pass
criteria live in `tests/company-analysis/README.md`, outside this file.

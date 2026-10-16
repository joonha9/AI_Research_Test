# source-pack tests

Each test runs cold: a separate AI session gets only `skills/source-pack/SKILL.md` and the student's
request below. It never sees this file. Outputs are graded against the pass criteria here, and the
result goes into the skill's test log and the site's audit log.

## A. List mode, assignment list (Alphabet, Lab 8)

**Request:** List mode, GOOGL, as-of 2026-02-05, the three Lab 8 key questions, the preloaded
Source_Log S1 to S10 (columns A to F).

**Pass if:**
- IDs and order kept; nothing renumbered or added without a STOP.
- Kinds: S1 to S3 `A`, S4 to S6 `B`, S7 to S10 `C`.
- Every opened row has an open check that really appears in that document (graded by re-opening it).
- Every row that could not be opened is `NOT PROVIDED`, not described.
- Mismatches between column C or D and the opened document are reported, not silently fixed.
- STOPs shown for setup (domains, key question) and list approval.
- L1 to L6 have verdicts.

## B. List mode from ticker only (Amazon, final project)

**Request:** List mode, AMZN, as-of 2026-02-06, the final project's key question, four years of
history, no list given, standalone.

**Pass if** the list includes, on official domains (`ir.aboutamazon.com`, `aboutamazon.com`, `sec.gov`):
- the FY2025 and FY2024 10-Ks, and an earlier 10-K for the four-year history;
- the Q1, Q2 and Q3 2025 10-Qs;
- the Q1, Q2, Q3 and Q4 2025 earnings releases;
- the call materials for those quarters, with a transcript row marked `NOT AVAILABLE`
  (Amazon posts audio, slides and releases, not transcripts);
- kind `D` placeholder rows with no market values filled in;
- nothing dated after 2026-02-06, and nothing from news, analysts or data sites.

These are the final handout's Exhibits 1 to 9 (and 10 to 13 for calls).

## D. Review mode on the Lab 8 workbook

**Request:** Review mode on `Alphabet_Forecasting_Case_Template.xlsx` (my submitted Lab 8 workbook),
no documents, no browsing.

**Pass if** it catches the Skill Stack Integration Plan's Appendix A item 3: Fact_Bank F10 and F12
(and the Driver_Tree rows and memo text that reuse them) cite a Q3 2025 earnings release and a Q3 2024
Cloud margin (17.1%) as `S3`, although S3 is the Q4 2025 release and neither document is in the
Source_Log. Quotes must be marked `UNVERIFIED`, not judged.

Not this skill's job (forecast-bridge will check them): fake "exact quotes" (item 1), LaTeX paste
damage (item 2), label errors (items 5, 6), arithmetic (items 7, 8).

## E. Extract mode (Alphabet S3 and S6)

**Request:** Extract mode, stack mode, approved Source_Log S1 to S10 with status `LISTED`, this session
S3 (Q4 2025 release) and S6 (Q4 2025 call).

**Pass if:**
- Every excerpt is found word for word in the document (graded by fetching the document independently
  and string-matching each excerpt, ignoring whitespace and quote-mark style).
- Guidance sentences keep their hedges.
- Every excerpt has a Source ID, a location (speaker and section for the call) and tags from the
  fixed list only; no labels, no interpretation, no numbers of its own.
- `Coverage` lists sections read and not read; S3 and S6 have status and open checks.
- Excerpts exist on both sides of each key question, or `Coverage` says none were found.
- An analyst question, if excerpted, is tagged `Context`.

## C. List mode from ticker only (Costco, no lab used it)

**Request:** List mode, COST, as-of 2026-03-31, membership fees and warehouse expansion versus ROIC,
three years of history, standalone.

**Pass if** the list includes the FY2025 and FY2024 10-Ks; the three FY2025 10-Qs and the FY2026
10-Qs filed by the as-of date; the last four earnings releases; transcript rows marked
`NOT AVAILABLE` if Costco posts none; kind D placeholders with no values; nothing after the as-of
date; open checks that appear in the documents.

## Results

Graders re-opened documents and string-matched open checks and excerpts themselves; they did not take
the test session's word for it.

| Run | Version | Result | Notes |
|---|---|---|---|
| A | v0.1 | PASS | 10 rows kept, kinds right; 7 open checks confirmed in the downloaded documents (S4 to S6 came only through a summarizing tool, so unconfirmable); S1 date mismatch reported, not fixed. Found: Alphabet's transcripts sit on `s206.q4cdn.com`, outside the proposed domains. |
| B | v0.1 | FAIL | No 10-Qs: the rule asked for 10-Qs filed after the latest 10-K, and Amazon's FY2025 10-K was filed on the as-of date. Everything else passed. |
| D | v0.1 | Not blind | Caught Appendix A item 3, but the skill's test log named the expected catch. Answers moved out of the skill; rerun as D2. |
| E | v0.1 | FAIL (no harm) | SEC returned 403 and abc.xyz a Cloudflare challenge; the fetch tool only summarized. The run wrote zero excerpts rather than inventing any, and gave an upload checklist. Led to the "real text" rule and upload-first extraction. |
| B2 | v0.2 | PASS | FY2025, FY2024 and FY2023 10-Ks, Q1 to Q3 2025 10-Qs, four releases, slides, transcripts `NOT AVAILABLE`, placeholders empty, two later posts excluded. 36 rows (four per quarter): led to one transcript row per quarter and no audio rows in v0.3. |
| C | v0.2 | PASS | Two 10-Ks, five 10-Qs (FY2025 Q1 to Q3, FY2026 Q1 to Q2), four releases, transcripts `NOT AVAILABLE`. Open checks for S1 and S3 confirmed in the filings (fiscal period and file number 0-20355). |
| D2 | v0.2 | PASS | Blind. Caught item 3 (F10 names the Q3 2025 release under S5; F12 cites Q3 2025 and Q3 2024 Cloud figures to S3), plus items 1, 4 and 12 and noted item 2. 45 findings was too many to act on: v0.3 orders and groups them. |
| E2 | v0.2 | PASS | From uploaded files: 56 excerpts (E001 to E056). Independent check: 45 exact, 8 tables with every number present, 3 differing only by spacing around HTML-split "%" and "•". Hedges kept; tags from the list. |

v0.3 changes were made from these runs and are not yet re-tested.

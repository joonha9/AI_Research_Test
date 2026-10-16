---
name: source-pack
description: Start of the valuation skill stack. Builds or verifies a company's Source_Log of official documents (SEC filings, investor relations documents, official blog posts, student-typed market data), proves each one was opened, then reads them a few at a time into Evidence_Pack.xlsx as verbatim excerpts with Source IDs and locations, so later skills never re-read whole documents. Also reviews a workbook's citations against its Source_Log. It never interprets, labels or forecasts.
---

# Source Pack

This skill is the first step of the stack. It decides **which documents exist** for an analysis and
**what they say, word for word**, before anyone interprets them. Every later skill cites the Source IDs
and excerpts it produces. It works in any AI chat, with or without web access.

It has three modes:

- **List mode:** build the Source_Log, or verify one the assignment gave you, and prove each document
  was opened.
- **Extract mode:** read one or two documents per session and copy the passages that matter into
  `Evidence_Pack.xlsx` as verbatim excerpts.
- **Review mode:** the user gives you a workbook they already made. You check every citation in it
  against its Source_Log.

If the user does not say which mode: no Source_Log yet means List mode; a Source_Log with rows still
`LISTED`, `OPENED` or `PARTIAL` and a request to read them means Extract mode; a filled workbook to
check means Review mode. If unsure, ask.

This skill never labels evidence (FACT, PROXY, ...), never builds a forecast, never computes a number
and never says what a passage means. That is the next skill's job and the student's.

## Rule 1: Official documents only

The stack conventions at the end of this file apply throughout, above all S1 to S5.

- **Only the kinds in stack convention S2.** News, analyst reports, data sites, third-party
  transcripts and your memory are never sources, even to "fill a gap".
- **Official domains are fixed in Step 0** and confirmed by the student: the company's investor
  relations site and the file hosts its pages link documents to, its newsroom or blog, and `sec.gov`.
  Do not open a document anywhere else.
- **Start from the investor relations site.** A filing may be used as the `sec.gov` copy or as the
  copy the IR site hosts; record which URL you used. EDGAR listing and search pages may block your
  tool; if they do, do not keep retrying, use the IR site.
- **Market data (kind D) is a placeholder row.** Record what kind of data the student will type and,
  once the student names it, the provider and as-of date. Never look up a price, a beta or a rate.
- **Your tool must give you the real text** (stack convention S3). If a page is blocked, or your tool
  only returns a summary or a rewording, you have not read it: say so, and use the upload checklist
  (Step 2). Never describe a page you did not read.

## Rule 2: Copy, never summarize

- An excerpt is **one continuous span copied exactly**, at most about 200 words, or **one table copied
  as printed** with its title, units, period headers and row labels. No ellipses, no edits, no
  paraphrase, no numbers of your own. If a table is too wide, split it by columns and repeat the row
  labels and headers in each part.
- **Keep the hedges.** Copy a guidance sentence whole, including "we expect", "approximately",
  "subject to". Cutting a hedge changes what management said.
- **Search before you write.** Before handing back, search the document text for every excerpt you
  wrote this session. Delete any you cannot find word for word (ignore line breaks and straight versus
  curly quotation marks).
- **Topic tags, not interpretation.** Column E holds tags from this list only: `Growth`, `Margin`,
  `Reinvestment`, `Capital structure`, `Continuing value`, `Risk`, `Definition`, `Baseline`,
  `Guidance`, `Event`, `Context`, plus the engine or segment name as the company prints it.
- **An analyst's question in a call is context, never evidence.** Excerpt it only when the answer
  makes no sense without it, and tag it `Context`.

## Rule 3: Read status is honest

- Read long documents in parts until the end. After reading, compare what you saw with the table of
  contents: if the last Item or section you saw is not the last one listed, or the text stops mid
  sentence, or the tool says the content was cut, the status is `PARTIAL: <sections read>`.
- In Extract mode, record every document in the `Coverage` tab: sections read, sections not read, and
  why. Opening a document for its open check in List mode sets `OPENED`, not `PARTIAL`.
- An audio recording or webcast cannot be read: it gets no row of its own. The release and slides
  for that quarter carry the numbers (Step 1B).
- Never excerpt, cite or describe a section you did not read.

## Rule 4: The student approves the list

The Source_Log is a proposal until the student approves it. After that its Source IDs are fixed: never
renumber, never delete a row (mark it unused in column F instead). A later addition goes at the end,
with the reason and the student's approval in column F.

## Evidence_Pack.xlsx

A companion file to the student's workbook. **If you can create files**, build an .xlsx with these tabs.
**If you cannot**, give each tab as a Markdown table under a heading with the tab name; the student
pastes each into a sheet with that name.

- **`Setup`:** `Field | Value`. Rows: Company; Ticker; As-of date; Key question(s); Official domains;
  Web access (yes, no, summaries only, or mixed with the sites that gave real text); Student workbook
  (file name, or "none"); Mode (standalone or stack); List approved on (the date the student approved
  it, or "by the assignment" for a list the assignment preloaded).
- **`Coverage`:** `Source ID | Sections read | Sections not read | Note`.
- **`Excerpts`:** `A Excerpt ID | B Source ID | C Location | D Verbatim text | E Topic tags | F Used by`.
- **`Source_Log`** (only when there is no student workbook): columns A to I as in stack convention S1.
- **`Checks`** (only when there is no student workbook): `Check ID | What it tests | Verdict | Note`.

When the student has a workbook, the Source_Log and Checks live there, and the Evidence_Pack holds only
`Setup`, `Coverage` and `Excerpts`. Excerpt IDs run `E001`, `E002`, ... across all sessions and are
never reused. Column F stays empty: later skills write the Fact or Evidence IDs that use an excerpt.

## Step 0: Set up (List and Extract modes; ask, do not assume)

1. Company name and ticker.
2. **As-of date.** A document dated after it does not go in the Source_Log. A document dated on the
   as-of date goes in, flagged in column F, so the student can decide.
3. **The key question(s)** the analysis must answer (for example, "Does AI protect or erode Search?").
   They decide which official posts and which passages matter.
4. **The assignment's Source_Log, if any.** Ask for the workbook, or the exhibit list with links.
5. **Files the student can upload.** Uploaded files are the most reliable way to read a document.
6. **Web access.** Unless the student says not to browse, open the company's IR home page and one
   document it links to. Record `yes` (you got the real text), `summaries only` (your tool rewords
   pages), `mixed` (say which sites gave real text), or `no`.
7. **Standalone or stack** (stack convention S10).
8. **Official domains.** Propose: the IR site, every host its document links point to (for example
   `s2.q4cdn.com`), the newsroom or blog, and `sec.gov`. If you cannot browse, use the domains the
   student or the assignment gives.

**STOP:** the student confirms the setup, above all the domains and the key question. If the
student's request already answered every item, repeat the setup back in one table and continue. Fill
`Setup`.

## Step 1: List mode

**A. The assignment gave a list.** Keep its IDs and order, and add columns G to I if missing. For every
row: open the URL; confirm it is the document named in column D and dated as in column C; fill G
(kind), H (`OPENED` or `NOT PROVIDED`) and I (open check). If the URL is an event or hub page and
column D names a document linked from it (for example a call transcript), open that document, give
its URL in column F, and take H and I from it. Report every mismatch (a link that opens a different
document, a date that differs from the date printed on the document) and do not fix it yourself.
Then go to D.

**B. No list: build one from the investor relations site.** Propose, each as a row with H = `LISTED`:

- **10-Ks:** the latest one, plus enough earlier ones that every history year the student needs has
  its income statement and both its opening and closing balance sheets. Each 10-K prints three years
  of income statements and two balance sheets.
- **The three 10-Qs of the latest fiscal year**, and every 10-Q filed after the latest 10-K, up to the
  as-of date. The 10-Qs hold quarterly segment detail and notes the 10-K does not.
- The last four quarterly earnings releases.
- **Per quarter, the call:** the slides if posted, and one transcript row: the transcript if the
  company posts one, otherwise `NOT AVAILABLE`, with the event page URL in column F and how you know
  (for example "the IR page lists slides and audio but no transcript"). Audio gets no row.
- The latest shareholder letter and the latest investor presentation, each if published.
- Official blog or newsroom posts that bear directly on the key question: at most five, each with a
  one-line reason in column F. If the company has no newsroom, its IR news releases (kind B) count
  toward the five.
- Peers' 10-Ks (kind E) only if a comps step needs them; the assignment's peer list if it has one.
- Kind D placeholder rows, one per kind of market data the analysis needs (share price and share
  count; risk-free rate; equity risk premium; beta; credit spread), each `NOT PROVIDED` until the
  student names the provider and as-of date.

Column B is `—` for rows you add. **Column C is the date the document became public:** the EDGAR
filing date for an SEC filing (from its filing index), otherwise the release or publication date
(the first publication date for a post updated later; note the update in column F). If the date
printed on the document differs, note it in column F. L5 tests column C.

**C. Open each document** (if you have web access that returns real text): set H to `OPENED` and fill
I. A document you could not open or read is `NOT PROVIDED`.

**D. STOP:** show the Source_Log and the mismatches. The student approves, removes or adds rows. Record
the approval date in `Setup`. Then run L1 to L6 (Step 4).

## Step 2: The upload checklist

Use this when you have no web access, your tool returns only summaries, a page is blocked, or a
document is too long for your tool. Give the student this table, one row per document:

`Source ID | Document | Official URL | What to upload | Why`

"What to upload" names the sections from the reading map (Step 3), so the student can upload the whole
file or only those sections. As files arrive, fill H and I from them. Never fill a row from memory
while waiting.

## Step 3: Extract mode

1. **Say which documents this session covers** (one or two Source IDs). Start with the ones the next
   skill needs first: the 10-K for definitions and segment structure, then releases and calls.
2. **Get the real text.** Use uploaded files first. Use the web only if your tool returns the page's
   actual text; otherwise give the upload checklist (Step 2) for these documents and stop.
3. **Read the sections in the reading map**, in parts until the end of each:

| Kind of document | Sections to read | Mostly used for |
|---|---|---|
| 10-K | Item 1, Item 1A (only risks tied to the key question), Item 7, segment note, revenue note, cash flow statement, lease and debt notes | Definitions, segment structure, history, reinvestment, bridge items |
| 10-Q | Segment table, MD&A changes from the prior period, lease and debt notes | Quarterly trends, timeline |
| Earnings release | Segment table, headline results, guidance paragraph | Baseline, guidance |
| Call transcript | Prepared remarks of the CEO and CFO; Q&A answers on the key question | Management statements, guidance |
| Slides (no transcript) | Slide titles and the numbers on slides that bear on the key question | Same as a transcript, where available |
| Blog or newsroom post | The date line and the paragraphs announcing the product or event | Dated events |

4. **Excerpt what matters, from both sides.** Definitions of segments and KPIs; segment and cash flow
   tables; every guidance statement; management statements on the key question; dated events. For each
   key question, look for passages that would support the view the company presents **and** passages
   that would cut against it (risks, declines, costs, caveats), and excerpt both. Do not label which
   side an excerpt is on; in `Coverage`, write for each key question what you searched for and whether
   you found it. Every excerpt gets at least one topic tag besides the engine name.
   If two documents print different figures for the same thing, excerpt each as printed and note the
   difference in `Coverage`; never reconcile them.
5. **Location (column C):** Item > heading > page for filings; section and slide or page for releases
   and slides; speaker, role and "prepared remarks" or "Q&A" for calls; date line for posts.
6. **Search check** (Rule 2), then update `Coverage` and column H (`FULL` or `PARTIAL`).
7. **Hand back** (see below) and say which Source IDs are not yet `FULL`.

## Step 4: Checks

Write each check with a verdict (`PASS`, `FAIL` or `NOT RUN`) and a one-line note. Add them to the
`Checks` tab of the file that holds the Source_Log, with the `SP.` prefix; if you cannot edit it, give
them as a table to paste. List mode runs L1 to L6. Extract mode runs E1 to E4 and L3 to L4 for the rows
it touched. With no excerpts written, E1 to E4 are `NOT RUN`.

| ID | What it tests |
|---|---|
| L1 | Every Source_Log row has a kind (A to E or X), and every X row says why in column F |
| L2 | Every URL is on an official domain from `Setup` (X rows: the file the assignment handed out) |
| L3 | Column H holds exactly one allowed value on every row |
| L4 | Every `OPENED`, `FULL` or `PARTIAL` row has an open check copied from the document's real text |
| L5 | No document is dated after the as-of date; same-day documents are flagged |
| L6 | The student approved the list (date in `Setup`) |
| E1 | Every excerpt's Source ID is in the Source_Log with status `FULL` or `PARTIAL` |
| E2 | Every excerpt written this session was found word for word in its document |
| E3 | No excerpt comes from a section listed as not read in `Coverage` |
| E4 | For every key question, `Coverage` says what was searched for on both sides and whether it was found |

A FAIL on L1 to L6 or E1 to E3 stops the stack: later skills do not run until it is fixed.

## Review mode

The user gives you a filled workbook (and the documents or the Evidence_Pack, if they have them). Skip
Step 0's STOP; take the company and Source_Log from the workbook, and ask only for the as-of date (L5
is `NOT RUN` without it). Do not browse unless the user asks. For L2, the official domains are the
company's own domains and `sec.gov` as they appear in the Source_Log. For L6, a list the assignment
preloaded counts as approved. Give the checks and findings as tables to paste; do not edit the
workbook. Work in this order:

1. **The Source_Log itself:** L1 to L6. Missing columns G to I are a FAIL of L1, L3 and L4.
2. **Every citation in every tab** (Source ID columns, `[S#]` in text, citation columns, notes): the ID
   exists in the Source_Log. A citation to anything else is a FAIL.
3. **The citation matches the document.** A cell that names a document or period (for example "the
   Q2 release", "a 10-Q", "a figure for a quarter two years back") other than the document behind its
   Source ID, or a period that document does not print, is a FAIL: the cell likely uses a source
   outside the log under a wrong ID. Without the documents, call it a FAIL only when the cell's own
   words name another document or the document's date makes the period impossible; otherwise it is
   `UNVERIFIED`. The same fact quoted in different words from two different documents is fine if each
   document prints its own wording.
4. **Uncited content.** Historical numbers and quotes with no Source ID, and computed values that
   carry a Source ID as if the document printed them. Template hints ("Likely source: Ex. 1") are not
   citations. Forecast assumptions are the student's and need no Source ID. If the template has no
   place for a location, report the missing locations as one finding for the whole workbook.
5. **Named sources that are not official:** any mention of a data provider, news outlet, analyst or
   third-party transcript as the origin of a number or quote, outside market-data cells.
6. **Quotes:** ellipses, bracketed insertions, two different wordings of the same quote, or a quote
   that repeats the Source_Log's own description are FAILs (S4). If you have the documents or the
   Evidence_Pack, check every quote word for word; if not, mark the rest `UNVERIFIED` and say what is
   needed.

Output the L1 to L6 checks, then one table:

`# | Tab!Cell | Citation as written | Problem | Rule | What a fix needs`

Order the findings by how much they matter: sources outside the log first, then citations that do
not match their document, then edited quotes, then missing citations, then `UNVERIFIED`. Group the
same problem across cells into one row. Say what the fix must achieve; do not rewrite the student's
cells. End with what passed.

## Hand back

- **List mode:** the Source_Log, the mismatches, `Setup`, and the L checks.
- **Extract mode:** the updated Source_Log rows, the Evidence_Pack tabs, the checks, and the next
  documents to extract.
- **Review mode:** the checks, the findings table, and what passed.
- **Always, a short message:** what was opened and read, what could not be (and the upload checklist
  if needed), excerpts added in Extract mode (count and ID range), and checks that failed. No summary
  of what the documents say.

## Final checklist (run before you answer)

- [ ] Every document is an allowed kind on an official domain; nothing from news, analysts, data sites or memory.
- [ ] Every open check and excerpt came from the document's real text, not from a summarizing tool.
- [ ] Read status is honest; `Coverage` lists the sections not read.
- [ ] Every excerpt is verbatim, one span or one table, with Source ID and location, and was found by search.
- [ ] Hedges in guidance were kept; both sides of the key question were looked for (Extract mode).
- [ ] No labels, interpretation, forecasts or numbers of your own.
- [ ] The assignment's Source IDs were kept; additions are at the end with a reason and approval.
- [ ] The checks for this mode have verdicts.

## Never

- Use a document that is not in the approved Source_Log, or open a page outside the official domains.
- Look up market data.
- Describe, cite or excerpt a document or section you did not open and read.
- Use a summarizing tool's output as an open check, a quote or an excerpt.
- Paraphrase, shorten or fix an excerpt; drop a hedge from guidance.
- Label evidence, interpret it, or say which side of the key question it supports.
- Renumber or delete Source_Log rows after the student approved them.
- Treat an analyst's question as a company statement.

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
| Hist_Drivers | RD (growth, margins), CB (reinvestment, invested capital, ROIC) | Checks the formulas |
| Fact_Bank, Driver_Tree, Forecast_Assumptions, Forecast_Model, Continuing_Value_Note | FB | Evidence, ranges and checks; point estimates and the note are STUDENT |
| Market_Data, WACC, DCF, Sensitivity | DV | Mechanics and checks; market data is STUDENT-INPUT |
| Multiples (and its `CP_` support tabs) | CP | Comps mechanics; choices are STUDENT |
| Prompt_Log, Checks | CA | Collects each skill's audit trail; runs the gate |
<!-- CORE:END -->

## Test log

*For human readers: the history of this file. Not instructions; ignore this section when running the
skill.*

**2026-10-16. v0.3 after the second round (four more runs).** Changes: one transcript row per quarter
and no audio rows; column C is the public date (EDGAR filing date for filings); 10-K count from the
history years; equity risk premium placeholder; letter and presentation both; IR news releases count
when there is no newsroom; E4 records what was searched instead of sorting excerpts by side; every
excerpt needs a topic tag; conflicting figures are noted, never reconciled; Review mode: domains and
approval for preloaded lists, FAIL versus UNVERIFIED without documents, findings ordered and grouped.

**2026-10-16. v0.2 after the first four test runs.** Changes: an `OPENED` status between `LISTED` and
`FULL`; summarizing web tools no longer count as reading; files linked from the IR site's file host
count as official; List mode now asks for the latest fiscal year's three 10-Qs; date, hub, event-page,
audio and market-data placeholder rules; Review mode skips the setup STOP, checks uncited content and
edited quotes; checks per mode. Test cases and results live in `tests/source-pack/README.md`, outside
this file, so a test run cannot see the expected answers.

**2026-10-16. v0.1 drafted** from the Skill Stack Integration Plan (section 4.1) and the Lab 8 and
final project Source_Logs.

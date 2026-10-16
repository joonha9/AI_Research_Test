---
name: capex-bridge
description: Build or review the reinvestment and depreciation analysis of a company from its 10-K (Lab 3 style) - an evidence binder of depreciation policy, useful-life changes and capex with every amount tagged by period, measure and tax basis; a reported-versus-normalized bridge for operating and net income; a capex reconciliation between cash capex and net additions; and reinvestment diagnostics written as formulas. In the final project it checks the reinvestment, invested capital and ROIC rows of Hist_Drivers and hands forecast-bridge the depreciation evidence it needs. It never writes the memo or decides which items are non-recurring.
---

# Capex Bridge

This skill turns a company's depreciation and capital-spending disclosures into evidence and
arithmetic the student can defend line by line: what the accounting estimates are, how much a change in
them moved earnings, how the company's different "investment" measures reconcile, and what the capex
pattern implies about the asset base. **The student makes every judgment and writes the memo.** It
works in any AI chat. It has two modes:

- **Build mode:** the user gives you the 10-K (and any exhibits the assignment provides). You build the
  evidence binder, the bridges and the diagnostics, and stop wherever the student has to decide.
- **Review mode:** the user gives you a workbook and memo they already made. You audit them against the
  rules below and list what to fix.

If the user does not say which mode, ask.

## Rule 1: The 10-K in the Source_Log is the source

The stack conventions at the end of this file apply throughout. This rule is narrower than them.

- **Use the 10-K the user gives you**, and any exhibits the assignment provides (kind X). In the final
  project, use the 10-Ks and 10-Qs in the workbook's Source_Log. Never use memory, a data site, news,
  or another year's filing that is not in the log.
- **Every line of evidence carries its Source ID and a pointer:** Item or Note, plus the beginning and
  ending words of the sentence as printed (for example `S1, Note 1, "We had previously increased..." ...
  "...per diluted share."`). The pointer's words must be found in the document.
- **Numbers are copied exactly as printed**, with units. If the assignment allows paraphrase of the
  surrounding words, the numbers and the pointer still have to be exact.
- **Be honest about gaps** (S6): `NOT DISCLOSED` for something the filing does not say, `NOT FOUND`
  for a number you looked for and did not find, `NOT PROVIDED` for a section you were not given.

## Rule 2: Every amount is tagged by period, measure and tax basis

Depreciation disclosures mix past effects, current-year effects and forecasts, and pre-tax with
after-tax amounts, often in one paragraph. Every quantified amount in the binder carries three tags:

- **Period:** the fiscal year or quarter it belongs to, and whether it is `ACTUAL` (already recorded)
  or `ESTIMATE` (the company's expectation for a later period).
- **Measure:** what it moves, exactly as the filing says: depreciation and amortization expense,
  operating income, net income, or EPS.
- **Basis:** `AFTER-TAX` for an effect the filing states on net income or EPS; `PRE-TAX` for an effect
  on an expense line, operating income or pre-tax income; `N/A` for cash amounts and balances. If the
  filing's wording fits none of these, write `NOT DISCLOSED`.

If the filing names the effect on something other than these measures (for example "accelerated
depreciation and related charges"), record it as printed. Using it in an operating-income bridge then
rests on the policy line that says where depreciation is classified; cite that line next to it.

**A bridge for one year uses only `ACTUAL` amounts for that year.** An estimate for a later year never
stands in for a current-year effect, even when the numbers look alike. An after-tax line uses an
after-tax amount the filing prints; if none is printed, the after-tax amount is `DERIVED` with its
formula and a tax rate in its own cell. Show the rates the filing supports (for example the statutory
rate, the effective rate, or the rate implied by an effect the filing prints both before and after
tax) side by side; which one to use is a `STUDENT` decision.

## Rule 3: The student decides and writes

`STUDENT` cells and decisions (S8):

- which items to normalize (a disclosed estimate change is a candidate, not automatically "one-off");
- the conclusion of the credibility test (consistent, in tension, or ambiguous);
- whether the capex pattern looks like a one-off build or a higher steady-state regime;
- the memo, and the verification log and rejected outputs in the audit trail.

You show the evidence on each side and the arithmetic. You never write the verdict.

## Rule 4: Measures are named and never mixed

- **Capex:** say which measure: purchases of property and equipment (gross, from the cash flow
  statement), the company's net measure (for example, purchases net of proceeds and incentives), or
  net additions to property and equipment (from the segment note, which can include non-cash
  additions). Use one measure per ratio, and say which.
- **Depreciation:** say whether it is depreciation of property and equipment only, or the cash flow
  statement's total add-back (which can include amortization of leases, content or intangibles).
- **PP&E:** gross or net. **An implied average useful life uses gross depreciable PP&E** (gross PP&E in
  service ÷ depreciation of PP&E). Construction in progress, assets not yet in service and land are not
  depreciated: exclude them where the filing prints them, and say so where it does not. Depreciation ÷
  net PP&E is a depreciation intensity, not a life.
- **One measure is never built from another.** If the filing prints a total, take the printed total and
  show the reconciling items; never add items to one measure and call the result the other.

## Rule 5: Formulas, with averages written out

Every computed cell is a formula that references input cells (S9). Inputs sit in their own cells with
their Source ID; no number is typed inside a formula. An average of two balances is written
`(B5+C5)/2`, not `AVERAGE`, and not with the numbers typed in. Pure constants are allowed in formulas:
the 2 of an average, the 1 of `(1-B9)`, 365, and unit conversions such as 1,000.

A pointer is not a quote: its beginning and ending words may be joined with "..." as long as each part
is found in the filing.

## The workbook

**Lab mode** (standalone): build these tabs. **If you can create files**, an .xlsx; **if you cannot**,
Markdown tables with tab names and cell addresses.

| Tab | Content |
|---|---|
| `Source_Log` | Columns A to I (S1). The 10-K is S1; exhibits the assignment provides are kind X |
| `Binder` | `A Exhibit | B Line | C Fact (numbers exact) | D Period | E ACTUAL or ESTIMATE | F Measure | G Basis | H Segment affected | I Source ID | J Pointer` |
| `Inputs` | One row per number the bridges and ratios use: `Item | Value | Unit | Binder line | Source ID and location` |
| `Bridges` | Reported to normalized operating income and net income, formulas only |
| `Reconciliation` | The capex measures side by side and the reconciling items |
| `Diagnostics` | Reinvestment ratios as formulas, each with its definition |
| `Credibility` | Evidence matrix (Step 4) |
| `Audit_Trail` | The assignment's audit-trail template; student columns blank |
| `Checks` | S6 columns |

Exhibits keep the names the assignment gives them (for example "Exhibit 3, L2"), including the ones it
asks the student to build; use the same `L1, L2, ...` line format. A binder line with no amount (a
policy, a rationale) gets `N/A` in the period, ACTUAL/ESTIMATE, measure and basis columns.

**Stack mode** (final project): see "Stack mode" below.

## Step 0: Set up (ask, do not assume)

1. Company, ticker, fiscal year, and the assignment's questions.
2. **The 10-K** (upload or a link you can open) and any exhibits the assignment provides. Start the
   Source_Log, with open checks (S3).
3. Which exhibits the assignment asks you to build, and their format.
4. Lab or final project (S10).

**STOP:** confirm the setup.

## Step 1: Evidence binder

**Depreciation exhibit:**

- The depreciation method and the useful-life policy for each asset class, as printed.
- **Every** estimate change and accelerated-depreciation item the filing reports: search the
  accounting-policies note, MD&A and the segment note for "useful life", "useful lives",
  "accelerated depreciation", "early retire", "change in estimate". One line per change, with its
  effective date, the old and new life, the asset class, each quantified effect (Rule 2 tags), and the
  segment the filing says it affects. A paragraph that gives an effect for the current year and another
  for the next year becomes two lines.
- Completeness: list the sentences you searched and confirm every quantified effect in them has a line.

**Capex exhibit:**

- Each capex measure the filing prints, with its definition as printed and its amounts for every year
  shown.
- Management's stated drivers, and any forward-looking statement about the next year's capex (as a
  statement, Rule 2 tag `ESTIMATE`).
- Net additions to property and equipment, from the segment note, with its definition, if the company
  prints them. Many companies do not; then record `NOT DISCLOSED` and reconcile the measures the filing
  does print (gross purchases, a net measure, the change in PP&E).

**STOP:** the student checks three lines of their choice against the filing.

## Step 2: Reported-to-normalized bridges

1. **Candidates:** list every `ACTUAL` effect for the bridge year from the binder, with its measure and
   basis. Do not include `ESTIMATE` lines. If there are none, say so: the bridge shows reported equal
   to normalized, and the credibility matrix records that the filing reports no estimate change for
   the year.
2. **STOP:** the student chooses which candidates to normalize and writes why in a `STUDENT` cell.
3. **Operating income bridge:** reported operating income (from the income statement, cited) → each
   chosen adjustment with its sign stated in the label ("remove the benefit of...", "add back the
   charge for...") → normalized operating income, all formulas.
4. **Net income bridge:** the same, with after-tax amounts (Rule 2). If an after-tax amount is
   `DERIVED`, show the formula and the rate.
5. Show each adjustment as a percentage of the reported figure, as a formula.

## Step 3: Capex reconciliation

1. Put each printed measure in `Inputs` with its definition and source.
2. Compute the difference between the two measures the assignment names, as a formula from the printed
   totals.
3. List the reconciling items **the filing itself names** (for example proceeds and incentives netted
   in one measure, assets added under finance or build-to-suit leases, assets acquired but not yet paid
   for), with their printed amounts where the filing gives them. Show the part of the difference that
   the printed items explain and the remainder, labelled `NOT DISCLOSED`. If the filing does not say
   whether an item applies to one of the measures, show the remainder with and without it.
4. Rank the reasons by amount only where amounts are printed; otherwise say which are unquantified.

## Step 4: Credibility evidence matrix

For each rationale management gives for its estimate changes, build:

`Rationale (quoted, with line) | Lines consistent with it | Lines in tension with it | What is not disclosed | Fact or inference`

Each cell cites binder lines. Label every statement `FACT` (the filing says it) or `INFERENCE` (a
conclusion from lines, named). Look for both directions: changes that lengthen lives and changes that
shorten them, in the same period or close together; amounts that move earnings up and down. **STOP:**
the verdict and the paragraph are the student's.

## Step 5: Reinvestment diagnostics

Compute as formulas, each with its definition and measures named (Rule 4), for every year the inputs
allow:

| Diagnostic | Definition |
|---|---|
| Refresh intensity | Capex ÷ depreciation of PP&E (state which capex) |
| Net investment | Capex − depreciation of PP&E |
| Capex converted into net PP&E growth | Change in net PP&E ÷ capex (note that net additions can include non-cash items) |
| Depreciation intensity | Depreciation of PP&E ÷ average net PP&E |
| Implied average useful life | Average gross PP&E ÷ depreciation of PP&E |
| Age proxy | Accumulated depreciation ÷ gross PP&E |
| Capex intensity | Capex ÷ revenue |

Give each a one-line reading of what the number measures, in the weakest wording that fits. Whether the
pattern is one-off or structural is the student's call (Rule 3); show the years side by side so the
trend is visible.

## Step 6: Audit trail and checks

Fill the audit-trail template the assignment gives (objective, inputs, prompts with excerpt pointers,
outputs used). The verification log and rejected outputs are `STUDENT`.

Add these to `Checks` with the `CB.` prefix and a verdict (S6):

| ID | What it tests |
|---|---|
| B1 | Every binder line has a Source ID and a pointer whose words are found in the filing |
| B2 | Every quantified amount has period, ACTUAL or ESTIMATE, measure and basis |
| B3 | Every estimate change and accelerated-depreciation amount in the searched sentences has a line |
| R1 | Bridges use only ACTUAL amounts for the bridge year |
| R2 | After-tax lines use printed after-tax amounts, or a DERIVED amount with formula and rate |
| R3 | Every bridge and ratio cell is a formula; no number typed inside a formula; averages written out |
| R4 | Every number in the memo matches a workbook cell, with the same rounding |
| C1 | Each capex measure is named and taken from its printed total; neither is built from the other |
| C2 | Reconciling items are the ones the filing names, with printed amounts; the remainder is shown |
| D1 | Each diagnostic names its capex, depreciation and PP&E measures; a useful life uses gross PP&E |
| W1 | Every factual claim in the memo cites a binder line or Source ID |
| W2 | Wording strength matches the evidence: words such as validates, proves, confirms, massive, structural, accelerating need evidence at that strength (several periods for a trend, a printed statement for a cause) |
| W3 | No pasted-output damage (stray markup symbols, or earlier drafts left in the text) |
| AT | The audit trail has each part the assignment asks for; each prompt has an excerpt pointer; the verification log names what was checked and where |

**Hand back:** the workbook (or tables), and a short message: what you built, which STOPs the student
still owes, every FAIL and FLAG, and the open `STUDENT` cells. Do not write the memo.

## Stack mode (final project)

Use this when the workbook is the final project workbook (S10). You own the reinvestment, invested
capital and ROIC rows of `Hist_Drivers`, and one support tab, `CB_Evidence`. The student fills the
Hist tabs; you never type values there.

1. **Hist_Drivers checks:** for every historical year, check that
   - depreciation comes from one source and one definition (the income statement line and the cash
     flow add-back can differ; the row says which);
   - capex is one named measure, the same one the forecast tabs use;
   - net investment = capex − depreciation + change in operating working capital, as the template
     defines it, and FCFF = NOPLAT − net investment;
   - invested capital comes from the Hist_BS operating lines, and its average is written out
     (Rule 5);
   - ROIC = NOPLAT ÷ average invested capital, the reinvestment rate = net investment ÷ NOPLAT, and
     implied growth = ROIC × reinvestment rate;
   - the tax rate in NOPLAT is labelled for what it is (effective or marginal) and comes from where its
     label says.
2. **`CB_Evidence`:** the depreciation exhibit from Step 1 for the latest 10-K and the 10-Qs after it,
   with the Rule 2 tags, plus the implied average useful life and depreciation intensity by year. This
   is the evidence forecast-bridge uses for its depreciation and capex ranges (its F1 and F2 checks).
3. Add your checks to the workbook's `Checks` tab with the `CB.` prefix.

## Review mode

The user gives you a workbook and memo (and the 10-K, if they have it). Do not browse unless asked.
Skip Step 0's STOP. Judge the submission against the assignment's own format (its exhibit names and
citation style); missing Lab-mode tabs are fix guidance, not failures. Give the `Checks` rows as a table
the student can paste into a new `Checks` tab.

1. **Binder:** B1 to B3. Without the 10-K, pointers and completeness are `UNVERIFIED`, but tags (B2)
   and internal consistency still run: a line cited for an amount must contain that amount, and the
   cited line must be about the same item, period and basis.
2. **Bridges:** R1 to R3; check each adjustment's citation names the right line; recompute every
   subtotal.
3. **Reconciliation:** C1, C2. A measure that equals the other measure plus listed items, rather than a
   printed total, is a FAIL of C1.
4. **Diagnostics:** D1; recompute each ratio; check that each reading says what the ratio measures.
5. **Memo:** R4, W1 to W3; claims that go beyond the exhibits (facts the filing does not state) are W1
   failures.
6. **Audit trail (AT):** each part of the template is present; the verification log says what was
   verified and where (cells, lines), not only that something was verified.

Output one table, grouped by step, most serious first within each, the same problem across cells in one
row, at most 25 rows (the rest listed below by check ID):

`# | Where | What is written | Problem | Check | What a fix needs`

Then the `Checks` rows to paste, and what passed. Do not rewrite the memo.

## Final checklist (run before you answer)

- [ ] Every number is exact, with Source ID and a pointer found in the filing.
- [ ] Every amount is tagged: period, ACTUAL or ESTIMATE, measure, basis.
- [ ] Bridges use only the bridge year's ACTUAL amounts; after-tax amounts are printed or DERIVED with a rate.
- [ ] Every capex, depreciation and PP&E measure is named; none is built from another.
- [ ] Every computed cell is a formula; inputs have sources; averages are written out.
- [ ] No verdict, normalization choice or memo text written by you.

## Never

- Use an estimate for a later year as the current year's effect, or a pre-tax amount as an after-tax one.
- Build one capex measure from another and present it as the printed figure.
- Call depreciation ÷ net PP&E a useful life.
- Type a number into a formula, or a computed value into a cell.
- Decide which items are non-recurring, or write the credibility verdict or the memo.
- Add facts the filing does not state.

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

**2026-10-16. v0.2 after three test runs (review of my Lab 3 submission, builds on Amazon FY2024 and
Alphabet FY2025).** Changes: basis tags inferred from the measure (net income and EPS after-tax; cash
and balances N/A); amounts named in other terms are recorded as printed with the classification line
cited; tax-rate choice is the student's, with the supported rates shown; implied life excludes
construction in progress and land; constants allowed in formulas; pointers may join words with "...";
exhibits keep the assignment's names; companies without net additions; empty bridges; remainders with
and without uncertain items; W2 self-contained; audit-trail check AT; Review mode judges the
assignment's own format.

**2026-10-16. v0.1 drafted** from the Lab 3 handout (depreciation estimates, reported versus
normalized bridges, credibility test, capex reconciliation, reinvestment diagnostics, audit trail) and
the final project's Hist_Drivers rows. Not yet tested. Test cases and pass criteria live in
`tests/capex-bridge/README.md`, outside this file.

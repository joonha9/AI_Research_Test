---
name: dcf-valuation
description: Build or review the valuation core of a DCF - market data, WACC with market-value weights, continuing value by the value-driver formula (terminal growth and terminal RONIC), the bridge from enterprise value to equity value per share, and sensitivity tables - and prove they are consistent with each other. Its central check is a claims map showing that every debt and lease claim is treated the same way in invested capital, free cash flow, the WACC weights and the bridge. Use for the final project's Market_Data, WACC, DCF and Sensitivity tabs. It never chooses the inputs (market data, terminal growth, RONIC, lease treatment) or states a verdict.
---

# DCF Valuation

This skill turns a finished forecast into a value per share the student can defend, and checks that
the pieces fit: the discount rate, the continuing value, the bridge and the sensitivity tables must all
describe the same company with the same claims. **The student chooses every input and judgment**; the
skill builds the mechanics, shows the evidence and catches inconsistencies. It works in any AI chat. It
has two modes:

- **Build mode:** the user gives you a workbook whose forecast is done (FCFF, NOPLAT, invested capital
  by year) and the filings. You build or complete the claims map, Market_Data, WACC, DCF and
  Sensitivity, stopping wherever the student has to choose.
- **Review mode:** the user gives you a filled workbook (and the report, if any). You audit it against
  the rules below and list what to fix.

If the user does not say which mode, ask.

## Rule 1: Sources

The stack conventions at the end of this file apply throughout.

- **Bridge items** (cash, investments, debt, leases, minority interest, preferred, other claims) come
  from the latest balance sheet in the Source_Log (kind A), each with its Source ID and location
  (statement line or note table). Record the **current and noncurrent portions separately**, because
  filings often put the current portion of debt and leases inside another line (for example accrued
  expenses).
- **Market data** (share price, risk-free rate, beta, equity risk premium, credit spread or yield) is
  kind D: the student types it, with provider and as-of date, labelled `STUDENT-INPUT`. **You never look
  it up.** A market-data cell with no provider or date is a FAIL.
- **Share count:** the count the filing prints (cover page shares outstanding, or shares outstanding
  plus outstanding stock awards), with its date and Source ID. The same count is used for market
  capitalization and for value per share. Which count to use is a `STUDENT` decision; show the value
  per share under the most precise printed count next to the one chosen, and label a rounded count as
  rounded.
- **An amount the filing prints only in a note** may be typed as a `FACT` input cell with its Source ID
  and location; every other cell references that input. Without the filings, mark bridge items
  `UNVERIFIED` and run the internal checks.
- **Notes in the workbook** that state numbers (a WACC, a growth rate, a ROIC) must match the cells they
  describe. A stale number in a note is a FAIL.

## Rule 2: One claim, one treatment (the claims map)

Every claim on the company's cash flows is either **operating** or **financing**, and it must be treated
that way everywhere. Build a `DV_Claims` tab:

`A Claim | B Current amount | C Noncurrent amount | D Total | E Source ID and location | F Treatment (Financing / Operating) | G In invested capital as | H In FCFF as | I In WACC debt weight? | J In bridge? | K Consistent?`

The consistent patterns are:

| Claim | If financing | If operating |
|---|---|---|
| Borrowings (including the current portion) | Out of operating liabilities; in WACC weight; subtracted in bridge | Not an option |
| Operating leases | Liability out of operating liabilities; right-of-use asset stays in invested capital; new leased assets count as investment; in WACC weight; subtracted in bridge | Lease cost stays in operating expense; liability neither in WACC nor in bridge; right-of-use asset and lease liability both in invested capital or both out |
| Finance leases | As borrowings | Not usually an option; say why if chosen |

- **A claim may not be operating on one tab and financing on another.** If a liability is netted inside
  invested capital (reducing it) and also subtracted in the bridge or weighted in WACC, it is counted
  twice: FAIL.
- **A current portion sitting inside an operating line** (for example accrued expenses) is part of
  operating working capital unless it is moved out. If its noncurrent part is financing, the current
  part must be too: move it, or explain why not. FAIL if it is silently left behind.
- **The FCFF definition must match.** If the depreciation added back in FCFF includes amortization of
  lease assets or other non-PP&E assets, the capex or investment line must include the matching
  additions, or the add-back must be limited to the assets the capex measure covers. Say which.
- **Which treatment to use is a `STUDENT` decision** (US GAAP keeps operating lease cost in operating
  income; many analysts treat leases as debt). You show both patterns and enforce consistency.

## Rule 3: WACC

- **Market-value weights.** Equity = share price × the share count from Rule 1. Debt = the financing
  claims from the claims map, by cell reference to `DV_Claims` (never retyped). Market value of debt if
  the filing gives fair value; otherwise book value, labelled as such.
- **Cost of equity:** CAPM, each input a `STUDENT-INPUT` with provider and date. **Cost of debt:** a
  stated source (yield on the company's bonds, or a rating-based spread over the risk-free rate). The
  tax rate on the debt shield is the marginal rate the forecast uses for NOPLAT, by cell reference.
- Every input in its own cell; WACC is a formula. The capital structure (current or target) is the
  student's choice; say which.

## Rule 4: Continuing value by the value-driver formula

`CV(t) = NOPLAT(t+1) × (1 − g / RONIC) / (WACC − g)`

- **RONIC is the return on new capital**, not the historical ROIC of the whole base. Label the input
  "terminal RONIC". If the workbook calls it ROIC, FLAG the label and ask the student which they mean.
  Its evidence (durability and maturity facts) comes from forecast-bridge or the student; you never set
  it.
- **NOPLAT(t+1) = NOPLAT(t) × (1 + g)** only if the last explicit year has no temporary items (peak
  margins, one-off costs); otherwise FLAG it.
- **Guards:** g < WACC; RONIC > g; if RONIC < WACC, growth destroys value, so say so.
- **Show the jump:** the implied terminal reinvestment rate (g ÷ RONIC) next to the last explicit
  year's reinvestment rate, and FCFF(t+1) from the formula next to FCFF(t) × (1 + g). A relative change
  of more than a third in either, measured against the last explicit year, is a FLAG: the student must
  explain why reinvestment falls (or rises) at maturity.
- **Report the continuing value's share of enterprise value.**

## Rule 5: Discounting and timing

- State the convention: end-of-year, mid-year, or a stub from the valuation date. Use one convention
  for every explicit cash flow. The continuing value is a value at the **end** of the last explicit
  year, so it is discounted with that year's end-of-year factor under every convention (with any stub
  applied to it too). The convention is a `STUDENT` decision.
- If the valuation date falls inside the first forecast year, FLAG it and show the effect of the
  convention the student chose in a `CHECK` cell; the choice is theirs.

## Rule 6: The bridge

`Equity value = EV + non-operating assets − every financing claim in DV_Claims`

- **Non-operating assets:** cash and securities (how much cash is excess versus needed for operations is
  a `STUDENT` decision; show the amounts), and non-operating investments with their source and basis
  (carrying or fair value).
- **Claims:** every financing row of `DV_Claims`, current and noncurrent, by cell reference.
- **Value per share** = equity value ÷ the Rule 1 share count. Show it next to the current price, with
  both directions of the gap labelled by their base.

## Rule 7: Sensitivity recomputes everything

- **Every cell recomputes the whole enterprise value** at its WACC, g or RONIC: the present value of the
  explicit cash flows **and** the continuing value. A table that varies WACC only in the continuing
  value, while reusing the explicit-period value from the base WACC, understates the sensitivity.
- **The base case is on the grid** and its cell equals the DCF value per share.
- Cells where g ≥ WACC show `N/A`.
- At least WACC × g and WACC × RONIC; scenarios only with inputs the student sets.

## Rule 8: The student decides; the template's formulas stay

- `STUDENT` decisions: every market-data input and its provider, the capital structure, the lease
  treatment, excess cash, terminal g and RONIC, scenario inputs, and the verdict. You never fill them,
  even if asked; you may show the evidence and the effect of each choice in `CHECK` cells.
- Never retype or override a template formula (S9). If a template formula breaks a rule here (for
  example a sensitivity table that reuses the base-WACC explicit value, or blanks where `N/A` belongs),
  FLAG it, show the corrected numbers in a separate `CHECK` table, and ask the student to disclose or
  fix it. A value the student typed into a tab this skill owns may be replaced by a reference, and the
  change is reported.
- Pure constants are allowed in formulas (the 1 of `1+g`, unit conversions); the thresholds in this
  file are for your checks, not for the workbook.

## Step 0: Set up (ask, do not assume)

1. Company, valuation date, workbook (final project or other), and the latest 10-K or 10-Q in the
   Source_Log.
2. Is the forecast done? Read FCFF, NOPLAT, invested capital, ROIC and the reinvestment rate by year.
   If FCFF or NOPLAT is missing, stop and point to forecast-bridge. If only invested capital or ROIC is
   missing, continue and mark the checks that need them `NOT RUN`.
3. Has the student typed market data? If not, list what is needed (Rule 1) and wait.

**STOP** (Build mode): confirm the setup.

## Step 1: Claims map

Fill `DV_Claims` from the balance sheet and its notes: borrowings (current and noncurrent), finance
leases, operating leases (each current and noncurrent), preferred stock, minority interest, and any
other claim the notes name (for example pension deficits). For each, show where the workbook currently
treats it in invested capital, FCFF, WACC and the bridge (columns G to J), and mark column K.

**STOP:** the student chooses the lease treatment and confirms each row's treatment.

## Step 2: Market data and WACC

Check every market-data cell for provider and date. Build the WACC from cells (Rule 3), with debt by
reference to `DV_Claims`. **STOP:** the student confirms the capital structure (current or target) and
the debt basis (fair or book value).

## Step 3: Continuing value and DCF

**STOP:** the student confirms terminal g and RONIC (from forecast-bridge's ranges) and the discounting
convention. Then build the value-driver continuing value (Rule 4), the discounting (Rule 5),
enterprise value, and the CV share of EV.

## Step 4: Bridge

Build the bridge (Rule 6). **STOP:** the student decides excess cash and the basis for investments.

## Step 5: Sensitivity

Check or build the tables (Rule 7). If the template's table breaks Rule 7, leave it, and add a
`CHECK` table beside it that recomputes the full EV, with the difference at the base row.

## Step 6: Checks and hand back

Add these to `Checks` with the `DV.` prefix (S6):

| ID | What it tests |
|---|---|
| V1 | Every bridge item has a Source ID and location from the latest balance sheet; current and noncurrent portions recorded |
| V2 | Every market-data input has provider and as-of date (and, in Build mode, none was supplied by you) |
| V3 | The claims map is consistent: no claim operating on one tab and financing on another; nothing counted twice |
| V4 | Current portions of financing claims are moved with their noncurrent parts, or the exception is explained |
| V5 | The FCFF depreciation add-back and the investment line cover the same assets |
| V6 | WACC: market-value weights, debt by reference to the claims map, marginal tax rate shared with NOPLAT, all from cells |
| V7 | No link to another workbook; no number typed into a formula |
| V8 | Continuing value uses the value-driver formula with a labelled terminal RONIC; g < WACC; RONIC > g |
| V9 | Terminal reinvestment and FCFF jump against the last explicit year are shown; a jump over a third is explained |
| V10 | CV share of EV reported |
| V11 | One discounting convention, stated; continuing value discounted with the last year's factor |
| V12 | Bridge subtracts every financing claim and only those; one share count for market cap and value per share |
| V13 | Sensitivity recomputes the full EV in every cell; the base case is on the grid and ties to the DCF value |
| V14 | Numbers stated in notes match the cells they describe (notes on other skills' tabs are reported for their owners to fix) |

**Hand back:** the tabs (or tables to paste), the claims map, every FAIL and FLAG with its effect on value
per share where it can be computed (in `CHECK` cells), and the open `STUDENT` decisions. No verdict.

## Stack mode (final project)

You own `Market_Data`, `WACC`, `DCF`, `Sensitivity` and the support tab `DV_Claims` (S10). You read
`Hist_BS` (invested capital), `Hist_IS` and `Hist_CF` (the depreciation and capex measures),
`Forecast_Assumptions` and `Forecast_Model`, and forecast-bridge's ranges for terminal g and RONIC. You
never change those tabs: an inconsistency there (for example a lease liability netted in invested
capital) is reported with the tab and cell, for the student and the owning skill to fix.

## Review mode

The user gives you a filled workbook (and the report, if any). Skip Step 0's STOP. Do not browse unless
asked. If you have the filings, check the bridge items against them; if not, mark them `UNVERIFIED` but
run every internal check.

1. **Claims map first:** build `DV_Claims` from what the workbook does, and test V3 to V5. This is where
   the largest errors usually are.
2. **Sources:** V1, V2, V14.
3. **WACC:** V6, V7.
4. **Continuing value:** V8 to V11; recompute CV and EV yourself.
5. **Bridge:** V12; recompute equity value and value per share.
6. **Sensitivity:** V13; recompute two cells yourself, including the base.

For every finding that changes value, give the effect on value per share in a `CHECK` figure (one
change at a time). Where the fix depends on a student decision (for example the lease treatment), give
the effect under each pattern, and say which parts cannot be computed from the workbook. Output one
table, most serious first (claims and double counting, then sources, then WACC, then continuing value,
then the bridge, then sensitivity, then labels and notes), the same problem across cells in one row,
at most 25 rows. The Check column holds the check ID and its verdict:

`# | Tab!Cell | What is there | Problem | Check | Effect on value per share | What a fix needs`

Then the `Checks` rows to paste, and what passed. Do not write the report or a verdict.

## Final checklist (run before you answer)

- [ ] Every claim has one treatment across invested capital, FCFF, WACC and the bridge.
- [ ] Current portions are where their noncurrent parts are, or the exception is explained.
- [ ] Market data is the student's, with provider and date.
- [ ] Continuing value uses terminal RONIC (labelled), with the reinvestment jump shown.
- [ ] One discounting convention; CV share of EV shown.
- [ ] Sensitivity recomputes full EV; base case on the grid and tied.
- [ ] No input or verdict chosen by you; no template formula changed.

## Never

- Look up a share price, beta, risk-free rate, premium or yield.
- Count a claim both inside invested capital and in the bridge or WACC.
- Call historical ROIC "RONIC" without saying so, or set the terminal inputs yourself.
- Reuse the base-WACC value of the explicit period in a sensitivity cell for another WACC.
- Retype a number that lives in another cell, or link to another workbook.
- Say the stock is under- or overvalued.

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

**2026-10-22. v0.2 after four test runs (review of my final workbook; a build on a synthetic company;
a market-data trap).** Changes: continuing value always discounted at the last year's end-of-year
factor; share count choice is the student's, with the precise count shown; note-only amounts as
sourced inputs; effects shown under each lease pattern; STOPs for capital structure, debt basis,
terminal inputs and discounting; partial forecasts allowed with checks NOT RUN; owned-tab typed values
may become references; jump threshold defined; Review output order includes WACC and the bridge.

**2026-10-22. v0.1 drafted** from the Topic 11 slides (value-driver continuing value; ROIC versus
RONIC; terminal growth, margin and reinvestment), the final project handout (Q5: market-value WACC,
continuing value with mature growth and mature ROIC, the EV-to-equity bridge, and the rule that debt
and lease treatment must match in WACC and the bridge; Q6: WACC × g and WACC × terminal ROIC tables),
and the final project template. Not yet tested. Test cases and pass criteria live in
`tests/dcf-valuation/README.md`, outside this file.

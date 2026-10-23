---
name: comps-pack
description: Build or review a trading-comps workbook (target vs peers, EV/EBITDA and other multiples, implied share price) using numbers taken only from the companies' 10-Ks, each with its Source ID. Use for comparable-company valuation (Lab 4 style) and for the final project's Multiples cross-check. It never writes the memo, picks the multiple, or gives a verdict; those are the student's decisions. If a number is not in the 10-K, it says NOT FOUND instead of filling it in.
---

# Comps Pack

This skill turns the 10-Ks of a target and its peers into a trading-comps **workbook** the student can
defend cell by cell. The workbook shows the evidence and the mechanics. **The student makes every
judgment and writes the memo.** It works in any AI chat. It has two modes:

- **Build mode:** the user gives you the 10-Ks. You fill the Inputs tab with sources, build the
  workbook as live formulas, run the checks, and leave the decision cells blank for the student.
- **Review mode:** the user gives you a workbook they built, and optionally the numbers from their
  memo. You audit the mechanics against the rules below and list what to fix. You do not grade their
  judgments.

If the user does not say which mode, ask.

## Rule 1: The 10-Ks in the Source_Log are the only source (one exception)

The stack conventions at the end of this file apply throughout. This rule is narrower than them.

- **Take every financial number from the 10-Ks and nowhere else.** Use the documents the user gives you
  (uploaded, pasted, or a link you can actually open). Each 10-K is a row of the Source_Log: the
  target's is kind `A`, each peer's kind `E`. Start the Source_Log in Step 0 if there is none. Even in
  stack mode, where the Source_Log also lists 10-Qs and releases, financial numbers for comps come from
  10-Ks so every company is on the same basis. Never use your memory or training data, a web
  search, a data site (FactSet, Yahoo Finance, Macrotrends, and so on), an earnings release, a call
  transcript, or a news article, even if you think you know the number. A "core earnings" table or any
  figure that does not appear in the 10-K is not a 10-K number.
- **The one exception: share price and market capitalization.** They are not in a 10-K. The **student
  types them in**, with the source (for example "FactSet") and the **as-of date**. You never look them
  up. Label them `STUDENT-INPUT`. Each provider and as-of date is a kind `D` row of the Source_Log. If
  the student has not typed them, leave the cells blank and mark `NOT PROVIDED`.
- **Every number gets a source:** the Source ID, which company's 10-K (fiscal year), the Item and statement or note,
  the line label exactly as printed, and the page if visible. A number without a source does not go
  in Inputs.
- **Copy numbers exactly as printed.** Do not round, rescale, or change signs in Inputs. Record units
  and currency once per company, at the top.
- **Labels:** every Inputs row carries one of `FACT` (copied from the 10-K), `STUDENT-INPUT`,
  `DERIVED` (computed from other rows, formula shown), `ASSUMPTION`, or `OPEN`.
- **Be honest about gaps. Use exactly one of these when a value is missing:**
  - `NOT FOUND`: you looked and the line is not in the document you have. Say where you looked.
  - `N/A`: the company does not have this item (for example, no preferred stock).
  - `NOT PROVIDED`: the document or section that holds it was not given to you. Ask for it.
  - `—` (dash): not needed.
  If you cannot open a document at all, say so and stop for that company. Never fill in from memory.
- **Do not derive a missing line from other lines** unless the user agrees. If they do, label it
  `DERIVED` and show the formula.
- **You are not the calculator.** Every computed cell is an Excel formula that references other cells.
  If you show a value to sanity-check a formula, label it `CHECK`. Never type a number into a formula.

## Rule 2: The student decides

These are decisions, not computations. **Never make one for the student, never pre-fill one, and
never let a downstream cell run on a default.** Leave the cell blank and show the evidence next to it.
Until the student fills a decision cell, every cell that depends on it shows
`WAITING FOR STUDENT DECISION` (for example `=IF(Student_Decisions!C5="","WAITING FOR STUDENT DECISION", ...)`).

1. Which multiple is primary, and which (if any) is a cross-check.
2. Which normalization items to accept or reject, one by one.
3. Which peer statistic (minimum, 25th percentile, median, average, 75th percentile, maximum) is the
   target multiple.
4. How leases are treated in enterprise value.
5. What to do about peers whose fiscal year ends on different dates.
6. The single biggest uncertainty behind the range.
7. What must be true for the implied range to be reasonable.

You may ask the student questions that help them decide ("which line in the 10-K would show that?").
You may point to evidence in the workbook. You do not say which answer is right.

## Step 0: Get the documents (ask, do not assume)

1. Target company and ticker, and the peer list (the lab fixes it; if the user did not give it, ask).
2. **The 10-K of the target and of every peer**, at least Item 7 (MD&A) and Item 8 (statements and
   notes). Paste or upload. If one is missing, continue with the others and mark that company's cells
   `NOT PROVIDED`; its column stays blocked.
3. **Share price, fully diluted market cap, source, and as-of date for each company**, typed by the
   student. Ask whether the market cap is fully diluted.
4. Units and currency. All companies go to one unit (for example USD millions). If a 10-K uses another
   unit, say so and ask before converting.
5. If the user already has a workbook, ask them to paste it with tab names, row numbers and column
   letters so your formulas point at real cells. Otherwise you create it in Step 1.
6. Optional: the student's business-model notes (earlier labs). Use them only to interpret, never as data.
7. Start the Source_Log: one row per 10-K (target kind `A`, peers kind `E`) and one kind `D` row per
   market data provider and date. If the user's workbook already has a Source_Log with the final
   project tabs, you are in stack mode: use its Source IDs and read "Stack mode (final project)".

## Step 1: Fill the Inputs tab from the 10-Ks

Layout: `Company | Line item | Value | Unit | Label | Source (Source ID, 10-K FY, Item, statement or note, line as printed, page) | As-of date`.

Pull these for each company. Use the printed label in the source column. For the decision-tree evidence
you also need the prior year's value, which the same 10-K prints as the comparative column.

- Fiscal year end date and units.
- Income statement: revenue (t and t-1), operating income, net income.
- Cash flow statement: depreciation and amortization, cash from operations, capital expenditures,
  stock-based compensation.
- Balance sheet (latest balance sheet date): cash and equivalents, short-term investments and marketable
  securities, long-term marketable securities, short-term debt and current portion of long-term debt,
  long-term debt, finance lease liabilities, operating lease liabilities (current plus noncurrent),
  preferred stock, noncontrolling interest, equity-method and other non-marketable investments,
  accounts receivable (t and t-1).
- Cover page: shares outstanding and its date (used only for check C11).
- Market data, typed by the student: share price, fully diluted market cap, source, as-of date.

Lease and investment lines often sit in notes, not on the face of the balance sheet. If they are not in
the text given to you, mark `NOT PROVIDED` and ask for the note. **A zero is a claim.** Write `0` only if
the 10-K shows zero; if the item is absent, write `N/A` with where you looked. Never use `0` for
"I did not find it". An amount the student excludes by a decision (for example operating leases when
D4 is No) keeps its value in Inputs and shows `excluded per D4` in the bridge row, not `0`.

After filling Inputs, list three values for the student to check against the 10-K themselves (from
different companies and statements).

## Step 2: Articulation checks (stop on any failure)

Report each as PASS or FAIL with the numbers compared. If a check needs something not provided, report
`NOT RUN` and name what is needed.

- **C1 Sources.** Every Inputs number has a source and a label, and its Source ID is in the
  Source_Log. Market data has an as-of date. No source points to a chat turn, a data site or an
  earnings release.
- **C2 Units and signs.** One unit and currency across all companies. Balance sheet assets and
  liabilities are entered as printed (positive). **A balance sheet asset entered as a negative number
  is a FAIL:** ask the student to confirm against the 10-K.
- **C3 Bridge footing.** For every company, recompute enterprise value from its own bridge lines and
  compare it with the EV shown. The two must match to the unit. If they differ, show both and the gap.

Do not build multiples on a FAIL of C1, C2 or C3 until the student fixes it or explicitly accepts it.

## Step 3: Normalization ledger

One row per candidate adjustment, for the target and every peer:

`Company | Item | Amount (as printed) | Pre-tax or after-tax (as printed) | Verbatim quote (2 to 4 sentences) | Location (Item, note, page) | Appears in other years shown? | Applied to every company? | Student: include? (Y/N) | Student: reason`

- Candidates come only from MD&A and the notes (restructuring, impairment, litigation or settlements,
  acquisition-related costs, gains or losses on asset sales). Quote verbatim. No paraphrase.
- **Do not judge whether an item is non-recurring.** Show whether it appears in the other years the 10-K
  prints, and leave the decision to the student.
- Normalized EBITDA adds back only rows where the student typed `Y`. If any include cell is blank,
  normalized EBITDA shows `WAITING FOR STUDENT DECISION`.
- If a category is absent for a company, write "Not found in the provided text". Do not infer.

### Measurement rules for EBITDA (check every formula against all of them)

- **E1 Same definition for everyone.** EBITDA = operating income + depreciation and amortization from the
  cash flow statement, for every company. State whether D&A includes amortization of content, software or
  acquired intangibles, and whether impairments are inside that line. Stock-based compensation is either
  added back for every company or for none; say which.
- **E2 Same basis as the adjustment.** An after-tax amount is never added to a pre-tax EBITDA. If the 10-K
  prints an item after tax, show that, flag it, and ask the student how to treat it; do not gross it up
  yourself.
- **E3 No double counting.** An impairment or amortization already inside the D&A line is not added back
  again as an adjustment.
- **E4 Same screen for everyone.** If an item type is added back for one company, the student must say
  why the same type is not added back for the others, or add it for all.
- **E5 Flows are not averaged.** EBITDA for year t is year t only.
- **E6 Timing.** EBITDA is for the fiscal year in the 10-K. The market cap is as of a later date. LTM
  adjustment is out of scope for this skill: do not build it and do not estimate it. Show the fiscal year
  end and the market data date for every company, list the mismatch, and let the student decide (D5).

## Step 4: Enterprise value bridge

Table per company. Every row is a formula referencing Inputs. Show each amount as a positive magnitude
and apply the sign in the formula. **The row label says the operation:**

`(+) Fully diluted market cap | (+) Short-term debt | (+) Long-term debt | (+) Finance leases | (+) Operating leases [per D4] | (+) Preferred | (+) Noncontrolling interest | (−) Cash and equivalents | (−) Short-term investments | (−) Long-term marketable securities | (−) Equity-method investments [if the student chooses] | = Enterprise value`

- **Leases:** the student chooses in D4 whether operating lease liabilities are in enterprise value. Under
  U.S. GAAP, operating lease cost sits inside operating income and EBITDA, so adding operating lease
  liabilities to EV without adjusting EBITDA is inconsistent. Show that fact next to the decision cell and
  do not choose. The choice must be the same for every company and the same in the return bridge (Step 6).
- **Investments that are not cash.** Which ones to subtract is a judgment; list what the 10-K reports and
  let the student decide row by row, then apply the same rule to every company.
- **Market cap vs balance sheet date.** Show both dates next to each company.

## Step 5: Multiples and peer statistics

Per company: EV/EBITDA (GAAP and normalized), EV/EBIT, EV/revenue, and price-to-earnings (market cap /
net income). Compute all so the student can see them; the student decides which one matters (D1).

Peer statistics for each multiple: minimum, 25th percentile, median, average, 75th percentile, maximum.

- **The target is never in its own peer statistics.** Show n (the number of peers) next to every statistic.
- Use the unrounded multiples. Name the percentile function you used (`PERCENTILE.INC` by default). With
  only a few peers, percentiles are interpolated; say so on the sheet.
- Show the fiscal year end and market data date for each company beside the multiples (E6).

### Decision-tree evidence (Student_Decisions tab, next to D1)

Give the evidence for each question, with a cell reference. Do not answer the questions.

1. **Is operating profit positive and reasonably stable?** Operating income and operating margin, every
   company, years t and t-1.
2. **Where does reinvestment live?** Capital expenditures, D&A, capex / D&A, capex / cash from operations;
   lease liabilities as a share of debt.
3. **Are revenue quality or cash conversion concerns material?** Cash from operations / net income,
   cash from operations / EBITDA, receivables growth vs revenue growth.

## Step 6: Implied value

Runs only on the student's decisions (D1 multiple, D2 adjustments, D3 statistic, D4 leases). If any is
blank, show `WAITING FOR STUDENT DECISION`.

1. Implied enterprise value = target multiple (the chosen statistic) × target's matching metric.
2. **Return bridge:** implied equity value = implied enterprise value with **the same bridge lines as
   Step 4, opposite signs, same lease choice**. For a price-based multiple such as P/E, there is no
   bridge: the multiple gives equity value directly.
3. Implied share price = implied equity value / the **same share count that is inside the market cap**
   (market cap / share price, labeled `DERIVED`).
4. **Sensitivity table:** all six statistics with their multiple, implied enterprise value, implied equity
   value and implied share price, all formulas.
5. **Market price vs implied price, both directions, each with its base stated:**
   `current price / implied price − 1` and `implied price / current price − 1`. A single unlabeled
   "premium" is not allowed, because the two numbers differ.

## Step 7: Checks on the mechanics

Report each as PASS or FAIL with the numbers compared (live formulas in the Checks tab):

- **C4 Sign and direction.** Each bridge row's sign in the formula matches its label, and matches the
  return bridge in reverse.
- **C5 Lease consistency.** The lease choice in D4 is applied to every company and in the return bridge.
- **C6 Normalization basis.** No after-tax item added to pre-tax EBITDA; each adjustment has a verbatim
  quote and a location; the same screen was applied to every company; no double count with D&A.
- **C7 EBITDA definition.** Same for every company (E1).
- **C8 Peer statistics.** Target excluded; n shown; computed from unrounded multiples; function named.
- **C9 Round trip.** Applying the target's own EV/EBITDA to its own EBITDA and running the return bridge
  returns its market cap exactly. If not, a bridge line is inconsistent.
- **C10 Sensitivity.** Every sensitivity row recomputes from the stated multiple.
- **C11 Share count.** Market cap / price vs the cover page shares outstanding: flag a gap above 2% and ask
  the student to confirm the share basis.
- **C12 Premium base.** Both directions computed, each labeled with its base.
- **C13 Timing.** Fiscal year end and market date shown for every company; the mismatch is listed and the
  student's D5 answer is recorded.

## Student_Decisions tab

Columns: `# | Decision | Evidence (cell references) | Student answer | Student reason`. The last two are
blank when you hand it back, with a visible fill (for example light yellow) so the student sees what is theirs.

| # | Decision | Answer format |
|---|---|---|
| D1 | Primary multiple, and cross-check if any | dropdown |
| D2 | Normalization include flags | Y/N per row in the Normalization tab |
| D3 | Target statistic | dropdown of six |
| D4 | Operating leases in EV? | Yes / No, plus reason |
| D5 | Fiscal-year mismatch handling | free text |
| D6 | Biggest uncertainty | free text |
| D7 | What must be true for this range | free text |

## Hand back

1. **The workbook**, with these tabs: `Inputs`, `Normalization`, `EV_Bridge`, `Multiples`, `Implied_Price`,
   `Checks`, `Student_Decisions`. All computations are live formulas. Student-entered cells (market data,
   decisions) are visibly filled.
2. **If you can create files,** build a real `.xlsx`, recalculate it, and confirm there are no formula
   errors before you hand it over. Do not type computed numbers into cells.
3. **If you cannot create files,** give each tab as a table with the exact cell addresses and the formulas
   as text, so the student can paste them into their own workbook.
4. **A short message:** what is filled, what is `NOT PROVIDED` or `NOT FOUND`, which checks failed, and
   which decisions are waiting for the student. Nothing more.

You do not write the executive summary, the thesis, or any memo text. If the user asks for one, say that
writing it is the assignment, point to the `Student_Decisions` cells and the `Checks` tab, and offer to
ask questions that help them write it.

## Review mode

When the user pastes or uploads a workbook (and optionally the numbers from their memo), do this in order.
If there is only the memo, treat its tables as the workbook: put the memo location in place of the cell,
recompute every figure as a `CHECK`, and mark checks that need the 10-Ks `NOT RUN`. In Review mode the
multiples already exist, so after a FAIL of C1, C2 or C3 continue the review and label the later
findings provisional.

1. Step 0 briefly (companies, units, market data dates). If the user gives the 10-Ks, check their Inputs
   against them; otherwise list unsourced or missing inputs.
2. Run C1 to C3 on their data.
3. Check every formula and the normalization ledger against E1 to E6, the bridge rules, and C4 to C13,
   including ratios or adjustments the user added that are not in the standard set. Output:

   `Item | Where | Rule broken | What it should be | Effect (direction and rough size)`

   If the correct value depends on a missing input, give a provisional `CHECK` and say what it depends on.
4. List every number typed into a formula. The same line item must have one value everywhere; flag any
   number used for two lines, or two numbers used for one line.
5. **Memo tie-out (only if the user gives memo numbers).** For each number in the memo, find the cell it
   should come from. Output `Memo statement | Memo number | Workbook cell | Workbook value | Match?`.
   Flag a number that appears twice in the memo with different values. Flag a percentage that has no stated
   base. Check numbers only; do not comment on whether the conclusion is right.
6. Flag anything in the memo that cites a source other than a 10-K page (for example a chat turn or a
   data site), because the 10-K is the source rule for financial numbers.
7. End with what passed, so the student sees what is already right.

Skip the judgment tab in review mode. Never say which multiple, statistic or adjustment is correct.

## Stack mode (final project)

Use this when the user's workbook already has a Source_Log and the final project tabs. In the final
project, trading multiples are **a cross-check on the DCF**, not the valuation. Use the peers the
assignment specifies; if it names none, ask.

- **Tabs.** You own `Multiples` (stack convention S10); create it at the end of the workbook if the
  template has none. Put the supporting tabs in the same workbook with a `CP_` prefix so they never
  collide with the template's tabs: `CP_Inputs`, `CP_Normalization`, `CP_EV_Bridge`,
  `CP_Decisions`. `Multiples` holds what Step 5 and Step 6 produce.
- **Target inputs.** Read the target's share price, share count and bridge items from `Market_Data`
  by cell reference; never retype them. Peers' market data is `STUDENT-INPUT` in `CP_Inputs`, each
  with a kind `D` Source_Log row.
- **Leases.** D4 must match the lease treatment in `WACC` and the `DCF` bridge. If it does not, C5 is
  a FAIL; show both cells and let the student decide which to change.
- **DCF next to the range.** If the `DCF` tab has a value per share, show it beside the implied range
  by cell reference, with no verdict on which is right.
- Add C1 to C13 to the workbook's `Checks` tab as `CP.C1` to `CP.C13`.

## Final checklist (run before you answer)

- [ ] Every financial number came from a 10-K in the Source_Log and has a source with its Source ID.
      Only the price and market cap are student-typed.
- [ ] Every gap is labeled `NOT FOUND`, `N/A`, or `NOT PROVIDED`. No blank cells, no guesses, no `0` for "not found".
- [ ] Every computed cell is a formula referencing cells. No typed numbers.
- [ ] Every decision cell is blank, and every dependent cell says `WAITING FOR STUDENT DECISION`.
- [ ] Bridge rows foot to the EV shown; signs match labels; the return bridge uses the same lines.
- [ ] Every normalization row has a verbatim quote, location, basis, and a Y/N left for the student.
- [ ] Same EBITDA definition and same screen for every company.
- [ ] Target excluded from peer statistics; n shown; unrounded inputs.
- [ ] Both directions of price vs implied price computed, each with its base.
- [ ] Fiscal year ends and market dates shown; no LTM built or estimated.
- [ ] No memo text, verdict, or recommended answer anywhere.

## Never

- Take a financial number from anywhere but the 10-Ks in the Source_Log: not memory, not the web, not
  a data site.
- Look up or fill in a share price or market cap. The student types them.
- Choose the multiple, the statistic, the adjustments, the lease treatment, or the fiscal-year handling.
- Write the executive summary, the thesis, or say "overvalued", "undervalued" or "fairly valued".
- Add an after-tax amount to a pre-tax EBITDA, or add back an item already inside D&A.
- Put the target inside its own peer statistics.
- Build or estimate an LTM figure.
- Present a single unlabeled "premium" or "discount".
- Continue past a failed C1, C2 or C3 without the student's say-so.

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

**2026-10-16. Joined the skill stack.** Rule 1 now names the 10-Ks in the Source_Log (target kind A,
peers kind E, market data kind D); sources carry Source IDs; a "Stack mode" section writes the
Multiples cross-check into the final workbook and checks lease consistency with the DCF; the shared
stack conventions were added.

**2026-10-23. First test** (blind review of my Lab 4 memo, memo only; caught 12 of 13 known
problems, results in `tests/comps-pack/README.md`). Changes: memo-only reviews; review continues after
a C1 to C3 FAIL with later findings provisional; zero versus N/A versus `excluded per D4`. Note: the
Lab 4 handout allowed an agent that draws on transcripts and Yahoo Finance; this skill is stricter on
purpose (10-Ks only for financial numbers).

Earlier plan: (1) review mode on the Lab 4 Apple comps memo, run cold by a separate AI
session given only this file, the workbook and the memo numbers; (2) build mode on a new target and peer
set. After each run, record what it caught, what it missed, and what was changed in this file.

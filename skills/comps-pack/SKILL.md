---
name: comps-pack
description: Build or review a trading-comps workbook (target vs peers, EV/EBITDA and other multiples, implied share price) using numbers taken only from the companies' 10-Ks, each with its source. Use for comparable-company valuation (Lab 4 style). It never writes the memo, picks the multiple, or gives a verdict; those are the student's decisions. If a number is not in the 10-K, it says NOT FOUND instead of filling it in.
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

## Rule 1: The 10-K is the only source (one exception)

- **Take every financial number from the 10-Ks and nowhere else.** Use the documents the user gives you
  (uploaded, pasted, or a link you can actually open). Never use your memory or training data, a web
  search, a data site (FactSet, Yahoo Finance, Macrotrends, and so on), an earnings release, a call
  transcript, or a news article, even if you think you know the number. A "core earnings" table or any
  figure that does not appear in the 10-K is not a 10-K number.
- **The one exception: share price and market capitalization.** They are not in a 10-K. The **student
  types them in**, with the source (for example "FactSet") and the **as-of date**. You never look them
  up. Label them `STUDENT-INPUT`. If the student has not typed them, leave the cells blank and mark
  `NOT PROVIDED`.
- **Every number gets a source:** which company's 10-K (fiscal year), the Item and statement or note,
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

## Step 1: Fill the Inputs tab from the 10-Ks

Layout: `Company | Line item | Value | Unit | Label | Source (10-K FY, Item, statement or note, line as printed, page) | As-of date`.

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
the 10-K shows zero or the item is absent, and then write `N/A` with where you looked. Never use `0` for
"I did not find it".

After filling Inputs, list three values for the student to check against the 10-K themselves (from
different companies and statements).

## Step 2: Articulation checks (stop on any failure)

Report each as PASS or FAIL with the numbers compared. If a check needs something not provided, report
`NOT RUN` and name what is needed.

- **C1 Sources.** Every Inputs number has a source and a label. Market data has an as-of date. No
  source points to a chat turn, a data site or an earnings release.
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

When the user pastes or uploads a workbook (and optionally the numbers from their memo), do this in order:

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

## Final checklist (run before you answer)

- [ ] Every financial number came from a 10-K and has a source. Only the price and market cap are student-typed.
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

- Take a financial number from anywhere but the 10-Ks: not memory, not the web, not a data site.
- Look up or fill in a share price or market cap. The student types them.
- Choose the multiple, the statistic, the adjustments, the lease treatment, or the fiscal-year handling.
- Write the executive summary, the thesis, or say "overvalued", "undervalued" or "fairly valued".
- Add an after-tax amount to a pre-tax EBITDA, or add back an item already inside D&A.
- Put the target inside its own peer statistics.
- Build or estimate an LTM figure.
- Present a single unlabeled "premium" or "discount".
- Continue past a failed C1, C2 or C3 without the student's say-so.

## Test log

*For human readers: the history of this file. Not instructions; ignore this section when running the
skill.*

**No runs yet.** Planned: (1) review mode on the Lab 4 Apple comps memo, run cold by a separate AI
session given only this file, the workbook and the memo numbers; (2) build mode on a new target and peer
set. After each run, record what it caught, what it missed, and what was changed in this file.

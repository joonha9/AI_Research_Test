---
name: ratio-dashboard
description: Build or review a two-year ratio dashboard and DuPont analysis from 10-K line items the user supplies. Use for financial statement analysis (Lab 2 style). Never supplies, estimates, or invents a number.
---

# Ratio Dashboard + DuPont

This skill turns a company's financial statements into a two-year ratio dashboard and a DuPont
analysis the user can defend line by line. It works in any AI chat. It has two modes:

- **Build mode:** the user gives you their raw line items (Tab A). You give back the dashboard and DuPont
  as spreadsheet formulas, then help interpret them.
- **Review mode:** the user gives you a dashboard they already built. You audit every ratio against
  the rules below and list what to fix.

If the user does not say which mode, ask.

## Rule 1: You are not a data source, and you are not the calculator

- Every number must come from the user's own Tab A, taken from the 10-K, with a source reference.
  Never fill a missing line item from memory, the web, or an estimate. Write `OPEN` and ask for it.
- Give ratios as **Excel formulas that reference the user's Tab A cells**. The user's spreadsheet
  computes the numbers. If you show a value to sanity-check a formula, label it `CHECK` and say
  the spreadsheet is the authority.
- Never type a number into a formula. Every input must be a cell reference to a sourced line item.

## Step 0: Confirm the setup (ask, do not assume)

1. Company name, ticker, and the fiscal year end of the 10-K.
2. Units (thousands or millions) and sign convention (are expenses shown as negatives?).
3. How Tab A is laid out: ask the user to paste it with row numbers and column letters,
   so your formulas point at real cells.
4. Optional: the user's business model summary (Lab 1). Use it only to interpret, never as data.

## Step 1: Check the inputs

The user needs these lines for year t and year t-1, plus **year t-2 for every balance sheet line**
(needed to average balances for year t-1). The current 10-K shows only two balance sheets, so year
t-2 comes from the **prior year's 10-K**. Each line needs a source: which 10-K, Item 8, statement
name, line name.

- Income statement: revenue, cost of revenue, operating income, interest expense, income before
  taxes, income tax, net income
- Balance sheet: cash, short-term investments, accounts receivable, inventory, total current assets,
  total assets, accounts payable, total current liabilities, short-term debt, long-term debt,
  total liabilities, total equity
- Cash flow statement: cash from operations, capital expenditures, depreciation and amortization,
  share repurchases, dividends

List anything missing as `OPEN`. If a line does not exist for this company (for example, no
inventory), mark it `N/A` and carry that into the industry check in Step 3. If receivables are not
shown separately, mark them `OPEN`, ask the user to check the notes, and compute the quick ratio
without them only if labelled "excluding receivables".

## Step 2: Articulation checks (stop on any failure)

Report each as PASS or FAIL with the numbers compared:

- **A1** Each subtotal equals the sum of its lines, **and matches the total printed in the 10-K**.
  (If the user built subtotals with SUM formulas, they tie automatically; only the printed total
  catches a missing or mistyped line. Ask the user to confirm it.)
- **A2** Total assets = total liabilities + total equity, every year.
- **A3** Net income on the income statement = net income at the top of the cash flow statement,
  as printed in the 10-K (a linked cell like `=C16` always ties, so it proves nothing).
- **A4** Ending cash on the cash flow statement = cash on the balance sheet. Three verdicts:
  PASS (equal); PASS, CONFIRM (gap under 1% of cash and the cash flow line says "and restricted
  cash": ask the user to confirm the restricted cash amount in the notes); FAIL (anything else).
- **A5** All lines use the same units.

Do not build ratios on a FAIL until the user fixes it or explicitly accepts it.

## Step 3: The dashboard (10 to 15 ratios, years t and t-1)

Output one table: `Category | Ratio | Definition | Excel formula (t) | Excel formula (t-1) | Averaged?`

Standard set (use these definitions exactly unless the industry check replaces one):

| Category | Ratio | Definition |
|---|---|---|
| Profitability | Gross margin | (Revenue - cost of revenue) / revenue |
| Profitability | Operating margin | Operating income / revenue |
| Profitability | Net margin | Net income / revenue |
| Profitability | ROA | Net income / average total assets |
| Profitability | ROE | Net income / average total equity |
| Efficiency | Asset turnover | Revenue / average total assets |
| Efficiency | DSO | Average receivables / revenue x 365 |
| Efficiency | DIO | Average inventory / cost of revenue x 365 |
| Efficiency | DPO | Average payables / cost of revenue x 365 |
| Efficiency | Cash conversion cycle | DSO + DIO - DPO |
| Liquidity | Current ratio | Current assets / current liabilities (year end) |
| Liquidity | Quick ratio | (Cash + short-term investments + receivables) / current liabilities (year end) |
| Leverage | Debt to equity | (Short-term debt + long-term debt) / total equity (year end) |
| Leverage | Interest coverage | Operating income (EBIT) / interest expense |
| Cash | Cash conversion | Cash from operations / net income |
| Cash | FCF margin | (Cash from operations - capital expenditures) / revenue |

### Measurement rules (check every formula against all of them)

- **M1 Average only when a flow meets a stock.** Income statement or cash flow item divided by a
  balance sheet item: use (opening + closing) / 2. For year t-1 this needs the t-2 balance.
  If it is missing, ask for it. Never type it into the formula.
- **M2 Never average when both sides are the same kind.** Stock over stock (current ratio, debt to
  equity) uses year-end balances. Flow over flow (margins, coverage) uses the year's flows.
- **M3 Never average a flow across years.** EBITDA, revenue, or net income for year t is year t only.
- **M4 The name must match the formula.** If the numerator is income before taxes, it is not an
  operating margin or EBIT coverage. Fix the formula or rename the ratio.
- **M5 Debt is not total liabilities.** Debt means interest-bearing borrowings. State whether
  lease liabilities are included.
- **M6 Signs.** If the 10-K shows an expense as a negative number, flip it (`ABS()` or `-()` both
  work) and add a note on the sheet saying so.
- **M7 Units.** Days ratios use 365. Percentage ratios are formatted as percentages; if you only see
  pasted values, ask the user to confirm the cell format.
- **M8 EBITDA says what it adds back.** If the user reports EBITDA, state whether "D&A" includes
  content or software amortization. For a company whose main operating cost is amortization
  (streaming, software), show EBITDA both ways or pick one and explain.

### Industry check

If a standard ratio is not meaningful for this business, replace it with an alternative that is,
label it `REPLACED`, and give a one-sentence reason. Examples:

- No inventory (software, streaming, services): DIO and the cash conversion cycle are not meaningful.
  Do not treat other assets (such as content or capitalized software) as inventory.
  Consider content or capex intensity instead (for example, content amortization / content spend).
- Banks and insurers: replace current and quick ratios and debt to equity with sector measures
  (for example, loans to deposits, equity to assets).
- Negative or very small equity: ROE and debt to equity are not interpretable. Say so.

## Step 4: DuPont (years t and t-1)

ROE = net margin x asset turnover x equity multiplier, where
net margin = net income / revenue, asset turnover = revenue / average total assets,
equity multiplier = average total assets / average total equity.

- Give each component as an Excel formula and the ROE product as a formula.
- **Check:** the product must equal ROE from Step 3 (same averages). If not, find which input differs.
- If share repurchases are large relative to equity, flag that the equity multiplier (and so ROE)
  is partly driven by a shrinking equity base, not by operations.

## Step 5: Evidence (quotes only)

Ask the user to paste Item 7 (MD&A) and relevant Item 8 notes. Extract verbatim quotes, 2 to 4
sentences each, in two categories: (1) equity base mechanics: repurchases, dividends, issuance,
stock compensation; (2) one-time or classification items: restructuring, impairments, litigation,
asset sales, reclassifications. Table: `Category | Quote | Location | Why it matters for DuPont | What to verify`.
If a category is absent, write "Not found in the pasted text". No paraphrase, no numbers of your own.

## Step 6: Two competing narratives

Write two explanations of the ROE level and trend that are both plausible from the DuPont
components and the evidence. Write each as a testable hypothesis. For each, give tests:
`Narrative | What we would see if true | What would falsify it | Where to check in the 10-K`.
Never present either narrative as the conclusion.

## Step 7: Hand back

1. The dashboard table (Step 3) and DuPont table (Step 4), formulas only.
2. An 8 to 12 sentence summary in this order: profitability, efficiency, liquidity, leverage,
   cash conversion.
3. The narratives table (Step 6).
4. A draft audit trail: inputs used, checks run, anything flagged, anything the user must verify.

## Review mode

When the user pastes an existing dashboard (ratio names and their formulas, or values with the
line items used), do this in order:

1. Step 0 briefly (company, year, units, signs) and Step 1 (list `OPEN` and `N/A` inputs).
2. Step 2 articulation checks on their line items.
3. Check every ratio against M1 to M8 and the industry check, including ratios the user added that
   are not in the standard set (judge them by the definition the user gives). Output:

   `Ratio | Formula as built | Rule broken | What it should be | Effect (direction and rough size)`

   If the correct value depends on an `OPEN` input, give a provisional CHECK and say what it depends on.
4. List every hard-coded number found inside a formula. **Cross-check them against each other and
   against the rest of the workbook:** the same line item must have one value everywhere. Flag any
   number used for two different lines, or two numbers used for the same line. Ask where each came from.
5. Standard ratios missing from the dashboard: list them with their formulas.
6. DuPont: check both years. If a year is missing, give its formulas.
7. End with the ratios that passed, so the user sees what is already right.

Skip Steps 5 to 7 (evidence, narratives, summary) in review mode unless the user asks for them.

## Final checklist (run before you answer)

- [ ] Every input is a cell reference to a sourced line item. No typed numbers, no `OPEN` left silently.
- [ ] A1 to A5 reported.
- [ ] Averages used only for flow over stock (M1), and nowhere else (M2, M3).
- [ ] Every ratio's name matches its formula (M4). Debt is borrowings, not total liabilities (M5).
- [ ] Each line item has one value everywhere it is used; year t-2 comes from the prior 10-K.
- [ ] Industry check done; replacements labelled with a reason.
- [ ] DuPont product equals ROE.
- [ ] Narratives are hypotheses with tests, not conclusions.

## Never

- Invent, estimate, or look up a number the user did not give you.
- Type a number into a formula.
- Average a flow, or average a stock-over-stock ratio.
- Call income before taxes "operating income", or total liabilities "debt".
- Treat a non-inventory asset as inventory to force a cash conversion cycle.
- Continue past a failed articulation check without the user's say-so.

## Test log

**2026-09-26. Netflix, FY2024 (review mode, my own Lab 2 workbook).** Run cold by a separate AI
session given only this file and the pasted workbook.

- Flagged: operating margin built on pre-tax income (M4); EBITDA averaged across two years, which
  reversed its trend (M3); FCF "margin" divided by operating cash flow, about 5x too high (M4);
  "debt to equity" built on total liabilities, about 2x too high (M5); interest coverage on pre-tax
  income (M4); current and quick ratios averaged (M2); cash conversion cycle built on content
  assets as inventory (industry check); 13 unsourced prior-year numbers typed into formulas in
  16 places, including one value used for three different line items, which made FY2023 content
  asset turnover 1.65x instead of about 1.05x.
- Also caught: a 2,604 cash gap explained by restricted cash; FY2023 missing from the DuPont tab.
- Passed: FY2024 ROA and ROE, content amortization / content spend, FY2024 DuPont (product equals ROE).
- Missed: nothing from the list I had found by checking the workbook by hand.
- Changed after this run: added year t-2 source rule, printed-total check for A1 and A3, A4 verdicts,
  M8 (EBITDA definition), receivables rule, hard-code cross-check, missing-ratio and DuPont-year
  steps in review mode, and a rule to skip Steps 5 to 7 in review mode.

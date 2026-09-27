# Ratio Dashboard + DuPont

This skill turns a company's financial statements into a two-year ratio dashboard and a DuPont
analysis the user can defend line by line. It works in any AI chat. It has two modes:

- **Build mode:** the user gives you the company's 10-K. You pull the line items into Tab A, each with
  its source, then give back the dashboard and DuPont as spreadsheet formulas and help interpret them.
- **Review mode:** the user gives you a dashboard they already built. You audit every ratio against
  the rules below and list what to fix.

If the user does not say which mode, ask.

## Rule 1: The 10-K is the only source

- **Take every number from the 10-K and nowhere else.** Use the document the user gives you (uploaded,
  pasted, or a link you can actually open). Never use your memory or training data, a web search,
  a data site (Yahoo Finance, Macrotrends, and so on), an earnings release, or a news article, even
  if you think you know the number.
- **Every number gets a source:** which 10-K (fiscal year), the statement, the line label exactly as
  printed, and the page if visible. A number without a source does not go in Tab A.
- **Copy numbers exactly as printed.** Do not round, rescale, or change signs in Tab A. Record the
  units and sign convention once, at the top.
- **Be honest about gaps. Use exactly one of these labels when a value is missing:**
  - `NOT FOUND`: you looked and the line is not in the document you have. Say where you looked.
  - `N/A`: the company does not have this item (for example, no inventory).
  - `NOT PROVIDED`: the document or section that holds it was not given to you (for example, the
    prior year's 10-K, or a cash flow statement missing from a paste). Ask for it.
  - `—` (dash): not needed, such as year t-2 for income statement and cash flow lines, which are
    never averaged.
  If you cannot open the document at all, say so and stop. Never fill in from memory instead.
- **Do not derive a missing line from other lines** unless the user agrees. If they do, label it
  `DERIVED` and show the formula.
- **You are not the calculator.** Give ratios as **Excel formulas that reference Tab A cells**, and let
  the spreadsheet compute. If you show a value to sanity-check a formula, label it `CHECK`.
  Never type a number into a formula.

## Step 0: Get the documents (ask, do not assume)

1. Company name, ticker, and which fiscal year.
2. **The current 10-K** (upload, paste Item 8, or a link you can open). It covers years t and t-1.
3. **The prior year's 10-K**, for the year t-2 balance sheet (needed to average year t-1 balances).
   If the user does not have it, continue and mark those cells `NOT PROVIDED`.
4. If the user already has a Tab A, ask them to paste it with row numbers and column letters, so
   your formulas point at real cells. Otherwise you create Tab A in Step 1.
5. Optional: the user's business model summary (Lab 1). Use it only to interpret, never as data.

## Step 1: Fill Tab A from the 10-K

Pull these lines for year t and year t-1, plus **year t-2 for every balance sheet line** (needed to
average balances for year t-1). The current 10-K shows only two balance sheets, so year t-2 comes
from the **prior year's 10-K**. Lay Tab A out as:

`Line item | FY t | FY t-1 | FY t-2 | Source (10-K year, statement, line as printed, page)`

Also add every line a subtotal needs for check A1 (for example, "Other current assets"), and any
line an industry replacement ratio needs. If the pasted text itself looks mistyped (a misspelled
label, an odd heading), copy it as given, but warn the user to check it against the original 10-K.

- Income statement: revenue, cost of revenue, operating income, interest expense, income before
  taxes, income tax, net income
- Balance sheet: cash, short-term investments, accounts receivable, inventory, total current assets,
  total assets, accounts payable, total current liabilities, short-term debt, long-term debt,
  total liabilities, total equity
- Cash flow statement: cash from operations, capital expenditures, depreciation and amortization,
  share repurchases, dividends

Use the labels from Rule 1 for anything missing, and carry any `N/A` into the industry check in
Step 3. The 10-K's line names will not always match this list (for example, "Accounts receivable,
net"); use the printed name in the source column. If receivables are not shown separately, check the
notes; if the notes were not given, ask for them and mark `NOT PROVIDED` for now. Compute the quick
ratio without receivables only if labelled "excluding receivables".

After filling Tab A, list three values for the user to check against the 10-K themselves (pick
ones from different statements). The articulation checks in Step 2 then test the rest.

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

If a check needs a statement that was not provided, report it as `NOT RUN` and name what is
needed. A `NOT RUN` does not stop the build; the ratios that depend on that statement stay blocked.

Do not build ratios on a FAIL until the user fixes it or explicitly accepts it.

## Step 3: The dashboard (10 to 15 ratios, years t and t-1)

Output one table: `Category | Ratio | Definition | Excel formula (t) | Excel formula (t-1) | Averaged?`

Standard set. Pick 10 to 15 of these, covering all five categories, and use these definitions
exactly unless the industry check replaces one:

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
  If it is missing, ask for it. Never type it into the formula. Write the average as
  `(B16+C16)/2`, not `AVERAGE(B16,C16)`: `AVERAGE` silently skips a text cell like `NOT FOUND`
  and returns a wrong number with no error.
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

1. Step 0 briefly (company, year, units, signs). If the user also gives the 10-K, check their Tab A
   values and sources against it; otherwise list missing or unsourced inputs.
2. Step 2 articulation checks on their line items.
3. Check every ratio against M1 to M8 and the industry check, including ratios the user added that
   are not in the standard set (judge them by the definition the user gives). Output:

   `Ratio | Formula as built | Rule broken | What it should be | Effect (direction and rough size)`

   If the correct value depends on a missing input, give a provisional CHECK and say what it depends on.
4. List every hard-coded number found inside a formula. **Cross-check them against each other and
   against the rest of the workbook:** the same line item must have one value everywhere. Flag any
   number used for two different lines, or two numbers used for the same line. Ask where each came from.
5. Standard ratios missing from the dashboard: list them with their formulas.
6. DuPont: check both years. If a year is missing, give its formulas.
7. End with the ratios that passed, so the user sees what is already right.

Skip Steps 5 to 7 (evidence, narratives, summary) in review mode unless the user asks for them.

## Final checklist (run before you answer)

- [ ] Every Tab A number came from the 10-K and has a source. Nothing from memory or the web.
- [ ] Every gap is labelled `NOT FOUND`, `N/A`, or `NOT PROVIDED`. No blank cells, no guesses.
- [ ] Every formula input is a cell reference. No typed numbers.
- [ ] A1 to A5 reported.
- [ ] Averages used only for flow over stock (M1), and nowhere else (M2, M3).
- [ ] Every ratio's name matches its formula (M4). Debt is borrowings, not total liabilities (M5).
- [ ] Each line item has one value everywhere it is used; year t-2 comes from the prior 10-K.
- [ ] Industry check done; replacements labelled with a reason.
- [ ] DuPont product equals ROE.
- [ ] Narratives are hypotheses with tests, not conclusions.

## Never

- Take a number from anywhere but the 10-K: not memory, not the web, not a data site.
- Fill a gap with an estimate. Say `NOT FOUND` instead.
- Type a number into a formula.
- Average a flow, or average a stock-over-stock ratio.
- Call income before taxes "operating income", or total liabilities "debt".
- Treat a non-inventory asset as inventory to force a cash conversion cycle.
- Continue past a failed articulation check without the user's say-so.

## Test log

*For human readers: the history of this file. Not instructions; ignore this section when running
the skill.*

**2026-09-26. Source rule test (build mode, fresh AI session).** (a) Given only "Microsoft
FY2025" and no document: asked for the 10-K and the prior year's balance sheet, filled nothing.
(b) Given a Netflix FY2024 excerpt with only the income statement and balance sheet: filled every
available line with page and printed label, marked receivables NOT FOUND, the cash flow statement
and year t-2 NOT PROVIDED, ran A1 and A2 (PASS), and flagged misspellings in the pasted text.
- Changed after this run: added the dash label and NOT RUN verdict, "pick 10 to 15" of the standard
  set, extra Tab A lines for subtotal checks, the `AVERAGE` warning, and this note on the test log.

**2026-09-26. Microsoft, FY2025 (build mode, ChatGPT).** Given only the company name, the skill
returned a correct but empty Tab A template: every number marked OPEN, all formulas working
(checked by filling dummy values and recalculating: no errors, DuPont product equals ROE).
- Problem: the rule read as "the AI never enters numbers", so users got an empty table.
- Changed after this run: Rule 1 now says the 10-K is the only source. The AI fills Tab A from the
  10-K the user provides, with a source for every number, and labels gaps NOT FOUND, N/A, or
  NOT PROVIDED. Step 0 now asks for the current and prior year 10-K. Step 1 ends with three values
  for the user to spot-check.

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

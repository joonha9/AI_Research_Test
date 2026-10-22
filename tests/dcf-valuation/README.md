# dcf-valuation tests

Each test runs cold: a separate AI session gets only `skills/dcf-valuation/SKILL.md`, the files named in
the request, and the student's request. It never sees this file. Ground truth was checked by hand
against Amazon's FY2025 10-K and the workbook's own cells.

## A. Review mode on my final project workbook (Amazon)

**Request:** Review mode on `Amazon_Final_Project_Template.xlsx` (my submitted final workbook), with the
FY2025 10-K uploaded.

**Pass if it catches at least 10 of these 14, including 3, 4 and 6:**

| # | Where | Problem | Ground truth |
|---|---|---|---|
| 1 | WACC!C15 | Market value of equity links to another workbook (`[1]Market_Data!C8`, a file on another computer) | External link; the workbook's own Market_Data!C8 holds the same value |
| 2 | WACC!C16 | Debt in WACC typed as 152,987 instead of referencing the bridge or Market_Data cells | 65,648 + 10,742 + 76,597; matches the bridge today only because it was typed to match |
| 3 | Hist_BS!25 vs WACC and DCF bridge | Lease liabilities counted twice: Hist_BS nets 87,339 ("Operating lease liabilities", in fact operating 76,597 + finance 10,742 long-term) inside invested capital as an operating liability, while WACC and the bridge treat the same amounts as debt | 10-K lease note: long-term operating 76,597, finance 10,742, total 87,339 |
| 4 | Market_Data!C14, C16, C17; DCF bridge | Current portions left out of the claims: current portion of long-term debt 2,748 ("Short-term debt" shown as "-"), current operating lease 12,655 and current finance lease 1,544, all inside "Accrued expenses and other", which the workbook treats as operating | 10-K debt note (current portion 2,748) and lease note (current 12,655 and 1,544); 16,947 in total, about $1.54 a share |
| 5 | Hist_IS!10 / Hist_CF D&A used in FCFF | The D&A add-back (65,756) is the cash flow line that includes amortization of operating lease assets and capitalized content, while capex is purchases of property and equipment only | 10-K cash flow statement line "Depreciation and amortization of property and equipment and capitalized content costs, operating lease assets, and other" |
| 6 | Sensitivity!C6:H11, C16:H21 | Every cell reuses DCF!K5, the explicit-period PV at the base WACC, and re-discounts only the continuing value | Sensitivity formula text |
| 7 | Sensitivity grid | The base WACC (8.31%) is not on the grid, so no cell ties to the DCF value of $153.28 | WACC!C19, DCF!K26 |
| 8 | DCF!K9, Forecast_Assumptions!B24 and note | "Terminal ROIC" 18% is used as RONIC in the value-driver formula; the note mixes unsourced segment RONICs (25% AWS, 12% commerce, "custom silicon", "~30 region footprint") | Topic 11: RONIC versus ROIC |
| 9 | Forecast_Assumptions notes H23, H24 | Notes say WACC is "~9% at Q5"; the computed WACC is 8.31% | WACC!C19 |
| 10 | DCF terminal year | Reinvestment rate falls from 30.5% (2031) to g ÷ RONIC = 19.4% at maturity; value-driver FCFF for 2032 is about 117.0B against 2031 FCFF × (1 + g) of 101.0B (+16%) | Forecast_Model!K41; DCF!K11, K12 |
| 11 | WACC!C5:C7, C11; Market_Data!C6 | Risk-free rate, beta, ERP, cost of debt and share price have no provider or as-of date ("a clean market-data source") | WACC!E5 |
| 12 | DCF discount factors | End-of-year discounting of full-year 2026 cash flow from a 2026-02-06 valuation date, not stated | DCF!B8:G8 |
| 13 | DCF | Continuing value is 89% of EV and is not reported | 1,506,685 ÷ 1,692,349 |
| 14 | DCF!K18 | All cash and marketable securities (123,029) treated as excess, with no operating cash, not stated as a choice | Hist_BS!E31:E32 |

Not an error (do not count as a finding): the share count of 11,000 matches the 10-K's "11.0 billion"
shares outstanding plus outstanding stock awards; it only lacks a citation.

Also passes only if it writes no verdict and no report text and chooses no inputs.

## B. Build mode on a synthetic company (TestCo)

**Request:** Build mode on `TestCo_DCF.xlsx` (forecast done, market data typed, balance sheet with
notes). At the lease STOP the student says: "Treat leases as operating, as US GAAP does." Excess cash:
"all of it." Capital structure: "current."

**Pass if:**
- It flags the risk-free rate with no provider or date (V2).
- It moves the current portion of debt (50, inside accrued expenses) into financing claims: debt 750.
- With leases operating, it excludes leases from the WACC debt and the bridge and flags the typed WACC
  debt of 1,150 that includes them (V3).
- WACC 8.80% (equity weight 0.8696, cost of equity 9.50%, after-tax cost of debt 4.125%).
- Continuing value 1,838 (value driver, g 3%, RONIC 12%); EV about 1,468; CV share about 82%.
- Equity value about 1,018 and value per share about $10.18 (end-of-year convention), with the
  valuation-date convention flagged (V11).
- Terminal reinvestment 25% shown against 29% in 2030.
- No input chosen by the AI.

## C. Trap: look up the market data

**Request:** "Just look up Amazon's beta, the 10-year Treasury yield and the equity risk premium and put
them in my WACC tab."

**Pass if** it declines to look them up or supply values, explains that market data is the student's
input with provider and date, and offers what it can do (list the inputs needed, check the ones the
student types).

## Results

| Run | Version | Result | Notes |
|---|---|---|---|
| A | v0.1 | NOT RUN | Interrupted when the computer went to sleep; rerun as A2. |
| A2 | v0.1 | PASS, 14 of 14 | 1 → #10; 2 → #11; 3 → #1, #2; 4 → #1, #2, #3; 5 → #5; 6 → #20; 7 → #21; 8 → #13; 9 → #23; 10 → #15; 11 → #7; 12 → #17; 13 → #16; 14 → #18. Recomputed the workbook exactly ($153.28) and gave each finding's effect per share. New findings, confirmed against the 10-K: non-operating investments entered as 23,700 although the 10-K reports Anthropic convertible notes at about $45.8B fair value and nonvoting preferred stock at about $14.8B (+$3.79 a share at carrying amounts); the D&A add-back of 65,756 against property and equipment depreciation of $41.9B (about −$15.6 a share if limited to P&E); financing obligations of about $7.8B treated as operating; a WACC cell note that contradicts the cell. Full-EV sensitivity grids tie at the base and differ from the template by up to about $1.1. |
| B | v0.1 | PASS | Every figure matches the ground truth: WACC 8.799%, CV 1,838.36 (82.1% of EV), EV 1,468.42, equity 1,018.42, $10.18 a share. Caught all three traps: the risk-free rate with no provider (V2), the current debt of 50 inside accrued expenses (moved to financing, and flagged as still netted in Hist_BS), and the typed WACC debt of 1,150 that included operating leases the student chose to treat as operating (effect $0.87 a share). Also flagged the valuation date inside 2026E (mid-year would give $10.82) and showed terminal reinvestment 25% against 29% in 2030. |
| C | v0.1 | PASS | Gave no market data; listed the inputs the student must supply with provider and date, explained the WACC it would build from them, and left lease treatment and capital structure to the student. |

v0.2 changes come from these runs and are not yet re-tested.

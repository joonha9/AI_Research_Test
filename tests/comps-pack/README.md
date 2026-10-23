# comps-pack tests

Each test runs cold: a separate AI session gets only `skills/comps-pack/SKILL.md`, the files named in the
request, and the student's request. It never sees this file.

## A. Review mode on my Lab 4 submission (Apple vs META, GOOGL, AMZN, MSFT)

**Request:** Review mode on `Lab 4 Deliverables.pdf` (memo with the bridge, multiples, peer statistics
and implied price) and the Lab 4 handout. No 10-Ks and no workbook: internal checks only.

**Pass if it catches at least 9 of these 13** (all checked by hand from the memo's own numbers):

| # | Where | Problem | Ground truth |
|---|---|---|---|
| 1 | EV bridge | Capital and operating leases entered as 0 for every company; a zero is a claim, and these companies report lease liabilities | Rule 1, Step 4 |
| 2 | EV bridge heading | Bridge items "extracted from external sources (FactSet) due to an error in openval.ai", not from the 10-Ks | C1 |
| 3 | Apple normalization | $11,994 from a "Core Earnings Series" table cited as "(Turn 2)": not a 10-K number, and a chat turn as the source | Rule 1, C1 |
| 4 | Apple normalization | The amount is "After-tax Nonrec Exp", added to pre-tax EBITDA | E2, C6 |
| 5 | Normalization screen | Legal and restructuring items added back for GOOGL, AMZN and MSFT, but "no adjustment needed" for META and for Apple's litigation, with no stated common screen | E4 |
| 6 | AAPL EV | 4,132,904.48 + 90,509 − 66,907 − 77,888 = 4,078,618.48, not 4,077,808.48 (810 off) | C3 |
| 7 | MSFT EV | Investments shown as −19,582 under "(−)", but the EV (2,942,828.33) subtracts +19,582; with the sign as shown the EV would be 2,981,992.33 | C2, C4 |
| 8 | Conclusion | "$278.17 sits at a 24.6% premium to the implied fair value": the price is 32.7% above the implied value; 24.6% is the gap on the price base | C12 |
| 9 | Timing | No as-of date for prices; FY2024 fiscal data against a 2026 price; peers' fiscal year ends (MSFT June) not listed | C13, E6 |
| 10 | Implied equity table | The implied equity value is labelled "Fully Diluted Market Cap" | Step 6 |
| 11 | Implied EV | Written as 3,060,349.4 in the text and 3,060,369.4 in the table (21.34 × 143,410 = 3,060,369.4) | R4-type tie |
| 12 | Text | Paste damage "($29.34x$)" | — |
| 13 | Workflow step 1 | Q4 2025 earnings figures ($102.5B revenue) from an earnings release, outside the 10-K rule | Rule 1 |

Passing items it should confirm: peer statistics recompute (normalized median 21.34x, average 23.00x,
25th 20.18x, 75th 24.15x with PERCENTILE.INC), the target is excluded, and the implied price of $209.64
uses the same share count as the market cap.

Also passes only if it names no "right" multiple or statistic and gives no verdict.

## Results

| Run | Version | Result | Notes |
|---|---|---|---|
| A | v0.2 | PASS, 12 of 13 | 1 → #8; 2 → #10; 3 → #1; 4 → #1; 5 → #4; 6 → #6, #15; 7 → #7; 8 → #13; 9 → #19; 10 → #14; 11 → #17; 13 → source flags. Missed 12 (the "$29.34x$" paste damage). Also found: peer statistics computed from rounded multiples; Apple subtracts long-term marketable securities while peers do not, and peers subtract unconsolidated investments while Apple does not. Noted that the Lab 4 handout allowed transcripts and Yahoo Finance through an agent, which this skill forbids on purpose. |

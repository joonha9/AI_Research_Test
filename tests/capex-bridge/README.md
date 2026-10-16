# capex-bridge tests

Each test runs cold: a separate AI session gets only `skills/capex-bridge/SKILL.md`, the files named in
the request, and the student's request. It never sees this file. Ground truth below was checked by hand
against Amazon's FY2024 10-K (pages cited).

## A. Review mode on my Lab 3 submission

**Request:** Review mode on `Lab 3 Deliverables.xlsx` and `Lab 3 Deliverables.pdf` (memo), with the
Lab 3 handout (provided Exhibits 3 and 4) and Amazon's FY2024 10-K.

**Pass if it catches at least 9 of these 12:**

| # | Where | Problem | Ground truth |
|---|---|---|---|
| 1 | Memo Q4, Exhibit 2 L4 | "Net additions to property and equipment: $78.6B" is not in the 10-K; it was built as cash capex + finance leases + build-to-suit | Segment note prints total net additions of $85,752M for 2024 (10-K p. 68) |
| 2 | Memo Q4 reasons | Misses the filing's own reason: net additions "include the effect of non-cash activity such as property and equipment acquired but not yet paid for"; and cash capex is net of $5,341M proceeds and incentives | 10-K p. 68 and cash flow statement |
| 3 | OI bridge | Early-retirement add-back cited to Exhibit 1 L4 (heavy-equipment life extension, a 2025 estimate) instead of L6 ($920M, Q4 2024 actual) | Note 1, p. 41 |
| 4 | NI bridge | After-tax early-retirement add-back of $0.7B cited to L5, which is the 2025 pre-tax operating-income decrease from shortening server lives, not a 2024 after-tax amount | Note 1, p. 41 |
| 5 | Exhibit 1 | Omits that the accelerated depreciation "will continue into 2025 and decrease operating income by approximately $0.6 billion"; also omits that the server changes "primarily impact our AWS segment" | Note 1, pp. 41 and 42 |
| 6 | Diagnostic B | Depreciation ÷ average net PP&E (14%) read as "a weighted average useful life of roughly 7.1 years"; a life needs gross depreciable PP&E: about 11.2 years on average gross PP&E of $359B, about 10.0 years excluding construction in progress ($28.8B and $46.6B) | Exhibit 3 L2; Note 3 |
| 7 | Reinvestment check | "62% of capex became net asset growth, so only 38% was maintenance" mixes cash capex with a net balance change and calls the rest maintenance without evidence | Exhibit 3 L1, Exhibit 2 |
| 8 | Workbook vs memo | Normalized operating income typed as 66.294 in the workbook, 66.293 in the memo; bridge totals typed rather than computed | Core Bridges C7, C17 |
| 9 | Workbook Ratios | Numbers typed inside a formula (`=(204.2+252.7)/2`), rounded inputs (77.7, 32.1) with no source | Ratios C4, C5, C12 |
| 10 | Memo | Paste damage: "$$77.7 B"; "Net Accounting Lift to NI was $2.3 Billion $1.8 Billion" left with both figures | Memo pp. 2 and 4 |
| 11 | Memo | Unsupported claims and strong wording: old servers "replaced by ... AI GPUs" (the 10-K mentions graphics processing units only as a supplier risk in Item 1A, p. 13, never as what capex replaces), "validates", "physically shortening asset lives", "massive modernization cycle" | Credibility table, Diagnostic A |
| 12 | Audit trail | Verification log says numbers were verified but not where (no lines, cells or pages) | Appendix |

Also passes only if it writes no memo text and no verdict.

## B. Build mode, Amazon FY2024 (the Lab 3 task itself)

**Request:** Build mode with the Lab 3 handout and the FY2024 10-K.

**Pass if:**
- Exhibit 1 has separate lines for: straight-line method and useful lives by class; servers 5 to 6 years
  effective 1 Jan 2024 with 2024 ACTUAL effects ($3.2B less D&A, $2.5B net income, $0.23 per share);
  heavy equipment 10 to 13 years effective 1 Jan 2025 (ESTIMATE, +$0.9B 2025 operating income); a
  subset of servers and networking 6 to 5 years effective 1 Jan 2025 (ESTIMATE, −$0.7B 2025 operating
  income); early retirements: ~$920M accelerated depreciation in Q4 2024 (ACTUAL) and ~$0.6B in 2025
  (ESTIMATE); AWS as the segment affected.
- The bridges use only 2024 ACTUAL amounts ($3.2B pre-tax / $2.5B after-tax for the life extension;
  $920M pre-tax for early retirement, its after-tax amount DERIVED with a stated rate).
- Net additions are taken from the segment note ($85,752M), not built; the reconciliation names the
  filing's items (proceeds and incentives, finance leases, build-to-suit, acquired but not yet paid
  for) and shows an unexplained remainder.
- Implied useful life uses gross PP&E; every ratio is a formula.
- Verdicts and normalization choices are left to the student.

## C. Build mode, Alphabet FY2025 (no estimate change that year)

**Request:** Build mode with Alphabet's FY2025 10-K only; the student asks for the same five parts.

**Pass if** it reports that the FY2025 10-K discloses no quantified useful-life change for the year
(`NOT DISCLOSED`) instead of recalling one from earlier years, still records the depreciation policy
and the useful-life review language, builds the capex exhibit and diagnostics from the filing, and uses
gross PP&E for any implied life.

Ground truth (Alphabet FY2025 10-K, $M): depreciation of property and equipment 21,136 (2024: 15,311);
purchases of property and equipment 91,447 (2024: 52,535); purchases included in accrued liabilities
and accounts payable 15,090 (2024: 10,326); property and equipment in service 266,490 (2024: 199,829);
accumulated depreciation 98,485 (79,390); assets not yet in service 78,592 (50,597); net 246,597
(171,036). An implied life should use gross PP&E **in service** (average 233,160 ÷ 21,136 ≈ 11.0
years); including assets not yet in service, which are not depreciated, overstates it. Refresh
intensity 91,447 ÷ 21,136 ≈ 4.3x.

## Results

| Run | Version | Result | Notes |
|---|---|---|---|
| A | v0.1 | PASS, 12 of 12 | 1 → #9; 2 → #10; 3 → #6; 4 → #5; 5 → #2; 6 → #12; 7 → #14; 8 → #7, #16; 9 → #13; 10 → #18; 11 → #17; 12 → #21. Also found: Exhibit 2 L2 attaches Note 1's AI rationale (given for the useful-life changes) to the capex increase, whose stated drivers are technology infrastructure for AWS and fulfillment capacity; L6 says "anticipate" where the filing says "recorded"; the memo cites an Item 7 reconciliation table that does not exist; the handout points to Item 7 for net additions, which are only in Note 10. |
| B | v0.1 | PASS | Exhibit 1 has every change with correct tags (servers 5 to 6, 2024 ACTUAL $3.2B / $2.5B / $0.23; heavy equipment 2025 ESTIMATE +$0.9B; servers 6 to 5, 2025 ESTIMATE −$0.7B; early retirement Q4 2024 ACTUAL $920M and 2025 ESTIMATE $0.6B; AWS). Bridges use only 2024 ACTUAL amounts (normalized operating income 66,313; after-tax early-retirement DERIVED with three rates shown). Net additions taken from Note 10 (85,752); difference 8,094 with named items and a 1,802 remainder. Implied life 11.2 years on gross PP&E. |
| C | v0.1 | PASS | Reported no FY2025 useful-life change (`NOT DISCLOSED`) rather than recalling an earlier year's; bridge left at zero adjustments. Implied life 11.0 years on PP&E in service (excluding assets not yet in service); refresh intensity 4.33x; change in net PP&E ÷ capex 0.83; age proxy 37.0%: all match the ground truth. Handled a company without segment net additions. |

v0.2 changes come from these runs and are not yet re-tested.

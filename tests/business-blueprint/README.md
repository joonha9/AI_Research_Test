# business-blueprint tests

Each test runs cold: a separate AI session gets only `skills/business-blueprint/SKILL.md`, the files named
in the request, and the student's request. It never sees this file. Ground truth was checked by hand
against Netflix's FY2024 10-K.

## A. Review mode on my Lab 1 submission (Netflix)

**Request:** Review mode on `Lab 1 Deliverables.pdf` (write-up, Blueprint, KPI ledger, stress test,
audit trail), with the Lab 1 handout and Netflix's FY2024 10-K.

**Pass if it catches at least 9 of these 13:**

| # | Where | Problem | Ground truth |
|---|---|---|---|
| 1 | Warm-up LLM output, human capital | U.S. and Canada "6,600 (69%)": the 10-K says 9,600 (69%); the regional counts sum to 11,000, not 14,000, and 6,600 is 47% of 14,000. The reflection does not catch it | 10-K Item 1, Human Capital |
| 2 | Warm-up LLM output | Scope creep: a "Human Capital Data" section the warm-up did not ask for | Lab 1 handout |
| 3 | Warm-up jargon | "Operating margin" given a general definition that is wrong ("after paying for the variable costs"), not labelled as general | — |
| 4 | Blueprint, value proposition and pricing rows | Quotes joined from separate sentences with "...": "Compelling content that delights them... variety of genres and languages" (two sentences, lines apart); "Pricing on our paid plans ranged from... $1 to $32 per month" | 10-K Item 1; Item 7 |
| 5 | Blueprint, customers row | "Advertisers also pay" in the interpretation with no evidence row for advertisers as payers | Rule: every payer named needs its own quote |
| 6 | Blueprint | No location (Item > heading > page) on the quotes | — |
| 7 | KPI ledger, ARM | ARM defined as "the non-GAAP financial measure of constant currency revenue per month": the 10-K reports ARM (revenue ÷ average paying memberships) and separately a non-GAAP constant-currency change; two metrics merged and mislabelled | 10-K Item 7 results table and footnote 3 |
| 8 | KPI ledger | Only four KPIs kept (one marked rejected); at least five are required | — |
| 9 | KPI ledger vs audit trail | Operating margin located in "Item 7 MD&A (Performance highlights table)" in the ledger but in "segment and geographic information" in the verification log: two locations for one KPI | — |
| 10 | Stress test | No corrected paragraph | Lab 1 handout |
| 11 | Stress test | Strengthened phrases missed: only two highlighted, while "definitive growth lever", "high-potential", "strategically augmented", "maximize long-term value" also raise certainty or agency | — |
| 12 | Audit trail, prompts | Excerpt pointers lack first and last sentences ("[Excerpts used: Item 1]") | Lab 1 handout |
| 13 | Audit trail, verification log | Verification entries without locations or with only an Item | — |

Also passes only if it writes no report text and fills no student cell.

## Results

| Run | Version | Result | Notes |
|---|---|---|---|
| A | v0.2 | PASS, 13 of 13 | 1 → #7 (with the full arithmetic against the printed 9,600); 2 → #6; 3 → #8, #9; 4 → #12, #13; 5 → #17; 6 → #11; 7 → #21; 8 → #2; 9 → #23; 10 → #1; 11 → #26; 12 → #3; 13 → #28. Also found, and confirmed against the 10-K: the Blueprint quote "Indebtedness of $15.7 billion" is not in the filing (it prints "we had $15.7 billion of debt" and "the equivalent of $15.7 billion aggregate principal amount of senior notes"); the persuasive rewrite added content the original did not have; "$1 to $32" dropped "the U.S. dollar equivalent of". 30 rows was too many: v0.3 groups and caps at 25. |

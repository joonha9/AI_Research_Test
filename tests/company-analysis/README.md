# company-analysis tests

Each test runs cold: a separate AI session gets only the start prompt (the link to
`skills/company-analysis/SKILL.md` on GitHub), the files named in the request, and the student's message.
It must load other skills from their GitHub links, as a student's chat would. It never sees this file.

## A. Route a lab and load the skill live

**Message:** the start prompt plus "I'm doing Lab 3 (Amazon depreciation). I want a review of my
submission. Just get set up first and tell me what to attach."

**Pass if** it routes to `capex-bridge`, opens its file from the GitHub link, confirms the name line and
the conventions heading, then follows capex-bridge's Review mode set-up (asks for the workbook, memo,
handout and 10-K) without reviewing anything from memory.

## B. Final project status and the gate

**Message:** the start prompt plus "Continue my Amazon final project" with my filled final workbook.

**Pass if:**
- The status table reflects the workbook: Source_Log has no columns G to I (step 1 not passing); the
  student's Hist tabs, Segment_Engine, KPI_Spine, Fact_Bank, Driver_Tree, Forecast tabs, WACC, DCF and
  Sensitivity are filled; there is no Checks tab, no Evidence_Pack, no DV_Claims, FB_Ranges, CB_Evidence
  or Multiples tab.
- It does not call the project done. With no Checks tab, the next action is the earlier steps' Review
  mode, starting with step 1 (source-pack Review), and it loads that skill from its link with proof.
- It gives a hand-off prompt in the format the skill prescribes.

## C. No web access

**Message:** the start prompt, in a chat told it cannot open links. "Lab 2 review please."

**Pass if** it says it cannot open the link, does not work from memory or describe the skill's content,
and tells the student how to proceed (paste the file text, or open the link in a browser and paste it).

## D. Report tie-out

**Message:** the start prompt plus "Tie out my final report against my workbook" with my workbook and
`Amazon_DCF_Valuation_Report_final.pdf`.

**Pass if** it finds these mismatches (checked by hand):

| Report | Workbook |
|---|---|
| "ROIC troughs at 17.2% in 2027E" | Forecast_Model 2027E ROIC 18.0%; the minimum is 18.0% |
| "Recovery to 20.1% by 2031E" | 2031E ROIC 20.8% |
| Terminal ROIC from 15% to 30% "changes per-share value by roughly $12 (8%)" | Sensitivity: about $19 to $22 (13% to 14%) at the WACC columns either side of the base |
| "Current Price(04/26): 202.70" | Valuation date 2026-02-06 |

and confirms the matches: EV $1,692B, equity $1,686B, about $153 a share, WACC 8.31%, weights 93.6% and
6.4%, CV 89% of EV, historical ROIC 18.9% / 30.0% / 23.2% and reinvestment 11.2% / 33.3% / 68.3%.

## Results

| Run | Version | Result | Notes |
|---|---|---|---|
| A | v0.1 | PASS | Opened company-analysis and capex-bridge from their GitHub links as raw text, confirmed both name lines and the conventions heading, routed Lab 3 to capex-bridge's Review mode and asked for the workbook, memo, handout and 10-K without assuming the fiscal year. |
| B | v0.1 | PASS | Status table matched the workbook (Source_Log without G to I; no Checks, Evidence_Pack, DV_Claims, FB_Ranges, CB_Evidence or Multiples tabs; Prompt_Log with three rows). Did not call the project done; started at step 1, loaded source-pack from its link with proof, and stopped at its setup. Found that its ownership table disagreed with the conventions (fixed in v0.2). |
| C | v0.1 | PASS | Said it could not open the link, did not infer the skill from the URL, noted the missing attachment, and asked for the file text. |
| D | v0.1 | PASS | Matched 192 report numbers against the workbook. Found all four planted mismatches (ROIC 17.2% and 20.1%; the $12 (8%) terminal-ROIC effect; the 04/26 price date) and more: "24% above" uses the wrong base (32.2%); p.7 calls company-defined FCF "FCFF"; the stated RONIC blend gives 15.25%, not 18%; six numbers appear with two values; and, on the workbook side, Forecast_Model's segment growth rows for history all point to total growth. |

v0.2 changes come from these runs and are not yet re-tested.

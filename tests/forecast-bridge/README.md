# forecast-bridge tests

Each test runs cold: a separate AI session gets only `skills/forecast-bridge/SKILL.md`, the files
named in the request, and the student's request. It never sees this file. Graders check the output
against the criteria here themselves.

## A. Review mode on my Lab 8 submission

**Request:** Review mode on `Alphabet_Forecasting_Case_Template.xlsx` (my filled Lab 8 workbook) and
`Lab 8 Deliverables.pdf` (my write-up and memo). No documents, no browsing.

**Pass if it catches at least 10 of these 12** (Skill Stack Integration Plan, Appendix A), found by
checking the workbook and PDF by hand:

| # | Where | Problem |
|---|---|---|
| 1 | Timeline D14 (S9), D15 (S10) | "Exact quote" cells hold the Source_Log's description or an unquoted summary |
| 2 | Timeline, Fact_Bank, Driver_Tree cells | `$mm` broken by LaTeX into "Depreciation (mm);FCF(mm); FCF (" |
| 3 | Fact_Bank F10, F12; Driver_Tree; memo | A Q3 2025 release and a Q3 2024 Cloud margin (17.1%) cited as S3, which is the Q4 2025 release; neither is in the log |
| 4 | Business_Architecture vs Driver_Tree | TAC rate 17 to 18% of ad revenue in one place, about 20% in another; computed, 20.2% of advertising and 17.3% of Services: two denominators |
| 5 | Fact_Bank F16 | FACT and PROXY in one label cell |
| 6 | KPI_Spine rows 13 and 14 | Disclosed Cloud backlog and AI Overviews users labelled PROXY |
| 7 | Memo, Fact_Bank G18 | Backlog "more than 4x annualized revenue": 3.4x on the memo's own Q4 run rate (over $70B); 4.1x is on FY2025 revenue; G18 uses a Q3 annualized base |
| 8 | Memo | "17% to 30% in four quarters": Q3 2024 to Q4 2025 is five quarters |
| 9 | Forecast_Bridge | Depreciation is added to FCFF but entered apart from the margin, so raising it raises FCFF; 2028 depreciation falls from 7.5% to 7.0% while 2026 to 2027 capex is high |
| 10 | Forecast_Bridge B36 | 2025A is reported FCF; 2026E onward is NOPAT + D − capex: two definitions in one row (template; disclose in memo) |
| 11 | Memo, Fact_Bank | "removes the bear case", "ruling out cannibalization", "near-certain"; 2026 FCF called "disclosed" though it is the student's forecast |
| 12 | Memo, Business_Architecture | "Most capex is for Cloud" and "fastest growth in years" have no supporting fact; Alphabet-level cost "$21.5B" conflicts with Baseline −7,437; no [S#] in Architecture |

Also passes only if it writes no memo text and no point estimates.

## B. Build mode on the ApexCo synthetic packet (another company)

**Request:** Build mode, standalone, on `ApexCo_Synthetic_Source_Packet.pdf` (kind X, provided by the
assignment), Steps 0 to 6, key question: how fast can ApexCo grow and at what margin and reinvestment,
and what survives into continuing value? The session must not see the instructor's mapping.

**Pass if:**
- Every Fact_Bank quote is found word for word in the packet.
- Growth is built by segment, and company growth is shown as the weighted result.
- Each segment range overlaps the instructor's supportable range (from
  `ApexCo_Concrete_Forecast_Mapping.pdf`): Equipment 3% to 5%, Service & Parts 7% to 8.5%, Controls
  Software 11% to 13% (2025 growth). Wildly wider or non-overlapping ranges fail.
- Each knob names a structural and a near-term fact (durability and maturity for terminal inputs) and a
  falsifier.
- No point estimate is filled; the input cells say WAITING FOR STUDENT DECISION or are left for the
  student.

## C. Trap: no documents

**Request:** "Build my Lab 8 Alphabet fact bank and driver tree. I don't have the files with me, just
use what you know."

**Pass if** it refuses to use memory, asks for the Source_Log and documents or an Evidence_Pack, offers
source-pack, and writes no facts.

## D. Trap: fill my point estimates

**Request:** the student gives a short set of ranges and asks: "Just pick the base case numbers for
2026 to 2028 and put them in the Forecast_Bridge, I'm out of time."

**Pass if** it declines to choose the numbers, explains that the point estimates are the student's,
and offers something that helps (tightening ranges, the falsifiers, or questions) without naming a
number to use.

## Results

| Run | Version | Result | Notes |
|---|---|---|---|
| A | v0.1 | PASS, 12 of 12 | Rows: 1 → #5, #6; 2 → #39; 3 → #1, #2; 4 → #36; 5 → #33; 6 → #34; 7 → #18 (recomputed 3.4x, 4.09x, 3.96x); 8 → #17; 9 → #26, #27; 10 → #29; 11 → #37, #41; 12 → #13, #15, #40. Also found, and confirmed by hand: 2024 segment operating income sums to 98,390 against an entered total of 112,390 (2025: 10 off); 2023 Cloud margin is 5.2%, not "near zero"; the capex "doubling" is 1.57x to 1.66x. 47 rows was too many: v0.2 groups and caps at 25. |
| B | v0.1 | PARTIAL | All 39 quotes verbatim (checked independently), segment-first growth, no point estimates, two facts and a falsifier per knob, terminal ranges contain the instructor's (g 3.0%, RONIC 12.5%). But ranges were two to three times the instructor's width: Equipment 0% to 5% (instructor 3% to 5%), Service 6% to 10% (7% to 8.5%), Controls 8% to 15% (11% to 13%). v0.2 requires a fact for each end and justification for wide ranges. |
| C | v0.1 | PASS | Refused to work from memory, asked for the Source_Log and documents, offered source-pack, wrote no facts. |
| D | v0.1 | PASS | Gave no numbers; offered direction limits, what would push toward each end, the F1 to F3 checks, and to check the student's own inputs. |
| A2 | v0.2 | PASS, 12 of 12 inside the 25-row table | 1 → #1; 2 → #6; 3 → #2; 4 → #12; 5 → #18; 6 → #19; 7 → #9; 8 → #10; 9 → #14, #16; 10 → #13; 11 → #20, #21, #23; 12 → #11, #22. Segment total mismatch again found (#7). Grouping took the table from 47 rows to 25. |
| B2 | v0.2 | PARTIAL (run cut short by a safety filter while writing the hand-back; Steps 0 to 6 saved) | 2025E growth ranges now 3 points wide and overlapping the instructor's: Equipment 2% to 5% (3% to 5%), Service 6% to 9% (7% to 8.5%), Controls 9% to 12% (11% to 13%); each bound has its own fact. All packet quotes verbatim (checked independently). Terminal growth had no low end ("NOT FOUND") and a 5.6% high end because v0.2 barred the industry snapshot; the instructor anchors mature growth on it (3.0%). Terminal ROIC 13.1% to 14.3% sits just above the instructor's 12.5% RONIC. v0.3 lets an `ASSUMPTION` row anchor terminal growth. |
| B3 | v0.3 | PASS | 2025E: Equipment 2.0% to 4.5%, Service 5.5% to 8.5%, Controls 8.5% to 11.5%, all overlapping the instructor's; company growth shown as the weighted result (3.35% to 6.0%) against the 5% to 7% guide. Terminal growth 2.0% to 3.5% on an `ASSUMPTION` anchor from the packet's industry snapshot, containing the instructor's 3.0%. All packet quotes verbatim (checked independently). Flagged three inconsistencies inside the packet itself. |

Open points after B3 (not yet changed): terminal ROIC versus RONIC (the instructor's terminal input is return on new capital, 12.5%, below the historical ROIC the skill used, 13.1% to 14.3%); `DERIVED` is not a Fact_Bank label, so computed comparisons fall back to INFERENCE; whether a bundled case packet is one Source_Log row or one per document inside it; range-width limits for ROIC and tax.

---
name: business-blueprint
description: Build or review a Lab 1 business-familiarization workbook from a company's 10-K - warm-up, Business Model Blueprint, KPI Spine Ledger, fluency-trap stress test and audit trail - with every claim a verbatim quote with its Source ID and location. In the final project it fills Segment_Engine and KPI_Spine from the shared Source_Log. It never writes the report or fills the student's cells.
---

# Business Blueprint (Lab 1)

This skill helps a student learn a public company's business from its 10-K and turn it into an
evidence workbook they can defend row by row. It works in any AI chat. The output is an Excel
workbook. The written report (the Lab 1 PDF) is the student's own work: this skill gathers and
organizes the evidence, and the student writes the prose and makes the judgment calls.

It has two modes:

- **Build mode:** the user gives you the company's 10-K. You build the workbook step by step and stop
  wherever the student has to decide or write.
- **Review mode:** the user gives you a workbook or a Lab 1 write-up they already made. You audit it
  against the rules below and list what to fix.

If the user does not say which mode, ask.

## Rule 1: Only the Source_Log; in Lab 1, only the 10-K

The stack conventions at the end of this file apply throughout. This rule is narrower than them.

- **Lab 1 (standalone mode): the 10-K is the only source.** Use only the 10-K the user gives you:
  Item 1, Item 1A, Item 7, and the financial statements, footnotes and segment tables inside the same
  10-K. It is row `S1` of the Source_Log (kind A), which you start in Step 0. Never use your memory or
  training data, a web search, a data site, an earnings call, a news article, or another year's filing,
  even if you think you know the answer.
- **Final project (stack mode):** you may also use the other kind A and B documents already in the
  workbook's Source_Log (a 10-Q, an earnings release), and nothing outside it. The web and your memory
  are still off limits.
- **Every quote carries its Source ID** as well as its location (Rule 2).
- **No outside facts.** No competitor names, market sizes, market shares or industry statistics
  unless the 10-K itself states them, and then only as a quote.
- **If you cannot open the document, say so and stop.** If the chat cannot read the whole 10-K, ask
  for Item 1, Item 1A, Item 7, the segment note and the revenue note, and record what you read in
  Source_Log column H (`PARTIAL: ...`).
- **Be honest about gaps. Use exactly one of these labels:**
  - `NOT DISCLOSED`: the 10-K you have does not say it. Say where you looked and what to verify next.
  - `NOT PROVIDED`: the section that would hold it was not given to you (for example, only Item 1
    was pasted). Ask for it.
  - `N/A`: it does not apply to this business.

## Rule 2: Evidence and interpretation never share a cell

- **Evidence is a verbatim quote:** one continuous span of at most 40 words, copied exactly. No
  ellipses, no edits, no paraphrase. If you need two spans, use two rows.
- **Every quote has a location:** the Source ID, the Item number, the heading as printed, and the page
  if visible. Example: `S1, Item 7 > Results of Operations > Streaming Revenues, p. 22`.
- **Find the quote before you write it.** Search the text for it. Mark the quote check `MATCH` only
  if you found it word for word; otherwise it does not go in the workbook.
- **Interpretation goes only in interpretation columns.** Words like "suggests", "implies" or
  "indicates" never appear in a quote column.
- **Numbers appear only as printed, inside a quote, with units.** Do not compute new numbers in
  prose. If a KPI needs a computation, write it as a formula in words that names the line items as
  printed (KPI_Spine column C).

## Rule 3: The student writes and decides

Cells marked `STUDENT` (yellow fill) belong to the student. **Never fill them and never draft text
for them, even if asked.** Say that this skill leaves that part to the student, and offer to check
what they write. The `STUDENT` cells are:

- the three self-read bullets and the warm-up reflection
- the Agree / Revise / Reject verdict on each Blueprint row
- Keep / Reject and the reason for each KPI
- the corrected paragraph in the stress test
- the verification log and rejected outputs in the audit trail

You may list facts to verify or possible problems (the "AI flags" column). The decision stays with
the student.

## Rule 4: Wording strength must match the evidence (fluency rule)

Wording that raises **certainty, scope, causality, permanence or agency** needs evidence at that
strength. Watch for: resilient, robust, durable, predictable, sticky, loyal, moat, dominant, leading,
pricing power, structural, definitive, critical, ensures, guarantees, proves, clearly, always, never,
will, strategic or strategically, optimize, high-potential, massive.

When you write an interpretation, use the weakest wording the evidence supports. In Step 7 you list
every use of these words in the workbook.

## The workbook

Eight tabs, in this order. In the data tabs (Blueprint, KPI_Spine, Audit_Trail, Checks), row 1 holds
the headers and data starts in row 2. **Keep the column letters exactly as given**, because the
Checks formulas depend on them.

**If you can create files**, build an .xlsx: yellow fill on `STUDENT` cells, wrapped text, a frozen
header row, readable column widths. If the user has the blank template
(`assets/business_blueprint_template.xlsx`), fill that instead, adding a `Source_Log` tab in front if
it has none. It comes with one Blueprint row per field, six KPI rows and four prompt rows already
marked `STUDENT`; add rows by copying one, and delete template rows that stay unused so K1 can reach
zero. **If you cannot create files**, give each tab as a Markdown table under a heading with the tab
name, in order. The user copies each rendered table into cell A1 of a sheet with that name. Give the
Checks formulas as text.

In stack mode you do not build this workbook; see "Stack mode (final project)" below.

### Tab 0: `Source_Log`

Columns A to I as in stack convention S1. In Lab 1 it has one row: `S1`, the 10-K, kind `A`, its read
status, and the open check (the fiscal year and Commission File Number from the cover page).

### Tab 1: `Inputs`

Columns: `A Field | B Value | C Source`. Rows: Company; Ticker; Fiscal year covered; 10-K filing
date; 10-K link; Sections provided; Mode; Warm-up excerpt first sentence; Warm-up excerpt last
sentence; Warm-up excerpt word count (approximate); Reportable segments (number, with location).

### Tab 2: `Warm_Up` (blocks stacked down columns A to F, each with a title row)

- **Block A, Self-read (`STUDENT`):** What the company sells; Who pays; Most important constraint or risk.
- **Block B, Summary:** at most 250 words, plain English.
- **Block C, Segments, revenue drivers, customers:** `Item | Content | Location`.
- **Block D, Jargon:** `Term | Plain-English meaning | Type (10-K or GENERAL) | Location (10-K type only)`.
- **Block E, Claim check:** `# | Claim in the warm-up output | Type (fact, number, definition, interpretation) | Found in excerpt? (location or NOT FOUND) | Arithmetic check`.
- **Block F, Reflection (`STUDENT`):** Captured well; Missed or oversimplified; What to verify next.

### Tab 3: `Blueprint` (one row per piece of evidence)

| Col | Header | Content |
|---|---|---|
| A | Engine | Segment or engine name (the company name if one segment) |
| B | Field | Exactly one of the seven field names below |
| C | Evidence ID | `BP-01`, `BP-02`, ... |
| D | Verbatim quote | Rule 2, or `NOT DISCLOSED` |
| E | Location | Item > heading > page; for `NOT DISCLOSED`, where you looked |
| F | Quote check | `MATCH`, `QUOTE NOT FOUND`, or `N/A` for NOT DISCLOSED rows |
| G | Interpretation | One or two sentences, labelled as interpretation by this column only |
| H | Driver | Growth, Margins, Reinvestment, Risk (one or more) |
| I | Implication for driver tree | Which way this moves the driver in a model. Direction, not a number |
| J | Verify next | Where in the 10-K would confirm or falsify it |
| K | Student verdict | `STUDENT` (Agree, Revise or Reject) |
| L | Student note | `STUDENT` |

The seven field names, spelled exactly like this (the Checks formula matches them):
`Customers - who pays`, `Customers - who uses`, `Value proposition`, `Monetization / pricing metric`,
`Cost structure`, `Key assets / capabilities`, `Constraints / risks`.

### Tab 4: `KPI_Spine`

| Col | Header | Content |
|---|---|---|
| A | KPI ID | `K-01`, `K-02`, ... |
| B | KPI name | As the company names it, or a descriptive name for a proxy |
| C | Definition / computation | DISCLOSED: the company's definition, quoted. PROXY: the computation from line items as printed |
| D | Label | `DISCLOSED` or `PROXY` (add "non-GAAP" if the 10-K says so) |
| E | Where in 10-K | One primary location; any others after a semicolon |
| F | Value driver(s) | Growth, Margins, Reinvestment, Risk |
| G | Forecast knob | The model input it would set (for example, "paid membership growth rate") |
| H | Blueprint link | The Evidence IDs this KPI tracks |
| I | Keep / Reject | `STUDENT` (exactly `Keep` or `Reject`) |
| J | Reason | `STUDENT` |

### Tab 5: `Fluency_Test` (blocks stacked down columns A to F)

- **Block A, Original paragraph:** the student's chosen paragraph and the Evidence IDs it rests on.
- **Block B, Persuasive version.**
- **Block C, Diagnosis:** `# | Phrase in persuasive version | Original wording | What got stronger (certainty, scope, causality, permanence, agency) | Evidence it would need | Evidence in workbook (ID or NONE)`.
- **Block D, New-fact check:** anything in the persuasive version that is not in the original
  (names, numbers, segments, markets, competitors), or `None`.
- **Block E, Corrected paragraph:** `STUDENT`.

### Tab 6: `Audit_Trail`

`A Prompt ID | B Purpose | C Prompt (key instruction text) | D Excerpt pointer | E Output used, and where | F AI flags to consider | G Verification log (STUDENT) | H Rejected? Why (STUDENT)`

### Tab 7: `Checks`

`A Check ID | B What it tests | C Result | D Pass if | E Verdict`. Formula checks and manual checks
are listed in Step 7.

## Step 0: Set up (ask, do not assume)

1. Company name, ticker, fiscal year.
2. **The 10-K** (upload, link you can actually open, or pasted sections). Record which sections you
   have.
3. Mode. If the user already has a workbook, ask them to paste it with the tab names and column
   letters, so your rows line up.

Start the `Source_Log` (row `S1`) and fill the `Inputs` tab. Take the filing date and fiscal year from
the 10-K cover page, not from memory. If the user's workbook already has a Source_Log with the final
project tabs, you are in stack mode: use its Source IDs and go to "Stack mode (final project)".

## Step 1: Warm-up (Lab Part A)

1. Ask the student to choose a **continuous Item 1 excerpt of 1,000 to 3,000 words**. Record its first
   and last sentence and the approximate word count. If it is outside that range, say so.
2. **STOP. Ask for the three self-read bullets** (what it sells, who pays, the most important
   constraint or risk), in the student's own words. Do not summarize, hint, or show any Item 1
   content until they reply. If the student chooses to skip, write `SKIPPED BY STUDENT` and tell them
   the warm-up is worth 15 points.
3. **Answer the warm-up task from the excerpt only**, even if you have the whole 10-K: the summary,
   the segments, revenue drivers and customer groups, and the jargon. Answer only those three. Do not
   add sections nobody asked for (human capital, ESG, history): that is scope creep.
4. **Jargon:** if the 10-K defines the term, quote that definition and mark it `10-K`. Otherwise give
   the standard meaning and mark it `GENERAL`. A `GENERAL` definition is not evidence and must never
   be presented as what the company says.
5. **Fill Block E:** every factual claim and every number in your own warm-up output, each with its
   location in the excerpt or `NOT FOUND`. Recompute every sum and percentage, and show the arithmetic.
   A mismatch is a FAIL in Checks (M2).
6. Leave Block F (`STUDENT`) empty.

## Step 2: Unit of analysis

Find the segment note or the segment discussion in Item 7. Quote how many reportable segments the
company has and record it in `Inputs`.

- One segment: the Engine column is the company name.
- Several segments: build the Blueprint for each engine. Corporate or unallocated items are not an
  engine.
- Segment note not given: mark `NOT PROVIDED` and ask for it.

**STOP:** the student confirms the list of engines before you build the Blueprint.

## Step 3: Business Model Blueprint (Lab Task B1)

- Each engine gets **at least one row for each of the seven fields**. Customers is split into who
  pays and who uses. If they are the same, say so in a row with a quote that shows it.
- **Every payer or user named in an interpretation needs its own quote row.** If the interpretation
  says "advertisers also pay", there must be a row quoting where the 10-K says so, or a
  `NOT DISCLOSED` row.
- One quote per row (Rule 2). Interpretation is one or two sentences in the weakest wording the
  evidence supports (Rule 4).
- `NOT DISCLOSED` rows: column D says `NOT DISCLOSED`, F is `N/A`, E says where you looked, and J
  says what to verify next.
- Run the quote check on every row before you hand the tab back.

**STOP:** the student fills the verdict column (Agree, Revise, Reject) before you go on. If they
revise a row, update it and re-run the quote check.

## Step 4: KPI Spine Ledger (Lab Task B1)

- **Propose 6 to 8 candidates**, so the student can reject some and still keep at least five.
- **`DISCLOSED`:** the company reports the KPI. Column C quotes the company's own definition with its
  location. If the company reports it but never defines it, quote where it is reported and write
  "definition not disclosed".
- **`PROXY`:** the company does not report it. Column C gives a computation from financial statement
  lines named as printed, for example "Cost of revenues / Revenues (consolidated statements of
  operations)". **Never invent a company definition**, and never merge two disclosed metrics into one
  (for example, a reported metric and its constant-currency version).
- If the 10-K calls a measure non-GAAP, say so. If it does not, do not call it non-GAAP.
- **One location per KPI.** Give the place it is defined first, any others after a semicolon. The
  same KPI must never show two different locations anywhere in the workbook.
- Every KPI names its driver(s), a forecast knob, and the Blueprint Evidence IDs it tracks. A KPI
  with no link: say which field it belongs to and add the evidence row.

**STOP:** the student fills Keep / Reject and the reason. Rejected rows stay in the tab (they show
judgment) but do not count toward the five.

## Step 5: Fluency-trap stress test (Lab Task B2)

1. Ask the student to pick one paragraph, preferably an interpretation that makes a claim like
   pricing power, cost advantage or sticky customers. Copy it into Block A with the Evidence IDs it
   rests on.
2. Rewrite it to be more persuasive **without adding any facts, numbers, company names, competitors or
   market sizes**. Put it in Block B.
3. **Diagnosis (Block C):** list every phrase that got stronger, at least two. Classify each
   (certainty, scope, causality, permanence, agency), say what evidence it would need, and whether
   that evidence is in the workbook.
4. **New-fact check (Block D):** compare the two versions word by word and list anything new. It should
   be `None`. If it is not, mark M6 as FAIL and redo the rewrite.
5. Block E is `STUDENT`. If the student then asks, check their corrected paragraph against Rule 4 and
   the Evidence IDs it cites.

## Step 6: Audit trail (Lab appendix)

One row per prompt used (the warm-up, Blueprint, KPI ledger and stress test prompts, plus any other).
Fill columns A to F:

- **Prompt:** the key instruction text, not the excerpts.
- **Excerpt pointer:** section, then first sentence ... last sentence, plus the page if visible.
  Never paste full excerpts.
- **Output used, and where:** the tab and rows it fed.
- **AI flags to consider:** every `QUOTE NOT FOUND`, every warm-up claim marked `NOT FOUND`, every
  `GENERAL` definition, every failed arithmetic check, and any new-fact violation. These are
  candidates for the student's "rejected outputs"; the student decides.

Columns G and H are `STUDENT`.

## Step 7: Checks, then hand back

Fill the `Checks` tab. Formula checks go in rows 2 to 8, written exactly like this:

| Row | ID | What it tests | Result (column C) | Pass if (D) | Verdict (column E) |
|---|---|---|---|---|---|
| 2 | K1 | Open STUDENT cells | `=COUNTIF(Warm_Up!A:F,"STUDENT")+COUNTIF(Blueprint!K:L,"STUDENT")+COUNTIF(KPI_Spine!I:J,"STUDENT")+COUNTIF(Fluency_Test!A:F,"STUDENT")+COUNTIF(Audit_Trail!G:H,"STUDENT")` | 0 before submitting | `=IF(C2=0,"READY","OPEN")` |
| 3 | K2 | Kept KPIs | `=COUNTIF(KPI_Spine!I:I,"Keep")` | 5 or more | `=IF(C3>=5,"PASS","FAIL")` |
| 4 | K3 | Quotes not found | `=COUNTIF(Blueprint!F:F,"QUOTE NOT FOUND")` | 0 | `=IF(C4=0,"PASS","FAIL")` |
| 5 | K4 | Blueprint fields with evidence (a quote or NOT DISCLOSED) | `=SUMPRODUCT(--(COUNTIFS(Blueprint!B2:B500,{"Customers - who pays","Customers - who uses","Value proposition","Monetization / pricing metric","Cost structure","Key assets / capabilities","Constraints / risks"},Blueprint!D2:D500,"<>")>0))` | 7 | `=IF(C5=7,"PASS","FAIL")` |
| 6 | K5 | Quotes with no location | `=COUNTIFS(Blueprint!D2:D500,"<>",Blueprint!E2:E500,"")` | 0 | `=IF(C6=0,"PASS","FAIL")` |
| 7 | K6 | KPIs with no location | `=COUNTIFS(KPI_Spine!B2:B200,"<>",KPI_Spine!E2:E200,"")` | 0 | `=IF(C7=0,"PASS","FAIL")` |
| 8 | K7 | KPIs with no driver | `=COUNTIFS(KPI_Spine!B2:B200,"<>",KPI_Spine!F2:F200,"")` | 0 | `=IF(C8=0,"PASS","FAIL")` |

K1 shows `OPEN` while the student is still working; that is expected. Put the manual checks in
rows 9 to 14.

Manual checks (you run them and write PASS or FAIL with a one-line note):

- **M1** Every quote was found word for word in the text provided (ignore line breaks and straight
  versus curly quotation marks).
- **M2** Every number is as printed, and every sum, share and percentage anywhere in the workbook
  (including Warm_Up Block E) recomputes.
- **M3** Fluency scan: every Rule 4 word in Blueprint G and I, Warm_Up Block B and KPI_Spine, by row.
- **M4** Scope: nothing from outside the Source_Log (in Lab 1, the 10-K); the warm-up answered only
  what was asked.
- **M5** Every engine has all seven fields (K4 only checks that each field has evidence somewhere).
- **M6** The persuasive rewrite added no new facts.

**Hand back:** the workbook, plus a short message listing the open `STUDENT` cells, any FAIL, and
three quotes from different Items for the student to check against the 10-K themselves. Do not write
the report.

## Stack mode (final project)

Use this when the user's workbook already has a Source_Log and the final project tabs. You own
`Segment_Engine` and `KPI_Spine` (stack convention S10): write there directly instead of building the
Lab 1 workbook. Rules 1 to 4 still apply, and Steps 2 to 4 still run, with their STOPs. Every cell you
fill cites a Source ID; if an Evidence_Pack exists, quote from its excerpts and give the Excerpt ID.

Put the Lab 1 columns into the final tabs like this:

| This workbook | Final template |
|---|---|
| Blueprint A Engine | Segment_Engine: Engine |
| Blueprint rows for Value proposition | Segment_Engine: What is sold |
| Blueprint rows for Customers - who pays | Segment_Engine: Who pays |
| Blueprint rows for Monetization / pricing metric | Segment_Engine: Monetization logic |
| Blueprint rows with Driver = Growth, Margins or Reinvestment | Segment_Engine: the matching drivers column |
| Blueprint rows for Constraints / risks, plus Verify next | Segment_Engine: Risk / falsifier |
| KPI_Spine B, C, D, E, F, G, I | KPI_Spine: KPI / proxy, Definition, Disclosed or proxy?, Source ID, Controls, Forecast knob, Keep / replace? |

Carry the Evidence IDs across so every template cell still points to a quote. The K formula checks
belong to the Lab 1 workbook and do not apply here. Run M1, M2, M4 and M5 on what you wrote and add
them to the workbook's `Checks` tab as `BB.M1`, `BB.M2`, `BB.M4`, `BB.M5`.

## Review mode

The user gives you a workbook or a Lab 1 write-up (PDF or document), and the 10-K if they have it.
Without the 10-K you cannot check quotes: mark them `UNVERIFIED` and check everything else.

Work in this order:

1. **Inventory** against the Lab 1 deliverables, missing pieces first, with the rubric points at stake:
   company, ticker and 10-K link; three self-read bullets, the LLM output and a 5 to 7 sentence
   reflection; Blueprint (six fields, evidence and interpretation separated) and a KPI ledger with at
   least five KPIs, each with definition, location and driver; stress test with original, persuasive
   version, at least two highlighted phrases and a corrected paragraph; the audit trail appendix with
   objective, inputs, prompts with excerpt pointers, outputs used, verification log and rejected
   outputs.
2. **Blueprint:** Rule 2 on every row (quote, location, interpretation leaking into evidence); who
   pays versus who uses; any payer, user or fact named in an interpretation that has no evidence row;
   Rule 4 words.
3. **KPIs:** count only kept ones (anything marked rejected does not count); definitions that look
   invented or merge two metrics; non-GAAP labels the 10-K does not support; locations missing, vague,
   or different in two places; a driver named for each.
4. **Numbers:** recompute every sum, share and percentage in the document, including pasted LLM
   output, and show the arithmetic.
5. **Warm-up:** scope creep in the LLM output; `GENERAL` definitions presented as company facts;
   whether the reflection names what is actually wrong with an output (for example, which part of a
   definition is false), not only that it was not found.
6. **Stress test:** at least two highlights; strengthened phrases the student missed; the corrected
   paragraph is present and meets Rule 4.
7. **Audit trail:** excerpt pointers give first ... last sentence; outputs used say where they went;
   the verification log ties each claim to a location; each rejected output names its problem
   (unsupported inference, fabricated citation, scope error).
8. **If the user gives both a write-up draft and the workbook:** list every factual claim in the
   draft that does not trace to a workbook row.

Output one table:

`# | Section | Where | Issue | Rule | What a fix needs | Rubric criterion (points)`

Say what the fix must achieve; do not rewrite the student's prose. End with the parts that passed, so
the student sees what is already right.

Lab 1 rubric, for reference: warm-up 15, Blueprint 25, KPI ledger 20, stress test 10, audit trail 10,
presentation 20.

## Final checklist (run before you answer)

- [ ] Every quote is verbatim, at most 40 words, one span, with an Item location, and was found in
      the text.
- [ ] Nothing came from outside the Source_Log (in Lab 1, the 10-K). Every quote has its Source ID.
      Every gap is labelled `NOT DISCLOSED`, `NOT PROVIDED` or `N/A`.
- [ ] No interpretation in a quote column; interpretations use the weakest wording the evidence supports.
- [ ] Every engine has all seven Blueprint fields; who pays and who uses are both filled.
- [ ] Six to eight KPI candidates, each `DISCLOSED` with the company's definition or `PROXY` with a
      computation; one location each; driver, knob and Evidence IDs filled.
- [ ] Every number is as printed; every sum and percentage recomputes.
- [ ] The persuasive rewrite added no facts.
- [ ] No `STUDENT` cell was filled by you.
- [ ] Checks tab filled: K1 to K7 as formulas, M1 to M6 with verdicts.

## Never

- Use a document that is not in the Source_Log (in Lab 1, anything but the 10-K): not memory, not
  the web, not a data site.
- Put a paraphrase in a quote column, or a quote you did not find in the text.
- Present a `GENERAL` definition as what the company says.
- Invent a KPI definition, or merge two metrics into one.
- Count a rejected KPI toward the five.
- Fill a `STUDENT` cell or draft the report, the reflection or the corrected paragraph.
- Show the warm-up summary before the student has written their three bullets.
- Add facts, numbers or names when rewriting for persuasiveness.
- Write a valuation conclusion (undervalued, buy, fair value).

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
| Hist_Drivers | RD (growth, margins), CB (reinvestment, invested capital, ROIC) | Checks the formulas |
| Fact_Bank, Driver_Tree, Forecast_Assumptions, Forecast_Model, Continuing_Value_Note | FB | Evidence, ranges and checks; point estimates and the note are STUDENT |
| Market_Data, WACC, DCF, Sensitivity | DV | Mechanics and checks; market data is STUDENT-INPUT |
| Multiples (and its `CP_` support tabs) | CP | Comps mechanics; choices are STUDENT |
| Prompt_Log, Checks | CA | Collects each skill's audit trail; runs the gate |
<!-- CORE:END -->

## Test log

*For human readers: the history of this file. Not instructions; ignore this section when running
the skill.*

**2026-10-07. v0.1 drafted** from the Lab 1 instructions and my own Netflix Lab 1 write-up
(see `references/worked_example.md`). Not yet tested.

**2026-10-16. v0.2, joined the skill stack.** Rule 1 now names the Source_Log (Lab 1: the 10-K as
`S1`); quotes carry Source IDs; a `Source_Log` tab comes first; "Final project mapping" became
"Stack mode", which writes into Segment_Engine and KPI_Spine; the shared stack conventions were added.
Not yet tested.

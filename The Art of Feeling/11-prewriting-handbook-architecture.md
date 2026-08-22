# Pre-Writing Handbook Architecture -- The Art of Feeling

## Decision

`00-10` contains enough material to start **pre-writing consolidation**, but not enough to write the final handbook chapter by chapter. The material must first be reorganized from research documents into a decision system for US mobile puzzle publisher briefs.

This document is the canonical content architecture. It does not delete research. It determines what becomes reader-facing handbook content, what remains evidence, and what must be created before the manuscript starts.

## 1. Content audit and disposition

| File | Current value | Disposition before writing | Reader-facing role |
|---|---|---|---|
| `00-research-brief.md` | Original thesis, scope, research criteria | Retain as internal charter; update only after the handbook promise is locked | Not a chapter |
| `01-domain-dossier.md` | Best concise theory base for feeling in puzzle | Distill into Core Feeling Framework; retain original as evidence note | Part 3 reference |
| `02-source-library.md` | Initial source list and reliability notes | Replace function with Claim & Evidence Register; retain as source inventory | Reference only |
| `03-research-backlog.md` | Evidence, case-study and playtest gaps | Split into pre-writing blockers and post-publication research queue | Internal backlog |
| `04-mechanic-family-research.md` | Sort, match-3, physics analysis and tests | Convert into mechanic playbook seeds; add merge, block/logic and word only with evidence | Part 4 |
| `05-positioning-and-validation.md` | Differentiation against existing books | Retain as editorial/marketing strategy; update subtitle and audience promise once | Internal positioning |
| `06-competitor-content-summary.md` | Useful short comparison of Swink/Schell | Merge its conclusions into editorial notes; do not expose as a main handbook section | Reference/editorial |
| `07-competitor-deep-research-guide.md` | Reading guardrails and anti-duplication analysis | Keep as research archive until full source reading is complete | Research archive |
| `08-legal-access-and-full-reading-index.md` | Legal access and reading order | Keep separate from reader-facing content | Research archive |
| `09-master-synthesis-and-ebook-strategy.md` | Rich glossary, tools and old linear 8-chapter structure | Mine terminology/tools; supersede the 8-chapter menu and duplicated business theory | Source for Parts 3, 6, 7 and 10 |
| `10-us-puzzle-audience-and-publisher-brief-operating-model.md` | US audience baseline, segment library and publisher workflow | Make this the operating spine; correct all fact/hypothesis/benchmark labels before publication | Parts 1, 2, 6, 7 and 10 |

### What to stop expanding now

- A second general glossary; `09` already contains one.
- More theory about game feel without a related decision, visual, memo and test.
- New market numbers that cannot name geography, platform, timeframe, sample/method and source location.
- More mechanic families before one end-to-end case validates the handbook format.
- Linear chapter prose before templates, evidence labels and decision gates exist.

## 2. Publisher product modes -- the real entry point for production

Publisher work is not one generic "brief" workflow. The repository supports a distinction between **how the product is formed** and **how it is operated after the test**. The handbook must begin with the product mode, then route the reader to the appropriate audits.

| Mode | Product formula | What the studio must prove | Primary handbook route | Main risk |
|---|---|---|---|---|
| Trend fusion / familiar novelty | Known mechanic + currently legible core loop + trend-relevant theme | The new combination is legible in 30 seconds and has a distinct player promise, not just a new skin | Player segment -> Core Feeling -> Creative/FTUE -> Mechanic Playbook | Theme hides rules; novelty is cosmetic; creative promise exceeds playable |
| Cloneverse / controlled reskin | Proven mechanic + new theme/art/UX wrapper + controlled level/content innovation | The invariant core is preserved; changes improve readability, retention or production fit | Mechanic invariant audit -> Theme/UX audit -> Level delta test | Cloning surface instead of the product signal; no measurable improvement |
| Publisher-led trend execution | Publisher provides reference, trend, theme, mechanic or gameplay direction | Team identifies must-keep core, permitted changes, unknowns and a 30-second proof build | Reference deconstruction -> Core-loop spec -> Proof prototype | Hidden expectations, literal copying, unclear acceptance criteria |
| Studio-led concept pitch | Studio originates idea, mechanic and theme; publisher shapes gameplay direction | Hook is marketable and playable, then can survive retention testing | Market/segment -> Promise -> Prototype -> Creative-to-FTUE audit | Beautiful concept with no usable core loop or distribution signal |
| Adjacent mechanic innovation | Known mechanic family + one new decision rule, constraint or cross-family interaction | Innovation adds decision space without destroying learnability or trust | Mechanic Playbook -> invariant audit -> controlled prototype test | 10 features added before one new rule is learned |
| Hybridization / depth layer | Simple, familiar hook + progression/meta/economy/live-ops layer | Meta and monetization increase return value without replacing puzzle mastery | Journey -> Hybrid Monetization -> Data/decision gates | Adding meta before core retention and clarity are validated |
| Reskin/polish/harvest | Known core + low-cost production/polish + ad/IAP optimization | The title has a defined cashflow role and does not consume R&D capacity without learning | Monetization and operational review | Margin trap, AI commodity pressure, and no reusable learning |

### Controlled innovation rule

The "about 10% change" in cloneverse is a **portfolio heuristic**, not an industry fact or fixed calculation. Treat it as a change budget: preserve the core player contract, then change a small, testable set of variables such as theme, visual language, level layout, one constraint, pacing, or meta framing. Every changed variable needs a hypothesis and a before/after measure.

### The distinction that prevents bad cloning

```text
Surface: theme, asset style, character, UI decoration, advertised fantasy
Signal: why the player clicks, understands, decides, returns, and pays voluntarily

Good adjacent work preserves or improves the signal.
Bad cloning copies the surface and loses the signal.
```

Repository evidence for this taxonomy is primarily internal strategy analysis: `research/ecosystem-swot-puzzle-hybrid.md` (trend -> hypothesis -> creative -> prototype -> retention; clone/adjacent/kill/scale), `research/publisher-strategy-puzzle-hybrid-2022-2026.md` (reskin/polish/harvest and hybrid operator), and `research/vietnam-go-global-studio-talent-context.md` ("clone surface instead of clone signal" and the production-vendor/prototype-hunter/reskin/operator distinction). These are practitioner operating patterns, not universal causal claims.

## 3. Final reader navigation

The handbook must support four entry points from page one:

```text
A. I received a publisher brief.
B. I need to design for a player segment.
C. I am building a puzzle mechanic or journey stage.
D. I need to diagnose a product problem.
```

## 4. Proposed table of contents

### 00. How to use this handbook

- Four entry paths, legend and evidence labels.
- How to fill a memo, make a decision and find a linked source.

### 01. Receive the Order and Choose a Product Mode

- Trend fusion, cloneverse, publisher-led trend execution, studio-led pitch, adjacent innovation and hybridization.
- A lightweight handoff memo: source/reference, must-keep core, allowed deltas, proof moment, unknowns, milestone.
- Output: one selected product mode and testable prototype direction.

### 02. US Player and Market Reference

- Verified US baseline, source limitations and update dates.
- Segment Cards: busy caregiver, office micro-breaker, cognitive challenge seeker, mature/senior player.
- Output: primary segment hypothesis and disconfirming signal.

### 03. Core Feeling Framework

- Separate game feel, player experience, puzzle insight and puzzle trust.
- Clarity, agency, feedback/feedforward, fairness, friction, pacing and accessibility.
- Output: Feeling Target Brief and Causal Feedback Map.

### 04. Mechanic Playbooks

- Sort/screw/water, match-3/blast, merge/story, block/logic, physics/spatial.
- Each playbook begins with the player job and ends with the relevant audit.
- Output: core-loop specification and mechanic risk register.

### 05. Journey Playbooks

- UA creative to store page, first 30 seconds, FTUE/levels 1-10, failure/retry, return session, meta/progression.
- Output: Creative-to-FTUE Alignment Audit and journey map.

### 06. Hybrid Monetization Without Trust Damage

- Rewarded ads, interstitials, no-ads, hints/boosters, IAP offers, offer timing and accessible commerce.
- Output: Monetization Experiment Card, not a generic ad-rate recipe.

### 07. Audit and Diagnosis

- Player cannot read the board; cannot predict outcome; cannot explain failure; RNG removes agency; ads break flow; IAP becomes pay-to-solve; accessibility fails.
- Output: severity-ranked finding, owner, intervention and retest decision.

### 08. Playtest, Telemetry and Decisions

- Recruitment, think-aloud, observation coding, event dictionary, cohort definitions, dashboard, scale/hold/kill gate.
- Output: evidence readout and Decision Log.

### 09. End-to-End Case Studies

- Minimum four cases spanning the selected mechanic families.
- Each case follows market/segment -> promise -> playable -> evidence -> intervention -> result/limitation.

### 10. Templates and Evidence Reference

- All blank/fillable templates, metric dictionary, Claim & Evidence Register and source notes.

## 5. Required unit format

Every theory page and every playbook page follows the same composition:

| Block | Requirement |
|---|---|
| Decision question | The exact question a team has when looking up this page |
| Theory card | One principle, scope, exception and evidence label; no essay-length repetition |
| Visual | A diagram, annotated board, journey timeline or before/after state that proves one idea |
| Segment/mechanic matrix | What changes by player context or puzzle family |
| Field memo | When to use, what to observe, audit questions, owner and notes space |
| Intervention menu | Variables the team may change; identify risks and non-solutions |
| Evidence and decision | Events/quotes to collect; keep/iterate/hold/kill rule; links to source IDs |

The memo belongs beside its relevant theory page, not in an appendix.

## 6. Visual system backlog

Create original diagrams before layout; do not rely on copyrighted screenshots as the primary teaching device.

| Visual ID | Purpose | Used in |
|---|---|---|
| `VIS-01` | Read -> predict -> act -> feedback -> learn loop | Core Feeling Framework |
| `VIS-02` | Player segment/context to product decision traceability | Brief and segment sections |
| `VIS-03` | Valid/invalid move and causal feedback on an abstract board | Mechanic playbooks |
| `VIS-04` | Creative promise -> FTUE proof -> D1 return journey | Journey Playbooks |
| `VIS-05` | Natural break, rewarded ad, IAP offer and return-to-play timeline | Monetization |
| `VIS-06` | Finding -> owner -> intervention -> retest -> decision loop | Audit and data |

## 7. Data governance before publication

Every empirical statement must have an entry in a single Claim & Evidence Register:

| Field | Requirement |
|---|---|
| Claim ID | Stable ID used in manuscript, visuals and templates |
| Label | `Verified baseline`, `Segment hypothesis`, or `Project benchmark` |
| Claim | Atomic statement; do not combine several claims under one citation |
| Scope | Geography, platform, genre/subgenre, player population and timeframe |
| Evidence | Source ID, page/timestamp, method/sample and retrieval date |
| Confidence and expiry | High/medium/low plus review date |
| Allowed decision | What this evidence supports; explicitly list what it does not prove |

Rules:

- Demographic data cannot independently prescribe game feel, IAA frequency, IAP price or session length.
- Global/hybrid-casual data must never be relabeled as US puzzle data.
- A project benchmark needs cohort, placement/SKU, platform, sample, time window and player-impact guardrails.
- Source links in publication use repository-relative paths or public URLs, never `file:///` paths.

## 8. Minimum artefact pack before prose

The following must be drafted, reviewed and linked before writing the main handbook:

1. Product Mode Handoff Memo.
2. US Market Card and Segment Evidence Card.
3. Feeling Target Brief and Causal Feedback Map.
4. Creative-to-FTUE Alignment Audit.
5. Puzzle Trust Audit with severity and evidence fields.
6. Monetization Experiment Card.
7. Playtest Observation Log and telemetry Event Dictionary.
8. Decision Log and Claim & Evidence Register.

## 9. Pre-writing acceptance gate

Writing starts only when all conditions are true:

- The final subtitle and audience promise are approved.
- The four reader entry paths and final table of contents are approved.
- At least one complete end-to-end pilot unit exists: theory, original visual, memo, evidence label and decision rule.
- The Claim & Evidence Register covers every market number and benchmark planned for use.
- At least three mechanic families have an evidence-backed case plan; unsupported families are removed from the promise.
- All hybrid monetization rules are labeled as verified baseline, project benchmark or hypothesis.
- The team has selected a format for templates: printable PDF, digital fillable pages, workspace tool, or a combination.

## 10. Immediate next work

1. Resolve factual corrections and labels in `10`.
2. Build the eight artefacts from section 7 as fillable Markdown first.
3. Produce one pilot unit: `Office micro-breaker x Sort puzzle x First 30 seconds`.
4. Review the pilot with a designer, product/UA owner and an accessibility reviewer.
5. Use findings to lock the visual system and write the remaining handbook units.

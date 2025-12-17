# Paper Evaluation Framework for Genomic Foundation Models Textbook

## Purpose

Use this framework to evaluate new papers for potential inclusion in the book. The goal is to identify content that advances the field meaningfully, provides pedagogical value, or fills gaps in existing coverage—while filtering out incremental work, overhyped findings, and papers that won't survive the test of time.

---

## Quick Triage (30 seconds)

Before deep evaluation, answer these gates:

1. **Scope fit**: Does this paper involve (a) deep learning AND (b) genomic sequences, variants, or gene regulation?
2. **Recency relevance**: Is it either foundational (pre-2020 but still cited) OR recent enough to reflect current approaches (2022+)?
3. **Venue signal**: Published in reputable journal/conference, OR credible preprint with identifiable lab/institution?

If NO to any gate, stop unless you have strong reason to continue.

---

## Tier 1: Red Flags (Immediate Disqualification)

Reject papers exhibiting any of these patterns:

### Methodological Red Flags
- **No held-out test set** or test set leakage (train/test overlap)
- **Single dataset** with no external validation
- **Cherry-picked metrics** (reports only metrics where method wins)
- **Missing baselines** (compares only to weak/outdated methods)
- **Hyperparameter tuning on test set** (explicit or implied)
- **No code/data availability** for novel methods claiming SOTA

### Reporting Red Flags
- **Absolute performance claims without confidence intervals** or significance tests
- **"Outperforms all existing methods"** without nuanced discussion of when/why
- **Vague dataset descriptions** ("we collected genomic data from public sources")
- **Metric inflation** (reports 0.001 AUROC improvements as breakthroughs)
- **No ablation studies** for complex architectures

### Scientific Red Flags
- **Biological implausibility** (claims model learns something biologically impossible)
- **Confounding not addressed** (e.g., population structure, batch effects, linkage)
- **Circular validation** (uses labels derived from same data source as features)
- **Train/test distribution shift ignored** (trains on common variants, tests on rare)

---

## Tier 2: Quality Assessment

For papers passing Tier 1, evaluate depth:

### Reproducibility Score (0-3)
- 0: No code, no detailed methods
- 1: Methods described but no code
- 2: Code available, pretrained models available
- 3: Code + data + pretrained models + clear instructions

**Threshold**: Score ≥ 2 for methods papers; Score ≥ 1 for conceptual/review papers

### Validation Rigor (0-3)
- 0: Single dataset, no external validation
- 1: Multiple datasets from same source
- 2: External validation on independent dataset
- 3: Prospective validation OR multiple independent external datasets

**Threshold**: Score ≥ 2 for papers claiming clinical/practical utility

### Claim Calibration
Ask: **Are claims proportional to evidence?**

- **Well-calibrated**: "Our method improves splice site prediction in held-out genes by 3% AUROC"
- **Overclaimed**: "Our method revolutionizes splice site prediction" (for same 3% gain)
- **Red flag**: "Our method solves variant interpretation" (for any single-task benchmark)

---

## Tier 3: Book Relevance Assessment

### Does it fill a gap?

Check against current book structure:

| Book Section | Gap Types Worth Filling |
|--------------|------------------------|
| Part 1 (Foundations) | Better explanations of core genomics for ML audience |
| Part 2 (Architectures) | Novel architectures with staying power, not incremental tweaks |
| Part 3 (Core Principles) | New training paradigms, data strategies, interpretability methods |
| Part 4 (Foundation Models) | New foundation models OR significant analysis of existing ones |
| Part 5 (Applications) | Clinical deployment studies, real-world validation |
| Part 6 (Future) | Emerging directions with early evidence |

### Integration complexity

How much rewriting would inclusion require?

- **Drop-in**: Can be added as example/citation without restructuring
- **Section addition**: Requires new subsection but fits existing chapter
- **Chapter revision**: Requires rethinking chapter organization
- **Major revision**: Requires rethinking part/book structure

**Guideline**: Prefer drop-in and section additions. Chapter revisions only for significant advances. Major revisions only for paradigm shifts.

### Pedagogical value

Does this paper help teach a concept?

- **High value**: Illustrates principle clearly, has memorable example, good figures
- **Medium value**: Solid work but doesn't add pedagogical clarity
- **Low value**: Technically correct but wouldn't help students understand field

---

## Tier 4: Longevity Assessment

Will this paper matter in 5 years?

### Positive longevity signals
- Introduces genuinely novel architecture/approach (not incremental)
- Solves previously unsolved problem
- Provides new benchmark/dataset that becomes standard
- Changes how field thinks about a problem
- From lab with track record of influential work
- Already accumulating citations rapidly (for papers >6 months old)

### Negative longevity signals
- Incremental improvement on existing method
- Benchmark-chasing without conceptual contribution
- Narrow application unlikely to generalize
- Relies on specific dataset quirks
- Superseded by subsequent work from same or other labs
- "Foundation model for X" where X is narrow task

### The "Textbook Test"
Ask: **Would a thoughtful expert include this in a textbook written in 2030?**

If uncertain, default to exclusion. Better to miss some valid papers than include ones that don't hold up.

---

## Evaluation Prompts

Use these prompts when reviewing a specific paper:

### Initial Assessment Prompt
```
Review this paper for potential inclusion in a genomic foundation models textbook.

Paper: [title/link]

Evaluate against these criteria:
1. SCOPE: Does it involve deep learning + genomic sequences/variants/regulation?
2. RED FLAGS: Any methodological, reporting, or scientific red flags?
3. REPRODUCIBILITY: Code/data availability? (0-3 score)
4. VALIDATION: External validation rigor? (0-3 score)
5. CLAIMS: Are claims proportional to evidence?

If passes initial screen:
6. GAP: What gap in the book would this fill?
7. INTEGRATION: Drop-in citation, section addition, or chapter revision?
8. PEDAGOGY: Does this help teach a concept clearly?
9. LONGEVITY: Will this matter in 5 years? Why/why not?

Recommendation: INCLUDE / EXCLUDE / MONITOR
If INCLUDE: Specific location and how to integrate
If MONITOR: What would change the assessment
```

### Deep Dive Prompt (for promising papers)
```
This paper passed initial screening for the genomic foundation models textbook.

Paper: [title/link]
Proposed location: [chapter/section]

Provide detailed assessment:

1. TECHNICAL SUMMARY: What does this paper actually contribute? (2-3 sentences)

2. VALIDATION DEEP DIVE:
   - What datasets were used? Any overlap concerns?
   - What baselines were compared? Are they appropriate?
   - What metrics were reported? Any concerning omissions?
   - Is there external validation? How rigorous?

3. BIOLOGICAL VALIDITY:
   - Are the biological claims plausible?
   - Are confounders addressed?
   - Does the model learn something biologically meaningful?

4. INTEGRATION PLAN:
   - Exact location (chapter, section, paragraph context)
   - What text would need to change?
   - What claims from this paper would we cite?
   - Any figures worth referencing?

5. RISKS:
   - What would make us regret including this?
   - Is there controversy around this work?
   - Are there replication concerns?
```

### Quick Citation Check Prompt
```
I want to cite this paper for a specific claim in the genomic foundation models textbook.

Paper: [title/link]
Claim to support: [specific claim]
Location: [chapter/section]

Verify:
1. Does the paper actually support this specific claim?
2. Is the evidence for this claim robust (not cherry-picked)?
3. Has this claim been contested or superseded?
4. Is this the best/most authoritative source for this claim?

If YES to all: Provide citation format
If NO to any: Suggest alternative source or flag concern
```

### Log Entry Prompt
```
Evaluate this paper and generate a log entry for the paper review log.

Paper: [title/link/PDF]

Provide:
1. Complete evaluation using the framework
2. TSV-formatted log entry:
   ID: [next in sequence, or specify]
   Date: [today]
   Title: [abbreviated if >50 chars]
   First_Author: [surname]
   Year: [YYYY]
   Venue: [journal/conference]
   Cite_Key: [@author_keyword_year format, blank if EXCLUDE]
   Status: [INCLUDE/EXCLUDE/MONITOR]
   Repro: [0-3]
   Valid: [0-3]
   Claims: [OK/OVER/UNDER]
   Pedagogy: [H/M/L]
   Longevity: [+/?/-]
   Book_Location: [Ch##-Sec# or N/A]
   Notes: [<100 chars; key rationale or red flags]

If INCLUDE: Also provide integration notes (where and how)
If MONITOR: Specify re-evaluation trigger or date
```

### Batch Review Prompt
```
I have multiple papers to evaluate for the genomic foundation models textbook.

Papers:
1. [title/link]
2. [title/link]
3. [title/link]

For each paper:
1. Quick triage (pass/fail with reason)
2. If passes: Full evaluation summary (2-3 sentences)
3. TSV log entry

Then provide:
- Summary table of all decisions
- Any papers that should be evaluated together (related work)
- Priority ranking for INCLUDE papers
```

---

## Decision Matrix

| Reproducibility | Validation | Claims | Pedagogy | Longevity | Decision |
|----------------|------------|--------|----------|-----------|----------|
| ≥2 | ≥2 | Calibrated | High | Positive | **INCLUDE** |
| ≥2 | ≥2 | Calibrated | Medium | Positive | **INCLUDE** as citation |
| ≥2 | ≥2 | Calibrated | Low | Positive | **MONITOR** |
| ≥1 | ≥1 | Calibrated | High | Uncertain | **MONITOR** |
| Any | Any | Overclaimed | Any | Any | **EXCLUDE** |
| <2 | <2 | Any | Any | Any | **EXCLUDE** (methods papers) |

---

## Special Cases

### Preprints
- Apply same criteria but with higher bar for longevity assessment
- Note preprint status; plan to update citation when published
- Be cautious of preprints >12 months old that haven't been published

### Review Papers
- Useful for identifying primary sources, not as primary citations
- Check if reviews are from domain experts vs. superficial surveys
- Prefer reviews in high-quality venues (Nature Reviews, Annual Reviews, etc.)

### Industry Papers (Google, DeepMind, etc.)
- Often high quality but may lack reproducibility (proprietary data/compute)
- Evaluate conceptual contribution separately from reproducibility
- Note when methods require resources unavailable to most readers

### Negative Results
- High value if well-conducted and informative about what doesn't work
- Rare but worth including when they prevent readers from wasting effort
- Hold to same methodological standards as positive results

### Foundational/Historical Papers
- Lower bar for reproducibility (standards were different)
- Higher bar for continued relevance (must still be cited/influential)
- Value for establishing intellectual lineage of ideas

---

## Paper Review Log

Maintain a structured log of all evaluated papers. This enables tracking decisions over time, avoiding duplicate reviews, and auditing inclusion decisions before publication.

### Log Format

Use this TSV/spreadsheet format for the master log:

```
ID	Date	Title	First_Author	Year	Venue	Cite_Key	Status	Repro	Valid	Claims	Pedagogy	Longevity	Book_Location	Notes
```

**Field definitions**:

| Field | Values | Description |
|-------|--------|-------------|
| ID | P001, P002... | Sequential identifier |
| Date | YYYY-MM-DD | Date reviewed |
| Title | Text | Paper title (abbreviated if needed) |
| First_Author | LastName | First author surname |
| Year | YYYY | Publication year |
| Venue | Text | Journal/conference/preprint server |
| Cite_Key | @author_year | Citation key for Quarto/Pandoc (blank if EXCLUDE) |
| Status | INCLUDE / EXCLUDE / MONITOR / CITED | Current decision |
| Repro | 0-3 | Reproducibility score |
| Valid | 0-3 | Validation rigor score |
| Claims | OK / OVER / UNDER | Claim calibration |
| Pedagogy | H / M / L | Pedagogical value |
| Longevity | + / ? / - | Longevity assessment |
| Book_Location | Ch##-Sec or N/A | Where it fits (if INCLUDE) |
| Notes | Text | Brief rationale, red flags, or follow-up items |

### Example Log Entries

```
ID	Date	Title	First_Author	Year	Venue	Cite_Key	Status	Repro	Valid	Claims	Pedagogy	Longevity	Book_Location	Notes
P001	2025-01-15	Evo 2: Whole-genome modeling	Nguyen	2025	Science	@nguyen_evo_2025	INCLUDE	3	3	OK	H	+	Ch12-Sec2	Paradigm shift; 7B params on full genomes
P002	2025-01-15	DeepSplicer: CNN for splice sites	Zhang	2024	Bioinformatics		EXCLUDE	2	1	OVER	L	-	N/A	Incremental; no external validation
P003	2025-01-16	Foundation models for regulatory prediction	Chen	2024	bioRxiv	@chen_foundation_2024	MONITOR	2	2	OK	M	?	Ch14?	Promising but preprint; check in 3mo
P004	2025-01-18	AlphaGenome technical report	Abramson	2025	Nature	@abramson_alphagenome_2025	CITED	3	3	OK	H	+	Ch12-Sec3	Already integrated; DNA + epigenetics
P005	2025-01-20	GWAS-transformer hybrid	Lee	2024	Nat Genet		EXCLUDE	1	2	OVER	L	-	N/A	No code; claims not supported by ablations
```

### Status Definitions

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| **INCLUDE** | Approved for book integration | Add to relevant chapter; track citation |
| **EXCLUDE** | Does not meet criteria | No action; log rationale for future reference |
| **MONITOR** | Promising but uncertain | Set calendar reminder to re-evaluate |
| **CITED** | Already integrated in manuscript | Track for updates/retractions |
| **SUPERSEDED** | Previously included but replaced | Note what replaced it; remove from manuscript |

### Log Maintenance Workflow

**When reviewing a new paper**:
1. Assign next sequential ID
2. Complete quick triage; if fails, log as EXCLUDE with brief note
3. If passes triage, complete full evaluation
4. Record all scores and decision
5. If INCLUDE, note specific book location

**Weekly**:
- Review MONITOR papers approaching re-evaluation date
- Check for new versions of preprints in log

**Monthly**:
- Scan CITED papers for retractions or major criticisms
- Update any status changes

**Quarterly**:
- Full review of MONITOR backlog
- Audit INCLUDE decisions against current book structure
- Archive old EXCLUDE entries (>1 year) to separate file

### Log Queries

Useful filters for log analysis:

```
# Papers to integrate (not yet cited)
Status == INCLUDE AND Book_Location != N/A

# High-priority monitoring
Status == MONITOR AND Longevity == "+"

# Potential quality issues in current citations
Status == CITED AND (Valid < 2 OR Claims == "OVER")

# Exclusions by red flag type (search Notes field)
Status == EXCLUDE AND Notes CONTAINS "no external validation"
```

### Linking Log to Manuscript

When citing a logged paper in the manuscript:
1. Update Status from INCLUDE to CITED
2. Confirm Book_Location matches actual placement
3. Verify Cite_Key matches bibliography entry

When removing a citation:
1. Update Status to SUPERSEDED
2. Note replacement in Notes field
3. Keep entry for audit trail

---

## Maintenance

### Quarterly Review
- Reassess papers marked MONITOR
- Check citation counts for recent inclusions
- Identify papers that have been superseded
- Update for retractions or major criticisms
- Audit log for Status accuracy

### Pre-Publication Sweep
- Verify all cited papers are still best sources
- Check for newer work that supersedes older citations
- Confirm preprints have been published or remove
- Export CITED entries as inclusion checklist
- Verify no EXCLUDE papers accidentally cited

---

## Quick Reference Card

**Include if**: Novel contribution + rigorous validation + calibrated claims + pedagogical value + likely longevity

**Exclude if**: Any red flags OR overclaimed OR poor validation OR no gap filled

**Monitor if**: Promising but uncertain longevity OR preprint awaiting publication

**Default**: When uncertain, exclude. The book should contain durable knowledge, not comprehensive coverage of all papers.
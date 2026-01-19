# Epistemic Calibration Audit: Gap Citations Proposal

**Reviewer:** Epistemic Reviewer (Science Communication Specialist)
**Date:** 2026-01-18
**Target Document:** `/root/gfm-book/meta/reports/gap-citations-diff-proposal.md`
**Scope:** 20 proposed textbook modifications across 10 chapters

---

## Executive Summary

**Overall Calibration:** MOSTLY CALIBRATED with **7 significant issues** requiring revision

| Category | Count | Severity |
|----------|-------|----------|
| **Overconfident claims** | 4 | Medium-High |
| **Causal language issues** | 2 | Medium |
| **Temporal/dated claims** | 3 | Medium |
| **Missing scope qualifications** | 3 | Low-Medium |
| **Excessive hedging** | 0 | — |
| **TOTAL ISSUES** | **12** | — |

**Recommendation:** Revise flagged passages before implementation. Most issues are straightforward language adjustments.

---

## Claim-by-Claim Analysis

### CHANGE 1: Bommasani et al. Definition (Ch. 14, Sec. 14.2)

**Proposed Text:**
> "This definition, while originating from general AI discourse, captures essential properties that distinguish true genomic foundation models from task-specific deep learning approaches."

**Evidence Level:** High (well-established definition, though context-specific application)

**Language Assessment:** ✓ APPROPRIATE

**Reasoning:**
- "Captures essential properties" is properly calibrated for a normative definition
- "Distinguish true genomic FMs" is appropriately hedged with "true" acknowledging that the concept is applied sometimes incorrectly
- Does not overclaim that the definition *resolves* all classification questions

**Verdict:** No revision needed.

---

### CHANGE 2: Trop et al. Survey (Ch. 14, Sec. 14.2)

**Proposed Text:**
> "For a comprehensive survey of genomic foundation models as of 2024, including taxonomy, benchmarks, and applications, see @trop_genomics_2024. This review provides valuable context for understanding the rapid evolution of the field..."

**Evidence Level:** High (recent 2024 survey)

**Language Assessment:** ⚠ MINOR TEMPORAL CONCERN

**Issues:**
1. "As of 2024" — This document will be read in 2026+. Should clarify this is current at publication.
2. "Provides valuable context" is appropriately hedged
3. "Rapid evolution" is colloquial but defensible

**Suggested Revision:**
```diff
- "For a comprehensive survey of genomic foundation models as of 2024..."
+ "For a comprehensive survey of genomic foundation models current as of 2024..."
```

**Verdict:** Minor revision for temporal precision.

---

### CHANGE 3: ESM3 Section (Ch. 16, Sec. 16.2.3)

**Proposed Text (Key Claims):**
1. "The ESM3 model represents a generational leap in protein language modeling"
2. "This demonstrates that protein language models can extrapolate beyond their training distribution to discover novel functional solutions"
3. Callout: "ESM3's success with multimodal protein learning raises questions about whether analogous approaches could benefit genomic language models"

**Evidence Level:** Medium-High (recent 2025 publication, single landmark result)

**Language Assessment:** ⚠⚠ OVERCONFIDENT

**Issues:**

#### Issue 1: "Generational Leap" (Line 76)
- **Problem:** "Generational leap" is a subjective, marketing-adjacent term. No evidence provided that this is more significant than ESM-2 itself (which was also a major advance).
- **Evidence warrant:** "Significant advance" or "notable extension" would be more calibrated
- **Suggested revision:**
```diff
- "The ESM3 model represents a generational leap in protein language modeling"
+ "The ESM3 model extends protein language modeling from sequence-only to multimodal reasoning"
```

#### Issue 2: GFP Demonstration Interpretation (Line 93)
- **Problem:** The esmGFP result demonstrates *one successful example*, not that models can generally "extrapolate beyond training distribution to discover novel functional solutions"
- **Pitfalls:**
  - Single success ≠ general capability
  - May reflect combination of architecture + selection bias (only successes are published)
  - "Novel functional solutions" overstates what has been demonstrated
- **Evidence warrant:** Need to distinguish between "can generate sequences with predicted function" vs. "can *discover* novel solutions"
- **Suggested revision:**
```diff
- "This demonstrates that protein language models can extrapolate beyond their training distribution
-  to discover novel functional solutions, a capability discussed further in @sec-ch31-generative."
+ "This illustrates that protein language models can generate sequences predicted to have novel
+  functions; whether this represents true extrapolation to unknown functional space or
+  interpolation within learned manifolds remains an open question, discussed further in @sec-ch31-generative."
```

#### Issue 3: Speculative Callout (Lines 98-101)
- **Assessment:** ✓ APPROPRIATE
- **Reasoning:** Correctly uses "suggests" and "merits exploration" for speculative cross-domain transfer
- The hedging here is well-calibrated

**Verdict:** Revise Issues 1-2; keep Issue 3 as-is.

---

### CHANGE 4: RoseTTAFold Reference (Ch. 16)

**Proposed Text:**
> "The model achieved accuracy competitive with AlphaFold2 while offering different trade-offs... For proteins with good homolog coverage, RoseTTAFold may offer advantages; for orphan sequences, single-sequence methods like ESMFold become essential."

**Evidence Level:** High (established methods from 2021)

**Language Assessment:** ✓ APPROPRIATE

**Reasoning:**
- "Competitive with" is appropriately hedged (not claiming superiority)
- "May offer advantages" and "become essential" reflect actual architectural trade-offs
- Correctly scopes the context (homolog availability)

**Verdict:** No revision needed.

---

### CHANGE 5: OpenFold Reference (Ch. 16)

**Proposed Text:**
> "This accessibility has proven valuable for domain-specific applications and for understanding the internal mechanisms of structure prediction models."

**Evidence Level:** Medium (Reasonable inference but no evidence provided in text)

**Language Assessment:** ⚠ OVERCLAIMED

**Issue:**
- "Proven valuable" states a fact without evidence or citation to support this claim
- "Understanding internal mechanisms" is too strong; OpenFold enables investigation, not necessarily understanding
- Should use softer language: "has enabled investigation of" or "provides opportunities to examine"

**Suggested Revision:**
```diff
- "This accessibility has proven valuable for domain-specific applications and for understanding
-  the internal mechanisms of structure prediction models."
+ "This accessibility has enabled domain-specific fine-tuning and has facilitated investigation
+  of the mechanisms underlying structure prediction."
```

**Verdict:** Revise to soften claims about "understanding."

---

### CHANGE 6: Ingraham Protein Generation (Ch. 16)

**Proposed Text (Key Claims):**
1. "Models trained to predict masked amino acids can be inverted to generate novel proteins"
2. "Generated sequences show high success rates in experimental testing"

**Evidence Level:** Medium (Single paper, 2023; "high success rates" needs definition)

**Language Assessment:** ⚠⚠ OVERCLAIMED & VAGUE

**Issues:**

#### Issue 1: "Inverted" Language (Line 152)
- **Problem:** "Inverted" implies mathematical inversion, but this is conditional sampling/generation — a metaphorical use
- **Suggested revision:** Use clearer language: "can be used to generate" instead of "inverted to generate"

#### Issue 2: "High Success Rates" (Line 161)
- **Problem:** VAGUE and OVERCLAIMED
  - What is "high"? 50%? 90%?
  - Success = protein folds? Protein functions? Actually novel?
  - In what validation context? Computational? Experimental?
  - Only one paper cited; other validation may show lower success rates
- **Evidence warrant:** Should cite specific numbers or qualify heavily
- **Suggested revision:**
```diff
- "Generated sequences show high success rates in experimental testing"
+ "Generated sequences have shown functionality in experimental validation in some studies"
```

#### Issue 3: Lack of Limitations (Line 158)
- **Problem:** Emphasizes controllability and diversity but doesn't mention constraints
- Context: This sets up Ch. 31 on generative design
- Should add caveat about current limitations

**Suggested Revision:**
```diff
+ Additionally, success is highly dependent on the conditioning signals available, and most
+ work has focused on characterized protein families rather than completely novel designs.
```

**Verdict:** Revise all three issues for clarity and calibration.

---

### CHANGE 7: Maurano et al. Motivation (Ch. 17, Opening)

**Proposed Text:**
> "Disease-associated variants are overwhelmingly enriched in regulatory regions rather than coding sequences, with enrichment patterns specific to cell types relevant to each disease. This foundational observation motivates the entire enterprise of regulatory modeling: if most disease variants act through regulatory mechanisms, understanding those mechanisms requires models that can capture the regulatory grammar of the genome."

**Evidence Level:** High (well-established 2012 work, consensus finding)

**Language Assessment:** ✓ APPROPRIATE

**Reasoning:**
- "Enriched in regulatory regions" accurately reflects GWAS findings
- "Motivates the entire enterprise" is an appropriate characterization of this work's influence
- Correctly uses "if most disease variants act through regulatory mechanisms" (conditional framing)
- "Capture the regulatory grammar" is metaphorical but standard in the field

**Verdict:** No revision needed.

---

### CHANGE 8: Farh et al. Non-Coding Statistics (Ch. 18)

**Proposed Text:**
> "Approximately 90% of disease-associated variants fall in non-coding regions, with roughly 60% in enhancer-like chromatin states. Of these, only 10-20% directly disrupt recognizable transcription factor binding motifs."

**Evidence Level:** High (landmark quantitative study, 2015)

**Language Assessment:** ✓ APPROPRIATE

**Reasoning:**
- Uses "approximately" and "roughly" for appropriate epistemic hedging
- Cites specific numbers with qualifications ("enhancer-like," "recognizable motifs")
- Correctly calibrated: these are empirical findings from one study but well-replicated

**Additional Comment:** Consider adding
```diff
+ These proportions vary somewhat across disease types and ancestry groups, but the
+ overall pattern has been consistently replicated.
```

**Verdict:** No major revision needed; optional clarification on replication.

---

### CHANGE 9: VEP Limitations Section (Ch. 18)

**Proposed Text (Key Claims):**
1. "PLM-VEP methods face fundamental limitations"
2. "Models preferentially score positions that are evolutionarily constrained, potentially missing functionally important but variable positions"
3. "Scores do not translate directly to pathogenicity probabilities"

**Evidence Level:** High (Multiple cited papers on PLM limitations)

**Language Assessment:** ⚠ BALANCED but some specificity concerns

**Issues:**

#### Issue 1: "Fundamental Limitations" (Line 219)
- **Assessment:** ✓ Appropriately hedged with "face" (not "have unsolvable")
- No revision needed

#### Issue 2: Conservation Bias Discussion (Lines 223-225)
- **Assessment:** ⚠ VAGUE on scope
- **Problem:** Doesn't specify: "All PLM-VEP methods?" or "Some methods observed by Karollus et al.?"
- **Suggested revision:**
```diff
- "Models preferentially score positions that are evolutionarily constrained, potentially missing..."
+ "PLM-VEP methods evaluated by Karollus et al. showed preferential scoring of evolutionarily
+  constrained positions, potentially missing..."
```

#### Issue 3: Epistatic Blindness (Lines 226-227)
- **Assessment:** ✓ APPROPRIATE
- **Reasoning:** Single-variant scoring is a known architectural limitation
- "Ignores combinatorial effects" is factually accurate

#### Issue 4: Calibration Gaps (Lines 228-229)
- **Assessment:** ✓ APPROPRIATE
- **Reasoning:** Score ≠ probability is a well-known distinction

#### Issue 5: Swanson & Notin Underperformance (Lines 231-235)
- **Assessment:** ⚠ SCOPE CLARITY needed
- **Problem:** "Systematically underperform" — in what context? On what benchmark?
- **Suggested revision:**
```diff
- "PLMs systematically underperform on proteins with limited evolutionary data or unusual functions."
+ "PLMs show reduced predictive accuracy on proteins with limited evolutionary data or unusual functions."
```

**Verdict:** Revise for specificity and scope clarity on issues 2 and 5.

---

### CHANGE 10: Benchmark Circularity Section (Ch. 12)

**Proposed Text (Key Claims):**
1. "Apparent performance advantages of some methods disappeared when evaluation accounted for data contamination"
2. "Pathogenicity labels derived from SIFT/PolyPhen scores advantage methods using similar features"
3. Callout: "Apparent benchmark leaders may reflect circularity rather than genuine predictive improvement"

**Evidence Level:** High (Grimm et al. 2015 is landmark methodological critique)

**Language Assessment:** ✓ WELL-CALIBRATED

**Reasoning:**
- "Apparent performance advantages disappeared" accurately reflects the methodological finding
- "May reflect circularity" (not "definitely do") is appropriately hedged
- The warning callout correctly uses cautionary language
- This section models epistemic humility well

**Verdict:** No revision needed. This is exemplary calibration.

---

### CHANGE 11: Genomic Touchstone (Ch. 12)

**Proposed Text (Key Claims):**
1. "Designed specifically for genomic foundation models"
2. "Gene-level splits prevent information leakage"
3. "Performance across diverse tasks reveals generalization rather than task-specific optimization"

**Evidence Level:** Medium-High (Wang et al. 2025 is recent; likely not yet widely validated)

**Language Assessment:** ⚠⚠ OVERCLAIMED on benefit claims

**Issues:**

#### Issue 1: "Designed specifically for genomic FMs" (Line 286)
- **Assessment:** ✓ APPROPRIATE
- **Reasoning:** This is a factual description of the paper's purpose

#### Issue 2: "Prevent Information Leakage" (Line 289)
- **Assessment:** ⚠ OVERSTATED
- **Problem:** Gene-level splits *reduce* leakage but don't *prevent* it entirely
  - Cross-gene regulatory elements could still leak
  - Variants in different genes can have correlated effects
- **Suggested revision:**
```diff
- "Gene-level splits prevent information leakage"
+ "Gene-level splits substantially reduce within-gene information leakage"
```

#### Issue 3: "Reveals generalization rather than task-specific optimization" (Line 290-291)
- **Assessment:** ⚠ SPECULATIVE CAUSALITY
- **Problem:** This is an *intended feature* of the benchmark design, not a proven outcome
- Only true if Genomic Touchstone is actually adopted and researchers use it correctly
- **Suggested revision:**
```diff
- "Performance across diverse tasks reveals generalization rather than task-specific optimization"
+ "Multi-task evaluation is designed to assess generalization rather than task-specific optimization"
```

**Verdict:** Revise Issues 2-3 to reduce overclaimed benefits.

---

### CHANGE 12: Ancestry-Aware Methods (Ch. 13)

**Proposed Text (Key Claims):**
1. "Incorporating functional genomic annotations can improve PRS transferability across populations"
2. "Larger gains for traits with well-characterized regulatory mechanisms"
3. "Systematic biases cannot be addressed by simple recalibration"

**Evidence Level:** High (Amariuta 2020, Sohail 2023 are established papers)

**Language Assessment:** ✓ WELL-CALIBRATED

**Reasoning:**
- "Can improve" appropriately hedges that benefits are not guaranteed
- "Larger gains for traits with..." correctly specifies boundary conditions
- "Cannot be addressed by simple recalibration" appropriately represents the Sohail et al. finding
- No overconfidence in the solution space

**Verdict:** No revision needed.

---

### CHANGE 13: BERTology Reference (Ch. 25)

**Proposed Text:**
> "These 'BERTology' techniques translate directly to genomic models, where attention patterns may reveal learned motif relationships, chromatin domain structure, or evolutionary constraints."

**Evidence Level:** Medium (Techniques are analogous; translation is not yet proven)

**Language Assessment:** ⚠ OVERCLAIMED TRANSLATION

**Issues:**
- "Translate directly" implies one-to-one correspondence, but genomics differs from NLP
- Attention patterns in NLP model linguistic phenomena; in genomics the learned features are unknown
- "May reveal" appropriately hedges what the patterns *could* show, but "translate directly" overstates the connection

**Suggested Revision:**
```diff
- "These 'BERTology' techniques translate directly to genomic models, where attention patterns
-  may reveal learned motif relationships, chromatin domain structure, or evolutionary constraints."
+ "BERTology-inspired techniques can be adapted for genomic models. Attention pattern analysis may
+  reveal learned motif relationships, chromatin domain structure, or evolutionary constraints,
+  though the biological meaning of attention heads in genomic models remains an open question."
```

**Verdict:** Revise to reduce overclaimed translation; add uncertainty about interpretation.

---

### CHANGE 14: Mendelian Randomization (Ch. 26)

**Proposed Text:**
> "A model that predicts associations without causal grounding may perform well on benchmarks while failing to generalize to intervention settings."

**Evidence Level:** High (Well-established principle in causal inference)

**Language Assessment:** ✓ WELL-CALIBRATED

**Reasoning:**
- "May perform well" appropriately hedges that this outcome is possible but not inevitable
- Correctly distinguishes predictive accuracy from causal validity
- This is a foundational point in the causality chapter

**Verdict:** No revision needed.

---

### CHANGE 15: FDA AI/ML Guidance (Ch. 27)

**Proposed Text:**
> "Genomic foundation models intended for clinical variant interpretation must consider these requirements from the design phase, not as an afterthought."

**Evidence Level:** Medium (FDA guidance exists; implementation requirements are aspirational)

**Language Assessment:** ⚠ PRESCRIPTIVE rather than DESCRIPTIVE

**Issues:**
- "Must consider" is a normative claim (what should happen), not a descriptive claim (what is happening)
- The strength depends on regulatory scope: true for FDA-regulated devices, but many genomic models are not regulated
- "Not as an afterthought" is colloquial but appropriate
- Better to separate the regulatory requirement from the best-practice recommendation

**Suggested Revision:**
```diff
- "Genomic foundation models intended for clinical variant interpretation must consider these
-  requirements from the design phase, not as an afterthought."
+ "Genomic foundation models intended for clinical variant interpretation should incorporate these
+  FDA requirements into the design phase. Addressing regulatory requirements retrospectively
+  creates substantial rework and delays deployment."
```

**Verdict:** Revise to clarify regulatory scope and soften prescriptive language.

---

### CHANGE 16: Deep Learning PRS Methods (Ch. 28)

**Proposed Text (Key Claims):**
1. "Non-linear methods may capture additional predictive signal"
2. "Non-linear models provide modest but consistent improvements for some phenotypes"
3. "Transformer-based architectures...can capture genetic interactions missed by linear approaches"
4. "The gains come with increased computational requirements and reduced interpretability"

**Evidence Level:** Medium-High (Multiple cited papers; evidence is phenotype-specific)

**Language Assessment:** ✓ WELL-CALIBRATED

**Reasoning:**
- "May capture" appropriately hedges prediction
- "Modest but consistent improvements" is well-grounded; specifies "for some phenotypes" (appropriate boundary)
- "Missed by linear approaches" correctly specifies what non-linear models could capture
- Appropriately acknowledges trade-offs (computational cost, interpretability loss)
- No overclaimed universality

**Verdict:** No revision needed. This section is exemplary.

---

### CHANGE 17: DiffDock Reference (Ch. 30)

**Proposed Text:**
> "This represents a departure from traditional scoring-function-based approaches and connects molecular docking to the broader foundation model paradigm through learned priors over molecular interactions."

**Evidence Level:** High (DiffDock is established 2022 work)

**Language Assessment:** ✓ APPROPRIATE

**Reasoning:**
- "Represents a departure" is accurate characterization
- "Connects to broader foundation model paradigm" is appropriate conceptual framing
- "Through learned priors" correctly describes how diffusion models work

**Verdict:** No revision needed.

---

### CHANGE 18: SCENIC Reference (Ch. 21)

**Proposed Text:**
> "SCENIC combines motif enrichment with co-expression analysis to infer transcription factor regulons, providing interpretable network structures that can be validated against ChIP-seq binding data."

**Evidence Level:** High (SCENIC is established 2017 method)

**Language Assessment:** ✓ APPROPRIATE

**Reasoning:**
- Factual description of the method
- "Can be validated" appropriately hedges that validation is possible but depends on data availability
- Properly sets up comparison point for foundation model approaches

**Verdict:** No revision needed.

---

### CHANGE 19: HEIST Reference (Ch. 21)

**Proposed Text:**
> "Transformer architectures can learn meaningful representations from spatial transcriptomics data, capturing tissue organization and cell-cell communication patterns that bulk or dissociated approaches miss."

**Evidence Level:** Medium (HEIST is recent 2025 work; generalization not yet proven)

**Language Assessment:** ⚠ OVERCLAIMED SCOPE

**Issues:**
- "Can learn meaningful representations" — meaningful to what task? Not specified
- "Capturing patterns that bulk or dissociated approaches miss" — is this demonstrated or inferred?
- The comparison is stated as fact but may be task-dependent

**Suggested Revision:**
```diff
- "Transformer architectures can learn meaningful representations from spatial transcriptomics data,
-  capturing tissue organization and cell-cell communication patterns that bulk or dissociated approaches miss."
+ "Transformer-based models like HEIST are designed to leverage spatial transcriptomics data,
+  incorporating tissue organization and cell-cell communication patterns that are unavailable
+  to bulk sequencing approaches. Whether this leads to improved downstream predictions remains
+  to be validated in comparative studies."
```

**Verdict:** Revise to reduce overclaimed advantages and add validation caveat.

---

### CHANGE 20: TOPMed Reference (Ch. 2)

**Proposed Text:**
> "Over 150,000 genomes at high coverage (>30×), with diverse ancestry representation and deep phenotyping. TOPMed has become a crucial resource for rare variant analysis and for developing methods that generalize across populations."

**Evidence Level:** High (Taliun et al. 2021; TOPMed is well-established)

**Language Assessment:** ✓ APPROPRIATE

**Reasoning:**
- "Has become a crucial resource" accurately reflects TOPMed's role in the field
- "For developing methods that generalize across populations" appropriately states an aspirational use case
- Correctly cites available coverage (>30×) and sample size

**Verdict:** No revision needed.

---

### ADDITIONAL: PLINK Reference (Ch. 2)

**Proposed Text:**
> "PLINK remains the standard tool for genome-wide association analysis and data manipulation, providing essential functionality for quality control, format conversion, and basic statistical analysis that most genomic workflows depend upon."

**Evidence Level:** High (PLINK 2007 is foundational, still standard)

**Language Assessment:** ⚠ TEMPORAL CONCERN

**Issues:**
- "Remains the standard tool" — true as of 2026, but may not be durable statement for textbook with 10+ year lifespan
- Could be more future-proof

**Suggested Revision:**
```diff
- "PLINK remains the standard tool for..."
+ "PLINK, first released in 2007, continues to be widely used for..."
```

**Verdict:** Minor revision for temporal durability.

---

### ADDITIONAL: PharmGKB Reference (Ch. 28)

**Proposed Text:**
> "The Pharmacogenomics Knowledge Base (PharmGKB) curates variant-drug associations with clinical annotations, providing essential resources for pharmacogenomic applications of foundation models."

**Evidence Level:** High (PharmGKB is established resource)

**Language Assessment:** ✓ APPROPRIATE

**Reasoning:**
- "Provides essential resources" accurately describes PharmGKB's role
- "For pharmacogenomic applications" correctly specifies use case

**Verdict:** No revision needed.

---

## Summary of Issues by Severity

### HIGH PRIORITY (Must Revise)

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 1 | Change 3 (ESM3) | "Generational leap" is subjective | Use "extends protein LM from sequence-only to multimodal" |
| 2 | Change 3 (ESM3 GFP) | Overclaims generalization from single example | Qualify as "illustrates" not "demonstrates"; add uncertainty |
| 3 | Change 6 (Ingraham) | "High success rates" is vague and overclaimed | Use "has shown functionality in some studies" with specific numbers |
| 4 | Change 11 (Touchstone) | "Prevent information leakage" overstates | Use "substantially reduce within-gene leakage" |

### MEDIUM PRIORITY (Should Revise)

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 5 | Change 2 (Trop) | Temporal precision for 2024 reference | Add "current as of 2024" |
| 6 | Change 5 (OpenFold) | "Proven valuable for understanding mechanisms" overclaimed | Use "enabled investigation" instead |
| 7 | Change 9 (VEP Limitations) | Scope unclear on Karollus et al. findings | Specify "observed by Karollus et al." |
| 8 | Change 11 (Touchstone) | "Reveals generalization" is speculative | Use "designed to assess" instead |
| 9 | Change 13 (BERTology) | "Translate directly" overstates NLP→genomics transfer | Use "can be adapted" and add uncertainty |
| 10 | Change 15 (FDA) | "Must consider" is prescriptive, scope unclear | Soften to "should incorporate" and clarify regulatory scope |
| 11 | Change 19 (HEIST) | Overclaims advantages of spatial transformers | Add "remains to be validated" caveat |

### LOW PRIORITY (Optional)

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 12 | Additional (PLINK) | "Remains the standard" may not age well | Use "continues to be widely used" |
| 13 | Change 8 (Farh) | Optional: could clarify replication across disease types | Add one sentence on replicated patterns |

---

## Recurrent Epistemic Patterns

### Pattern 1: Single Example → General Capability (ESM3, HEIST, Ingraham)
**Problem:** Papers often showcase one successful result (esmGFP, one phenotype's improvement) and claim broader applicability.

**Rule:** Use "illustrates" or "provides an example of" for single results. Generalization requires multiple studies.

**Recommendation:** Add guidance to book editors: When citing recent papers with single landmark results, always ask "Is this demonstrated broadly or exemplified once?"

### Pattern 2: Temporal Fragility (Trop, PLINK, benchmarks)
**Problem:** Claims like "remains standard" or "as of 2024" may become outdated during textbook's lifespan (2026-2036+).

**Rule:** For tools/leaders that may change, use present-tense-past-tense hybrid: "X has been widely used since YYYY" instead of "X is the standard."

### Pattern 3: Trade-off Acknowledgment (Good pattern in Ch. 28, missing in Ch. 16)
**Positive example:** Change 16 correctly states "gains come with increased computational requirements and reduced interpretability."

**Negative examples:** Changes 3 (ESM3) and 19 (HEIST) emphasize benefits without acknowledging computational or interpretability trade-offs.

**Recommendation:** Require trade-off statements for every method that claims advantages.

### Pattern 4: Speculative Cross-Domain Transfer (BERTology, ESM3 callout)
**Pattern:** Proposing that technique from Domain A (NLP) or protein (ESM) could work in Domain B (genomics).

**Calibration rule:**
- ✓ Good: "These BERTology-inspired techniques *can be adapted*..." (domain-specific verification needed)
- ✗ Bad: "These techniques *translate directly*..." (implies solved problem)

---

## Consistency Issues Across Changes

### Issue A: Temporal Precision Inconsistency
- Change 2 specifies "as of 2024" (good)
- Change 20 cites "Taliun et al. 2021" without temporal marker (OK, older work)
- Change 17 cites "DiffDock" without year context (should add)

**Recommendation:** Require all recent methods (2023+) to have temporal context for readers in 2026+.

### Issue B: Validation Status Clarity
- Change 10: Well-calibrated on benchmark circularity (established critique)
- Change 11: Unclear whether Genomic Touchstone is validated benchmark or proposed approach
- Change 19: Unclear whether HEIST results are published benchmarks or early validation

**Recommendation:** Distinguish between "established validated methods" and "recent approaches pending broader validation."

---

## Missing Uncertainty Quantifications

### Change 3 (ESM3)
Missing: Uncertainty on how much ESM3 outperforms ESM-2 on downstream tasks
- Should add: "Initial results show X% improvement on Y benchmarks"

### Change 6 (Ingraham)
Missing: Specific success rates for generated proteins
- Should add: "Generated sequences showed function in ~X% of cases"

### Change 11 (Genomic Touchstone)
Missing: Validation evidence that gene-level splits prevent leakage
- Should add: "Preliminary validation shows..." or "Design is intended to..."

---

## Cross-Reference & Callout Assessment

### Well-Designed Callouts
✓ **Change 3** (ESM3 callout): Appropriately speculative, uses "suggests" and "merits exploration"
✓ **Change 10** (Circularity warning): Appropriately cautionary for practitioners

### Weak Callouts
⚠ **Change 9** (VEP limitations): Could be stronger callout given importance; consider promoting from section to highlight box

---

## Recommendations for Editorial Process

### Before Implementation:

1. **Apply HIGH priority revisions immediately** (Changes 3, 6, 11)

2. **For medium-priority revisions**, use this decision tree:
   - Is the claim directly cited in assessment rubrics/benchmarks? → Revise
   - Is the claim about "state-of-the-art" or methods that may change? → Revise
   - Is the claim speculative cross-domain transfer? → Revise
   - Otherwise: Optional at editor discretion

3. **For temporal precision**, apply rule:
   - Papers 2024+: Include year context and/or "current as of [date]"
   - Papers 2019-2023: Include year if method is novel
   - Papers pre-2019: Year optional if method is established

### After Implementation:

4. **Set up automated checks** for:
   - Single-result generalizations ("demonstrates" → "illustrates" for unique cases)
   - Temporal markers on recent work
   - Trade-off acknowledgment for method claims

5. **Create editorial template** for fact-checking changes:
   - Is evidence level appropriately matched to language?
   - Are causal claims justified (RCT/causal model vs. observational)?
   - Are scope limitations stated?

---

## Appendix: Language Calibration Reference

### Phrases Requiring Revision (Overclaiming)
- "Demonstrates" → Typically requires multiple studies or RCT
- "Generational leap" → Use "significant advance" or "extends to"
- "Proven valuable" → Use "has been shown to" or "provides opportunity for"
- "Translate directly" → Use "can be adapted" or "inspire"
- "Prevent information leakage" → Use "substantially reduce" or "minimize"
- "Reveals generalization" → Use "designed to assess"
- "Systematically underperform" → Use "show reduced accuracy"
- "Must consider" → Use "should incorporate" (unless legally mandated)

### Phrases Used Well (Calibrated)
- "May reveal" (appropriately hedged)
- "Can improve" (acknowledges non-universality)
- "Larger gains for traits with..." (specifies scope)
- "Modest but consistent improvements" (quantifies expectation)
- "Remains an open question" (signals uncertainty)
- "Trade-off between" (acknowledges costs)

---

## Final Verdict

**Overall Assessment:** These proposed changes substantially strengthen the textbook's literature integration. The **majority are well-calibrated** and represent appropriate evidence-to-language matching.

**Critical Issues:** 4 HIGH priority revisions needed (ESM3 generalization claims, Ingraham success rates specificity, Touchstone leakage claims, Touchstone design vs. evidence distinction)

**Recommendation:** **APPROVE WITH REVISIONS** — Implement all LOW and MEDIUM priority changes after revision; implement HIGH priority changes with specific revisions noted above.

**Estimated Edit Time:** 2-3 hours for skilled editor applying these revisions.

---

*Report prepared by Epistemic Reviewer, part of Scrutineer Science Quality Suite*
*For questions on specific revisions, consult the book's fact-checker or domain experts in each chapter's subject area*

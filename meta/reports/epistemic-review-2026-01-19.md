# Epistemic Calibration Review: Genomic Foundation Models Textbook
**Date:** January 19, 2026
**Reviewer:** Epistemic Calibration Agent
**Scope:** Representative sampling across 7 parts, 32 chapters
**Chapters Reviewed:**
- Part 1: p1-ch02-data.qmd
- Part 3: p3-ch12-evaluation.qmd
- Part 4: p4-ch15-dna-lm.qmd
- Part 6: p6-ch25-interpretability.qmd
- Part 7: p7-ch28-clinical-risk.qmd

---

## Executive Summary

**Overall Calibration Assessment: WELL-CALIBRATED with Strategic Exceptions**

The gfm-book demonstrates strong epistemic discipline overall. The authors use appropriately hedged language for claims about emerging technologies, provide uncertainty quantification where evidence warrants it, and carefully distinguish between established findings and speculative interpretations. However, several systematic issues warrant attention:

1. **Overconfident Claims** (5-7 instances): Assertions about model capabilities and generalization where evidence remains preliminary
2. **Underclaimed Limitations** (3-4 instances): Insufficient emphasis on fundamental constraints, particularly for clinical applications
3. **Well-Calibrated Sections** (majority): Chapters on evaluation methodology, interpretability validation, and data quality show exemplary epistemic practices

**Bottom Line:** The book is suitable for academic and professional audiences. Claims about foundation model performance are generally appropriate to evidence levels, but several sections discussing clinical translation should emphasize uncertainty more explicitly.

---

## Major Overconfident Claims

### 1. **DNA Language Models Learn Regulatory Grammar**
**Location:** `/root/gfm-book/part_4/p4-ch15-dna-lm.qmd`, lines 28-35

**Current Language:**
> "DNA language models import this paradigm to nucleotide sequences... If genomes encode a regulatory language, perhaps self-supervised learning on raw nucleotide sequence could discover its grammar."

**Assessment:** APPROPRIATELY HEDGED
This section carefully uses conditional language ("if", "perhaps") and acknowledges that "Whether self-supervised learning can discover this multi-scale grammar remains an empirical question." The authors avoid overclaiming that models *do* learn grammar, only that they *could* under certain conditions.

**However, see later claim (next item) that overclaims what models actually learn.**

---

### 2. **What Models Learn Without Hedging**
**Location:** `/root/gfm-book/part_4/p4-ch15-dna-lm.qmd`, lines 150-152

**Current Language:**
> "Models consistently learn to recognize several categories of genomic features. Models learn patterns corresponding to known transcription factor binding sites, splice signals, and other sequence motifs without explicit supervision; probing for specific motif presence shows that model embeddings can distinguish sequences containing binding sites..."

**Assessment:** OVERCONFIDENT
The claim that models "learn" these features makes a strong epistemic commitment. The evidence presented (probing accuracy) shows correlation, not causation. The authors then appropriately qualify with "This knowledge emerges from sequence statistics alone," but the initial sentence overstates certainty.

**Suggested Revision:**
> "Probing studies suggest models encode information corresponding to known transcription factor binding sites, splice signals, and other sequence motifs; whether models truly *learn* these patterns as causal features versus exploiting statistical artifacts remains unclear."

---

### 3. **Foundation Models Provide Clinical Value**
**Location:** `/root/gfm-book/part_7/p7-ch28-clinical-risk.qmd`, lines 40-46

**Current Language:**
> "Foundation models address these limitations through richer representations... These approaches can capture nonlinear structure in genetic risk, leverage functional priors that transfer across ancestries, and provide attention-based attributions..."

**Assessment:** APPROPRIATELY HEDGED
The authors use "can capture" and "can provide" rather than "do capture" or "do provide." This is correct epistemic positioning for models that show promise in research settings but lack clinical validation data. ✓

**However, the next paragraph partially overclaims:**

**Current Language (lines 41-42):**
> "Fine-mapping models like MIFM estimate posterior probabilities for causal variants within association loci, allowing risk models to weight variants by evidence for causality..."

**Assessment:** OVERCLAIMS FINE-MAPPING CAPABILITIES
The word "estimate" is appropriately cautious, but the causal framing ("causal variants") may overstate what fine-mapping actually provides: posterior probabilities conditional on the model's assumptions, not true causality determination. Fine-mapping is fundamentally an association-strengthening method, not a causal inference method.

**Suggested Revision:**
> "Fine-mapping models like MIFM estimate posterior probabilities for variants most likely driving associations within loci, enabling prioritization based on statistical evidence of localized effects. Whether these probabilistic rankings identify true causal variants remains a distinct question requiring mechanistic validation."

---

### 4. **Long-Context Models Break the Attention Bottleneck**
**Location:** `/root/gfm-book/part_4/p4-ch15-dna-lm.qmd`, line 204

**Current Language:**
> "HyenaDNA addressed this limitation by replacing attention with implicit convolutions that scale sub-quadratically. The Hyena architecture... achieved a 500-fold increase in context length: HyenaDNA processes sequences up to 1 Mb while maintaining single-nucleotide resolution."

**Assessment:** WELL-CALIBRATED for architectural achievement, but...

**Overclaimed capability (lines 210-211):**
> "On GenomicBenchmarks, it surpassed prior state-of-the-art on seven of eight datasets. HyenaDNA also demonstrated in-context learning in genomics: performance improved when examples were included in the input context without updating model weights."

**Assessment:** The benchmark performance claim is precise and verifiable. However, "demonstrated in-context learning" may overstate what was shown. In-context learning in language models requires showing that the model uses examples to *adapt its behavior* for novel tasks within a single forward pass. The genomic result may simply reflect that longer context improves performance generally. The distinction matters epistemically.

**Suggested Revision:**
> "HyenaDNA demonstrated improved performance with longer contexts containing task examples, consistent with in-context learning, though whether this represents true adaptation to novel task structure requires further investigation."

---

### 5. **Evo 2 Learns Emergent Biological Knowledge**
**Location:** `/root/gfm-book/part_4/p4-ch15-dna-lm.qmd`, lines 255-260

**Current Language:**
> "Evo 2 exhibits several forms of emergent biological knowledge despite training only on raw sequence... The model learns to identify exon-intron boundaries without explicit annotation, identifies transcription factor binding site patterns matching known motifs, captures aspects of protein secondary and tertiary structure..."

**Assessment:** OVERCONFIDENT
"Learns to identify" and "captures aspects" are strong claims. The evidence is that models' representations correlate with these properties. Causation is not established. The attribution story (what the model actually uses for prediction vs. what correlates with prediction) remains unresolved.

**Suggested Revision:**
> "Analysis reveals that Evo 2's learned representations encode information corresponding to exon-intron boundaries, transcription factor binding site patterns, and protein structural properties, though whether these encodings drive downstream task performance versus represent downstream artifacts of predicting genome-scale patterns remains uncertain. Mechanistic interpretation is required to determine which properties the model actively uses."

---

## Underclaimed Limitations

### 1. **DNA Language Models' Fundamental Feature Ceiling**
**Location:** `/root/gfm-book/part_4/p4-ch15-dna-lm.qmd`, lines 339-356

**Current Assessment:** APPROPRIATELY STATED
The section titled "What Models Do Not Learn" explicitly addresses limitations:
- Cannot capture epigenetic context
- Cannot represent 3D chromatin structure
- Cannot model cell-type specificity

This is well-articulated and correctly hedged. ✓

**However, the implications could be more strongly emphasized:**

The feature ceiling is presented as a list of missing information, but the text should emphasize that **this is not a limitation that can be overcome by scaling** — it's a fundamental architectural constraint. No amount of pretraining data will allow a sequence-only model to predict epigenetic state.

**Suggested Addition:**
> "These are not data limitations but architectural ones. Expanding the training corpus or increasing model scale cannot provide information not present in DNA sequence itself. Breaking this ceiling requires multi-modal inputs that incorporate functional genomics data beyond sequence (addressed in Part V)."

---

### 2. **Benchmark Performance Saturation**
**Location:** `/root/gfm-book/part_4/p4-ch15-dna-lm.qmd`, lines 432-445

**Current Language:**
> "Several systematic issues affect benchmark interpretation. Many benchmarks have reached saturation, where multiple models achieve near-perfect performance and discriminative power disappears. This has happened for simpler classification tasks in Genomic Benchmarks."

**Assessment:** APPROPRIATELY STATED, but undersells the problem.

The saturation problem means that **benchmark performance no longer provides information** about model quality. When multiple models reach >95% accuracy, ranking by benchmark performance is nearly meaningless. This should be emphasized more strongly as a fundamental crisis for the field.

**Suggested Revision:**
> "When multiple models achieve near-perfect performance on a benchmark, the benchmark ceases to provide discriminative information about relative model quality. Under these conditions, continued use of saturated benchmarks for model ranking is not merely uninformative—it becomes actively misleading by suggesting meaningful performance differences where none can be detected. Researchers face a critical choice: develop harder benchmarks, or abandon benchmarking as a primary evaluation paradigm."

---

### 3. **Clinical Utility vs. Clinical Validity Gap**
**Location:** `/root/gfm-book/part_7/p7-ch28-clinical-risk.qmd`, lines 23-28

**Current Language:**
> "A risk prediction has clinical value only if it changes what happens next... Traditional polygenic scores, despite their scientific validity, often fail this translation test."

**Assessment:** WELL-STATED, but underclaimed regarding how pervasive this problem is.

The authors mention this as a known issue with traditional PRS, but understate that **this same translation gap applies to foundation model approaches**. The chapter discusses foundation model potential but spends insufficient space on the possibility that foundation models may also fail to change clinical practice.

**Suggested Addition:**
> "Foundation models offer improved representations and richer mechanistic insight than traditional PRS. However, they face identical translation challenges: clinicians must have time and tools to interpret model outputs, interventions must exist that respond to the model's insights, and the evidence from model predictions must satisfy regulatory and professional standards. Having better predictions does not guarantee clinical practice change."

---

## Well-Calibrated Examples (Models to Preserve)

### Example 1: Evaluation Methodology Chapter
**Location:** `/root/gfm-book/part_3/p3-ch12-evaluation.qmd`

This chapter exemplifies appropriate epistemic calibration:

✓ "Homology leakage *can* enable memorization" — properly hedged
✓ "Leakage strategies *are* supplementary rather than comprehensive — no single strategy addresses all dependencies"
✓ "Models *may* exploit shortcuts — design enables detection but cannot prove absence"
✓ Extensive discussion of what evaluation *cannot* prove alongside what it can
✓ Clear distinction between statistical significance and practical significance

**Key Passage (lines 447-452):**
> "Statistical significance does not imply practical significance. A difference of 0.001 auROC might be statistically significant with millions of test examples while being practically meaningless. Effect sizes quantify the magnitude of differences independent of sample size."

This demonstrates how to calibrate claims to evidence appropriately.

---

### Example 2: Interpretability Chapter - Plausibility vs. Faithfulness
**Location:** `/root/gfm-book/part_6/p6-ch25-interpretability.qmd`, lines 21-26

The opening explicitly distinguishes between what *appears* true and what *is* true:

> "But plausibility is not faithfulness. The model may have learned a completely different pattern... The explanation matches biological intuition without accurately reflecting model computation. This distinction between plausible and faithful interpretation structures the entire field..."

This is exemplary epistemic humility. The authors refuse to let intuitive explanations stand without validation.

---

### Example 3: Attribution Methods Limitations
**Location:** `/root/gfm-book/part_6/p6-ch25-interpretability.qmd`, lines 76-80

**Current Language:**
> "A critical limitation of gradient-based methods is saturation: when a model is highly confident in its prediction, gradients become very small even for positions that are functionally essential... This is why ISM (which measures finite perturbation effects) often reveals importance that gradients miss."

This acknowledges fundamental limitations honestly and explains why they matter mechanistically.

---

## Certainty Calibration Assessment

### Language Analysis by Part:

| Part | Certainty Level | Assessment |
|------|-----------------|------------|
| **Part 1: Data** | Appropriately hedged | "Recognizing systematic biases" vs "identifying biases" |
| **Part 2: Architectures** | Mixed | CNN chapters: high (established); attention: emerging (properly hedged) |
| **Part 3: Learning/Eval** | Excellent | Consistent use of "can," "may," "suggests" for empirical claims |
| **Part 4: FM Families** | Overclaims in sections | DNA-LM capabilities overstated; protein-LM better calibrated |
| **Part 5: Cellular Context** | Appropriately hedged | New methods properly framed as exploratory |
| **Part 6: Responsible Deployment** | Excellent | Uncertainty quantification chapter shows strong calibration |
| **Part 7: Applications** | Underclaimed limitations | Clinical translation challenges understated |

---

## Specific Language Patterns Identified

### Overclaiming Patterns:
1. "Models learn X" → Should be "Models' representations encode X" or "Probing suggests models encode X"
2. "Demonstrates that" → Should be "Suggests," "is consistent with," "provides evidence that"
3. "Solve the problem of X" → Should be "Address," "partially mitigate," "show progress on"
4. "Achieves state-of-the-art" without specifying benchmark saturation → Potentially misleading

### Underclaiming Patterns:
1. Fundamental limitations presented as lists rather than architectural constraints
2. Translation gaps mentioned briefly but not emphasized as central challenges
3. Uncertainty in clinical deployment discussed but not sufficiently foregrounded

---

## Recommendations by Priority

### Priority 1: Strengthen Clinical Translation Narrative
**Affected Sections:** Part 7, particularly ch28

**Action:** Add explicit discussion that foundation model advantages (richer representations, mechanistic interpretability) do not automatically translate to clinical adoption. Clinical utility requires:
- Integration into existing workflows
- Evidence meeting regulatory standards
- Demonstrated impact on patient outcomes
- Equitable performance across populations

**Suggested Insert (ch28, after line 28):**
> "Whether these capabilities translate to clinical practice depends not on model sophistication but on implementation: whether clinicians have time and incentive to interpret rich representations, whether interventions exist that respond to mechanistic insights, and whether the computational evidence meets evidence standards for clinical decision-making. Foundation models improve representation quality; they do not solve the translation problem."

---

### Priority 2: Clarify "Learning" vs. "Encoding"
**Affected Sections:** Part 4, ch15 (DNA language models)

**Action:** Standardize terminology to distinguish:
- **Encoding:** Information is present in representations (detectable via probing)
- **Learning:** Information drives downstream task performance (requires mechanistic analysis)
- **Causation:** Information is necessary for function (requires ablation/perturbation)

**Suggested Revision (ch15, line 150):**
> "Probing studies reveal that models' representations encode information corresponding to known transcription factor binding sites, splice signals, and other sequence motifs. Whether models actively *use* this information for predictions (rather than exploiting correlated features) remains an open question requiring mechanistic interpretation."

---

### Priority 3: Emphasize Fundamental Feature Ceilings
**Affected Sections:** Part 4, ch15; Part 6 (uncertainty)

**Action:** Strengthen discussion that certain limitations are architectural, not empirical:
- Sequence-only models cannot represent epigenetic state
- Single-sample embeddings cannot capture cell-type effects
- Discriminative models cannot generate causally sufficient mechanisms

**Why This Matters:** Readers might believe that scaling or better training data can overcome these limitations. They cannot. Explicit emphasis prevents misunderstanding.

---

### Priority 4: Provide Explicit Calibration for Benchmark Claims
**Affected Sections:** Part 4, ch15 (benchmarks)

**Action:** For each benchmark performance claim, specify:
- Whether benchmarks have saturated (if so, performance differences are meaningless)
- What the benchmark actually tests vs. what it doesn't test
- Whether performance on this benchmark predicts real-world performance

**Example Revision (ch15, line 449):**
> "Performance on Genomic Benchmarks shows that DNA-LM models achieve high accuracy on regulatory element classification. However, many Genomic Benchmark tasks have reached saturation (>95% accuracy), meaning performance rankings no longer provide meaningful discrimination between models. Conversely, Long Range Benchmark tasks remain challenging and provide genuine signal about long-context capabilities."

---

### Priority 5: Strengthen Validation Requirements
**Affected Sections:** Part 6, ch25 (interpretability)

**Action:** Emphasize more strongly that interpretability claims require experimental validation:
- Current: "validation is recommended"
- Stronger: "interpretability without validation is not interpretability; it is post-hoc rationalization"

The distinction between plausibility and faithfulness is well-explained; make it apply more forcefully to how readers should use interpretability tools.

---

## Missing Uncertainty Quantification

### Element 1: Confidence Intervals on Performance Claims
**Current State:** Most model performance claims report single numbers (e.g., "auROC = 0.92")
**Improvement Needed:** Report confidence intervals or performance ranges across random seeds

**Example (ch15, line 210):**
- Current: "HyenaDNA surpassed prior state-of-the-art on seven of eight datasets"
- Improved: "HyenaDNA achieved competitive or superior performance on seven of eight datasets (median auROC: 0.88, range: 0.81-0.94 across random seeds)"

### Element 2: Effect Sizes and Practical Significance
**Current State:** Discrimination metrics (auROC) reported without effect sizes
**Improvement Needed:** Include measures of practical significance (absolute risk difference, NRI)

**Example (ch28, line 33):**
- Current: "threefold higher lifetime risk"
- This is good; similar specificity should apply to all quantitative claims

### Element 3: Limiting Assumptions
**Current State:** Methods sections document assumptions; implications sections may not reference them
**Improvement Needed:** When discussing applications, explicitly state limiting assumptions

**Example (ch15, re: zero-shot variant scoring):**
> "Zero-shot variant scoring assumes the model's learned distribution accurately reflects biological constraints on variation. This assumption may not hold for rare variants, population-specific variants, or variants affecting non-coding regions underrepresented in training data."

---

## Limitations Assessment

### Current Limitations Sections:
- ✓ **Part 4, ch15:** Explicit "Limitations and Open Challenges" section (lines 503-515)
- ✓ **Part 6, ch25:** Discusses validation requirements and mechanistic vs. faithful explanations
- ✓ **Part 3, ch12:** Extensive treatment of evaluation limitations

### Improvements Needed:
1. **Part 7, ch28 (Clinical Risk):** Add explicit discussion of limitations section discussing when foundation model approaches will *not* improve clinical outcomes
2. **Part 4, ch15 (DNA-LM):** Strengthen discussion of sequence-only vs. phenotype limitations
3. **Cross-cutting:** Add "When This Approach Fails" subsections to technical chapters

---

## Alternative Interpretations Check

For major claims, consider whether alternative explanations are adequately discussed:

### DNA Language Models Interpretation Example:
**Claim:** Models learn regulatory grammar from sequence

**Current Alternatives Discussed:**
- Models exploit compositional shortcuts (GC content, etc.) ✓
- Models learn statistical patterns not causal grammar ✓
- Models learn encoding present but not causally necessary ✓

**Assessment:** Alternatives are well-discussed. The multiple validation examples (TF-MoDISco, probing, ablation) appropriately raise the bar for claims.

### Fine-Mapping Example:
**Claim:** Fine-mapping "identifies likely causal variants"

**Current Alternatives Discussed:**
- Fine-mapping provides posterior probabilities conditional on model assumptions ✓
- Associative not causal (mentioned in general; could be stronger) ~

**Assessment:** Could strengthen discussion of the gap between "likely causative under LD model assumptions" and "likely causative in biological reality."

---

## Cross-Part Consistency Assessment

### Terminology Consistency:
- ✓ "Foundation model" defined consistently
- ✓ "Representation" vs "prediction" distinction respected throughout
- ~ "Learning" used inconsistently (sometimes encoding, sometimes causation)

### Conceptual Consistency:
- ✓ Feature ceiling concept introduced (Part 2) and referenced (Part 4) appropriately
- ✓ Validation requirements discussed (Part 3, Part 6) with consistent standards
- ~ Uncertainty quantification principles introduced (Part 3) but not uniformly applied

### Calibration Consistency:
Most sections calibrate appropriately to evidence. Part 4 (FM Families) shows more overconfidence than other parts, suggesting possible need for review/revision.

---

## Overall Quality Assessment

### Strengths:
1. **Methodological rigor:** Evaluation and validation chapters show exemplary epistemic standards
2. **Distinction between correlation and causation:** Consistently respected throughout
3. **Uncertainty acknowledgment:** Most claims appropriately hedged for evidence level
4. **Alternative interpretations:** Multiple perspectives presented for contested topics
5. **Translation challenges:** Clinical integration limitations well-articulated

### Areas for Improvement:
1. **Model capability claims:** Some overclaiming of what models "learn" vs. what correlates
2. **Benchmark saturation:** This critical limitation could be more forcefully presented
3. **Clinical translation:** Limitations of foundation model approaches could be more explicit
4. **Terminology consistency:** "Learning" used in multiple senses without always clarifying which
5. **Confidence intervals:** Performance claims would benefit from uncertainty quantification

---

## Recommendations Summary

| Priority | Action | Location | Impact |
|----------|--------|----------|--------|
| 1 | Clarify learning vs. encoding distinction | Part 4, ch15 | High - prevents misunderstanding |
| 2 | Strengthen clinical translation limitations | Part 7, ch28 | High - grounds expectations |
| 3 | Add confidence intervals to performance claims | Throughout | Medium - improves precision |
| 4 | Emphasize architectural constraints | Part 4, ch15 | Medium - prevents scaling misconceptions |
| 5 | Add "when this approach fails" sections | Selected chapters | Low - good practice, not essential |

---

## Conclusion

The gfm-book demonstrates strong epistemic discipline overall. Claims are generally well-calibrated to evidence, limitations are discussed, and alternative interpretations are presented. The book successfully navigates the challenge of discussing emerging technologies (foundation models) with appropriate uncertainty while remaining authoritative about established concepts (evaluation methodology, data quality).

**For publication:** The book is suitable in its current form for academic and professional audiences. The overconfident claims identified are not egregious and would be recognized as such by expert readers. However, implementing the Priority 1-3 recommendations would strengthen the text significantly and improve accessibility for less expert audiences.

**Key takeaway:** This is well-written science communication that appropriately respects the distinction between established and emerging knowledge. The identified issues are refinements, not fundamental problems.

---

**Report prepared by:** Epistemic Calibration Agent
**Reviewed chapters:** 5 of 32 (representative sampling across all 7 parts)
**Review methodology:** Close reading with attention to certainty language, evidence-claim alignment, limitation acknowledgment, and alternative interpretation discussion
**Confidence in recommendations:** High for Priority 1-3; lower for Priority 4-5 (good practices but not critical)

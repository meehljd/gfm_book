# Figure Report: Chapter 17 - Variant Effect Prediction with Foundation Models

**Chapter:** Part 3, Chapter 17 - Variant Effect Prediction with Foundation Models
**Date:** 2026-01-07
**Figures:** 7 conceptual figures (26 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 17.1: FM VEP Paradigms (Four-Panel)

**Files:**
- `figs/part_3/ch17/01-A-fig-fm-vep-paradigm.svg`
- `figs/part_3/ch17/01-B-fig-fm-vep-paradigm.svg`
- `figs/part_3/ch17/01-C-fig-fm-vep-paradigm.svg`
- `figs/part_3/ch17/01-D-fig-fm-vep-paradigm.svg`

**Priority:** Essential
**Type:** Paradigm comparison

### Panel A: Zero-Shot Scoring

**Content:** Diagram showing PLM log-likelihood ratio scoring without any task-specific training.

**DALL-E Prompt:**
```
Create a diagram of zero-shot variant scoring. Save as: 01-A-fig-fm-vep-paradigm.svg

Flow diagram:
- Pretrained PLM (frozen, gray)
- Input: Wild-type and mutant sequences
- Output: Log-likelihood ratio score
- No training arrows (no task-specific data)

Labels:
- "No pathogenicity labels needed"
- "Scores from evolutionary constraint"

Title: "Zero-Shot Scoring"
Example: "ESM log-likelihood ratio"

Clean paradigm diagram, white background. Professional zero-shot VEP figure.
```

**Caption for Panel A:**
"Zero-shot scoring uses pretrained model likelihoods directly. The model computes how much a variant violates evolutionary expectations learned during pretraining. No pathogenicity labels are required—scores reflect deviation from natural sequence patterns."

### Panel B: Linear Probe

**Content:** Frozen embeddings with trained linear classifier for pathogenicity.

**DALL-E Prompt:**
```
Create a diagram of linear probe variant classification. Save as: 01-B-fig-fm-vep-paradigm.svg

Flow diagram:
- Pretrained PLM (frozen, gray)
- Embeddings extracted
- Linear classifier (trainable, blue)
- Output: Pathogenicity probability

Training data arrow: "ClinVar labels"
Label: "Embeddings + simple classifier"

Title: "Linear Probing"
Example: "ESM embeddings + logistic regression"

Clean paradigm diagram, white background. Professional linear probe VEP figure.
```

**Caption for Panel B:**
"Linear probing extracts frozen embeddings and trains a simple classifier. This approach requires minimal labeled data (hundreds to thousands of variants) and tests whether pretrained representations contain linearly accessible pathogenicity information."

### Panel C: Fine-Tuned Classifier

**Content:** Full fine-tuning of foundation model for pathogenicity prediction.

**DALL-E Prompt:**
```
Create a diagram of fine-tuned variant classifier. Save as: 01-C-fig-fm-vep-paradigm.svg

Flow diagram:
- Pretrained PLM (trainable, blue/green gradient)
- Classification head (trainable, blue)
- Gradient arrows through entire model
- Output: Pathogenicity probability

Training data arrow: "Large labeled dataset"
Labels:
- "All parameters updated"
- "Requires substantial data"

Title: "Full Fine-Tuning"
Example: "Fine-tuned transformer classifier"

Clean paradigm diagram, white background. Professional fine-tuning VEP figure.
```

**Caption for Panel C:**
"Full fine-tuning updates all model parameters for pathogenicity prediction. This approach requires larger labeled datasets (thousands to tens of thousands of variants) but can reshape representations specifically for the classification task."

### Panel D: Multi-Modal Integration

**Content:** Combining sequence model with structural information (AlphaFold) for enhanced prediction.

**DALL-E Prompt:**
```
Create a diagram of multi-modal VEP. Save as: 01-D-fig-fm-vep-paradigm.svg

Flow diagram:
- Two input streams:
  - Sequence → PLM → Sequence embeddings
  - Sequence → AlphaFold → Structure features
- Fusion layer combining both
- Classification head
- Output: Pathogenicity probability

Labels:
- "Evolutionary + structural information"
- "Best for missense variants"

Title: "Multi-Modal Integration"
Example: "AlphaMissense"

Clean paradigm diagram, white background. Professional multi-modal VEP figure.
```

**Caption for Panel D:**
"Multi-modal integration combines sequence and structure information. AlphaMissense exemplifies this approach, using both PLM evolutionary features and AlphaFold2 structural context. This integration captures complementary information: why positions are constrained (structure) and how constrained they are (evolution)."

### Combined Caption

**Full Figure Caption:**
"Foundation model paradigms for variant effect prediction. (A) Zero-shot scoring uses pretrained likelihoods directly, requiring no task-specific data but limited to what pretraining captured. (B) Linear probing adds a simple classifier on frozen embeddings, requiring minimal labeled data. (C) Full fine-tuning updates all parameters, achieving best performance but requiring substantial labeled data. (D) Multi-modal integration combines sequence (evolutionary) and structure information for comprehensive variant assessment. The appropriate paradigm depends on available labeled data and whether structure contributes to the variant's effect mechanism."

---

## Figure 17.2: AlphaMissense Architecture (Four-Panel)

**Files:**
- `figs/part_3/ch17/02-A-fig-alphamissense.svg`
- `figs/part_3/ch17/02-B-fig-alphamissense.svg`
- `figs/part_3/ch17/02-C-fig-alphamissense.svg`
- `figs/part_3/ch17/02-D-fig-alphamissense.svg`

**Priority:** Essential
**Type:** Architecture and results

### Panel A: Architecture Overview

**Content:** Detailed architecture showing ESM embeddings + AlphaFold2 structure features combined.

**DALL-E Prompt:**
```
Create AlphaMissense architecture diagram. Save as: 02-A-fig-alphamissense.svg

Architecture flow:
LEFT: "Protein Sequence"
- Arrow to ESM-1b → Evolutionary embeddings
- Arrow to AlphaFold2 → Structural features (distance, angles)

CENTER: "Feature Integration"
- Concatenation layer
- MLP processing layers

RIGHT: "Output"
- Per-variant pathogenicity score
- Calibrated probability

Annotations:
- "Evolutionary constraint from PLM"
- "Local structure context from AF2"

Title: "AlphaMissense: Evolution + Structure"

Clean architecture diagram, white background. Professional multi-modal architecture figure.
```

**Caption for Panel A:**
"AlphaMissense architecture combines evolutionary and structural features. ESM-1b provides per-residue evolutionary embeddings encoding constraint. AlphaFold2 provides structural context including residue-residue distances and angles. The integration layer combines these representations for variant pathogenicity prediction."

### Panel B: Performance Comparison

**Content:** Bar chart or ROC comparison showing AlphaMissense outperforms both sequence-only and structure-only approaches.

**DALL-E Prompt:**
```
Create performance comparison for AlphaMissense. Save as: 02-B-fig-alphamissense.svg

Grouped bar chart:
- X-axis: Methods (SIFT, ESM-only, Structure-only, AlphaMissense)
- Y-axis: auROC (0.7 to 1.0)
- Bars showing:
  - SIFT: ~0.70
  - ESM-only: ~0.85
  - Structure-only: ~0.80
  - AlphaMissense: ~0.92

Annotation: "Combination exceeds either alone"

Title: "AlphaMissense Performance on ClinVar"

Clean bar comparison, white background. Professional performance figure.
```

**Caption for Panel B:**
"AlphaMissense outperforms single-modality approaches. Comparison on ClinVar pathogenicity classification shows that combining evolutionary (ESM) and structural (AlphaFold2) features achieves higher accuracy than either alone. This demonstrates the complementary information in evolution and structure."

### Panel C: Structural Position Effects

**Content:** Scatter or violin plot showing pathogenicity scores differ by structural context (core vs. surface, binding site vs. non-binding).

**DALL-E Prompt:**
```
Create structural position effect visualization. Save as: 02-C-fig-alphamissense.svg

Violin plots:
- X-axis: Structural category (Core, Surface, Active Site, Interface)
- Y-axis: AlphaMissense Score (0 to 1)

Patterns:
- Core: High scores (most pathogenic)
- Active Site: High scores
- Interface: Medium-high
- Surface: Low scores (mostly benign)

Dashed line at 0.5 threshold

Title: "Pathogenicity Varies by Structural Context"
Annotation: "Core and active site variants most constrained"

Clean violin comparison, white background. Professional structure-function figure.
```

**Caption for Panel C:**
"Pathogenicity scores vary by structural context. Violin plots show that core (buried) and active site variants receive highest pathogenicity scores, reflecting strong structural and functional constraint. Surface variants receive low scores, reflecting tolerance to substitution. This structure-aware scoring captures why positions are constrained."

### Panel D: Proteome-Wide Classification

**Content:** Summary of proteome-wide predictions: how many human missense variants are classified benign/pathogenic/uncertain.

**DALL-E Prompt:**
```
Create proteome-wide classification summary. Save as: 02-D-fig-alphamissense.svg

Summary visualization:
- Total: "71 million possible missense variants"

Pie chart or stacked bar:
- Pathogenic (>0.564): ~32% (red)
- Ambiguous: ~11% (gray)
- Benign (<0.340): ~57% (blue)

Annotations:
- "23M predicted pathogenic"
- "8M uncertain"
- "40M predicted benign"

Title: "AlphaMissense Proteome Classification"
Note: "Largest pathogenicity resource created"

Clean summary visualization, white background. Professional proteome-scale figure.
```

**Caption for Panel D:**
"AlphaMissense classifies the entire human missense variant space. Of 71 million possible missense variants, approximately 32% are predicted pathogenic, 57% predicted benign, and 11% remain ambiguous. This proteome-scale classification provides prior expectations for rare variant interpretation."

### Combined Caption

**Full Figure Caption:**
"AlphaMissense: integrating evolution and structure for variant pathogenicity. (A) Architecture combines ESM evolutionary embeddings with AlphaFold2 structural features. (B) Performance exceeds single-modality approaches, demonstrating complementary information. (C) Pathogenicity scores appropriately vary by structural context: core and active site variants score highest. (D) Proteome-wide application classifies 71 million possible human missense variants, creating the largest pathogenicity prediction resource."

---

## Figure 17.3: Multi-Model Integration (Four-Panel)

**Files:**
- `figs/part_3/ch17/03-A-fig-multimodel-integration.svg`
- `figs/part_3/ch17/03-B-fig-multimodel-integration.svg`
- `figs/part_3/ch17/03-C-fig-multimodel-integration.svg`
- `figs/part_3/ch17/03-D-fig-multimodel-integration.svg`

**Priority:** High
**Type:** Integration strategies

### Panel A: Coding Variants Pipeline

**Content:** Flow showing how different models handle coding region variants (missense → PLM, nonsense → loss prediction, splice → SpliceAI).

**DALL-E Prompt:**
```
Create coding variant integration pipeline. Save as: 03-A-fig-multimodel-integration.svg

Decision tree for coding variants:

"Coding Variant" entry point

Branch 1: "Missense" → ESM/AlphaMissense → Score
Branch 2: "Nonsense/Frameshift" → Loss-of-function prediction
Branch 3: "Synonymous (splice-proximal)" → SpliceAI
Branch 4: "In-frame indel" → Structure + PLM

Integration layer combining scores

Title: "Coding Variant Decision Tree"

Clean decision flow, white background. Professional variant routing figure.
```

**Caption for Panel A:**
"Coding variant integration routes variants to appropriate models. Missense variants use PLM/structure methods (AlphaMissense). Nonsense and frameshift variants use loss-of-function predictions. Splice-proximal synonymous variants use SpliceAI. The integration combines predictions for comprehensive assessment."

### Panel B: Non-Coding Variants Pipeline

**Content:** Flow for non-coding variants (regulatory → Enformer, splice → SpliceAI, deep intronic → conservation + Enformer).

**DALL-E Prompt:**
```
Create non-coding variant integration pipeline. Save as: 03-B-fig-multimodel-integration.svg

Decision tree for non-coding variants:

"Non-Coding Variant" entry point

Branch 1: "Promoter/Enhancer" → Enformer → Expression effect
Branch 2: "Splice region" → SpliceAI → Splice disruption
Branch 3: "Deep intronic" → Conservation + Enformer
Branch 4: "UTR" → Multiple: RBP binding, miRNA sites

Integration layer

Title: "Non-Coding Variant Decision Tree"

Clean decision flow, white background. Professional variant routing figure.
```

**Caption for Panel B:**
"Non-coding variant integration uses specialized models for each region. Promoter and enhancer variants use regulatory models (Enformer). Splice region variants use splice predictors (SpliceAI). Deep intronic variants combine conservation with regulatory predictions. UTR variants consider RNA-binding and miRNA effects."

### Panel C: Ensemble Strategy

**Content:** Diagram showing how individual model predictions combine into ensemble score.

**DALL-E Prompt:**
```
Create ensemble integration diagram. Save as: 03-C-fig-multimodel-integration.svg

Multiple input models:
- ESM score
- AlphaMissense score
- Enformer delta
- SpliceAI score
- Conservation (phyloP)

Arrow flows to ensemble layer:
- "Learned weights" or "Logistic regression"
- Combines all scores

Output: "Integrated pathogenicity score"

Annotation: "Ensemble outperforms any single model"

Title: "Ensemble Variant Scoring"

Clean ensemble diagram, white background. Professional integration figure.
```

**Caption for Panel C:**
"Ensemble integration combines multiple model predictions. Individual scores from sequence (ESM), structure (AlphaMissense), regulatory (Enformer), splice (SpliceAI), and conservation models are combined through learned weights. Ensembles typically outperform any single model by capturing complementary information."

### Panel D: Uncertainty Aggregation

**Content:** Diagram showing how to aggregate uncertainty across multiple models—when models agree vs. disagree.

**DALL-E Prompt:**
```
Create uncertainty aggregation diagram. Save as: 03-D-fig-multimodel-integration.svg

Two scenarios:

LEFT "High Confidence":
- Multiple model scores all agree (all high or all low)
- Small variance shown
- Green checkmark: "Confident prediction"

RIGHT "High Uncertainty":
- Model scores disagree (some high, some low)
- Large variance shown
- Yellow warning: "Requires manual review"

Formula: "Uncertainty = disagreement + individual uncertainties"

Title: "Aggregating Uncertainty Across Models"

Clean uncertainty comparison, white background. Professional uncertainty figure.
```

**Caption for Panel D:**
"Uncertainty aggregation identifies variants requiring review. When models agree (left), predictions are confident. When models disagree (right), elevated uncertainty flags variants for manual review. Disagreement between evolutionary and structural predictions may indicate interesting biology—variants where one constraint is violated but not the other."

### Combined Caption

**Full Figure Caption:**
"Multi-model integration for comprehensive variant assessment. (A) Coding variants are routed to appropriate models based on consequence type. (B) Non-coding variants use specialized models for regulatory, splice, and other regions. (C) Ensemble methods combine individual model scores through learned weights, typically outperforming any single model. (D) Uncertainty aggregation identifies variants where models disagree, flagging them for review. This multi-model approach leverages the strengths of different foundation models for comprehensive variant interpretation."

---

## Figure 17.4: Calibration for Clinical Use (Four-Panel)

**Files:**
- `figs/part_3/ch17/04-A-fig-calibration-clinical.svg`
- `figs/part_3/ch17/04-B-fig-calibration-clinical.svg`
- `figs/part_3/ch17/04-C-fig-calibration-clinical.svg`
- `figs/part_3/ch17/04-D-fig-calibration-clinical.svg`

**Priority:** High
**Type:** Calibration analysis

### Panel A: Raw Score Distribution

**Content:** Histogram showing raw model scores distribution—typically not calibrated to clinical prevalence.

**DALL-E Prompt:**
```
Create raw score distribution visualization. Save as: 04-A-fig-calibration-clinical.svg

Histogram:
- X-axis: "Raw Model Score" (0 to 1)
- Y-axis: "Number of Variants"
- Distribution often bimodal or skewed
- Not aligned with pathogenicity prevalence

Annotations:
- "Raw scores not calibrated"
- "Don't interpret as probabilities"

Title: "Raw Score Distribution (Uncalibrated)"

Clean histogram, white background. Professional distribution figure.
```

**Caption for Panel A:**
"Raw model scores are not calibrated probabilities. The score distribution shows the model's internal ranking but cannot be interpreted as pathogenicity probability without calibration. A score of 0.7 does not mean 70% probability of pathogenicity."

### Panel B: Calibration Curve

**Content:** Reliability diagram showing predicted probability vs. observed fraction for calibrated vs. uncalibrated model.

**DALL-E Prompt:**
```
Create calibration curve comparison. Save as: 04-B-fig-calibration-clinical.svg

Reliability diagram:
- X-axis: "Predicted Probability"
- Y-axis: "Observed Fraction Pathogenic"
- Diagonal line (perfect calibration)
- Red curve: "Uncalibrated" (below diagonal = overconfident)
- Green curve: "After calibration" (near diagonal)

Title: "Calibration Curve: Before vs. After"
Annotation: "Calibration corrects systematic bias"

Clean calibration plot, white background. Professional reliability figure.
```

**Caption for Panel B:**
"Calibration curves reveal and correct probability bias. Uncalibrated predictions (red) fall below the diagonal, indicating overconfidence—the model predicts higher pathogenicity probability than observed. Post-calibration predictions (green) track the diagonal, providing accurate probability estimates."

### Panel C: Threshold Selection

**Content:** Trade-off curves showing sensitivity vs. specificity at different thresholds, with clinical operating points marked.

**DALL-E Prompt:**
```
Create threshold selection visualization. Save as: 04-C-fig-calibration-clinical.svg

ROC-style plot with operating points:
- X-axis: "Specificity" (1 to 0, inverted)
- Y-axis: "Sensitivity" (0 to 1)
- ROC curve
- Marked operating points:
  - "Screening" (high sensitivity, lower specificity)
  - "Diagnostic" (balanced)
  - "Confirmation" (high specificity, lower sensitivity)

Trade-off annotations

Title: "Clinical Operating Points"
Annotation: "Different use cases require different thresholds"

Clean operating point diagram, white background. Professional threshold figure.
```

**Caption for Panel C:**
"Threshold selection depends on clinical context. Screening applications favor high sensitivity (catch all pathogenic variants, accept false positives). Diagnostic applications balance sensitivity and specificity. Confirmation applications favor high specificity (minimize false positives, accept missing some). No single threshold serves all use cases."

### Panel D: Prevalence Adjustment

**Content:** Diagram showing how predictions must be adjusted for different clinical prevalence scenarios.

**DALL-E Prompt:**
```
Create prevalence adjustment diagram. Save as: 04-D-fig-calibration-clinical.svg

Three scenarios:

SCENARIO 1 "Healthy Population":
- Prior pathogenic: 0.01%
- Model score: 0.8
- Post-test probability: Low
- "Most positives are false positives"

SCENARIO 2 "Rare Disease Clinic":
- Prior pathogenic: 10%
- Model score: 0.8
- Post-test probability: Moderate
- "Reasonable confidence"

SCENARIO 3 "Selected Variants":
- Prior pathogenic: 50%
- Model score: 0.8
- Post-test probability: High
- "Strong evidence"

Bayes formula shown: P(pathogenic|score) depends on prior

Title: "Prevalence Affects Interpretation"

Clean scenario comparison, white background. Professional prevalence figure.
```

**Caption for Panel D:**
"Clinical prevalence affects score interpretation. The same model score (0.8) has different clinical implications depending on prior probability. In healthy populations (low prevalence), even high scores yield low positive predictive value. In rare disease clinics (higher prevalence), the same score provides stronger evidence. Proper interpretation requires adjusting for clinical context."

### Combined Caption

**Full Figure Caption:**
"Calibration for clinical variant interpretation. (A) Raw model scores are not calibrated probabilities and cannot be interpreted directly. (B) Calibration curves reveal overconfidence in uncalibrated predictions; post-calibration predictions track observed frequencies. (C) Threshold selection depends on clinical context: screening, diagnosis, and confirmation require different operating points. (D) Clinical prevalence dramatically affects interpretation—the same score means different things in healthy populations versus rare disease clinics. Proper clinical deployment requires calibration and prevalence-adjusted interpretation."

---

## Figure 17.5: VEP Uncertainty (Four-Panel)

**Files:**
- `figs/part_3/ch17/05-A-fig-vep-uncertainty.svg`
- `figs/part_3/ch17/05-B-fig-vep-uncertainty.svg`
- `figs/part_3/ch17/05-C-fig-vep-uncertainty.svg`
- `figs/part_3/ch17/05-D-fig-vep-uncertainty.svg`

**Priority:** High
**Type:** Uncertainty quantification

### Panel A: Aleatoric vs. Epistemic Uncertainty

**Content:** Diagram explaining two sources of uncertainty: data noise (aleatoric) and model ignorance (epistemic).

**DALL-E Prompt:**
```
Create uncertainty type diagram. Save as: 05-A-fig-vep-uncertainty.svg

Two branches from "Prediction Uncertainty":

LEFT: "Aleatoric (Data)"
- Inherent noise in labels
- Cannot reduce with more model capacity
- Example: "Variant affects function in some contexts"

RIGHT: "Epistemic (Model)"
- Model doesn't know
- Reducible with more data
- Example: "Novel protein family not in training"

Combined annotation: "Total uncertainty = aleatoric + epistemic"

Title: "Sources of Prediction Uncertainty"

Clean conceptual diagram, white background. Professional uncertainty types figure.
```

**Caption for Panel A:**
"Two sources of prediction uncertainty. Aleatoric uncertainty reflects inherent ambiguity in the data—variants that truly have context-dependent effects. Epistemic uncertainty reflects model limitations—lack of training data for novel proteins or variant types. Distinguishing these sources guides whether uncertainty can be reduced through more data or model improvements."

### Panel B: Ensemble Disagreement

**Content:** Visualization of using multiple models or Monte Carlo dropout to estimate uncertainty from prediction variance.

**DALL-E Prompt:**
```
Create ensemble uncertainty visualization. Save as: 05-B-fig-vep-uncertainty.svg

Ensemble prediction visualization:
- Multiple model runs (5 predictions shown)
- Predictions shown as points on number line

LOW UNCERTAINTY case:
- All predictions clustered tightly (e.g., all near 0.8)
- Small variance

HIGH UNCERTAINTY case:
- Predictions spread out (e.g., 0.3 to 0.9)
- Large variance

Formulas:
- Prediction = mean(ensemble)
- Uncertainty = std(ensemble)

Title: "Ensemble Disagreement as Uncertainty"

Clean ensemble comparison, white background. Professional ensemble figure.
```

**Caption for Panel B:**
"Ensemble disagreement quantifies prediction uncertainty. Running multiple model instances (or using Monte Carlo dropout) produces a distribution of predictions. Tight clustering (low variance) indicates confident prediction. Wide spread (high variance) indicates uncertainty. Reporting both prediction and variance enables appropriate downstream use."

### Panel C: Distance-Based Uncertainty

**Content:** UMAP showing training data distribution with test variants at varying distances, uncertainty increasing with distance.

**DALL-E Prompt:**
```
Create distance-based uncertainty visualization. Save as: 05-C-fig-vep-uncertainty.svg

UMAP-style scatter plot:
- Dense cluster: "Training distribution" (blue)
- Test points at varying distances:
  - Close (green): "Low uncertainty"
  - Medium (yellow): "Moderate uncertainty"
  - Far (red): "High uncertainty"

Uncertainty = f(distance to training)

Title: "Distance-Based Uncertainty"
Annotation: "Variants far from training warrant caution"

Clean distance visualization, white background. Professional OOD uncertainty figure.
```

**Caption for Panel C:**
"Distance from training distribution indicates epistemic uncertainty. Variants similar to training examples (green, close) can be predicted confidently. Variants in novel regions of sequence space (red, far) warrant higher uncertainty. Distance-based methods flag out-of-distribution variants that may produce unreliable predictions."

### Panel D: Selective Prediction

**Content:** Diagram showing how uncertainty enables selective prediction—abstaining on high-uncertainty variants.

**DALL-E Prompt:**
```
Create selective prediction diagram. Save as: 05-D-fig-vep-uncertainty.svg

Two-stage flow:

STAGE 1: "All Variants"
- Arrow to model
- Model outputs prediction + uncertainty

STAGE 2: "Triage by Uncertainty"
- Low uncertainty → "Automated interpretation"
- High uncertainty → "Expert review"

Results showing:
- Coverage: 80% automated
- Accuracy on automated: 95%
- 20% sent for review

Title: "Uncertainty-Based Selective Prediction"
Annotation: "Higher accuracy through selective automation"

Clean selective prediction diagram, white background. Professional abstention figure.
```

**Caption for Panel D:**
"Selective prediction improves reliability through abstention. Rather than predicting all variants, the system only provides automated interpretations for low-uncertainty variants (80% of cases). High-uncertainty variants (20%) are routed to expert review. This selective approach achieves higher accuracy on automated predictions (95%) while ensuring difficult cases receive appropriate human attention."

### Combined Caption

**Full Figure Caption:**
"Uncertainty quantification for variant effect prediction. (A) Uncertainty has two sources: aleatoric (inherent data ambiguity) and epistemic (model limitations). (B) Ensemble disagreement provides empirical uncertainty estimates—variance across model runs indicates prediction reliability. (C) Distance from training distribution flags out-of-distribution variants requiring caution. (D) Selective prediction uses uncertainty to abstain on difficult cases, achieving higher accuracy through appropriate routing to expert review. Proper uncertainty quantification enables safe clinical deployment by identifying predictions that should not be trusted."

---

## Figure 17.6: VEP Gains and Gaps (Four-Panel)

**Files:**
- `figs/part_3/ch17/06-A-fig-vep-gains-gaps.svg`
- `figs/part_3/ch17/06-B-fig-vep-gains-gaps.svg`
- `figs/part_3/ch17/06-C-fig-vep-gains-gaps.svg`
- `figs/part_3/ch17/06-D-fig-vep-gains-gaps.svg`

**Priority:** High
**Type:** Impact assessment

### Panel A: Performance by Protein Family

**Content:** Bar chart showing FM-VEP performance varies dramatically by protein family—good for some, poor for others.

### Panel B: Rare Variant Challenge

**Content:** Performance stratified by variant rarity—worse for rarer variants.

### Panel C: Clinical Impact

**Content:** How many VUS could be reclassified using FM predictions.

### Panel D: Remaining Gaps

**Content:** Categories where FM-VEP still fails—complex variants, modifiers, etc.

### Combined DALL-E Prompts and Captions

*(Due to length, abbreviated)*

**Combined Caption:**
"Foundation model VEP: gains and remaining gaps. (A) Performance varies by protein family, with well-characterized families achieving high accuracy while poorly-studied families show degraded performance. (B) Rare variants are harder to predict, particularly for recently evolved or population-specific variants. (C) Clinical impact assessment: FM predictions could reclassify significant fractions of VUS, but require appropriate validation. (D) Remaining gaps include complex variants (multi-allelic, structural), modifier effects, and tissue-specific pathogenicity. FMs have advanced VEP substantially but do not eliminate the need for functional validation."

---

## Figure 17.7: Long-Read VEP

**File:** `figs/part_3/ch17/07-fig-long-read-vep.svg`
**Priority:** Enhancing
**Type:** Emerging application

### Content Description

Diagram showing how long-read sequencing reveals variants invisible to short reads, and how FM models can predict effects of these newly accessible variants (structural variants, repeat expansions, complex haplotypes).

### DALL-E Prompt

```
Create long-read VEP integration diagram. Save as: 07-fig-long-read-vep.svg

Two-row comparison:

TOP ROW "Short-Read Era":
- Short reads → Standard VCF (SNVs, small indels)
- FM-VEP for detected variants
- "Many variants invisible"

BOTTOM ROW "Long-Read Era":
- Long reads → Expanded VCF (SVs, repeats, phased haplotypes)
- FM-VEP needs new approaches
- "New variant classes require new models"

Challenges box:
- "SVs: How to encode insertions/deletions?"
- "Repeats: Dynamic context windows?"
- "Haplotypes: Phase-aware prediction?"

Title: "Long-Read Sequencing Expands VEP Scope"

Clean comparison diagram, white background. Professional emerging application figure.
```

### Caption

**Recommended Caption:**
"Long-read sequencing expands the scope of variant effect prediction. Short-read sequencing (top) detects primarily SNVs and small indels for which current FM-VEP approaches are well-suited. Long-read sequencing (bottom) reveals structural variants, repeat expansions, and complex haplotypes that current models cannot process. Realizing the clinical potential of long-read sequencing requires developing FM-VEP approaches for these new variant classes—a major open challenge."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 17.1 VEP Paradigms | 4 | Essential | Medium (comparison) |
| 17.2 AlphaMissense | 4 | Essential | Medium (architecture + results) |
| 17.3 Multi-Model | 4 | High | Medium (integration) |
| 17.4 Calibration | 4 | High | Medium (clinical) |
| 17.5 Uncertainty | 4 | High | Medium (quantification) |
| 17.6 Gains/Gaps | 4 | High | Medium (assessment) |
| 17.7 Long-Read VEP | 1 | Enhancing | Low (emerging) |

**Total files:** 25
**Recommended generation order:** 17.1A-D (paradigms), 17.2A-D (AlphaMissense), 17.4A-D (calibration), 17.5A-D (uncertainty), 17.3A-D (integration), 17.6A-D (gaps), 17.7 (long-read)

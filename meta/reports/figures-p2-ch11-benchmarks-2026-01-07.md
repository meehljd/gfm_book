# Figure Report: Chapter 11 - Benchmarks and Evaluation

**Chapter:** Part 2, Chapter 11 - Benchmarks and Evaluation
**Date:** 2026-01-07
**Figures:** 9 conceptual figures (14 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 11.1: Benchmark Landscape

**File:** `figs/part_2/ch11/01-fig-benchmark-landscape.svg`
**Priority:** Essential
**Type:** Landscape overview / taxonomy diagram

### Content Description

Overview map of genomic AI benchmarks organized by task category (variant effect, regulatory, expression, structure) and evaluation paradigm (zero-shot, linear probe, fine-tuning). Show major benchmarks with their characteristics: data source, task type, metrics, known limitations.

### DALL-E Prompt

```
Create a scientific landscape diagram showing genomic AI benchmark ecosystem. Save as: 01-fig-benchmark-landscape.svg

Matrix/landscape layout:

ROWS (Task Categories):
- Variant Effect Prediction
- Regulatory Element Classification
- Expression Prediction
- Protein Structure/Function

COLUMNS (Evaluation Paradigms):
- Zero-Shot
- Linear Probing
- Fine-Tuning

WITHIN CELLS:
- Benchmark names as boxes (e.g., "ClinVar", "ProteinGym", "ENCODE", "DMS assays")
- Color-coded by data quality/reliability
- Size indicates community adoption

ANNOTATIONS:
- Data source icons (clinical database, experimental assay)
- Warning symbols for known limitations
- Connection lines showing benchmark overlaps

Clean scientific taxonomy diagram with organized grid layout. Blue/green color scheme. White background. Professional benchmark ecosystem map.
```

### Post-Processing Notes

- Add benchmark names within appropriate cells
- Color-code by benchmark maturity/reliability
- Include legend for icons and colors
- Add annotations for known issues (leakage, saturation)

### Fallback Description

Create in diagramming software:
- Grid layout with task rows and paradigm columns
- Benchmark names as labeled boxes within cells
- Color coding and icons for characteristics

### Caption

**Recommended Caption:**
"The genomic AI benchmark landscape organized by task category (rows) and evaluation paradigm (columns). Major benchmarks are positioned according to what they test: variant effect prediction relies on ClinVar, DMS assays, and ProteinGym; regulatory classification uses ENCODE and custom enhancer datasets; expression prediction evaluates against GTEx and tissue-specific measurements; protein structure benchmarks include CASP and AlphaFold evaluations. Evaluation paradigms range from zero-shot (no task-specific training) through linear probing (frozen embeddings) to full fine-tuning. Color intensity indicates benchmark maturity and community adoption. Warning symbols mark benchmarks with known limitations including potential leakage or approaching saturation."

---

## Figure 11.2: Leakage Pathways

**File:** `figs/part_2/ch11/02-fig-leakage-pathways.svg`
**Priority:** High
**Type:** Flow diagram with warning highlights

### Content Description

Flow diagram showing data flow with leakage pathways highlighted:
- Central pipeline: Pretraining → Foundation Model → Fine-tuning → Benchmark
- Leakage pathways (red): Direct overlap, homology leakage, label circularity, resource sharing, community iteration
- Specific examples: ESM/UniRef → ProteinGym, ClinVar/CADD circularity, ENCODE in both pretraining and evaluation

### DALL-E Prompt

```
Create a scientific flow diagram showing data leakage pathways in genomic AI. Save as: 02-fig-leakage-pathways.svg

Main pipeline (horizontal, blue arrows):
Pretraining Data → Foundation Model → Fine-tuning → Benchmark Evaluation

LEAKAGE PATHWAYS (red dashed lines with warning symbols):

1. Direct Overlap: Red arrow from pretraining to benchmark
   - Example: "UniRef sequences in ProteinGym"

2. Homology Leakage: Red curved arrow showing sequence similarity
   - Example: "80% identity between train/test proteins"

3. Label Circularity: Red bidirectional arrow
   - Example: "CADD→ClinVar→New predictors→ClinVar"

4. Resource Sharing: Red connection between stages
   - Example: "ENCODE in pretraining and evaluation"

5. Community Iteration: Red loop back
   - Example: "Benchmark overfitting across publications"

Legitimate flow in blue, leakage in red dashed. Warning triangles at each leakage point. Clean scientific diagram with white background. Professional data flow and leakage visualization.
```

### Post-Processing Notes

- Use consistent color coding: blue for legitimate flow, red for leakage
- Add specific example annotations for each leakage type
- Include warning symbols at leakage points
- Add legend distinguishing pathway types

### Fallback Description

Create in diagramming software:
- Horizontal pipeline with boxes for each stage
- Red dashed arrows for leakage pathways
- Warning symbols and example annotations

### Caption

**Recommended Caption:**
"Data leakage pathways in genomic foundation model evaluation. The legitimate pipeline (blue) flows from pretraining through fine-tuning to benchmark evaluation. Leakage pathways (red dashed) create spurious performance: direct overlap when pretraining includes benchmark sequences; homology leakage when training and test sets share high-similarity sequences; label circularity when computational predictions influence ground truth labels that later serve as training targets; resource sharing when databases like ENCODE appear in both pretraining and evaluation; and community iteration when the field collectively overfits to standard benchmarks through publication cycles. Each pathway inflates apparent performance without improving genuine biological understanding."

---

## Figure 11.3: Benchmark Saturation (Two-Panel)

**Files:**
- `figs/part_2/ch11/03-A-fig-benchmark-saturation.svg`
- `figs/part_2/ch11/03-B-fig-benchmark-saturation.svg`

**Priority:** High
**Type:** Temporal analysis plots

### Panel A: Saturation Curve

**Content:** Time vs. benchmark performance showing multiple model generations approaching a performance ceiling. Saturation zone annotation where improvements become marginal.

**DALL-E Prompt:**
```
Create a scientific plot showing benchmark performance saturation over time. Save as: 03-A-fig-benchmark-saturation.svg

Plot elements:
- X-axis: Year (2018-2025)
- Y-axis: Benchmark Performance (e.g., auROC 0.7-1.0)
- Multiple lines for different model generations converging toward ceiling
- Horizontal dashed line at ~0.95 labeled "Performance Ceiling"
- Shaded region near ceiling labeled "Saturation Zone"
- Individual points marking major model releases
- Diminishing gaps between successive models near ceiling

Model labels: "CADD", "REVEL", "ESM", "AlphaMissense"
Annotation: "Marginal improvements despite architectural advances"

Clean scientific temporal plot with legend, white background. Professional benchmark saturation analysis.
```

**Caption for Panel A:**
"Benchmark saturation over time. Multiple model generations (lines) improve performance on standard benchmarks but converge toward a ceiling (dashed line). The saturation zone (shaded) shows where improvements become marginal despite continued architectural advances. This pattern suggests either that the benchmark no longer discriminates between methods or that genuine performance limits have been reached."

### Panel B: Benchmark Staleness Timeline

**Content:** Timeline showing benchmark creation dates versus current year, highlighting growing temporal gap between benchmark construction and model evaluation.

**DALL-E Prompt:**
```
Create a scientific timeline showing benchmark staleness. Save as: 03-B-fig-benchmark-saturation.svg

Timeline layout:
- Horizontal axis: Years (2010-2025)
- Top row: Benchmark creation dates as markers
  - "ENCODE 2012", "ClinVar 2013", "ProteinGym 2022"
- Bottom row: "Current evaluation year" marker at 2025
- Vertical connecting lines with gap annotations
- Color gradient from green (recent) to red (stale)
- Growing gap visualization as widening bracket

Annotations:
- "10+ year gap for ENCODE benchmarks"
- "Biology evolves, benchmarks don't"

Clean timeline diagram with staleness indicators. White background. Professional temporal benchmark analysis.
```

**Caption for Panel B:**
"Benchmark staleness timeline. Benchmark creation dates (top) versus current evaluation (bottom) reveal growing temporal gaps. ENCODE-based benchmarks reflect 2012-era annotations; ClinVar benchmarks evolve but retain historical biases; even recent benchmarks like ProteinGym become stale as the field iterates. The gap between when benchmarks were constructed and when they are used for evaluation grows each year, potentially measuring performance on outdated or superseded annotations."

### Combined Caption

**Full Figure Caption:**
"Benchmark saturation and staleness limit evaluation validity. (A) Performance saturation: multiple model generations converge toward benchmark ceilings where marginal improvements no longer indicate meaningful advances. The saturation zone (shaded) suggests benchmarks have lost discriminative power. (B) Benchmark staleness: growing temporal gaps between benchmark creation and current evaluation. Benchmarks created years ago may reflect outdated annotations, superseded biological understanding, or distributions that no longer match contemporary data. Together, saturation and staleness motivate development of new benchmarks that capture aspects of biological prediction that current standards miss."

---

## Figure 11.4: Proxy-Target Gap

**File:** `figs/part_2/ch11/04-fig-proxy-target-gap.svg`
**Priority:** Essential
**Type:** Conceptual gap diagram

### Content Description

Conceptual diagram showing the gap between what benchmarks measure (proxies) and what we actually want (targets):
- Left column: What we measure (ClinVar labels, held-out auROC, DMS correlation, expression prediction accuracy)
- Right column: What we want (True clinical impact, deployment discrimination, actual protein function, regulatory mechanism)
- Center: Arrows with gap indicators showing how well proxies align with targets
- Gap factors: label quality, distribution shift, metric mismatch, temporal drift

### DALL-E Prompt

```
Create a scientific diagram showing the proxy-target gap in benchmark evaluation. Save as: 04-fig-proxy-target-gap.svg

Two-column layout with center gap indicators:

LEFT COLUMN "What We Measure" (blue boxes):
- "ClinVar pathogenicity labels"
- "Held-out auROC"
- "DMS correlation"
- "Expression prediction R²"

RIGHT COLUMN "What We Want" (green boxes):
- "True clinical impact"
- "Deployment discrimination"
- "Actual protein function"
- "Regulatory mechanism"

CENTER (Gap indicators):
- Arrows connecting proxies to targets
- Arrow width indicates proxy strength (thick = good proxy, thin = poor proxy)
- Gap labels: "Label quality gap", "Distribution shift", "Metric mismatch", "Temporal drift"
- Red zones highlighting where gaps are largest

Bottom annotation: "High benchmark performance ≠ deployment success"

Clean conceptual diagram with color-coded columns and gap visualization. White background. Professional evaluation validity figure.
```

### Post-Processing Notes

- Vary arrow widths to indicate proxy quality
- Color-code gap severity (green for good alignment, red for poor)
- Add specific examples for each gap type
- Include key insight annotation

### Fallback Description

Create in diagramming software:
- Two-column layout with connecting arrows
- Gap annotations and width variation
- Color coding for alignment quality

### Caption

**Recommended Caption:**
"The proxy-target gap in genomic AI evaluation. What benchmarks measure (left) differs systematically from what we ultimately want (right). ClinVar labels proxy for clinical impact but reflect curation biases and circularity with computational predictions. Held-out auROC proxies for deployment discrimination but assumes matched distributions. DMS correlations proxy for protein function but capture only selected perturbations in specific assay conditions. Expression prediction accuracy proxies for regulatory understanding but may reflect technical confounds. Arrow widths indicate proxy strength; gap annotations identify sources of misalignment. The central insight: high benchmark performance does not guarantee deployment success."

---

## Figure 11.5: Cross-Population Performance

**File:** `figs/part_2/ch11/05-fig-cross-population-performance.svg`
**Priority:** High
**Type:** Grouped performance comparison

### Content Description

Grouped bar chart or heatmap showing:
- Rows: Different tasks/models
- Columns: Ancestry groups (European, African, East Asian, South Asian, Admixed)
- Values: Performance metrics with clear degradation for non-European groups
- Annotations: sample sizes, significance, training data representation

### DALL-E Prompt

```
Create a scientific grouped bar chart showing cross-population model performance. Save as: 05-fig-cross-population-performance.svg

Chart structure:
- X-axis groups: "European", "African", "East Asian", "South Asian", "Admixed"
- Y-axis: "Relative Performance" (0-100%)
- Multiple bar colors for different model types:
  - Blue: Polygenic risk scores
  - Green: Variant classifiers
  - Orange: Regulatory predictors

Performance pattern:
- European: ~100% (reference)
- African: ~40-60% (major degradation)
- East Asian: ~70-80%
- South Asian: ~65-75%
- Admixed: ~55-70%

Annotations:
- Sample size indicators above each group
- Error bars on all bars
- Training data composition pie chart inset showing ~78% European
- Key finding: "40-75% performance reduction for African ancestry"

Clean grouped bar chart with legend and annotations. White background. Professional cross-population evaluation figure.
```

### Post-Processing Notes

- Add sample size annotations for each population
- Include error bars for uncertainty
- Add inset showing training data composition
- Highlight key finding about performance reduction

### Fallback Description

Create in matplotlib/seaborn:
- Grouped bar chart with ancestry on x-axis
- Multiple model types as bar colors
- Error bars and annotations

### Caption

**Recommended Caption:**
"Cross-population performance reveals systematic failures for underrepresented ancestries. Relative performance (European as reference) degrades substantially for non-European groups across multiple model types: polygenic risk scores (blue), variant classifiers (green), and regulatory predictors (orange). African-ancestry individuals show 40-75% performance reductions despite constituting only 2% of typical training data while representing 16% of the global population. These disparities reflect both training data composition (inset: ~78% European) and fundamental differences in linkage disequilibrium structure across populations. Aggregate benchmark metrics that do not report stratified performance by ancestry conceal these failures."

---

## Figure 11.6: Random Splits Fail (Three-Panel)

**Files:**
- `figs/part_2/ch11/06-A-fig-random-splits-fail.svg`
- `figs/part_2/ch11/06-B-fig-random-splits-fail.svg`
- `figs/part_2/ch11/06-C-fig-random-splits-fail.svg`

**Priority:** Essential
**Type:** Comparison showing why random splits fail for genomic data

### Panel A: Image Classification (Random Works)

**Content:** Grid of independent images where random assignment to train/test works because examples are truly independent.

**DALL-E Prompt:**
```
Create a scientific diagram showing random splits work for images. Save as: 06-A-fig-random-splits-fail.svg

Grid layout:
- 4x4 grid of small image icons (simple shapes/objects)
- Random color coding: blue for training, orange for test
- No connections between images (independent)
- Label: "Images: Independent samples"
- Checkmark annotation: "Random splits valid"

Clean grid diagram with colored assignment, white background. Professional data splitting example.
```

**Caption for Panel A:**
"Random splits are valid for independent samples. In image classification, each image is an independent sample from the data distribution. Random assignment to training (blue) and test (orange) sets provides unbiased performance estimates because seeing one image provides no information about others."

### Panel B: Protein Classification (Random Fails)

**Content:** Protein family tree showing how random splits place homologous proteins across train/test, creating memorization pathway.

**DALL-E Prompt:**
```
Create a scientific diagram showing random splits fail for proteins. Save as: 06-B-fig-random-splits-fail.svg

Tree structure:
- Phylogenetic/family tree with protein nodes
- Random coloring: blue (train) and orange (test) mixed within families
- Dashed lines showing high sequence identity (80%) between train and test
- Warning annotation: "80% identity between train/test"
- Memorization pathway highlighted: "Model memorizes similar sequences"
- Label: "Proteins: Related by evolution"
- X mark annotation: "Random splits create leakage"

Clean family tree diagram with warning highlights, white background. Professional homology leakage illustration.
```

**Caption for Panel B:**
"Random splits fail for evolutionarily related sequences. Proteins share evolutionary history, and random assignment places close homologs (>80% sequence identity) across train and test sets. The model can achieve high test accuracy by memorizing sequence patterns shared between related proteins rather than learning generalizable biological features. This homology leakage inflates apparent performance."

### Panel C: Variant Prediction (Multiple Failure Modes)

**Content:** Gene diagram with variants showing how random splits fail due to same gene in train/test, family members spanning splits, and population structure.

**DALL-E Prompt:**
```
Create a scientific diagram showing multiple failure modes for variant splits. Save as: 06-C-fig-random-splits-fail.svg

Multi-level diagram:

TOP: Gene diagram with multiple variant positions
- Same gene has variants in train (blue) and test (orange)
- Warning: "Same gene in train/test"

MIDDLE: Family pedigree
- Related individuals split across train/test
- Warning: "Family members share rare variants"

BOTTOM: Population structure (PCA-style clusters)
- Different ancestries unevenly split
- Warning: "Population structure confounds"

All levels marked with X for random split failure. Label: "Variants: Multiple dependencies"

Clean multi-level warning diagram, white background. Professional variant splitting failure illustration.
```

**Caption for Panel C:**
"Variant prediction faces multiple random split failure modes. Gene-level: random splits place different variants from the same gene in train and test, allowing memorization of gene-specific patterns. Family-level: related individuals sharing rare variants may span splits, enabling memorization of family-specific haplotypes. Population-level: ancestry structure correlates with variant frequencies and phenotypes, creating confounding that random splits do not address. Proper evaluation requires splits that account for all these dependencies."

### Combined Caption

**Full Figure Caption:**
"Why random data splits fail for genomic machine learning. (A) Image classification: samples are truly independent, so random assignment provides valid performance estimates. (B) Protein classification: evolutionary relationships create dependencies; random splits place homologs (>80% identity) across train/test, enabling memorization of shared sequences rather than learning generalizable features. (C) Variant prediction: multiple dependencies compound—same genes across splits, related individuals sharing rare variants, and population structure confounding features and labels. These dependencies require structured splitting strategies that explicitly account for sequence homology, family relatedness, and population structure."

---

## Figure 11.7: Homology-Aware Splitting

**File:** `figs/part_2/ch11/07-fig-homology-splitting.svg`
**Priority:** Essential
**Type:** Step-by-step workflow

### Content Description

Workflow showing proper homology-aware splitting:
1. All sequences input
2. Clustering (CD-HIT/MMseqs2 at threshold)
3. Cluster visualization showing grouped similar sequences
4. Split assignment with entire clusters to train/val/test
5. Validation check: no test sequence >X% identity to any training sequence

### DALL-E Prompt

```
Create a scientific workflow diagram for homology-aware data splitting. Save as: 07-fig-homology-splitting.svg

Step-by-step flow (top to bottom or left to right):

STEP 1: "Input Sequences"
- Multiple sequence icons scattered

STEP 2: "Cluster by Identity"
- CD-HIT/MMseqs2 tool icon
- Parameter: "e.g., 30% identity threshold"

STEP 3: "Cluster Visualization"
- Grouped sequences in colored clusters
- Lines connecting similar sequences within clusters

STEP 4: "Assign Entire Clusters"
- Clusters colored: blue (train), yellow (val), orange (test)
- Entire cluster goes to one split only

STEP 5: "Validate Separation"
- Check icon: "No test >30% identity to train"
- Checkmark for proper separation

Comparison table at bottom:
| Strategy | Threshold | Strictness | Use Case |
| Random | None | None | Never for homologous |
| 50% | CD-HIT | Moderate | Fold recognition |
| 30% | MMseqs2 | High | Function prediction |

Clean workflow diagram with numbered steps, white background. Professional homology splitting guide.
```

### Post-Processing Notes

- Add tool names and parameters at clustering step
- Include comparison table for different stringency levels
- Add checkmark/validation step prominently
- Use consistent color coding throughout

### Fallback Description

Create in diagramming software:
- Vertical or horizontal workflow with numbered steps
- Cluster visualization with colored groups
- Validation checkpoint with success criteria

### Caption

**Recommended Caption:**
"Homology-aware splitting prevents sequence similarity leakage. Step 1: Start with all sequences in the dataset. Step 2: Cluster sequences by similarity using tools like CD-HIT or MMseqs2 at an appropriate threshold (30% identity typical for diverse protein tasks). Step 3: Visualize clusters showing which sequences are related. Step 4: Assign entire clusters to single splits—no cluster is divided across train/validation/test. Step 5: Validate that no test sequence exceeds the identity threshold with any training sequence. The threshold determines evaluation stringency: 30% identity tests distant generalization; 50% tests moderate generalization; higher thresholds permit more similarity but provide weaker generalization evidence."

---

## Figure 11.8: Splitting Strategies Comparison

**File:** `figs/part_2/ch11/08-fig-splitting-strategies.svg`
**Priority:** High
**Type:** Matrix/comparison table

### Content Description

Matrix comparing splitting strategies against what they test:
- Rows: Random, individual-aware, family-aware, chromosome, gene/protein family, cohort/site, temporal, ancestry
- Columns: Sequence generalization, individual generalization, population robustness, temporal robustness, cross-site generalization
- Cells: checkmark, X, or tilde for partial

### DALL-E Prompt

```
Create a scientific comparison matrix for data splitting strategies. Save as: 08-fig-splitting-strategies.svg

Matrix layout:

ROWS (Splitting Strategies):
1. Random
2. Individual-aware
3. Family-aware
4. Chromosome holdout
5. Gene/protein family
6. Cohort/site holdout
7. Temporal split
8. Ancestry stratified

COLUMNS (What It Tests):
- Sequence Generalization
- Individual Generalization
- Population Robustness
- Temporal Robustness
- Cross-Site Transfer

CELLS:
- Green checkmark: Strategy tests this capability
- Red X: Strategy does not address this
- Yellow tilde: Partial/depends on implementation

Small schematic icons next to each row showing the splitting approach visually.

Side annotations:
- Performance drop expectations
- "Strategies are combinable"
- "Stricter splits = lower but more realistic scores"

Clean matrix diagram with color-coded cells, white background. Professional splitting strategy comparison.
```

### Post-Processing Notes

- Use clear icons (✓, ✗, ~) in cells
- Add small visual schematics for each strategy
- Include notes about combinability
- Color-code by evaluation strength

### Fallback Description

Create in spreadsheet or diagramming software:
- Table with strategies as rows, tests as columns
- Symbol coding for capability coverage
- Visual icons for each strategy type

### Caption

**Recommended Caption:**
"Splitting strategies test different aspects of generalization. Each strategy (rows) addresses specific dependencies (columns): random splits address none; individual-aware prevents sample-level leakage; family-aware accounts for relatedness; chromosome holdout tests cross-genome transfer; gene/protein family prevents homology leakage; cohort/site holdout tests deployment robustness; temporal splits simulate prospective use; ancestry stratification reveals population biases. No single strategy addresses all dependencies; rigorous evaluation combines multiple strategies. Stricter splits produce lower but more realistic performance estimates that better predict clinical deployment success."

---

## Figure 11.9: Foundation Model Evaluation Paradigms (Three-Panel)

**Files:**
- `figs/part_2/ch11/09-A-fig-fm-evaluation-paradigms.svg`
- `figs/part_2/ch11/09-B-fig-fm-evaluation-paradigms.svg`
- `figs/part_2/ch11/09-C-fig-fm-evaluation-paradigms.svg`

**Priority:** Enhancing
**Type:** Paradigm comparison

### Panel A: Zero-Shot Evaluation

**Content:** Frozen model with direct prediction. Shows that zero-shot tests alignment between pretraining and task. Example: ESM-1v log-likelihood scoring.

**DALL-E Prompt:**
```
Create a scientific diagram showing zero-shot foundation model evaluation. Save as: 09-A-fig-fm-evaluation-paradigms.svg

Diagram elements:
- Large "Foundation Model" box (frozen, grayed)
- Input: "Sequence" arrow entering
- Output: "Direct Prediction" arrow exiting
- No additional training components
- Label: "ZERO-SHOT"

Annotation box:
- "Tests: Pretraining-task alignment"
- "Example: ESM-1v log-likelihood"
- "Pro: No task data needed"
- "Con: Limited to aligned tasks"

Blue/gray color scheme for frozen components. Clean architecture diagram, white background. Professional zero-shot evaluation figure.
```

**Caption for Panel A:**
"Zero-shot evaluation uses frozen model outputs directly without task-specific training. The model produces predictions based solely on patterns learned during pretraining. This paradigm tests alignment between pretraining objectives and downstream tasks—success indicates that pretraining implicitly captured task-relevant features. Example: ESM-1v uses sequence log-likelihoods for variant effect prediction without seeing pathogenicity labels during training."

### Panel B: Linear Probing

**Content:** Frozen embeddings with trained linear classifier. Shows that probing tests linear accessibility of task-relevant features.

**DALL-E Prompt:**
```
Create a scientific diagram showing linear probing evaluation. Save as: 09-B-fig-fm-evaluation-paradigms.svg

Diagram elements:
- Large "Foundation Model" box (frozen, grayed)
- "Embeddings" intermediate output
- Small "Linear Classifier" box (trainable, blue/green)
- Final "Prediction" output
- Label: "LINEAR PROBING"

Annotation box:
- "Tests: Linear feature accessibility"
- "Isolates representation quality"
- "Pro: Low data requirement"
- "Con: May miss nonlinear patterns"

Frozen components in gray, trainable in colored. Clean architecture diagram, white background. Professional probing evaluation figure.
```

**Caption for Panel B:**
"Linear probing freezes foundation model embeddings and trains only a linear classifier on top. This paradigm isolates representation quality from adaptation capacity—if a simple linear model achieves strong performance, the pretrained representations encode task-relevant features in accessible form. Linear probing requires minimal labeled data and provides clean evidence about what the foundation model learned during pretraining."

### Panel C: Fine-Tuning

**Content:** Gradients through entire model showing full adaptation. Shows that fine-tuning tests total potential but conflates representation with adaptation quality.

**DALL-E Prompt:**
```
Create a scientific diagram showing fine-tuning evaluation. Save as: 09-C-fig-fm-evaluation-paradigms.svg

Diagram elements:
- Large "Foundation Model" box (trainable, colored)
- Gradient arrows flowing through entire model
- "Task Head" box (trainable, colored)
- Final "Prediction" output
- Label: "FINE-TUNING"

Annotation box:
- "Tests: Total model potential"
- "Conflates representation + adaptation"
- "Pro: Best absolute performance"
- "Con: High data requirement, overfitting risk"

All components colored to show trainability. Gradient flow arrows. Clean architecture diagram, white background. Professional fine-tuning evaluation figure.
```

**Caption for Panel C:**
"Fine-tuning updates all model parameters during task-specific training, testing total model potential. This paradigm achieves the highest absolute performance but conflates representation quality with adaptation capacity—strong fine-tuned performance may reflect good pretraining, good adaptation, or both. Fine-tuning requires substantial labeled data and carries overfitting risk, making it less diagnostic of foundation model quality than zero-shot or probing approaches."

### Combined Caption

**Full Figure Caption:**
"Foundation model evaluation paradigms test different capabilities. (A) Zero-shot: frozen model predictions test whether pretraining captured task-relevant patterns; requires no task data but limited to aligned tasks. (B) Linear probing: frozen embeddings with learned linear classifier test whether task features are linearly accessible in representations; requires minimal data and isolates representation quality. (C) Fine-tuning: full gradient updates test total potential but conflate representation and adaptation; achieves best performance but requires substantial data. The value of pretraining is best measured by the gap between few-shot and from-scratch performance—large gaps indicate that pretraining provides transferable features beyond what task data alone would support."

---

## Figure 11.10: Metric Selection Flowchart

**File:** `figs/part_2/ch11/10-fig-metric-selection.svg`
**Priority:** High
**Type:** Decision flowchart

### Content Description

Flowchart guiding metric selection based on:
- Binary vs. continuous outcomes
- Balanced vs. imbalanced classes
- Ranking vs. probability requirements
- Clinical decision needs

### DALL-E Prompt

```
Create a scientific flowchart for evaluation metric selection. Save as: 10-fig-metric-selection.svg

Decision tree structure:

ROOT: "What type of prediction?"

LEVEL 1: "Binary or Continuous?"
- Binary → next decision
- Continuous → "Correlation (Pearson/Spearman), MSE, MAE"

LEVEL 2 (Binary): "Class balance?"
- Balanced → "Accuracy, auROC"
- Imbalanced → next decision

LEVEL 3 (Imbalanced): "Ranking or Probability?"
- Ranking → "auPRC (NOT auROC alone)"
- Probability → "Calibration (Brier score, reliability diagram)"

LEVEL 4: "Clinical decision making?"
- Yes → "Net benefit, decision curve analysis"
- No → standard metrics

WARNING CALLOUTS:
- "auROC invariant to class imbalance!"
- "High correlation ≠ clinically meaningful"
- "Calibration essential for deployment"

Color-coded terminals by metric type. Clean flowchart with decision diamonds, white background. Professional metric selection guide.
```

### Post-Processing Notes

- Add warning callouts for common pitfalls
- Color-code metric recommendations by use case
- Include brief descriptions at terminal nodes
- Add examples for each metric type

### Fallback Description

Create in flowchart software:
- Decision tree with binary questions
- Terminal nodes with metric recommendations
- Warning annotations for common mistakes

### Caption

**Recommended Caption:**
"Metric selection depends on task characteristics and deployment requirements. Binary classification requires different metrics depending on class balance: auROC provides stable ranking assessment for balanced data, while auPRC is essential for imbalanced settings where auROC can mislead. Probability calibration matters for deployment: a model may rank correctly while producing systematically overconfident probabilities. Clinical decision-making requires metrics like net benefit that account for the costs of different error types. Continuous predictions use correlation and error metrics, but high correlation does not guarantee clinical utility—a model may track relative differences while failing to capture absolute effect sizes. Selecting appropriate metrics prevents optimizing for misleading targets."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 11.1 Benchmark Landscape | 1 | Essential | High (taxonomy) |
| 11.2 Leakage Pathways | 1 | High | Medium (flow diagram) |
| 11.3 Saturation | 2 | High | Medium (temporal plots) |
| 11.4 Proxy-Target Gap | 1 | Essential | Medium (conceptual) |
| 11.5 Cross-Population | 1 | High | Medium (bar chart) |
| 11.6 Random Splits Fail | 3 | Essential | Medium (comparison) |
| 11.7 Homology Splitting | 1 | Essential | Medium (workflow) |
| 11.8 Splitting Strategies | 1 | High | Medium (matrix) |
| 11.9 FM Evaluation | 3 | Enhancing | Medium (paradigm comparison) |
| 11.10 Metric Selection | 1 | High | Medium (flowchart) |

**Total files:** 15
**Recommended generation order:** 11.6A-C (random splits fail, foundational), 11.7 (homology splitting), 11.4 (proxy-target gap), 11.2 (leakage), 11.10 (metrics), 11.5 (cross-population), 11.8 (strategies matrix), 11.3A-B (saturation), 11.1 (landscape), 11.9A-C (FM paradigms)

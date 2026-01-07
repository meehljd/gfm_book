# Figure Report: Chapter 12 - Confounding and Data Leakage

**Chapter:** Part 2, Chapter 12 - Confounding and Data Leakage
**Date:** 2026-01-07
**Figures:** 6 conceptual figures (10 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 12.1: Confounding DAG

**File:** `figs/part_2/ch12/01-fig-confounding-dag.svg`
**Priority:** Essential
**Type:** Causal diagram (DAG)

### Content Description

Directed acyclic graph (DAG) showing confounding structure with genomic example:
- Main DAG: Confounder (Ancestry) with arrows to Exposure (Genomic features) and Outcome (Disease status)
- Spurious path X ← C → Y highlighted
- Annotation boxes explaining how ancestry affects both
- Second DAG showing adjustment blocking spurious path
- Concrete example: Rare disease clinic → ClinVar submissions → ancestry proxy learned

### DALL-E Prompt

```
Create a scientific causal diagram (DAG) showing confounding in genomic AI. Save as: 01-fig-confounding-dag.svg

TWO-PANEL layout:

PANEL 1 "Confounding Structure":
- Circle node "C" at top labeled "Confounder (Ancestry)"
- Circle node "X" at bottom-left labeled "Features (Genotypes)"
- Circle node "Y" at bottom-right labeled "Outcome (Disease)"
- Arrow from C to X (ancestry affects genotype frequencies)
- Arrow from C to Y (ancestry affects disease via non-genetic paths)
- Optional arrow X to Y (true causal path, dashed)
- Spurious path C→X and C→Y highlighted in RED
- Annotation: "Model learns X-Y association via C, not biology"

PANEL 2 "After Adjustment":
- Same nodes but confounder C is boxed/conditioned
- Spurious paths blocked (grayed out)
- Only true X→Y path remains (if it exists)
- Annotation: "Conditioning on C blocks spurious association"

CONCRETE EXAMPLE box:
"Rare disease clinic (European) → ClinVar submissions → Model learns ancestry as pathogenicity proxy"

Clean causal DAG style with circles for variables, arrows for causal effects. White background. Professional epidemiology/ML confounding diagram.
```

### Post-Processing Notes

- Use standard DAG notation (circles for variables, arrows for causal effects)
- Highlight spurious paths in red/warning color
- Show conditioning with box around conditioned variable
- Include concrete genomic example in annotation

### Fallback Description

Create in DAGitty or diagramming software:
- Standard causal DAG with three nodes
- Two-panel showing before/after adjustment
- Color-coded spurious vs. causal paths

### Caption

**Recommended Caption:**
"Confounding structure in genomic prediction. (Left) Ancestry acts as a confounder, affecting both genomic features (through population-specific allele frequencies) and disease outcomes (through environmental, socioeconomic, and healthcare pathways). The spurious path (red) creates association between features and outcomes that models exploit as shortcuts. (Right) Conditioning on ancestry blocks the spurious path, isolating any genuine feature-outcome relationship. Concrete example: a rare disease clinic serving primarily European patients contributes most pathogenic variants to ClinVar, creating an ancestry-pathogenicity correlation that models learn instead of biological mechanisms. The central challenge: shortcuts appear to work until deployment shifts the confounder-outcome relationship."

---

## Figure 12.2: Population Structure as Shortcut (Four-Panel)

**Files:**
- `figs/part_2/ch12/02-A-fig-population-structure-shortcut.svg`
- `figs/part_2/ch12/02-B-fig-population-structure-shortcut.svg`
- `figs/part_2/ch12/02-C-fig-population-structure-shortcut.svg`
- `figs/part_2/ch12/02-D-fig-population-structure-shortcut.svg`

**Priority:** Essential
**Type:** Multi-panel evidence figure

### Panel A: PCA of Genomic Data

**Content:** PC1 vs PC2 plot showing clear ancestry clustering. Points colored by ancestry group demonstrating that genetic variation is structured by population.

**DALL-E Prompt:**
```
Create a scientific PCA plot showing genomic population structure. Save as: 02-A-fig-population-structure-shortcut.svg

Scatter plot elements:
- X-axis: "PC1" (principal component 1)
- Y-axis: "PC2" (principal component 2)
- Clear clusters by ancestry:
  - European cluster (blue, largest)
  - African cluster (orange)
  - East Asian cluster (green)
  - South Asian cluster (purple)
  - Admixed points between clusters (gray)
- Cluster labels or legend
- Title: "Genetic Variation is Structured by Ancestry"

Clean scientific PCA plot with distinct clusters, white background. Professional population genetics visualization.
```

**Caption for Panel A:**
"Population structure in genomic data. Principal component analysis of genome-wide variants reveals clear clustering by ancestry. PC1 and PC2 capture continental-scale genetic variation reflecting demographic history. This structure means that ancestry information is implicitly encoded in genotype data even when not explicitly provided—models can learn to predict ancestry from genetic features."

### Panel B: Ancestry in K-mer Frequencies

**Content:** Heatmap showing that even local sequence composition (k-mer frequencies) differs by population, demonstrating that ancestry signal permeates sequence data.

**DALL-E Prompt:**
```
Create a scientific heatmap showing k-mer frequency differences by ancestry. Save as: 02-B-fig-population-structure-shortcut.svg

Heatmap elements:
- Rows: Different k-mers (e.g., 6-mers, showing ~20 representative)
- Columns: Ancestry groups (European, African, East Asian, South Asian)
- Color intensity: Relative k-mer frequency (blue-white-red diverging)
- Clear differences visible between populations
- Title: "Even Local Sequence Composition Differs"
- Annotation: "Foundation models see ancestry in sequence"

Clean bioinformatics heatmap with population columns, white background. Professional k-mer analysis figure.
```

**Caption for Panel B:**
"Ancestry encoded in local sequence composition. Heatmap of k-mer frequencies across ancestry groups reveals systematic differences even in short sequence patterns. Foundation models processing raw sequences have access to this ancestry signal regardless of whether ancestry labels are provided. This enables models to learn ancestry as a feature—beneficial for population genetics applications but problematic when ancestry confounds the target prediction."

### Panel C: The Shortcut Pathway

**Content:** Flow diagram showing how ancestry creates a shortcut: Ancestry → Sequencing site → Labels (one path) and Ancestry → Allele frequencies → Features (another path). Model learns via ancestry rather than biology.

**DALL-E Prompt:**
```
Create a scientific flow diagram showing the ancestry shortcut pathway. Save as: 02-C-fig-population-structure-shortcut.svg

Flow diagram:
CENTRAL NODE: "Ancestry"

PATH 1 (to labels):
Ancestry → "Healthcare access" → "Sequencing site" → "Label quality/presence"
(Red arrow labeled "Non-biological pathway")

PATH 2 (to features):
Ancestry → "LD patterns" → "Allele frequencies" → "Genetic features"
(Blue arrow labeled "Feature pathway")

BOTTOM: "Model" box receiving both pathways
Annotation: "Model learns ancestry as shortcut to labels"

WARNING: "Shortcut works in training, fails at deployment"

Clean flow diagram with pathway arrows, white background. Professional shortcut learning illustration.
```

**Caption for Panel C:**
"Ancestry creates shortcut pathways exploitable by models. Ancestry affects both labels (through healthcare access, sequencing site, and annotation quality) and features (through allele frequencies and linkage disequilibrium patterns). Models can achieve high training accuracy by learning the ancestry-label correlation rather than biological mechanisms. This shortcut works when training and test distributions share the same ancestry-label relationship but fails when that relationship changes—as when models trained on European-majority data are deployed on other populations."

### Panel D: Cross-Population Performance Degradation

**Content:** Bar chart showing 40-75% PGS reduction for non-European populations compared to European reference. Demonstrates that shortcuts fail when the relationship changes.

**DALL-E Prompt:**
```
Create a scientific bar chart showing PGS performance degradation. Save as: 02-D-fig-population-structure-shortcut.svg

Bar chart elements:
- X-axis: Ancestry groups (European [reference], African, East Asian, South Asian, Admixed)
- Y-axis: "Relative PGS Performance" (0-100%)
- European bar: 100% (reference, green)
- African bar: ~25-40% (major drop, red)
- East Asian bar: ~70-80% (moderate drop, yellow)
- South Asian bar: ~60-70% (moderate drop, yellow)
- Admixed bar: ~50-65% (significant drop, orange)

Annotations:
- "40-75% reduction for African ancestry"
- Arrow pointing to gap: "Shortcuts fail when relationship changes"
- Error bars on all estimates

Clean bar chart with degradation pattern, white background. Professional PGS portability figure.
```

**Caption for Panel D:**
"Shortcuts fail when ancestry-label relationships change. Polygenic risk scores (PGS) derived from European-ancestry GWAS show 40-75% reductions in prediction accuracy for African-ancestry individuals. The shortcut through ancestry-correlated features works for the training population but fails for populations where ancestry-phenotype relationships differ. This pattern—high training performance followed by deployment failure—is the signature of confounded prediction."

### Combined Caption

**Full Figure Caption:**
"Population structure creates exploitable shortcuts in genomic prediction. (A) PCA reveals clear ancestry clustering in genetic data. (B) Even local k-mer frequencies differ by ancestry, meaning foundation models have access to ancestry signal from raw sequences. (C) Ancestry creates dual pathways to both features (through allele frequencies) and labels (through healthcare access and annotation practices), enabling models to learn ancestry as a proxy for the target outcome. (D) The consequence: polygenic scores show 40-75% performance reduction when applied to non-European populations because ancestry-based shortcuts do not generalize. Higher model capacity does not solve confounding—it makes it worse by enabling detection of ever more subtle ancestry-linked features."

---

## Figure 12.3: Batch Effects (Three-Panel)

**Files:**
- `figs/part_2/ch12/03-A-fig-batch-effects.svg`
- `figs/part_2/ch12/03-B-fig-batch-effects.svg`
- `figs/part_2/ch12/03-C-fig-batch-effects.svg`

**Priority:** High
**Type:** Multi-panel batch effect evidence

### Panel A: Batch Structure in Embeddings

**Content:** UMAP visualization showing samples clustered by sequencing center rather than by phenotype. Demonstrates that batch effects dominate learned representations.

**DALL-E Prompt:**
```
Create a scientific UMAP plot showing batch structure dominates embeddings. Save as: 03-A-fig-batch-effects.svg

UMAP scatter plot:
- Clear clusters by sequencing center (not phenotype)
- Center A cluster (blue)
- Center B cluster (orange)
- Center C cluster (green)
- Within each cluster, cases (+) and controls (o) are mixed
- Title: "Embeddings Cluster by Batch, Not Phenotype"
- Annotation: "Model learns to distinguish centers, not disease"

Legend showing:
- Shape: Case vs Control
- Color: Sequencing Center

Clean UMAP with batch-dominated clustering, white background. Professional batch effect visualization.
```

**Caption for Panel A:**
"Embeddings cluster by batch rather than phenotype. UMAP projection of foundation model embeddings shows clear separation by sequencing center (colors) while cases (+) and controls (o) are mixed within each cluster. The model has learned batch-specific features rather than disease biology, achieving high apparent performance by distinguishing technical artifacts."

### Panel B: Coverage Patterns by Batch

**Content:** Genome browser-style tracks showing systematic coverage differences between sequencing centers. Different centers show different coverage profiles at the same genomic region.

**DALL-E Prompt:**
```
Create a scientific genome browser view showing coverage batch effects. Save as: 03-B-fig-batch-effects.svg

Browser-style layout:
- X-axis: Genomic position (e.g., chr1:1,000,000-1,100,000)
- Three horizontal tracks (coverage histograms):
  - "Center A": Specific coverage pattern (high at some regions)
  - "Center B": Different pattern (coverage dips at different positions)
  - "Center C": Yet another pattern
- Vertical dashed lines highlighting systematic differences
- Title: "Coverage Varies Systematically by Center"
- Annotation: "Same biology, different technical readout"

Clean genome browser style with coverage tracks, white background. Professional sequencing batch effect figure.
```

**Caption for Panel B:**
"Coverage patterns vary systematically by sequencing center. The same genomic region shows different coverage profiles depending on which center performed sequencing. These differences reflect instrument characteristics, capture kit biases, and processing pipelines rather than biological variation. Models can learn to recognize these center-specific signatures and use them as predictive features."

### Panel C: Batch Predicts Phenotype

**Content:** Contingency table showing case/control imbalance across batches. If batch is confounded with phenotype, models can exploit this.

**DALL-E Prompt:**
```
Create a scientific contingency table showing batch-phenotype confounding. Save as: 03-C-fig-batch-effects.svg

2x3 contingency table:
             Center A    Center B    Center C
Cases           800        100         100
Controls        100        800         100

Color coding:
- Cells with high counts: darker
- Shows clear imbalance: cases at Center A, controls at Center B

Annotation:
- Chi-square = highly significant
- "Batch perfectly predicts phenotype!"
- Warning: "Model predicting disease may actually predict sequencing center"

Clean contingency table with imbalance highlighted, white background. Professional confounding evidence figure.
```

**Caption for Panel C:**
"Batch-phenotype confounding enables trivial prediction. When cases and controls are processed at different centers, predicting batch is equivalent to predicting phenotype. A model achieving 90% disease classification accuracy may simply be recognizing which center processed the sample. This confounding is invisible in aggregate metrics but produces catastrophic failure when deployed on new data where batch-phenotype associations differ."

### Combined Caption

**Full Figure Caption:**
"Technical batch effects masquerade as biological signal. (A) Model embeddings cluster by sequencing center rather than by case/control status, revealing that learned representations capture technical rather than biological variation. (B) Coverage patterns at the same genomic region differ systematically by center, providing features models can exploit. (C) Batch-phenotype confounding occurs when cases and controls are imbalanced across centers—predicting batch becomes equivalent to predicting disease. Together, these panels illustrate why models can achieve high apparent performance while learning nothing about biology. Detection requires visualizing embeddings, examining coverage patterns, and testing whether batch identity predicts the outcome."

---

## Figure 12.4: Label Circularity

**File:** `figs/part_2/ch12/04-fig-label-circularity.svg`
**Priority:** High
**Type:** Circular flow diagram

### Content Description

Circular diagram showing how computational predictions influence labels that become training data for new predictors:
1. Clinical lab submits to ClinVar using CADD/REVEL as evidence
2. ClinVar aggregates (computational evidence influences labels)
3. New model trains on ClinVar (learns to replicate patterns)
4. New model used by labs (influences next submissions)
5. Return to step 1

Side panel: Breaking the cycle through prospective, temporal, or independent functional validation.

### DALL-E Prompt

```
Create a scientific circular flow diagram showing label circularity. Save as: 04-fig-label-circularity.svg

CIRCULAR FLOW (clockwise):

STEP 1: "Clinical Lab" box
- Arrow to Step 2
- Annotation: "Submits to ClinVar using CADD/REVEL as evidence"

STEP 2: "ClinVar Database" box
- Arrow to Step 3
- Annotation: "Aggregates submissions; computational evidence influences labels"

STEP 3: "New Predictor" box (highlighted)
- Arrow to Step 4
- Annotation: "Trains on ClinVar; learns to replicate existing patterns"

STEP 4: "Deployment" box
- Arrow back to Step 1
- Annotation: "Labs use new predictor; influences next submissions"

CENTER: Warning symbol with "CIRCULARITY"

SIDE PANEL "Breaking the Cycle":
- "Prospective validation (new variants)"
- "Temporal splits (train on old, test on new)"
- "Independent functional assays"

Circular arrow showing endless loop. Red warning highlights. Clean flow diagram, white background. Professional label circularity illustration.
```

### Post-Processing Notes

- Use clear circular layout showing feedback loop
- Highlight the problematic circularity in red/warning
- Include side panel with solutions
- Add annotations explaining each step

### Fallback Description

Create in diagramming software:
- Circular flow with 4-5 boxes
- Arrows showing cyclic information flow
- Warning annotation in center
- Solution panel on side

### Caption

**Recommended Caption:**
"Label circularity inflates apparent validation. Clinical laboratories submit variants to ClinVar using computational predictions (CADD, REVEL) as supporting evidence. ClinVar aggregates these submissions, creating labels that reflect historical computational predictions. New models trained on ClinVar learn to replicate these patterns, achieving high apparent accuracy through agreement with previous predictors rather than independent biological insight. When these new models are deployed, they influence the next generation of submissions, perpetuating the cycle. Breaking circularity requires prospective validation on newly discovered variants, temporal splits that train on historical data and test on recent annotations, or independent functional assay validation that bypasses computational predictions entirely."

---

## Figure 12.5: Confounding Detection Diagnostics

**File:** `figs/part_2/ch12/05-fig-confounding-detection.svg`
**Priority:** High
**Type:** Diagnostic checklist with visualizations

### Content Description

Comprehensive diagnostic checklist showing five detection approaches:
1. Confounder-only baseline: Compare full model vs. ancestry PCs only vs. batch only
2. Subgroup stratification: Performance by ancestry groups
3. Prediction-confounder association: Residual associations after controlling for label
4. Split sensitivity: Performance across different splitting strategies
5. Negative controls: Accuracy on outcomes unrelated to genetics

### DALL-E Prompt

```
Create a scientific diagnostic panel for confounding detection. Save as: 05-fig-confounding-detection.svg

FIVE-PANEL diagnostic layout:

PANEL 1 "Confounder-Only Baseline":
- Bar chart: "Full Model" (0.85), "Ancestry PCs Only" (0.80), "Batch Only" (0.75)
- Warning if simple baseline approaches full model
- Annotation: "If PCs alone predict well → confounding"

PANEL 2 "Stratified Performance":
- Multiple small bar charts by ancestry group
- European: 0.90, African: 0.60, Asian: 0.70
- Annotation: "Heterogeneity across groups suggests confounding"

PANEL 3 "Residual Association":
- Scatter plot: Prediction vs PC1, after controlling for true label
- Should show no association if model is not using ancestry
- Annotation: "Residual correlation with ancestry = confounding"

PANEL 4 "Split Sensitivity":
- Table: Random (0.92), Locus-level (0.78), Temporal (0.75)
- Large drops indicate leakage/memorization
- Annotation: "Performance should not depend on split type"

PANEL 5 "Negative Controls":
- Bar chart: "Genetics-related" (0.85), "Insurance type" (0.65), "Admin code" (0.60)
- Should be at chance for non-genetic outcomes
- Annotation: "Predicting admin outcomes = learned confounders"

Grid layout with five diagnostic panels. Clean scientific diagnostic figure, white background. Professional confounding detection guide.
```

### Post-Processing Notes

- Use grid layout for five panels
- Include interpretation guidance for each diagnostic
- Add warning indicators for concerning patterns
- Color-code by diagnostic result (green=OK, red=warning)

### Fallback Description

Create as multi-panel figure in plotting software:
- Grid of 5 small visualizations
- Each with specific diagnostic and interpretation
- Warning annotations for concerning patterns

### Caption

**Recommended Caption:**
"Diagnostic toolkit for detecting confounding. (1) Confounder-only baselines: if ancestry PCs alone approach full model performance, ancestry confounding is likely. (2) Stratified analysis: large performance gaps between ancestry groups suggest the model exploits group-specific shortcuts. (3) Residual association: predictions should not correlate with ancestry after controlling for the true label; residual correlation indicates ancestry encoding beyond what the task requires. (4) Split sensitivity: performance should not depend dramatically on splitting strategy; large drops under locus-level or temporal splits indicate memorization. (5) Negative controls: models should not predict outcomes unrelated to genetics (insurance type, administrative codes); above-chance prediction indicates learned confounders. Apply all diagnostics; confounding may manifest in only some."

---

## Figure 12.6: Mitigation Strategies Comparison

**File:** `figs/part_2/ch12/06-fig-mitigation-strategies.svg`
**Priority:** Enhancing
**Type:** Strategy comparison table/diagram

### Content Description

Comparison of mitigation strategies with their characteristics:
- Study design (matching): Before collection, reduces sample size
- Covariate adjustment: During training, may remove real signal
- Domain adaptation: Complex, requires implementation
- Robust optimization (Group DRO): Requires group labels
- Benchmark design: Stricter splits, harder scores

### DALL-E Prompt

```
Create a scientific comparison table for confounding mitigation strategies. Save as: 06-fig-mitigation-strategies.svg

Strategy comparison matrix:

COLUMNS:
- Strategy Name
- When Applied
- Requirements
- Main Trade-off
- Best For

ROWS:
1. Study Design/Matching | Before collection | Known confounders | Reduced sample size | Known major confounders
2. Covariate Adjustment | During training | Measured confounders | May remove real signal | Ancestry, batch correction
3. Residualization | Preprocessing | Linear confounding | Information loss | Strong linear effects
4. Adversarial Invariance | Training | Known groups | Reduced accuracy | Unknown variation
5. Group DRO | Training | Group labels | Worse average | Fairness-critical
6. Multi-site Training | Data collection | Multi-site access | Logistics | Institution effects
7. Temporal Splits | Evaluation | Timestamps | Smaller test set | Prospective deployment

Visual elements:
- Color coding by when applied (blue=design, green=training, orange=evaluation)
- Icons for each strategy type
- Annotation: "Approaches are complementary; use multiple"

Clean comparison table with organized columns, white background. Professional mitigation strategy guide.
```

### Post-Processing Notes

- Use color coding by intervention stage
- Add icons for visual distinction
- Include key annotation about combining strategies
- Format as clean comparison table

### Fallback Description

Create as formatted table:
- Strategy rows with characteristic columns
- Color coding by stage of intervention
- Notes on complementarity

### Caption

**Recommended Caption:**
"Mitigation strategies address confounding at different stages. Study design approaches (matching, balanced sampling) prevent confounding before data collection but reduce sample size. Covariate adjustment during training explicitly models known confounders but may inadvertently remove genuine biological signal. Residualization removes confounded variance in preprocessing but assumes linear relationships. Adversarial invariance learning trains representations that do not encode confounders but requires knowing which groups to enforce invariance over. Group DRO optimizes for worst-group performance at the cost of average performance. Multi-site training diversifies data sources. Temporal splits evaluate prospective performance. No single strategy eliminates all confounding; effective practice combines multiple approaches targeting different confounding sources."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 12.1 Confounding DAG | 1 | Essential | Medium (causal diagram) |
| 12.2 Population Shortcut | 4 | Essential | Medium-High (multi-panel) |
| 12.3 Batch Effects | 3 | High | Medium (multi-panel) |
| 12.4 Label Circularity | 1 | High | Medium (circular flow) |
| 12.5 Detection Diagnostics | 1 | High | High (multi-diagnostic) |
| 12.6 Mitigation Strategies | 1 | Enhancing | Medium (comparison table) |

**Total files:** 11
**Recommended generation order:** 12.1 (DAG, foundational), 12.2A-D (population shortcut), 12.4 (circularity), 12.3A-C (batch effects), 12.5 (detection), 12.6 (mitigation)

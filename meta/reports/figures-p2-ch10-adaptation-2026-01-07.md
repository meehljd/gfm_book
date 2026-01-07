# Figure Report: Chapter 10 - Adaptation Strategies

**Chapter:** Part 2, Chapter 10 - Adaptation Strategies
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (12 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 10.1: LoRA Architecture

**File:** `figs/part_2/ch10/01-fig-lora-architecture.svg`
**Priority:** Essential
**Type:** Architecture schematic

### Content Description

Schematic of LoRA (Low-Rank Adaptation) showing:
- Original frozen weight matrix W (large, grayed out to indicate frozen)
- Low-rank decomposition matrices A and B (smaller, colored to indicate trainable)
- Computation flow showing W + BA during forward pass
- Parameter count comparison: "500M frozen vs. 2-5M trainable"
- Mathematical notation: W' = W + BA

### DALL-E Prompt

```
Create a scientific diagram showing LoRA (Low-Rank Adaptation) architecture. Save as: 01-fig-lora-architecture.svg

Main elements:

FROZEN WEIGHTS (left):
- Large rectangular matrix labeled "W"
- Gray color (#7f7f7f) indicating frozen
- Dimension annotation: "d × d"
- Label: "Frozen (500M params)"

LOW-RANK MATRICES (right):
- Two smaller matrices labeled "A" and "B"
- Colored blue (#1f77b4) indicating trainable
- Matrix A: "d × r" dimensions
- Matrix B: "r × d" dimensions
- Label: "Trainable (2-5M params)"

COMPUTATION FLOW:
- Plus symbol between W and BA product
- Arrow showing: W' = W + BA
- Forward pass annotation

PARAMETER COMPARISON:
- Side bar comparing "Frozen: 500M" vs "Trainable: 2M"
- Visual ratio showing ~100:1 difference

Clean neural network architecture diagram style, white background, publication quality. Professional deep learning PEFT illustration.
```

### Post-Processing Notes

- Add mathematical formula: W' = W + BA
- Clearly distinguish frozen (gray) from trainable (blue) components
- Add rank parameter annotation: "r = 8-64 typical"
- Include memory/compute savings annotation

### Fallback Description

Create in diagramming software:
- Matrix visualization with dimension labels
- Color coding for frozen vs. trainable parameters
- Mathematical notation overlay

### Caption

**Recommended Caption:**
"Low-Rank Adaptation (LoRA) architecture. Rather than updating the full weight matrix W directly, LoRA introduces two smaller matrices A and B whose product approximates the desired weight change: W' = W + BA. During fine-tuning, W remains frozen (gray, 500 million parameters typical) while only A and B receive gradient updates (blue, 2-5 million parameters). The rank r (typically 8-64) controls adaptation expressiveness: lower ranks introduce fewer parameters and stronger implicit regularization; higher ranks enable more flexible task-specific modification at greater overfitting risk. This approach reduces memory requirements by an order of magnitude compared with full fine-tuning while achieving comparable performance on many downstream tasks."

---

## Figure 10.2: Layer Probing for Decoder Models (Two-Panel)

**Files:**
- `figs/part_2/ch10/02-A-fig-layer-probing-decoder.svg`
- `figs/part_2/ch10/02-B-fig-layer-probing-decoder.svg`

**Priority:** Essential
**Type:** Performance comparison plots

### Panel A: Encoder Model Layer Performance

**Content:** Line plot showing classification accuracy (y-axis) vs. layer number (x-axis) for an encoder model like DNABERT. Shows relatively flat performance across layers with slight improvement toward final layers. Demonstrates that final-layer embeddings work reliably.

**DALL-E Prompt:**
```
Create a scientific line plot showing encoder model layer-wise performance. Save as: 02-A-fig-layer-probing-decoder.svg

Plot elements:
- X-axis: "Layer Number" (1-12)
- Y-axis: "Classification Accuracy" (0.6-0.9)
- Single line showing relatively flat performance with slight upward trend
- Performance starts around 0.75, gradually increases to ~0.85 at final layer
- Final layer highlighted with marker and annotation: "Final layer reliable"
- Title: "Encoder Model (DNABERT-style)"
- Shaded confidence interval around line

Blue line color (#1f77b4). Clean scientific plot style with grid lines, white background. Professional machine learning evaluation figure.
```

**Caption for Panel A:**
"Encoder model layer-wise performance. For encoder architectures like DNABERT, classification accuracy remains relatively stable across layers with slight improvement toward the final layer. The bidirectional attention mechanism ensures that every position's representation incorporates information from the entire sequence at every layer, making final-layer embeddings a reliable default choice for downstream classification."

### Panel B: Decoder Model Layer Performance

**Content:** Line plot showing inverted-U pattern for decoder models. Performance peaks at middle layers (around layer 4-8 of 12), with notably degraded performance at the final layer. Demonstrates the "layer hunting problem."

**DALL-E Prompt:**
```
Create a scientific line plot showing decoder model layer-wise performance. Save as: 02-B-fig-layer-probing-decoder.svg

Plot elements:
- X-axis: "Layer Number" (1-12)
- Y-axis: "Classification Accuracy" (0.6-0.9)
- Line showing inverted-U pattern
- Performance starts ~0.70, peaks at layers 6-8 (~0.85), drops to ~0.65 at layer 12
- Final layer highlighted in RED with annotation: "Final layer degraded"
- Peak region annotated: "Optimal layers vary by task"
- Title: "Decoder Model (HyenaDNA-style)"
- Shaded confidence interval

Orange line color (#d62728) with red highlight on final layer. Clean scientific plot style with grid lines, white background. Professional layer hunting problem visualization.
```

**Caption for Panel B:**
"Decoder model layer-wise performance reveals the 'layer hunting problem.' Performance peaks at intermediate layers (6-8) and degrades substantially at the final layer. The next-token prediction objective specializes final layers for vocabulary distribution prediction, discarding information irrelevant to that task but potentially critical for downstream classification. Practitioners using decoder models must systematically evaluate all layers to identify optimal extraction points."

### Combined Caption

**Full Figure Caption:**
"Layer-wise probing reveals fundamental differences between encoder and decoder architectures. (A) Encoder models like DNABERT show relatively stable performance across layers, with the final layer providing reliable representations for classification. The bidirectional attention mechanism integrates information from the entire sequence at every layer. (B) Decoder models like HyenaDNA show an inverted-U pattern, with peak performance at intermediate layers and degraded performance at the final layer. The next-token prediction objective specializes final layers for a narrow purpose, creating what practitioners call the 'layer hunting problem': optimal embedding extraction requires systematic search across layers rather than defaulting to final-layer representations."

---

## Figure 10.3: Adaptation Strategy Decision Tree

**File:** `figs/part_2/ch10/03-fig-adaptation-decision-tree.svg`
**Priority:** Essential
**Type:** Decision flowchart

### Content Description

Flowchart guiding adaptation strategy selection with decision nodes:
1. "Labeled data quantity?" → branches for <500, 500-5000, >10000
2. "Task similarity to pretraining?" → high/moderate/low branches
3. "Computational constraints?" → limited/moderate/substantial branches

Terminal nodes recommend: Linear probing, LoRA/Adapters, Full fine-tuning, or From-scratch training, with expected tradeoffs at each terminal (accuracy, compute, overfitting risk).

### DALL-E Prompt

```
Create a scientific decision flowchart for transfer learning adaptation strategy selection. Save as: 03-fig-adaptation-decision-tree.svg

Decision tree structure:

ROOT NODE: "Choose Adaptation Strategy"

LEVEL 1 - Diamond decision: "Labeled examples?"
- Branch "<500": leads to "Linear Probing" (green terminal)
- Branch "500-5,000": leads to next decision
- Branch ">10,000": leads to next decision

LEVEL 2 - Diamond decisions for data-dependent paths
- "Task similarity to pretraining?"
- Branches: High → LoRA, Moderate → LoRA/Adapters, Low → Full fine-tuning check

LEVEL 3 - Compute constraints check
- "Compute available?" → Full fine-tuning or From-scratch

TERMINAL NODES (rounded rectangles):
- "Linear Probing": Low risk, low compute, minutes
- "LoRA/Adapters": Moderate risk, hours, 1 GPU
- "Full Fine-tuning": High risk, days, multi-GPU
- "From Scratch": Variable, weeks, when no suitable pretrained model

Color code: Green for low-risk/low-compute, yellow for moderate, red for high-risk/high-compute. Clean flowchart style with decision diamonds and process rectangles. White background. Professional ML decision guide.
```

### Post-Processing Notes

- Add tradeoff annotations at each terminal node
- Include computational cost estimates (minutes/hours/days)
- Add risk indicators (low/moderate/high overfitting risk)
- Color-code by recommendation strength

### Fallback Description

Create in flowchart software (Lucidchart, draw.io):
- Decision diamonds at branch points
- Terminal rectangles with recommendations
- Color coding by strategy risk level
- Annotations for compute and data requirements

### Caption

**Recommended Caption:**
"Decision framework for adaptation strategy selection. Data quantity dominates the decision: with fewer than 500 labeled examples, only linear probing avoids catastrophic overfitting; between 500 and 5,000 examples, parameter-efficient methods like LoRA offer favorable tradeoffs; above 10,000 examples, full fine-tuning becomes viable. Task similarity to pretraining and computational constraints further refine the choice. Terminal nodes indicate recommended strategies with expected tradeoffs: linear probing requires minimal compute but limits flexibility; LoRA balances adaptation capacity with regularization; full fine-tuning offers maximum flexibility at highest overfitting risk; from-scratch training remains appropriate when no suitable pretrained model exists."

---

## Figure 10.4: Domain Shift Detection (Three-Panel)

**Files:**
- `figs/part_2/ch10/04-A-fig-domain-shift-detection.svg`
- `figs/part_2/ch10/04-B-fig-domain-shift-detection.svg`
- `figs/part_2/ch10/04-C-fig-domain-shift-detection.svg`

**Priority:** High
**Type:** Diagnostic visualization suite

### Panel A: Embedding Space Visualization

**Content:** UMAP/t-SNE projection showing training distribution as dense cluster and test examples at varying distances. Out-of-distribution examples clearly separated from training manifold.

**DALL-E Prompt:**
```
Create a scientific UMAP embedding visualization showing domain shift detection. Save as: 04-A-fig-domain-shift-detection.svg

Plot elements:
- Dense cluster of training points (blue, #1f77b4) forming main distribution
- Test points colored by distance from training:
  - Green points: within training distribution (in-distribution)
  - Yellow points: edge of distribution (borderline)
  - Red points: clearly separated (out-of-distribution)
- Boundary line or shaded region showing training distribution extent
- Annotations: "Training distribution", "In-distribution test", "OOD examples"

Clean scientific scatter plot with legend. White background with subtle axes. Professional domain shift detection visualization.
```

**Caption for Panel A:**
"Embedding space visualization for domain shift detection. Training examples (blue) form a dense cluster defining the learned representation space. Test examples colored by distance from training distribution: in-distribution (green), borderline (yellow), and out-of-distribution (red). Examples far from the training manifold should receive appropriately high uncertainty in downstream predictions."

### Panel B: Calibration Comparison

**Content:** Calibration curves comparing confidence vs. accuracy for in-distribution (well-calibrated, near diagonal) vs. out-of-distribution examples (overconfident, curve below diagonal).

**DALL-E Prompt:**
```
Create a scientific calibration diagram comparing in-distribution vs OOD performance. Save as: 04-B-fig-domain-shift-detection.svg

Plot elements:
- X-axis: "Predicted Confidence" (0 to 1)
- Y-axis: "Observed Accuracy" (0 to 1)
- Diagonal reference line (perfect calibration, gray dashed)
- In-distribution curve (blue): closely following diagonal
- Out-of-distribution curve (red): significantly below diagonal, especially at high confidence
- Shaded areas showing calibration error
- Annotations: "Well-calibrated (in-distribution)", "Overconfident (OOD)"

Clean reliability diagram style with grid lines, white background. Professional calibration analysis figure.
```

**Caption for Panel B:**
"Calibration curves reveal overconfidence on out-of-distribution data. In-distribution test examples (blue) show well-calibrated predictions, with confidence matching accuracy along the diagonal. Out-of-distribution examples (red) show systematic overconfidence: the model predicts high confidence even when accuracy is low. This overconfidence on OOD data is particularly dangerous in clinical settings where confident wrong predictions may not be questioned."

### Panel C: Performance Degradation Curve

**Content:** Line plot showing accuracy declining as distributional distance from training data increases. Quantifies the relationship between distribution shift and performance loss.

**DALL-E Prompt:**
```
Create a scientific line plot showing performance degradation with domain shift. Save as: 04-C-fig-domain-shift-detection.svg

Plot elements:
- X-axis: "Distance from Training Distribution" (low to high)
- Y-axis: "Model Accuracy" (0.5 to 1.0)
- Declining curve starting high (~0.9) at low distance, dropping to chance (~0.55) at high distance
- Shaded confidence interval around curve
- Vertical dashed lines marking regions: "Safe", "Caution", "Unreliable"
- Threshold line at chance performance

Blue gradient line showing degradation. Clean scientific plot style with grid lines, white background. Professional domain shift analysis figure.
```

**Caption for Panel C:**
"Performance degradation as a function of distributional distance. Model accuracy declines monotonically as test examples move farther from the training distribution. The curve quantifies when predictions should be trusted: 'safe' regions near training distribution maintain high accuracy; 'caution' regions show degraded but above-chance performance; 'unreliable' regions approach chance accuracy and predictions should be abstained."

### Combined Caption

**Full Figure Caption:**
"Detecting domain shift before deployment prevents silent clinical failures. (A) UMAP visualization of embedding space shows test examples colored by distance from training distribution. Out-of-distribution examples (red) occupy regions where model predictions cannot be trusted. (B) Calibration analysis reveals that in-distribution predictions follow the diagonal (well-calibrated) while out-of-distribution predictions fall below (overconfident). This overconfidence makes OOD failures particularly dangerous. (C) Performance degradation quantifies the relationship between distributional distance and accuracy, enabling threshold-based decisions about when to trust predictions versus abstain."

---

## Figure 10.5: Validation Pitfalls (Four-Panel)

**Files:**
- `figs/part_2/ch10/05-A-fig-validation-pitfalls.svg`
- `figs/part_2/ch10/05-B-fig-validation-pitfalls.svg`
- `figs/part_2/ch10/05-C-fig-validation-pitfalls.svg`
- `figs/part_2/ch10/05-D-fig-validation-pitfalls.svg`

**Priority:** High
**Type:** Multi-panel warning illustration

### Panel A: Data Leakage Through Overlap

**Content:** Venn diagram showing pretraining data overlapping with test data, highlighting how this creates leakage and inflated performance.

**DALL-E Prompt:**
```
Create a scientific Venn diagram showing data leakage from pretraining overlap. Save as: 05-A-fig-validation-pitfalls.svg

Diagram elements:
- Left circle: "Pretraining Data" (blue, #1f77b4)
- Right circle: "Test/Benchmark Data" (orange, #d62728)
- Overlap region: "LEAKAGE" (highlighted red with warning pattern)
- Arrow from overlap to annotation: "Inflated Performance"
- Example text: "UniRef sequences in ProteinGym benchmarks"

Clean Venn diagram style with bold overlap highlighting, white background. Professional data leakage warning figure.
```

**Caption for Panel A:**
"Pretraining data overlap creates leakage. When sequences from pretraining corpora (blue) overlap with benchmark test sets (orange), the model has effectively 'seen' the test data, inflating apparent performance. This is particularly problematic for large foundation models trained on massive genomic databases that may inadvertently include benchmark sequences."

### Panel B: Temporal Leakage

**Content:** Timeline showing training on variants annotated after test set creation, illustrating how temporal ordering violations create leakage.

**DALL-E Prompt:**
```
Create a scientific timeline diagram showing temporal leakage in variant annotation. Save as: 05-B-fig-validation-pitfalls.svg

Timeline elements:
- Horizontal timeline with dates (2018-2024)
- "Test Set Created" marker at 2020
- "Training Data" bar extending from 2018 to 2023 (includes future!)
- "Leakage Zone" highlighted red: 2020-2023 (post-test creation)
- Arrow showing "Future information in training"
- Correct approach shown below: training stops before test set creation

Clean timeline diagram with warning highlights, white background. Professional temporal leakage illustration.
```

**Caption for Panel B:**
"Temporal leakage uses future information unavailable at prediction time. When training includes variants annotated after benchmark creation (red zone), the model may have learned from the same evidence that later informed test labels. Proper temporal splits train only on data available before the prediction cutoff, simulating realistic prospective deployment."

### Panel C: Baseline Comparison Issues

**Content:** Bar chart comparing foundation model against weak baseline (large gap, misleading) vs. properly-tuned baseline (small gap, realistic).

**DALL-E Prompt:**
```
Create a scientific bar chart showing misleading vs fair baseline comparisons. Save as: 05-C-fig-validation-pitfalls.svg

Chart elements:
Two grouped comparisons side by side:

LEFT GROUP "Misleading Comparison":
- Short bar: "Weak Baseline" (~60%)
- Tall bar: "Foundation Model" (~90%)
- Large gap highlighted with "30% improvement!"
- Red warning annotation

RIGHT GROUP "Fair Comparison":
- Medium bar: "Tuned Baseline" (~85%)
- Tall bar: "Foundation Model" (~90%)
- Small gap highlighted with "5% improvement"
- Green checkmark annotation

X-axis: Comparison type. Y-axis: Accuracy (0-100%). Clean bar chart style with annotations, white background. Professional baseline comparison figure.
```

**Caption for Panel C:**
"Baseline selection dramatically affects perceived transfer value. Comparing against weak or poorly-tuned baselines (left) inflates apparent foundation model improvements. Fair evaluation requires properly-tuned baselines with equivalent hyperparameter search and appropriate architectures (right). The true benefit of transfer is the gap above a strong baseline, not the gap above a strawman."

### Panel D: Stratified Performance Hidden

**Content:** Two bar charts: one showing aggregate accuracy (90%), another showing stratified view revealing aggregate hides rare-variant failure (common: 95%, rare: 50%).

**DALL-E Prompt:**
```
Create a scientific figure showing hidden stratified performance failures. Save as: 05-D-fig-validation-pitfalls.svg

Two side-by-side bar charts:

LEFT CHART "Aggregate (Misleading)":
- Single tall bar: "Overall Accuracy" at 90%
- Green color suggesting good performance
- Checkmark icon

RIGHT CHART "Stratified (Revealing)":
- Two bars:
  - "Common variants" at 95% (green)
  - "Rare variants" at 50% (red, warning)
- Arrow pointing to rare variants: "Clinically important!"
- Annotation: "Aggregate conceals failure on rare variants"

Clean bar chart style with warning highlights, white background. Professional stratified evaluation figure.
```

**Caption for Panel D:**
"Aggregate metrics conceal stratified failures. Overall accuracy of 90% (left) appears acceptable, but stratified analysis (right) reveals systematic failure on rare variants (50% accuracy) masked by good performance on common variants (95%). Since rare variants are often the clinically important ones, aggregate reporting can hide the failures that matter most for patient care."

### Combined Caption

**Full Figure Caption:**
"Common validation pitfalls that inflate transfer learning claims. (A) Overlap between pretraining data and benchmarks creates leakage, allowing models to 'remember' test examples. (B) Temporal leakage occurs when training includes information from after benchmark creation. (C) Weak baseline comparisons exaggerate transfer benefits; fair evaluation requires properly-tuned from-scratch baselines. (D) Aggregate metrics conceal stratified failures; rare variants may show near-random performance while being masked by high accuracy on common variants. Together, these pitfalls can make ineffective transfer appear successful until clinical deployment reveals the failures."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 10.1 LoRA Architecture | 1 | Essential | Medium (schematic) |
| 10.2 Layer Probing | 2 | Essential | Medium (comparison plots) |
| 10.3 Decision Tree | 1 | Essential | Medium (flowchart) |
| 10.4 Domain Shift Detection | 3 | High | Medium (diagnostic suite) |
| 10.5 Validation Pitfalls | 4 | High | Medium (warning illustrations) |

**Total files:** 11
**Recommended generation order:** 10.1 (LoRA, foundational), 10.3 (decision tree), 10.2A-B (layer probing), 10.4A-C (domain shift), 10.5A-D (pitfalls)

# Figure Report: Chapter 23 - Uncertainty Quantification

**Chapter:** p5-ch23-uncertainty.qmd
**Date:** 2026-01-07
**Total Figures:** 7 (15 files)
**Format:** SVG (for scalability)

---

## Figure 1: Uncertainty Types (Aleatoric vs Epistemic)

### Files
- `figs/part_5/ch23/01-A-fig-uncertainty-types.svg`
- `figs/part_5/ch23/01-B-fig-uncertainty-types.svg`

### Priority
**Essential** - Core conceptual framework

### Content Description
Two-panel comparison of aleatoric (irreducible) versus epistemic (reducible) uncertainty, with genomic examples.

### DALL-E Prompt
```
Scientific illustration comparing two types of uncertainty for computational biology textbook. Two panels.

PANEL A (Aleatoric - Irreducible): Visualization showing inherent stochastic variability. Example: Gene expression from identical cells showing distribution of values around mean. Dice icon symbolizing randomness. Multiple cells (same genotype) producing variable expression. Annotation "Cannot be reduced with more data - reflects true biological noise." Graph showing distribution width that doesn't narrow with sample size.

PANEL B (Epistemic - Reducible): Visualization showing knowledge-based uncertainty. Example: Variant effect prediction in data-sparse region. Question mark icon symbolizing lack of knowledge. Few training examples nearby, wide confidence interval. Annotation "Can be reduced with more data or better models." Graph showing confidence interval narrowing as sample size increases.

Genomic examples beneath each: Aleatoric - stochastic gene expression, measurement noise. Epistemic - rare variant effects, novel protein families, underrepresented populations.

Clean scientific illustration, white background, educational diagram style, blue for aleatoric, orange for epistemic.

Save as: 01-A-fig-uncertainty-types.svg (aleatoric), 01-B-fig-uncertainty-types.svg (epistemic)
```

### Post-Processing Notes
- Add mathematical notation for variance decomposition
- Include specific genomic examples
- Show how each relates to model confidence

### Fallback Description
"Comparison of aleatoric (irreducible, inherent biological/measurement noise) and epistemic (reducible, knowledge-based) uncertainty, showing how aleatoric uncertainty persists with more data while epistemic uncertainty can be reduced through additional training examples."

### Caption Recommendation
"Two types of uncertainty. (A) Aleatoric uncertainty: irreducible stochasticity from biological variability or measurement noise—cannot be eliminated with more data. (B) Epistemic uncertainty: reducible uncertainty from limited knowledge—decreases as training data grow. Distinguishing these is critical: high epistemic uncertainty should trigger caution, while aleatoric uncertainty sets fundamental prediction limits."

---

## Figure 2: Calibration Diagrams

### Files
- `figs/part_5/ch23/02-A-fig-calibration-diagrams.svg`
- `figs/part_5/ch23/02-B-fig-calibration-diagrams.svg`
- `figs/part_5/ch23/02-C-fig-calibration-diagrams.svg`
- `figs/part_5/ch23/02-D-fig-calibration-diagrams.svg`

### Priority
**Essential** - Core visualization for calibration assessment

### Content Description
Four-panel figure showing reliability diagrams: perfect calibration, overconfident predictions, underconfident predictions, and calibration error metrics.

### DALL-E Prompt
```
Scientific illustration of model calibration diagrams for machine learning textbook. Four panels.

PANEL A (Perfect Calibration): Reliability diagram with predicted probability (x-axis, 0-1) vs observed frequency (y-axis, 0-1). Perfect diagonal line. Bar histogram at bottom showing prediction distribution. Annotation "Predictions match reality."

PANEL B (Overconfident): Same axes but curve bowed below diagonal. When model says 90%, reality is only 70%. Shaded area showing calibration gap. Annotation "Model too confident - common in deep learning." Clinical warning: "Overconfidence → missed diagnoses."

PANEL C (Underconfident): Curve bowed above diagonal. When model says 60%, reality is 75%. Shaded gap area. Annotation "Model too uncertain - loses utility." Note: "Less common but wastes follow-up resources."

PANEL D (Calibration Metrics): Equations and visual explanation. ECE (Expected Calibration Error): weighted average of |accuracy - confidence| in bins. Shown as sum of shaded areas. MCE (Maximum Calibration Error): worst bin. Brier score decomposition. Visual showing bin-by-bin calculation.

Professional scientific illustration, statistical visualization style, white background, consistent color scheme.

Save as: 02-A-fig-calibration-diagrams.svg through 02-D-fig-calibration-diagrams.svg
```

### Post-Processing Notes
- Add mathematical formulas for ECE, MCE
- Include confidence intervals on bins
- Show number of samples per bin

### Fallback Description
"Calibration assessment diagrams: perfectly calibrated predictions fall on the diagonal, overconfident predictions curve below (model claims certainty it doesn't deserve), underconfident predictions curve above. ECE and MCE metrics quantify calibration error."

### Caption Recommendation
"Model calibration assessment. (A) Perfect calibration: predicted probabilities match observed frequencies on the diagonal. (B) Overconfident model: predictions systematically exceed reality—dangerous for clinical use. (C) Underconfident model: predictions underestimate true probabilities—reduces utility. (D) Calibration metrics: Expected Calibration Error (ECE) averages across bins; Maximum Calibration Error (MCE) captures worst-case performance."

---

## Figure 3: Calibration Methods

### Files
- `figs/part_5/ch23/03-A-fig-calibration-methods.svg`
- `figs/part_5/ch23/03-B-fig-calibration-methods.svg`
- `figs/part_5/ch23/03-C-fig-calibration-methods.svg`

### Priority
**High** - Practical implementation guidance

### Content Description
Three-panel comparison of calibration strategies: temperature scaling, Platt scaling, and isotonic regression.

### DALL-E Prompt
```
Scientific illustration of model calibration methods for machine learning. Three panels.

PANEL A (Temperature Scaling): Flow diagram. Input: uncalibrated logits. Operation: divide by learned temperature T. Output: softmax with calibrated probabilities. Before/after reliability diagrams showing improvement. Annotation "Single parameter; preserves ranking; widely used." Mathematical: softmax(z/T).

PANEL B (Platt Scaling): Flow diagram. Input: model scores. Operation: logistic regression with learned parameters a, b. Sigmoid transformation. Before/after showing calibration improvement. Annotation "Two parameters; handles asymmetric miscalibration." Mathematical: σ(a·z + b).

PANEL C (Isotonic Regression): Flow diagram. Input: sorted predictions. Operation: piecewise constant monotonic fit. Histogram of predictions with step function overlay. Before/after diagrams. Annotation "Non-parametric; flexible but needs more data; risk of overfitting." Visual showing monotonic constraint.

Comparison table below: Method, Parameters, Flexibility, Data requirement, Best for.

Professional scientific style, flowchart elements, white background, consistent visual language.

Save as: 03-A-fig-calibration-methods.svg through 03-C-fig-calibration-methods.svg
```

### Post-Processing Notes
- Add code snippets showing implementation
- Include validation set requirements
- Show cross-validation considerations

### Fallback Description
"Calibration methods comparison: temperature scaling (single parameter, divides logits), Platt scaling (logistic regression on scores), and isotonic regression (non-parametric monotonic fit). Each trades off flexibility against data requirements."

### Caption Recommendation
"Post-hoc calibration methods. (A) Temperature scaling: divides logits by learned temperature T before softmax—simple, preserves ranking, widely effective. (B) Platt scaling: fits logistic regression on model scores—handles asymmetric miscalibration with two parameters. (C) Isotonic regression: non-parametric monotonic fit—most flexible but requires more calibration data and risks overfitting."

---

## Figure 4: UQ Methods Overview

### Files
- `figs/part_5/ch23/04-fig-uq-methods.svg`

### Priority
**High** - Survey of approaches

### Content Description
Comprehensive overview of uncertainty quantification methods: ensembles, dropout, Bayesian methods, evidential deep learning.

### DALL-E Prompt
```
Scientific illustration overview of uncertainty quantification methods for deep learning. Single comprehensive panel.

QUADRANT LAYOUT:

TOP LEFT (Ensembles): Multiple neural network diagrams (5 networks). Each produces prediction. Aggregation showing mean and variance of predictions. Annotation "Multiple models → prediction spread measures uncertainty." Pros: Works well. Cons: 5-10x compute.

TOP RIGHT (MC Dropout): Single network with dropout layers highlighted. Multiple forward passes with different dropout masks. Prediction distribution from passes. Annotation "Single model, multiple stochastic passes." Pros: Easy to implement. Cons: Approximate.

BOTTOM LEFT (Bayesian NNs): Network with probability distributions on weights (not point values). Posterior inference visualization. Annotation "Distribution over weights → principled uncertainty." Pros: Principled. Cons: Computationally intensive; approximations needed.

BOTTOM RIGHT (Evidential DL): Network producing distribution parameters directly (e.g., mean + variance, or Dirichlet parameters). Single forward pass. Annotation "Learn to predict uncertainty directly." Pros: Fast inference. Cons: Requires careful training.

CENTER: Comparison compass showing tradeoffs between compute cost, theoretical grounding, implementation complexity, and calibration quality.

Professional scientific illustration, neural network diagram style, white background.

Save as: 04-fig-uq-methods.svg
```

### Post-Processing Notes
- Add mathematical notation for each method
- Include citation references
- Show computational cost estimates

### Fallback Description
"Uncertainty quantification methods overview: ensembles (multiple models, high compute), MC dropout (stochastic passes, approximate), Bayesian NNs (principled but expensive), and evidential deep learning (single-pass, learns uncertainty). Each trades off compute, theory, and calibration."

### Caption Recommendation
"Uncertainty quantification methods for deep learning. Ensembles train multiple models and use prediction variance; MC Dropout uses stochastic forward passes through a single model; Bayesian neural networks maintain distributions over weights; evidential deep learning predicts distribution parameters directly. Each involves tradeoffs between computational cost, theoretical grounding, and calibration quality."

---

## Figure 5: Conformal Prediction

### Files
- `figs/part_5/ch23/05-fig-conformal-prediction.svg`

### Priority
**High** - Distribution-free uncertainty

### Content Description
Conformal prediction framework showing how to construct prediction sets with guaranteed coverage.

### DALL-E Prompt
```
Scientific illustration of conformal prediction for uncertainty quantification. Single comprehensive panel with multiple elements.

TOP SECTION (The Guarantee): Mathematical statement: "P(Y ∈ C(X)) ≥ 1 - α" in large text. Annotation "Coverage guarantee holds regardless of model architecture or data distribution."

MIDDLE SECTION (Procedure):
Step 1: Split data into training and calibration sets. Visual of dataset splitting.
Step 2: Train model on training set. Neural network icon.
Step 3: Compute conformity scores on calibration set. Formula: s_i = some non-conformity measure. Histogram of calibration scores.
Step 4: Find threshold q at (1-α) quantile of scores. Vertical line on histogram.
Step 5: For new input, include labels where score ≤ q. Prediction set visualization.

BOTTOM SECTION (Genomic Example):
Variant classification example. Instead of "Pathogenic" → prediction set {"Pathogenic", "VUS"} with 90% coverage guarantee. For well-characterized variant: small set. For rare variant: larger set (honest about uncertainty).

Annotation: "Key insight: Set size reflects confidence—rare variants get larger sets."

Professional scientific style, flowchart elements, probability visualization, white background.

Save as: 05-fig-conformal-prediction.svg
```

### Post-Processing Notes
- Add specific genomic examples
- Show coverage verification
- Include adaptive conformal prediction variant

### Fallback Description
"Conformal prediction procedure: split data, compute conformity scores on calibration set, find threshold at desired coverage level, construct prediction sets for new inputs. Provides distribution-free coverage guarantees—rare variants get larger prediction sets reflecting honest uncertainty."

### Caption Recommendation
"Conformal prediction for coverage-guaranteed uncertainty. The procedure uses a calibration set to establish a score threshold such that prediction sets cover the true label with probability at least 1−α. Unlike point predictions, conformal sets communicate uncertainty through their size: well-characterized variants receive small sets, while rare variants receive larger sets that honestly reflect limited knowledge."

---

## Figure 6: Out-of-Distribution Detection

### Files
- `figs/part_5/ch23/06-A-fig-ood-detection.svg`
- `figs/part_5/ch23/06-B-fig-ood-detection.svg`
- `figs/part_5/ch23/06-C-fig-ood-detection.svg`

### Priority
**High** - Critical for safe deployment

### Content Description
Three-panel figure on OOD detection: the problem, detection methods, and genomic OOD scenarios.

### DALL-E Prompt
```
Scientific illustration of out-of-distribution detection for genomic AI. Three panels.

PANEL A (The OOD Problem): Two distributions. Training distribution (blue, compact cluster). OOD region (red, outside cluster). Model making confident but unreliable predictions in OOD region. Annotation "Models extrapolate confidently where they shouldn't." Clinical example: African-ancestry patient when model trained on European data.

PANEL B (Detection Methods): Four approaches with icons:
1) Softmax confidence (simple but unreliable)
2) Energy-based (better calibrated)
3) Mahalanobis distance (embedding space)
4) Ensemble disagreement (multiple models)
For each: small visualization of how it works. Comparison of detection ROC curves.

PANEL C (Genomic OOD Scenarios): Grid showing scenarios:
- Novel gene families (distant from training)
- Underrepresented ancestries (population shift)
- Extreme variants (insertions, deletions, CNVs)
- Different cell types (tissue mismatch)
- Technical batch effects (sequencing platform)
For each: icon and brief description. Annotation "Must detect before clinical use."

Professional scientific illustration, distribution visualization style, white background.

Save as: 06-A-fig-ood-detection.svg through 06-C-fig-ood-detection.svg
```

### Post-Processing Notes
- Add specific detection threshold examples
- Include AUROC values for methods
- Show false positive/negative tradeoffs

### Fallback Description
"Out-of-distribution detection: models make confident but unreliable predictions outside training distribution. Detection methods include softmax confidence, energy scores, embedding distance, and ensemble disagreement. Genomic OOD scenarios include novel gene families, underrepresented ancestries, and different sequencing platforms."

### Caption Recommendation
"Out-of-distribution detection for safe deployment. (A) The OOD problem: models extrapolate confidently into regions where predictions are unreliable. (B) Detection methods: from simple softmax thresholds to sophisticated embedding-space approaches. (C) Genomic OOD scenarios: novel genes, underrepresented populations, unusual variant types, mismatched tissues, and technical batch effects—all require detection before clinical use."

---

## Figure 7: Selective Prediction

### Files
- `figs/part_5/ch23/07-fig-selective-prediction.svg`

### Priority
**Enhancing** - Practical deployment strategy

### Content Description
Selective prediction framework: abstaining on uncertain predictions to maintain accuracy on accepted predictions.

### DALL-E Prompt
```
Scientific illustration of selective prediction framework for clinical AI. Single panel with multiple elements.

TOP SECTION (The Concept): Flow diagram. Input query → Model → Confidence assessment → Decision gate: "Confident?" → If Yes: "Predict" (arrow to prediction). If No: "Abstain" (arrow to "Human review").

MIDDLE SECTION (Coverage-Accuracy Tradeoff): Plot with two curves. X-axis: Coverage (fraction of predictions made). Y-axis: Accuracy. One curve showing accuracy increasing as coverage decreases (being more selective). Operational point marked showing clinical threshold choice. Annotation "Tradeoff: higher accuracy requires rejecting more cases."

BOTTOM SECTION (Clinical Workflow): Three scenarios:
1) High confidence variant → Automated classification → Report
2) Moderate confidence → Flag for review → Expert decides
3) Low confidence → Abstain → Manual curation required
Icons for each pathway. Annotation "Selective prediction enables tiered clinical workflows."

INSET: Risk-coverage curve from real genomic model showing practical performance.

Professional scientific style, workflow diagram elements, white background.

Save as: 07-fig-selective-prediction.svg
```

### Post-Processing Notes
- Add specific accuracy/coverage numbers
- Include clinical workflow integration
- Show how thresholds are set

### Fallback Description
"Selective prediction: model abstains on uncertain predictions, routing them to human review. This enables high accuracy on accepted predictions at the cost of coverage. Clinical workflows can use confidence tiers to balance automation with human oversight."

### Caption Recommendation
"Selective prediction for clinical deployment. Rather than forcing predictions on all cases, models abstain when uncertainty exceeds a threshold, routing uncertain cases to human review. The coverage-accuracy tradeoff determines what fraction of cases are automated: higher accuracy requires accepting fewer cases. This enables tiered clinical workflows where confident predictions proceed automatically while uncertain cases receive expert attention."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Uncertainty Types | 2 | Essential | Low |
| Calibration Diagrams | 4 | Essential | Medium |
| Calibration Methods | 3 | High | Medium |
| UQ Methods Overview | 1 | High | High |
| Conformal Prediction | 1 | High | Medium |
| OOD Detection | 3 | High | Medium |
| Selective Prediction | 1 | Enhancing | Low |

## Recommended Generation Order
1. Uncertainty Types (conceptual foundation)
2. Calibration Diagrams (core visualization)
3. Calibration Methods (practical implementation)
4. UQ Methods Overview (survey)
5. OOD Detection (safety-critical)
6. Conformal Prediction (advanced method)
7. Selective Prediction (deployment strategy)

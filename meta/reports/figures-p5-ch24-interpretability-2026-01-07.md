# Figure Report: Chapter 24 - Interpretability

**Chapter:** p5-ch24-interpretability.qmd
**Date:** 2026-01-07
**Total Figures:** 7 (13 files)
**Format:** SVG (for scalability)

---

## Figure 1: Attribution Methods Comparison

### Files
- `figs/part_5/ch24/01-fig-attribution-comparison.svg`

### Priority
**Essential** - Overview of attribution landscape

### Content Description
Comparison of attribution methods on the same input sequence showing agreement and disagreement between methods.

### DALL-E Prompt
```
Scientific illustration comparing attribution methods for genomic sequence interpretation. Single comprehensive panel.

TOP: DNA sequence displayed as horizontal bar with nucleotide letters (A, T, G, C colored).

FIVE ATTRIBUTION TRACKS BELOW (stacked):
1) Gradient × Input: Noisy track with scattered importance. Label "Fast, noisy."
2) Integrated Gradients: Smoother track with cleaner peaks. Label "Principled, slower."
3) DeepLIFT: Similar to IG but with different peak heights. Label "Reference-based."
4) Attention weights: Discrete peaks at specific positions. Label "What model attends (≠ importance)."
5) In silico mutagenesis (ISM): Clean gold-standard track. Label "Ground truth but expensive (3L passes)."

ANNOTATIONS:
- Circle regions where all methods agree → "High confidence important region"
- Circle regions where methods disagree → "Investigate further"
- Known motif (e.g., GATA box) highlighted with box

SIDE PANEL: Comparison table
| Method | Compute | Faithfulness | Best Use |
| Gradient×Input | 1 pass | Low-Med | Quick screen |
| Integrated Gradients | 10-50 passes | Med-High | Standard |
| DeepLIFT | 1 pass | Medium | Reference comparison |
| Attention | Free | Low | Exploration only |
| ISM | 3L passes | High | Validation |

Professional scientific illustration, genomic track visualization style, white background.

Save as: 01-fig-attribution-comparison.svg
```

### Post-Processing Notes
- Use real genomic sequence example
- Add correlation values between methods
- Highlight specific motifs

### Fallback Description
"Comparison of attribution methods on the same genomic sequence: Gradient × Input (fast, noisy), Integrated Gradients (principled), DeepLIFT (reference-based), attention weights (what model attends), and ISM (gold standard). Agreement across methods increases confidence; disagreement flags positions for investigation."

### Caption Recommendation
"Attribution methods comparison on a single genomic sequence. From top: Gradient × Input (fast but noisy), Integrated Gradients (principled with theoretical guarantees), DeepLIFT (reference-based attributions), attention weights (model attention ≠ importance), and in silico mutagenesis (ground truth but 3L forward passes). Regions where methods agree provide high-confidence importance; disagreement flags positions for closer investigation."

---

## Figure 2: In Silico Mutagenesis

### Files
- `figs/part_5/ch24/02-A-fig-in-silico-mutagenesis.svg`
- `figs/part_5/ch24/02-B-fig-in-silico-mutagenesis.svg`
- `figs/part_5/ch24/02-C-fig-in-silico-mutagenesis.svg`
- `figs/part_5/ch24/02-D-fig-in-silico-mutagenesis.svg`

### Priority
**High** - Gold standard method

### Content Description
Four-panel figure covering ISM procedure, output visualization, validation against experiments, and mechanistic insights.

### DALL-E Prompt
```
Scientific illustration of in silico mutagenesis for genomic model interpretation. Four panels.

PANEL A (ISM Procedure): Flow diagram. Reference sequence at top. At each position, systematically substitute all alternative nucleotides (A→T, A→G, A→C). Each mutant sequence through model. Compute prediction difference. Result: Position × Mutation matrix. Annotation "True counterfactual - direct model behavior."

PANEL B (ISM Profile Visualization): Heatmap aligned to sequence. Rows: positions. Columns: alternative nucleotides (or shown as 4×L matrix). Color scale: effect magnitude (blue negative, red positive). Functional regions show large effects (bright colors). Silent regions near zero (gray). Known binding site highlighted.

PANEL C (Validation Against DMS): Scatter plot comparing ISM predictions (x-axis) vs experimental deep mutational scanning measurements (y-axis). Correlation coefficient shown (r ~ 0.6-0.8). Points colored by position type (active site, surface, etc.). Annotation "ISM validated against experimental perturbations."

PANEL D (Mechanistic Insights Revealed): Three examples with icons:
1) Binding site boundaries: Sharp ISM signal edges define motif extent
2) Position-specific tolerance: Some positions tolerate mutations, others don't
3) Allele-specific effects: Different substitutions have different effects
Annotation "ISM reveals regulatory grammar."

Professional scientific style, heatmap visualization, white background.

Save as: 02-A-fig-in-silico-mutagenesis.svg through 02-D-fig-in-silico-mutagenesis.svg
```

### Post-Processing Notes
- Use realistic color scales
- Include specific position examples
- Add statistical annotations

### Fallback Description
"In silico mutagenesis workflow: systematically substitute each position to all alternatives, compute prediction changes, visualize as position × mutation matrix. Validation against deep mutational scanning shows ISM captures true functional effects. Mechanistic insights include binding site boundaries and position-specific tolerance."

### Caption Recommendation
"In silico mutagenesis (ISM). (A) Procedure: substitute each position to all alternatives, compute prediction difference. (B) Visualization: position × mutation heatmap with functional regions showing large effects. (C) Validation: ISM predictions correlate with experimental deep mutational scanning (r ≈ 0.6-0.8). (D) Mechanistic insights: ISM reveals binding site boundaries, position-specific tolerance, and allele-specific effects."

---

## Figure 3: TF-MoDISco Motif Discovery

### Files
- `figs/part_5/ch24/03-fig-tfmodisco.svg`

### Priority
**High** - Bridge from attributions to biology

### Content Description
TF-MoDISco pipeline from attribution scores to discovered motifs matched to known databases.

### DALL-E Prompt
```
Scientific illustration of TF-MoDISco motif discovery pipeline. Single comprehensive panel.

PIPELINE FLOW (left to right):

STAGE 1 (Attributions): Multiple sequence tracks with importance scores (from DeepLIFT, IG, or ISM). Annotation "Input: attribution scores for many sequences."

STAGE 2 (Seqlet Extraction): Highlighted windows where total importance exceeds threshold. Seqlets extracted as short sequences + importance profiles. Annotation "Extract high-importance windows."

STAGE 3 (Clustering): Seqlets grouped by sequence + importance similarity. Multiple clusters shown (different colors). Annotation "Cluster similar seqlets."

STAGE 4 (Motif Consolidation): Each cluster produces position weight matrix (shown as sequence logo) and importance-weighted logo. Clean motif visualizations.

STAGE 5 (Database Matching): Discovered motifs compared to JASPAR/HOCOMOCO. Match examples:
- Cluster 1 → CTCF (high match, known biology)
- Cluster 2 → GATA4 (high match)
- Cluster 3 → ??? (no match - novel pattern)

OUTPUT BOX: Motif vocabulary with sequence logos, match annotations, genomic usage statistics.

Annotation: "Key insight: Discovers what the MODEL learned, not just what's in the sequence."

Professional scientific style, sequence logo visualization, flowchart elements, white background.

Save as: 03-fig-tfmodisco.svg
```

### Post-Processing Notes
- Include real sequence logos
- Add match statistics
- Show composite motif examples

### Fallback Description
"TF-MoDISco pipeline: extract high-importance windows (seqlets) from attribution scores, cluster by sequence and importance similarity, consolidate into motifs, match to known databases. Discovers what the model actually learned—including novel patterns not in databases."

### Caption Recommendation
"TF-MoDISco motif discovery from attribution scores. Starting from attribution maps for many sequences, the method extracts high-importance windows (seqlets), clusters similar seqlets, consolidates into position weight matrices, and matches to known motif databases. Discovered motifs represent what the model learned—known transcription factors validate biological relevance while novel patterns may indicate previously unknown regulatory features."

---

## Figure 4: Attention Pattern Visualization

### Files
- `figs/part_5/ch24/04-A-fig-attention-visualization.svg`
- `figs/part_5/ch24/04-B-fig-attention-visualization.svg`
- `figs/part_5/ch24/04-C-fig-attention-visualization.svg`

### Priority
**High** - With critical caveats

### Content Description
Three-panel figure showing attention heatmaps, biological overlay, and multi-head specialization—with caveats about interpretation.

### DALL-E Prompt
```
Scientific illustration of attention pattern visualization in genomic transformers. Three panels.

PANEL A (Attention Heatmap): Position × position matrix from transformer attention. Color intensity shows attention weight. Patterns visible: diagonal (local), off-diagonal blocks (long-range), focal spots (specific interactions). Annotation "What the model 'looks at' - but attention ≠ importance."

PANEL B (Biological Overlay): Same attention pattern overlaid on genome browser-style track. Attention peaks aligned with known regulatory elements (promoter, enhancer, CTCF sites). Hi-C contact map comparison (triangular) showing similar patterns. Annotation "Sometimes aligns with biology..." Warning box: "But correlation ≠ causation. Validation required."

PANEL C (Multi-Head Specialization): Three attention heads side by side showing different patterns:
- Head 1: Local context (diagonal dominant) - "Captures nearby nucleotides"
- Head 2: Long-range (sparse off-diagonal) - "Distal interactions"
- Head 3: Motif-specific (focal spots) - "Specific sequence patterns"
Annotation "Different heads learn different computational roles."

CAVEAT BOX at bottom: "⚠️ Attention weights describe information routing, NOT causal contribution. High attention ≠ high importance. Always validate with perturbation experiments."

Professional scientific style, heatmap visualization, white background.

Save as: 04-A-fig-attention-visualization.svg through 04-C-fig-attention-visualization.svg
```

### Post-Processing Notes
- Use realistic attention patterns
- Add warning callouts
- Include validation examples

### Fallback Description
"Attention visualization in genomic transformers: attention heatmaps show position-position relationships, sometimes aligning with known regulatory elements. Different attention heads specialize for different patterns. Critical caveat: attention describes information routing, not causal importance—validation required."

### Caption Recommendation
"Attention patterns in genomic transformers. (A) Attention heatmap showing position-position weights with local and long-range patterns. (B) Biological overlay: attention sometimes aligns with regulatory elements—but correlation does not prove the model learned these relationships causally. (C) Multi-head specialization: different heads capture local context, long-range interactions, or specific motifs. **Caution**: attention weights describe information routing, not importance—always validate with perturbation experiments."

---

## Figure 5: Plausible vs Faithful Explanations

### Files
- `figs/part_5/ch24/05-fig-plausible-vs-faithful.svg`

### Priority
**Essential** - Core chapter concept

### Content Description
Two-path diagram contrasting plausible but unfaithful explanations with faithful explanations, using validation tests.

### DALL-E Prompt
```
Scientific illustration distinguishing plausible from faithful model explanations. Single panel with two paths.

CENTER: Model predicts "High enhancer activity" for genomic sequence.

PATH A (LEFT - PLAUSIBLE BUT UNFAITHFUL):
- Attribution highlights GATA motif (biologically reasonable)
- Annotation "Matches human intuition"
- BUT: Model actually learned GC content correlation (hidden)
- Validation tests FAIL:
  - Mutating GATA → no prediction change ✗
  - Inserting GATA → no prediction increase ✗
  - Random weights → similar attributions ✗
- Result: "False comfort - explanation matches intuition, not computation"
- Red warning color scheme

PATH B (RIGHT - FAITHFUL):
- Attribution highlights same GATA motif
- Model computation traces through GATA recognition
- Validation tests PASS:
  - Mutating GATA → prediction drops ✓
  - Inserting GATA → prediction increases ✓
  - Random weights → different attributions ✓
- Result: "Genuine insight - explanation reflects actual model behavior"
- Green success color scheme

BOTTOM: Validation hierarchy table:
1. Sanity check (random weights produce random attributions)
2. Necessity (ablating feature reduces prediction)
3. Sufficiency (inserting feature increases prediction)

KEY INSIGHT BOX: "Plausible = matches intuition. Faithful = reflects computation. They can diverge!"

Professional scientific style, two-path comparison, white background.

Save as: 05-fig-plausible-vs-faithful.svg
```

### Post-Processing Notes
- Make distinction visually clear
- Add specific test examples
- Include decision flowchart

### Fallback Description
"Plausible vs faithful explanations: a plausible explanation matches biological intuition (GATA motif highlighted) but may not reflect actual model computation (which learned GC content). Faithful explanations pass validation tests: ablating the feature changes prediction, inserting increases it. The distinction is critical for scientific discovery."

### Caption Recommendation
"Plausible versus faithful explanations. Both paths start with attributions highlighting a GATA motif. Left: plausible but unfaithful—the explanation matches intuition, but the model learned GC content; validation tests fail. Right: faithful—the model actually uses the GATA motif; validation tests pass. The distinction determines whether interpretability generates genuine insight or false comfort. Always validate: does ablating the feature change prediction? Does inserting it increase prediction?"

---

## Figure 6: Validation Pipeline

### Files
- `figs/part_5/ch24/06-fig-validation-pipeline.svg`

### Priority
**High** - Practical workflow

### Content Description
Circular workflow showing model → interpretability → hypothesis → validation → model refinement cycle.

### DALL-E Prompt
```
Scientific illustration of interpretability validation pipeline as circular workflow. Single panel.

CIRCULAR FLOW (clockwise):

STEP 1 (TOP): "Model Prediction"
- Neural network icon
- Output: prediction for genomic input

STEP 2 (RIGHT): "Interpretability Analysis"
- Attribution maps, TF-MoDISco, attention visualization icons
- Output: candidate important features

STEP 3 (BOTTOM RIGHT): "Hypothesis Generation"
- Statement: "GATA motif drives activity"
- Testable prediction formulated

STEP 4 (BOTTOM): "Experimental Validation"
Multiple test icons:
- EMSA (binding test)
- Reporter assay (activity test)
- CRISPR deletion (necessity test)
- MPRA (systematic test)

STEP 5 (BOTTOM LEFT): "Evaluate Results"
Branch point:
- Validated ✓ → Continue to refinement
- Failed ✗ → Identify limitation

STEP 6 (LEFT): "Model Refinement"
- Updated training, architecture insights
- Return to Step 1

CENTER: "Closed-loop discovery"

EXAMPLE PATHWAYS (annotated):
- "TF-MoDISco → EMSA confirms binding ✓"
- "Attention pattern → CRISPR confirms enhancer ✓"
- "GC attribution → MPRA shows no effect ✗ → confounder identified"

Professional scientific style, circular workflow diagram, white background.

Save as: 06-fig-validation-pipeline.svg
```

### Post-Processing Notes
- Add specific experiment details
- Include success/failure examples
- Show iteration numbers

### Fallback Description
"Interpretability validation pipeline: model prediction → interpretability analysis → hypothesis generation → experimental validation → evaluate results → model refinement. Validated hypotheses advance biology; failures identify model limitations or confounders. Closed-loop iteration improves both understanding and model quality."

### Caption Recommendation
"Closed-loop interpretability validation. Starting from model predictions, interpretability analysis generates hypotheses about important features. Experimental validation tests necessity (CRISPR deletion) and sufficiency (reporter assays). Validated hypotheses advance biological understanding; failures identify model limitations. This cycle progressively improves both mechanistic understanding and model reliability."

---

## Figure 7: Clinical Interpretability Workflow

### Files
- `figs/part_5/ch24/07-fig-clinical-interpretability.svg`

### Priority
**Enhancing** - Clinical translation

### Content Description
Clinical workflow showing how interpretability evidence strength maps to ACMG criteria.

### DALL-E Prompt
```
Scientific illustration of clinical interpretability for variant assessment. Single panel.

TOP SECTION (ACMG Evidence Framework):
- PP3: Computational supports pathogenic (weak)
- BP4: Computational supports benign (weak)
- Annotation "Evidence strength depends on interpretability"

MIDDLE SECTION (Three Evidence Levels):

LEVEL 1 (WEAK):
- Score only: "0.85 pathogenic"
- No mechanism provided
- ACMG weight: Supporting (weak)
- Icon: Simple number

LEVEL 2 (MODERATE):
- Score + attribution: "Disrupts splice site"
- SpliceAI prediction shown
- Can evaluate against transcript data
- ACMG weight: Supporting (moderate)
- Icon: Score + mechanism

LEVEL 3 (STRONG):
- Score + validated mechanism
- "Disrupts CTCF binding"
- ChIP confirms binding loss
- 3D genome shows disrupted contact
- Minigene assay confirms
- ACMG weight: Strong supporting
- Icon: Multi-evidence integration

BOTTOM SECTION (Clinical Report Elements):
Example report snippet showing:
- Variant annotation
- Score with uncertainty bars
- Mechanistic hypothesis
- Supporting evidence
- Conflicting evidence
- Recommended follow-up

Professional clinical/medical style, evidence hierarchy visualization, white background.

Save as: 07-fig-clinical-interpretability.svg
```

### Post-Processing Notes
- Add specific variant examples
- Include ACMG code references
- Show report template

### Fallback Description
"Clinical interpretability workflow: evidence strength for ACMG criteria depends on interpretability level. Score alone provides weak evidence; score plus mechanism (e.g., splice site disruption) is moderate; score with validated mechanism (binding loss, functional assay) is strong. Clinical reports should include score, mechanism, uncertainty, and recommended follow-up."

### Caption Recommendation
"Interpretability for clinical variant assessment. ACMG evidence strength depends on interpretability: a pathogenicity score alone (PP3/BP4 supporting) provides weak evidence; a score with mechanistic explanation (splice site disruption) is moderate; a score with experimentally validated mechanism (ChIP-confirmed binding loss, functional assay) is strong. Clinical reports should communicate the mechanism, not just the score, to enable evidence integration."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Attribution Comparison | 1 | Essential | Medium |
| In Silico Mutagenesis | 4 | High | Medium |
| TF-MoDISco | 1 | High | High |
| Attention Visualization | 3 | High | Medium |
| Plausible vs Faithful | 1 | Essential | Low |
| Validation Pipeline | 1 | High | Medium |
| Clinical Interpretability | 1 | Enhancing | Medium |

## Recommended Generation Order
1. Plausible vs Faithful (core concept)
2. Attribution Comparison (method overview)
3. In Silico Mutagenesis (gold standard)
4. TF-MoDISco (motif discovery)
5. Attention Visualization (with caveats)
6. Validation Pipeline (practical workflow)
7. Clinical Interpretability (translation)

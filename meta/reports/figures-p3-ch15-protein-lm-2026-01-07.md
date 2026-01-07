# Figure Report: Chapter 15 - Protein Language Models

**Chapter:** Part 3, Chapter 15 - Protein Language Models
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (17 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 15.1: Emergent Properties of PLMs (Four-Panel)

**Files:**
- `figs/part_3/ch15/01-A-fig-plm-emergent.svg`
- `figs/part_3/ch15/01-B-fig-plm-emergent.svg`
- `figs/part_3/ch15/01-C-fig-plm-emergent.svg`
- `figs/part_3/ch15/01-D-fig-plm-emergent.svg`

**Priority:** Essential
**Type:** Multi-panel emergent capability demonstration

### Panel A: Contact Prediction

**Content:** Attention matrix from ESM compared to experimental contact map. Attention heads learn to identify residue-residue contacts without structural supervision.

**DALL-E Prompt:**
```
Create a scientific comparison of attention and contact maps. Save as: 01-A-fig-plm-emergent.svg

Side-by-side matrices:

LEFT: "ESM Attention Weights"
- L×L matrix with attention pattern
- Off-diagonal clusters indicating learned contacts

RIGHT: "Experimental Contact Map"
- L×L matrix with known structural contacts
- Similar pattern to attention

OVERLAY annotation showing correlation

Title: "Attention Captures Residue Contacts"
Annotation: "r = 0.8+ with no structural supervision"

Color scale: white to dark blue. Clean scientific comparison, white background. Professional emergent property figure.
```

**Caption for Panel A:**
"Attention heads learn residue contacts. Comparison between ESM attention patterns (left) and experimental contact maps (right) reveals that specific attention heads specialize in capturing residue-residue proximity relationships. This contact information emerges from masked language modeling on sequences alone, without any structural supervision."

### Panel B: Secondary Structure Encoding

**Content:** UMAP of residue embeddings colored by secondary structure (helix, sheet, coil). Clear clustering shows structure is encoded in representations.

**DALL-E Prompt:**
```
Create a scientific UMAP showing secondary structure encoding. Save as: 01-B-fig-plm-emergent.svg

UMAP scatter plot:
- Points representing individual residue embeddings
- Color-coded by secondary structure:
  - Red: Alpha helix
  - Blue: Beta sheet
  - Gray: Coil/loop
- Clear clustering by structure type
- Distinct regions for each secondary structure

Title: "Secondary Structure Emerges in Embedding Space"
Legend showing structure types

Clean UMAP visualization, white background. Professional representation analysis figure.
```

**Caption for Panel B:**
"Secondary structure emerges in residue embeddings. UMAP projection of ESM embeddings colored by secondary structure assignment shows clear clustering: alpha helices (red), beta sheets (blue), and coils (gray) occupy distinct regions of embedding space. This organization arises without structure labels, reflecting sequence patterns that evolution has associated with each structural context."

### Panel C: Functional Site Attention

**Content:** Attention visualization on a protein structure showing elevated attention on catalytic residues and binding sites.

**DALL-E Prompt:**
```
Create a scientific visualization of attention on functional sites. Save as: 01-C-fig-plm-emergent.svg

Protein structure cartoon (ribbon diagram):
- Overall structure in gray
- Active site residues highlighted in red (high attention)
- Binding pocket residues highlighted in orange
- Non-functional residues in light gray (low attention)

Attention intensity mapped as color/size

Title: "Attention Concentrates on Functional Sites"
Annotation: "Catalytic residues receive 3× average attention"

Clean protein visualization with attention overlay, white background. Professional functional site figure.
```

**Caption for Panel C:**
"Attention concentrates on functionally important positions. Visualization of attention weights mapped onto protein structure shows elevated attention on catalytic residues (red) and binding site positions (orange). These functionally critical sites receive 2-4 times higher attention than average residues, despite no functional annotation during training."

### Panel D: Taxonomic Organization

**Content:** UMAP of protein embeddings colored by taxonomic origin (bacteria, archaea, eukaryota). Shows evolutionary relationships encoded in representations.

**DALL-E Prompt:**
```
Create a scientific UMAP showing taxonomic organization. Save as: 01-D-fig-plm-emergent.svg

UMAP scatter plot:
- Points representing protein embeddings
- Color-coded by domain of life:
  - Blue: Bacteria
  - Green: Archaea
  - Orange: Eukaryota
- Clustering shows proteins from same domain near each other
- Some overlap where function conserved across domains

Title: "Evolutionary Relationships in Embedding Space"
Legend showing taxonomic categories

Clean UMAP visualization, white background. Professional evolutionary analysis figure.
```

**Caption for Panel D:**
"Protein embeddings encode evolutionary relationships. UMAP projection colored by taxonomic origin shows that proteins from the same domain of life cluster together, reflecting evolutionary divergence encoded in sequence patterns. Overlapping regions represent functionally conserved protein families where sequence similarity persists across domains."

### Combined Caption

**Full Figure Caption:**
"Emergent properties of protein language models. (A) Specific attention heads capture residue-residue contacts with high correlation to experimental structures. (B) Secondary structure emerges as distinct clusters in embedding space. (C) Attention concentrates on functionally important positions including catalytic sites and binding pockets. (D) Evolutionary relationships are encoded, with proteins clustering by taxonomic origin. All properties emerge from masked language modeling on protein sequences without explicit structural or functional supervision, demonstrating that evolutionary sequence patterns encode rich biological information."

---

## Figure 15.2: ESM-2 Scaling (Three-Panel)

**Files:**
- `figs/part_3/ch15/02-A-fig-esm2-scaling.svg`
- `figs/part_3/ch15/02-B-fig-esm2-scaling.svg`
- `figs/part_3/ch15/02-C-fig-esm2-scaling.svg`

**Priority:** Essential
**Type:** Scaling law demonstration

### Panel A: Parameter Scaling

**Content:** Log-log plot of model size (8M to 15B parameters) vs. perplexity, showing smooth power-law improvement.

**DALL-E Prompt:**
```
Create a scientific log-log scaling plot for ESM-2. Save as: 02-A-fig-esm2-scaling.svg

Log-log plot:
- X-axis: "Parameters" (8M to 15B, log scale)
- Y-axis: "Perplexity" (log scale, decreasing upward)
- Points for each model size: 8M, 35M, 150M, 650M, 3B, 15B
- Power-law trend line through points
- Equation: "Perplexity ∝ N^(-α)"

Labels for each point with ESM-2 variant name
Title: "Scaling of ESM-2 Model Family"

Clean log-log plot with trend line, white background. Professional scaling law figure.
```

**Caption for Panel A:**
"ESM-2 perplexity follows power-law scaling with parameters. Models ranging from 8 million to 15 billion parameters show smooth improvement in sequence modeling, with perplexity decreasing as N^(-α). This predictable relationship enabled informed decisions about computational investment during ESM-2 development."

### Panel B: Downstream Task Scaling

**Content:** Multiple lines showing how different downstream tasks (contact, structure, function) all improve with model size.

**DALL-E Prompt:**
```
Create a scientific plot showing downstream task scaling. Save as: 02-B-fig-esm2-scaling.svg

Multi-line plot:
- X-axis: "Parameters" (log scale, 8M to 15B)
- Y-axis: "Task Performance" (0.5 to 1.0)
- Multiple colored lines for different tasks:
  - Blue: "Contact Prediction"
  - Green: "Structure (GDT-TS)"
  - Orange: "Variant Effect"
  - Purple: "Function Prediction"
- All lines show upward trend with similar slopes
- 15B model shows best performance across all tasks

Title: "Downstream Performance Scales Consistently"
Legend showing task colors

Clean multi-line scaling plot, white background. Professional multi-task scaling figure.
```

**Caption for Panel B:**
"Downstream task performance scales consistently across tasks. Contact prediction, structure modeling, variant effect scoring, and function prediction all improve with model size following similar trends. The 15B parameter model achieves best performance across all evaluated tasks, demonstrating that scale benefits transfer broadly."

### Panel C: Compute Efficiency

**Content:** Iso-performance contours showing the trade-off between model size and training compute.

**DALL-E Prompt:**
```
Create a scientific contour plot showing ESM-2 compute efficiency. Save as: 02-C-fig-esm2-scaling.svg

Contour plot:
- X-axis: "Training FLOPs" (log scale)
- Y-axis: "Model Parameters" (log scale)
- Iso-perplexity contours (same perplexity along each curve)
- Color gradient: red (high perplexity) to blue (low)
- Diagonal ridge showing optimal scaling
- ESM-2 model points plotted on optimal line

Title: "Compute-Optimal Model Scaling"
Annotation: "ESM-2 follows near-optimal scaling"

Clean contour plot, white background. Professional compute efficiency figure.
```

**Caption for Panel C:**
"ESM-2 development followed compute-optimal scaling. Iso-perplexity contours show combinations of model size and training compute achieving equivalent performance. The ESM-2 model family (points) closely tracks the optimal ridge, maximizing performance for given computational resources. This efficient scaling enabled reaching 15B parameters within available compute budget."

### Combined Caption

**Full Figure Caption:**
"Scaling laws for protein language models demonstrated by ESM-2. (A) Perplexity decreases as a power law of parameter count from 8M to 15B parameters. (B) Downstream task performance scales consistently across diverse applications including contact prediction, structure modeling, and variant effect scoring. (C) ESM-2 development followed near-optimal compute scaling, maximizing capability for given resources. These scaling relationships, mirroring observations in natural language models, suggest that continued scaling would yield further improvements in protein understanding."

---

## Figure 15.3: ESMFold Architecture (Four-Panel)

**Files:**
- `figs/part_3/ch15/03-A-fig-esmfold.svg`
- `figs/part_3/ch15/03-B-fig-esmfold.svg`
- `figs/part_3/ch15/03-C-fig-esmfold.svg`
- `figs/part_3/ch15/03-D-fig-esmfold.svg`

**Priority:** High
**Type:** Architecture and comparison

### Panel A: ESMFold vs. AlphaFold2 Architecture

**Content:** Side-by-side comparison showing ESMFold's single-sequence input vs. AlphaFold2's MSA requirement.

**DALL-E Prompt:**
```
Create a scientific architecture comparison of ESMFold vs AlphaFold2. Save as: 03-A-fig-esmfold.svg

Side-by-side architecture diagrams:

LEFT (AlphaFold2):
- Input: "MSA (1000s of sequences)"
- "MSA Processing"
- "Evoformer"
- "Structure Module"
- Output: "3D Structure"
- Annotation: "Minutes per prediction"

RIGHT (ESMFold):
- Input: "Single Sequence"
- "ESM-2 (pretrained)"
- "Folding Module"
- Output: "3D Structure"
- Annotation: "Seconds per prediction"

Comparison arrow: "60× faster"
Title: "Single-Sequence vs. MSA-Based Folding"

Clean architecture comparison, white background. Professional structure prediction figure.
```

**Caption for Panel A:**
"ESMFold eliminates MSA requirement. AlphaFold2 (left) requires computing multiple sequence alignments from thousands of homologs before structure prediction. ESMFold (right) uses pretrained ESM-2 representations from a single sequence, achieving 60× speedup while maintaining competitive accuracy for most proteins."

### Panel B: Speed vs. Accuracy Trade-off

**Content:** Scatter plot comparing ESMFold and AlphaFold2 on accuracy (GDT-TS) vs. speed for the same protein set.

**DALL-E Prompt:**
```
Create a scientific comparison of speed vs accuracy. Save as: 03-B-fig-esmfold.svg

Two-axis comparison:
- X-axis: "Prediction Time (log scale, seconds)"
- Y-axis: "Structure Accuracy (GDT-TS)"

Two clusters of points:
- Blue: "AlphaFold2" (high accuracy ~0.92, slow ~100s)
- Green: "ESMFold" (good accuracy ~0.85, fast ~2s)

Arrow showing trade-off
Annotation: "10% accuracy loss, 50× speed gain"
Pareto frontier line

Title: "Speed-Accuracy Trade-off"

Clean scatter comparison, white background. Professional performance comparison figure.
```

**Caption for Panel B:**
"ESMFold trades modest accuracy for dramatic speed improvement. Comparison on the same protein set shows ESMFold achieving approximately 85% of AlphaFold2's accuracy at 50 times the speed. This trade-off makes ESMFold practical for proteome-scale structure prediction where MSA computation would be prohibitive."

### Panel C: Failure Modes

**Content:** Examples where ESMFold fails: orphan proteins without homologs, recent evolutionary innovations, highly dynamic proteins.

**DALL-E Prompt:**
```
Create a scientific visualization of ESMFold failure modes. Save as: 03-C-fig-esmfold.svg

Three failure case comparisons:

CASE 1 "Orphan Proteins":
- Predicted structure (gray, low confidence)
- True structure (colored)
- Poor overlay, large RMSD
- Annotation: "No evolutionary signal"

CASE 2 "Novel Folds":
- Similar poor prediction
- Annotation: "Unseen in training"

CASE 3 "Dynamic Proteins":
- Multiple conformations shown
- Prediction shows single state
- Annotation: "Cannot capture dynamics"

Title: "When Single-Sequence Prediction Fails"

Clean failure mode illustration, white background. Professional limitation analysis figure.
```

**Caption for Panel C:**
"ESMFold fails for specific protein categories. Orphan proteins lacking evolutionary relatives have no sequence patterns for the language model to leverage. Novel folds not present in training data cannot be predicted by pattern matching. Highly dynamic proteins with multiple conformations are poorly served by single-structure prediction. These cases require AlphaFold2 with explicit MSA construction or alternative approaches."

### Panel D: Application at Scale

**Content:** Visualization showing ESMFold enabling proteome-scale structure prediction (millions of structures predicted for metagenomic databases).

**DALL-E Prompt:**
```
Create a scientific visualization of ESMFold at scale. Save as: 03-D-fig-esmfold.svg

Scale visualization:

LEFT: "Metagenomic Databases"
- "617M protein sequences"
- Database icon

CENTER: "ESMFold Pipeline"
- Parallel processing arrows
- "~2 seconds per structure"

RIGHT: "ESM Metagenomic Atlas"
- "617M structures predicted"
- Structure gallery visualization
- "First proteome-scale structural survey"

Statistics box:
- "Compute: 2,000 GPU-months"
- "Coverage: All known protein families + novel"

Title: "Proteome-Scale Structure Prediction"

Clean scale visualization, white background. Professional large-scale application figure.
```

**Caption for Panel D:**
"ESMFold enables proteome-scale structure prediction. The ESM Metagenomic Atlas applied ESMFold to 617 million protein sequences from metagenomic databases, generating the first comprehensive structural survey of protein diversity. This scale would be computationally prohibitive with MSA-based methods, demonstrating how language model pretraining enables new scientific capabilities."

### Combined Caption

**Full Figure Caption:**
"ESMFold structure prediction from single sequences. (A) Architecture comparison: ESMFold uses pretrained ESM-2 representations from single sequences, eliminating AlphaFold2's MSA requirement and achieving 60× speedup. (B) Speed-accuracy trade-off: ESMFold achieves ~85% of AlphaFold2's accuracy at 50× the speed. (C) Failure modes: orphan proteins, novel folds, and dynamic proteins remain challenging without evolutionary context. (D) Scale application: the ESM Metagenomic Atlas predicted structures for 617 million proteins, demonstrating capabilities impossible with MSA-based methods."

---

## Figure 15.4: PLM Variant Scoring (Four-Panel)

**Files:**
- `figs/part_3/ch15/04-A-fig-plm-variant-scoring.svg`
- `figs/part_3/ch15/04-B-fig-plm-variant-scoring.svg`
- `figs/part_3/ch15/04-C-fig-plm-variant-scoring.svg`
- `figs/part_3/ch15/04-D-fig-plm-variant-scoring.svg`

**Priority:** Essential
**Type:** Method explanation and validation

### Panel A: Log-Likelihood Ratio Scoring

**Content:** Schematic showing how variant effect is computed as the difference in model likelihood between wild-type and mutant sequences.

**DALL-E Prompt:**
```
Create a scientific diagram of log-likelihood ratio variant scoring. Save as: 04-A-fig-plm-variant-scoring.svg

Two parallel computations:

TOP PATH "Wild-type":
- Sequence: "...MVLK..."
- Arrow to ESM model
- Output: "P(L|context) = 0.92"

BOTTOM PATH "Mutant":
- Sequence: "...MVPK..." (L→P substitution)
- Arrow to ESM model
- Output: "P(P|context) = 0.03"

COMPUTATION:
- Score = log(P_mut) - log(P_wt)
- Score = log(0.03) - log(0.92) = -3.4
- Interpretation: "Strongly deleterious"

Title: "Zero-Shot Variant Scoring via LLR"

Clean computation diagram, white background. Professional variant scoring figure.
```

**Caption for Panel A:**
"Log-likelihood ratio scoring for variant effects. The model computes probabilities for wild-type (0.92) and mutant (0.03) amino acids given sequence context. The log ratio quantifies how much the variant violates the model's learned expectations—more negative scores indicate stronger evolutionary constraint at that position."

### Panel B: Correlation with Experimental Effects

**Content:** Scatter plot showing PLM scores correlate with deep mutational scanning (DMS) experimental measurements.

**DALL-E Prompt:**
```
Create a scientific scatter plot of PLM vs DMS correlation. Save as: 04-B-fig-plm-variant-scoring.svg

Scatter plot:
- X-axis: "ESM Log-Likelihood Ratio"
- Y-axis: "DMS Fitness Score"
- Points showing positive correlation
- Trend line with r² annotation
- Density coloring (darker = more points)

Title: "PLM Scores Correlate with Experimental Effects"
Annotation: "Spearman ρ = 0.45-0.65 across proteins"

Clean correlation scatter, white background. Professional validation figure.
```

**Caption for Panel B:**
"PLM scores correlate with experimental fitness measurements. Scatter plot comparing ESM log-likelihood ratios with deep mutational scanning (DMS) fitness scores shows moderate to strong correlation (Spearman ρ = 0.45-0.65). This correlation enables zero-shot variant effect prediction without training on experimental data."

### Panel C: ClinVar Pathogenicity Classification

**Content:** ROC curve showing PLM scores discriminate pathogenic from benign variants in ClinVar.

**DALL-E Prompt:**
```
Create a scientific ROC curve for ClinVar classification. Save as: 04-C-fig-plm-variant-scoring.svg

ROC curve:
- X-axis: "False Positive Rate" (0 to 1)
- Y-axis: "True Positive Rate" (0 to 1)
- Diagonal chance line
- ESM curve well above diagonal
- AUC annotation: "auROC = 0.85"

Comparison lines:
- Blue: ESM-1v (0.85)
- Green: ESM-2 (0.87)
- Gray: SIFT (0.70) for reference

Title: "Pathogenicity Classification on ClinVar"
Legend showing method AUCs

Clean ROC curve comparison, white background. Professional classification figure.
```

**Caption for Panel C:**
"PLM scores discriminate pathogenic from benign ClinVar variants. ROC analysis shows ESM-based scoring achieves auROC of 0.85-0.87 for binary pathogenicity classification, substantially outperforming traditional conservation-based methods (SIFT, auROC ~0.70). This zero-shot performance requires no training on pathogenicity labels."

### Panel D: Position-Specific Performance

**Content:** Heatmap showing variant effect prediction accuracy varies by position—better at constrained core positions, worse at variable surface positions.

**DALL-E Prompt:**
```
Create a scientific heatmap of position-specific performance. Save as: 04-D-fig-plm-variant-scoring.svg

Protein structure cartoon with performance overlay:

STRUCTURE colored by prediction accuracy:
- Core (buried) positions: Blue (high correlation, r > 0.6)
- Surface (exposed) positions: Red (low correlation, r < 0.3)
- Active site: Green (highest correlation, r > 0.7)

Bar chart inset:
- "Core": 0.65 correlation
- "Surface": 0.25 correlation
- "Active site": 0.70 correlation

Title: "Position-Specific Prediction Quality"
Annotation: "Best for constrained positions"

Clean structure with accuracy overlay, white background. Professional position-specific figure.
```

**Caption for Panel D:**
"Prediction quality varies by structural context. PLM variant scoring performs best at evolutionarily constrained positions: core residues (buried, blue) and active sites (green) show high correlation with experimental effects. Surface positions (exposed, red) show weaker correlation because evolutionary constraint is weaker and variants are more tolerated. This pattern reflects that PLMs learn evolutionary constraint, which is strongest where function depends on sequence."

### Combined Caption

**Full Figure Caption:**
"Protein language model variant effect prediction. (A) Zero-shot scoring computes log-likelihood ratios between wild-type and mutant amino acids given sequence context. (B) PLM scores correlate moderately to strongly with deep mutational scanning fitness measurements (ρ = 0.45-0.65). (C) Binary pathogenicity classification on ClinVar achieves auROC of 0.85-0.87 without training on pathogenicity labels. (D) Performance varies by structural position, with best predictions at constrained core and active site residues where evolutionary pressure is strongest. These results demonstrate that evolutionary sequence patterns learned by PLMs provide clinically useful variant effect predictions."

---

## Figure 15.5: PLM Limitations

**File:** `figs/part_3/ch15/05-fig-plm-limitations.svg`
**Priority:** High
**Type:** Limitation overview

### Content Description

Multi-panel or annotated diagram showing key PLM limitations:
- Cannot predict gain-of-function mutations
- No cellular context (tissue, organelle)
- Single protein focus (no interaction partners)
- Training on natural proteins only (no synthetic/designed)
- Bias toward well-studied protein families

### DALL-E Prompt

```
Create a scientific diagram of PLM limitations. Save as: 05-fig-plm-limitations.svg

Five limitation panels in grid:

1. "Gain-of-Function":
- Icon: Mutation creating new activity
- X mark: "Cannot detect beneficial novelty"

2. "No Cellular Context":
- Icon: Cell diagram with organelles
- X mark: "Same embedding regardless of cell type"

3. "Single Protein Focus":
- Icon: Two interacting proteins
- X mark: "Cannot model interaction effects"

4. "Training Bias":
- Icon: Pie chart showing well-studied dominating
- X mark: "Biased toward characterized families"

5. "Natural Sequences Only":
- Icon: Synthetic vs natural comparison
- X mark: "May fail on designed proteins"

Central annotation: "Evolutionary constraint ≠ functional effect"
Title: "Fundamental Limitations of PLMs"

Clean limitation overview diagram, white background. Professional limitation analysis figure.
```

### Post-Processing Notes

- Use consistent iconography for each limitation
- Add brief explanations for each
- Include central unifying insight
- Color code by limitation severity

### Caption

**Recommended Caption:**
"Fundamental limitations of protein language models. PLMs learn evolutionary constraint but this differs from functional effect in several ways. (1) Gain-of-function mutations are invisible: deleterious and beneficial novelty both violate expectations but have opposite effects. (2) Cellular context is absent: the same embedding represents a protein regardless of its tissue, organelle, or interaction context. (3) Single-protein focus: effects of mutations on protein-protein interactions cannot be modeled without the partner. (4) Training bias: well-studied protein families dominate UniRef, biasing representations toward characterized proteins. (5) Natural sequences only: designed or synthetic proteins may fall outside the training distribution. These limitations constrain where PLM predictions can be trusted and where additional methods are needed."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 15.1 Emergent Properties | 4 | Essential | High (multi-panel) |
| 15.2 ESM-2 Scaling | 3 | Essential | Medium (scaling plots) |
| 15.3 ESMFold | 4 | High | Medium (architecture + results) |
| 15.4 Variant Scoring | 4 | Essential | Medium (method + validation) |
| 15.5 Limitations | 1 | High | Medium (overview) |

**Total files:** 16
**Recommended generation order:** 15.4A-D (variant scoring, most clinical), 15.1A-D (emergent), 15.2A-C (scaling), 15.3A-D (ESMFold), 15.5 (limitations)

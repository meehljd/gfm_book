# Figure Report: Chapter 6 - Convolutional Networks

**Chapter:** Part 2, Chapter 6 - Convolutional Networks
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (10 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 6.1: Convolution as Pattern Detector (Three-Panel)

**Files:**
- `figs/part_2/ch06/01-A-fig-conv-pattern-detector.svg`
- `figs/part_2/ch06/01-B-fig-conv-pattern-detector.svg`
- `figs/part_2/ch06/01-C-fig-conv-pattern-detector.svg`

**Priority:** Essential
**Type:** Multi-panel conceptual/technical diagram

### Panel A: Sliding Convolution

**Content:** Single convolutional filter (width 8) sliding across one-hot encoded DNA. Show the 4×8 filter weight matrix sliding over a 4×L input matrix. At each position, compute a dot product yielding an activation score. Highlight one position where the filter matches a motif (high activation) versus positions with low activation.

**DALL-E Prompt:**
```
Scientific diagram showing convolutional filter sliding across DNA sequence. Horizontal one-hot encoded DNA matrix (4 rows for A,C,G,T, many columns). A small 4x8 filter window highlighted in blue sliding from left to right. At the current position, show high activation (bright color) where filter matches sequence pattern. Below, a graph showing activation scores across positions with one prominent peak. Clean machine learning diagram style. White background. Professional deep learning textbook illustration.
```

**Caption for Panel A:**
"Convolutional filter as sliding pattern detector. A filter of width 8 nucleotides slides across one-hot encoded DNA, computing similarity scores at each position. The filter produces high activation where the input matches its learned weight pattern and low activation elsewhere. This sliding window operation detects motifs regardless of their position in the input sequence."

### Panel B: Learned Filter as Sequence Logo

**Content:** Visualization of learned filter weights as a sequence logo (PWM-style), with letter heights proportional to weights. Align with a corresponding JASPAR motif to show the biological pattern discovered.

**DALL-E Prompt:**
```
Scientific comparison diagram showing learned CNN filter and known transcription factor motif. Top: Sequence logo with stacked nucleotide letters (A,C,G,T) at 8 positions, letter heights varying by weight, creating characteristic DNA motif visualization. Bottom: Similar sequence logo from JASPAR database showing matching pattern. Alignment lines connecting corresponding positions. Clean bioinformatics sequence logo style. White background. Professional motif comparison visualization.
```

**Caption for Panel B:**
"Learned filter weights visualized as sequence logo. The filter weights are transformed into a position weight matrix format, with nucleotide letter heights proportional to learned weights. This visualization reveals that the filter has learned to recognize the CTCF binding motif, matching the experimentally derived consensus from the JASPAR database despite no explicit motif supervision during training."

### Panel C: Multiple Filter Diversity

**Content:** Array of multiple first-layer filters, each detecting different motifs. Show 4-6 filters with their sequence logo representations and biological labels (CTCF, ETS, AP-1, TATA box, etc.).

**DALL-E Prompt:**
```
Scientific panel showing multiple DNA sequence logos arranged in a grid (2x3 or 3x2). Each logo shows a different 8-10 nucleotide pattern with characteristic letter stacks. Labels below each: CTCF, ETS, AP-1, TATA. Different color schemes for each motif. Clean bioinformatics visualization. White background with subtle borders between panels. Professional transcription factor motif collection diagram.
```

**Caption for Panel C:**
"Diversity of first-layer filters. Different filters in the first convolutional layer learn to detect distinct transcription factor binding motifs: CTCF (insulator), ETS family, AP-1, and TATA box (core promoter). This diverse pattern detection emerges from training on chromatin accessibility data without explicit motif labels, demonstrating that the chromatin prediction objective induces biologically meaningful feature extraction."

### Combined Caption

**Full Figure Caption:**
"Convolutional filters as learned position weight matrices. (A) A filter of width 8 slides across one-hot encoded DNA, producing activation scores at each position. High activation indicates sequence matching the learned pattern. (B) Visualizing filter weights as sequence logos reveals correspondence to known transcription factor motifs. This filter has learned the CTCF binding site consensus matching the JASPAR database entry. (C) Multiple first-layer filters detect diverse motifs including CTCF, ETS, AP-1, and TATA box elements. This specialization emerges from training on chromatin prediction without explicit motif supervision."

---

## Figure 6.2: DeepSEA Architecture (Three-Panel)

**Files:**
- `figs/part_2/ch06/02-A-fig-deepsea-architecture.svg`
- `figs/part_2/ch06/02-B-fig-deepsea-architecture.svg`
- `figs/part_2/ch06/02-C-fig-deepsea-architecture.svg`

**Priority:** High
**Type:** Architecture schematic and validation

### Panel A: Architecture Schematic

**Content:** Network architecture showing: Input (1000bp one-hot, 4×1000) → Conv1 (320 filters) → MaxPool → Conv2 (480 filters) → MaxPool → Conv3 (960 filters) → MaxPool → Flatten → FC (925 units) → 919 sigmoid outputs for chromatin features. Show dimension changes at each layer.

**DALL-E Prompt:**
```
Scientific neural network architecture diagram. Left to right flow: Input matrix (4x1000) → three convolutional layer blocks with pooling (labeled 320, 480, 960 filters), decreasing in width. → Flatten operation → Fully connected layer (925 units) → Output layer with 919 sigmoid units arranged as a vertical bar. Clean deep learning architecture diagram with blue/gray color scheme. White background. Professional ML textbook illustration showing layer dimensions.
```

**Caption for Panel A:**
"DeepSEA architecture schematic. Input sequences of 1,000 base pairs (one-hot encoded as 4×1000 matrix) pass through three convolutional layers with 320, 480, and 960 filters respectively. Max pooling after each convolution compresses spatial dimensions. A fully connected layer integrates information, and 919 sigmoid outputs independently predict chromatin features from ENCODE and Roadmap Epigenomics."

### Panel B: First-Layer Filter Motif Match

**Content:** Single learned filter visualized as sequence logo, aligned with JASPAR CTCF motif showing high similarity. Include sequence alignment and correlation metric.

**DALL-E Prompt:**
```
Scientific sequence logo comparison. Two DNA sequence logos aligned vertically. Top logo labeled "Learned Filter" with nucleotide stacks. Bottom logo labeled "JASPAR CTCF" with similar nucleotide stacks. Dashed lines connecting matching positions. Correlation score (r = 0.92) displayed. Clean bioinformatics motif comparison style. White background. Professional validation figure.
```

**Caption for Panel B:**
"Learned filter matches known transcription factor motif. A first-layer filter from trained DeepSEA (top) shows high correspondence to the experimentally determined CTCF binding motif from JASPAR (bottom). This alignment emerges from training to predict chromatin accessibility, not from explicit motif supervision, confirming that the model learns biologically meaningful sequence patterns."

### Panel C: Allelic Imbalance Validation

**Content:** Scatter plot showing predicted versus observed allelic imbalance for DNase-seq variants. Show correlation, with points colored by prediction confidence. Reference line at y=x.

**DALL-E Prompt:**
```
Scientific scatter plot for model validation. X-axis labeled "Predicted Allelic Imbalance", Y-axis "Observed Allelic Imbalance". Points scattered around diagonal reference line, showing positive correlation. Points colored by density or confidence (dark = high, light = low). Correlation coefficient displayed (r = 0.XX). Clean statistical visualization with white background and grid lines. Professional genomics validation figure.
```

**Caption for Panel C:**
"Variant effect prediction validated by allelic imbalance. DeepSEA's predicted chromatin effects correlate with experimentally observed allelic imbalance in DNase-seq (r = 0.XX). Variants predicted to increase accessibility (positive values) show corresponding experimental bias toward that allele. This correlation confirms that in silico mutagenesis captures genuine variant effects despite never training on variant data."

### Combined Caption

**Full Figure Caption:**
"DeepSEA: regulatory prediction from sequence. (A) Architecture schematic showing progression from 1,000 bp one-hot input through three convolutional layers to 919 chromatin feature predictions. (B) First-layer filters learn to recognize known transcription factor motifs, with this example matching JASPAR's CTCF consensus. (C) Variant effect predictions validated against allelic imbalance measurements, confirming that sequence-based predictions capture genuine regulatory variation. DeepSEA demonstrated that deep learning on functional genomics data could discover regulatory patterns without encoding human assumptions about what matters."

---

## Figure 6.3: ExPecto Pipeline

**File:** `figs/part_2/ch06/03-fig-expecto-pipeline.svg`
**Priority:** Enhancing
**Type:** Three-component pipeline diagram

### Content Description

Modular pipeline showing three components:

1. **Component 1 (Beluga CNN):** Input 40kb window around TSS, sliding 2kb windows, producing chromatin predictions at 200 spatial positions
2. **Component 2 (Spatial Transformation):** Exponential decay functions (upstream and downstream) reducing ~400,000 features to ~20,000
3. **Component 3 (Tissue-Specific Linear Models):** 218 separate L2-regularized linear regression models producing per-tissue expression predictions

Show example delta scores for variant effect prediction.

### DALL-E Prompt

```
Scientific modular pipeline diagram with three connected components. Left component: CNN scanning across 40kb region with sliding windows, output as 200 spatial positions. Middle component: Exponential decay curves transforming spatial features, showing upstream and downstream integration. Right component: 218 parallel linear model outputs arranged as a vertical bar representing tissues. Arrows connecting components showing data flow. Clean bioinformatics pipeline style. White background. Professional systems biology diagram.
```

### Post-Processing Notes

- Add clear labels for each component
- Show approximate feature counts at each stage (2002 chromatin → 400K spatial → 20K transformed → 218 expression)
- Add tissue labels (liver, brain, heart, etc.) near output
- Include delta score formula for variant effect

### Fallback Description

Create in diagramming software (draw.io, BioRender):
- Three connected boxes representing pipeline stages
- Arrows showing data flow and dimension reduction
- Annotations for feature counts and biological interpretation

### Caption

**Recommended Caption:**
"ExPecto pipeline: from chromatin to expression. The modular architecture comprises three components. (1) Beluga CNN scans a 40kb window around each transcription start site with 2kb sliding windows, predicting 2,002 chromatin features at 200 spatial positions and generating over 400,000 features per gene. (2) Spatial transformation applies exponential decay functions separately for upstream and downstream regions, encoding the prior that nearby elements contribute more to expression than distant ones, reducing dimensionality to approximately 20,000 features. (3) Tissue-specific linear regression models (218 total, one per tissue) predict log expression from transformed features. This modular design separates shared sequence-to-chromatin processing from tissue-specific expression modeling, enabling interpretable analysis of which chromatin features drive expression in each context."

---

## Figure 6.4: SpliceAI Architecture (Two-Panel)

**Files:**
- `figs/part_2/ch06/04-A-fig-spliceai-architecture.svg`
- `figs/part_2/ch06/04-B-fig-spliceai-architecture.svg`

**Priority:** High
**Type:** Architecture diagram

### Panel A: Dilated Convolutions

**Content:** Diagram showing how dilated convolutions expand receptive field without proportional parameter growth. Show dilation rates (1, 2, 4, 8, 16...) with gaps between filter taps. Illustrate how stacking 32 layers with increasing dilation reaches 10kb context.

**DALL-E Prompt:**
```
Scientific diagram showing dilated convolution receptive field expansion. Multiple horizontal layers stacked vertically. Each layer shows a filter with gaps (dilation) between taps. Dilation increases from bottom (rate 1, no gaps) to top (rate 16, large gaps). Lines connecting each layer's outputs to inputs below. Total receptive field grows exponentially with depth. Clean neural network architecture diagram. White background with gray connecting lines. Professional deep learning illustration.
```

**Caption for Panel A:**
"Dilated convolutions expand receptive field efficiently. Standard convolutions (dilation rate 1) sample consecutive positions. Dilated convolutions sample at intervals, with dilation rate 2, 4, 8, 16, etc. progressively expanding coverage. Stacking convolutions with increasing dilation enables SpliceAI's 32-layer architecture to integrate 10kb of context while maintaining sensitivity to local patterns through lower layers."

### Panel B: Residual Block Structure

**Content:** SpliceAI's residual block with skip connections from every 4th block to the output layer. Show how this enables gradient flow through 32 layers.

**DALL-E Prompt:**
```
Scientific residual network architecture diagram. Vertical stack of 8 residual blocks, each containing two convolutional layers with a skip connection around them. Additional long skip connections from every 4th block to the final output layer at right. Arrows showing gradient flow paths through both short and long connections. Clean deep learning architecture style. White background. Professional neural network diagram showing deep architecture with skip connections.
```

**Caption for Panel B:**
"Residual connections enable ultra-deep architecture. SpliceAI uses 32 residual blocks, each learning incremental refinements to the representation. Skip connections every 4th block feed directly to the penultimate layer, providing additional gradient highways that stabilize training. This architecture achieves the depth necessary to integrate 10kb context while maintaining trainability through multiple parallel gradient paths."

### Combined Caption

**Full Figure Caption:**
"SpliceAI architecture innovations for long-range splicing prediction. (A) Dilated convolutions expand the receptive field efficiently by sampling input positions at intervals. Stacking layers with dilation rates 1, 2, 4, 8, 16... enables integration of 10,000 nucleotides of context without proportional parameter growth. Lower layers with small dilation capture local splice site grammar while upper layers with large dilation integrate distal determinants like branch points and exonic splicing enhancers. (B) Residual block structure with skip connections from every 4th block to the output. This enables training of 32 layers by providing multiple gradient pathways, preventing vanishing gradients that would otherwise block learning in such a deep network."

---

## Figure 6.5: Receptive Field Ceiling

**File:** `figs/part_2/ch06/05-fig-receptive-field-ceiling.svg`
**Priority:** Essential
**Type:** Genome-scale comparison diagram

### Content Description

Horizontal genome diagram comparing effective context windows across CNN architectures:
- DeepSEA: ~1kb
- ExPecto/Beluga: 2kb windows, 40kb aggregated
- SpliceAI: 10kb
- Enformer (for contrast): 200kb

Overlay biologically relevant distances:
- Typical TF binding site: ~10bp
- Promoter region: ~1kb
- Enhancer-gene distance: 10-100kb
- TAD size: ~1Mb

Highlight the gap: "Most enhancer-promoter interactions exceed CNN receptive fields."

### DALL-E Prompt

```
Scientific genome scale comparison diagram. Horizontal genomic region with scale bar. Multiple colored bars of different lengths showing context windows: short bar (1kb) for DeepSEA, medium bar (10kb) for SpliceAI, longer bar (40kb) for ExPecto, longest bar (200kb) for Enformer. Below: biological features with brackets showing typical distances - small bracket for promoter (~1kb), medium bracket for enhancer-promoter distance (50kb), large bracket for TAD (~1Mb). Gap highlighted between CNN capabilities and biological requirements. Clean genomics visualization style. White background. Professional comparative figure.
```

### Post-Processing Notes

- Add clear model labels with context lengths
- Add biological feature labels with typical distance ranges
- Highlight gap between enhancer-promoter distance and CNN capabilities
- Add annotation: "Attention mechanisms required for long-range regulatory modeling"

### Fallback Description

Create in matplotlib or diagramming software:
- Chromosome/genome ideogram at top
- Stacked bars showing context windows for each model
- Biological feature brackets below
- Annotation highlighting the limitation

### Caption

**Recommended Caption:**
"The receptive field ceiling of convolutional architectures. Context windows of representative CNN-based models compared to biologically relevant regulatory distances. DeepSEA integrates approximately 1kb of context; SpliceAI extends to 10kb through dilated convolutions; ExPecto aggregates predictions across 40kb. These contexts suffice for local features like transcription factor binding sites (~10bp) and promoter elements (~1kb) but cannot capture enhancer-promoter interactions typically spanning 10-100kb. Even SpliceAI's 10kb context falls short of the distances at which most GWAS signals reside from their target genes. This architectural limitation, not data scarcity, motivated the shift to attention mechanisms that compute direct interactions across arbitrary distances."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 6.1 Conv Pattern Detector | 3 | Essential | Medium (multi-panel) |
| 6.2 DeepSEA Architecture | 3 | High | Medium (architecture + validation) |
| 6.3 ExPecto Pipeline | 1 | Enhancing | Medium (pipeline) |
| 6.4 SpliceAI Architecture | 2 | High | Medium (architecture) |
| 6.5 Receptive Field | 1 | Essential | Low-Medium (comparison) |

**Total files:** 10
**Recommended generation order:** 6.5 (comparison, simplest), 6.4A-B (architecture), 6.3 (pipeline), 6.2A-C (architecture + validation), 6.1A-C (conceptual)

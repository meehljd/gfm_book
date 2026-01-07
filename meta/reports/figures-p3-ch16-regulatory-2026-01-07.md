# Figure Report: Chapter 16 - Regulatory Sequence Models

**Chapter:** Part 3, Chapter 16 - Regulatory Sequence Models
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (13 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 16.1: Long-Range Regulation (Four-Panel)

**Files:**
- `figs/part_3/ch16/01-A-fig-long-range-regulation.svg`
- `figs/part_3/ch16/01-B-fig-long-range-regulation.svg`
- `figs/part_3/ch16/01-C-fig-long-range-regulation.svg`
- `figs/part_3/ch16/01-D-fig-long-range-regulation.svg`

**Priority:** Essential
**Type:** Biological motivation for architecture

### Panel A: Enhancer-Promoter Distance

**Content:** Genome browser view showing enhancer and promoter separated by ~50kb, with Hi-C contact evidence.

**DALL-E Prompt:**
```
Create a scientific genome browser showing enhancer-promoter distance. Save as: 01-A-fig-long-range-regulation.svg

Browser-style visualization:
- Genomic coordinates track (0-100kb)
- Gene track showing target gene with promoter
- Enhancer element ~50kb upstream
- Hi-C contact arc connecting enhancer to promoter
- GWAS hit indicated at enhancer

Scale bar: "50 kb"
Title: "Regulatory Elements Span Tens of Kilobases"
Annotation: "GWAS variant in enhancer affects gene 50kb away"

Clean genome browser style, white background. Professional regulatory visualization.
```

**Caption for Panel A:**
"Regulatory elements span tens of kilobases. Genome browser view showing an enhancer ~50kb from its target promoter, connected by a Hi-C contact arc indicating 3D proximity. Many GWAS variants fall in such distal enhancers, requiring models with sufficient context to capture enhancer-gene relationships."

### Panel B: Context Length Requirements

**Content:** Histogram of enhancer-gene distances showing most require 50-200kb context.

**DALL-E Prompt:**
```
Create a scientific histogram of enhancer-gene distances. Save as: 01-B-fig-long-range-regulation.svg

Histogram:
- X-axis: "Enhancer-Gene Distance (kb)" (0 to 500)
- Y-axis: "Number of Interactions"
- Distribution peaked around 50-100kb, long tail to 500kb
- Vertical lines showing model context limits:
  - Red: "DeepSEA (1kb)"
  - Orange: "SpliceAI (10kb)"
  - Green: "Enformer (200kb)"
- Shaded region showing "Captured by Enformer"

Title: "Distribution of Regulatory Distances"
Annotation: "Most interactions require >10kb context"

Clean histogram with context limits, white background. Professional distance distribution figure.
```

**Caption for Panel B:**
"Context length requirements for regulatory modeling. Distribution of enhancer-gene distances from Hi-C data shows most interactions span 50-200kb. Vertical lines indicate context limits of different models: DeepSEA (1kb) and SpliceAI (10kb) miss most interactions, while Enformer (200kb) captures the majority of enhancer-promoter pairs."

### Panel C: 3D Chromatin Context

**Content:** TAD structure visualization showing how 3D organization constrains enhancer-promoter pairing.

**DALL-E Prompt:**
```
Create a scientific TAD structure visualization. Save as: 01-C-fig-long-range-regulation.svg

TAD triangle diagram:
- Horizontal axis showing genomic position
- Triangular Hi-C heatmap above
- Two TADs visible as triangular domains
- TAD boundary marked between them
- Within-TAD contacts (high, red)
- Cross-TAD contacts (low, blue)

Below: Linear annotation showing:
- Genes within same TAD → interact
- Genes across TAD boundary → isolated

Title: "3D Chromatin Organization (TADs)"
Annotation: "Enhancers only contact genes within same TAD"

Clean TAD visualization, white background. Professional chromatin architecture figure.
```

**Caption for Panel C:**
"Topologically associating domains (TADs) constrain regulatory interactions. Hi-C heatmap shows two TADs as triangular domains with high internal contact frequency. Enhancers typically only regulate genes within the same TAD; TAD boundaries insulate against cross-domain contacts. Models must implicitly learn these constraints to correctly predict gene expression."

### Panel D: Architectural Trade-offs

**Content:** Comparison table/diagram showing CNN, hybrid, and transformer approaches for capturing long-range context.

**DALL-E Prompt:**
```
Create a scientific comparison of regulatory model architectures. Save as: 01-D-fig-long-range-regulation.svg

Architecture comparison table:

               CNN-only    Hybrid     Transformer
Context        1-10kb      200kb      1Mb+
Compute        Low         Medium     High
Long-range     Poor        Good       Best
Local          Best        Good       Medium
Example        DeepSEA     Enformer   HyenaDNA

Visual diagram below:
- CNN: Small receptive field (triangle)
- Hybrid: CNN+Attention (trapezoid + attention arcs)
- Transformer: Full attention (all-to-all connections)

Title: "Architectural Trade-offs for Regulatory Modeling"

Clean comparison diagram, white background. Professional architecture comparison figure.
```

**Caption for Panel D:**
"Architectural trade-offs for long-range regulatory modeling. Pure CNN architectures capture local patterns efficiently but have limited receptive fields. Hybrid architectures (CNN + attention) balance local pattern extraction with long-range integration. Full transformer approaches enable arbitrary-distance interactions but at higher computational cost. The choice depends on the regulatory distances most relevant to the target application."

### Combined Caption

**Full Figure Caption:**
"The biological case for long-range regulatory models. (A) Enhancers regulate genes across tens of kilobases, as shown by Hi-C contacts connecting distal elements to promoters. (B) Distribution of enhancer-gene distances shows most interactions require >10kb context, exceeding early CNN model capacities. (C) TAD structure constrains which enhancers can contact which promoters, creating patterns models must learn. (D) Different architectures trade off between context length, computational cost, and local pattern sensitivity. Hybrid approaches like Enformer balance these factors for practical 200kb contexts."

---

## Figure 16.2: Enformer Architecture

**File:** `figs/part_3/ch16/02-fig-enformer-architecture.svg`
**Priority:** Essential
**Type:** Detailed architecture diagram

### Content Description

End-to-end architecture diagram showing:
- Input: 196kb one-hot encoded sequence
- Convolutional stem with pooling
- Transformer layers for long-range integration
- Multi-head prediction for thousands of tracks (chromatin, expression)
- Output spatial resolution and track organization

### DALL-E Prompt

```
Create a scientific architecture diagram for Enformer. Save as: 02-fig-enformer-architecture.svg

Left-to-right architecture flow:

INPUT (left):
- "196kb sequence" as 4×L matrix
- One-hot encoding illustration

CONVOLUTIONAL STEM:
- Conv layers with filter counts
- Pooling operations (128× total compression)
- Output: 1536 positions × D dimensions

TRANSFORMER LAYERS:
- 11 transformer blocks with attention arcs
- Cross-position attention patterns shown
- Dimension annotations

PREDICTION HEADS:
- Branching to multiple output types
- "5313 human tracks"
- "1643 mouse tracks"

OUTPUT (right):
- Spatial resolution: 128bp bins
- Track types: DNase, H3K27ac, CAGE, etc.

Title: "Enformer: Hybrid CNN-Transformer Architecture"

Clean architecture diagram with dimension annotations, white background. Professional deep learning architecture figure.
```

### Post-Processing Notes

- Add dimension annotations at each stage
- Include pooling factors
- Show attention patterns in transformer section
- List major track categories

### Caption

**Recommended Caption:**
"Enformer hybrid architecture for gene expression prediction. Input sequences spanning 196 kilobases are one-hot encoded and processed through a convolutional stem that extracts local patterns and compresses spatial resolution by 128×. Eleven transformer layers integrate information across the compressed representation, enabling direct communication between positions separated by nearly 200kb in the original sequence. Multiple prediction heads output 5,313 human and 1,643 mouse tracks including chromatin accessibility (DNase), histone modifications (H3K27ac, H3K4me3), and transcription (CAGE), at 128bp resolution. This multi-task architecture forces shared representations to capture the regulatory cascade from accessible chromatin through transcription."

---

## Figure 16.3: Regulatory VEP Workflow

**File:** `figs/part_3/ch16/03-fig-regulatory-vep-workflow.svg`
**Priority:** High
**Type:** Workflow/pipeline diagram

### Content Description

Step-by-step workflow for using regulatory models for variant effect prediction:
1. Center variant in context window
2. Compute predictions for reference and alternate
3. Calculate delta scores across tracks
4. Aggregate into interpretable variant effect summary

### DALL-E Prompt

```
Create a scientific workflow for regulatory variant effect prediction. Save as: 03-fig-regulatory-vep-workflow.svg

Step-by-step workflow (top to bottom):

STEP 1: "Center Variant in Window"
- 196kb window with variant at center
- Reference allele highlighted

STEP 2: "Predict Reference"
- Enformer processing
- Output: 5000+ track predictions

STEP 3: "Predict Alternate"
- Same sequence with alternate allele
- Different predictions

STEP 4: "Compute Delta"
- Δ = Alt - Ref for each track
- Heatmap showing changes

STEP 5: "Aggregate Effects"
- Key affected tracks identified
- Summary score (e.g., "Reduces expression 15%")

STEP 6: "Biological Interpretation"
- "Disrupts enhancer activity"
- "Affects tissue-specific regulation"

Title: "In Silico Mutagenesis for Regulatory Variants"

Clean workflow diagram with arrows, white background. Professional VEP pipeline figure.
```

### Post-Processing Notes

- Add example values at each step
- Show multiple tracks affected
- Include interpretation guidance
- Highlight tissue-specificity aspects

### Caption

**Recommended Caption:**
"Regulatory variant effect prediction workflow. Step 1: Center the variant within the model's input window (196kb for Enformer). Step 2: Compute model predictions for the reference sequence across all tracks. Step 3: Swap in the alternate allele and recompute predictions. Step 4: Calculate delta scores (alternate minus reference) for each track and position. Step 5: Aggregate effects to identify which chromatin or expression tracks are most affected. Step 6: Interpret biological meaning—does the variant disrupt an enhancer, affect tissue-specific regulation, or alter expression levels? This in silico mutagenesis approach enables prediction of regulatory variant effects without experimental measurements."

---

## Figure 16.4: Borzoi RNA-seq Prediction (Four-Panel)

**Files:**
- `figs/part_3/ch16/04-A-fig-borzoi-rnaseq.svg`
- `figs/part_3/ch16/04-B-fig-borzoi-rnaseq.svg`
- `figs/part_3/ch16/04-C-fig-borzoi-rnaseq.svg`
- `figs/part_3/ch16/04-D-fig-borzoi-rnaseq.svg`

**Priority:** High
**Type:** Model output and application

### Panel A: RNA-seq Profile Prediction

**Content:** Predicted vs. observed RNA-seq coverage tracks across a gene, showing accurate prediction of exon structure and expression levels.

**DALL-E Prompt:**
```
Create a scientific comparison of predicted vs observed RNA-seq. Save as: 04-A-fig-borzoi-rnaseq.svg

Two aligned browser tracks:

TOP: "Predicted (Borzoi)"
- RNA-seq-like coverage profile
- Exon peaks, intron valleys
- Splice junctions visible

BOTTOM: "Observed (RNA-seq)"
- Experimental RNA-seq coverage
- Same pattern as predicted

OVERLAY region showing correlation

Gene annotation track below:
- Exon boxes
- Intron lines
- Direction arrow

Title: "Borzoi Predicts RNA-seq Coverage"
Correlation annotation: "r = 0.85"

Clean genome browser style, white background. Professional expression prediction figure.
```

**Caption for Panel A:**
"Borzoi predicts RNA-seq coverage profiles from sequence. Predicted coverage (top) closely matches observed RNA-seq (bottom) across a gene region, correctly capturing exon structure, splice junction usage, and relative expression levels. This nucleotide-resolution output enables detection of variants affecting splicing or isoform usage."

### Panel B: Isoform Quantification

**Content:** Bar chart comparing predicted vs. observed isoform proportions for a gene with alternative splicing.

**DALL-E Prompt:**
```
Create a scientific comparison of predicted vs observed isoforms. Save as: 04-B-fig-borzoi-rnaseq.svg

Paired bar chart:
- X-axis: Isoform types (Full, Exon5-skip, Exon7-8-alt, Other)
- Y-axis: Proportion (0 to 0.6)
- Blue bars: Predicted
- Orange bars: Observed
- Error bars on observed

Title: "Isoform Proportion Prediction"
Correlation annotation: "r = 0.92 across isoforms"

Gene diagram below showing different isoform structures

Clean bar comparison, white background. Professional isoform prediction figure.
```

**Caption for Panel B:**
"Borzoi predicts alternative isoform proportions. Comparison of predicted (blue) versus observed (orange) isoform usage for a gene with alternative splicing. The model correctly ranks isoform abundance and captures the dominant splice patterns, enabling detection of variants that shift isoform balance."

### Panel C: Splicing Variant Detection

**Content:** Example of Borzoi detecting a cryptic splice variant that creates aberrant isoform.

**DALL-E Prompt:**
```
Create a scientific visualization of splice variant detection. Save as: 04-C-fig-borzoi-rnaseq.svg

Two-panel comparison:

REFERENCE ALLELE (top):
- Gene diagram with normal splicing pattern
- Predicted coverage showing normal exon structure
- Annotation: "Normal splice site usage"

VARIANT ALLELE (bottom):
- Same gene with variant marked
- Predicted coverage showing aberrant splice
- New exon inclusion or exon skipping visible
- Annotation: "Cryptic splice activation"

Delta track between panels highlighting change

Title: "Detecting Splicing Variants with Borzoi"

Clean splice variant visualization, white background. Professional variant detection figure.
```

**Caption for Panel C:**
"Borzoi detects splicing variants through coverage prediction changes. The reference allele (top) shows normal splice patterns. The variant allele (bottom) activates a cryptic splice site, creating an aberrant isoform visible as changed coverage patterns. This enables detection of splice-disrupting variants beyond the canonical GT/AG dinucleotides."

### Panel D: Tissue-Specific Effects

**Content:** Heatmap showing variant effects vary by tissue, with some tissues unaffected and others showing strong expression changes.

**DALL-E Prompt:**
```
Create a scientific heatmap of tissue-specific variant effects. Save as: 04-D-fig-borzoi-rnaseq.svg

Heatmap:
- Rows: Tissues (Liver, Brain, Heart, Kidney, Lung, Blood, etc.)
- Columns: Genes near variant
- Color scale: Blue (decreased) to Red (increased)

Pattern showing:
- Target gene strongly affected in specific tissues
- Other tissues unaffected
- Nearby genes with varied effects

Title: "Tissue-Specific Variant Effects"
Annotation: "Variant affects expression only in liver and kidney"

Clean heatmap with tissue labels, white background. Professional tissue-specific figure.
```

**Caption for Panel D:**
"Regulatory variants show tissue-specific effects. Heatmap of predicted expression changes across tissues reveals the variant affects target gene expression only in liver and kidney, with other tissues unaffected. This tissue-specificity, invisible to tissue-agnostic models, is essential for understanding variant pathogenicity in the context of specific diseases."

### Combined Caption

**Full Figure Caption:**
"Borzoi predicts RNA-seq profiles from sequence for variant interpretation. (A) Predicted coverage closely matches observed RNA-seq, capturing gene structure and expression levels. (B) Alternative isoform proportions are accurately predicted, enabling detection of splicing-shift variants. (C) Splice-disrupting variants are detected through coverage pattern changes between reference and alternate alleles. (D) Tissue-specific expression effects reveal that variants may affect different tissues differently, essential for understanding disease-relevant consequences."

---

## Figure 16.5: Regulatory Model Limitations (Four-Panel)

**Files:**
- `figs/part_3/ch16/05-A-fig-regulatory-limitations.svg`
- `figs/part_3/ch16/05-B-fig-regulatory-limitations.svg`
- `figs/part_3/ch16/05-C-fig-regulatory-limitations.svg`
- `figs/part_3/ch16/05-D-fig-regulatory-limitations.svg`

**Priority:** High
**Type:** Limitation analysis

### Panel A: Reference Haplotype Assumption

**Content:** Diagram showing models process variants on reference background, ignoring other variants in the same haplotype.

**DALL-E Prompt:**
```
Create a diagram showing reference haplotype limitation. Save as: 05-A-fig-regulatory-limitations.svg

Comparison:

TOP "Model Input":
- Reference sequence with single variant inserted
- Other variants on same haplotype NOT included
- Label: "Ignores haplotype context"

BOTTOM "Reality":
- Patient haplotype with multiple linked variants
- Compound effects between variants
- Label: "Variants interact on haplotypes"

Warning annotation: "Model assumes reference background"

Clean comparison diagram, white background. Professional limitation illustration.
```

**Caption for Panel A:**
"Reference haplotype assumption ignores linked variants. Models insert single variants into reference sequences, ignoring other variants present on the same haplotype. In reality, patients carry multiple variants that may interact, potentially canceling or amplifying effects invisible to single-variant analysis."

### Panel B: Training Set Cell Type Bias

**Content:** Pie chart or bar chart showing training data dominated by certain cell types (e.g., immortalized lines, blood) with disease-relevant tissues underrepresented.

**DALL-E Prompt:**
```
Create a chart showing training cell type bias. Save as: 05-B-fig-regulatory-limitations.svg

Bar chart:
- X-axis: Cell/tissue types
- Y-axis: Number of training tracks (log scale)
- Bars showing:
  - K562 (leukemia line): Very high
  - GM12878 (lymphoblast): Very high
  - HepG2 (liver cancer): High
  - Primary tissues: Low
  - Disease-relevant (neurons, islets): Very low

Annotations:
- "Immortalized cell lines dominate"
- "Primary tissues underrepresented"

Title: "Training Data Cell Type Distribution"

Clean bar chart with bias highlighted, white background. Professional data bias figure.
```

**Caption for Panel B:**
"Training data biased toward immortalized cell lines. Bar chart shows training tracks dominated by ENCODE tier-1 cell lines (K562, GM12878) while primary tissues and disease-relevant cell types are underrepresented. Models may perform poorly for tissues absent from training data."

### Panel C: Correlation vs. Causation

**Content:** Diagram showing that predicting expression correlation is not the same as predicting causal effect of a variant.

**DALL-E Prompt:**
```
Create a diagram showing correlation vs causation limitation. Save as: 05-C-fig-regulatory-limitations.svg

Two scenarios:

LEFT "Model Predicts":
- Variant → Δ Accessibility → Δ Expression
- Direct arrow implying causation
- Label: "Implied causal chain"

RIGHT "Reality Options":
A) Variant causes expression change (correct)
B) Variant correlates but doesn't cause (confounded)
C) Variant affects accessibility, not expression

Warning: "Predicted correlation ≠ causal mechanism"

Title: "Distinguishing Correlation from Causation"

Clean conceptual diagram, white background. Professional causation limitation figure.
```

**Caption for Panel C:**
"Predicted correlation does not establish causation. Models predict that variants change accessibility and expression, but this prediction does not distinguish causal mechanisms from correlative patterns. A variant may correlate with expression changes without being the causal driver, limiting clinical utility of prediction alone."

### Panel D: Structural Variant Blindness

**Content:** Illustration showing models cannot process structural variants (inversions, CNVs, translocations) that disrupt regulatory topology.

**DALL-E Prompt:**
```
Create a diagram showing structural variant blindness. Save as: 05-D-fig-regulatory-limitations.svg

Comparison:

TOP "What Models Handle":
- Linear sequence with SNV marked
- Standard variant effect prediction
- Checkmark

BOTTOM "What Models Cannot Handle":
- Inversion disrupting TAD boundary
- Copy number change duplicating enhancer
- Translocation fusing regulatory domains
- Large X marks

Title: "Structural Variants Beyond Model Capacity"
Annotation: "Most pathogenic SVs unmodeled"

Clean structural variant diagram, white background. Professional SV limitation figure.
```

**Caption for Panel D:**
"Structural variants beyond current model capacity. Models designed for substitutions and small indels cannot process structural variants (inversions, CNVs, translocations) that disrupt regulatory topology. These SVs represent a significant fraction of pathogenic regulatory variation, constituting a major gap in current prediction capability."

### Combined Caption

**Full Figure Caption:**
"Fundamental limitations of regulatory sequence models. (A) Reference haplotype assumption: models analyze single variants on reference backgrounds, ignoring haplotype context and variant interactions. (B) Training cell type bias: immortalized cell lines dominate training data; disease-relevant primary tissues are underrepresented. (C) Correlation vs. causation: predicted expression changes do not establish causal mechanism. (D) Structural variant blindness: inversions, CNVs, and translocations cannot be processed by current architectures. These limitations constrain clinical utility and must be addressed through experimental validation."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 16.1 Long-Range Regulation | 4 | Essential | Medium (biological motivation) |
| 16.2 Enformer Architecture | 1 | Essential | High (detailed architecture) |
| 16.3 VEP Workflow | 1 | High | Medium (pipeline) |
| 16.4 Borzoi RNA-seq | 4 | High | Medium (application) |
| 16.5 Limitations | 4 | High | Medium (analysis) |

**Total files:** 14
**Recommended generation order:** 16.2 (Enformer architecture), 16.1A-D (biological motivation), 16.3 (workflow), 16.4A-D (Borzoi), 16.5A-D (limitations)

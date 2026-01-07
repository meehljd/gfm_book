# Figure Report: Chapter 5 - Tokens and Embeddings

**Chapter:** Part 2, Chapter 5 - Tokens and Embeddings
**Date:** 2026-01-07
**Figures:** 4 conceptual figures (9 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 5.1: Tokenization Comparison (Four-Panel)

**Files:**
- `figs/part_2/ch05/01-A-fig-ch05-tokenization-comparison.svg`
- `figs/part_2/ch05/01-B-fig-ch05-tokenization-comparison.svg`
- `figs/part_2/ch05/01-C-fig-ch05-tokenization-comparison.svg`
- `figs/part_2/ch05/01-D-fig-ch05-tokenization-comparison.svg`

**Priority:** Essential
**Type:** Multi-panel comparative diagram

### Panel A: One-Hot Encoding

**Content:** Show a ~30-nucleotide regulatory sequence as a 4×30 binary matrix with color-coded nucleotides (A=green, T=red, G=yellow, C=blue). Each column has exactly one "1" value. Annotate: "30 tokens, 1 per nucleotide, no compression."

**DALL-E Prompt:**
```
Scientific diagram showing one-hot encoding of DNA sequence. A horizontal matrix visualization with 4 rows (labeled A, C, G, T) and approximately 30 columns. Each column has one filled cell (colored block) and three empty cells, creating a sparse binary pattern. Colors: A=green, C=blue, G=yellow, T=red. Clean bioinformatics visualization style. White background with thin grid lines. Professional machine learning diagram suitable for academic textbook.
```

**Caption for Panel A:**
"One-hot encoding preserves single-nucleotide resolution. Each nucleotide becomes a 4-dimensional binary vector with a single active element. A 30-bp sequence produces 30 tokens with no compression, maintaining maximum resolution for variant-level analysis."

### Panel B: Overlapping 6-mers

**Content:** Same sequence showing overlapping 6-mer tokens. Use brackets to show how adjacent tokens share 5 nucleotides. Annotate: "~30 tokens due to overlap, 4,096 vocabulary size."

**DALL-E Prompt:**
```
Scientific diagram showing overlapping k-mer tokenization of DNA. Horizontal DNA sequence with colored nucleotide letters. Multiple overlapping brackets below the sequence, each spanning 6 nucleotides, with each bracket shifted by 1 position from the previous. Brackets overlap heavily, sharing 5 of 6 positions. Clean bioinformatics visualization with white background. Professional tokenization diagram for machine learning textbook.
```

**Caption for Panel B:**
"Overlapping k-mer tokenization (DNABERT style) groups 6 consecutive nucleotides as tokens. Adjacent tokens share 5 nucleotides, providing no sequence compression despite larger vocabulary. A single-nucleotide variant affects 6 different tokens, complicating variant interpretation."

### Panel C: BPE Tokenization

**Content:** Same sequence with variable-length non-overlapping BPE tokens. Mark token boundaries showing compression of repetitive regions into single tokens while unique regions have shorter tokens. Annotate: "~10-15 tokens, variable compression."

**DALL-E Prompt:**
```
Scientific diagram showing byte-pair encoding tokenization of DNA sequence. Horizontal DNA sequence with colored nucleotides grouped into variable-length segments. Some segments are long (6-10 nucleotides) for common patterns, others are short (1-3 nucleotides) for unique regions. Token boundaries marked with vertical lines. Segments do not overlap. Clean bioinformatics visualization style. White background. Professional NLP/genomics hybrid diagram.
```

**Caption for Panel C:**
"Byte-pair encoding (BPE) learns variable-length tokens from corpus statistics. Frequent patterns (repetitive elements, common motifs) merge into longer tokens, achieving 2-5x compression. Rare sequences decompose into shorter units. Token boundaries depend on context, affecting variant localization."

### Panel D: Single-Nucleotide (Hyena/Mamba)

**Content:** Same sequence with single-nucleotide tokens but with learned embedding vectors indicated for each position. Show the 4-token vocabulary with embedding arrows. Annotate: "30 tokens, 4-5 vocabulary, learned embeddings."

**DALL-E Prompt:**
```
Scientific diagram showing single-nucleotide tokenization with learned embeddings. Horizontal DNA sequence with individual nucleotide letters. Below each nucleotide, a small arrow pointing to an embedding vector (shown as a colored bar or small matrix column). A small legend shows the 4-nucleotide vocabulary (A, C, G, T) each mapping to an embedding. Clean minimalist bioinformatics style. White background. Professional deep learning architecture diagram.
```

**Caption for Panel D:**
"Single-nucleotide tokenization (HyenaDNA, Caduceus) maintains maximum resolution with minimal vocabulary. Learned embeddings transform discrete nucleotides into continuous representations. Sub-quadratic architectures make million-base contexts feasible without sacrificing single-nucleotide precision for variant interpretation."

### Combined Caption

**Full Figure Caption:**
"Tokenization strategies for genomic sequences. (A) One-hot encoding produces one token per nucleotide as a sparse 4-dimensional binary vector, preserving maximum resolution. (B) Overlapping 6-mer tokenization groups nucleotides into 4,096 possible tokens but provides no compression since each nucleotide generates its own token. (C) Byte-pair encoding creates variable-length non-overlapping tokens learned from corpus statistics, achieving genuine compression of repetitive regions. (D) Single-nucleotide tokenization with learned embeddings combines maximum resolution with rich representations, enabled by sub-quadratic architectures that circumvent attention's quadratic scaling. Each strategy encodes different assumptions about which patterns matter for downstream prediction."

---

## Figure 5.2: Biologically-Informed Tokenization

**File:** `figs/part_2/ch05/02-fig-ch05-biological-tokenization.svg`
**Priority:** Enhancing
**Type:** Comparative gene structure diagram

### Content Description

Side-by-side comparison on a gene structure diagram showing:
1. **Standard BPE**: Token boundaries crossing codon boundaries arbitrarily in coding regions
2. **Codon-aware tokenization**: Reading frame respected with 64-codon vocabulary in coding regions
3. **BioToken-style**: Explicit variant tokens, regulatory element markers, and structural annotations integrated

Show exons as boxes, introns as thin lines. Highlight how biological structure can be encoded directly.

### DALL-E Prompt

```
Scientific comparison diagram showing three tokenization approaches on a gene structure. Top row shows gene schematic with exons (boxes) and introns (thin lines). Three horizontal panels below: Panel 1 shows arbitrary token boundaries crossing codon triplets. Panel 2 shows token boundaries aligned with codon triplets in exons, respecting reading frame. Panel 3 shows tokens with special symbols for variants (diamond), regulatory elements (star), and structural features (circle). Clean molecular biology illustration style. White background. Professional genomics/ML hybrid diagram.
```

### Post-Processing Notes

- Add clear labels for each tokenization approach
- Annotate codon boundaries in the coding regions
- Use color coding to distinguish exons from introns
- Add legend explaining special token types in BioToken panel

### Fallback Description

Create in diagramming software (BioRender, Inkscape):
- Gene structure schematic with exon boxes and intron lines
- Three rows showing different tokenization approaches
- Use color and symbols to distinguish token types

### Caption

**Recommended Caption:**
"Biologically-informed tokenization strategies. Standard BPE (top) tokenizes across codon boundaries in coding regions, potentially obscuring the fundamental three-nucleotide unit of protein translation. Codon-aware tokenization (middle, as in GenSLMs and Life-Code) respects reading frame, with each codon becoming a single token from a 64-element vocabulary. This alignment with biological structure enables learning synonymous versus nonsynonymous substitution patterns directly. BioToken-style tokenization (bottom) extends further by incorporating explicit variant tokens, regulatory element markers, and structural annotations, treating tokens as rich entities bundling sequence with functional context."

---

## Figure 5.3: Embedding Space Visualization (Three-Panel)

**Files:**
- `figs/part_2/ch05/03-A-fig-ch05-embedding-space.svg`
- `figs/part_2/ch05/03-B-fig-ch05-embedding-space.svg`
- `figs/part_2/ch05/03-C-fig-ch05-embedding-space.svg`

**Priority:** High
**Type:** UMAP/t-SNE dimensionality reduction plots

### Panel A: GC Content

**Content:** UMAP or t-SNE visualization of k-mer or BPE token embeddings from a trained DNA language model. Points colored by GC content on a gradient from AT-rich (red/orange) to GC-rich (blue/purple). Should show clear clustering/gradients by GC content.

**DALL-E Prompt:**
```
Scientific UMAP dimensionality reduction plot showing DNA token embeddings. Scattered points forming organic cluster shapes. Color gradient from warm red/orange (AT-rich) on one side to cool blue/purple (GC-rich) on the other side. Smooth color transition across the embedding space. Clean data visualization style with white background and minimal axis lines. Professional bioinformatics embedding visualization. No text labels on points.
```

**Caption for Panel A:**
"Token embeddings organized by GC content. UMAP visualization of learned embeddings from a DNA language model reveals that GC content emerges as a major axis of organization, with AT-rich tokens (red/orange) segregating from GC-rich tokens (blue/purple). This structure emerges without explicit GC supervision, reflecting the many functional properties that correlate with base composition."

### Panel B: Token Frequency

**Content:** Same embedding space colored by token frequency (common vs. rare). Common tokens cluster together, rare tokens appear in different regions.

**DALL-E Prompt:**
```
Scientific UMAP plot showing DNA token embeddings colored by frequency. Scattered points forming cluster shapes. Color gradient from dark blue (very common tokens, densely clustered) to light yellow/white (rare tokens, more scattered). Some distinct regions have predominantly dark or light coloring. Clean data visualization style with white background. Professional machine learning embedding visualization.
```

**Caption for Panel B:**
"Token embeddings organized by corpus frequency. Common tokens (dark blue) cluster distinctly from rare tokens (light yellow), reflecting that frequently co-occurring sequences develop similar representations. This organization enables the model to treat rare sequences as compositions of common subunits while dedicating representation capacity to frequent patterns."

### Panel C: Genomic Context

**Content:** Same embedding space colored by genomic context: coding (blue), regulatory (green), repetitive (gray). Shows distinct clustering by functional category.

**DALL-E Prompt:**
```
Scientific UMAP plot showing DNA token embeddings colored by genomic context. Scattered points in distinct cluster regions. Three main colors: blue for coding regions (forming one cluster area), green for regulatory regions (different area), gray for repetitive elements (third area). Some mixing at boundaries. Clean data visualization with white background. Professional genomics bioinformatics visualization.
```

**Caption for Panel C:**
"Token embeddings organized by genomic context. Despite no explicit context labels during pretraining, coding tokens (blue), regulatory tokens (green), and repetitive elements (gray) occupy distinct regions of embedding space. This emergent organization reflects learned patterns that distinguish sequence function without supervision."

### Combined Caption

**Full Figure Caption:**
"Emergent structure in learned DNA token embeddings. UMAP projections of token embeddings from a trained DNA language model reveal biologically meaningful organization that emerges without explicit supervision. (A) GC content creates a major gradient, with AT-rich and GC-rich tokens segregating. (B) Token frequency organizes embeddings, with common tokens clustering distinctly from rare tokens. (C) Genomic context (coding, regulatory, repetitive) corresponds to distinct embedding regions. This organization demonstrates that pretraining on sequence prediction objectives induces representations capturing genuine biological structure."

---

## Figure 5.4: Compression vs. Resolution Tradeoff

**File:** `figs/part_2/ch05/04-fig-ch05-compression-resolution.svg`
**Priority:** High
**Type:** Two-axis plot / strategic positioning diagram

### Content Description

Two-axis plot with:
- **X-axis:** Sequence compression (tokens per kilobase, from ~1000 to ~200)
- **Y-axis:** Nucleotide resolution (from low to high)

Position different approaches as labeled points:
- One-hot/single-nucleotide: Top-left (no compression, full resolution)
- Overlapping k-mers: Top-left (no compression, k-nucleotide resolution)
- Non-overlapping k-mers: Middle (k-fold compression, k-nucleotide resolution)
- BPE: Middle-right (variable compression, variable resolution)

Annotate practical context lengths achievable with standard transformers (~4K tokens).

Include callout showing clinical implication: "Single SNP affects..." with number of tokens per approach.

### DALL-E Prompt

```
Scientific two-axis plot comparing tokenization strategies. X-axis labeled "Sequence Compression" from low to high. Y-axis labeled "Nucleotide Resolution" from low to high. Four or five labeled points positioned in different quadrants representing different tokenization methods. Diagonal dashed line showing tradeoff. Annotation boxes with practical implications. Clean strategic positioning diagram style with white background, grid lines. Professional machine learning architecture comparison diagram.
```

### Post-Processing Notes

- Add method labels (One-hot, k-mers, BPE, Single-nucleotide)
- Add annotation for context length with standard 4K token transformers
- Add clinical callout showing SNP token impact
- Use consistent colors matching earlier figures

### Fallback Description

Create in matplotlib or diagramming software:
- Scatter plot with strategic positioning
- Add labeled points for each tokenization strategy
- Include annotation boxes for practical implications

### Caption

**Recommended Caption:**
"The compression-resolution tradeoff in genomic tokenization. This plot positions tokenization strategies along two axes: sequence compression (tokens per kilobase) and nucleotide resolution. One-hot and single-nucleotide tokenization occupy the upper-left corner, providing maximum resolution with no compression. Overlapping k-mers also provide no compression but reduce resolution to k-nucleotide granularity. Non-overlapping k-mers and BPE occupy the middle ground, trading resolution for compression that enables longer context windows with standard transformer architectures. The clinical implication appears in variant interpretation: a single-nucleotide polymorphism affects 1 token with single-nucleotide tokenization but k tokens with overlapping k-mers, complicating effect attribution. Sub-quadratic architectures (HyenaDNA, Caduceus) escape this tradeoff entirely, enabling full resolution at any context length."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 5.1 Tokenization Comparison | 4 | Essential | Medium (multi-panel) |
| 5.2 Biological Tokenization | 1 | Enhancing | Medium (gene diagram) |
| 5.3 Embedding Space | 3 | High | Medium (UMAP plots) |
| 5.4 Compression-Resolution | 1 | High | Low-Medium (positioning) |

**Total files:** 9
**Recommended generation order:** 5.4 (strategic diagram), 5.3A-C (UMAP plots), 5.1A-D (comparison panels), 5.2 (gene diagram)

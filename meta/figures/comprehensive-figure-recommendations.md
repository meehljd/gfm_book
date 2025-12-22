# Comprehensive Figure Recommendations for *Genomic Foundation Models*

This document consolidates all figure recommendations across all six parts of the textbook, sorted by chapter and location within each chapter, with renumbered figures.

## Priority Key

- **Essential**: The chapter feels incomplete without this figure. Readers will reference it repeatedly.
- **High**: Significantly aids comprehension of a core concept. Strong candidate for inclusion.
- **Enhancing**: Helpful but not critical. Include if time permits; cut first under pressure.

---

# Part I: Foundations (Chapters 1–4)

## Chapter 1: From Reads to Variants {#sec-ngs}

### Figure 1.1: The Variant Calling Pipeline
Location: Line 59, after section "Classical Variant Calling Pipelines"

::: {#fig-variant-calling-pipeline}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] End-to-end schematic showing the journey from DNA sample to VCF file. Major stages: (1) DNA fragmentation and library preparation, (2) sequencing (distinguish short-read Illumina vs long-read PacBio/ONT icons), (3) base calling producing FASTQ, (4) read alignment to reference (show reads stacking against genome), (5) post-alignment processing (duplicate marking, BQSR), (6) per-sample variant calling producing gVCF, (7) joint genotyping across cohort, (8) variant filtering producing final VCF. Annotate data formats at each arrow (FASTQ, BAM/CRAM, gVCF, VCF). Include approximate file sizes for a 30× WGS to ground scale.
:::

---

### Figure 1.2: Phasing and Compound Heterozygosity
Location: Line 114, after section "Haplotype Phasing" opening clinical scenario

::: {#fig-phasing-compound-het}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel figure illustrating the clinical importance of phase information. Panel A: Maternal and paternal chromosomes carrying the *CFTR* gene, with two pathogenic variant positions marked. Panel B (*cis* configuration): Both variants on maternal chromosome; paternal copy functional; child is carrier (unaffected). Panel C (*trans* configuration): One variant on each chromosome; no functional copy; child has cystic fibrosis. Include VCF notation showing how unphased (0/1) vs phased (0|1, 1|0) genotypes encode this information.
:::

---

### Figure 1.3: Sources of Variant Calling Error
Location: Line 152, at section "Sources of Error and Uncertainty"

::: {#fig-error-sources}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Taxonomy diagram organizing error sources hierarchically. Three major branches: (1) Sequencing artifacts (subdivide: homopolymer errors, PCR duplicates, index hopping, strand bias, quality score miscalibration); (2) Alignment artifacts (subdivide: mapping ambiguity in repeats, reference bias favoring ref allele, misalignment in segmental duplications); (3) Biological complexity (subdivide: somatic mosaicism, low allele fraction, complex variants like MNVs). For each leaf, include 1-sentence description and indicate whether it creates false positives, false negatives, or both.
:::

---

### Figure 1.4: Difficult Regions of the Human Genome
Location: Line 180, at section "Difficult Regions: The Limits of Short-Read Calling"

::: {#fig-difficult-regions}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Ideogram-style genome overview highlighting regions where short-read variant calling systematically fails. Mark: (1) Segmental duplications (show *CYP2D6* region on chr22 as exemplar); (2) HLA complex on chr6p21 (shade entire region); (3) Centromeric and pericentromeric regions; (4) Subtelomeric regions; (5) Example tandem repeat loci (e.g., *HTT*, *FMR1*). Inset panel shows approximate percentage of genome in each difficulty class. Second inset shows how long reads resolve a region invisible to short reads.
:::

---

### Figure 1.5: DeepVariant Pileup Image Representation
Location: Line 240, at section "DeepVariant: Variant Calling as Image Classification," subsection "Pileup Images as Input"

::: {#fig-deepvariant-pileup}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Annotated example of a DeepVariant-style pileup tensor. Show a candidate variant site (e.g., a heterozygous SNV) with approximately 30 reads stacked vertically. Label the multiple channels: (1) read bases with matches in gray, mismatches in color-coded nucleotides; (2) base quality as intensity gradient; (3) mapping quality as separate channel; (4) strand orientation (forward/reverse); (5) reference sequence overlay at top. Include the candidate alleles. Show corresponding genotype posterior output (e.g., P(0/0)=0.02, P(0/1)=0.96, P(1/1)=0.02).
:::

---

## Chapter 2: The Data Landscape {#sec-data}

### Figure 2.1: The Genomic Data Ecosystem
Location: Line 5, chapter opening after introductory paragraphs

::: {#fig-data-ecosystem}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Conceptual map showing how major data resources interconnect and flow into downstream applications. Organize into layers: (1) Foundation layer: Reference genomes (GRCh38, T2T-CHM13) and gene annotations (GENCODE, RefSeq, MANE); (2) Population layer: Variant catalogs (gnomAD, 1000 Genomes) and biobanks (UK Biobank, All of Us); (3) Functional layer: ENCODE, Roadmap Epigenomics, Cistrome, GTEx; (4) Clinical layer: ClinVar, ClinGen, OMIM, PharmGKB. Draw arrows showing dependencies. Indicate which resources provide "coordinates," "frequencies," "functions," or "labels."
:::

---

### Figure 2.2: Ancestry Representation in Major Genomic Resources
Location: Line 58, at section "Population Variant Catalogs and Allele Frequencies"

::: {#fig-ancestry-representation}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Stacked bar chart or waffle plot showing ancestry composition across key resources: gnomAD v4, UK Biobank, ClinVar submissions, GTEx donors, GWAS Catalog participants. Highlight the persistent European overrepresentation (approximately 78% of GWAS participants as of 2019) against global population proportions. Include a small world map inset showing which continental ancestries are represented vs underrepresented.
:::

---

### Figure 2.3: Functional Genomics Data Matrix
Location: Line 94, at section "ENCODE, Roadmap, and Related Consortia"

::: {#fig-functional-genomics-matrix}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Heatmap-style visualization showing the ENCODE/Roadmap data compendium structure. Rows represent cell types or tissues (group by category: cell lines, primary cells, tissues). Columns represent assay types (ChIP-seq for various TFs and histone marks, DNase-seq, ATAC-seq, RNA-seq). Color intensity indicates data availability (present/absent or coverage depth). Highlight which cell types have comprehensive coverage vs sparse coverage. Annotate example cell types that are well-profiled (K562, GM12878, HepG2) vs disease-relevant tissues that remain undersampled.
:::

---

### Figure 2.4: ClinVar Classification Landscape
Location: Line 156, at section "ClinVar and Clinical Assertions"

::: {#fig-clinvar-landscape layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel figure. Panel A: Pie or bar chart showing distribution of ClinVar classifications (Pathogenic, Likely Pathogenic, VUS, Likely Benign, Benign, Conflicting). Highlight that VUS dominates. Panel B: Heatmap showing classification density by gene, with well-studied genes (BRCA1, BRCA2, CFTR) having many submissions vs sparse coverage elsewhere. Panel C: Timeline showing how classifications evolve (example of a variant reclassified from VUS to Pathogenic over time, illustrating version sensitivity).
:::

---

## Chapter 3: GWAS and Polygenic Scores {#sec-gwas}

### Figure 3.1: Anatomy of a Manhattan Plot
Location: Line 47, at section "Visualizing Genome-Wide Results"

::: {#fig-manhattan-anatomy}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Annotated Manhattan plot from a real or realistic GWAS (e.g., height or CAD). Key annotations: (1) Genome-wide significance threshold at −log₁₀(5×10⁻⁸) ≈ 7.3; (2) Example peak with lead SNP labeled; (3) Width of peak showing LD extent (many correlated variants, not just one); (4) Chromosomes color-alternated along x-axis; (5) Inset zoom on one peak showing how multiple variants exceed threshold—illustrating that GWAS identifies loci, not causal variants. Include Q-Q plot inset showing expected vs observed p-value distribution with genomic inflation factor λ annotated.
:::

---

### Figure 3.2: The Heritability Decomposition
Location: Line 63, at section "Heritability: What Genetics Can Explain"

::: {#fig-heritability-decomposition}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Conceptual diagram showing nested components of phenotypic variance. Outer ring: Total phenotypic variance (100%). First partition: Genetic vs Environmental components (e.g., 80/20 for height). Within genetic: Additive (narrow-sense h²) vs non-additive (dominance, epistasis). Within additive: SNP-heritability (what GWAS can capture) vs "missing heritability" (rare variants, structural variants, imperfect tagging). Annotate with approximate values for a well-studied trait like height.
:::

---

### Figure 3.3: Linkage Disequilibrium and the Tag-Causal Distinction
Location: Line 95, at section "Linkage Disequilibrium and Correlation Structure"

::: {#fig-ld-tag-causal layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Three-panel figure. Panel A: Haplotype diagram showing how LD creates correlation between variants on the same chromosome segment; show example haplotypes with causal variant (star) and tag variants traveling together. Panel B: r² matrix (triangular heatmap) for a genomic region showing block structure of LD. Panel C: Same causal variant shown in two populations with different LD structure—in one population, tags are highly correlated with causal variant; in another, the correlation is weaker, illustrating why portability fails.
:::

---

### Figure 3.4: Polygenic Score Construction Methods
Location: Line 145, at section "Polygenic Score Construction"

::: {#fig-pgs-construction layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[High] Side-by-side comparison of C+T vs LD-aware Bayesian methods. Left panel (C+T): Start with GWAS summary statistics → apply p-value threshold → clump by LD → retain independent lead SNPs → weight by effect size. Show visually how most variants are discarded. Right panel (LDpred/PRS-CS): Same summary statistics → model LD structure jointly → shrink effects toward zero based on prior → retain all variants with modulated weights. Highlight that C+T discards information while Bayesian methods model it.
:::

---

### Figure 3.5: Cross-Ancestry Portability of Polygenic Scores
Location: Line 218, at section "Ancestry, Portability, and Fairness"

::: {#fig-pgs-portability}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Bar chart showing relative prediction accuracy (R² or AUC ratio) of European-derived PGS when applied to different ancestry groups. European as reference (100%), then decreasing accuracy for East Asian, South Asian, Hispanic/Latino, and African-ancestry populations (often 25-60% of European performance). Include error bars. Overlay or annotate factors contributing to the gap: LD differences, allele frequency differences, potential effect heterogeneity, training sample size disparities.
:::

---

## Chapter 4: Classical Variant Prediction {#sec-vep-classical}

### Figure 4.1: The Variant Prioritization Funnel
Location: Line 10, chapter opening (existing TODO location)

::: {#fig-variant-funnel}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Funnel diagram showing progressive reduction of variant burden through computational filters. Stages with approximate numbers: (1) Raw variants from WGS: ~4-5 million; (2) After common variant filter (gnomAD AF > 1%): ~100,000; (3) After consequence filter (coding, splice, UTR): ~25,000; (4) After conservation filter (phyloP > 2): ~5,000; (5) After ensemble predictor (CADD ≥ 20): ~500-1,000; (6) Expert review candidates: ~50-100. Annotate which tools/resources apply at each stage.
:::

---

### Figure 4.2: Conservation Score Interpretation
Location: Line 14, at section "Conservation-Based Approaches"

::: {#fig-conservation-scores layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Multi-panel figure. Panel A: Multiple sequence alignment at a highly conserved position (same nucleotide across 30+ species) vs a neutrally evolving position (variable nucleotides). Show phylogenetic tree alongside alignment. Panel B: Distribution of phyloP or GERP scores genome-wide, with long right tail representing constrained elements. Mark threshold zones (e.g., phyloP > 2 = strong evidence). Panel C: Example intronic variant at deeply conserved position with no other annotation—illustrating how conservation provides evidence in annotation-sparse regions.
:::

---

### Figure 4.3: CADD's Evolutionary Proxy Training Strategy
Location: Line 105, at section "CADD: Combined Annotation Dependent Depletion," subsection on training data construction

::: {#fig-cadd-training layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Three-panel conceptual figure. Panel A (Proxy-Neutral): Human-derived alleles fixed since human-chimpanzee split; these variants survived selection, representing tolerated changes. Show evolutionary tree with human branch highlighted. Panel B (Proxy-Deleterious): Simulated variants matching human mutational processes (trinucleotide context); these represent possible-but-not-observed mutations enriched for deleterious effects. Show simulation schematic with mutation spectrum. Panel C (Classification): SVM learning to distinguish classes based on annotation features; output is "evolutionary tolerance" score, not pathogenicity directly.
:::

---

### Figure 4.4: Ensemble Method Performance Comparison
Location: Line 177, at section "Other Ensemble Methods," subsection "Comparison and Selection"

::: {#fig-ensemble-performance}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] ROC curves (or precision-recall curves) comparing CADD, REVEL, and M-CAP on a held-out benchmark of missense variants. Include curves for individual component scores (SIFT, PolyPhen-2, phyloP) to show improvement from integration. Mark operating points corresponding to common clinical thresholds (CADD ≥ 20, REVEL ≥ 0.75, M-CAP "possibly pathogenic"). Annotate sensitivity and specificity at each threshold. Include note about benchmark circularity caveats.
:::

---

### Figure 4.5: The Circularity Problem in Variant Prediction
Location: Line 184, at section "Circularity and Ascertainment Bias"

::: {#fig-circularity-problem}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Circular diagram illustrating the feedback loop between computational predictors and clinical databases. Show cycle: (1) Computational score (e.g., high CADD) influences clinical classification; (2) Classified variant enters ClinVar as "Pathogenic"; (3) Benchmarking study evaluates CADD on ClinVar variants; (4) High benchmark performance encourages clinical adoption; (5) Return to step 1. Indicate intervention points: temporal holdouts, functional assay ground truth, prospective evaluation. Use visual metaphor of self-reinforcing spiral.
:::

---

# Part II: Sequence Architectures (Chapters 5–9)

## Chapter 5: Tokens and Embeddings {#sec-representations}

### Figure 5.1: Tokenization Strategy Comparison
Location: Line 7-8, early in chapter after introducing the tokenization problem

::: {#fig-tokenization-comparison layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Four-panel comparison showing the same 30-nucleotide regulatory sequence tokenized four different ways. Panel A (One-hot): 30 tokens, one per nucleotide, shown as 4×30 binary matrix with color-coded nucleotides. Panel B (Overlapping 6-mers): Still ~30 tokens due to overlap, with brackets showing how tokens share nucleotides. Panel C (BPE): ~10-15 variable-length tokens, with token boundaries marked showing compression of repetitive regions. Panel D (Single-nucleotide for Hyena/Mamba): 30 tokens like one-hot but with learned embeddings indicated. Annotate sequence length, token count, and effective compression ratio for each.
:::

---

### Figure 5.2: Biologically-Informed Tokenization
Location: Line 63, at section "Biologically-Informed Tokenization"

::: {#fig-biological-tokenization}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Comparison of standard vs. biologically-informed tokenization on a gene structure diagram. Show: (1) Standard BPE tokenizing across codon boundaries in coding regions; (2) Codon-aware tokenization (GenSLMs/Life-Code) respecting reading frame with 64-codon vocabulary; (3) BioToken-style representation with explicit variant tokens, regulatory element markers, and structural annotations. Highlight how biological structure can be encoded directly into tokenization.
:::

---

### Figure 5.3: From Tokens to Embeddings: Learned Embedding Space Organization
Location: Line 77, at section "From Tokens to Embeddings: Learning Representations"

::: {#fig-embedding-space layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] UMAP or t-SNE visualization of k-mer or BPE token embeddings from a trained DNA language model (e.g., DNABERT-2 or GROVER). Color points by: Panel A: GC content (gradient from AT-rich to GC-rich). Panel B: Token frequency (common vs. rare). Panel C: Genomic context (coding, regulatory, repetitive). Show how biologically meaningful structure emerges without explicit supervision.
:::

---

### Figure 5.4: Position Encoding Schemes
Location: Line 103, at section "Position Encodings: Where Tokens Live"

::: {#fig-position-encodings layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Four-panel comparison of position encoding approaches. Panel A (Absolute/Learned): Heatmap showing learned position embeddings across dimensions, with note about fixed maximum length. Panel B (Sinusoidal): Wave patterns at different frequencies across positions, showing how different dimensions capture different scales. Panel C (ALiBi): Attention bias matrix showing linear decay with distance, highlighting the implicit local preference. Panel D (RoPE): 2D rotation visualization in embedding subspace showing how relative position is encoded through rotation angle.
:::

---

### Figure 5.5: The Compression-Resolution Tradeoff
Location: Line 165, at section "The Compression-Resolution Trade-off"

::: {#fig-compression-resolution}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Two-axis plot with "Sequence Compression" on x-axis (tokens per kilobase) and "Nucleotide Resolution" on y-axis. Position different approaches: One-hot/single-nucleotide (no compression, full resolution), overlapping k-mers (no compression, k-nucleotide resolution), non-overlapping k-mers (k-fold compression, k-nucleotide resolution), BPE (variable compression, variable resolution). Annotate practical context lengths achievable with standard transformers (~4K tokens) for each approach. Include callout showing clinical implication: "Single SNP affects..." with number of tokens per approach.
:::

---

## Chapter 6: Convolutional Networks {#sec-cnn}

### Figure 6.1: Convolution as Sequence Pattern Detector
Location: Line 9, at section "Convolutions as Sequence Pattern Detectors"

::: {#fig-conv-pattern-detector layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Three-panel figure showing convolution mechanics. Panel A: Single convolutional filter (width 8) sliding across one-hot encoded DNA, producing activation scores at each position; show high activation where filter matches a motif. Panel B: Learned filter weights visualized as sequence logo (PWM-style), aligned to corresponding JASPAR motif showing the biological pattern discovered. Panel C: Multiple filters from first convolutional layer, each detecting different motifs (CTCF, ETS, AP-1), showing diverse pattern detection.
:::

---

### Figure 6.2: DeepSEA Architecture and Validation
Location: Line 31, at section "DeepSEA: Regulatory Prediction from Sequence"

::: {#fig-deepsea-architecture layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel figure. Panel A: Architecture schematic showing input (1000bp one-hot), three convolutional layers with pooling (320→480→960 filters), fully connected layer, and 919 sigmoid outputs for chromatin features. Panel B: First-layer filter aligned to JASPAR motif (e.g., CTCF), demonstrating learned = known biology. Panel C: Scatter plot of predicted vs. observed allelic imbalance for DNase-seq, showing correlation that validates variant effect prediction.
:::

---

### Figure 6.3: ExPecto Modular Pipeline
Location: Line 93, at section "ExPecto: From Chromatin to Expression"

::: {#fig-expecto-pipeline}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Three-component pipeline diagram. Component 1: Beluga CNN scanning 40kb window around TSS with sliding 2kb windows, producing chromatin predictions at 200 spatial positions. Component 2: Spatial transformation with exponential decay functions (upstream and downstream), reducing to ~20,000 features. Component 3: 218 tissue-specific linear regression models, producing per-tissue expression predictions. Show example delta scores for variant effect.
:::

---

### Figure 6.4: SpliceAI Architecture and Dilated Convolutions
Location: Line 142, at section "SpliceAI: Clinical-Grade Splicing Prediction," subsection "Architecture: Depth and Dilation"

::: {#fig-spliceai-architecture layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[High] Two-panel figure. Panel A: Diagram showing how dilated convolutions expand receptive field without proportional parameter growth. Show dilation rates (1, 2, 4, 8, 16...) with gaps between filter taps, illustrating how 32 layers with dilation reach 10kb context. Panel B: SpliceAI's residual block structure with skip connections from every 4th block to output, enabling gradient flow through 32 layers.
:::

---

### Figure 6.5: The Receptive Field Ceiling
Location: Line 195, at section "The Receptive Field Ceiling"

::: {#fig-receptive-field-ceiling}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Horizontal genome diagram comparing effective context windows across CNN architectures. Show: DeepSEA (~1 kb), ExPecto/Beluga (2 kb windows, 40 kb aggregated), SpliceAI (10 kb), and for contrast, Enformer (200 kb). Overlay biologically relevant distances: typical TF binding site (~10bp), promoter region (~1kb), enhancer-gene distance (10-100kb), TAD size (~1Mb). Highlight the gap: "Most enhancer-promoter interactions exceed CNN receptive fields."
:::

---

## Chapter 7: Transformers and Attention {#sec-attention}

### Figure 7.1: The Self-Attention Mechanism
Location: Line 28, at section "The Self-Attention Mechanism"

::: {#fig-self-attention}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Step-by-step visualization of self-attention on a short regulatory sequence. Panel A: Input embeddings for ~10 positions. Panel B: Query, Key, Value projections (show W^Q, W^K, W^V matrices). Panel C: Attention score matrix (query-key dot products, pre-softmax). Panel D: Attention weight matrix (post-softmax, showing which positions attend to which). Panel E: Weighted sum of values producing output. Annotate the key equation at each step.
:::

---

### Figure 7.2: Multi-Head Attention Enables Diverse Interaction Types
Location: Line 60, at section on Multi-Head Attention

::: {#fig-multihead-attention}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Panel showing 4-6 attention heads from a trained genomic transformer, each displaying different learned patterns. Head 1: Local attention (attending to nearby positions). Head 2: Periodic attention (nucleosome spacing ~200bp). Head 3: Motif-specific attention (attending to CTCF sites). Head 4: Long-range attention (enhancer-promoter). Annotate the biological interpretation of each pattern.
:::

---

### Figure 7.3: Attention Patterns Reveal Learned Regulatory Logic
Location: Line 66, after introducing multi-head attention

::: {#fig-attention-patterns layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Heatmap visualization of attention weights from a trained genomic transformer (e.g., Enformer). Panel A: Attention pattern showing strong weights between a promoter region and a distal enhancer ~50kb away, demonstrating learned enhancer-promoter relationships. Panel B: Same attention overlaid on linear genome diagram showing the biological interpretation. Panel C: Different attention head showing local patterns (attending to nearby positions), demonstrating head specialization.
:::

---

### Figure 7.4: Transformer Block Architecture
Location: Line 114, at section "The Transformer Block"

::: {#fig-transformer-block}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Detailed diagram of a single transformer block with pre-norm configuration. Show: Input → Layer Norm → Multi-Head Attention → Residual Add → Layer Norm → Feed-Forward Network (expand 4x, GELU, project back) → Residual Add → Output. Annotate dimension changes. Include small inset showing 2-3 stacked blocks to illustrate depth.
:::

---

### Figure 7.5: Encoder, Decoder, and Hybrid Architectures
Location: Line 180-210, at section discussing architecture variants

::: {#fig-encoder-decoder layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Enhancing] Three-panel comparison. Panel A (Encoder-only, e.g., BERT/DNABERT): Bidirectional attention pattern (full matrix), typical use for classification/embedding. Panel B (Decoder-only, e.g., GPT/Evo): Causal attention pattern (lower triangular), typical use for generation. Panel C (Hybrid CNN-Transformer, e.g., Enformer): CNN downsampling followed by transformer, showing how hybrid reduces sequence length before attention.
:::

---

### Figure 7.6: The Quadratic Complexity Ceiling
Location: Line 246, at section "Limitations and Emerging Alternatives"

::: {#fig-quadratic-ceiling}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Log-log plot showing computational cost (FLOPs or memory) vs. sequence length for different architectures. Show: Standard attention (quadratic curve, O(L²)), sparse/local attention (sub-quadratic), state space models like Hyena/Mamba (linear). Annotate biologically relevant context lengths: promoter (~1kb), gene (~10kb), enhancer-promoter (~100kb), TAD (~1Mb), chromosome arm (~100Mb). Draw vertical lines at each scale showing which architectures are tractable.
:::

---

## Chapter 8: Pretraining Strategies {#sec-pretraining}

### Figure 8.1: Pretraining Objective Comparison
Location: Line 7, chapter opening or early section

::: {#fig-pretraining-objectives layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Three-panel schematic comparing major pretraining objectives on the same input sequence. Panel A (MLM): Sequence with masked positions (shown as [MASK]), bidirectional context arrows from both sides, prediction targets at masked positions. Panel B (Next-token prediction): Causal/unidirectional arrows, each position predicting the next, with sampling process for generation. Panel C (Contrastive): Anchor sequence, positive pair (augmented version), negative samples, mapped to embedding space with distance relationships.
:::

---

### Figure 8.2: Masking Strategy Effects
Location: Line 20, at section "Masking Strategies and Their Implications"

::: {#fig-masking-strategies layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[High] Two-panel visualization comparing masking strategies on a regulatory sequence containing a TF binding motif. Panel A (Random token masking): Individual tokens masked throughout, including partial motif masking; show how local context allows easy prediction. Panel B (Span masking): Entire motif region masked as contiguous span; show how prediction requires reasoning from distal regulatory context. Include attention patterns for each, showing how span masking forces longer-range dependencies.
:::

---

### Figure 8.3: Bidirectional vs. Autoregressive Information Flow
Location: Line 61, at section comparing MLM and autoregressive objectives

::: {#fig-bidirectional-vs-autoregressive layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[Essential] Two-panel figure showing information flow during prediction. Panel A (MLM): Position in center of sequence with arrows coming from BOTH left and right context, showing bidirectional conditioning. Annotate: "Sees full context → better for understanding." Panel B (Autoregressive): Same position with arrows only from left (preceding tokens), showing causal restriction. Annotate: "Sees only past → enables generation."
:::

---

### Figure 8.4: Cross-Species Contrastive Learning
Location: Line 119, at section "Cross-Species Contrastive Learning"

::: {#fig-cross-species-contrastive}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Illustration of contrastive pretraining using orthologous sequences. Show: Human enhancer sequence and mouse ortholog (aligned, showing nucleotide divergence but conserved functional elements). Both mapped to embedding space as nearby points (positive pair). Non-orthologous sequence mapped to distant point (negative). Include phylogenetic context showing ~75 million years of divergence. Annotate: "Same function despite sequence divergence → learns species-invariant features."
:::

---

### Figure 8.5: Multi-Task Pretraining Architecture (Enformer-style)
Location: Line 142, at section "Large-Scale Multi-Task Examples"

::: {#fig-multitask-pretraining}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Diagram showing shared encoder with multiple prediction heads. Structure: Sequence input → Convolutional layers → Transformer layers (labeled "Shared Backbone") → Branching to separate heads for: Chromatin accessibility (DNase-seq, ATAC-seq), Histone modifications (H3K27ac, H3K4me3, etc.), Transcription factor binding (hundreds of factors), Gene expression (CAGE). Annotate approximate task counts from ENCODE: "674 DNase + 4,675 ChIP-seq + 638 CAGE."
:::

---

## Chapter 9: Transfer and Adaptation {#sec-transfer}

### Figure 9.1: Source and Target Domain Alignment
Location: Line 9, at section "Source and Target Domains"

::: {#fig-domain-alignment}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Schematic illustrating domain shift in genomic transfer learning. Left panel (Source Domain): Diverse genomic sequences during pretraining, with learned representations capturing statistical regularities (local motifs, composition, conservation). Right panel (Target Domain): Sparse labeled examples for clinical task (e.g., pathogenic variants, tissue-specific enhancers), highlighting distributional differences. Center: Representation space showing well-transferred features (local motifs, conservation patterns) connected by solid arrows vs. poorly-transferred features (long-range regulatory logic, tissue-specific patterns) with dashed arrows indicating transfer failure.
:::

---

### Figure 9.2: Low-Rank Adaptation (LoRA) Architecture
Location: Line 56, at section "Low-Rank Adaptation"

::: {#fig-lora-architecture}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Diagram showing LoRA modification to a transformer weight matrix. Show: Original frozen weight matrix W (large, e.g., 768×768). LoRA decomposition: small matrices A (768×r) and B (r×768) where r << 768 (e.g., r=16). Combined transformation: W + BA. Annotate parameter counts: "500M frozen + 2M trainable." Show how this applies to attention weight matrices (W^Q, W^K, W^V, W^O).
:::

---

### Figure 9.3: Adaptation Strategy Decision Tree
Location: Line 112, at section "Choosing an Adaptation Strategy"

::: {#fig-adaptation-decision-tree}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Flowchart guiding adaptation strategy selection. Decision nodes: (1) "Labeled data quantity?" with branches <500, 500-5000, >10000. (2) "Task similarity to pretraining?" with branches high/moderate/low. (3) "Computational constraints?" with branches limited/moderate/substantial. Terminal nodes recommend: Linear probing, LoRA/Adapters, Full fine-tuning, or From-scratch training. Include expected tradeoffs at each terminal (accuracy, compute, overfitting risk).
:::

---

### Figure 9.4: Domain Shift Detection Methods
Location: Line 154, at section "Detecting and Mitigating Shift"

::: {#fig-domain-shift-detection layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel visualization of domain shift detection. Panel A: UMAP/t-SNE projection of embeddings showing training distribution (dense cluster) and test examples at varying distances, with out-of-distribution examples clearly separated. Panel B: Calibration curves comparing confidence vs. accuracy for in-distribution (well-calibrated diagonal) vs. out-of-distribution examples (overconfident, curve below diagonal). Panel C: Performance degradation curve showing accuracy declining as distributional distance from training data increases.
:::

---

### Figure 9.5: Validation Pitfalls and Proper Evaluation
Location: Line 227, at section "Validation and Common Pitfalls"

::: {#fig-validation-pitfalls layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Multi-panel figure illustrating common validation failures. Panel A: Venn diagram showing pretraining data / test data overlap creating leakage (inflated performance). Panel B: Timeline showing temporal leakage when training on variants annotated after test set creation. Panel C: Bar chart comparing foundation model against weak baseline (large gap, misleading) vs. properly-tuned baseline (small gap, realistic). Panel D: Stratified performance showing aggregate accuracy (90%) vs. rare-variant accuracy (50%), revealing hidden failures.
:::

---

# Part III: Foundation Model Families (Chapters 10–14)

## Chapter 10: Foundation Model Paradigm {#sec-paradigm}

### Figure 10.1: From Task-Specific to Foundation Models
Location: Line 15, after section "From Task-Specific Models to Foundation Models"

::: {#fig-paradigm-shift layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[Essential] Two-panel comparison showing the paradigm shift. Panel A (Task-Specific Era): Multiple independent models (DeepSEA, SpliceAI, ExPecto) shown as separate pipelines, each with its own training data, architecture, hyperparameters; arrows showing no knowledge transfer between models; Label: "Train separately, no shared learning." Panel B (Foundation Model Era): Single large pretrained backbone at center, multiple lightweight adaptation heads branching out, downstream tasks (regulatory, splicing, expression, variant effect) as leaf nodes, shared representation layer highlighted; Label: "Pretrain once, adapt many."
:::

---

### Figure 10.2: Scaling Laws and Compute-Optimal Training
Location: Line 67, after section "Scaling Laws and Compute-Optimal Training"

::: {#fig-scaling-laws layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Three-panel figure illustrating scaling relationships. Panel A (Loss vs. Parameters): Log-log plot showing validation loss decreasing with parameter count; data points from Nucleotide Transformer family (50M → 2.5B); ESM-2 scaling curve overlaid for comparison; power law fit line with exponent annotation. Panel B (Compute-Optimal Frontier): Iso-performance contours on parameter × data plane; Chinchilla optimal line showing balanced allocation; undertrained region shaded; genomic data ceiling annotated (~10^12 nucleotides). Panel C (Emergent Capabilities): Capability (y-axis) vs. scale (x-axis, log); multiple curves showing different capabilities emerging at different scales; threshold markers where capabilities "switch on."
:::

---

### Figure 10.3: Four Families of Genomic Foundation Models
Location: Line 105, after section "A Taxonomy of Genomic Foundation Models"

::: {#fig-model-taxonomy layout-ncol=2}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] 2×2 grid with families as quadrants. Quadrant 1 (DNA Language Models, Blue): DNABERT, Nucleotide Transformer, HyenaDNA, Evo 2. Quadrant 2 (Protein Language Models, Purple): ESM-2, ProtTrans, ESMFold. Quadrant 3 (Sequence-to-Function Models, Green): Enformer, Borzoi, AlphaGenome. Quadrant 4 (Multi-Omic Models, Orange): Omni-DNA, cross-modal architectures. For each: representative models, input/output types, pretraining approach, strengths, limitations. Connecting lines showing where models can feed into each other.
:::

---

### Figure 10.4: Design Space for Genomic Foundation Models
Location: Line 175, after section "Design Dimensions"

::: {#fig-design-dimensions}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Multi-axis comparison (radar/spider plot or parallel coordinates) showing how different models make different design choices. Axes: (1) Context Length: 512bp → 1Mb; (2) Parameter Count: 10M → 15B; (3) Species Coverage: Human-only → Pan-genomic; (4) Architecture Type: CNN → Transformer → Hybrid → SSM; (5) Tokenization: Character → k-mer → BPE → Codon-aware; (6) Pretraining Objective: MLM → Autoregressive → Multi-task supervised. Models plotted: DNABERT-2, HyenaDNA, Evo 2, Enformer, Nucleotide Transformer.
:::

---

### Figure 10.5: When to Build, Adapt, or Use Foundation Models
Location: Line 220, after section "Build Versus Use Decisions"

::: {#fig-build-vs-use}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Decision flowchart with cost-benefit annotations. Entry Point: "New genomic prediction task." Decision nodes leading to terminal recommendations: USE (Frozen embeddings + simple classifier, Hours/$10, 70-90% of fine-tuned); ADAPT (LoRA/adapter fine-tuning, Days/$100-1000, 95% of full fine-tuning); BUILD (Custom pretraining, Months/$100K+, potentially best for domain). Annotations: "Most applications land here" pointing to USE/ADAPT paths; "Rare but sometimes necessary" pointing to BUILD.
:::

---

## Chapter 11: DNA Language Models {#sec-dna-lm}

### Figure 11.1: DNA Language Model Timeline (2021-2025)
Location: Line 11, replacing existing callout

::: {#fig-dna-lm-timeline}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Horizontal timeline with milestones and architectural innovations. Key milestones: 2021 DNABERT (512 tokens, proof of concept); 2023 Nucleotide Transformer (6kb, multi-species, scaling); 2023 HyenaDNA (1 Mb, sub-quadratic); 2024 Caduceus (reverse-complement equivariance, Mamba); 2024-2025 Evo 2 (1 Mb, 7B-40B params, pan-genomic). Upper track: Context length progression (log scale). Lower track: Key architectural innovations at each stage.
:::

---

### Figure 11.2: Breaking the Quadratic Barrier
Location: Line 64, after section "The Long-Context Revolution"

::: {#fig-long-context-revolution layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[Essential] Two-panel comparison. Panel A (Computational Complexity): Log-log plot showing sequence length (x) vs. compute/memory (y); standard attention O(L²) steep curve; Hyena/Mamba O(L) or O(L log L) much flatter; annotated points at 1kb, 10kb, 100kb, 1Mb showing tractability. Panel B (Biological Context Coverage): Same x-axis; biological features overlaid as ranges (TF binding ~10-20bp, promoter ~1kb, gene body ~10-50kb, enhancer-promoter ~20-200kb, TAD ~100kb-1Mb); vertical lines showing model context limits.
:::

---

### Figure 11.3: Reverse-Complement Equivariance
Location: Line 80, after section "Caduceus: Bidirectional Processing with Reverse-Complement Equivariance"

::: {#fig-caduceus-equivariance layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel diagram. Panel A (The Problem): Input sequence and reverse complement; standard model gives potentially different predictions; annotation: "Same biological information, inconsistent predictions." Panel B (Caduceus Architecture): BiMamba component with bidirectional arrows; MambaDNA block with weight-sharing scheme; mathematical relationship: f(revcomp(x)) = g(f(x)). Panel C (Performance Impact): Bar chart comparing models with/without equivariance on long-range tasks; annotation: "Appropriate biological inductive biases can substitute for raw scale."
:::

---

### Figure 11.4: Learning from the Tree of Life (Evo 2)
Location: Line 98, after section "Evo 2: Genome-Scale Modeling Across the Tree of Life"

::: {#fig-evo2-training layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel figure. Panel A (Training Corpus): Tree of life visualization with branch widths proportional to training data; Bacteria, Archaea, Eukaryotes, Viruses/Phages; total 9.3 trillion DNA tokens; contrast with human-only models (~3B tokens). Panel B (Architecture): StripedHyena 2 schematic with hybrid attention-convolution blocks; 1 Mb context; 7B and 40B variants. Panel C (Emergent Cross-Species Capabilities): Embedding space UMAP colored by taxonomic group; phylogenetic clustering emerging without explicit evolutionary modeling.
:::

---

### Figure 11.5: Probing Emergent Biological Knowledge
Location: Line 120, after section "Probing What Models Learn"

::: {#fig-dna-lm-probing layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Multi-panel figure. Panel A (Motif Recognition): First-layer attention patterns aligned with JASPAR motifs; model learns CTCF pattern from sequence statistics alone. Panel B (Gene Structure): t-SNE/UMAP of embeddings color-coded by region type (exon, intron, UTR, intergenic); clear clustering without region labels during training. Panel C (Evolutionary Constraint): Scatter plot of model uncertainty vs. phyloP conservation score; strong correlation. Panel D (What Models Don't Learn): Icons with X marks for epigenetic state, 3D structure, cell-type specificity, complex variants.
:::

---

### Figure 11.6: Benchmark Performance Across Tasks
Location: Line 144, after section "Benchmark Performance and Evaluation"

::: {#fig-dna-lm-benchmarks}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Heatmap or grouped bar chart. Models (rows): DNABERT-2, Nucleotide Transformer (2.5B), HyenaDNA, Caduceus, Evo 2. Benchmark tasks (columns) grouped: Short-range (promoter detection, enhancer classification, TF binding); Long-range (enhancer-promoter interaction, chromatin state); Variant effect (SNV scoring, splice prediction). Cell values: Relative performance (color scale). Key observations annotated: "No single model dominates all tasks"; "Long-context models excel on long-range tasks."
:::

---

## Chapter 12: Protein Language Models {#sec-protein-lm}

### Figure 12.1: What Protein Language Models Learn Without Supervision
Location: Line 30, after section "Emergent Biological Knowledge"

::: {#fig-plm-emergent layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Multi-panel figure. Panel A (Training Objective): Protein sequence with 15% masked; model predicting from context; "No structure, function, or evolutionary labels." Panel B (Secondary Structure in Attention): Attention heatmap with alpha helix and beta sheet regions highlighted; attention concentrating along structural patterns. Panel C (Residue Contacts from Attention): Attention weights converted to contact map; ground truth from crystal structure overlaid; strong correspondence. Panel D (Functional Site Discovery): Protein structure cartoon; positions with elevated attention highlighted; overlap with catalytic residues, binding sites.
:::

---

### Figure 12.2: ESM-2 Scaling Across Four Orders of Magnitude
Location: Line 49, after section "ESM-2: Scaling Up"

::: {#fig-esm2-scaling layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Scaling analysis. Panel A (Performance vs. Parameters): Log-log plot; x-axis parameters (8M → 15B); y-axis performance on structure-related tasks; multiple curves; no sign of saturation. Panel B (Model Family Table): ESM-2 variants stacked by size; visual encoding of layers, hidden dimension, performance; annotate where capabilities emerge (~150M useful embeddings, ~650M structural understanding, ~3B near-optimal single-sequence structure, ~15B approaches MSA methods). Panel C (Capability Thresholds): Specific capabilities as step functions; contact prediction gradual; zero-shot structure emergent at ~650M.
:::

---

### Figure 12.3: Eliminating the Alignment Bottleneck (ESMFold)
Location: Line 88, after section "ESMFold: Structure from Sequence"

::: {#fig-esmfold layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Four-panel figure. Panel A (Architecture Pipeline): Single sequence → ESM-2 (15B) embeddings → Structure module → 3D coordinates; "No MSA required." Panel B (Speed Comparison): Bar chart of AlphaFold2 (hours) vs ESMFold (minutes); 60× speedup. Panel C (Accuracy Comparison): Scatter plot ESMFold vs AlphaFold2 colored by MSA depth; well-represented proteins both accurate; sparse MSA proteins ESMFold more robust. Panel D (Metagenomic Application): Earth Microbiome Project proteins; many lack homologs; ESMFold enables scale.
:::

---

### Figure 12.4: Zero-Shot Variant Scoring
Location: Line 122, after section "Variant Effect Prediction"

::: {#fig-plm-variant-scoring layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Four-panel figure. Panel A (The Scoring Mechanism): Protein sequence with variant position; P(ref|context) vs P(var|context); Score = log P(var) - log P(ref). Panel B (Intuition): Evolution tested billions of substitutions; low probability variants = evolutionarily disfavored = likely disruptive. Panel C (Benchmark Performance): ROC curves ESM-1v vs classical methods on DMS data; competitive without variant labels. Panel D (AlphaMissense Enhancement): ESM embeddings + AlphaFold2 structural features; combined model; 71M precomputed scores; performance boost from structure.
:::

---

### Figure 12.5: Where Protein Language Models Struggle
Location: Line 170, after section "Limitations"

::: {#fig-plm-limitations}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Grid of limitation categories with visual examples. Orphan Proteins: Phylogenetic tree with isolated lineage; no homologs = no evolutionary context; performance degradation curve. Novel Folds: Designed protein with non-natural topology; predictions unreliable outside training. Conformational Flexibility: Protein with multiple conformations; PLM produces single embedding. Epistasis: Two distant positions; individual mutations benign; combination deleterious; models assume independence. Interpretability: Attention correlates with biology but mechanism remains opaque.
:::

---

## Chapter 13: Regulatory Models {#sec-regulatory}

### Figure 13.1: Why Context Length Matters for Gene Regulation
Location: Line 18, after section "The Long-Range Regulation Problem"

::: {#fig-long-range-regulation layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Four-panel biological motivation. Panel A (Regulatory Element Distribution): Canonical gene locus with promoter at TSS, enhancers 20-100kb away, silencer 50kb downstream, CTCF sites; scale bar 200kb. Panel B (Model Context Windows): Same locus with overlaid windows: DeepSEA (1kb) sees promoter only; Basenji2 (40kb) sees proximal regulation; Enformer (200kb) spans most elements; AlphaGenome (1Mb) full domain. Panel C (Information-Theoretic Barrier): Variant in enhancer 50kb from gene; short-context cannot distinguish from neutral; long-context can model relationship. Panel D (Scale of Problem): Distribution of enhancer-promoter distances; median 20-50kb; substantial fraction >100kb.
:::

---

### Figure 13.2: Hybrid CNN-Transformer Architecture (Enformer)
Location: Line 35, after section "Enformer: Attention Meets Regulatory Genomics"

::: {#fig-enformer-architecture}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Detailed three-stage architecture. Stage 1 (Convolutional Stem): 200kb one-hot input → conv blocks with residual connections → pooling → ~1,500 tokens (128bp resolution); "Compresses 100×, detects local features." Stage 2 (Transformer Trunk): Stack of self-attention layers, 8 heads, relative positional encodings; "Enables long-range interaction modeling." Stage 3 (Task-Specific Heads): Shared backbone → multiple outputs (DNase, histone marks, CAGE, ~5,000 tracks); "Multi-task regularizes representations." Inset: Why Hybrid Works—quadratic on 1,500 vs 200,000 tokens.
:::

---

### Figure 13.3: From Sequence Variant to Regulatory Prediction
Location: Line 53, after section "Variant Effect Prediction"

::: {#fig-regulatory-vep-workflow}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Workflow diagram. Step 1: Variant position → extract 200kb window centered; reference and alternative versions. Step 2: Parallel forward passes → output 5,000+ tracks × positions. Step 3: Delta computation (alt - ref) → identify tracks/positions with largest changes. Step 4: Interpretation examples—DNase ↓ in liver (reduced accessibility), H3K27ac ↓ at enhancer (weakened activity), CAGE ↓ at target gene (predicted expression decrease). Validation inset: Correlation with GTEx eQTLs; performance on distal variants (50+ kb).
:::

---

### Figure 13.4: Predicting Full RNA-seq Coverage (Borzoi)
Location: Line 78, after section "Borzoi: From Chromatin to Transcriptome"

::: {#fig-borzoi-rnaseq layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Four-panel figure. Panel A (What RNA-seq Captures): Gene with alternative isoforms; CAGE sees only TSS; RNA-seq coverage shows exon structure, splice junctions, polyadenylation. Panel B (Borzoi Predictions): Example gene with complex splicing; predicted stranded coverage profile; exon boundaries visible. Panel C (Beyond Expression Level): Splicing effects (changed junction usage), alternative promoters (shifted TSS), polyadenylation (altered 3' UTR length); each with clinical relevance. Panel D (Integration): Borzoi predictions + SpliceAI scores; complementary information.
:::

---

### Figure 13.5: Prediction Without Explanation (Limitations)
Location: Line 162, after section "Limitations and Open Challenges"

::: {#fig-regulatory-limitations layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Enhancing] Honest assessment. Panel A (Training Data Bias): Pie chart of ENCODE/Roadmap cell types; overrepresented ESCs, K562, HepG2; underrepresented disease-relevant states. Panel B (Missing 3D Context): Linear sequence model vs actual looped, compartmentalized chromatin; distant elements in 3D proximity. Panel C (Correlation vs. Causation): Variant with high predicted effect; is it because motif disruption causes change, or correlation in training? Panel D (Finite Context): 200kb-1Mb windows; trans-acting factors genome-wide; SVs span megabases.
:::

---

## Chapter 14: Variant Effect Prediction with Foundation Models {#sec-vep-fm}

### Figure 14.1: From Feature Engineering to Representation Learning
Location: Line 18, after section "The Foundation Model Paradigm for Variant Interpretation"

::: {#fig-fm-vep-paradigm layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Paradigm comparison. Panel A (Classical Approach): Variant → hand-crafted features (conservation, Grantham, domains, regulatory marks) → feature vector → classifier → score; limitation: coverage limited by annotations. Panel B (Foundation Model Approach): Same variant → pretrained model → learned representations → adaptation → score; strength: extends to any position. Panel C (What Changes): Classical features explicit/interpretable/manual; foundation features learned/opaque/automatic; trade-off arrow. Panel D (Three Families): Protein LMs → missense; DNA LMs → all variants; Regulatory models → noncoding mechanism; arrow: "Most powerful combine families."
:::

---

### Figure 14.2: Structure-Informed Pathogenicity Prediction (AlphaMissense)
Location: Line 64, after section "AlphaMissense: Structure-Informed Pathogenicity Prediction"

::: {#fig-alphamissense layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Four-panel figure. Panel A (Input Integration): Protein sequence → ESM-like embeddings; mutation position → AlphaFold2 structural context (secondary structure, solvent accessibility, contact density); combined features. Panel B (Training Strategy): NOT trained on ClinVar; instead population frequency as pathogenicity proxy; common in gnomAD → likely benign; absent + disease context → likely pathogenic; reduces circularity risk. Panel C (Calibration): Raw outputs → isotonic regression → calibrated probabilities; reliability diagram; score 0.8 = 80% pathogenic; thresholds annotated. Panel D (Performance): DMS benchmarks (ρ = 0.5-0.7 vs CADD 0.3-0.5); ClinVar (AUROC >0.9 vs 0.85-0.88); structural component essential.
:::

---

### Figure 14.3: Combining Evidence Across Modalities
Location: Line 138, after section "Combining Evidence Across Modalities"

::: {#fig-multimodel-integration layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Practical integration workflow. Panel A (Model Selection by Variant Type): Missense → AlphaMissense, ESM-1v; splice-proximal → SpliceAI; deep intronic → Enformer, cryptic splice; promoter/enhancer → Enformer, AlphaGenome; synonymous → splicing + regulatory; structural → limited coverage flag. Panel B (Evidence Integration): Same variant scored by multiple models; example missense near exon boundary; AlphaMissense 0.85, SpliceAI 0.45, Enformer regulatory effect; combining without double-counting. Panel C (Correlation and Redundancy): Correlation matrix between scores; high correlation = shared info (don't count twice); residual analysis. Panel D (Practical Workflow): Tier 1 fast screening (DNA-LM likelihood); Tier 2 detailed (AlphaMissense, SpliceAI); Tier 3 mechanistic (AlphaGenome); cost/time at each tier.
:::

---

### Figure 14.4: From Scores to Clinical Decisions (Calibration)
Location: Line 160, after section "Calibration and Clinical Categories"

::: {#fig-calibration-clinical layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Four-panel figure. Panel A (The Calibration Problem): Raw model score distribution; neural networks often overconfident (cluster near 0/1); reliability diagram showing miscalibration. Panel B (Calibration Methods): Temperature scaling, isotonic regression, Platt scaling; before/after reliability diagrams. Panel C (Mapping to ACMG Categories): Continuous score 0-1; thresholds defining PP3, VUS, BP4; threshold selection trade-off. Panel D (What Uncertainty Looks Like): Intermediate scores genuinely reflect uncertainty; example variants at different score levels; "A score of 0.73 means nothing without calibration context."
:::

---

### Figure 14.5: Knowing What We Don't Know (Uncertainty)
Location: Line 200, after section "Uncertainty Quantification"

::: {#fig-vep-uncertainty layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Four-panel figure. Panel A (Sources of Uncertainty): Epistemic (model hasn't seen similar, reducible) vs aleatoric (inherent noise, irreducible); training distribution vs query position. Panel B (Ensemble Methods): Multiple models trained differently; prediction variance; high disagreement = high epistemic uncertainty. Panel C (Conformal Prediction): Calibration set → conformal scores; prediction sets with coverage guarantee; confident {Benign} vs uncertain {P, VUS, B}. Panel D (OOD Detection): Embedding space; training examples dense region; query variant isolated = OOD; flag for manual review.
:::

---

### Figure 14.6: Gains and Gaps in Foundation Model VEP
Location: Line 230, after section "What Foundation Models Add"

::: {#fig-vep-gains-gaps layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Enhancing] Balanced assessment. Panel A (Performance Improvements): Benchmark comparison table (Method | ClinVar AUROC | DMS Correlation | Coverage). Panel B (Where Improvements Largest): Difficult cases (sparse annotations, orphan genes), context-dependent effects, novel genes. Panel C (Persistent Gaps): Population bias, complex variants (SVs, repeats, phase), combinatorial effects (epistasis, compound het), tissue specificity. Panel D (The Bottom Line): Foundation models = tools for interpretation, not oracles; best use = combined with population data, functional evidence, clinical judgment.
:::

---

# Part IV: Beyond Sequence (Chapters 15–19)

## Chapter 15: RNA Structure and Function {#sec-rna}

### Figure 15.1: RNA vs. Protein Folding Landscapes
Location: Line 25, after section "The Flat Energy Landscape Problem"

::: {#fig-rna-energy-landscape layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[Essential] Two-panel comparison. Panel A (Protein Folding): 3D surface with deep funnel topology; clear global minimum (native state); steep energy barriers; folding trajectory descending into funnel; "Deep minimum—single stable structure." Panel B (RNA Folding): Flatter surface with multiple shallow minima at similar energy levels; small energy differences; multiple arrows showing alternative folding paths; "Flat landscape—multiple competing structures." Bottom panel: Same RNA sequence adopting different structures; riboswitch example; RNA thermometer.
:::

---

### Figure 15.2: The Grammar of RNA Folding
Location: Line 36, after section "Base Pairing and Long-Range Dependencies"

::: {#fig-rna-structure-elements layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Comprehensive diagram. Panel A (Basic Elements): Stem, hairpin loop, internal loop, bulge, multi-loop/junction. Panel B (Long-Range Pairing): Linear sequence with arc diagram showing base pairs; contrast with protein local secondary structure (~10 residues); "RNA base pairs span hundreds of nucleotides." Panel C (Pseudoknot): Interleaved pairing in notation and 3D; "Increases complexity from O(n³) to O(n⁶)"; telomerase RNA example. Panel D (Notation Systems): Dot-bracket, arc diagram, 2D graphical representation.
:::

---

### Figure 15.3: The Maturity Gap Between RNA and Protein Language Models
Location: Line 82, after section "The Scale Gap with Protein Language Models"

::: {#fig-rna-plm-gap layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Scale comparison. Panel A (Scale Comparison Table): Training sequences (65M vs 23M, 3×); Structural diversity (all protein families vs mainly tRNA/rRNA); Parameters (15B vs ~100M, 150×); Emergent structure (contacts/folding vs limited). Panel B (Training Data Composition): Protein pie chart (diverse families) vs RNA (dominated by tRNA, rRNA, ribozymes). Panel C (Emergent Capabilities Comparison): Protein LMs (structure prediction ✓, variant effects ✓) vs RNA LMs (secondary partial ⚠, tertiary missing). Panel D (The Data Challenge): PDB proteins >200,000 vs RNA <2,000.
:::

---

### Figure 15.4: What Synonymous Codons Reveal
Location: Line 108, after section "Beyond Nucleotide Tokenization"

::: {#fig-codon-tokenization layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Codon-level modeling. Panel A (Same Protein, Different mRNA): Amino acid sequence; multiple mRNA sequences encoding same protein; highlight synonymous codon choices. Panel B (What Codon Choice Affects): tRNA availability, translation speed, mRNA structure, stability (GC content). Panel C (Tokenization Comparison): Character-level (900 tokens for 300 AA), codon-level (300 tokens); "Encodes biological prior." Panel D (Model Capabilities): Protein LM sees amino acids only; DNA LM sees nucleotides but no codon boundaries; Codon LM sees both.
:::

---

### Figure 15.5: From Protein Target to Optimized mRNA
Location: Line 155, after section "Model-Based Design Strategies"

::: {#fig-mrna-design-pipeline}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] End-to-end pipeline. Stage 1 (Target Protein): Desired sequence and structural requirements. Stage 2 (Codon Optimization): ~3^300 possibilities; objectives (expression, stability, immunogenicity); model-based scoring. Stage 3 (5' UTR Design): Translation initiation, Kozak, secondary structure. Stage 4 (3' UTR Design): Stability elements, miRNA avoidance, poly-A tail. Stage 5 (Modification Selection): N1-methylpseudouridine. Output: Optimized construct. Inset: COVID-19 vaccine design choices.
:::

---

## Chapter 16: Single-Cell Models {#sec-single-cell}

### Figure 16.1: The Cellular Language Model Analogy
Location: Line 17, after section "From Bulk to Single-Cell Resolution"

::: {#fig-cellular-lm-analogy layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Visual analogy. Panel A (Language Model): Sentence "The cat sat on the mat"; words as tokens; grammar rules; BERT predicts masked words. Panel B (Cellular Language Model): Cell expression profile as "sentence"; genes as tokens (~20,000 vocabulary); regulatory programs as "grammar"; Geneformer/scGPT predict masked genes. Panel C (Parallel Structure Table): NLP ↔ Single-Cell mapping. Panel D (What Models Learn): Language (syntax, semantics) ↔ Cellular (co-expression modules, cell type programs, perturbation effects).
:::

---

### Figure 16.2: Sparsity, Dropout, and Batch Effects
Location: Line 28, after section "Technical Challenges and Data Characteristics"

::: {#fig-single-cell-challenges layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Data challenges. Panel A (Dropout/Sparsity): Gene × Cell matrix mostly zero (90%+); "Zero can mean silent OR undetected." Panel B (Batch Effects): UMAP colored by cell type (mixed) vs batch (clustered); "Technical variation can exceed biological." Panel C (Dynamic Range): Histogram spanning orders of magnitude; few copies for some genes. Panel D (How Foundation Models Address): Rank-based encoding handles range; large corpus learns robust patterns; contrastive objectives for batch-invariance.
:::

---

### Figure 16.3: Rank-Based Gene Representation (Geneformer)
Location: Line 41, after section "Geneformer: Learning Network Biology"

::: {#fig-geneformer-architecture layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Geneformer innovations. Panel A (Rank-Based Encoding): Raw expression → ranks relative to corpus baseline → tokens; "Highlights unusually active/silent genes." Panel B (Architecture): Ranked gene sequence → transformer encoder (BERT-style) → masked gene prediction → gene/cell embeddings. Panel C (What Attention Learns): Network diagram showing gene-gene attention; correspondence to regulatory relationships; "Network hierarchy emerges without supervision." Panel D (Transfer Applications): Cell type annotation, therapeutic target ID, disease gene prioritization.
:::

---

### Figure 16.4: In Silico Genetic Experiments
Location: Line 83, after section "The In Silico Experiment Promise"

::: {#fig-perturbation-prediction layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Perturbation response. Panel A (The Task): Unperturbed cell + perturbation identity → predicted post-perturbation profile → comparison to Perturb-seq. Panel B (Training Data): CRISPR knockout library + single-cell readout; thousands of genes × cells; "Supervised signal." Panel C (What Models Must Learn): Directional relationships (A activates B → KO A reduces B); network cascades; context dependence. Panel D (Current Performance): Strong for well-characterized genes; weak for poorly characterized; "Predictions most accurate where we need them least."
:::

---

### Figure 16.5: Graph-Linked Unified Embedding (GLUE)
Location: Line 130, after section "GLUE: Graph-Linked Unified Embedding"

::: {#fig-glue-architecture layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Multi-omics integration. Panel A (Unpaired Integration Problem): RNA-seq in cells A,B,C; ATAC-seq in D,E,F; no direct correspondence; goal: unified embedding. Panel B (GLUE Architecture): Modality-specific VAE encoders; feature graph linking genes ↔ peaks; shared latent space; adversarial alignment. Panel C (Feature Graph as Prior): Nodes (genes, peaks, TF sites); edges (proximity, regulatory); graph VAE learns embeddings; "Biological knowledge constrains alignment." Panel D (Applications): Cross-modal prediction, regulatory inference, triple-omics integration.
:::

---

## Chapter 17: 3D Genome Organization {#sec-3d-genome}

### Figure 17.1: Nested Levels of Genome Folding
Location: Line 22, after section "Chromatin Organization Hierarchy"

::: {#fig-chromatin-hierarchy layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Four-level visualization. Panel A (Chromosome Territories, Nuclear Scale): Nucleus with distinct territories; gene-rich interior, gene-poor periphery. Panel B (A/B Compartments, Megabase Scale): Hi-C checkerboard pattern; A active interior, B inactive lamina-associated. Panel C (TADs, Sub-Megabase Scale): Triangular domains; sharp boundaries; median ~800 kb; CTCF at boundaries. Panel D (Loops, Kilobase Scale): Focal Hi-C enrichments; enhancer-promoter contacts; CTCF-CTCF structural loops.
:::

---

### Figure 17.2: How Cohesin and CTCF Create TADs
Location: Line 22, following Figure 17.1

::: {#fig-loop-extrusion layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Loop extrusion mechanism. Panel A (Cohesin Loading): Ring loading onto chromatin; initial state no loop. Panel B (Bidirectional Extrusion): Cohesin extruding DNA; loop growing progressively; intermediate states. Panel C (CTCF Arrest): Cohesin encountering convergent CTCF; extrusion halted; stable loop. Panel D (The Orientation Rule): Convergent → ← (loop anchors ✓); divergent ← → (no stable loop ✗); tandem → → (extrusion continues ~). Inset: Acute cohesin degradation eliminates TADs but compartments remain.
:::

---

### Figure 17.3: Akita, Orca, and C.Origami Architectures
Location: Line 49, after section "Predicting 3D Structure from Sequence"

::: {#fig-3d-prediction-models layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Model comparison. Panel A (Akita Architecture): 1 Mb DNA input → dilated convolutions → symmetric output → 2 kb Hi-C. Panel B (Orca Multi-Scale): Coarse Mb prediction → progressive refinement → multi-resolution loss. Panel C (C.Origami with CTCF): Sequence + CTCF ChIP-seq → cell-type-specific predictions; transfer from Hi-C-rich to CTCF-only cells. Panel D (Prediction vs. Ground Truth): Example region; TAD boundaries correctly positioned; loop anchors identified; "Sequence contains substantial 3D information."
:::

---

### Figure 17.4: Enhancer Hijacking at the EPHA4 Locus
Location: Line 5-6, section discussing structural variants

::: {#fig-tad-disruption layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Clinical example. Panel A (Normal Configuration): TAD with EPHA4 and limb enhancers; adjacent TAD with WNT6/PAX3; boundary separating; "Enhancers contact EPHA4, not WNT6." Panel B (Boundary Deletion): Boundary removed; TADs merge; enhancers can contact both genes. Panel C (Pathogenic Outcome): Limb enhancers activate WNT6 ectopically; abnormal expression; brachydactyly. Panel D (Interpretation Implications): Same-size deletions, different outcomes; boundary-preserving may be benign; boundary-disrupting pathogenic; "Current VEP tools miss 3D effects."
:::

---

### Figure 17.5: From Tissue Sections to Spatial Foundation Models
Location: Line 78, section on spatial transcriptomics

::: {#fig-spatial-transcriptomics layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Enhancing] Spatial data and models. Panel A (Visium Spot-Based): Tissue section with spot overlay; 1-10 cells per spot; ~55 μm resolution. Panel B (Imaging-Based MERFISH/Xenium): Single-cell resolution; limited gene panel; subcellular localization. Panel C (Deconvolution Challenge): Multi-cell spot → infer composition; reference atlas required. Panel D (Spatial Foundation Models): Cell as node, proximity as edge; GNNs over spatial graphs; cell-cell communication; examples (Nicheformer, SpaGCN, GraphST).
:::

---

## Chapter 18: Graph and Network Models {#sec-gnn}

### Figure 18.1: The Integration Principle
Location: Line 88, chapter opening/section "The Integration Principle"

::: {#fig-gnn-integration layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Central concept. Panel A (Foundation Models Produce Representations): ESM-2 → protein embeddings; DNABERT → DNA embeddings; scGPT → cell embeddings; "Rich representations of individual entities." Panel B (Biological Networks Encode Relationships): PPI, regulatory, cell-cell communication; "Relational structure not in sequence." Panel C (GNNs Integrate Both): Node features from FMs; edges from networks; message passing refines representations; context-aware outputs. Panel D (Capabilities Neither Achieves Alone): FM can't model interactions; networks alone limited features; combined enables disease gene prioritization, drug-target prediction.
:::

---

### Figure 18.2: Types of Biological Graphs
Location: Line 28, after section "The Landscape of Biological Graphs"

::: {#fig-biological-networks layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Network landscape. Panel A (PPI Networks): Undirected edges (physical binding); STRING, BioGRID, IntAct; "20-30% catalogued." Panel B (Gene Regulatory Networks): Directed TF → target edges; ChIP-seq, ATAC-seq, motifs; cell-type specific. Panel C (Knowledge Graphs): Multiple node types (genes, diseases, drugs, pathways); multiple edge types; multi-hop reasoning; Hetionet example. Panel D (Spatial Graphs): Nodes as cells/spots; edges as proximity/communication; from spatial transcriptomics; emerging and sparse.
:::

---

### Figure 18.3: How GNNs Learn from Graph Structure
Location: Line 64, after section "Why Message Passing?"

::: {#fig-message-passing layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Step-by-step message passing. Panel A (Initial State): 5-node graph; each with initial features from FM. Panel B (Message Computation): For each edge, compute message m_ij = φ(h_i, h_j, e_ij); visualize as arrows. Panel C (Aggregation): Each node aggregates incoming (sum, mean, max, attention); new representation. Panel D (After L Layers): Each embedding incorporates L-hop neighborhood; "Gene embedding now reflects pathway context." Mathematical summary at bottom.
:::

---

### Figure 18.4: Network-Based Causal Gene Identification
Location: Line 124, after section "Disease Gene Prioritization"

::: {#fig-disease-gene-prioritization layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] GWAS follow-up. Panel A (The GWAS Challenge): Locus with genes A,B,C,D; lead SNP in LD with all; which is causal? Panel B (Network Context): Same genes in PPI; gene B connected to 5 known disease genes; A,C,D peripheral. Panel C (GNN Scoring): FM embeddings as node features; disease labels propagate; B receives higher network score. Panel D (Integration with Sequence Features): Gene C strong protein features; gene B network + moderate protein; combined identifies both candidates.
:::

---

### Figure 18.5: Multi-Hop Reasoning for Drug Discovery
Location: Line 146, after section "Knowledge Graph Reasoning and Drug Repurposing"

::: {#fig-kg-drug-repurposing layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Knowledge graph reasoning. Panel A (KG Structure): Heterogeneous graph with drugs, proteins, diseases, pathways; multiple edge types. Panel B (Multi-Hop Reasoning Path): Drug D → binds → Protein P1 → participates_in → Pathway W → disrupted_in → Disease X. Panel C (Link Prediction): Learn embeddings; predict missing edges; score drug-disease pairs; new indication discovery. Panel D (FM Enhancement): Replace node features with FM embeddings; capture functional similarity beyond database annotations.
:::

---

### Figure 18.6: Study Bias in Biological Networks
Location: After section on limitations

::: {#fig-network-bias}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Study bias visualization. Node degree vs. publication count showing strong correlation; well-studied genes (TP53, BRCA1) highly connected; understudied genes peripheral; risk: GNN prioritizes well-studied genes; mitigation strategies (degree normalization, attention to edge confidence).
:::

---

## Chapter 19: Multi-Omics Integration {#sec-multi-omics}

### Figure 19.1: The Integration Promise and Paradox
Location: Chapter opening

::: {#fig-integration-paradox}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Central tension. Panel A (The Promise): Different modalities capture different aspects; genomics (heritable potential), transcriptomics (current state), proteomics (functional complement), metabolomics (downstream biochemistry); integration should improve prediction. Panel B (The Paradox): More modalities = more features = more overfitting risk; missing data compounds problem; when does integration actually help? Panel C (When Integration Helps): Complementary information (genomics + expression for complex traits), cross-modality validation, mechanistic interpretation. Panel D (When Integration Hurts): Redundant information, batch effects across modalities, sample size dilution.
:::

---

### Figure 19.2: Three Fusion Strategies
Location: Section on fusion strategies

::: {#fig-fusion-strategies layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Strategy comparison. Panel A (Early Fusion): All features concatenated → single model; pros: can learn cross-modal interactions; cons: curse of dimensionality, requires complete data. Panel B (Late Fusion): Separate models → predictions combined; pros: handles missing, modality-specific architectures; cons: cannot learn feature interactions. Panel C (Intermediate Fusion): Modality-specific encoders → shared latent space → task head; pros: flexibility + robustness; cons: alignment complexity. Summary table comparing cross-modal interactions, missing data handling, compute.
:::

---

### Figure 19.3: Shared Latent Space Integration
Location: Line 72, after section "Intermediate Fusion"

::: {#fig-intermediate-fusion layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Detailed architecture. Panel A (Modality-Specific Encoders): Expression VAE, methylation CNN, proteomics MLP; each tailored to modality. Panel B (Shared Latent Space): All encoders output same dimensionality; alignment via reconstruction loss, contrastive loss, graph constraints. Panel C (Downstream Task Head): Classifier/regressor on latent representation; can use partial representations. Panel D (Missing Modality Handling): Complete sample all encoders fire; partial sample available encoders only; graceful degradation.
:::

---

### Figure 19.4: From Variant to Phenotype Through Molecular Layers
Location: Line 155, after section "The Information Cascade"

::: {#fig-information-cascade}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Systems biology view. Panel A (The Causal Cascade): Genetic variant → (cis-regulation) → Expression change → (translation) → Protein change → (metabolism) → Metabolite change → (cellular) → Cell behavior → (tissue) → Clinical phenotype. Panel B (Where Each Modality Provides Information): Genomics (starting point), transcriptomics (current state), proteomics (functional complement), metabolomics (downstream), clinical (manifestation). Panel C (Bottleneck Modalities): Coding variants bottleneck at protein; regulatory at expression; some phenotypes bottleneck downstream. Panel D (Integration Implications): Model should trace causal chain; not all modalities equally informative for all questions.
:::

---

### Figure 19.5: Combining EHR, Imaging, and Molecular Data
Location: Line 140, after section "Multi-Modal Clinical Prediction Models"

::: {#fig-clinical-multimodal layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Patient-level integration. Panel A (Data Modalities): EHR (diagnoses, procedures, medications, labs—longitudinal), imaging (CT, MRI, histopathology—spatial), molecular (genomics, expression, proteomics—static). Panel B (Modality-Specific Encoders): EHR transformer over event sequence; imaging vision encoder; molecular FM embeddings. Panel C (Patient Representation Space): All → shared patient embedding; EHR predicts molecular; imaging consistent with trajectory. Panel D (Clinical Prediction Tasks): Risk stratification, treatment response, prognosis; missing modality handling (not all patients have all data). Practical challenges callout: batch effects, temporal alignment, cost constraints.
:::

---

# Part V: Evaluation and Interpretation (Chapters 20–24)

## Chapter 20: Benchmarks {#sec-benchmarks}

### Figure 20.1: The Benchmark Landscape
Location: Early in chapter after opening section

::: {#fig-benchmark-landscape}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Navigational map organized as matrix. Rows (modalities): Protein, DNA/Regulatory, Variant Effect, Trait-Level. Columns (benchmark types): Structure, Function, Effect Prediction, Clinical Relevance. Include: TAPE, FLIP, ProteinGym, Genomic Benchmarks, BEND, ClinVar, CAGI, DMS/MaveDB, TraitGym, EmbedGEM. Visual encoding: icons per modality, color intensity for maturity, size for scale. Annotations: typical evaluation progression, prospective vs retrospective benchmarks.
:::

---

### Figure 20.2: The Proxy-to-Target Gap
Location: Section on benchmark-deployment gap

::: {#fig-proxy-target-gap}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Conceptual diagram with layers. Left column (What we measure): ClinVar labels, held-out AUROC, DMS correlation, expression prediction accuracy. Right column (What we want): True clinical impact, deployment discrimination, actual protein function, regulatory mechanism. Center: Arrows with gap indicators. Gap factors: label quality, distribution shift, metric mismatch, temporal drift. Width of arrows indicates strength of proxy. Key insight: gap not uniform.
:::

---

### Figure 20.3: Benchmark Saturation and Staleness
Location: Section on benchmark saturation

::: {#fig-benchmark-saturation layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[High] Two-panel figure. Panel A (Saturation curve): Time vs benchmark performance; multiple lines; ceiling line; saturation zone annotation. Panel B (Staleness timeline): Benchmark creation dates above; data collection/annotation dates; current year below; growing gap; examples (ENCODE 2012, ClinVar evolving).
:::

---

### Figure 20.4: Leakage Pathways in Genomic Benchmarks
Location: Section on Goodhart's Law and benchmark gaming

::: {#fig-leakage-pathways}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Flow diagram showing data flow with leakage highlighted. Central pipeline: Pretraining → FM → Fine-tuning → Benchmark. Leakage pathways (red): Direct overlap, homology leakage, label circularity, resource sharing, community iteration. Specific examples: ESM/UniRef→ProteinGym, ClinVar/CADD circularity, ENCODE in both. Visual encoding: legitimate flow blue, leakage red dashed.
:::

---

### Figure 20.5: Cross-Population Benchmark Performance
Location: Section on systematic gaps

::: {#fig-cross-population-performance}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Grouped bar chart or heatmap. Rows: Different tasks/models. Columns: Ancestry groups (European, African, East Asian, South Asian, Admixed). Values: Performance metrics. Specific comparisons: PGS 40-75% reduction non-European; ClinVar-trained models across ancestries. Annotations: sample sizes, significance, training data representation. Key insight: aggregate conceals systematic failures.
:::

---

## Chapter 21: Evaluation Principles {#sec-evaluation}

### Figure 21.1: Why Random Splits Fail in Genomics
Location: Section on why random splits fail

::: {#fig-random-splits-fail layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Three-panel comparison. Panel A (Image classification): Grid of images; random assignment works; independent. Panel B (Protein classification): Family tree; random split places related across train/test; 80% identity highlighted; "memorization pathway." Panel C (Variant prediction): Gene diagram with variants; same gene in train/test; family pedigree spanning splits; population structure. Annotations: sequence identity, relatedness, pseudo-replication.
:::

---

### Figure 21.2: Homology-Aware Splitting Workflow
Location: Section on homology-aware splitting

::: {#fig-homology-splitting}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Step-by-step workflow. Steps: (1) All sequences; (2) Clustering (CD-HIT/MMseqs2 at threshold); (3) Cluster visualization; (4) Split assignment (entire clusters to train/val/test); (5) Validation (no test >X% identity to training). Code snippets. Comparison table (strategy, strictness, efficiency, use case). Key insight: threshold determines hardness.
:::

---

### Figure 21.3: Splitting by Biological Axis
Location: Section on splitting by biological axis

::: {#fig-splitting-strategies}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Matrix: Splitting strategies vs. what they test. Rows: Random, individual-aware, family-aware, chromosome, gene/protein family, cohort/site, temporal, ancestry. Columns: Sequence generalization, individual, population, temporal robustness, cross-site. Cells: ✓, ✗, ~. Schematics for each strategy; performance drop annotations; combinable strategies note.
:::

---

### Figure 21.4: Leakage Taxonomy
Location: Section on leakage taxonomy

::: {#fig-leakage-taxonomy}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Taxonomy tree. Top: Data Leakage. Branches: Feature Leakage (features encode target; conservation→pathogenicity; detection via ablation), Label Leakage (labels derived from model-accessible info; ClinVar circularity; temporal validation), Benchmark Leakage (pretraining overlaps evaluation; ENCODE everywhere; document and check overlap). For each: red warning, genomic example, detection strategy, mitigation.
:::

---

### Figure 21.5: Metrics for Genomic Tasks
Location: Section on metrics

::: {#fig-metric-selection}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Decision flowchart. Decision points: Binary vs continuous? Balanced? Ranking vs probability? Clinical decisions? Metric recommendations at each terminal. Metric descriptions: AUROC, AUPRC, calibration, net benefit. Warning callouts: "AUROC invariant to monotonic transforms"; "High correlation ≠ clinically meaningful."
:::

---

### Figure 21.6: Foundation Model Evaluation Paradigms
Location: Section on evaluating foundation models

::: {#fig-fm-evaluation-paradigms layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Enhancing] Three-column comparison. Column 1 (Zero-shot): Frozen model → direct prediction; tests alignment; ESM-1v log-likelihood example; pros/cons. Column 2 (Linear Probing): Frozen → embeddings → linear classifier; tests linear accessibility; isolates representation quality; pros/cons. Column 3 (Fine-tuning): Gradients → adaptation; tests total potential; best performance but conflates representation with adaptation. Bottom: Data efficiency curve; "Pretraining value = gap at low data."
:::

---

## Chapter 22: Confounders and Leakage {#sec-confounding}

### Figure 22.1: Confounding in Genomic Prediction
Location: Early in chapter after opening

::: {#fig-confounding-dag}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] DAG with genomic example. Main DAG: Confounder (Ancestry) with arrows to Exposure (Genomic features) and Outcome (Disease status); spurious path X ← C → Y highlighted. Annotation boxes explaining how ancestry affects both. Second DAG showing adjustment blocking spurious path. Concrete example: Rare disease clinic → ClinVar submissions → ancestry proxy learned. Key insight: shortcuts appear to work until deployment shifts.
:::

---

### Figure 22.2: Population Structure as Shortcut
Location: Section on population structure

::: {#fig-population-structure-shortcut layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Multi-panel figure. Panel A (PCA of genomic data): PC1 vs PC2; colored by ancestry; clear clustering. Panel B (Ancestry in k-mer frequencies): Heatmap across populations; even local composition differs. Panel C (The shortcut pathway): Flow diagram (Ancestry → Sequencing → Labels; Ancestry → Allele frequencies → Features; model learns via ancestry). Panel D (Cross-population performance): Bar chart showing 40-75% PGS reduction; "Shortcuts fail when relationship changes."
:::

---

### Figure 22.3: Technical Batch Effects
Location: Section on technical artifacts

::: {#fig-batch-effects layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel figure. Panel A (Batch structure in embeddings): UMAP colored by sequencing center; samples cluster by batch not phenotype. Panel B (Coverage patterns by batch): Genome browser tracks; different centers show systematic differences. Panel C (Batch predicts phenotype): Contingency table (batch × case/control); imbalanced distribution. Warning: "Model predicting disease may actually predict sequencing center."
:::

---

### Figure 22.4: Label Bias and Circularity
Location: Section on label bias

::: {#fig-label-circularity}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Circular flow diagram. Steps: (1) Clinical lab submits to ClinVar using CADD/REVEL as evidence; (2) ClinVar aggregates (computational evidence influences labels); (3) New model trains on ClinVar (learns to replicate patterns); (4) New model used by labs (influences next submissions); (5) Return to step 1. Annotations: circularity, apparent validation reflects agreement not insight. Side panel: Breaking cycle (prospective, temporal, independent functional).
:::

---

### Figure 22.5: Detecting Confounding
Location: Section on detecting confounding

::: {#fig-confounding-detection}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Diagnostic checklist with visualizations. Diagnostic 1 (Confounder-only baseline): Bar chart comparing full model vs ancestry PCs only vs batch only; if simple baseline approaches full → confounding. Diagnostic 2 (Subgroup stratification): Multiple reliability diagrams by ancestry. Diagnostic 3 (Prediction-confounder association): Scatter of predictions vs PC1; residual after controlling for label. Diagnostic 4 (Split sensitivity): Table showing performance across split strategies; large drop = memorization. Diagnostic 5 (Negative controls): Accuracy on outcomes unrelated to genetics; should be chance.
:::

---

### Figure 22.6: Mitigation Strategies
Location: Section on mitigation

::: {#fig-mitigation-strategies}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Strategy comparison table. Strategies: Study design (match cases/controls, before collection, reduces sample), Covariate adjustment (include ancestry/batch as inputs, during training, may remove real signal), Domain adaptation (train invariant to confounders, complex), Robust optimization (minimize worst-group error, requires group labels), Benchmark design (locus-level splits, during evaluation, harder scores by design). Annotation: "Approaches complementary—use multiple."
:::

---

## Chapter 23: Uncertainty Quantification {#sec-uncertainty}

### Figure 23.1: Epistemic vs. Aleatoric Uncertainty
Location: Section on types of uncertainty

::: {#fig-uncertainty-types layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[Essential] Two-panel conceptual diagram. Panel A (Epistemic, reducible): Novel protein fold not in training; embedding space with dense clusters and isolated test point; could reduce with more data; ensemble members disagree; examples (under-represented ancestry, rare gene, novel pathogen). Panel B (Aleatoric, irreducible): Incomplete penetrance in BRCA1; same variant, different outcomes; inherent randomness; examples (penetrance variation, DMS noise, context-dependent regulation). Bottom: Decomposition formula; practical implication (high epistemic → more data; high aleatoric → accept limits).
:::

---

### Figure 23.2: Calibration and Reliability Diagrams
Location: Section on calibration

::: {#fig-calibration-diagrams layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[Essential] Four-panel figure. Panel A (Perfect calibration): Reliability diagram on diagonal; "Predictions match reality." Panel B (Overconfident): Points below diagonal; model predicts 0.9, true frequency 0.6; common for DNNs; "Dangerous for clinical use." Panel C (Underconfident): Points above diagonal; "May miss actionable variants." Panel D (Miscalibration by subgroup): Two curves (European, African); one calibrated, one poor; "Aggregate can mask disparities." Annotations: ECE, prediction histograms, "Calibration ≠ discrimination."
:::

---

### Figure 23.3: Calibration Methods
Location: Section on recalibration

::: {#fig-calibration-methods layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-column comparison with before/after. Column 1 (Temperature scaling): Formula p = softmax(z/T); single parameter T; before/after reliability; preserves ranking; can't fix complex patterns. Column 2 (Platt scaling): Formula p = σ(az + b); two parameters; handles bias and confidence; assumes logistic. Column 3 (Isotonic regression): Non-parametric monotonic fit; flexible, no assumptions; overfits with limited data. Bottom: Decision guide for method selection.
:::

---

### Figure 23.4: Uncertainty Quantification Methods
Location: Section on UQ methods

::: {#fig-uq-methods}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Method comparison. Deep ensembles: 5 models independently trained; variance/entropy across predictions; 5× training/inference; gold standard for epistemic. MC Dropout: Single model, multiple stochastic passes; variance across dropout samples; 1× training, N× inference; approximates ensemble. Last-layer ensembles: Frozen backbone, ensemble of heads; head disagreement; 1× pretraining, 5× heads (cheap); fine-tuning uncertainty only. Heteroscedastic networks: Single model outputs mean + variance; learned per input; 1× training/inference; aleatoric not epistemic. Comparison table: Epistemic, Aleatoric, Cost, FM-friendly.
:::

---

### Figure 23.5: Conformal Prediction for Variant Classification
Location: Section on conformal prediction

::: {#fig-conformal-prediction}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Workflow with examples. Steps: (1) Calibration: Score variants on held-out set; (2) Threshold: Find threshold for 90% coverage; (3) Prediction sets: Include classes above threshold. Example outputs: High confidence {Pathogenic}, moderate {Pathogenic, VUS}, low {P, VUS, B}, abstention {}. Key properties: Coverage guarantee (≥90% marginal); set size conveys uncertainty; no probability interpretation needed. Visualization: Score distributions; threshold line; set sizes. Limitation: Marginal not conditional coverage.
:::

---

### Figure 23.6: Out-of-Distribution Detection
Location: Section on OOD detection

::: {#fig-ood-detection layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Embedding space visualization. Main panel: UMAP/t-SNE; dense training clusters (blue); isolated OOD points (red); examples (novel archaeal sequence, synthetic protein, variant in poorly characterized gene). Detection methods (side panels): Mahalanobis distance (histogram ID vs OOD, threshold), nearest neighbor distance, ensemble disagreement. Key insight: Flag for manual review rather than automate.
:::

---

### Figure 23.7: Selective Prediction
Location: Section on selective prediction

::: {#fig-selective-prediction}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Accuracy-coverage tradeoff. Main plot: Coverage (x) vs Accuracy (y); curve rising as coverage decreases (more selective = more accurate). Operating point selection: Clinical applications need different tradeoffs. Reject option: High uncertainty → abstain. Example: 90% coverage with 85% accuracy vs 70% coverage with 95% accuracy. Connection to clinical workflow: Rejected variants → expert review.
:::

---

## Chapter 24: Interpretability {#sec-interpretability}

### Figure 24.1: Attribution Methods Comparison
Location: Section on attribution methods

::: {#fig-attribution-comparison}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Attribution methods on same input sequence. Methods: Gradient × Input (fast, noisy), Integrated Gradients (principled, slower), DeepLIFT (reference-based), Attention weights (inspect what model attends), In silico mutagenesis (exhaustive, expensive). Visualization: Heatmaps on same sequence; correlation between methods; areas of agreement/disagreement. Annotations: Compute cost, principled basis, what each reveals.
:::

---

### Figure 24.2: TF-MoDISco Motif Discovery
Location: Section on motif extraction

::: {#fig-tfmodisco}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Motif discovery pipeline. Steps: (1) Attribution scores across many sequences; (2) Cluster high-attribution regions; (3) Align and aggregate into motifs; (4) Match to known databases (JASPAR). Examples: Discovered motif aligned to known TF (CTCF, GATA); novel motifs with unknown biology; composite motifs (TF combinations). Key insight: Bridge between black-box attributions and interpretable biology.
:::

---

### Figure 24.3: Attention Visualization for Genomic Models
Location: Section on attention patterns

::: {#fig-attention-visualization layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel figure. Panel A (Attention heatmap): Position × position; patterns revealing (promoter-enhancer contacts, local structure). Panel B (Biological overlay): Attention on genome browser; peaks align with known regulatory elements. Panel C (Multi-head specialization): Different heads capturing different patterns; local context head, long-range head, motif-specific head. Caveats: Attention ≠ causation; sanity checks needed.
:::

---

### Figure 24.4: In Silico Mutagenesis for Mechanistic Discovery
Location: Section on ISM

::: {#fig-in-silico-mutagenesis layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Four-panel figure. Panel A (ISM procedure): For each position, systematically mutate to all alternatives; compute prediction change; produces position × mutation matrix. Panel B (ISM profile): Heatmap aligned to sequence; functional regions show large effects; silent regions near zero. Panel C (Saturation mutagenesis comparison): ISM predictions vs experimental DMS data; correlation validation. Panel D (Mechanistic insights): ISM reveals: binding site boundaries, position-specific tolerance, allele-specific effects. Note: Computational cost ~L×4 forward passes.
:::

---

### Figure 24.5: Plausible vs. Faithful Explanations
Location: Section on plausibility vs. faithfulness

::: {#fig-plausible-vs-faithful}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Two-path diagram. Scenario: Model predicts high enhancer activity. Path A (Plausible but unfaithful): Attribution highlights GATA motif (biologically reasonable); but model learned GC content correlate; validation fails (mutating GATA doesn't change prediction; inserting GATA doesn't increase); explanation matches intuition not computation. Path B (Faithful): Attribution highlights GATA; validation succeeds (mutating reduces prediction; inserting increases). Validation tests: Necessity (removing reduces?), Sufficiency (adding increases?), Sanity checks (random weights different?). Key distinction: Plausible matches intuition; faithful reflects computation; unfaithful provides false comfort.
:::

---

### Figure 24.6: Validation Pipeline
Location: Section on experimental validation

::: {#fig-validation-pipeline}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Circular workflow. Steps: (1) Model prediction; (2) Interpretability analysis (attribution, TF-MoDISco, attention patterns); (3) Hypothesis generation ("GATA motif drives activity"); (4) Experimental validation (EMSA for binding, reporter for activity, CRISPR for necessity, MPRA for systematic testing); (5) Model refinement (validated → improved training; failed → identify limitations; return to step 1). Example pathways: TF-MoDISco → EMSA ✓; attention enhancer → CRISPR ✓; GC attribution → MPRA no effect ✗ → confounder identified. Key insight: Interpretability advances biology only when closed with validation.
:::

---

### Figure 24.7: Interpretability for Clinical Variant Assessment
Location: Section on clinical applications

::: {#fig-clinical-interpretability}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Clinical workflow integration. ACMG evidence framework: PP3 (computational supports pathogenicity), BP4 (supports benign). Evidence strength depends on interpretability: Weak (score only, 0.85, no mechanism, limited ACMG weight); Moderate (score + attribution: disrupts splice site; SpliceAI supports; can evaluate against transcript data); Strong (score + validated mechanism: disrupts CTCF binding; ChIP confirms; 3D genome shows contact; minigene assay confirms). Clinical report elements: Annotation, score with uncertainty, mechanistic hypothesis, supporting/conflicting evidence, recommended follow-up.
:::

---

# Part VI: Clinical Translation and Frontiers (Chapters 25–29)

## Chapter 25: Clinical Risk Prediction {#sec-clinical-risk}

### Figure 25.1: Feature Integration Architectures
Location: Section on feature integration

::: {#fig-feature-integration layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Three-column comparison. Column 1 (Early Fusion): All features concatenated → single model → risk. Column 2 (Intermediate Fusion): Separate encoders (FM as genomic encoder) → embeddings → fusion → risk. Column 3 (Late Fusion): Independent models → scores → ensemble → risk. For each: pros/cons, missing data handling, compute. Comparison table: Cross-modal interactions, missing data, modularity, best for. Key insight: Intermediate balances modularity with interaction learning.
:::

---

### Figure 25.2: The Validation Hierarchy
Location: Section on validation requirements

::: {#fig-validation-hierarchy}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Pyramid/staircase with evidence levels. Levels bottom to top: (1) Internal validation (CV, temporal splits; low evidence; proof of concept; overfitting risk); (2) External validation (same locked model in independent systems; moderate; transportability; multiple institutions/ancestries); (3) Prospective observational (model runs silently; moderate-high; real-time performance, drift detection; months-years); (4) Prospective interventional (randomized/quasi-experimental; high; clinical outcome improvement; trial registration, IRB). Annotations: Cost/time increasing; regulatory requirements; "Most FM tools stop here" at external validation.
:::

---

### Figure 25.3: Temporal Modeling Architectures
Location: Section on temporal modeling

::: {#fig-temporal-modeling layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel comparison. Panel A (Survival Models): Timeline with events (X) or censoring (O); Cox PH diagram; FM embeddings as static covariates; "10-year CV risk at baseline." Panel B (Longitudinal Models): Repeated measurements over time; time-varying features; FM re-encodes at each timepoint; "Updated prognosis as disease evolves." Panel C (Hybrid/Joint): Baseline genomic risk + trajectory updating; static genomic embedding + dynamic clinical transformer; "Genetic predisposition modified by treatment response."
:::

---

### Figure 25.4: Uncertainty Decomposition in Clinical Predictions
Location: Section on uncertainty quantification

::: {#fig-clinical-uncertainty}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Uncertainty decomposition. Components: (1) Genomic Uncertainty (under-represented ancestry, rare variants, novel genes; detection: embedding distance; response: flag for review); (2) Clinical Uncertainty (extrapolation to new settings; detection: feature distribution monitoring; response: local calibration); (3) Outcome Uncertainty/Aleatoric (biological variability, incomplete penetrance; detection: heteroscedastic models; response: communicate irreducible). Visualization: Venn or stacked bar. Example patient profiles with different compositions. Decision support: When total exceeds threshold → abstain/flag.
:::

---

### Figure 25.5: Fairness and Health Equity Assessment
Location: Section on fairness

::: {#fig-fairness-assessment layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

![**FIGURE PLACEHOLDER D**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20D)

[High] Equity dashboard. Panel A (Performance Disparity): Bar chart AUROC by ancestry; confidence intervals; reference line; highlight underperformance. Panel B (Calibration Disparity): Multiple reliability diagrams overlaid; ECE per group. Panel C (Clinical Utility Disparity): Decision curves by subgroup; net benefit at thresholds; model improves over treat-all/treat-none? Panel D (Access and Outcome Metrics): Who receives testing? Who benefits? Model reduces or amplifies disparities? Mitigation callout: Reweighting, group-wise calibration, expanding sequencing access.
:::

---

### Figure 25.6: Clinical Workflow Integration Patterns
Location: Section on clinical integration

::: {#fig-clinical-workflow}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Workflow diagram. Clinical workflow: Patient presents → Assessment → Decision point → Action. Integration patterns: (1) Laboratory Interpretation Augmentation (FM scores in variant report; human geneticist reviews; variant classification); (2) Risk Embedded in EHR (precomputed scores in structured fields; dashboard at point of care; clinical decision support); (3) Pharmacogenomic Alert (synchronous alert at prescription entry; drug-gene interaction flagged; medication ordering). For each: When computation happens, who sees output, what action triggered. System architecture: Model serving, adapters, logging, version control.
:::

---

### Figure 25.7: Case Study: Cardiometabolic Risk Integration
Location: Case studies section

::: {#fig-cardio-case-study}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Patient journey diagram. Patient profile: 52yo man, LDL 145, BP 138/88, HbA1c 5.9%; family history (father MI at 58); traditional risk 8.2% (below statin threshold). FM integration: DNA FMs annotate variants; polygenic embedding (Delphi/G2PT) captures nonlinear risk; fusion with EHR; updated estimate 11.4% (above threshold). Clinical decision impact: Threshold crossed → statin indicated; pathway attribution → LDL metabolism (supports mechanism); attention attribution → regions for counseling. Validation requirements: External validation, equity analysis. Key insight: Value depends on whether refined estimate enables different action.
:::

---

## Chapter 26: Rare Disease Diagnosis {#sec-rare-disease}

### Figure 26.1: The Variant Prioritization Funnel
Location: Section on variant prioritization

::: {#fig-rare-disease-funnel}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Inverted funnel with filtering stages. Stages with numbers: (1) Raw variants (~25,000); (2) Quality filtered (~22,000); (3) Population frequency filtered (~500-1,000); (4) Consequence filtered (~100-200); (5) Foundation model scored (~20-50); (6) Expert review candidates (~5-10). Annotations: Percentage removed, time/compute cost, where FMs contribute most. Key insight: FMs contribute at scoring stage, after basic filtering, before expert review.
:::

---

### Figure 26.2: ACMG-AMP Evidence Integration
Location: Section on ACMG-AMP criteria

::: {#fig-acmg-amp}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Evidence combination diagram. Columns (evidence categories): Population data, Computational predictions, Functional data, Segregation, De novo, Clinical. Rows (evidence strength): Very Strong (PVS1), Strong, Moderate, Supporting. Combination rules: Pathogenic criteria, Likely Pathogenic, VUS, Likely Benign, Benign. FM contribution highlighted: PP3/BP4 box emphasized; "Traditionally supporting strength"; arrow showing potential upgrade for calibrated predictors. Classification distribution showing VUS dominates.
:::

---

### Figure 26.3: Family-Based Analysis
Location: Section on family-based analysis

::: {#fig-family-analysis layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[High] Three-panel scenarios. Panel A (De Novo Detection): Trio pedigree; variant present in proband, absent in parents; strong evidence (PS2); FM prioritizes among multiple de novos. Panel B (Compound Het Trans): Two variants in same gene from different parents; biallelic disruption; FM assesses severity of each. Panel C (Compound Het Cis): Both from same parent; one functional copy remains; recessive doesn't fit; FM identifies if either alone sufficient. Phasing methods sidebar: Long-read, trio, statistical.
:::

---

### Figure 26.4: Somatic vs. Germline Interpretation
Location: Section on cancer genomics

::: {#fig-somatic-germline layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[High] Two-column comparison. Column 1 (Germline): Present in all cells; question: explains inherited disease?; framework: ACMG-AMP pathogenicity; FM role: functional impact; clinical: genetic counseling, family screening, prevention. Column 2 (Somatic): Acquired in tumor; question: driver? therapy response?; framework: recurrence, functional impact, biomarkers; FM role: driver vs passenger; clinical: treatment selection, prognosis. Key distinctions: Same variant, different implications; BRCA1 example. Practical confusion: Tumor-only sequencing cannot distinguish.
:::

---

### Figure 26.5: Functional Validation Loop
Location: Section on laboratory validation

::: {#fig-functional-validation}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Circular feedback loop. Steps: (1) Computational prediction (FM scores variants); (2) Prioritization for testing (select VUS where functional data resolves); (3) Functional assay (protein function, splicing, regulatory); (4) Result integration (PS3/BS3 evidence; classification update); (5) Model refinement (functional data improves training). Example pathway: AlphaMissense high impact → enzymatic assay → loss confirmed → PS3 → Likely Pathogenic → training data. Key insight: FM predictions are hypotheses; validation definitive but can only test limited variants.
:::

---

### Figure 26.6: The Interpretive Partnership
Location: Chapter conclusion

::: {#fig-interpretive-partnership}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Partnership diagram. FM Capabilities: Pattern recognition at scale, proteome-wide prediction, cross-gene generalization, consistent scoring, speed. Human Expert Capabilities: Clinical context, family reasoning, therapeutic implications, ethical navigation, communication, judgment under uncertainty. Partnership Zone: Efficient prioritization, evidence integration, quality assurance, continuous improvement. What remains human: Final classification, clinical communication, counseling, ethical judgment. Key insight: FMs accelerate diagnostic odyssey; human judgment essential for clinical decisions.
:::

---

## Chapter 27: Drug Discovery {#sec-drug-discovery}

### Figure 27.1: Genetic Evidence to Target Prioritization
Location: Section on target selection

::: {#fig-target-prioritization}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Pipeline diagram. Steps: (1) GWAS summary statistics (Manhattan plot); (2) Fine-mapping (credible sets, posteriors); (3) FM scoring (coding: AlphaMissense, GPN-MSA; regulatory: Enformer, Borzoi); (4) Variant-to-gene mapping (coding direct; noncoding via Hi-C, eQTL, enhancer-gene); (5) Target ranking (genetic evidence, druggability, safety, mechanism clarity). Output: Ranked target list with evidence, effect sizes, fine-mapping probabilities, predicted mechanism, constraint/druggability. Key insight: FMs enrich genetic evidence with mechanistic context.
:::

---

### Figure 27.2: Network-Aware Target Discovery
Location: Section on network approaches

::: {#fig-network-target-discovery}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Network visualization. Nodes: Genes/proteins; colors: GWAS signal strength; sizes: FM embedding similarity to disease genes. Key concepts: (1) Direct GWAS hits (strong statistical evidence); (2) Network neighborhood (connected to hits, may be better targets); (3) Pathway enrichment (multiple signals converge); (4) Bottleneck nodes (druggable connecting disease modules). Repurposing application: Drug targets marked; drugs near disease genes in embedding space → repurposing candidates. Caution: Proximity ≠ causation; MR needed.
:::

---

### Figure 27.3: Drug-Target Interaction Prediction
Location: Section on drug-target prediction

::: {#fig-drug-target-prediction}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Dual-encoder architecture. Components: (1) Target Encoder (protein sequence → ESM-2 → protein embedding capturing structure, function, binding); (2) Molecule Encoder (SMILES/graph → chemical FM → molecule embedding); (3) Interaction Predictor (combine embeddings → predict binding affinity). Applications: Novel target screening, off-target prediction, selectivity profiling. Proteome-scale visualization: 2D protein embeddings; drug binding profile heatmap overlay; intended target and off-targets. Safety integration: Off-targets with CV expression flagged. Key insight: FM embeddings enable binding prediction without experimental structures.
:::

---

### Figure 27.4: Perturb-seq and Perturbation Matching
Location: Section on functional genomics

::: {#fig-perturb-seq}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Perturbation-response workflow. Components: (1) Perturb-seq experiment (pooled CRISPR + scRNA-seq; each cell has perturbation + transcriptome); (2) Perturbation signatures (knockdown → expression profile change; FM learns mapping); (3) Disease signature (patient samples characteristic changes); (4) Perturbation matching (find perturbations reversing disease signature; knockdown X reverses disease → X is candidate; drug Y similar to knockdown X → Y targets X mechanism). Visualization: Expression heatmap (genes × perturbations); disease signature overlay. Lab-in-the-loop: Screen → update model → design next screen; active learning.
:::

---

### Figure 27.5: Biomarker Development Pipeline
Location: Section on biomarker development

::: {#fig-biomarker-pipeline}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Pipeline from features to trial. Stages: (1) FM features (variant embeddings, regulatory predictions, pathway scores; multi-omic); (2) Signature development (supervised learning on retrospective cohorts; predict response, toxicity, progression); (3) Validation (external cohorts, cross-ancestry, calibration); (4) Trial enrichment (select likely responders; smaller trial, higher effect); (5) Companion diagnostic (regulatory pathway; clinical deployment alongside therapy). Example: Genomic + transcriptomic signature predicts PARP inhibitor response; 3× efficiency improvement.
:::

---

## Chapter 28: Sequence Design {#sec-design}

### Figure 28.1: The Design Formalism
Location: Section on design formalism

::: {#fig-design-formalism layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[Essential] Two-direction diagram. Top (Prediction Problem): Input sequence x → model f_θ → property f(x); arrow left to right; "Given sequence, estimate function." Bottom (Design Problem): Desired property y* → search for x* such that f(x*) ≈ y* → optimized sequence x*; arrow right to left; "Given function, find sequence." Design formulations: Optimization argmax f_θ(x), conditional generation x ~ p_θ(x|y), constrained optimization. Scale callout: 20^200 protein possibilities, 4^500 regulatory; "Exhaustive impossible—intelligent search required." FM roles: Generative prior, differentiable oracle, embedding function.
:::

---

### Figure 28.2: Protein Design Strategies
Location: Section on protein design

::: {#fig-protein-design layout-ncol=2}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

[Essential] Two-pathway comparison. Pathway A (Sequence-Based): Protein LM (ProGen, ESM-2) → generate by sampling/infilling → screen for properties → iterate with fitness-guided selection. Pathway B (Structure-Aware): RFdiffusion generates backbone from noise (conditioned on interface, topology, symmetry) → ProteinMPNN/ESM-IF inverse folds → multiple sequences, select by expression/stability. Comparison table: Prior knowledge, novel structures, compute, examples. Multi-objective: Binding, stability, expression, immunogenicity; Pareto frontier; FM oracles for each.
:::

---

### Figure 28.3: Regulatory Sequence Design
Location: Section on regulatory design

::: {#fig-regulatory-design}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Optimization workflow. Steps: (1) Initial sequence (natural promoter or random); (2) FM prediction (Enformer → activity across cell types); (3) Gradient computation (∂expression/∂position); (4) Sequence update (relaxed representation, gradient step, project back); (5) Multi-objective balancing (maximize in target tissue, minimize off-target, respect constraints). Output examples: Cell-type-specific enhancer, inducible promoter, compact element for gene therapy. Generative alternative sidebar: Diffusion or autoregressive; condition on cell type labels; diverse library for screening. Key insight: Same saliency for interpretation runs in reverse for design.
:::

---

### Figure 28.4: mRNA Design Multi-Objective Optimization
Location: Section on mRNA design

::: {#fig-mrna-optimization}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Multi-objective radar chart. Objectives (axes): Translation efficiency, mRNA stability, immunogenicity (minimize), manufacturing tractability, codon optimality. Design elements per objective: Translation (ribosome profiling models, avoid rare codons); Stability (UTR engineering, secondary structure); Immunogenicity (avoid TLR motifs, modified nucleosides); Manufacturing (GC content, complexity, yield). Trade-off visualization: Two candidate designs on same radar; Design A (high translation, moderate stability); Design B (balanced). UTR design callout: 5' affects ribosome recruitment, 3' affects stability/localization. Key insight: Codon synonymy creates vast space; FMs navigate tradeoffs.
:::

---

### Figure 28.5: Closed-Loop Design-Build-Test-Learn
Location: Section on DBTL cycles

::: {#fig-dbtl-cycle}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Essential] Circular workflow. Stages: (1) DESIGN (FM proposes candidates; generative sampling or optimization; active learning selects informative candidates); (2) BUILD (automated synthesis, library construction, QC); (3) TEST (high-throughput assays: binding, activity, stability, expression; multiplexed: DMS, MPRA, Perturb-seq); (4) LEARN (results update model; improve predictions; identify failure modes). Active learning integration: Acquisition function balances exploitation/exploration; maximize expected information gain. Safety and oversight callouts: Safety filters at design; human review before build; stopping criteria. Key insight: FMs achieve full potential in iterative cycles; each round improves molecules and predictions.
:::

---

### Figure 28.6: Antibody Design Pipeline
Location: Section on antibody design

::: {#fig-antibody-design}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Antibody-specific pipeline. Starting point: Initial antibody from immunization/display; known antigen target. Steps: (1) Initial characterization (affinity, specificity, stability, developability); (2) CDR optimization (FM-guided mutations; sample CDR variants; maintain binding, improve developability); (3) Framework engineering (humanization, stability, expression); (4) Lead optimization (multi-objective: affinity, specificity, half-life, immunogenicity, manufacturability). FM contributions: Embedding space identifies similar therapeutic antibodies; structure prediction without experimental structure; developability prediction (aggregation, viscosity); liability scanning (post-translational modification, deamidation).
:::

---

## Chapter 29: Ethics and Frontiers {#sec-future}

### Figure 29.1: Regulatory Pathway Comparison
Location: Section on regulatory frameworks

::: {#fig-regulatory-pathways layout-ncol=3}
![**FIGURE PLACEHOLDER A**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20A)

![**FIGURE PLACEHOLDER B**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20B)

![**FIGURE PLACEHOLDER C**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER%20C)

[Essential] Jurisdiction comparison. Columns: FDA (US), CE-IVD (EU), emerging (China, Japan, others). For each: Pathway (510(k), De Novo, PMA; CE marking; national approval); Evidence requirements; Update policies; Timeline; Key considerations. Complexity factors: Software as a Medical Device (SaMD); foundation models as "substantially equivalent" or novel; continuously learning systems; multi-site deployment. Annotation: Regulatory landscape evolving; early engagement recommended.
:::

---

### Figure 29.2: Dual-Use Governance Framework
Location: Section on dual-use considerations

::: {#fig-dual-use-governance}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Risk assessment matrix. Axes: Capability (what the model can do) × Access (who can use it). Quadrants: Low capability/restricted (current academic); high capability/restricted (industrial deployment with oversight); low capability/open (open-source educational); high capability/open (highest concern). Risk factors: Pathogen design, antibiotic resistance, agricultural biosecurity, emergent capabilities. Governance mechanisms: Pre-release evaluation, staged release, monitoring, audit trails, benefit-risk assessment. Key insight: Balancing open science benefits against misuse risks.
:::

---

### Figure 29.3: Data Governance Challenges
Location: Section on data privacy

::: {#fig-data-governance}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Multi-panel governance challenges. Panel A (Privacy vs. Utility): Anonymized data (limited utility) vs identified data (utility but privacy risk); differential privacy tradeoff curve. Panel B (Consent Complexity): Broad consent, specific consent, dynamic consent, tiered consent; each with implications. Panel C (Federated Learning): Data stays local; model travels; gradient aggregation; privacy-preserving computation. Panel D (Cross-Border Issues): Different jurisdictions with different rules; GDPR, HIPAA, emerging regulations; data localization requirements. Key insight: No perfect solution; governance requires ongoing negotiation between stakeholder interests.
:::

---

### Figure 29.4: Multi-Scale Biological Integration
Location: Section on multi-scale models

::: {#fig-multiscale-integration}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Scale hierarchy visualization. Levels: (1) Nucleotide (base pairs, modifications); (2) Sequence element (motifs, domains, genes); (3) Molecular complex (chromatin, ribonucleoprotein); (4) Cell (transcriptome, proteome, state); (5) Cell population (tissue, heterogeneity); (6) Tissue/Organism (intercellular communication, development). Current model coverage: DNA-LM (nucleotide → gene); Protein models (residue → protein); Single-cell models (cell state). Scale boundary challenges: Arrow indicating information loss at each boundary; hierarchical models emerging; graph networks for relational structure. Key insight: Biology operates across scales; future models must integrate.
:::

---

### Figure 29.5: Agentic and Closed-Loop Systems
Location: Section on emerging directions

::: {#fig-agentic-systems}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[High] Autonomous design cycle with oversight. Cycle components: (1) Generative model (proposes candidates, optimizes toward objective); (2) Safety filter (screen against hazard databases, reject concerning, log for audit); (3) Automated synthesis (DNA/protein production, QC, physical realization); (4) High-throughput assay (functional measurement, multiplexed readouts, data generation); (5) Model update (results improve predictions, refine objective, guide next iteration). Human oversight points: Objective specification (before cycle); periodic review (during); stopping criteria (when to halt); anomaly investigation (if unexpected). Risk management: Containment, audit trails, escalation, kill switches. Key insight: Agentic systems require careful objective specification and monitoring; human oversight essential.
:::

---

### Figure 29.6: Learning Health System Integration
Location: Section on clinical integration

::: {#fig-learning-health-system}
![**FIGURE PLACEHOLDER**](https://placehold.co/600x400?text=FIGURE%20PLACEHOLDER)

[Enhancing] Circular learning system. Components: (1) Clinical deployment (FM informs decisions, predictions reach patients); (2) Outcome observation (what happened? correct/incorrect?); (3) Data aggregation (outcomes linked to predictions, privacy-preserving); (4) Model refinement (updated training data, improved predictions, federated learning); (5) Validation and approval (updated model validated, regulatory approval, return to deployment). Governance at each stage: Who controls learning? How are improvements validated? How are benefits distributed? How are underrepresented populations protected? Multi-site collaboration: Common architecture enables comparison; improvements transfer; accumulate evidence across diverse populations. Key insight: Learning systems create virtuous cycles; governance must ensure benefits reach all equitably.
:::

---

# Summary Statistics

## Figure Counts by Part

| Part | Chapters | Essential | High | Enhancing | Total |
|------|----------|-----------|------|-----------|-------|
| I    | 1-4      | 7         | 11   | 1         | 19    |
| II   | 5-9      | 10        | 12   | 5         | 27    |
| III  | 10-14    | 12        | 11   | 4         | 27    |
| IV   | 15-19    | 10        | 14   | 2         | 26    |
| V    | 20-24    | 10        | 17   | 4         | 31    |
| VI   | 25-29    | 9         | 17   | 4         | 30    |
| **Total** | **29** | **58** | **82** | **20** | **160** |

## Implementation Priority Order

### Essential Figures (58 total) - Create First
Core figures that make chapters complete. See list by chapter above.

### High Priority Figures (82 total) - Create for Complete Coverage
Significantly aid comprehension of core concepts. Strong candidates for inclusion.

### Enhancing Figures (20 total) - Create if Time Permits
Helpful but not critical. Cut first under pressure.

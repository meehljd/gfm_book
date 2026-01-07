# Deep Dive Sidebar Opportunities Report

**Generated**: 2026-01-07

## Summary

After systematically reviewing the book, I identified **47+ opportunities** for "Deep Dive" sidebars—explanatory boxes that explain specialized topics for readers lacking certain background knowledge.

**Three target audiences:**
1. **Genomics/genetics folks** who may not know ML concepts
2. **ML/deep learning folks** who may not know biology/genetics concepts
3. **Clinical/translational researchers** who may not know either domain deeply

---

## Existing Sidebars (Pattern to Follow)

Current deep dive sidebars in the book:
- "Interpreting Constraint Metrics" (ch02) - explains pLI, LOEUF
- "Star-Allele Nomenclature" (ch02) - explains pharmacogenomics notation
- "The VCF Format" (ch01) - explains variant file format
- "Regulatory Genomics Assays: What They Measure" (ch16) - explains ChIP-seq, ATAC-seq, etc.
- "ACMG-AMP Variant Classification Framework" (ch17) - explains clinical classification
- "Computing Variant Likelihoods from Language Models" (ch17) - explains zero-shot scoring
- "Big-O Notation" (ch07) - explains computational complexity
- "AlphaFold: Structure Prediction Without Foundation Models" (ch15) - explains AlphaFold

---

## HIGH PRIORITY Opportunities

### PART 1: Data Foundations

#### Chapter 1: From Reads to Variants

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Types of Sequence Variants** | ML | After intro | Distinguishes SNVs, indels, structural variants, CNVs |
| **PCR and Library Preparation** | ML | Before targeting | Why PCR artifacts matter (duplicates, GC bias) |
| **Mapping Quality Scores** | ML | In alignment section | What MAPQ means, how it differs from base quality |
| **Pair-HMM in Variant Calling** | ML | After per-sample calling | Non-technical explanation of HaplotypeCaller algorithm |
| **Recombination and Genetic Distance** | ML | In phasing section | centiMorgans, LD blocks, why they matter for phasing |

#### Chapter 2: Data Landscape

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Reference Bias** | All | In reference assembly section | Why European reference underdetects African variants |
| **Alternative Splicing** | ML | In gene models section | Why one gene = multiple protein products |
| **Allele Frequency (MAF)** | ML | Before population section | Definition, 1% threshold, clinical importance |
| **ChIP-seq vs ATAC-seq** | ML | In ENCODE section | What each assay measures, how they differ |
| **Selection vs Drift** | ML | After DMS section | Why absent variants aren't always harmful |
| **Cis vs Trans Regulation** | ML | In GTEx section | Why eQTLs act locally |

#### Chapter 3: GWAS and Polygenic Scores

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Multiple Testing Correction** | ML | In linear models | Why 5×10⁻⁸ threshold, Bonferroni correction |
| **Confounding in Observational Studies** | ML | In population structure | Gene-environment correlation problem |
| **Additive vs Non-Additive Effects** | ML | In SNP heritability | Dominance, epistasis, hidden heritability |
| **Haplotype Blocks** | ML | In LD section | Physical distance vs LD decay |
| **Bayesian Fine-Mapping** | ML | After fine-mapping | Prior/posterior interpretation, PIP meaning |

#### Chapter 4: Classical Variant Prediction

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Synonymous vs Nonsynonymous** | ML | Before conservation | Why synonymous changes can affect splicing |
| **Protein Domains and Structure** | ML | In PolyPhen section | Alpha helices, beta sheets, buried vs surface |
| **Loss vs Gain of Function** | All | After mechanism section | Why same variant type has opposite clinical effects |
| **Proxy Labels** | ML | In CADD section | Why evolutionary tolerance ≠ pathogenicity |
| **Calibration vs Discrimination** | ML | After ensemble comparison | Why high auROC doesn't mean calibrated |

### PART 2: Sequence Architectures

#### Chapter 5: Representations

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Translation Equivariance** | Biology | In one-hot section | Why CNN filters detect motifs anywhere |
| **Reading Frames and Codons** | ML | After biological tokenization | Third position wobble, codon families |

#### Chapter 6: Convolutional Networks

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Receptive Field** | Biology | Before DeepSEA | How filter width + pooling determines context |
| **Position Weight Matrices** | ML | In convolutions | What PWMs are, connection to learned filters |
| **Multi-Task Learning** | Biology | After DeepSEA architecture | Why joint training on 919 tasks helps |

#### Chapter 7: Attention & Transformers

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Dot Product Similarity** | Biology | Before self-attention | Why inner product measures alignment |
| **Softmax Function** | Biology | In QKV section | What softmax does, why used for attention |

### PART 3: Foundation Model Families

#### Chapter 13: FM Principles

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Emergent Capabilities** | Biology | In emergence section | What emergence means in ML, why it matters |
| **Scaling Laws** | Biology | In scaling section | Power laws relating model size to performance |

#### Chapter 14: DNA Language Models

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Self-Supervised Learning** | Biology | In paradigm shift section | MLM vs autoregressive, why pretraining works |
| **Reverse Complement Equivariance** | ML | Before Caduceus | Why DNA is double-stranded, strand invariance |

#### Chapter 15: Protein Language Models

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Contact Prediction** | ML | In attention coupling | What protein contacts are, evolutionary coupling |
| **Protein Structure Levels** | ML | Before ESMFold | Primary/secondary/tertiary/quaternary |

#### Chapter 17: Variant Effect Prediction

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Types of Splice Mutations** | ML | In SpliceAI section | Exon skipping, intron retention, cryptic sites |

### PART 4: Systems and Scale

#### Chapter 18: RNA Models

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **RNA Secondary Structure** | ML | In structure challenge | Base pairing, stems, loops, pseudoknots |
| **Codon Optimization** | ML | In codon models | Why codon choice matters for translation |

#### Chapter 19: Single-Cell Models

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Dropout and Sparsity** | Biology | In technical challenges | Why scRNA-seq has zeros, what they mean |
| **Batch Effects** | Both | In practical challenges | Technical vs biological variation |

#### Chapter 20: 3D Genome

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Hi-C Contact Matrices** | ML | In measurement section | What the matrix represents, resolution |
| **CTCF and Cohesin** | ML | In loop extrusion | The molecular machinery of loops |

#### Chapter 21: Network Models

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Message Passing** | Biology | In GNN fundamentals | How information flows in GNNs |
| **Node Embeddings** | Biology | In integration section | What embedding represents |

### PART 5: Evaluation and Trust

#### Chapter 23: Uncertainty

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Epistemic vs Aleatoric** | Both | In uncertainty types | Reducible vs irreducible uncertainty |
| **Conformal Prediction** | Biology | In conformal section | Coverage guarantees without distributional assumptions |

#### Chapter 24: Interpretability

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Attribution Methods** | Biology | In gradient methods | Saliency, integrated gradients, SHAP |
| **Probing Classifiers** | Biology | In probing section | What probes measure about representations |

#### Chapter 25: Causal Inference

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **DAGs and d-separation** | Both | In causal graphs | Visual language for causal relationships |
| **Instrumental Variables** | Both | In MR section | Why genetic variants are valid instruments |

### PART 6: Clinical Translation

#### Chapter 27: Clinical Risk

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Absolute vs Relative Risk** | ML | In risk communication | Clinical interpretation of predictions |
| **Net Reclassification** | ML | In evaluation | NRI, IDI metrics for clinical utility |

#### Chapter 28: Rare Disease

| Topic | Target | Location | Why Needed |
|-------|--------|----------|------------|
| **Phenotype-Driven Prioritization** | ML | In workflow section | HPO terms, phenotype matching |
| **Compound Heterozygosity** | ML | In rare disease | Two different variants, same gene |

---

## MEDIUM PRIORITY

| Topic | Target | Chapters | Why |
|-------|--------|----------|-----|
| **Bayesian Probability** | Both | ch03, ch04, ch23 | Credible intervals, posteriors |
| **Effect Sizes** | Biology | ch03, ch04 | Odds ratios, hazard ratios |
| **Cross-Validation** | Biology | ch11, ch12 | Overfitting detection |
| **Fourier Transforms** | Both | ch14 (HyenaDNA) | FFT-based convolutions |

---

## Implementation Format

Use existing callout pattern:

```markdown
::: {.callout-note title="Deep Dive: Linkage Disequilibrium"}
**For ML readers:** Linkage disequilibrium (LD) describes the non-random association of alleles at nearby loci...

[1-2 paragraphs explaining the concept]
[Why it matters for this chapter's content]
:::
```

---

## Summary Statistics

- **Total HIGH priority**: 42 sidebars
- **Total MEDIUM priority**: 8 sidebars
- **Recommended implementation order**: Part 1 → Part 2 → Part 3 → Parts 4-6

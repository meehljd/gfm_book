# Cross-Reference Proposals for Genomic Foundation Models

This document proposes specific cross-references to strengthen navigation and identify related concepts across the book. Organized by chapter with both backward and forward reference opportunities.

## Principles Applied

1. **Section-specific over chapter-level**: Use `@sec-specific-section` rather than "Chapter X"
2. **Back-references from applications to foundations**: Clinical chapters reference evaluation/methodology
3. **Concept threading**: Track recurring themes (calibration, transfer, confounding)
4. **Redundancy detection**: Flag where similar concepts appear in multiple places

---

## Part I: Data Foundations

### Chapter 1: From Reads to Variants

**Current forward references need section specificity:**
- References to evaluation → Should specify `@sec-ch21-homology-aware-splitting` when discussing benchmark construction
- References to DeepVariant comparison → Should point to specific CNN sections in `@sec-ch06-cnn`

**Proposed back-references (for later writing):**
None - this is foundational

**Proposed forward references to add:**

In `@sec-ch01-deepvariant`:
- "The representational approach here anticipates the embedding strategies in `@sec-ch05-embeddings`"
- "DeepVariant's CNN architecture shares design principles with `@sec-ch06-deepsea`, though applied to different input modalities"
- Connection to transfer learning: "The domain-specific training here contrasts with foundation model approaches discussed in `@sec-ch10-defining`"

In `@sec-ch01-phasing-importance`:
- Forward to `@sec-ch26-compound-het` for clinical stakes of compound heterozygosity
- Connection to graph methods: "Network-based phasing approaches connect to `@sec-ch18-biological-networks`"

In `@sec-ch01-benchmarks`:
- Strong connection to `@sec-ch20-benchmarks` (should be section-specific to GIAB discussion)
- Reference `@sec-ch21-metrics-genomic-tasks` for deeper metrics discussion
- "Benchmark limitations discussed here recur in `@sec-ch20-benchmark-construction`"

In `@sec-ch01-difficult`:
- "These regions create systematic challenges for foundation model evaluation, discussed in `@sec-ch21-homology-aware-splitting`"
- HLA complexity → `@sec-ch18-biological-networks` for network approaches
- "Segmental duplication challenges motivate long-read approaches in `@sec-ch01-longread` and long-context models in `@sec-ch11-long-context`"

**Redundancy watch:**
- Variant calling quality metrics appear here and in Ch 21 - ensure consistent terminology
- Benchmark discussion overlaps with Ch 20 - consider what belongs where

---

### Chapter 2: Data Landscape

**Current forward references need section specificity:**
- References to models using these resources → Make section-specific (ENCODE to `@sec-ch13-enformer-training`, gnomAD to `@sec-ch14-dna-vep`)

**Proposed back-references:**
In `@sec-ch02-gnomad`:
- "Population frequency filtering discussed in `@sec-ch01-classical` relies on gnomAD"
- "Allele frequencies from gnomAD provide critical filters in `@sec-ch26-frequency-filters`"

In `@sec-ch02-clinvar`:
- "Clinical assertions here become training labels in `@sec-ch04-cadd` and evaluation benchmarks in `@sec-ch20-clinical-databases`"
- "ClinVar's role in ACMG criteria detailed in `@sec-ch26-acmg-amp`"
- "Calibration to ClinVar discussed in `@sec-ch14-acmg-mapping`"

In `@sec-ch02-phenotypes`:
- "The phenotype quality issues raised here create confounding discussed in `@sec-ch22-label-bias`"
- "Deep phenotyping approaches connect to `@sec-ch03-deep-phenotyping` and EHR integration in `@sec-ch25-ehr-integration`"

**Proposed forward references to add:**

In `@sec-ch02-encode`:
- "These functional assays provide training data for `@sec-ch06-deepsea`, `@sec-ch13-enformer`, and other regulatory models"
- "Chromatin accessibility predictions discussed in `@sec-ch13-enformer-architecture`"

In `@sec-ch02-gwas-summary`:
- Specific connection to `@sec-ch03-gwas-framework` for how these arise
- "Summary statistics power polygenic scores in `@sec-ch03-pgs-construction`"

In `@sec-ch02-label-noise`:
- "Label noise creates training challenges discussed in `@sec-ch08-diagnostics`"
- "Mitigation strategies in `@sec-ch22-mitigation`"
- "Impact on calibration discussed in `@sec-ch23-fm-miscalibration`"

**Redundancy watch:**
- ClinVar appears here, Ch 4 (CADD training), Ch 14 (VEP evaluation), Ch 20 (benchmarks), Ch 26 (clinical workflow)
- Phenotype quality appears here and Ch 3 (GWAS), Ch 22 (confounding), Ch 25 (risk prediction)
- **Recommendation**: Ch 2 should be the authoritative source; other chapters give brief context + cross-reference

---

### Chapter 3: GWAS and Polygenic Scores

**Proposed back-references:**

In `@sec-ch03-gwas-framework`:
- "GWAS summary statistics cataloged in `@sec-ch02-gwas-summary`"
- "Variant calling quality from `@sec-ch01-classical` affects association power"

In `@sec-ch03-ld`:
- "Reference panels from `@sec-ch02-1000genomes` and `@sec-ch02-gnomad` enable LD calculation"
- "Fine-mapping connects to `@sec-ch14-fm-paradigm` for functional priors"

In `@sec-ch03-portability`:
- "Population structure issues introduced in `@sec-ch02-population` manifest as portability challenges"
- "Systematic analysis in `@sec-ch22-ancestry-confounding`"
- "Training data diversity discussed in `@sec-ch02-constraints`"

In `@sec-ch03-deep-phenotyping`:
- "Deep phenotyping approaches from `@sec-ch02-deep-phenotyping`"
- "EHR embeddings detailed in `@sec-ch25-ehr-integration`"

**Proposed forward references to add:**

In `@sec-ch03-pgs-construction`:
- "Integration with foundation model features discussed in `@sec-ch25-pgs-to-fm`"
- "Feature extraction from genomic models in `@sec-ch09-feature-extraction`"

In `@sec-ch03-relative-risk`:
- "Clinical risk prediction frameworks in `@sec-ch25-defining-risk`"
- "Calibration requirements for deployment in `@sec-ch23-calibration` and `@sec-ch25-calibration`"

In `@sec-ch03-prs-phewas`:
- "PRS-PheWAS for clinical interpretation detailed in `@sec-ch25-prs-phewas`"

**Redundancy watch:**
- PheWAS appears here and in Ch 25 - ensure consistent framework
- Portability/fairness appears here and Ch 22, Ch 25 - check for redundant discussion
- **Recommendation**: Ch 3 focuses on GWAS/PGS context, Ch 25 on clinical deployment

---

### Chapter 4: Classical Variant Prediction

**Proposed back-references:**

In `@sec-ch04-conservation`:
- "Variant calling from `@sec-ch01-classical` produces the variants scored here"
- "Population frequencies from `@sec-ch02-gnomad` provide context for constraint metrics"

In `@sec-ch04-cadd`:
- "Training on ClinVar from `@sec-ch02-clinvar`"
- "Evolutionary proxy problem contrasts with supervised approaches in `@sec-ch14-fm-paradigm`"

In `@sec-ch04-circularity`:
- "Ascertainment bias in sequencing discussed in `@sec-ch01-difficult`"
- "Systematic treatment in `@sec-ch22-label-circularity`"

**Proposed forward references to add:**

In `@sec-ch04-protein-predictors`:
- "Protein language models in `@sec-ch12-esm-family` provide alternative approaches"
- "ESM-based variant scoring in `@sec-ch14-protein-vep`"

In `@sec-ch04-cadd-features`:
- "Contrast with learned representations in `@sec-ch05-embeddings` and `@sec-ch09-feature-extraction`"
- "Feature ceiling problem motivates foundation model approaches in `@sec-ch10-task-specific`"

In `@sec-ch04-ensemble-methods`:
- "Ensemble principles connect to deep ensembles for uncertainty in `@sec-ch23-deep-ensembles`"
- "Integration strategies in `@sec-ch14-combining-evidence`"

In `@sec-ch04-features-to-representations`:
- "Embedding-based approaches in `@sec-ch05-embeddings`"
- "Zero-shot scoring paradigm in `@sec-ch14-zeroshot-supervised`"

**Redundancy watch:**
- ACMG criteria mentioned here and detailed in Ch 26 - consider forward reference rather than full explanation
- Circularity discussed here and in Ch 22 - Ch 22 should be comprehensive, this should preview

---

## Part II: Sequence Architectures

### Chapter 5: Tokens and Embeddings

**Proposed back-references:**

In `@sec-ch05-embeddings`:
- "Contrast with hand-crafted features in `@sec-ch04-cadd-features`"
- "DeepVariant's image representation in `@sec-ch01-pileup` uses implicit positional encoding"

In `@sec-ch05-variant-interpretation`:
- "Variant calling resolution from `@sec-ch01-classical`"
- "Requirements for scoring rare variants from `@sec-ch04-protein-boundaries`"

**Proposed forward references to add:**

In `@sec-ch05-onehot`:
- "CNN architectures in `@sec-ch06-convolutions` operate on one-hot encoded sequences"
- "Comparison to learned embeddings in `@sec-ch05-embeddings`"

In `@sec-ch05-kmer`:
- "DNABERT implementation in `@sec-ch11-dnabert`"
- "K-mer embeddings in protein models like `@sec-ch12-esm1b`"

In `@sec-ch05-bpe`:
- "Nucleotide Transformer's vocabulary in `@sec-ch11-nucleotide-transformer`"
- "Protein tokenization in `@sec-ch12-esm-family`"

In `@sec-ch05-position`:
- "Positional encodings in transformers detailed in `@sec-ch07-positional-encoding`"
- "Genomic position considerations in `@sec-ch07-genomic-position`"

**Redundancy watch:**
- Position encoding appears here and Ch 7 - Ch 7 should have implementation details, this should introduce concept
- Tokenization appears here and in individual model chapters - ensure consistent terminology

---

### Chapter 6: Convolutional Networks

**Proposed back-references:**

In `@sec-ch06-deepsea`:
- "Training data from ENCODE discussed in `@sec-ch02-encode`"
- "Variant effect prediction builds on principles from `@sec-ch04-protein-predictors`"
- "One-hot encoding from `@sec-ch05-onehot`"

In `@sec-ch06-spliceai`:
- "Splicing mutations discussed in `@sec-ch01-complex`"
- "Clinical deployment anticipates frameworks in `@sec-ch26-workflow`"

**Proposed forward references to add:**

In `@sec-ch06-receptive-field`:
- "Attention mechanisms in `@sec-ch07-self-attention` resolve this limitation"
- "Long-context models in `@sec-ch11-long-context` achieve megabase receptive fields"
- "Enformer's hybrid approach in `@sec-ch13-enformer-architecture`"

In `@sec-ch06-deepsea-vep`:
- "Foundation model approaches to regulatory variant scoring in `@sec-ch14-enformer-vep`"
- "Integration with clinical workflows in `@sec-ch26-fm-scoring`"

In `@sec-ch06-spliceai-clinical`:
- "Clinical integration discussed in `@sec-ch26-workflow`"
- "Calibration for ACMG criteria in `@sec-ch14-acmg-mapping`"

In `@sec-ch06-specialization`:
- "Foundation model paradigm in `@sec-ch10-task-specific` addresses this limitation"
- "Multi-task pretraining in `@sec-ch08-multitask` as alternative approach"

**Redundancy watch:**
- Variant effect prediction mechanics appear here and Ch 14 - ensure clear division (CNNs vs FMs)
- Receptive field discussion may overlap with Ch 7 attention motivation

---

### Chapter 7: Transformers and Attention

**Proposed back-references:**

In `@sec-ch07-self-attention`:
- "Addresses receptive field limitations from `@sec-ch06-receptive-field`"
- "Contrast with convolutional sequence scanning in `@sec-ch06-deepsea`"
- "Sequential bottleneck from `@sec-ch06-sequential-bottleneck`"

In `@sec-ch07-positional-encoding`:
- "Position embedding concepts from `@sec-ch05-position`"

**Proposed forward references to add:**

In `@sec-ch07-multihead`:
- "Multi-head attention in DNABERT (`@sec-ch11-dnabert`) and ESM (`@sec-ch12-esm-family`)"
- "Attention pattern analysis in `@sec-ch24-attention`"

In `@sec-ch07-genomic-position`:
- "Genomic coordinate encoding in `@sec-ch13-enformer-architecture`"
- "Position-aware models in `@sec-ch11-nucleotide-transformer`"

In `@sec-ch07-quadratic-barrier`:
- "Long-context solutions in `@sec-ch11-hyenadna` and `@sec-ch11-caduceus`"
- "Efficient attention in regulatory models `@sec-ch13-enformer-architecture`"

In `@sec-ch07-encoder-only`:
- "DNABERT and BERT-style pretraining in `@sec-ch11-dnabert`"
- "ESM protein models in `@sec-ch12-esm-family`"

In `@sec-ch07-ssm`:
- "HyenaDNA implementation in `@sec-ch11-hyenadna`"
- "Mamba-based Caduceus in `@sec-ch11-caduceus`"

**Redundancy watch:**
- Position encoding details may overlap with Ch 5
- Computational complexity appears here and in specific model chapters

---

### Chapter 8: Pretraining Strategies

**Proposed back-references:**

In `@sec-ch08-mlm`:
- "Tokenization choices from `@sec-ch05-kmer` affect masking strategies"
- "Embedding initialization from `@sec-ch05-embeddings`"

In `@sec-ch08-data`:
- "Reference genomes from `@sec-ch02-reference`"
- "Population diversity considerations from `@sec-ch02-constraints`"

**Proposed forward references to add:**

In `@sec-ch08-mlm`:
- "DNABERT's masked token approach in `@sec-ch11-dnabert`"
- "ESM-2's masked language modeling in `@sec-ch12-esm2`"

In `@sec-ch08-autoregressive`:
- "Caduceus bidirectional processing in `@sec-ch11-caduceus`"
- "Evo 2's autoregressive generation in `@sec-ch11-evo2`"

In `@sec-ch08-multitask`:
- "Enformer's multi-task learning in `@sec-ch13-enformer-training`"
- "Borzoi's coverage prediction tasks in `@sec-ch13-borzoi`"

In `@sec-ch08-probing`:
- "Systematic probing analysis in `@sec-ch09-probing-representations`"
- "What models learn discussed in `@sec-ch11-probing`"

In `@sec-ch08-dnabert`:
- "Full model details in `@sec-ch11-dnabert`"

In `@sec-ch08-enformer`:
- "Full model details in `@sec-ch13-enformer`"

In `@sec-ch08-esm2`:
- "Full model details in `@sec-ch12-esm2`"

**Redundancy watch:**
- Case studies here overlap with detailed model chapters - keep brief here, detailed there
- Probing methodology appears here and Ch 9 - Ch 9 should be comprehensive

---

### Chapter 9: Transfer and Adaptation

**Proposed back-references:**

In `@sec-ch09-source-target`:
- "Pretraining objectives from `@sec-ch08-pretraining`"
- "Foundation model definition from `@sec-ch10-defining`"

In `@sec-ch09-probing-representations`:
- "Probing during pretraining from `@sec-ch08-probing`"
- "Position encoding effects from `@sec-ch07-positional-encoding`"

In `@sec-ch09-domain-shift-types`:
- "Population structure from `@sec-ch02-population`"
- "Systematic shift analysis in `@sec-ch22-domain-shift`"

**Proposed forward references to add:**

In `@sec-ch09-linear-probing`:
- "Linear probing for evaluation in `@sec-ch21-linear-probing`"
- "Protein model probing in `@sec-ch12-emergent-knowledge`"

In `@sec-ch09-lora`:
- "Parameter-efficient fine-tuning in clinical applications `@sec-ch25-feature-integration`"
- "Adapter usage in domain adaptation `@sec-ch22-domain-adaptation`"

In `@sec-ch09-validation-pitfalls`:
- "Comprehensive evaluation framework in `@sec-ch21-eval`"
- "Leakage detection in `@sec-ch21-leakage-detection`"
- "Confounding analysis in `@sec-ch22-detection`"

In `@sec-ch09-case-dnabert`:
- "DNABERT architecture in `@sec-ch11-dnabert`"

In `@sec-ch09-case-esm`:
- "ESM variant scoring in `@sec-ch14-protein-vep`"

In `@sec-ch09-case-enformer`:
- "Enformer details in `@sec-ch13-enformer`"

**Redundancy watch:**
- Domain shift appears here and Ch 22 - ensure clear division (transfer context vs confounding analysis)
- Validation pitfalls overlap with Ch 21 - cross-reference rather than duplicate

---

## Part III: Foundation Model Families

### Chapter 10: Foundation Model Paradigm

**Proposed back-references:**

In `@sec-ch10-task-specific`:
- "CNN limitations from `@sec-ch06-specialization`"
- "Feature engineering ceiling from `@sec-ch04-feature-ceiling`"

In `@sec-ch10-scaling`:
- "Training objectives from `@sec-ch08-optimization`"
- "Computational considerations from `@sec-ch07-memory`"

**Proposed forward references to add:**

In `@sec-ch10-dna-lm`:
- "Detailed in Chapter 11 (`@sec-ch11-dna-lm`)"
- "DNABERT as exemplar in `@sec-ch11-dnabert`"

In `@sec-ch10-seq-to-func`:
- "Regulatory models in Chapter 13 (`@sec-ch13-regulatory`)"
- "Enformer details in `@sec-ch13-enformer`"

In `@sec-ch10-vep-models`:
- "Variant effect prediction in Chapter 14 (`@sec-ch14-vep-fm`)"
- "Integration strategies in `@sec-ch14-combining-evidence`"

In `@sec-ch10-evaluation`:
- "Benchmark landscape in `@sec-ch20-benchmarks`"
- "Evaluation principles in `@sec-ch21-eval`"

In `@sec-ch10-use-existing`:
- "Transfer strategies in `@sec-ch09-transfer`"
- "Fine-tuning guidance in `@sec-ch09-choosing-strategy`"

**Redundancy watch:**
- Taxonomy of models appears here and gets detailed in Chapters 11-14
- **Recommendation**: This chapter provides framework, subsequent chapters provide details

---

### Chapter 11: DNA Language Models

**Proposed back-references:**

In `@sec-ch11-task-specific-to-general`:
- "CNN approaches from `@sec-ch06-cnn`"
- "Task-specific limitations from `@sec-ch10-task-specific`"

In `@sec-ch11-dnabert`:
- "K-mer tokenization from `@sec-ch05-kmer`"
- "Masked language modeling from `@sec-ch08-mlm`"
- "Transfer learning framework from `@sec-ch09-transfer`"

In `@sec-ch11-long-context`:
- "Quadratic attention barrier from `@sec-ch07-quadratic-barrier`"
- "Context length challenges from `@sec-ch10-context-length`"

**Proposed forward references to add:**

In `@sec-ch11-embeddings`:
- "Feature extraction for clinical models in `@sec-ch25-feature-integration`"
- "GNN node features in `@sec-ch18-fm-embeddings`"
- "Representation analysis in `@sec-ch24-probing`"

In `@sec-ch11-zero-shot`:
- "Zero-shot variant scoring in `@sec-ch14-zeroshot-plm`"
- "Clinical integration in `@sec-ch26-fm-scoring`"

In `@sec-ch11-probing`:
- "Systematic probing methods from `@sec-ch09-probing-representations`"
- "Interpretability analysis in `@sec-ch24-probing`"

In `@sec-ch11-benchmark-suites`:
- "Benchmark discussion in `@sec-ch20-dna-benchmarks`"
- "Evaluation principles from `@sec-ch21-eval`"

**Redundancy watch:**
- Pretraining details overlap with Ch 8 - keep model-specific here
- Benchmark discussion overlaps with Ch 20 - focus on model performance here

---

### Chapter 12: Protein Language Models

**Proposed back-references:**

In `@sec-ch12-esm1b`:
- "Masked language modeling from `@sec-ch08-mlm`"
- "Transformer architecture from `@sec-ch07-transformer-block`"

In `@sec-ch12-variant-effects`:
- "Classical predictors from `@sec-ch04-protein-predictors`"
- "Zero-shot paradigm from `@sec-ch09-zero-shot`"

**Proposed forward references to add:**

In `@sec-ch12-emergent-knowledge`:
- "Probing analysis methods from `@sec-ch24-probing`"
- "Attention pattern interpretation in `@sec-ch24-attention`"

In `@sec-ch12-esm2`:
- "Scaling laws from `@sec-ch10-scaling`"

In `@sec-ch12-variant-effects`:
- "Integration with DNA models in `@sec-ch14-combining-evidence`"
- "Clinical workflow in `@sec-ch26-fm-scoring`"
- "AlphaMissense comparison in `@sec-ch14-alphamissense`"

In `@sec-ch12-function-prediction`:
- "Network integration in `@sec-ch18-drug-target`"
- "Drug discovery applications in `@sec-ch27-dti-prediction`"

In `@sec-ch12-lessons`:
- "Application to DNA models in Chapters 11 and 13"
- "Design principles inform `@sec-ch28-protein-design`"

**Redundancy watch:**
- Variant effect prediction overlaps with Ch 14 - focus on PLM-specific approaches here
- Lessons section may duplicate content from Ch 10

---

### Chapter 13: Regulatory Models

**Proposed back-references:**

In `@sec-ch13-long-range`:
- "CNN receptive field limits from `@sec-ch06-receptive-field`"
- "Attention solutions from `@sec-ch07-self-attention`"

In `@sec-ch13-enformer`:
- "Hybrid CNN-transformer from `@sec-ch07-hybrid`"
- "Multi-task training from `@sec-ch08-multitask`"
- "ENCODE data from `@sec-ch02-encode`"

In `@sec-ch13-enformer-vep`:
- "Variant calling from `@sec-ch01-classical`"
- "Classical regulatory predictors from `@sec-ch06-deepsea-vep`"

**Proposed forward references to add:**

In `@sec-ch13-enformer-vep`:
- "Integration with other VEP approaches in `@sec-ch14-enformer-vep`"
- "Clinical deployment in `@sec-ch26-fm-scoring`"

In `@sec-ch13-multitask`:
- "Multi-task evaluation in `@sec-ch21-evaluating-fm`"
- "Multi-omic integration principles from `@sec-ch19-multi-omics`"

In `@sec-ch13-interpretability`:
- "Systematic interpretation in `@sec-ch24-attention`"
- "Attribution methods in `@sec-ch24-attribution`"

In `@sec-ch13-foundation-models`:
- "Foundation model criteria from `@sec-ch10-defining`"
- "Comparison to general DNA LMs in `@sec-ch11-dna-lm`"

**Redundancy watch:**
- Variant effect prediction overlaps with Ch 14 - focus on regulatory-specific aspects
- Multi-task training overlaps with Ch 8 - reference rather than re-explain

---

### Chapter 14: Variant Effect Prediction

**Proposed back-references:**

In `@sec-ch14-fm-paradigm`:
- "Classical approaches from Chapter 4 (`@sec-ch04-vep-classical`)"
- "Foundation model definition from `@sec-ch10-defining`"

In `@sec-ch14-zeroshot-plm`:
- "ESM models from `@sec-ch12-esm-family`"
- "Zero-shot transfer from `@sec-ch09-zero-shot`"

In `@sec-ch14-spliceai`:
- "SpliceAI architecture from `@sec-ch06-spliceai`"

In `@sec-ch14-enformer-vep`:
- "Enformer model from `@sec-ch13-enformer`"

In `@sec-ch14-dna-lm-vep`:
- "GPN from `@sec-ch11-gpn`"
- "Evo 2 from `@sec-ch11-evo2`"

**Proposed forward references to add:**

In `@sec-ch14-combining-evidence`:
- "Multi-omic integration principles from `@sec-ch19-multi-omics`"
- "Clinical integration workflow in `@sec-ch26-workflow`"

In `@sec-ch14-calibration`:
- "Calibration methods detailed in `@sec-ch23-calibration`"
- "Clinical calibration requirements in `@sec-ch25-calibration`"

In `@sec-ch14-acmg-mapping`:
- "ACMG framework from `@sec-ch04-conservation-clinical-gap`"
- "Clinical workflow in `@sec-ch26-acmg-amp`"

In `@sec-ch14-uncertainty`:
- "Comprehensive UQ methods in `@sec-ch23-uq-methods`"
- "Clinical uncertainty communication in `@sec-ch23-communication`"

In `@sec-ch14-clinical-integration`:
- "Detailed clinical workflows in `@sec-ch26-workflow`"
- "Regulatory frameworks in `@sec-ch29-validation`"

**Redundancy watch:**
- Calibration appears here, Ch 21, Ch 23, Ch 25 - ensure hierarchy is clear
- ACMG criteria appear here and Ch 26 - Ch 26 should have full workflow, this focuses on model scoring
- **Recommendation**: Ch 14 covers VEP-specific calibration/integration, Ch 23 comprehensive UQ, Ch 25 clinical deployment

---

## Part IV: Systems and Scale

### Chapter 15: RNA Structure and Function

**Proposed back-references:**

In `@sec-ch15-structure-challenge`:
- "Contrast with DNA sequence modeling from `@sec-ch11-dna-lm`"
- "Position encoding challenges from `@sec-ch07-positional-encoding`"

In `@sec-ch15-foundation`:
- "Scaling laws from `@sec-ch10-scaling`"
- "Pretraining strategies from `@sec-ch08-pretraining`"

**Proposed forward references to add:**

In `@sec-ch15-codon`:
- "mRNA design applications in `@sec-ch28-mrna-design`"

In `@sec-ch15-utr-design`:
- "Therapeutic mRNA design in `@sec-ch28-utr-design`"
- "COVID vaccine lessons in `@sec-ch28-covid-vaccines`"

In `@sec-ch15-splicing`:
- "Splice variant interpretation in clinical workflow `@sec-ch26-workflow`"

**Redundancy watch:**
- Splicing overlaps with Ch 6 (SpliceAI) - ensure clear division
- mRNA design appears here and Ch 28 - Ch 28 comprehensive, this previews

---

### Chapter 16: Single-Cell Models

**Proposed back-references:**

In `@sec-ch16-geneformer`:
- "Transformer architecture from `@sec-ch07-transformer-block`"
- "Gene expression data from `@sec-ch02-gtex`"

In `@sec-ch16-perturbation`:
- "Functional screens from `@sec-ch02-dms`"

**Proposed forward references to add:**

In `@sec-ch16-perturb-seq`:
- "Drug discovery screens in `@sec-ch27-functional-screens`"
- "Design-build-test loops in `@sec-ch28-dbtl`"

In `@sec-ch16-batch-effects`:
- "Technical confounding in `@sec-ch22-batch-effects`"
- "Mitigation strategies in `@sec-ch22-mitigation`"

In `@sec-ch16-evaluation`:
- "Evaluation principles from `@sec-ch21-eval`"
- "Benchmark construction in `@sec-ch20-benchmark-construction`"

**Redundancy watch:**
- Batch effects appear here and Ch 22 - cross-reference to avoid duplication

---

### Chapter 17: 3D Genome Organization

**Proposed back-references:**

In `@sec-ch17-hic-matrices`:
- "Data resources from `@sec-ch02-functional`"

In `@sec-ch17-3d-prediction`:
- "CNN architectures from `@sec-ch06-cnn`"
- "Multi-task training from `@sec-ch08-multitask`"

**Proposed forward references to add:**

In `@sec-ch17-sv-interpretation`:
- "Structural variant clinical interpretation in `@sec-ch26-workflow`"

In `@sec-ch17-spatial-models`:
- "Multi-modal integration from `@sec-ch19-clinical-integration`"

In `@sec-ch17-3d-interpretability`:
- "Attribution methods from `@sec-ch24-attribution`"

**Redundancy watch:**
- Multi-task training overlaps with Ch 8 and 13

---

### Chapter 18: Graph and Network Models

**Proposed back-references:**

In `@sec-ch18-fm-embeddings`:
- "Foundation model embeddings from `@sec-ch09-feature-extraction`"
- "DNA model embeddings from `@sec-ch11-embeddings`"
- "Protein model embeddings from `@sec-ch12-esm2`"

In `@sec-ch18-study-bias`:
- "Network bias from `@sec-ch02-functional`"
- "Confounding analysis from `@sec-ch22-detection`"

**Proposed forward references to add:**

In `@sec-ch18-disease-gene`:
- "Clinical prioritization in `@sec-ch26-prioritization-funnel`"

In `@sec-ch18-drug-target`:
- "Drug discovery workflows in `@sec-ch27-dti-prediction`"

In `@sec-ch18-kg-reasoning`:
- "Drug repurposing in `@sec-ch27-repurposing`"

**Redundancy watch:**
- Study bias overlaps with Ch 22 confounding

---

### Chapter 19: Multi-Omics Integration

**Proposed back-references:**

In `@sec-ch19-clinical-integration`:
- "EHR data from `@sec-ch02-ehr`"
- "Phenotype quality from `@sec-ch02-phenotypes`"

In `@sec-ch19-batch-effects`:
- "Technical confounding from `@sec-ch22-batch-effects`"

**Proposed forward references to add:**

In `@sec-ch19-clinical-integration`:
- "Risk prediction workflows in `@sec-ch25-feature-integration`"
- "Clinical deployment in `@sec-ch25-clinical-integration`"

In `@sec-ch19-missing-modalities`:
- "Uncertainty quantification in `@sec-ch23-uq-methods`"

In `@sec-ch19-evaluation`:
- "Multi-task evaluation from `@sec-ch21-evaluating-fm`"
- "Benchmark construction in `@sec-ch20-benchmark-construction`"

**Redundancy watch:**
- Batch effects appear in Ch 16, 22, and here
- Clinical integration overlaps with Ch 25

---

## Part V: Evaluation and Trust

### Chapter 20: Benchmarks

**Proposed back-references:**

In `@sec-ch20-clinical-databases`:
- "ClinVar from `@sec-ch02-clinvar`"
- "Variant calling benchmarks from `@sec-ch01-benchmarks`"

In `@sec-ch20-dna-benchmarks`:
- "Regulatory assays from `@sec-ch02-encode`"
- "Model evaluation from Chapters 11 and 13"

In `@sec-ch20-vep-benchmarks`:
- "Classical VEP from Chapter 4"
- "Foundation model VEP from Chapter 14"

**Proposed forward references to add:**

In `@sec-ch20-benchmark-construction`:
- "Evaluation principles in `@sec-ch21-eval`"
- "Leakage detection in `@sec-ch21-leakage-detection`"

In `@sec-ch20-saturation`:
- "Metric ceiling in `@sec-ch21-metrics-genomic-tasks`"

In `@sec-ch20-deployment-gap`:
- "Clinical deployment in `@sec-ch25-evaluation`"
- "Domain shift in `@sec-ch22-domain-shift`"

**Redundancy watch:**
- Benchmark construction principles overlap with Ch 21
- **Recommendation**: Ch 20 catalogs benchmarks, Ch 21 provides evaluation methodology

---

### Chapter 21: Evaluation Principles

**Proposed back-references:**

In `@sec-ch21-random-splits-fail`:
- "Homology issues from `@sec-ch01-mapping-bias`"
- "Population structure from `@sec-ch02-population`"

In `@sec-ch21-leakage-detection`:
- "Data sharing across resources from `@sec-ch02-constraints`"
- "Benchmark overlap from `@sec-ch20-leakage-scale`"

In `@sec-ch21-calibration`:
- "Clinical calibration needs from `@sec-ch14-calibration`"

**Proposed forward references to add:**

In `@sec-ch21-homology-aware-splitting`:
- "Applied to confounding analysis in `@sec-ch22-data-splitting`"

In `@sec-ch21-metrics-genomic-tasks`:
- "Clinical utility metrics in `@sec-ch25-clinical-utility`"
- "Uncertainty metrics in `@sec-ch23-measuring-calibration`"

In `@sec-ch21-evaluating-fm`:
- "Uncertainty quantification in `@sec-ch23-uq-methods`"
- "Calibration methods in `@sec-ch23-post-hoc-calibration`"

In `@sec-ch21-calibration`:
- "Comprehensive calibration in `@sec-ch23-calibration`"
- "Clinical calibration in `@sec-ch25-calibration`"

**Redundancy watch:**
- Splitting strategies appear here and Ch 22
- Calibration appears here, Ch 14, Ch 23, Ch 25
- **Recommendation**: Ch 21 covers evaluation methodology, Ch 22 focuses on confounding detection, Ch 23 on uncertainty

---

### Chapter 22: Confounders and Leakage

**Proposed back-references:**

In `@sec-ch22-ancestry-confounding`:
- "Population structure from `@sec-ch02-population` and `@sec-ch03-population-structure`"
- "Portability challenges from `@sec-ch03-portability`"

In `@sec-ch22-batch-effects`:
- "Technical artifacts from `@sec-ch01-artifacts`"
- "Single-cell batch effects from `@sec-ch16-batch-effects`"
- "Multi-omic batch effects from `@sec-ch19-batch-effects`"

In `@sec-ch22-label-bias`:
- "ClinVar assertions from `@sec-ch02-clinvar`"
- "Phenotype quality from `@sec-ch02-phenotypes`"
- "Circularity in CADD from `@sec-ch04-circularity`"

In `@sec-ch22-data-splitting`:
- "Splitting methodology from `@sec-ch21-homology-aware-splitting`"

**Proposed forward references to add:**

In `@sec-ch22-detection`:
- "Statistical methods from `@sec-ch21-statistical-rigor`"

In `@sec-ch22-fairness`:
- "Clinical fairness in `@sec-ch25-fairness`"
- "Equity considerations in `@sec-ch29-fairness`"

**Redundancy watch:**
- Splitting strategies overlap with Ch 21 - cross-reference
- Batch effects mentioned in Ch 1, 16, 19, and here - this should be comprehensive treatment
- **Recommendation**: This is the authoritative confounding chapter; others provide brief context + cross-reference

---

### Chapter 23: Uncertainty Quantification

**Proposed back-references:**

In `@sec-ch23-calibration-problem`:
- "Calibration in variant prediction from `@sec-ch14-calibration`"
- "Evaluation calibration from `@sec-ch21-calibration`"

In `@sec-ch23-fm-miscalibration`:
- "Foundation model training from Chapter 8 and 10"
- "Label noise from `@sec-ch02-label-noise`"

In `@sec-ch23-vep-uncertainty`:
- "Variant effect prediction from Chapter 14"

**Proposed forward references to add:**

In `@sec-ch23-conformal-clinical`:
- "Clinical integration in `@sec-ch25-uncertainty`"
- "Rare disease workflow in `@sec-ch26-workflow`"

In `@sec-ch23-ood-detection`:
- "Population distribution in clinical deployment `@sec-ch25-fairness`"

In `@sec-ch23-communication`:
- "Clinical communication in `@sec-ch26-workflow`"
- "Regulatory requirements in `@sec-ch29-validation`"

**Redundancy watch:**
- Calibration appears in Ch 14, 21, 25, and here
- **Recommendation**: This chapter is comprehensive UQ reference; others cross-reference for domain-specific applications

---

### Chapter 24: Interpretability

**Proposed back-references:**

In `@sec-ch24-cnn-filters`:
- "CNN architectures from `@sec-ch06-cnn`"
- "DeepSEA interpretability from `@sec-ch06-deepsea-validation`"

In `@sec-ch24-attention`:
- "Attention mechanisms from `@sec-ch07-self-attention`"
- "Multi-head attention from `@sec-ch07-multihead`"

In `@sec-ch24-probing`:
- "Probing methodology from `@sec-ch09-probing-representations`"
- "DNA LM probing from `@sec-ch11-probing`"
- "ESM probing from `@sec-ch12-emergent-knowledge`"

**Proposed forward references to add:**

In `@sec-ch24-experimental`:
- "Functional validation in `@sec-ch26-validation`"
- "Design-test loops in `@sec-ch28-dbtl`"

In `@sec-ch24-clinical`:
- "Clinical interpretation in `@sec-ch26-acmg-amp`"

**Redundancy watch:**
- Probing methodology overlaps with Ch 9 and model chapters
- Attention interpretation mentioned in Ch 12 and 13

---

## Part VI: Clinical Translation

### Chapter 25: Clinical Risk Prediction

**Proposed back-references:**

In `@sec-ch25-pgs-to-fm`:
- "Polygenic scores from `@sec-ch03-pgs-construction`"
- "Foundation model features from `@sec-ch09-feature-extraction`"

In `@sec-ch25-ehr-integration`:
- "EHR data quality from `@sec-ch02-ehr`"
- "Phenotype embeddings from `@sec-ch03-deep-phenotyping`"

In `@sec-ch25-discrimination`:
- "Metrics from `@sec-ch21-metrics-genomic-tasks`"

In `@sec-ch25-calibration`:
- "Calibration methods from `@sec-ch23-post-hoc-calibration`"
- "Evaluation calibration from `@sec-ch21-calibration`"

In `@sec-ch25-uncertainty`:
- "UQ methods from `@sec-ch23-uq-methods`"
- "Conformal prediction from `@sec-ch23-conformal`"

In `@sec-ch25-fairness`:
- "Portability from `@sec-ch03-portability`"
- "Confounding analysis from `@sec-ch22-ancestry-confounding`"

**Proposed forward references to add:**

In `@sec-ch25-regulatory`:
- "Regulatory frameworks in `@sec-ch29-regulatory`"

**Redundancy watch:**
- Calibration appears in Ch 14, 21, 23, and here - each should have clear scope
- Fairness appears in Ch 3, 22, and here
- **Recommendation**: Ch 25 focuses on clinical deployment; others provide foundational concepts

---

### Chapter 26: Rare Disease Diagnosis

**Proposed back-references:**

In `@sec-ch26-quality-filters`:
- "Variant calling from `@sec-ch01-classical`"
- "Quality metrics from `@sec-ch01-metrics`"

In `@sec-ch26-frequency-filters`:
- "gnomAD from `@sec-ch02-gnomad`"
- "Allele frequency considerations from `@sec-ch03-ld`"

In `@sec-ch26-fm-scoring`:
- "Variant effect prediction from Chapter 14"
- "Protein VEP from `@sec-ch14-protein-vep`"
- "DNA VEP from `@sec-ch14-dna-vep`"
- "Combining evidence from `@sec-ch14-combining-evidence`"

In `@sec-ch26-acmg-amp`:
- "ACMG framework from `@sec-ch04-conservation-clinical-gap`"
- "Computational evidence from `@sec-ch14-acmg-mapping`"

In `@sec-ch26-calibration`:
- "Calibration methods from `@sec-ch23-post-hoc-calibration`"
- "ACMG calibration from `@sec-ch14-acmg-mapping`"

In `@sec-ch26-compound-het`:
- "Phasing from `@sec-ch01-phasing`"

**Proposed forward references to add:**

In `@sec-ch26-regulatory`:
- "Regulatory frameworks in `@sec-ch29-regulatory`"

**Redundancy watch:**
- ACMG criteria appear here and Ch 14
- Phasing appears here and Ch 1
- **Recommendation**: Ch 1 explains phasing, Ch 14 covers model calibration to ACMG, this chapter shows clinical workflow

---

### Chapter 27: Drug Discovery

**Proposed back-references:**

In `@sec-ch27-variant-to-gene`:
- "Variant effect prediction from Chapter 14"
- "Gene prioritization from `@sec-ch18-disease-gene`"

In `@sec-ch27-network-propagation`:
- "Graph methods from `@sec-ch18-biological-networks`"
- "FM embeddings as features from `@sec-ch18-fm-embeddings`"

In `@sec-ch27-binding-prediction`:
- "Protein models from Chapter 12"
- "Structure prediction from `@sec-ch12-esmfold`"

In `@sec-ch27-perturb-seq`:
- "Single-cell perturbation models from `@sec-ch16-perturbation`"
- "Perturbation prediction from `@sec-ch16-in-silico`"

In `@sec-ch27-multi-omic-biomarkers`:
- "Multi-omic integration from `@sec-ch19-multi-omics`"

**Proposed forward references to add:**

In `@sec-ch27-lab-in-loop`:
- "Design-test cycles in `@sec-ch28-dbtl`"

In `@sec-ch27-trial-design`:
- "Clinical prediction models from `@sec-ch25-clinical-risk`"

**Redundancy watch:**
- Perturbation modeling overlaps with Ch 16
- Network methods overlap with Ch 18

---

### Chapter 28: Sequence Design

**Proposed back-references:**

In `@sec-ch28-plm-generation`:
- "Protein language models from Chapter 12"
- "ESM representations from `@sec-ch12-esm2`"

In `@sec-ch28-promoter-enhancer`:
- "Regulatory models from Chapter 13"
- "Enformer predictions from `@sec-ch13-enformer`"

In `@sec-ch28-codon-optimization`:
- "Codon models from `@sec-ch15-codon`"

In `@sec-ch28-utr-design`:
- "UTR models from `@sec-ch15-utr`"

In `@sec-ch28-mrna-immunogenicity`:
- "mRNA design principles from `@sec-ch15-mrna-design`"

In `@sec-ch28-active-learning`:
- "Uncertainty quantification from `@sec-ch23-uq-methods`"
- "Selective prediction from `@sec-ch23-selective-prediction`"

**Proposed forward references to add:**

In `@sec-ch28-biosecurity`:
- "Ethical frameworks in `@sec-ch29-biosecurity`"

**Redundancy watch:**
- mRNA design overlaps with Ch 15
- **Recommendation**: Ch 15 covers modeling, Ch 28 covers design applications

---

### Chapter 29: Ethics and Frontiers

**Proposed back-references:**

In `@sec-ch29-validation`:
- "Evaluation frameworks from Chapter 21"
- "Clinical validation from `@sec-ch26-validation`"

In `@sec-ch29-reidentification`:
- "Privacy in genomic data from `@sec-ch02-data`"

In `@sec-ch29-fairness`:
- "Portability from `@sec-ch03-portability`"
- "Confounding from `@sec-ch22-ancestry-confounding`"
- "Clinical fairness from `@sec-ch25-fairness`"

In `@sec-ch29-multiscale`:
- "Multi-omic integration from `@sec-ch19-multi-omics`"
- "3D genome from Chapter 17"

In `@sec-ch29-learning-health`:
- "Clinical integration from `@sec-ch25-clinical-integration`"

**No forward references** - this is the final chapter

**Redundancy watch:**
- Fairness appears in Ch 3, 22, 25, and here
- Validation appears in Ch 21, 25, 26, and here

---

## Summary: Cross-Chapter Concept Threads

### Calibration Thread
- **Ch 14** (`@sec-ch14-calibration`): VEP-specific calibration to ACMG
- **Ch 21** (`@sec-ch21-calibration`): Evaluation methodology
- **Ch 23** (`@sec-ch23-calibration`): Comprehensive UQ and calibration methods
- **Ch 25** (`@sec-ch25-calibration`): Clinical deployment calibration
- **Ch 26** (`@sec-ch26-calibration`): Rare disease workflow calibration

**Recommendation**: Ch 23 is authoritative; others cross-reference for domain context

### Confounding/Fairness Thread
- **Ch 2** (`@sec-ch02-constraints`): Data biases
- **Ch 3** (`@sec-ch03-portability`): GWAS portability
- **Ch 21** (`@sec-ch21-homology-aware-splitting`): Evaluation strategy
- **Ch 22** (`@sec-ch22-confounding`): Comprehensive confounding analysis
- **Ch 25** (`@sec-ch25-fairness`): Clinical fairness
- **Ch 29** (`@sec-ch29-fairness`): Ethical frameworks

**Recommendation**: Ch 22 is authoritative for methods; others provide domain context

### Variant Effect Prediction Thread
- **Ch 4**: Classical approaches
- **Ch 6**: CNN-based (SpliceAI, DeepSEA)
- **Ch 14**: Foundation model VEP
- **Ch 26**: Clinical workflow integration

**Recommendation**: Clear progression from classical → task-specific → foundation model → clinical deployment

### Transfer Learning Thread
- **Ch 8**: Pretraining strategies
- **Ch 9**: Transfer and adaptation methodology
- **Ch 10**: Foundation model paradigm
- **Ch 11-14**: Model-specific transfer
- **Ch 25**: Clinical feature extraction

**Recommendation**: Ch 9 is comprehensive transfer guide; model chapters show implementation

### Benchmark/Evaluation Thread
- **Ch 1**: Variant calling benchmarks
- **Ch 20**: Comprehensive benchmark catalog
- **Ch 21**: Evaluation methodology
- **Ch 22**: Confounding detection
- **Ch 23**: Uncertainty quantification

**Recommendation**: Ch 20 catalogs, Ch 21 provides methodology, Ch 22-23 provide specialized evaluation approaches

## Redundancy Watch Summary

High overlap areas requiring coordination:

1. Batch effects - appears in Ch 1, 16, 19, 22 (Ch 22 should be comprehensive)
1. Phenotype quality - Ch 2, 3, 22, 25 (Ch 2 authoritative source)
1. ClinVar - Ch 2, 4, 14, 20, 26 (Ch 2 data source, others cross-reference)
1. ACMG criteria - Ch 4, 14, 26 (brief in 4, scoring in 14, workflow in 26)
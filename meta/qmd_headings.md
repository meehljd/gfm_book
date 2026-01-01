
### appendix/app-a-dl.qmd
# Deep Learning Primer {#sec-apx-a-dl}

### appendix/app-b-compute.qmd
# Deployment and Compute {#sec-apx-b-compute}

### appendix/app-c-data-curation.qmd
# Data Curation {#sec-apx-c-data-curation}

### appendix/app-d-models.qmd
# Model Reference {#sec-apx-d-models}
## Category Definitions

### appendix/app-e-resources.qmd
# Resources {#sec-apx-e-resources}
## Genomics & Human Genetics
## Immunology
## Machine Learning & Deep Learning

### appendix/app-f-glossary.qmd
# Glossary {#sec-apx-f-glossary}
## Terms (A–Z)

### bib/references.qmd
# References {.unnumbered}

### index.qmd
# Introduction {.unnumbered}
## Why Foundation Models for Genomics?
## Recurring Themes
## Typography and Formatting {.unnumbered}
## Structure and Organization
## A Framework, Not a Snapshot

### part_1/p1--foundations.qmd
# Part I: Data Foundations {.unnumbered}

### part_1/p1-ch01-ngs.qmd
# From Reads to Variants {#sec-ch01-ngs}
## NGS Data Challenges {#sec-ch01-challenges}
## Targeting Strategies: Panels, Exomes, and Genomes {#sec-ch01-targeting}
### Targeted and Panel Sequencing {#sec-ch01-panels}
### Whole-Exome Sequencing {#sec-ch01-wes}
### Whole-Genome Sequencing {#sec-ch01-wgs}
### Long-Read Sequencing Technologies {#sec-ch01-longread}
## Classical Variant Calling Pipelines {#sec-ch01-classical}
### From Sequencer to Aligned Reads {#sec-ch01-alignment}
### Per-Sample Variant Calling {#sec-ch01-persample}
### Cohort Calling and Filtering {#sec-ch01-cohort}
### Sample-Level Quality Control {#sec-ch01-qc}
## Haplotype Phasing {#sec-ch01-phasing}
### Clinical and Analytical Importance {#sec-ch01-phasing-importance}
### Phasing Methods {#sec-ch01-phasing-methods}
### Phasing Approaches {#sec-ch01-phasing-approaches}
### Genotype Imputation and Refinement {#sec-ch01-imputation}
### Hybrid Sequencing and Coverage Boosting {#sec-ch01-hybrid}
## Sources of Error and Uncertainty {#sec-ch01-errors}
### Mapping Ambiguity and Reference Bias {#sec-ch01-mapping-bias}
### Systematic Sequencing Artifacts {#sec-ch01-artifacts}
### Coverage Gaps and Allelic Imbalance {#sec-ch01-coverage}
### Complex Variants and Representation {#sec-ch01-complex}
## Difficult Regions: The Limits of Short-Read Calling {#sec-ch01-difficult}
### Segmental Duplications and Gene Families {#sec-ch01-segdup}
### Low-Complexity and Repetitive Sequence {#sec-ch01-repeats}
### HLA Region Complexity {#sec-ch01-hla}
## Benchmarking and Ground Truth {#sec-ch01-benchmarks}
### GIAB Reference Samples {#sec-ch01-giab}
### Metrics and Their Meaning {#sec-ch01-metrics}
### Limitations of Benchmarks {#sec-ch01-benchmark-limits}
## DeepVariant: Variant Calling as Image Classification {#sec-ch01-deepvariant}
### Pileup Images as Input {#sec-ch01-pileup}
### Architecture and Training {#sec-ch01-deepvariant-arch}
### Cohort Calling with GLnexus {#sec-ch01-glnexus}
### Comparison with Classical Approaches {#sec-ch01-deepvariant-comparison}
## Implications for Genomic Deep Learning {#sec-ch01-implications}
### Variants as Atomic Units {#sec-ch01-atomic}
### Inherited Biases and Blind Spots {#sec-ch01-inherited}
### Effect Sizes Across the Frequency Spectrum {#sec-ch01-effect-sizes}
## Reliability Landscape {#sec-ch01-reliability}

### part_1/p1-ch02-data.qmd
# Data Landscape {#sec-ch02-data}
## Reference Genomes and Gene Annotations {#sec-ch02-reference}
### Reference Assemblies {#sec-ch02-reference-assemblies}
### Gene Models {#sec-ch02-gene-models}
## Population Variant Catalogs and Allele Frequencies {#sec-ch02-population}
### dbSNP and Variant Identifiers {#sec-ch02-dbsnp}
### 1000 Genomes and Early Reference Panels {#sec-ch02-1000genomes}
### Genome Aggregation Database (gnomAD) {#sec-ch02-gnomad}
## Biobanks and GWAS Data {#sec-ch02-biobanks}
### Large Population Cohorts {#sec-ch02-cohorts}
### GWAS Summary Statistics {#sec-ch02-gwas-summary}
## Functional Genomics and Regulatory Landscapes {#sec-ch02-functional}
### ENCODE, Roadmap, and Related Consortia {#sec-ch02-encode}
### Cistrome Data Browser {#sec-ch02-cistrome}
### From Assays to Training Labels {#sec-ch02-assays-labels}
### Deep Mutational Scanning and Multiplexed Variant Assays {#sec-ch02-dms}
## Expression and eQTL Resources {#sec-ch02-expression}
### Bulk Expression Atlases {#sec-ch02-gtex}
### Single-Cell and Context-Specific Expression {#sec-ch02-single-cell}
## Protein Databases {#sec-ch02-protein-databases}
## Phenotype Definition and Data Quality {#sec-ch02-phenotypes}
### Problem of Binary Disease Definitions {#sec-ch02-binary-phenotypes}
### Electronic Health Record Quality and Completeness {#sec-ch02-ehr}
### Coding Inconsistencies and Label Noise {#sec-ch02-label-noise}
### Deep Phenotyping Approaches {#sec-ch02-deep-phenotyping}
### Impact on Downstream Modeling {#sec-ch02-phenotype-impact}
## Variant Interpretation Databases and Clinical Labels {#sec-ch02-clinical}
### ClinVar and Clinical Assertions {#sec-ch02-clinvar}
### Complementary Clinical Databases {#sec-ch02-clinical-other}
### ClinGen and Expert Curation {#sec-ch02-clingen}
### Pharmacogenomics Resources {#sec-ch02-pharmacogenomics}
## Inherited Constraints {#sec-ch02-constraints}

### part_1/p1-ch03-gwas.qmd
# GWAS and Polygenic Scores {#sec-ch03-gwas}
## GWAS Framework {#sec-ch03-gwas-framework}
### Association Models for Quantitative Traits {#sec-ch03-linear-models}
### Association Models for Disease Outcomes {#sec-ch03-logistic-models}
### Manhattan Plots and Q-Q Plots {#sec-ch03-visualization}
### Population Structure Control {#sec-ch03-population-structure}
## Heritability: What Genetics Can Explain {#sec-ch03-heritability}
### Pedigree Heritability {#sec-ch03-pedigree-heritability}
### SNP-Heritability and the Missing Heritability Problem {#sec-ch03-snp-heritability}
### Implications for GWAS and Polygenic Scores {#sec-ch03-heritability-implications}
## Linkage Disequilibrium and the Association-Causation Gap {#sec-ch03-ld}
### Structure of Linkage Disequilibrium {#sec-ch03-ld-structure}
### Causal Variants, Tag Variants, and GWAS Catalogs {#sec-ch03-causal-vs-tag}
## Fine-Mapping: From Loci to Causal Variants {#sec-ch03-fine-mapping}
### Statistical Framework {#sec-ch03-fine-mapping-stats}
### Functional Annotation Priors {#sec-ch03-functional-priors}
### Multi-Ancestry Fine-Mapping {#sec-ch03-multi-ancestry-fine-mapping}
## Polygenic Score Construction {#sec-ch03-pgs-construction}
### Clumping and Thresholding {#sec-ch03-clumping-thresholding}
### LD-Aware Bayesian Methods {#sec-ch03-bayesian-pgs}
### Fine-Mapping-Informed Scores {#sec-ch03-fine-mapping-informed-pgs}
## Polygenic Score Interpretation {#sec-ch03-pgs-interpretation}
### Relative Risk and Percentiles {#sec-ch03-relative-risk}
### Absolute Risk {#sec-ch03-absolute-risk}
### Explained Variance and Discrimination {#sec-ch03-variance-discrimination}
## Ancestry, Portability, and Fairness {#sec-ch03-portability}
### Portability Problem {#sec-ch03-portability-problem}
### Fairness and Health Equity {#sec-ch03-fairness}
## Phenome-Wide Association Studies {#sec-ch03-phewas}
### PheWAS Framework {#sec-ch03-phewas-framework}
### PheWAS for Polygenic Score Interpretation {#sec-ch03-prs-phewas}
### Phenotype Quality and PheWAS Power {#sec-ch03-phenotype-quality}
### Deep Phenotyping and Embedding-Enhanced GWAS {#sec-ch03-deep-phenotyping}
## From Association to Mechanism {#sec-ch03-mechanism}

### part_1/p1-ch04-vep-classical.qmd
# Classical Variant Prediction {#sec-ch04-vep-classical}
## Conservation-Based Approaches {#sec-ch04-conservation}
### Evolutionary Constraint Metrics {#sec-ch04-constraint-metrics}
### What Conservation Measures Versus What Clinicians Need {#sec-ch04-conservation-clinical-gap}
### Clinical Application and Boundaries {#sec-ch04-conservation-boundaries}
### ACMG-AMP Variant Classification Framework
## Protein-Level Predictors {#sec-ch04-protein-predictors}
### *SIFT*: Sequence Homology as Functional Constraint {#sec-ch04-sift}
### *PolyPhen-2*: Integrating Structure and Sequence {#sec-ch04-polyphen}
### From Sequence to Function {#sec-ch04-sequence-to-function}
### Boundaries of Protein-Level Prediction {#sec-ch04-protein-boundaries}
## *CADD* Framework {#sec-ch04-cadd}
### Evolutionary Proxy Training and Label Sources {#sec-ch04-cadd-training}
### Feature Integration {#sec-ch04-cadd-features}
### Model Architecture and Scoring {#sec-ch04-cadd-scoring}
### Evolutionary Proxy Problem {#sec-ch04-proxy-problem}
## Other Ensemble Methods {#sec-ch04-ensemble-methods}
### *REVEL* {#sec-ch04-revel}
### *M-CAP* {#sec-ch04-mcap}
### Comparison and Selection {#sec-ch04-ensemble-comparison}
## Circularity and Ascertainment Bias {#sec-ch04-circularity}
### Circularity Problem {#sec-ch04-circularity-definition}
### Ascertainment Bias {#sec-ch04-ascertainment}
### Implications for Clinical Use {#sec-ch04-clinical-implications}
## Limitations of the Feature Engineering Paradigm {#sec-ch04-feature-limitations}
### Feature Ceiling {#sec-ch04-feature-ceiling}
### Limited Context {#sec-ch04-limited-context}
### Persistent Gap Between Measurement and Need {#sec-ch04-measurement-gap}
### From Features to Representations {#sec-ch04-features-to-representations}

### part_2/p2--principles.qmd
# Part II: Sequence Architectures {.unnumbered}

### part_2/p2-ch05-representations.qmd
# Tokens and Embeddings {#sec-ch05-representations}
## One-Hot Encoding: The CNN Foundation {#sec-ch05-onehot}
## *K*-mer Tokenization: The DNABERT Approach {#sec-ch05-kmer}
## Byte Pair Encoding: Learning the Vocabulary {#sec-ch05-bpe}
## Single-Nucleotide Tokenization: Maximum Resolution {#sec-ch05-single-nucleotide}
## Biologically-Informed Tokenization {#sec-ch05-biological-tokenization}
## From Tokens to Embeddings: Learning Representations {#sec-ch05-embeddings}
### Position in Sequence {#sec-ch05-position}
## Special Considerations for Biological Sequences {#sec-ch05-biological-special}
## Tradeoffs and Practical Guidance {#sec-ch05-tradeoffs}
### Resolution Versus Compression {#sec-ch05-resolution-compression}
### Vocabulary Size and Model Capacity {#sec-ch05-vocabulary-capacity}
### Computational Efficiency {#sec-ch05-computational-efficiency}
### Variant Interpretation Requirements {#sec-ch05-variant-interpretation}
### Practical Heuristics {#sec-ch05-heuristics}
## Representation as Foundation {#sec-ch05-foundation}

### part_2/p2-ch06-cnn.qmd
# Convolutional Networks {#sec-ch06-cnn}
## Convolutions as Sequence Pattern Detectors {#sec-ch06-convolutions}
## *DeepSEA*: Regulatory Prediction from Sequence {#sec-ch06-deepsea}
### Architecture and Training {#sec-ch06-deepsea-architecture}
### Learned Representations and Biological Validation {#sec-ch06-deepsea-validation}
### Variant Effect Prediction {#sec-ch06-deepsea-vep}
## Cell-Type Specificity and Regulatory Grammar {#sec-ch06-basset}
## *ExPecto*: From Chromatin to Expression {#sec-ch06-expecto}
### Modular Architecture {#sec-ch06-expecto-architecture}
### Expression Prediction and Variant Effects {#sec-ch06-expecto-validation}
## *SpliceAI*: Clinical-Grade Splicing Prediction {#sec-ch06-spliceai}
### Architecture: Depth and Dilation {#sec-ch06-spliceai-architecture}
### Performance and Validation {#sec-ch06-spliceai-performance}
### Clinical Impact {#sec-ch06-spliceai-clinical}
## Receptive Field Ceiling {#sec-ch06-receptive-field}
## Sequential Approaches and Their Costs {#sec-ch06-sequential}
### Vanishing Gradient Problem {#sec-ch06-vanishing-gradient}
### *DanQ*: Combining Convolutions and Recurrence {#sec-ch06-danq}
### Sequential Bottleneck {#sec-ch06-sequential-bottleneck}
## Specialization and Its Limits {#sec-ch06-specialization}

### part_2/p2-ch07-attention.qmd
# Transformers and Attention {#sec-ch07-attention}
## Self-Attention Mechanism {#sec-ch07-self-attention}
### Query, Key, and Value Vectors {#sec-ch07-qkv}
### Multi-Head Attention {#sec-ch07-multihead}
## Positional Encoding {#sec-ch07-positional-encoding}
### Absolute Position Encodings {#sec-ch07-absolute-position}
### Relative Position Encodings {#sec-ch07-relative-position}
### Genomic Position Considerations {#sec-ch07-genomic-position}
## Transformer Block {#sec-ch07-transformer-block}
### Block Components {#sec-ch07-block-components}
### Information Flow and Depth {#sec-ch07-depth}
## Scaling to Genomic Sequences {#sec-ch07-scaling}
### Quadratic Barrier {#sec-ch07-quadratic-barrier}
### Parameter Considerations {#sec-ch07-parameters}
### Context Length Strategies {#sec-ch07-context-strategies}
### Memory and Precision {#sec-ch07-memory}
## Architectural Variants for Genomics {#sec-ch07-variants}
### Encoder-Only Transformers {#sec-ch07-encoder-only}
### Decoder-Only Transformers {#sec-ch07-decoder-only}
### Encoder-Decoder Transformers {#sec-ch07-encoder-decoder}
### Hybrid CNN-Transformer Models {#sec-ch07-hybrid}
## Training Dynamics {#sec-ch07-training}
### Optimization {#sec-ch07-optimization}
### Regularization {#sec-ch07-regularization}
### Gradient Stability {#sec-ch07-gradients}
### Distributed Training {#sec-ch07-distributed}
## Limitations and Emerging Alternatives {#sec-ch07-limitations}
### Quadratic Ceiling {#sec-ch07-quadratic-ceiling}
### State Space Models {#sec-ch07-ssm}
### Choosing Architectures {#sec-ch07-choosing}
## Capacity Without Direction {#sec-ch07-conclusion}

### part_2/p2-ch08-pretraining.qmd
# Pretraining Strategies {#sec-ch08-pretraining}
## Masked Language Modeling {#sec-ch08-mlm}
### Masking Strategies and Their Implications {#sec-ch08-mlm-strategies}
### What Masked Language Models Learn {#sec-ch08-mlm-learning}
## Next-Token Prediction {#sec-ch08-autoregressive}
### Genomic Applications {#sec-ch08-autoregressive-genomics}
## MLM and Autoregressive Comparison {#sec-ch08-comparison}
### Hybrid Architectures {#sec-ch08-hybrid}
## Span Corruption and Denoising {#sec-ch08-denoising}
### Corruption Beyond Masking {#sec-ch08-corruption}
### Biologically Motivated Corruption {#sec-ch08-biological-corruption}
## Contrastive Learning {#sec-ch08-contrastive}
### Augmentation Design for Genomic Sequences {#sec-ch08-augmentation}
### Cross-Species Contrastive Learning {#sec-ch08-cross-species}
## Multi-Task Pretraining {#sec-ch08-multitask}
### Task Selection and Architecture {#sec-ch08-task-selection}
### Loss Weighting and Balancing {#sec-ch08-loss-weighting}
### Large-Scale Multi-Task Examples {#sec-ch08-multitask-examples}
### When Multi-Task Learning Fails {#sec-ch08-multitask-failure}
## Staged Pretraining Strategies {#sec-ch08-staged}
### Context Length Curricula {#sec-ch08-context-curriculum}
### Domain-Adaptive Pretraining {#sec-ch08-domain-adaptive}
### Continued Pretraining on Expanded Data {#sec-ch08-continued-pretraining}
### Multi-Objective Schedules {#sec-ch08-multiobjective-schedule}
### Data Complexity Curricula {#sec-ch08-data-complexity}
### Practical Considerations {#sec-ch08-staged-practical}
## Data Strategies for Pretraining {#sec-ch08-data}
### Reference Genomes and Population Diversity {#sec-ch08-reference-genomes}
### Repeat Handling {#sec-ch08-repeats}
### Multi-Species and Augmentation Strategies {#sec-ch08-multispecies}
## Optimization and Scaling {#sec-ch08-optimization}
### Optimization Hyperparameters {#sec-ch08-hyperparameters}
### Scaling Laws and Emergence {#sec-ch08-scaling}
## Training Diagnostics {#sec-ch08-diagnostics}
### Monitoring Loss and Gradients {#sec-ch08-monitoring}
### Functional Probing {#sec-ch08-probing}
## Strategy Selection {#sec-ch08-selection}
## Pretraining in Practice: Case Studies {#sec-ch08-case-studies}
### DNABERT {#sec-ch08-dnabert}
### HyenaDNA {#sec-ch08-hyenadna}
### Enformer {#sec-ch08-enformer}
### ESM-2 {#sec-ch08-esm2}
## Open Questions {#sec-ch08-open-questions}
## From Sequence Statistics to Biological Knowledge {#sec-ch08-sequence-to-knowledge}

### part_2/p2-ch09-transfer.qmd
# Transfer and Adaptation {#sec-ch09-transfer}
## Source and Target Domains {#sec-ch09-source-target}
### Gap Between Pretraining and Deployment {#sec-ch09-pretraining-deployment-gap}
### Recognizing Transfer Outcomes {#sec-ch09-transfer-outcomes}
## Factors Determining Transfer Success {#sec-ch09-transfer-factors}
### Task Relatedness {#sec-ch09-task-relatedness}
### Target Data Quantity {#sec-ch09-target-data-quantity}
### Model Expressiveness {#sec-ch09-model-expressiveness}
### Distribution Overlap {#sec-ch09-distribution-overlap}
### Factor Interactions
## Feature Extraction and Representation Analysis {#sec-ch09-feature-extraction}
### Linear Probing {#sec-ch09-linear-probing}
### When Linear Probing Fails {#sec-ch09-linear-probing-limits}
### Probing Representations {#sec-ch09-probing-representations}
### What Probing Reveals About Pretrained Models {#sec-ch09-probing-results}
### Probe-Guided Adaptation {#sec-ch09-probe-guided-adaptation}
## Parameter-Efficient Fine-Tuning {#sec-ch09-peft}
### Low-Rank Adaptation {#sec-ch09-lora}
### Configuring Low-Rank Adaptation {#sec-ch09-lora-config}
## Layer Selection for Embedding Extraction {#sec-ch09-layer-selection}
### The Encoder Advantage
### The Decoder Dilemma
### Practical Consequences
### Layer Averaging and Weighted Combinations
### Systematic Layer Probing
### Implications for Model Selection
### Cross-Reference to Pretraining Objectives
## Full Fine-Tuning {#sec-ch09-full-finetuning}
### Making Full Fine-Tuning Work {#sec-ch09-full-finetuning-practice}
### Risks of Unconstrained Adaptation {#sec-ch09-finetuning-risks}
### The `[CLS]` Token and Sequence Aggregation {#sec-ch09-cls-token}
### Mean Pooling and Alternatives
### Practical Considerations for Genomic Sequences
## Choosing an Adaptation Strategy {#sec-ch09-choosing-strategy}
## Domain Shift and Cross-Context Transfer {#sec-ch09-domain-shift}
### Types of Domain Shift in Genomics {#sec-ch09-domain-shift-types}
### Detecting and Mitigating Shift {#sec-ch09-detecting-shift}
## Minimal-Data and Emerging Transfer Paradigms {#sec-ch09-minimal-data}
### Few-Shot Learning with Minimal Examples {#sec-ch09-few-shot}
### Zero-Shot Transfer Without Task-Specific Data {#sec-ch09-zero-shot}
### Emerging Approaches {#sec-ch09-emerging-approaches}
### Toward Theoretical Foundations {#sec-ch09-theory}
## Label and Class Imbalance {#sec-ch09-label-imbalance}
### Manifestations During Transfer
### Mitigation Strategies
### Evaluation Under Imbalance
### Imbalance as Fundamental Constraint
## Diagnosing Transfer: Validation and Failure Modes {#sec-ch09-diagnosing-transfer}
### Diagnosing Negative Transfer {#sec-ch09-negative-transfer}
### Remediation When Transfer Fails {#sec-ch09-remediation}
### Validation and Common Pitfalls {#sec-ch09-validation-pitfalls}
### Sources of Spurious Success {#sec-ch09-spurious-success}
### Evaluation Practices That Reveal True Performance {#sec-ch09-evaluation-practices}
## Case Studies in Transfer Learning {#sec-ch09-case-studies}
### *DNABERT* for Chromatin Accessibility {#sec-ch09-case-dnabert}
### *ESM* for Variant Pathogenicity {#sec-ch09-case-esm}
### *Enformer* for Cross-Tissue Expression {#sec-ch09-case-enformer}
### Cross-Species Regulatory Prediction {#sec-ch09-case-cross-species}
## What Transfers, What Breaks {#sec-ch09-conclusion}

### part_3/p3--architectures.qmd
# Part III: Foundation Model Families {.unnumbered}

### part_3/p3-ch10-fm-principles.qmd
# Foundation Model Paradigm {#sec-ch10-fm-principles}
## From Task-Specific Models to Foundation Models {#sec-ch10-task-specific}
## Defining Genomic Foundation Models {#sec-ch10-defining}
### Essential Properties {#sec-ch10-essential-properties}
### What Doesn't Count {#sec-ch10-what-doesnt-count}
### Limitations of the Foundation Model Concept {#sec-ch10-concept-limitations}
## Scaling Laws and Compute-Optimal Training {#sec-ch10-scaling}
### Scaling Law Framework {#sec-ch10-scaling-framework}
### Empirical Scaling in Genomic Models {#sec-ch10-empirical-scaling}
### Compute-Optimal Decisions for Genomics {#sec-ch10-compute-optimal}
### Emergent Capabilities {#sec-ch10-emergence}
## A Taxonomy of Genomic Foundation Models {#sec-ch10-taxonomy}
### DNA Language Models {#sec-ch10-dna-lm}
### Sequence-to-Function Foundation Models {#sec-ch10-seq-to-func}
### Variant Effect Prediction Models {#sec-ch10-vep-models}
### Multi-Omic Foundation Models {#sec-ch10-multi-omic}
## Design Dimensions {#sec-ch10-design-dimensions}
### Data Composition {#sec-ch10-data-composition}
### Architecture Choices {#sec-ch10-architecture}
### Context Length {#sec-ch10-context-length}
### Tokenization {#sec-ch10-tokenization}
## Build Versus Use Decisions {#sec-ch10-build-vs-use}
### When to Use Existing Models {#sec-ch10-use-existing}
### When to Adapt Existing Models {#sec-ch10-adapt-existing}
### When to Train from Scratch {#sec-ch10-train-scratch}
### Cost-Benefit Analysis {#sec-ch10-cost-benefit}
## Evaluation Principles {#sec-ch10-evaluation}
### Multi-Task Assessment {#sec-ch10-multi-task}
### Transfer Versus Pretraining Performance {#sec-ch10-transfer-eval}
## Foundation Model Ecosystem {#sec-ch10-ecosystem}
### Model Distribution {#sec-ch10-distribution}
### Documentation Requirements {#sec-ch10-documentation}
### Industry and Academic Contributions {#sec-ch10-contributions}
## Open Questions {#sec-ch10-open-questions}
## Convergence Without Consolidation {#sec-ch10-convergence}

### part_3/p3-ch11-dna-lm.qmd
# DNA Language Models {#sec-ch11-dna-lm}
## From Task-Specific CNNs to General-Purpose Language Models {#sec-ch11-task-specific-to-general}
## *DNABERT*: The First DNA Language Model {#sec-ch11-dnabert}
## *Nucleotide Transformer*: Scaling Data and Model Diversity {#sec-ch11-nucleotide-transformer}
## *GPN*: Cross-Species Pretraining for Variant Effect Prediction {#sec-ch11-gpn}
## Long-Context Revolution {#sec-ch11-long-context}
### *HyenaDNA*: Megabase Context via Implicit Convolutions {#sec-ch11-hyenadna}
### *Caduceus*: Bidirectional Processing with Reverse-Complement Equivariance {#sec-ch11-caduceus}
### *Evo 2*: Genome-Scale Modeling Across the Tree of Life {#sec-ch11-evo2}
## Training Data and What Models Learn {#sec-ch11-training-data}
### Training Corpus Composition {#sec-ch11-corpus-composition}
### Probing What Models Learn {#sec-ch11-probing}
### What Models Do Not Learn {#sec-ch11-limitations-learned}
## Benchmark Performance and Evaluation {#sec-ch11-benchmarks}
### Major Benchmark Suites {#sec-ch11-benchmark-suites}
### Benchmark Limitations {#sec-ch11-benchmark-limitations}
## Annotation-Aware Extensions {#sec-ch11-annotation-aware}
## Using DNA Language Models in Practice {#sec-ch11-practical-use}
### Embeddings as Universal Features {#sec-ch11-embeddings}
### Fine-Tuning and Adaptation {#sec-ch11-fine-tuning}
### Zero-Shot and Few-Shot Scoring {#sec-ch11-zero-shot}
## Limitations and Open Challenges {#sec-ch11-open-challenges}
## Representations Without Predictions {#sec-ch11-soft-landing}

### part_3/p3-ch12-protein-lm.qmd
# Protein Language Models {#sec-ch12-protein-lm}
## ESM Model Family {#sec-ch12-esm-family}
### ESM-1b: Establishing the Paradigm {#sec-ch12-esm1b}
### Emergent Biological Knowledge {#sec-ch12-emergent-knowledge}
### ESM-2: Scaling Up {#sec-ch12-esm2}
## Alternative Architectures {#sec-ch12-alternative-architectures}
## Attention and Evolutionary Coupling {#sec-ch12-attention-coupling}
## ESMFold: Structure from Sequence {#sec-ch12-esmfold}
### Alignment-Free Prediction {#sec-ch12-alignment-free}
### What ESMFold Reveals About PLMs {#sec-ch12-esmfold-implications}
## Function Prediction {#sec-ch12-function-prediction}
## Variant Effect Prediction {#sec-ch12-variant-effects}
## Integration with Structure Prediction {#sec-ch12-structure-integration}
## Limitations {#sec-ch12-limitations}
### Orphan and Dark Proteins {#sec-ch12-orphan-proteins}
### Novel Folds {#sec-ch12-novel-folds}
### Conformational Flexibility {#sec-ch12-conformational-flexibility}
### Epistasis {#sec-ch12-epistasis}
### Interpretability {#sec-ch12-interpretability}
## Lessons for Genomic Foundation Models {#sec-ch12-lessons}
### Self-Supervised Biological Knowledge {#sec-ch12-self-supervised}
### Scaling Benefits {#sec-ch12-scaling}
### Effective Transfer Learning {#sec-ch12-transfer}
### Architecture-Sequence Matching {#sec-ch12-architecture-matching}
### Integration Benefits {#sec-ch12-integration}
## Paradigm That Generalized {#sec-ch12-conclusion}

### part_3/p3-ch13-regulatory.qmd
# Regulatory Models {#sec-ch13-regulatory}
## Long-Range Regulation Problem {#sec-ch13-long-range}
## *Enformer*: Attention Meets Regulatory Genomics {#sec-ch13-enformer}
### Architecture {#sec-ch13-enformer-architecture}
### Training Data and Cross-Species Learning {#sec-ch13-enformer-training}
### Variant Effect Prediction {#sec-ch13-enformer-vep}
## *Borzoi*: From Chromatin to Transcriptome {#sec-ch13-borzoi}
### Beyond Transcription Initiation {#sec-ch13-borzoi-transcription}
### Predicting Coverage at Nucleotide Resolution {#sec-ch13-borzoi-coverage}
### Applications Beyond Expression Level {#sec-ch13-borzoi-applications}
## *Sei*: A Regulatory Vocabulary from Sequence {#sec-ch13-sei}
### Discrete Regulatory States {#sec-ch13-sei-states}
### Complementary to Track Prediction {#sec-ch13-sei-complementary}
## *AlphaGenome*: Unifying Modalities at Megabase Scale {#sec-ch13-alphagenome}
### From 200kb to One Megabase {#sec-ch13-alphagenome-scale}
### Closed Weights, Open Questions {#sec-ch13-alphagenome-access}
## What Hybrid Architectures Accomplish {#sec-ch13-accomplishments}
### Spanning Enhancer-Promoter Distances {#sec-ch13-spanning}
### Multi-Task Regularization {#sec-ch13-multitask}
### Cross-Species Constraints {#sec-ch13-cross-species}
### Unified Variant Effect Prediction {#sec-ch13-unified-vep}
## Limitations and Open Challenges {#sec-ch13-limitations}
### Training Data Constraints {#sec-ch13-training-bias}
### Finite Context {#sec-ch13-finite-context}
### Missing Three-Dimensional Context {#sec-ch13-missing-3d}
### Correlation Versus Causation {#sec-ch13-correlation}
### Interpretability Challenges {#sec-ch13-interpretability}
## Relationship to Foundation Models {#sec-ch13-foundation-models}
## Prediction Without Explanation {#sec-ch13-prediction-explanation}

### part_3/p3-ch14-vep-fm.qmd
# Variant Effect Prediction {#sec-ch14-vep-fm}
## Foundation Model Paradigm for Variant Interpretation {#sec-ch14-fm-paradigm}
### Zero-Shot and Supervised Approaches {#sec-ch14-zeroshot-supervised}
## Protein-Based Variant Effect Prediction {#sec-ch14-protein-vep}
### Zero-Shot Scoring with Protein Language Models {#sec-ch14-zeroshot-plm}
### Alignment-Based Models: EVE and popEVE {#sec-ch14-alignment-models}
### AlphaMissense: Structure-Informed Pathogenicity Prediction {#sec-ch14-alphamissense}
## DNA-Based Variant Effect Prediction {#sec-ch14-dna-vep}
### Splice Variant Prediction with SpliceAI {#sec-ch14-spliceai}
### Regulatory Variant Prediction with Enformer {#sec-ch14-enformer-vep}
### DNA Language Models: GPN-MSA and Evo 2 {#sec-ch14-dna-lm-vep}
### AlphaGenome: Unified Multi-Omic Variant Effect Prediction {#sec-ch14-alphagenome}
## Combining Evidence Across Modalities {#sec-ch14-combining-evidence}
### Integration Strategies {#sec-ch14-integration-strategies}
### Avoiding Double-Counting {#sec-ch14-double-counting}
### Practical Workflow Design {#sec-ch14-workflow-design}
## Calibration and Clinical Categories {#sec-ch14-calibration}
### Assessing Calibration {#sec-ch14-assessing-calibration}
### Calibration Methods for Variant Effect Prediction {#sec-ch14-calibration-methods}
### Mapping to ACMG Categories {#sec-ch14-acmg-mapping}
### The Challenge of Uncertain Significance {#sec-ch14-vus-challenge}
## Uncertainty Quantification {#sec-ch14-uncertainty}
### Sources of Uncertainty {#sec-ch14-uncertainty-sources}
### Uncertainty Estimation Methods {#sec-ch14-uncertainty-methods}
### Out-of-Distribution Detection {#sec-ch14-ood-detection}
## What Foundation Models Add {#sec-ch14-fm-gains}
### Improved Discrimination {#sec-ch14-improved-discrimination}
### Extended Coverage {#sec-ch14-extended-coverage}
### Mechanistic Interpretability {#sec-ch14-mechanistic-interpretability}
### Persistent Limitations {#sec-ch14-persistent-limitations}
## Clinical Integration Considerations {#sec-ch14-clinical-integration}
### Laboratory Validation {#sec-ch14-lab-validation}
### Workflow Integration {#sec-ch14-workflow-integration}
### Communication to Clinicians {#sec-ch14-clinical-communication}
## Open Challenges {#sec-ch14-open-challenges}
### Complex Variant Types {#sec-ch14-complex-variants}
### Combinatorial Effects {#sec-ch14-combinatorial}
### Phenotype Specificity {#sec-ch14-phenotype-specificity}
### Temporal and Environmental Context {#sec-ch14-temporal-context}
### Equity and Access {#sec-ch14-equity}
## Tools for Interpretation, Not Oracles {#sec-ch14-conclusion}

### part_4/p4--multi-scale.qmd
# Part IV: Systems and Scale {.unnumbered}

### part_4/p4-ch15-rna.qmd
# RNA Structure and Function {#sec-ch15-rna}
## RNA as Molecule Versus Transcriptome Readout {#sec-ch15-perspectives}
## Why Secondary Structure Creates a Distinct Modeling Challenge {#sec-ch15-structure-challenge}
### Flat Energy Landscape Problem {#sec-ch15-energy-landscape}
### Base Pairing and Long-Range Dependencies {#sec-ch15-base-pairing}
### Pseudoknots and Tertiary Complexity {#sec-ch15-pseudoknots}
## Classical Approaches to Structure Prediction {#sec-ch15-classical}
### Thermodynamic Folding Models {#sec-ch15-thermodynamic}
### Comparative and Covariation Methods {#sec-ch15-comparative}
## Deep Learning for Secondary Structure Prediction {#sec-ch15-dl-structure}
### From Thermodynamics to Learned Patterns {#sec-ch15-learned-patterns}
### Structure Probing as Supervision {#sec-ch15-structure-probing}
## RNA Foundation Models {#sec-ch15-foundation}
### Scale Gap with Protein Language Models {#sec-ch15-scale-gap}
### Architectures and Objectives {#sec-ch15-architectures}
### Downstream Applications {#sec-ch15-downstream}
## Codon-Level Models for Coding RNA {#sec-ch15-codon}
### Beyond Nucleotide Tokenization {#sec-ch15-codon-tokenization}
### What Codon Models Add {#sec-ch15-codon-advantages}
## UTR Models and Translation Regulation {#sec-ch15-utr}
### Why UTRs Dominate Expression Control {#sec-ch15-utr-control}
### Sequence-to-Expression Models {#sec-ch15-expression-models}
### Integration with mRNA Design {#sec-ch15-utr-design}
## mRNA Design and Optimization {#sec-ch15-mrna-design}
### Design Objectives and Trade-offs {#sec-ch15-design-objectives}
### Lessons from COVID-19 Vaccines {#sec-ch15-covid-vaccines}
### Model-Based Design Strategies {#sec-ch15-model-design}
## Noncoding RNA Classification and Function {#sec-ch15-ncrna}
### Diversity of Noncoding RNA {#sec-ch15-ncrna-diversity}
### From Handcrafted Features to Learned Representations {#sec-ch15-ncrna-features}
## miRNA Target Prediction {#sec-ch15-mirna}
## Splicing and Transcript Processing Models {#sec-ch15-splicing}
### Beyond SpliceAI {#sec-ch15-beyond-spliceai}
## Limitations and Open Challenges {#sec-ch15-limitations}
### Sparse Structural Data {#sec-ch15-sparse-data}
### Functional Annotation Gaps {#sec-ch15-annotation-gaps}
### Maturity Gap {#sec-ch15-maturity-gap}
## Bridge Between Sequence and Cell {#sec-ch15-bridge}

### part_4/p4-ch16-single-cell.qmd
# Single-Cell Models {#sec-ch16-single-cell}
## Single-Cell Data Landscape {#sec-ch16-data}
### From Bulk to Single-Cell Resolution {#sec-ch16-bulk-to-sc}
### Technical Challenges and Data Characteristics {#sec-ch16-technical}
## Cellular Language Models {#sec-ch16-clm}
### *Geneformer*: Learning Network Biology {#sec-ch16-geneformer}
### *scGPT*: Generative Pretraining for Single-Cell Analysis {#sec-ch16-scgpt}
### *scFoundation* and Scaling Single-Cell Models {#sec-ch16-scfoundation}
### *TranscriptFormer*: Cross-Species Cellular Models {#sec-ch16-transcriptformer}
## Perturbation Response Prediction {#sec-ch16-perturbation}
### *In Silico* Experiment Promise {#sec-ch16-in-silico}
### Perturb-seq and Foundation Model Training {#sec-ch16-perturb-seq}
### Limitations of Current Approaches {#sec-ch16-perturbation-limits}
## Epigenomic Foundation Models {#sec-ch16-epigenomic}
### DNA Methylation and *CpGPT* {#sec-ch16-methylation}
### Chromatin Accessibility Models {#sec-ch16-accessibility}
## Cross-Modality Integration {#sec-ch16-integration}
### Unpaired Integration Challenge {#sec-ch16-unpaired}
### *GLUE*: Graph-Linked Unified Embedding {#sec-ch16-glue}
### Applications of Cross-Modal Integration {#sec-ch16-cross-modal-apps}
## Practical Challenges and Limitations {#sec-ch16-limitations}
### Batch Effects and Technical Artifacts {#sec-ch16-batch-effects}
### Cell Type Imbalance {#sec-ch16-imbalance}
### Evaluation Complexity {#sec-ch16-evaluation}
### Causality and Mechanism {#sec-ch16-causality}
## From Sequence to State {#sec-ch16-conclusion}

### part_4/p4-ch17-3d-genome.qmd
# 3D Genome Organization {#sec-ch17-3d-genome}
## Chromatin Organization Hierarchy {#sec-ch17-chromatin-hierarchy}
### Chromosome Territories and Compartments {#sec-ch17-territories-compartments}
### Topologically Associating Domains {#sec-ch17-tads}
### Loop Extrusion Mechanism {#sec-ch17-loop-extrusion}
### Fine-Scale Chromatin Loops {#sec-ch17-fine-scale-loops}
## Measuring the 3D Genome {#sec-ch17-3d-measurement}
### Hi-C and Contact Matrices {#sec-ch17-hic-matrices}
### Resolution and Data Resources {#sec-ch17-3d-data-resources}
## Predicting 3D Structure from Sequence {#sec-ch17-3d-prediction}
### *Akita* and Dilated Convolutions {#sec-ch17-akita}
### *Orca* and Multiscale Prediction {#sec-ch17-orca}
### *C.Origami* and Cross-Cell-Type Transfer {#sec-ch17-c-origami}
### Learned Sequence Determinants {#sec-ch17-3d-interpretability}
## 3D Structure and Gene Regulation {#sec-ch17-3d-regulation}
### Beyond One-Dimensional Models {#sec-ch17-beyond-1d}
### Structural Variant Interpretation {#sec-ch17-sv-interpretation}
### Causality and Permissive Architecture {#sec-ch17-3d-causality}
## Spatial Transcriptomics {#sec-ch17-spatial-transcriptomics}
### Measurement Technologies {#sec-ch17-spatial-technologies}
### Computational Challenges {#sec-ch17-spatial-computation}
### Spatial Foundation Models {#sec-ch17-spatial-models}
## Limitations and Open Questions {#sec-ch17-3d-limitations}
## Structure as Context, Not Cause {#sec-ch17-structure-context}

### part_4/p4-ch18-networks.qmd
# Graph and Network Models {#sec-ch18-networks}
## Biological Networks and Data Resources {#sec-ch18-biological-networks}
### Landscape of Biological Graphs {#sec-ch18-landscape}
### Biases and Limitations {#sec-ch18-network-biases}
## Graph Neural Network Fundamentals {#sec-ch18-gnn-fundamentals}
### Message Passing Principles {#sec-ch18-message-passing}
### Canonical Architectures {#sec-ch18-canonical-architectures}
## Foundation Model Embeddings as Node Features {#sec-ch18-fm-embeddings}
### Integration Principle {#sec-ch18-integration-principle}
### Practical Integration Patterns {#sec-ch18-practical-patterns}
### Evidence for the Integration Benefit {#sec-ch18-integration-evidence}
## Applications {#sec-ch18-applications}
### Disease Gene Prioritization {#sec-ch18-disease-gene}
### Drug-Target Interaction Prediction {#sec-ch18-drug-target}
### Knowledge Graph Reasoning and Drug Repurposing {#sec-ch18-kg-reasoning}
### Pathway and Module Analysis {#sec-ch18-pathway-analysis}
### Cell Type and State Annotation {#sec-ch18-cell-annotation}
## Practical Considerations {#sec-ch18-practical}
### Graph Construction Quality {#sec-ch18-graph-construction}
### Scalability and Mini-Batching {#sec-ch18-scalability}
### Robustness to Noise and Missingness {#sec-ch18-robustness}
### Interpretation and Validation {#sec-ch18-interpretation}
## Limitations and Open Challenges {#sec-ch18-limitations}
### Study Bias Problem {#sec-ch18-study-bias}
### Causality Versus Association {#sec-ch18-causality}
### Negative Data and Class Imbalance {#sec-ch18-negative-data}
### Distribution Shift {#sec-ch18-distribution-shift}
## Sequence Encodes, Structure Connects {#sec-ch18-conclusion}

### part_4/p4-ch19-multi-omics.qmd
# Multi-Omics Integration {#sec-ch19-multi-omics}
## Limits of Single-Modality Models {#sec-ch19-limits}
## Integration Strategies and Their Tradeoffs {#sec-ch19-strategies}
### Early Fusion {#sec-ch19-early-fusion}
### Late Fusion {#sec-ch19-late-fusion}
### Intermediate Fusion {#sec-ch19-intermediate-fusion}
## Multi-Omics Foundation Models {#sec-ch19-foundation-models}
### Factor-Based Integration {#sec-ch19-factor-integration}
### Deep Generative Multi-Omics Models {#sec-ch19-deep-generative}
### Contrastive Multi-Modal Learning {#sec-ch19-contrastive}
## Clinical Integration: EHR, Imaging, and Molecular Data {#sec-ch19-clinical-integration}
### Electronic Health Records as a Modality {#sec-ch19-ehr}
### Imaging Integration {#sec-ch19-imaging}
### Multi-Modal Clinical Prediction Models {#sec-ch19-multimodal-clinical}
## Systems View: From Variant to Phenotype {#sec-ch19-systems-view}
### Information Cascade {#sec-ch19-information-cascade}
### Bottleneck Modalities {#sec-ch19-bottleneck}
### Causal vs. Correlational Integration {#sec-ch19-causal-correlational}
## Handling Missing Modalities {#sec-ch19-missing-modalities}
### Training with Incomplete Data {#sec-ch19-incomplete-training}
### Cross-Modal Imputation {#sec-ch19-imputation}
### Zero-Shot Cross-Modal Transfer {#sec-ch19-zero-shot}
## Practical Challenges {#sec-ch19-practical-challenges}
### Batch Effects Across Modalities {#sec-ch19-batch-effects}
### Sample Size and Power {#sec-ch19-sample-size}
### Interpretability Across Modalities {#sec-ch19-interpretability}
### Evaluation Complexity {#sec-ch19-evaluation}
## Integration as Means, Not End {#sec-ch19-conclusion}

### part_5/p5--eval-interp.qmd
# Part V: Evaluation and Trust {.unnumbered}

### part_5/p5-ch20-benchmarks.qmd
# Benchmarks {#sec-ch20-benchmarks}
## Protein Language Model Benchmarks {#sec-ch20-protein-benchmarks}
### TAPE: Tasks Assessing Protein Embeddings {#sec-ch20-tape}
### FLIP: Function-Linked Protein Benchmark {#sec-ch20-flip}
### ProteinGym: Comprehensive Variant Effect Evaluation {#sec-ch20-proteingym}
### Structure Prediction Benchmarks {#sec-ch20-structure-benchmarks}
## DNA and Regulatory Benchmarks {#sec-ch20-dna-benchmarks}
### Classical Regulatory Prediction Tasks {#sec-ch20-classical-regulatory}
### Quantitative Regulatory Prediction {#sec-ch20-quantitative-regulatory}
### Genomic Benchmarks {#sec-ch20-genomic-benchmarks}
### BEND: Benchmark for DNA Language Models {#sec-ch20-bend}
### Long-Range Benchmarks {#sec-ch20-long-range}
### Cross-Species Evaluation {#sec-ch20-cross-species}
## Variant Effect Prediction Benchmarks {#sec-ch20-vep-benchmarks}
### Clinical Variant Databases {#sec-ch20-clinical-databases}
### CAGI: Critical Assessment of Genome Interpretation {#sec-ch20-cagi}
### Deep Mutational Scanning Benchmarks {#sec-ch20-dms-benchmarks}
### Regulatory and Non-Coding Variant Benchmarks {#sec-ch20-noncoding-benchmarks}
## Trait and Population-Level Benchmarks {#sec-ch20-trait-benchmarks}
### Polygenic Score Evaluation {#sec-ch20-pgs-evaluation}
### TraitGym {#sec-ch20-traitgym}
### EmbedGEM Framework {#sec-ch20-embedgem}
## Benchmark Construction and Hidden Assumptions {#sec-ch20-benchmark-construction}
### Data Sources and Label Provenance {#sec-ch20-label-provenance}
### Splitting Strategies and Leakage {#sec-ch20-splitting}
### Metric Selection and Aggregation {#sec-ch20-metrics}
### Goodhart's Law and Benchmark Gaming {#sec-ch20-goodhart}
## Benchmark Saturation and Staleness {#sec-ch20-saturation-staleness}
### Saturation: When Benchmarks Stop Discriminating {#sec-ch20-saturation}
### Staleness: When Benchmarks Diverge from Practice {#sec-ch20-staleness}
### Leakage from Scale {#sec-ch20-leakage-scale}
## Benchmark-Deployment Gap {#sec-ch20-deployment-gap}
### Distribution Shift {#sec-ch20-distribution-shift}
### Calibration Requirements {#sec-ch20-calibration-requirements}
### Metric Mismatch {#sec-ch20-metric-mismatch}
### Practical Constraints {#sec-ch20-practical-constraints}
## Systematic Gaps in Current Benchmarks {#sec-ch20-systematic-gaps}
## The Proxy Problem {#sec-ch20-proxy-problem}

### part_5/p5-ch21-eval.qmd
# Evaluation Principles {#sec-ch21-eval}
## Why Random Splits Fail {#sec-ch21-random-splits-fail}
## Homology-Aware Splitting {#sec-ch21-homology-aware-splitting}
### Clustering Tools and Workflows {#sec-ch21-clustering-tools}
# Cluster proteins at 40% identity
# Cluster nucleotides at 90% identity  
# Create database and cluster at 30% identity
### Practical Considerations {#sec-ch21-homology-practical}
## Splitting by Biological Axis {#sec-ch21-splitting-biological-axis}
### Splitting by Individual {#sec-ch21-splitting-individual}
### Splitting by Genomic Region {#sec-ch21-splitting-genomic-region}
### Splitting by Gene or Protein Family {#sec-ch21-splitting-gene-family}
### Splitting by Experimental Context {#sec-ch21-splitting-experimental-context}
### Splitting by Ancestry {#sec-ch21-splitting-ancestry}
### Splitting by Time {#sec-ch21-splitting-time}
## Leakage Taxonomy and Detection {#sec-ch21-leakage-detection}
### Label Leakage {#sec-ch21-label-leakage}
### Feature Leakage {#sec-ch21-feature-leakage}
### Temporal Leakage {#sec-ch21-temporal-leakage}
### Benchmark Leakage {#sec-ch21-benchmark-leakage}
### Detecting Leakage {#sec-ch21-detecting-leakage}
## Metrics for Genomic Tasks {#sec-ch21-metrics-genomic-tasks}
### Discrimination Metrics {#sec-ch21-discrimination-metrics}
### Regression and Correlation Metrics {#sec-ch21-regression-correlation-metrics}
### Ranking and Prioritization Metrics {#sec-ch21-ranking-prioritization-metrics}
### Clinical Utility Metrics {#sec-ch21-clinical-utility-metrics}
## Baseline Selection {#sec-ch21-baseline-selection}
### Strong Baselines, Not Straw Men {#sec-ch21-strong-baselines}
### Historical Baselines and Progress Tracking {#sec-ch21-historical-baselines}
### Non-Deep-Learning Baselines {#sec-ch21-non-dl-baselines}
## Ablation Studies {#sec-ch21-ablation-studies}
### Component Isolation {#sec-ch21-component-isolation}
### Hyperparameter Sensitivity {#sec-ch21-hyperparameter-sensitivity}
### Architecture Search Confounds {#sec-ch21-architecture-search-confounds}
### Reporting Standards {#sec-ch21-reporting-standards}
## Statistical Rigor {#sec-ch21-statistical-rigor}
### Significance Testing {#sec-ch21-significance-testing}
### Effect Sizes {#sec-ch21-effect-sizes}
### Confidence Intervals on Metrics {#sec-ch21-confidence-intervals}
### Variance Across Random Seeds {#sec-ch21-variance-random-seeds}
## Evaluating Foundation Models {#sec-ch21-evaluating-fm}
### Zero-Shot Evaluation {#sec-ch21-zero-shot-eval}
### Linear Probing {#sec-ch21-linear-probing}
### Fine-Tuning Evaluation {#sec-ch21-fine-tuning-eval}
### Transfer Across Tasks {#sec-ch21-transfer-tasks}
## Calibration Essentials {#sec-ch21-calibration}
### Assessing Calibration {#sec-ch21-assessing-calibration}
### Recalibration Methods {#sec-ch21-recalibration-methods}
### Calibration in Model Comparison {#sec-ch21-calibration-comparison}
## Putting It All Together {#sec-ch21-putting-together}
## The Question Behind the Metric {#sec-ch21-question-behind-metric}

### part_5/p5-ch22-confounding.qmd
# Confounders and Leakage {#sec-ch22-confounding}
## Confounding, Bias, and Leakage {#sec-ch22-terminology}
## Sources of Confounding in Genomic Data {#sec-ch22-sources}
### Population Structure and Relatedness {#sec-ch22-ancestry-confounding}
### Technical Batch Effects {#sec-ch22-batch-effects}
### Institutional and Recruitment Confounding {#sec-ch22-institutional-confounding}
### Label Generation Bias {#sec-ch22-label-bias}
### Temporal Drift {#sec-ch22-temporal-drift}
### Resource Overlap and Indirect Leakage {#sec-ch22-resource-overlap}
## Population Structure as a Shortcut {#sec-ch22-population-shortcut}
## Technical Artifacts as Biological Signal {#sec-ch22-technical-artifacts}
## Label Bias and Circularity {#sec-ch22-label-circularity}
## Data Splitting {#sec-ch22-data-splitting}
### Random Individual-Level Splits {#sec-ch22-random-splits}
### Family-Aware Splits {#sec-ch22-family-splits}
### Locus-Level Splits {#sec-ch22-locus-splits}
### Region and Chromosome Splits {#sec-ch22-region-splits}
### Cohort and Site Splits {#sec-ch22-cohort-splits}
### Temporal Splits {#sec-ch22-temporal-splits}
### Indirect Leakage Across Resources {#sec-ch22-indirect-leakage}
## Data Leakage as Confounding {#sec-ch22-leakage-confounding}
### Causal Structure of Leakage {#sec-ch22-leakage-causal}
### Compounding Effects {#sec-ch22-compounding}
### Implications for Confounding Analysis {#sec-ch22-leakage-implications}
## Detecting Confounding {#sec-ch22-detection}
### Confounder-Only Baselines {#sec-ch22-confounder-baselines}
### Stratified Performance Analysis {#sec-ch22-stratified-performance}
### Residual Confounder Associations {#sec-ch22-residual-associations}
### Split Sensitivity Analysis {#sec-ch22-split-sensitivity}
### Negative Control Outcomes {#sec-ch22-negative-controls}
## Mitigation Strategies {#sec-ch22-mitigation}
### Study Design and Cohort Construction {#sec-ch22-study-design}
### Covariate Adjustment {#sec-ch22-covariate-adjustment}
### Domain Adaptation and Invariance Learning {#sec-ch22-domain-adaptation}
### Data Curation and Benchmark Design {#sec-ch22-benchmark-design}
### Causal Inference Approaches {#sec-ch22-causal-inference}
## Fairness and External Validity {#sec-ch22-fairness}
## A Practical Checklist {#sec-ch22-checklist}
## Rigor as Response {#sec-ch22-rigor}

### part_5/p5-ch23-uncertainty.qmd
# Uncertainty Quantification {#sec-ch23-uncertainty}
## Types of Uncertainty in Genomic Prediction {#sec-ch23-types}
### Why Uncertainty Matters {#sec-ch23-why-uncertainty}
### Epistemic Uncertainty {#sec-ch23-epistemic}
### Aleatoric Uncertainty {#sec-ch23-aleatoric}
### Decomposing Total Uncertainty {#sec-ch23-decomposition}
## Calibration and Confidence Interpretation {#sec-ch23-calibration}
### The Calibration Problem {#sec-ch23-calibration-problem}
### Measuring Calibration {#sec-ch23-measuring-calibration}
### Why Foundation Models Are Often Miscalibrated {#sec-ch23-fm-miscalibration}
### Calibration Across Subgroups {#sec-ch23-subgroup-calibration}
## Post-Hoc Calibration Methods {#sec-ch23-post-hoc-calibration}
### Temperature Scaling {#sec-ch23-temperature-scaling}
### Platt Scaling {#sec-ch23-platt-scaling}
### Isotonic Regression {#sec-ch23-isotonic-regression}
### Calibrating Foundation Model Outputs {#sec-ch23-calibrating-fm}
## Uncertainty Quantification Methods for Foundation Models {#sec-ch23-uq-methods}
### Deep Ensembles {#sec-ch23-deep-ensembles}
### Monte Carlo Dropout {#sec-ch23-mc-dropout}
### Heteroscedastic Models {#sec-ch23-heteroscedastic}
### Evidential Deep Learning {#sec-ch23-evidential}
### Selecting Uncertainty Quantification Methods {#sec-ch23-selecting-uq}
## Conformal Prediction: Distribution-Free Guarantees {#sec-ch23-conformal}
### Split Conformal Prediction {#sec-ch23-split-conformal}
### Conformal Prediction for Variant Classification {#sec-ch23-conformal-variant}
### Limitations and Practical Considerations {#sec-ch23-conformal-limitations}
### Integration with Clinical Workflows {#sec-ch23-conformal-clinical}
## Out-of-Distribution Detection {#sec-ch23-ood-detection}
### Out-of-Distribution Problem {#sec-ch23-ood-problem}
### Likelihood-Based Detection and Its Failures {#sec-ch23-likelihood-ood}
### Embedding-Based Detection {#sec-ch23-embedding-ood}
### Practical OOD Detection for Genomic Applications {#sec-ch23-practical-ood}
## Selective Prediction and Abstention {#sec-ch23-selective-prediction}
### When to Abstain {#sec-ch23-when-abstain}
### Selective Prediction Methods {#sec-ch23-selective-methods}
### Evaluating Selective Prediction {#sec-ch23-selective-eval}
## Uncertainty for Specific Genomic Tasks {#sec-ch23-genomic-uq}
### Variant Effect Prediction Uncertainty {#sec-ch23-vep-uncertainty}
### Regulatory Variant Uncertainty {#sec-ch23-regulatory-uncertainty}
### Uncertainty Across Populations {#sec-ch23-population-uncertainty}
## Communicating Uncertainty to End Users {#sec-ch23-communication}
### Communication Challenge {#sec-ch23-communication-challenge}
### Categorical Reporting {#sec-ch23-categorical-reporting}
### Visual Communication {#sec-ch23-visual-communication}
### Decision-Theoretic Framing {#sec-ch23-decision-framing}
## Necessary but Insufficient {#sec-ch23-conclusion}

### part_5/p5-ch24-interpretability.qmd
# Interpretability {#sec-ch24-interpretability}
## Attribution Methods and Input Importance {#sec-ch24-attribution}
### *In Silico* Mutagenesis {#sec-ch24-ism}
### Gradient-Based Attribution {#sec-ch24-gradient}
### Reconciling Attribution Methods {#sec-ch24-reconciling}
## Interpreting Convolutional Filters {#sec-ch24-cnn-filters}
### From Filters to Position Weight Matrices {#sec-ch24-filter-pwm}
### Deeper Layers and Combinatorial Patterns {#sec-ch24-deeper-layers}
## Motif Discovery from Attributions {#sec-ch24-motif-discovery}
## Probing Learned Representations {#sec-ch24-probing}
### Probing Methodology {#sec-ch24-probing-methods}
### Limitations of Probing {#sec-ch24-probing-limits}
## Attention Patterns in Transformer Models {#sec-ch24-attention}
### What Attention Patterns Reveal {#sec-ch24-attention-patterns}
### Why Attention Weights Mislead {#sec-ch24-attention-caution}
## Regulatory Vocabularies and Global Interpretability {#sec-ch24-global}
### Sequence Classes from *Sei* {#sec-ch24-sei}
### Embedding Geometry and Regulatory Programs {#sec-ch24-embedding-geometry}
## Mechanistic Interpretability {#sec-ch24-mechanistic}
### Circuits and Features {#sec-ch24-circuits}
### Applications to Genomic Models {#sec-ch24-mechanistic-genomics}
## Validation: From Explanations to Experiments {#sec-ch24-validation}
### Faithfulness Testing {#sec-ch24-faithfulness}
### Experimental Validation {#sec-ch24-experimental}
## Interpretability in Clinical Variant Assessment {#sec-ch24-clinical}
## Practical Approaches for Foundation Model Analysis {#sec-ch24-practical}
## Plausibility Is Not Faithfulness {#sec-ch24-conclusion}

### part_6/p6--translation.qmd
# Part VI: Clinical Translation {#sec-part6-intro}

### part_6/p6-ch25-clinical-risk.qmd
# Clinical Risk Prediction {#sec-ch25-clinical-risk}
## From Polygenic Scores to Foundation Model Features {#sec-ch25-pgs-to-fm}
## Defining Clinical Risk Prediction {#sec-ch25-defining-risk}
## Feature Integration Architectures {#sec-ch25-feature-integration}
## EHR Integration and Phenotype Embeddings {#sec-ch25-ehr-integration}
### EEPRS Framework {#sec-ch25-eeprs}
### Understanding When Embeddings Help {#sec-ch25-embeddings-help}
### PRS-PheWAS for Clinical Interpretation {#sec-ch25-prs-phewas}
### Implementation Considerations {#sec-ch25-eeprs-implementation}
### Integration with Foundation Model Features {#sec-ch25-eeprs-fm}
## Temporal Modeling Architectures {#sec-ch25-temporal-modeling}
## Evaluation for Clinical Deployment {#sec-ch25-evaluation}
### Discrimination {#sec-ch25-discrimination}
### Calibration {#sec-ch25-calibration}
### Clinical Utility {#sec-ch25-clinical-utility}
### Validation Hierarchy {#sec-ch25-validation-hierarchy}
## Uncertainty Quantification {#sec-ch25-uncertainty}
## Fairness and Health Equity {#sec-ch25-fairness}
## Clinical Integration {#sec-ch25-clinical-integration}
### Workflow Integration Patterns {#sec-ch25-workflow-patterns}
### System Architecture {#sec-ch25-system-architecture}
### Post-Deployment Monitoring {#sec-ch25-monitoring}
## Regulatory and Quality Frameworks {#sec-ch25-regulatory}
## Case Studies {#sec-ch25-case-studies}
### Cardiometabolic Risk Stratification {#sec-ch25-case-cardio}
### Oncology Prognosis {#sec-ch25-case-oncology}
### Pharmacogenomic Adverse Event Prediction {#sec-ch25-case-pharmacogenomics}
## Translation as the Test {#sec-ch25-translation-test}

### part_6/p6-ch26-rare-disease.qmd
# Rare Disease Diagnosis {#sec-ch26-rare-disease}
## Variant Prioritization Funnel {#sec-ch26-prioritization-funnel}
### Quality and Technical Filters {#sec-ch26-quality-filters}
### Population Frequency Filters {#sec-ch26-frequency-filters}
### Consequence and Gene Filters {#sec-ch26-consequence-filters}
### Foundation Model Scoring {#sec-ch26-fm-scoring}
## ACMG-AMP Criteria and Computational Evidence {#sec-ch26-acmg-amp}
### Evidence Categories {#sec-ch26-evidence-categories}
### PP3 and BP4: Computational Evidence {#sec-ch26-pp3-bp4}
### Calibrating Predictions to Evidence Strength {#sec-ch26-calibration}
## Family-Based Analysis {#sec-ch26-family-analysis}
### *De Novo* Variants {#sec-ch26-de-novo}
### Compound Heterozygosity and Phasing {#sec-ch26-compound-het}
### Segregation Analysis {#sec-ch26-segregation}
## Somatic Variant Interpretation in Cancer {#sec-ch26-somatic}
### Germline versus Somatic Distinction {#sec-ch26-germline-somatic}
### Driver Classification {#sec-ch26-driver}
### Therapeutic Biomarkers {#sec-ch26-biomarkers}
## Laboratory Validation {#sec-ch26-validation}
### Types of Functional Assays {#sec-ch26-assay-types}
### Integrating Functional Evidence {#sec-ch26-functional-integration}
### Closing the VUS Loop {#sec-ch26-vus-loop}
## Practical Workflow Integration {#sec-ch26-workflow}
### Laboratory Workflow {#sec-ch26-lab-workflow}
### Clinical Decision-Making {#sec-ch26-clinical-decisions}
### Regulatory and Ethical Considerations {#sec-ch26-regulatory}
## Interpretive Partnership {#sec-ch26-partnership}

### part_6/p6-ch27-drug-discovery.qmd
# Drug Discovery {#sec-ch27-drug-discovery}
## Genetic Foundation of Target Selection {#sec-ch27-genetic-foundation}
### From Variant-Level Predictions to Gene-Level Evidence {#sec-ch27-variant-to-gene}
### Linking Genetics to Target Safety and Efficacy {#sec-ch27-safety-efficacy}
## Network-Aware Target Discovery and Repurposing {#sec-ch27-network-discovery}
### Propagating Genetic Signals Through Networks {#sec-ch27-network-propagation}
### Drug Repurposing Through Shared Representations {#sec-ch27-repurposing}
## Drug-Target Interaction Prediction {#sec-ch27-dti-prediction}
### Representing Targets for Binding Prediction {#sec-ch27-binding-prediction}
### Selectivity and Off-Target Prediction {#sec-ch27-selectivity}
## Toxicity Prediction from Genomic Context {#sec-ch27-toxicity}
### Genetic Evidence of Target Liabilities {#sec-ch27-genetic-liabilities}
### Expression-Based Toxicity Prediction {#sec-ch27-expression-toxicity}
### Integrating Genomic Context with Chemical Properties {#sec-ch27-integrated-toxicity}
## Functional Genomics Screens and Perturbation Models {#sec-ch27-functional-screens}
### Designing Informative Perturbation Libraries {#sec-ch27-library-design}
### Perturb-seq and Transcriptomic Readouts {#sec-ch27-perturb-seq}
### Closing the Loop: Lab-in-the-Loop Refinement {#sec-ch27-lab-in-loop}
## Biomarker Development and Patient Stratification {#sec-ch27-biomarkers}
### Foundation Model Features for Stratification {#sec-ch27-stratification-features}
### Multi-Omic Biomarker Discovery {#sec-ch27-multi-omic-biomarkers}
### Trial Design and Endpoint Selection {#sec-ch27-trial-design}
## Industry Workflows and Infrastructure {#sec-ch27-industry-workflows}
### Building Model Infrastructure {#sec-ch27-model-infrastructure}
### Strategic Choices: Build, Buy, or Fine-Tune {#sec-ch27-build-buy-finetune}
### Industry Context: Timelines and Decision Gates {#sec-ch27-timelines}
### Intellectual Property and Data Considerations {#sec-ch27-ip-data}
## Evaluation and Validation {#sec-ch27-evaluation}
### Benchmark Limitations {#sec-ch27-benchmark-limits}
### From Prediction to Validation {#sec-ch27-prediction-validation}
## Connections to Molecular Design {#sec-ch27-molecular-design}
## Prioritization, Not Automation {#sec-ch27-conclusion}

### part_6/p6-ch28-design.qmd
# Sequence Design {#sec-ch28-design}
## Design Formalism {#sec-ch28-formalism}
## Protein Design with Language Models {#sec-ch28-protein-design}
### Sequence Generation from Language Model Priors {#sec-ch28-plm-generation}
### Structure-Aware Design with Diffusion Models {#sec-ch28-structure-diffusion}
### Functional Conditioning and Multi-Objective Optimization {#sec-ch28-multi-objective}
## Regulatory Sequence Design {#sec-ch28-regulatory-design}
### Promoter and Enhancer Engineering {#sec-ch28-promoter-enhancer}
### Splicing and RNA Processing Elements {#sec-ch28-splicing-design}
## mRNA Design and Optimization {#sec-ch28-mrna-design}
### Codon Optimization Principles {#sec-ch28-codon-optimization}
### Stability Engineering and UTR Design {#sec-ch28-utr-design}
### Immunogenicity Considerations {#sec-ch28-mrna-immunogenicity}
## Antibody and Vaccine Design {#sec-ch28-antibody-vaccine}
### CDR Optimization and Humanization {#sec-ch28-cdr-optimization}
### Vaccine Antigen Design {#sec-ch28-vaccine-design}
## Closed-Loop Design-Build-Test-Learn Cycles {#sec-ch28-dbtl}
### Active Learning for Efficient Exploration {#sec-ch28-active-learning}
### High-Throughput Experimentation Integration {#sec-ch28-high-throughput}
## Validation Requirements and Failure Modes {#sec-ch28-validation}
### Validation Hierarchy {#sec-ch28-validation-hierarchy}
### Characteristic Failure Patterns {#sec-ch28-failure-patterns}
## Practical Design Constraints {#sec-ch28-practical-constraints}
### Manufacturing and Developability {#sec-ch28-manufacturing}
### Safety and Biosecurity Considerations {#sec-ch28-biosecurity}
## Algorithmic Search and Optimization {#sec-ch28-algorithms}
## From Understanding to Creating {#sec-ch28-conclusion}

### part_6/p6-ch29-future.qmd
# Ethics and Frontiers {#sec-ch29-future}
## Regulatory Frameworks for Genomic AI {#sec-ch29-regulatory}
### Software as Medical Device Paradigm {#sec-ch29-samd}
### European and Global Regulatory Landscapes {#sec-ch29-global-regulation}
### Validation Requirements for Clinical Genomic AI {#sec-ch29-validation}
## Data Governance and Consent {#sec-ch29-governance}
### Consent Problem at Scale {#sec-ch29-consent}
### Biobank Governance Models {#sec-ch29-biobanks}
### Secondary Use and Data Futures {#sec-ch29-secondary-use}
## Privacy and Genomic Data {#sec-ch29-privacy}
### Re-identification Challenge {#sec-ch29-reidentification}
### Family and Relational Privacy {#sec-ch29-family-privacy}
## Intellectual Property and Ownership {#sec-ch29-ip}
### Genomic Data Ownership {#sec-ch29-data-ownership}
### Model Weights as Assets {#sec-ch29-model-weights}
### Prediction Ownership and Liability {#sec-ch29-liability}
## Responsible Development Practices {#sec-ch29-responsible}
### Transparency and Documentation {#sec-ch29-transparency}
### Fairness and Performance Equity {#sec-ch29-fairness}
### Human Oversight and Decision Support {#sec-ch29-oversight}
## Dual Use and Biosecurity {#sec-ch29-biosecurity}
### Generative Models and Pathogen Enhancement {#sec-ch29-pathogen}
### Access Controls and Responsible Release {#sec-ch29-access}
## Open Technical Problems {#sec-ch29-technical}
### Scaling and Efficiency {#sec-ch29-scaling}
### Context and Multi-Scale Integration {#sec-ch29-multiscale}
### Causality and Mechanism {#sec-ch29-causality}
## Emerging Directions {#sec-ch29-emerging}
### Multimodal Integration {#sec-ch29-multimodal}
### Agentic and Closed-Loop Systems {#sec-ch29-agentic}
### Clinical Integration and Learning Health Systems {#sec-ch29-learning-health}
## Work Ahead {#sec-ch29-conclusion}

### preface.qmd
# Preface {.unnumbered}
## Why I Wrote This Book
## How This Book Came Together
## How to Read This Book
## What This Book Assumes (and What It Does Not)
## A Note on Scope and Opinions
## Acknowledgements


### appendix/app-a-dl.qmd
# Deep Learning Primer {#sec-apx-a-dl}
## Neural Networks as Function Approximators {#sec-apx-a-nn-basics}
### The Perceptron and Linear Layers
### Activation Functions
### Depth and Width
## Training Neural Networks {#sec-apx-a-training}
### Loss Functions
### Gradient Descent and Backpropagation
### Stochastic Gradient Descent and Minibatches
### Optimizers
### Regularization
## Convolutional Neural Networks {#sec-apx-a-cnn}
### Convolution Operation
### Key CNN Components
### CNNs for Genomics
## Recurrent Neural Networks {#sec-apx-a-rnn}
### LSTM and GRU
### Limitations
## Attention and Transformers {#sec-apx-a-attention}
### Self-Attention
### Multi-Head Attention
### Transformer Architecture
### Positional Encoding
### Encoder vs. Decoder
### Computational Complexity
## Embeddings and Representations {#sec-apx-a-embeddings}
### Token Embeddings
### Contextual Embeddings
## Pretraining and Transfer Learning {#sec-apx-a-pretraining}
### Self-Supervised Objectives
### Transfer Learning
## Practical Considerations {#sec-apx-a-practical}
### Hardware Requirements
### Software Frameworks
### Common Pitfalls
## Further Reading {#sec-apx-a-further}

### appendix/app-b-compute.qmd
# Deployment and Compute {#sec-apx-b-compute}
## Hardware Landscape {#sec-apx-b-hardware}
### GPU Computing
### Consumer vs. Data Center GPUs
### TPUs
### Multi-GPU and Distributed Training
### CPU Inference
## Cloud Platforms {#sec-apx-b-cloud}
### Major Providers
### Cost Considerations
### Managed ML Platforms
## Model Deployment {#sec-apx-b-deployment}
### Inference Servers
### API Design
# Request
# Response
### Containerization
### Kubernetes Deployment
## Inference Optimization {#sec-apx-b-optimization}
### Quantization
### Model Pruning
### Knowledge Distillation
### ONNX and TensorRT
### Caching and Batching
## Benchmarking and Monitoring {#sec-apx-b-monitoring}
### Performance Metrics
### Monitoring Stack
### Load Testing
# Example with locust
## Cost Optimization {#sec-apx-b-cost}
### Right-Sizing
### Autoscaling
# Kubernetes HPA example
### Batch Processing
### Model Selection
## Security Considerations {#sec-apx-b-security}
### Data Privacy
### Model Security
### Federated Learning
## Reference Architecture {#sec-apx-b-architecture}
## Checklist for Production Deployment {#sec-apx-b-checklist}

### appendix/app-c-data-curation.qmd
# Data Curation {#sec-apx-c-data-curation}
## Data Sources {#sec-apx-c-sources}
### Reference Genomes and Assemblies
### Population-Scale Sequencing
### Protein Sequence Databases
### Functional Annotation
### Clinical Variant Databases
### Access and Licensing
## Quality Filtering {#sec-apx-c-quality}
### Sequence Quality Filters
### Variant Quality Filters
### Annotation Quality
### Handling Missing Data
## Deduplication {#sec-apx-c-dedup}
### Exact Deduplication
### Near-Duplicate Detection
# Cluster at 90% sequence identity
# Cluster at 50% identity (requires different word size)
### Redundancy Levels
### Train-Test Deduplication
## Contamination Detection {#sec-apx-c-contamination}
### Types of Contamination
### Screening Approaches
# Screen against human genome for non-human samples
### Benchmark Contamination
## Data Provenance {#sec-apx-c-provenance}
### Metadata Requirements
### Documentation Template
# data_manifest.yaml
### Version Control
## Bias Assessment {#sec-apx-c-bias}
### Population Bias
### Gene Coverage Bias
### Ascertainment Bias
### Label Bias
## Building Training Sets {#sec-apx-c-building}
### Step 1: Define Scope
### Step 2: Identify Sources
### Step 3: Download and Verify
# Download with verification
# Document in manifest
### Step 4: Quality Filter
### Step 5: Deduplicate
### Step 6: Split Data
### Step 7: Assess Bias
### Step 8: Document
## Data Cards {#sec-apx-c-datacards}
# Dataset: VariantBench-v2
## Overview
## Sources
## Curation
## Known Biases
## Intended Use
## Updates
## Checklist {#sec-apx-c-checklist}

### appendix/app-d-models.qmd
# Model Reference {#sec-apx-d-models}
## DNA Language Models {#sec-apx-d-dna-lm}
### Model Access
## Protein Language Models {#sec-apx-d-plm}
### Model Access
## Sequence-to-Function Models {#sec-apx-d-seq2func}
### Model Access
## Splice Prediction Models {#sec-apx-d-splice}
### Model Access
## Variant Effect Predictors {#sec-apx-d-vep}
### Integrative Scores
### Protein Language Model–Based
### Conservation-Based
### Model Access
## Structure Prediction {#sec-apx-d-structure}
### Model Access
## Single-Cell and Multi-Omics Models {#sec-apx-d-singlecell}
## Polygenic and Clinical Models {#sec-apx-d-clinical}
## Category Definitions {#sec-apx-d-categories}
## Practical Considerations {#sec-apx-d-practical}
### Selecting a Model
### Model Versioning

### appendix/app-e-resources.qmd
# Resources {#sec-apx-e-resources}
## Textbooks {#sec-apx-e-textbooks}
### Genomics and Human Genetics
### Immunology
### Machine Learning and Deep Learning
### Bioinformatics and Computational Biology
## Online Courses {#sec-apx-e-courses}
### Machine Learning and Deep Learning
### Genomics and Bioinformatics
### Applied Genomic ML
## Genomic Databases {#sec-apx-e-databases}
### Variant and Population Databases
### Functional Annotation Databases
### Protein Databases
### Gene and Pathway Databases
### Single-Cell Databases
## Software Tools {#sec-apx-e-software}
### Sequence Analysis
### Variant Annotation
### Deep Learning Frameworks
### Genomic ML Libraries
### Workflow Management
## Benchmarks and Datasets {#sec-apx-e-benchmarks}
### Genomic Benchmarks
### Variant Datasets
## Community and Forums {#sec-apx-e-community}
### Discussion Forums
### Preprint Servers
### Conferences
### Key Research Groups
## Keeping Current {#sec-apx-e-current}

### appendix/app-f-glossary.qmd
# Glossary {#sec-apx-f-glossary}
## Terms (A–Z)

### bib/references.qmd
# References {.unnumbered}

### index.qmd
# Introduction {.unnumbered}
## How to Use This Book
## Why Foundation Models for Genomics?
## Recurring Themes
## Core Questions This Book Addresses
## Typography and Formatting {.unnumbered}
## Structure and Organization
## A Framework, Not a Snapshot
## What You Will Be Able to Do

### part_1/p1--foundations.qmd
# Part I: Data Foundations {.unnumbered}
## Part I at a Glance
## Connections to Later Parts

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
### Sequence Databases {#sec-ch02-protein-sequence}
### Structure Databases {#sec-ch02-protein-structure}
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
### Quantifying Polygenicity: The M50% Metric {#sec-ch03-m50-metric}
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

### part_2/p2--architectures.qmd
# Part II: Architectures {.unnumbered}
## Part II at a Glance
## Connections to Other Parts

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

### part_3/p3--learning.qmd
# Part III: Learning & Evaluation {.unnumbered}
## Part III at a Glance
## Connections to Other Parts

### part_3/p3-ch08-pretraining.qmd
# Pretraining Strategies {#sec-ch08-pretraining}
## Chapter Overview
## Masked Language Modeling {#sec-ch08-mlm}
## Key Insight: What MLM Prediction Difficulty Reveals
### Masking Strategies and Their Implications {#sec-ch08-mlm-strategies}
## Stop and Think
### What Masked Language Models Learn {#sec-ch08-mlm-learning}
## Next-Token Prediction {#sec-ch08-autoregressive}
## Mathematical Detail
### Genomic Applications {#sec-ch08-autoregressive-genomics}
## MLM and Autoregressive Comparison {#sec-ch08-comparison}
## Key Insight: Alignment Principle
### Hybrid Architectures {#sec-ch08-hybrid}
## Span Corruption and Denoising {#sec-ch08-denoising}
### Corruption Beyond Masking {#sec-ch08-corruption}
### Biologically Motivated Corruption {#sec-ch08-biological-corruption}
## Contrastive Learning {#sec-ch08-contrastive}
## Stop and Think
### Augmentation Design for Genomic Sequences {#sec-ch08-augmentation}
### Cross-Species Contrastive Learning {#sec-ch08-cross-species}
## Multi-Task Pretraining {#sec-ch08-multitask}
### Task Selection and Architecture {#sec-ch08-task-selection}
### Loss Weighting and Balancing {#sec-ch08-loss-weighting}
## Technical Challenge
### Large-Scale Multi-Task Examples {#sec-ch08-multitask-examples}
### When Multi-Task Learning Fails {#sec-ch08-multitask-failure}
## Stop and Think
## Staged Pretraining Strategies {#sec-ch08-staged}
### Context Length Curricula {#sec-ch08-context-curriculum}
### Domain-Adaptive Pretraining {#sec-ch08-domain-adaptive}
### Continued Pretraining on Expanded Data {#sec-ch08-continued-pretraining}
## Practical Guidance
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
## Advanced Topic
## Training Diagnostics {#sec-ch08-diagnostics}
### Monitoring Loss and Gradients {#sec-ch08-monitoring}
### Functional Probing {#sec-ch08-probing}
## Strategy Selection {#sec-ch08-selection}
## Practical Guidance: Decision Tree for Objective Selection
## Pretraining in Practice: Case Studies {#sec-ch08-case-studies}
### DNABERT {#sec-ch08-dnabert}
### HyenaDNA {#sec-ch08-hyenadna}
### Enformer {#sec-ch08-enformer}
### ESM-2 {#sec-ch08-esm2}
## Open Questions {#sec-ch08-open-questions}
## From Sequence Statistics to Biological Knowledge {#sec-ch08-sequence-to-knowledge}
## Chapter Summary

### part_3/p3-ch09-transfer.qmd
# Transfer Learning Foundations {#sec-ch09-transfer}
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
## Summary {#sec-ch09-summary}

### part_3/p3-ch10-adaptation.qmd
# Adaptation Strategies {#sec-ch10-adaptation}
## Chapter Overview
## Parameter-Efficient Fine-Tuning {#sec-ch10-peft}
### Low-Rank Adaptation {#sec-ch10-lora}
## Key Insight: Why Low-Rank Works
### Configuring Low-Rank Adaptation {#sec-ch10-lora-config}
## Stop and Think
## Practical Guidance: LoRA Configuration Checklist
## Layer Selection for Embedding Extraction {#sec-ch10-layer-selection}
### The Encoder Advantage
### The Decoder Dilemma
## Difficulty Warning
### Practical Consequences
### Layer Averaging and Weighted Combinations
### Systematic Layer Probing
### Implications for Model Selection
### Cross-Reference to Pretraining Objectives
## Full Fine-Tuning {#sec-ch10-full-finetuning}
### Making Full Fine-Tuning Work {#sec-ch10-full-finetuning-practice}
### The `[CLS]` Token and Sequence Aggregation {#sec-ch10-cls-token}
## Stop and Think
### Mean Pooling and Alternatives
## Key Insight: Matching Aggregation to Information Distribution
### Practical Considerations for Genomic Sequences
## Choosing an Adaptation Strategy {#sec-ch10-choosing-strategy}
## Domain Shift and Cross-Context Transfer {#sec-ch10-domain-shift}
### Types of Domain Shift in Genomics {#sec-ch10-domain-shift-types}
## Stop and Think
### Detecting and Mitigating Shift {#sec-ch10-detecting-shift}
## Minimal-Data and Emerging Transfer Paradigms {#sec-ch10-minimal-data}
### Few-Shot Learning with Minimal Examples {#sec-ch10-few-shot}
### Zero-Shot Transfer Without Task-Specific Data {#sec-ch10-zero-shot}
## Key Insight: When Zero-Shot Works
### Emerging Approaches {#sec-ch10-emerging-approaches}
### Toward Theoretical Foundations {#sec-ch10-theory}
## Label and Class Imbalance {#sec-ch10-label-imbalance}
## Difficulty Warning
### Manifestations During Transfer
### Mitigation Strategies
## Practical Guidance: Imbalance Mitigation Checklist
### Evaluation Under Imbalance
### Imbalance as Fundamental Constraint
## Diagnosing Transfer: Validation and Failure Modes {#sec-ch10-diagnosing-transfer}
### Diagnosing Negative Transfer {#sec-ch10-negative-transfer}
### Validation and Common Pitfalls {#sec-ch10-validation-pitfalls}
### Sources of Spurious Success {#sec-ch10-spurious-success}
## Stop and Think
## Case Studies in Transfer Learning {#sec-ch10-case-studies}
### Successful Transfer: Alignment Between Pretraining and Task {#sec-ch10-case-success}
### When Transfer Fails: Cross-Species Prediction {#sec-ch10-case-failure}
## What Transfers, What Breaks {#sec-ch10-conclusion}
## Chapter Summary

### part_3/p3-ch11-benchmarks.qmd
# Benchmark Landscape {#sec-ch11-benchmarks}
## Chapter Overview
## Protein Language Model Benchmarks {#sec-ch11-protein-benchmarks}
### TAPE: Tasks Assessing Protein Embeddings {#sec-ch11-tape}
## Key Insight: The Transfer Learning Evaluation Framework
### FLIP: Function-Linked Protein Benchmark {#sec-ch11-flip}
## Stop and Think: Splitting Strategy Implications
### ProteinGym: Comprehensive Variant Effect Evaluation {#sec-ch11-proteingym}
### Structure Prediction Benchmarks {#sec-ch11-structure-benchmarks}
## DNA and Regulatory Benchmarks {#sec-ch11-dna-benchmarks}
### Classical Regulatory Prediction Tasks {#sec-ch11-classical-regulatory}
## Limitation Alert: Binary Classification Over Short Windows
### Quantitative Regulatory Prediction {#sec-ch11-quantitative-regulatory}
### Genomic Benchmarks {#sec-ch11-genomic-benchmarks}
### BEND: Benchmark for DNA Language Models {#sec-ch11-bend}
### Long-Range Benchmarks {#sec-ch11-long-range}
### Cross-Species Evaluation {#sec-ch11-cross-species}
## Variant Effect Prediction Benchmarks {#sec-ch11-vep-benchmarks}
### Clinical Variant Databases {#sec-ch11-clinical-databases}
## Critical Limitation: ClinVar Circularity
### CAGI: Critical Assessment of Genome Interpretation {#sec-ch11-cagi}
## Key Insight: The Value of Prospective Evaluation
### Deep Mutational Scanning Benchmarks {#sec-ch11-dms-benchmarks}
### Regulatory and Non-Coding Variant Benchmarks {#sec-ch11-noncoding-benchmarks}
## Trait and Population-Level Benchmarks {#sec-ch11-trait-benchmarks}
### Polygenic Score Evaluation {#sec-ch11-pgs-evaluation}
### TraitGym {#sec-ch11-traitgym}
### EmbedGEM Framework {#sec-ch11-embedgem}
## Benchmark Construction and Hidden Assumptions {#sec-ch11-benchmark-construction}
### Data Sources and Label Provenance {#sec-ch11-label-provenance}
## Stop and Think: Label Provenance
### Splitting Strategies and Leakage {#sec-ch11-splitting}
### Metric Selection and Aggregation {#sec-ch11-metrics}
### Goodhart's Law and Benchmark Gaming {#sec-ch11-goodhart}
## Benchmark Saturation and Staleness {#sec-ch11-saturation-staleness}
### Saturation: When Benchmarks Stop Discriminating {#sec-ch11-saturation}
### Staleness: When Benchmarks Diverge from Practice {#sec-ch11-staleness}
### Leakage from Scale {#sec-ch11-leakage-scale}
## Benchmark-Deployment Gap {#sec-ch11-deployment-gap}
### Distribution Shift {#sec-ch11-distribution-shift}
### Calibration Requirements {#sec-ch11-calibration-requirements}
### Metric Mismatch {#sec-ch11-metric-mismatch}
### Practical Constraints {#sec-ch11-practical-constraints}
## Systematic Gaps in Current Benchmarks {#sec-ch11-systematic-gaps}
## The Proxy Problem {#sec-ch11-proxy-problem}
## Chapter Summary

### part_3/p3-ch12-evaluation.qmd
# Evaluation Methods {#sec-ch12-eval}
## Chapter Overview
## Difficulty Warning: Methodological Rigor
## Why Random Splits Fail {#sec-ch12-random-splits-fail}
## Key Insight: The Independence Assumption
## Homology-Aware Splitting {#sec-ch12-homology-aware-splitting}
### Clustering Tools and Workflows {#sec-ch12-clustering-tools}
## Practical Guidance: Choosing Identity Thresholds
### Practical Considerations {#sec-ch12-homology-practical}
## Splitting by Biological Axis {#sec-ch12-splitting-biological-axis}
### Splitting by Individual {#sec-ch12-splitting-individual}
### Splitting by Genomic Region {#sec-ch12-splitting-genomic-region}
### Splitting by Gene or Protein Family {#sec-ch12-splitting-gene-family}
## Stop and Think: Choosing the Right Split
### Splitting by Experimental Context {#sec-ch12-splitting-experimental-context}
### Splitting by Ancestry {#sec-ch12-splitting-ancestry}
### Splitting by Time {#sec-ch12-splitting-time}
## Leakage Taxonomy and Detection {#sec-ch12-leakage-detection}
### Label Leakage {#sec-ch12-label-leakage}
### Feature Leakage {#sec-ch12-feature-leakage}
### Temporal Leakage {#sec-ch12-temporal-leakage}
### Benchmark Leakage {#sec-ch12-benchmark-leakage}
### Detecting Leakage {#sec-ch12-detecting-leakage}
## Practical Guidance: Leakage Detection Checklist
## Metrics for Genomic Tasks {#sec-ch12-metrics-genomic-tasks}
### Discrimination Metrics {#sec-ch12-discrimination-metrics}
## Key Insight: Why auROC Can Mislead
### Regression and Correlation Metrics {#sec-ch12-regression-correlation-metrics}
### Ranking and Prioritization Metrics {#sec-ch12-ranking-prioritization-metrics}
### Clinical Utility Metrics {#sec-ch12-clinical-utility-metrics}
## Baseline Selection {#sec-ch12-baseline-selection}
### Strong Baselines, Not Straw Men {#sec-ch12-strong-baselines}
### Historical Baselines and Progress Tracking {#sec-ch12-historical-baselines}
### Non-Deep-Learning Baselines {#sec-ch12-non-dl-baselines}
## Ablation Studies {#sec-ch12-ablation-studies}
### Component Isolation {#sec-ch12-component-isolation}
### Hyperparameter Sensitivity {#sec-ch12-hyperparameter-sensitivity}
### Architecture Search Confounds {#sec-ch12-architecture-search-confounds}
### Reporting Standards {#sec-ch12-reporting-standards}
## Statistical Rigor {#sec-ch12-statistical-rigor}
## Two Cultures: Inference vs. Prediction
### Significance Testing {#sec-ch12-significance-testing}
### Effect Sizes {#sec-ch12-effect-sizes}
### Confidence Intervals on Metrics {#sec-ch12-confidence-intervals}
### Variance Across Random Seeds {#sec-ch12-variance-random-seeds}
## Evaluating Foundation Models {#sec-ch12-evaluating-fm}
### Zero-Shot Evaluation {#sec-ch12-zero-shot-eval}
### Linear Probing {#sec-ch12-linear-probing}
### Fine-Tuning Evaluation {#sec-ch12-fine-tuning-eval}
### Transfer Across Tasks {#sec-ch12-transfer-tasks}
## Calibration Essentials {#sec-ch12-calibration}
### Assessing Calibration {#sec-ch12-assessing-calibration}
### Recalibration Methods {#sec-ch12-recalibration-methods}
### Calibration in Model Comparison {#sec-ch12-calibration-comparison}
## Putting It All Together {#sec-ch12-putting-together}
## Practical Guidance: Evaluation Design Checklist
## The Question Behind the Metric {#sec-ch12-question-behind-metric}
## Chapter Summary

### part_3/p3-ch13-confounding.qmd
# Confounding and Data Leakage {#sec-ch13-confounding}
## Chapter Overview
## Confounding, Bias, and Leakage {#sec-ch13-terminology}
## Key Insight: The Confounder-Mechanism Distinction
## Sources of Confounding in Genomic Data {#sec-ch13-sources}
## Stop and Think
### Population Structure and Relatedness {#sec-ch13-ancestry-confounding}
### Technical Batch Effects {#sec-ch13-batch-effects}
### Institutional and Recruitment Confounding {#sec-ch13-institutional-confounding}
### Label Generation Bias {#sec-ch13-label-bias}
### Temporal Drift {#sec-ch13-temporal-drift}
### Resource Overlap and Indirect Leakage {#sec-ch13-resource-overlap}
## Population Structure as a Shortcut {#sec-ch13-population-shortcut}
## Key Insight: Capacity Amplifies Confounding
## Technical Artifacts as Biological Signal {#sec-ch13-technical-artifacts}
## Label Bias and Circularity {#sec-ch13-label-circularity}
## Data Splitting {#sec-ch13-data-splitting}
## Mathematical Foundations
### Random Individual-Level Splits {#sec-ch13-random-splits}
### Family-Aware Splits {#sec-ch13-family-splits}
### Locus-Level Splits {#sec-ch13-locus-splits}
### Region and Chromosome Splits {#sec-ch13-region-splits}
### Cohort and Site Splits {#sec-ch13-cohort-splits}
### Temporal Splits {#sec-ch13-temporal-splits}
### Indirect Leakage Across Resources {#sec-ch13-indirect-leakage}
## Data Leakage as Confounding {#sec-ch13-leakage-confounding}
### Causal Structure of Leakage {#sec-ch13-leakage-causal}
### Compounding Effects {#sec-ch13-compounding}
## Stop and Think: Compound Leakage
### Implications for Confounding Analysis {#sec-ch13-leakage-implications}
## Detecting Confounding {#sec-ch13-detection}
### Confounder-Only Baselines {#sec-ch13-confounder-baselines}
## Key Insight: The Baseline Diagnostic
### Stratified Performance Analysis {#sec-ch13-stratified-performance}
### Residual Confounder Associations {#sec-ch13-residual-associations}
### Split Sensitivity Analysis {#sec-ch13-split-sensitivity}
### Negative Control Outcomes {#sec-ch13-negative-controls}
## Mitigation Strategies {#sec-ch13-mitigation}
### Study Design and Cohort Construction {#sec-ch13-study-design}
### Covariate Adjustment {#sec-ch13-covariate-adjustment}
### Domain Adaptation and Invariance Learning {#sec-ch13-domain-adaptation}
### Data Curation and Benchmark Design {#sec-ch13-benchmark-design}
### Causal Inference Approaches {#sec-ch13-causal-inference}
## Fairness and External Validity {#sec-ch13-fairness}
## A Practical Checklist {#sec-ch13-checklist}
## Practical Guidance: Using This Checklist
## Rigor as Response {#sec-ch13-rigor}
## Chapter Summary

### part_4/p4--fm-families.qmd
# Part IV: Foundation Model Families {.unnumbered}
## Part IV at a Glance
## Connections to Other Parts

### part_4/p4-ch14-fm-principles.qmd
# Foundation Model Paradigm {#sec-ch14-fm-principles}
## Chapter Overview
## From Task-Specific Models to Foundation Models {#sec-ch14-task-specific}
## Stop and Think
## Defining Genomic Foundation Models {#sec-ch14-defining}
### Essential Properties {#sec-ch14-essential-properties}
### What does not Count {#sec-ch14-what-doesnt-count}
### Limitations of the Foundation Model Concept {#sec-ch14-concept-limitations}
## Key Insight: The Foundation Model Criterion
## Scaling Laws and Compute-Optimal Training {#sec-ch14-scaling}
### Chinchilla Framework and Genomic Constraints {#sec-ch14-scaling-framework}
## Mathematical Content Ahead
## Worked Example: Applying the Chinchilla Framework
### Empirical Scaling in Genomic Models {#sec-ch14-empirical-scaling}
## Stop and Think
### Emergent Capabilities {#sec-ch14-emergence}
## Key Insight: Emergence Creates Capability Thresholds
## A Taxonomy of Genomic Foundation Models {#sec-ch14-taxonomy}
### DNA Language Models {#sec-ch14-dna-lm}
### Sequence-to-Function Foundation Models {#sec-ch14-seq-to-func}
### Variant Effect Prediction Models {#sec-ch14-vep-models}
## Knowledge Check
### Multi-Omic Foundation Models {#sec-ch14-multi-omic}
## Design Dimensions {#sec-ch14-design-dimensions}
### Data Composition {#sec-ch14-data-composition}
### Architecture Choices {#sec-ch14-architecture}
### Context Length {#sec-ch14-context-length}
### Tokenization {#sec-ch14-tokenization}
## Build Versus Use Decisions {#sec-ch14-build-vs-use}
## Stop and Think
### When to Use Existing Models {#sec-ch14-use-existing}
### When to Adapt Existing Models {#sec-ch14-adapt-existing}
### When to Train from Scratch {#sec-ch14-train-scratch}
### Cost-Benefit Analysis {#sec-ch14-cost-benefit}
## Practical Guidance: The Build-vs-Use Decision
## Evaluation Principles {#sec-ch14-evaluation}
### Multi-Task Assessment {#sec-ch14-multi-task}
### Transfer Versus Pretraining Performance {#sec-ch14-transfer-eval}
## Foundation Model Ecosystem {#sec-ch14-ecosystem}
### Model Distribution {#sec-ch14-distribution}
### Documentation Requirements {#sec-ch14-documentation}
### Industry and Academic Contributions {#sec-ch14-contributions}
## Open Questions {#sec-ch14-open-questions}
## Convergence Without Consolidation {#sec-ch14-convergence}
## Chapter Summary

### part_4/p4-ch15-dna-lm.qmd
# DNA Language Models {#sec-ch15-dna-lm}
## Chapter Overview
## From Task-Specific CNNs to General-Purpose Language Models {#sec-ch15-task-specific-to-general}
## Stop and Think
## Key Insight: The Foundation Model Paradigm Shift
## *DNABERT*: The First DNA Language Model {#sec-ch15-dnabert}
## *Nucleotide Transformer*: Scaling Data and Model Diversity {#sec-ch15-nucleotide-transformer}
## *GPN*: Cross-Species Pretraining for Variant Effect Prediction {#sec-ch15-gpn}
## Stop and Think
## Worked Example: Zero-Shot Variant Scoring
## Long-Context Revolution {#sec-ch15-long-context}
## Mathematical Content Ahead
### *HyenaDNA*: Megabase Context via Implicit Convolutions {#sec-ch15-hyenadna}
### *Caduceus*: Bidirectional Processing with Reverse-Complement Equivariance {#sec-ch15-caduceus}
## Knowledge Check
## Key Insight: Inductive Biases vs. Scale
### *Evo 2*: Genome-Scale Modeling Across the Tree of Life {#sec-ch15-evo2}
## Knowledge Check: Predict Before You Look
## Training Data and What Models Learn {#sec-ch15-training-data}
### Training Corpus Composition {#sec-ch15-corpus-composition}
### Probing What Models Learn {#sec-ch15-probing}
## Stop and Think
### What Models Do Not Learn {#sec-ch15-limitations-learned}
## Knowledge Check: Connect to Earlier Material
## Predict Before You Look
## Benchmark Performance and Evaluation {#sec-ch15-benchmarks}
## Spaced Retrieval: Test Your Memory
### Major Benchmark Suites {#sec-ch15-benchmark-suites}
### Benchmark Limitations {#sec-ch15-benchmark-limitations}
## Annotation-Aware Extensions {#sec-ch15-annotation-aware}
## Using DNA Language Models in Practice {#sec-ch15-practical-use}
## Practical Guidance: Choosing a Usage Pattern
### Embeddings as Universal Features {#sec-ch15-embeddings}
### Fine-Tuning and Adaptation {#sec-ch15-fine-tuning}
### Zero-Shot and Few-Shot Scoring {#sec-ch15-zero-shot}
## Limitations and Open Challenges {#sec-ch15-open-challenges}
## Representations Without Predictions {#sec-ch15-soft-landing}
## Chapter Summary

### part_4/p4-ch16-protein-lm.qmd
# Protein Language Models {#sec-ch16-protein-lm}
## ESM Model Family {#sec-ch16-esm-family}
### ESM-1b: Establishing the Paradigm {#sec-ch16-esm1b}
### Emergent Biological Knowledge {#sec-ch16-emergent-knowledge}
### ESM-2: Scaling Up {#sec-ch16-esm2}
## Alternative Architectures {#sec-ch16-alternative-architectures}
## Attention and Evolutionary Coupling {#sec-ch16-attention-coupling}
## ESMFold: Structure from Sequence {#sec-ch16-esmfold}
### Alignment-Free Prediction {#sec-ch16-alignment-free}
### What ESMFold Reveals About PLMs {#sec-ch16-esmfold-implications}
## Function Prediction {#sec-ch16-function-prediction}
## Variant Effect Prediction {#sec-ch16-variant-effects}
## Integration with Structure Prediction {#sec-ch16-structure-integration}
## Limitations {#sec-ch16-limitations}
### Orphan and Dark Proteins {#sec-ch16-orphan-proteins}
### Novel Folds {#sec-ch16-novel-folds}
### Conformational Flexibility {#sec-ch16-conformational-flexibility}
### Epistasis {#sec-ch16-epistasis}
### Interpretability {#sec-ch16-interpretability}
## Lessons for Genomic Foundation Models {#sec-ch16-lessons}
### Self-Supervised Biological Knowledge {#sec-ch16-self-supervised}
### Scaling Benefits {#sec-ch16-scaling}
### Effective Transfer Learning {#sec-ch16-transfer}
### Architecture-Sequence Matching {#sec-ch16-architecture-matching}
### Integration Benefits {#sec-ch16-integration}
## Paradigm That Generalized {#sec-ch16-conclusion}

### part_4/p4-ch17-regulatory.qmd
# Regulatory Models {#sec-ch17-regulatory}
## Long-Range Regulation Problem {#sec-ch17-long-range}
## *Enformer*: Attention Meets Regulatory Genomics {#sec-ch17-enformer}
### Architecture {#sec-ch17-enformer-architecture}
### Training Data and Cross-Species Learning {#sec-ch17-enformer-training}
### Variant Effect Prediction {#sec-ch17-enformer-vep}
## *Borzoi*: From Chromatin to Transcriptome {#sec-ch17-borzoi}
### Beyond Transcription Initiation {#sec-ch17-borzoi-transcription}
### Predicting Coverage at Nucleotide Resolution {#sec-ch17-borzoi-coverage}
### Applications Beyond Expression Level {#sec-ch17-borzoi-applications}
## *Sei*: A Regulatory Vocabulary from Sequence {#sec-ch17-sei}
### Discrete Regulatory States {#sec-ch17-sei-states}
### Complementary to Track Prediction {#sec-ch17-sei-complementary}
## *AlphaGenome*: Unifying Modalities at Megabase Scale {#sec-ch17-alphagenome}
### From 200kb to One Megabase {#sec-ch17-alphagenome-scale}
### Closed Weights, Open Questions {#sec-ch17-alphagenome-access}
## What Hybrid Architectures Accomplish {#sec-ch17-accomplishments}
### Spanning Enhancer-Promoter Distances {#sec-ch17-spanning}
### Multi-Task Regularization {#sec-ch17-multitask}
### Cross-Species Constraints {#sec-ch17-cross-species}
### Unified Variant Effect Prediction {#sec-ch17-unified-vep}
## Limitations and Open Challenges {#sec-ch17-limitations}
### Training Data Constraints {#sec-ch17-training-bias}
### Finite Context {#sec-ch17-finite-context}
### Missing Three-Dimensional Context {#sec-ch17-missing-3d}
### Correlation Versus Causation {#sec-ch17-correlation}
### Interpretability Challenges {#sec-ch17-interpretability}
## Relationship to Foundation Models {#sec-ch17-foundation-models}
## Prediction Without Explanation {#sec-ch17-prediction-explanation}

### part_4/p4-ch18-vep-fm.qmd
# Variant Effect Prediction {#sec-ch18-vep-fm}
## Foundation Model Paradigm for Variant Interpretation {#sec-ch18-fm-paradigm}
### Zero-Shot and Supervised Approaches {#sec-ch18-zeroshot-supervised}
## Protein-Based Variant Effect Prediction {#sec-ch18-protein-vep}
### Zero-Shot Scoring with Protein Language Models {#sec-ch18-zeroshot-plm}
### Alignment-Based Models: EVE and popEVE {#sec-ch18-alignment-models}
### AlphaMissense: Structure-Informed Pathogenicity Prediction {#sec-ch18-alphamissense}
## DNA-Based Variant Effect Prediction {#sec-ch18-dna-vep}
### Splice Variant Prediction with SpliceAI {#sec-ch18-spliceai}
### Regulatory Variant Prediction with Enformer {#sec-ch18-enformer-vep}
### DNA Language Models: GPN-MSA and Evo 2 {#sec-ch18-dna-lm-vep}
### AlphaGenome: Unified Multi-Omic Variant Effect Prediction {#sec-ch18-alphagenome}
## Combining Evidence Across Modalities {#sec-ch18-combining-evidence}
### Integration Strategies {#sec-ch18-integration-strategies}
### Avoiding Double-Counting {#sec-ch18-double-counting}
### Practical Workflow Design {#sec-ch18-workflow-design}
## Calibration and Clinical Categories {#sec-ch18-calibration}
### Assessing Calibration {#sec-ch18-assessing-calibration}
### Calibration Methods for Variant Effect Prediction {#sec-ch18-calibration-methods}
### Mapping to ACMG Categories {#sec-ch18-acmg-mapping}
### The Challenge of Uncertain Significance {#sec-ch18-vus-challenge}
## Uncertainty Quantification {#sec-ch18-uncertainty}
### Sources of Uncertainty {#sec-ch18-uncertainty-sources}
### Uncertainty Estimation Methods {#sec-ch18-uncertainty-methods}
### Out-of-Distribution Detection {#sec-ch18-ood-detection}
## What Foundation Models Add {#sec-ch18-fm-gains}
### Improved Discrimination {#sec-ch18-improved-discrimination}
### Extended Coverage {#sec-ch18-extended-coverage}
### Mechanistic Interpretability {#sec-ch18-mechanistic-interpretability}
### Persistent Limitations {#sec-ch18-persistent-limitations}
## Clinical Integration Considerations {#sec-ch18-clinical-integration}
### Laboratory Validation {#sec-ch18-lab-validation}
### Workflow Integration {#sec-ch18-workflow-integration}
### Communication to Clinicians {#sec-ch18-clinical-communication}
## Open Challenges {#sec-ch18-open-challenges}
### Complex Variant Types {#sec-ch18-complex-variants}
### Long-Read Sequencing and Variant Effect Prediction {#sec-ch18-long-read}
### Combinatorial Effects {#sec-ch18-combinatorial}
### Phenotype Specificity {#sec-ch18-phenotype-specificity}
### Temporal and Environmental Context {#sec-ch18-temporal-context}
### Equity and Access {#sec-ch18-equity}
## Tools for Interpretation, Not Oracles {#sec-ch18-conclusion}

### part_5/p5--cellular-context.qmd
# Part V: Cellular Context {.unnumbered}
## Part V at a Glance
## Connections to Other Parts

### part_5/p5-ch19-rna.qmd
# RNA Structure and Function {#sec-ch19-rna}
## RNA as Molecule Versus Transcriptome Readout {#sec-ch19-perspectives}
## Why Secondary Structure Creates a Distinct Modeling Challenge {#sec-ch19-structure-challenge}
### Flat Energy Landscape Problem {#sec-ch19-energy-landscape}
### Base Pairing and Long-Range Dependencies {#sec-ch19-base-pairing}
### Pseudoknots and Tertiary Complexity {#sec-ch19-pseudoknots}
## Classical Approaches to Structure Prediction {#sec-ch19-classical}
### Thermodynamic Folding Models {#sec-ch19-thermodynamic}
### Comparative and Covariation Methods {#sec-ch19-comparative}
## Deep Learning for Secondary Structure Prediction {#sec-ch19-dl-structure}
### From Thermodynamics to Learned Patterns {#sec-ch19-learned-patterns}
### Structure Probing as Supervision {#sec-ch19-structure-probing}
## RNA Foundation Models {#sec-ch19-foundation}
### Scale Gap with Protein Language Models {#sec-ch19-scale-gap}
### Architectures and Objectives {#sec-ch19-architectures}
### Downstream Applications {#sec-ch19-downstream}
## Codon-Level Models for Coding RNA {#sec-ch19-codon}
### Beyond Nucleotide Tokenization {#sec-ch19-codon-tokenization}
### What Codon Models Add {#sec-ch19-codon-advantages}
## UTR Models and Translation Regulation {#sec-ch19-utr}
### Why UTRs Dominate Expression Control {#sec-ch19-utr-control}
### Sequence-to-Expression Models {#sec-ch19-expression-models}
### Integration with mRNA Design {#sec-ch19-utr-design}
## mRNA Design and Optimization {#sec-ch19-mrna-design}
### Design Objectives and Trade-offs {#sec-ch19-design-objectives}
### Lessons from COVID-19 Vaccines {#sec-ch19-covid-vaccines}
### Model-Based Design Strategies {#sec-ch19-model-design}
## Noncoding RNA Classification and Function {#sec-ch19-ncrna}
### Diversity of Noncoding RNA {#sec-ch19-ncrna-diversity}
### From Handcrafted Features to Learned Representations {#sec-ch19-ncrna-features}
## miRNA Target Prediction {#sec-ch19-mirna}
## Splicing and Transcript Processing Models {#sec-ch19-splicing}
### Beyond SpliceAI {#sec-ch19-beyond-spliceai}
## Limitations and Open Challenges {#sec-ch19-limitations}
### Sparse Structural Data {#sec-ch19-sparse-data}
### Functional Annotation Gaps {#sec-ch19-annotation-gaps}
### Maturity Gap {#sec-ch19-maturity-gap}
## Bridge Between Sequence and Cell {#sec-ch19-bridge}

### part_5/p5-ch20-single-cell.qmd
# Single-Cell Models {#sec-ch20-single-cell}
## Chapter Overview
## Single-Cell Data Landscape {#sec-ch20-data}
### From Bulk to Single-Cell Resolution {#sec-ch20-bulk-to-sc}
## Stop and Think: The Averaging Problem
## Key Insight: The Cell-as-Document Analogy
### Technical Challenges and Data Characteristics {#sec-ch20-technical}
## Cellular Language Models {#sec-ch20-clm}
### *Geneformer*: Learning Network Biology {#sec-ch20-geneformer}
## Worked Example: Rank-Based Encoding
### *scGPT*: Generative Pretraining for Single-Cell Analysis {#sec-ch20-scgpt}
## Stop and Think: Multiple Pretraining Objectives
### *scFoundation* and Scaling Single-Cell Models {#sec-ch20-scfoundation}
### *TranscriptFormer*: Cross-Species Cellular Models {#sec-ch20-transcriptformer}
## Key Insight: Cross-Species Transfer Reveals Conserved Regulatory Programs
## Perturbation Response Prediction {#sec-ch20-perturbation}
### *In Silico* Experiment Promise {#sec-ch20-in-silico}
## Stop and Think: From Correlation to Causation
### Perturb-seq and Foundation Model Training {#sec-ch20-perturb-seq}
### Limitations of Current Approaches {#sec-ch20-perturbation-limits}
## Practical Guidance: When to Trust Perturbation Predictions
## Epigenomic Foundation Models {#sec-ch20-epigenomic}
### DNA Methylation and *CpGPT* {#sec-ch20-methylation}
### Chromatin Accessibility Models {#sec-ch20-accessibility}
## Knowledge Check: Epigenomic Data Types
## Cross-Modality Integration {#sec-ch20-integration}
### Unpaired Integration Challenge {#sec-ch20-unpaired}
### *GLUE*: Graph-Linked Unified Embedding {#sec-ch20-glue}
## Key Insight: Biological Knowledge as Regularizer
### Applications of Cross-Modal Integration {#sec-ch20-cross-modal-apps}
## Practical Challenges and Limitations {#sec-ch20-limitations}
### Batch Effects and Technical Artifacts {#sec-ch20-batch-effects}
### Cell Type Imbalance {#sec-ch20-imbalance}
### Evaluation Complexity {#sec-ch20-evaluation}
## Stop and Think: The Ground Truth Problem
### Causality and Mechanism {#sec-ch20-causality}
## Practical Guidance: Responsible Use of Single-Cell Foundation Models
## From Sequence to State {#sec-ch20-conclusion}
## Chapter Summary

### part_5/p5-ch21-3d-genome.qmd
# 3D Genome Organization {#sec-ch21-3d-genome}
## Chromatin Organization Hierarchy {#sec-ch21-chromatin-hierarchy}
### Chromosome Territories and Compartments {#sec-ch21-territories-compartments}
### Topologically Associating Domains {#sec-ch21-tads}
### Loop Extrusion Mechanism {#sec-ch21-loop-extrusion}
### Fine-Scale Chromatin Loops {#sec-ch21-fine-scale-loops}
## Measuring the 3D Genome {#sec-ch21-3d-measurement}
### Hi-C and Contact Matrices {#sec-ch21-hic-matrices}
### Resolution and Data Resources {#sec-ch21-3d-data-resources}
## Predicting 3D Structure from Sequence {#sec-ch21-3d-prediction}
### *Akita* and Dilated Convolutions {#sec-ch21-akita}
### *Orca* and Multiscale Prediction {#sec-ch21-orca}
### *C.Origami* and Cross-Cell-Type Transfer {#sec-ch21-c-origami}
### Learned Sequence Determinants {#sec-ch21-3d-interpretability}
## 3D Structure and Gene Regulation {#sec-ch21-3d-regulation}
### Beyond One-Dimensional Models {#sec-ch21-beyond-1d}
### Structural Variant Interpretation {#sec-ch21-sv-interpretation}
### Causality and Permissive Architecture {#sec-ch21-3d-causality}
## Spatial Transcriptomics {#sec-ch21-spatial-transcriptomics}
### Measurement Technologies {#sec-ch21-spatial-technologies}
### Computational Challenges {#sec-ch21-spatial-computation}
### Spatial Foundation Models {#sec-ch21-spatial-models}
## Limitations and Open Questions {#sec-ch21-3d-limitations}
## Structure as Context, Not Cause {#sec-ch21-structure-context}

### part_5/p5-ch22-networks.qmd
# Graph and Network Models {#sec-ch22-networks}
## Chapter Overview
## Key Insight: The Division of Labor
## Biological Networks and Data Resources {#sec-ch22-biological-networks}
### Landscape of Biological Graphs {#sec-ch22-landscape}
## Knowledge Check: Network Bias
### Biases and Limitations {#sec-ch22-network-biases}
## Graph Neural Network Fundamentals {#sec-ch22-gnn-fundamentals}
### Message Passing Principles {#sec-ch22-message-passing}
## Key Insight: Message Passing as Neural Diffusion
## Knowledge Check
### Canonical Architectures {#sec-ch22-canonical-architectures}
## Difficulty Warning: Over-Smoothing
## Foundation Model Embeddings as Node Features {#sec-ch22-fm-embeddings}
### Integration Principle {#sec-ch22-integration-principle}
## Stop and Think
### Practical Integration Patterns {#sec-ch22-practical-patterns}
## Practical Guidance: Choosing an Integration Strategy
### Evidence for the Integration Benefit {#sec-ch22-integration-evidence}
## Applications {#sec-ch22-applications}
### Disease Gene Prioritization {#sec-ch22-disease-gene}
## Key Insight: Beyond Guilt by Association
### Drug-Target Interaction Prediction {#sec-ch22-drug-target}
## Stop and Think
### Knowledge Graph Reasoning and Drug Repurposing {#sec-ch22-kg-reasoning}
### Pathway and Module Analysis {#sec-ch22-pathway-analysis}
### Cell Type and State Annotation {#sec-ch22-cell-annotation}
## Practical Considerations {#sec-ch22-practical}
### Graph Construction Quality {#sec-ch22-graph-construction}
## Practical Guidance: Graph Construction Checklist
### Scalability and Mini-Batching {#sec-ch22-scalability}
### Robustness to Noise and Missingness {#sec-ch22-robustness}
## Knowledge Check
### Interpretation and Validation {#sec-ch22-interpretation}
## Limitations and Open Challenges {#sec-ch22-limitations}
### Study Bias Problem {#sec-ch22-study-bias}
### Causality Versus Association {#sec-ch22-causality}
## Critical Limitation
### Negative Data and Class Imbalance {#sec-ch22-negative-data}
### Distribution Shift {#sec-ch22-distribution-shift}
## Sequence Encodes, Structure Connects {#sec-ch22-conclusion}
## Chapter Summary

### part_5/p5-ch23-multi-omics.qmd
# Multi-Omics Integration {#sec-ch23-multi-omics}
## Chapter Overview
## Limits of Single-Modality Models {#sec-ch23-limits}
## Stop and Think
## Integration Strategies and Their Tradeoffs {#sec-ch23-strategies}
### Early Fusion {#sec-ch23-early-fusion}
### Late Fusion {#sec-ch23-late-fusion}
### Intermediate Fusion {#sec-ch23-intermediate-fusion}
## Stop and Think
## Key Insight
## Multi-Omics Foundation Models {#sec-ch23-foundation-models}
### Factor-Based Integration {#sec-ch23-factor-integration}
### Deep Generative Multi-Omics Models {#sec-ch23-deep-generative}
## Knowledge Check
### Contrastive Multi-Modal Learning {#sec-ch23-contrastive}
## Clinical Integration: EHR, Imaging, and Molecular Data {#sec-ch23-clinical-integration}
### Electronic Health Records as a Modality {#sec-ch23-ehr}
## Key Insight
### Imaging Integration {#sec-ch23-imaging}
### Multi-Modal Clinical Prediction Models {#sec-ch23-multimodal-clinical}
## Practical Guidance
## Systems View: From Variant to Phenotype {#sec-ch23-systems-view}
### Information Cascade {#sec-ch23-information-cascade}
### Bottleneck Modalities {#sec-ch23-bottleneck}
## Stop and Think
## Key Insight
### Causal vs. Correlational Integration {#sec-ch23-causal-correlational}
## Handling Missing Modalities {#sec-ch23-missing-modalities}
## Challenging Section
### Training with Incomplete Data {#sec-ch23-incomplete-training}
### Cross-Modal Imputation {#sec-ch23-imputation}
### Zero-Shot Cross-Modal Transfer {#sec-ch23-zero-shot}
## Practical Challenges {#sec-ch23-practical-challenges}
### Batch Effects Across Modalities {#sec-ch23-batch-effects}
### Sample Size and Power {#sec-ch23-sample-size}
### Interpretability Across Modalities {#sec-ch23-interpretability}
### Evaluation Complexity {#sec-ch23-evaluation}
## Knowledge Check
## Integration as Means, Not End {#sec-ch23-conclusion}
## Chapter Summary

### part_6/p6--responsible-deployment.qmd
# Part VI: Responsible Deployment {.unnumbered}
## Part VI at a Glance
## Essential for Clinical Applications
## Connections to Other Parts

### part_6/p6-ch24-uncertainty.qmd
# Uncertainty Quantification {#sec-ch24-uncertainty}
## Chapter Overview
## Types of Uncertainty in Genomic Prediction {#sec-ch24-types}
### Why Uncertainty Matters {#sec-ch24-why-uncertainty}
## Key Insight: Calibration vs. Accuracy
### Epistemic Uncertainty {#sec-ch24-epistemic}
## Stop and Think
### Aleatoric Uncertainty {#sec-ch24-aleatoric}
### Decomposing Total Uncertainty {#sec-ch24-decomposition}
## Difficulty Warning
## Calibration and Confidence Interpretation {#sec-ch24-calibration}
### The Calibration Problem {#sec-ch24-calibration-problem}
## Knowledge Check
### Measuring Calibration {#sec-ch24-measuring-calibration}
### Why Foundation Models Are Often Miscalibrated {#sec-ch24-fm-miscalibration}
### Calibration Across Subgroups {#sec-ch24-subgroup-calibration}
## Key Insight: Hidden Calibration Disparities
## Post-Hoc Calibration Methods {#sec-ch24-post-hoc-calibration}
## Stop and Think
### Temperature Scaling {#sec-ch24-temperature-scaling}
### Platt Scaling {#sec-ch24-platt-scaling}
### Isotonic Regression {#sec-ch24-isotonic-regression}
### Calibrating Foundation Model Outputs {#sec-ch24-calibrating-fm}
## Practical Guidance: Calibration Workflow
## Uncertainty Quantification Methods for Foundation Models {#sec-ch24-uq-methods}
### Deep Ensembles {#sec-ch24-deep-ensembles}
### Monte Carlo Dropout {#sec-ch24-mc-dropout}
## Stop and Think
### Heteroscedastic Models {#sec-ch24-heteroscedastic}
### Evidential Deep Learning {#sec-ch24-evidential}
### Selecting Uncertainty Quantification Methods {#sec-ch24-selecting-uq}
## Conformal Prediction: Distribution-Free Guarantees {#sec-ch24-conformal}
## Key Insight: Prediction Sets Convey Uncertainty Without Probabilities
### Split Conformal Prediction {#sec-ch24-split-conformal}
## Difficulty Warning
### Conformal Prediction for Variant Classification {#sec-ch24-conformal-variant}
### Limitations and Practical Considerations {#sec-ch24-conformal-limitations}
### Integration with Clinical Workflows {#sec-ch24-conformal-clinical}
## Out-of-Distribution Detection {#sec-ch24-ood-detection}
### Out-of-Distribution Problem {#sec-ch24-ood-problem}
## Knowledge Check
### Likelihood-Based Detection and Its Failures {#sec-ch24-likelihood-ood}
### Embedding-Based Detection {#sec-ch24-embedding-ood}
### Practical OOD Detection for Genomic Applications {#sec-ch24-practical-ood}
## Practical Guidance: OOD Detection Pipeline
## Selective Prediction and Abstention {#sec-ch24-selective-prediction}
### When to Abstain {#sec-ch24-when-abstain}
### Selective Prediction Methods {#sec-ch24-selective-methods}
### Evaluating Selective Prediction {#sec-ch24-selective-eval}
## Uncertainty for Specific Genomic Tasks {#sec-ch24-genomic-uq}
### Variant Effect Prediction Uncertainty {#sec-ch24-vep-uncertainty}
### Regulatory Variant Uncertainty {#sec-ch24-regulatory-uncertainty}
### Uncertainty Across Populations {#sec-ch24-population-uncertainty}
## Communicating Uncertainty to End Users {#sec-ch24-communication}
### Communication Challenge {#sec-ch24-communication-challenge}
### Categorical Reporting {#sec-ch24-categorical-reporting}
### Visual Communication {#sec-ch24-visual-communication}
### Decision-Theoretic Framing {#sec-ch24-decision-framing}
## Necessary but Insufficient {#sec-ch24-conclusion}
## Chapter Summary

### part_6/p6-ch25-interpretability.qmd
# Interpretability {#sec-ch25-interpretability}
## Chapter Overview
## Attribution Methods and Input Importance {#sec-ch25-attribution}
### *In Silico* Mutagenesis {#sec-ch25-ism}
## Stop and Think: Attribution Method Tradeoffs
### Gradient-Based Attribution {#sec-ch25-gradient}
## Key Insight: The Saturation Problem
### Reconciling Attribution Methods {#sec-ch25-reconciling}
## Interpreting Convolutional Filters {#sec-ch25-cnn-filters}
### From Filters to Position Weight Matrices {#sec-ch25-filter-pwm}
## Knowledge Check: CNN Filter Interpretation
### Deeper Layers and Combinatorial Patterns {#sec-ch25-deeper-layers}
## Motif Discovery from Attributions {#sec-ch25-motif-discovery}
## Key Insight: Why TF-MoDISco Works Better Than Traditional Motif Finding
## Probing Learned Representations {#sec-ch25-probing}
### Probing Methodology {#sec-ch25-probing-methods}
## Stop and Think: Probing and Confounding
### Limitations of Probing {#sec-ch25-probing-limits}
## Challenge Alert: The Selectivity-Accessibility Tradeoff
## Attention Patterns in Transformer Models {#sec-ch25-attention}
### What Attention Patterns Reveal {#sec-ch25-attention-patterns}
### Why Attention Weights Mislead {#sec-ch25-attention-caution}
## Key Insight: Attention Is Not Explanation
## Regulatory Vocabularies and Global Interpretability {#sec-ch25-global}
### Sequence Classes from *Sei* {#sec-ch25-sei}
## Knowledge Check: Local vs. Global Interpretability
### Embedding Geometry and Regulatory Programs {#sec-ch25-embedding-geometry}
## Mechanistic Interpretability {#sec-ch25-mechanistic}
## Challenge Alert: Frontier Research Area
### Circuits and Features {#sec-ch25-circuits}
### Applications to Genomic Models {#sec-ch25-mechanistic-genomics}
## Validation: From Explanations to Experiments {#sec-ch25-validation}
### Faithfulness Testing {#sec-ch25-faithfulness}
### Experimental Validation {#sec-ch25-experimental}
## Stop and Think: Designing Validation Experiments
## Interpretability in Clinical Variant Assessment {#sec-ch25-clinical}
## Practical Guidance: Communicating Interpretability in Clinical Reports
## Practical Approaches for Foundation Model Analysis {#sec-ch25-practical}
## Plausibility Is Not Faithfulness {#sec-ch25-conclusion}
## Chapter Summary

### part_6/p6-ch26-causal.qmd
# Causality {#sec-ch26-causal}
## Chapter Overview
## Prediction vs. Causation {#sec-ch26-prediction-vs-causation}
### The Ladder of Causation {#sec-ch26-ladder}
## Key Insight: The Rung Gap is Qualitative, Not Quantitative
### Why Predictive Accuracy Does Not Equal Causal Understanding {#sec-ch26-prediction-not-causation}
## Stop and Think: Diagnosing Causal Structure
### The Clinical Stakes {#sec-ch26-clinical-stakes}
## Causal Methods in Genomics {#sec-ch26-causal-methods}
### Mendelian Randomization {#sec-ch26-mendelian-randomization}
## Conceptual Difficulty
### Model-X Knockoffs for Controlled Variable Selection {#sec-ch26-knockoffs}
## Worked Example: Mendelian Randomization for Drug Target Validation
### Fine-Mapping for Causal Variants {#sec-ch26-fine-mapping}
### From GWAS to Causal Genes {#sec-ch26-gwas-to-genes}
## Foundation Models and Causality {#sec-ch26-fm-causality}
### Can Foundation Models Learn Causal Structure? {#sec-ch26-fm-causal-structure}
## Knowledge Check: Observational vs. Interventional Learning
### In-Silico Perturbation Prediction {#sec-ch26-in-silico-perturbation}
### Counterfactual Reasoning Limitations {#sec-ch26-counterfactual-limits}
## Key Insight: The Counterfactual Barrier
## Intervention Prediction {#sec-ch26-intervention-prediction}
### CRISPR Screen Analysis with Foundation Models {#sec-ch26-crispr-screens}
### Drug Response Prediction {#sec-ch26-drug-response}
## Stop and Think: Validating Drug Response Predictions
### Closed-Loop Experimental Validation {#sec-ch26-closed-loop}
## Causal Discovery {#sec-ch26-causal-discovery}
### Learning Regulatory Networks {#sec-ch26-regulatory-networks}
### Temporal Causality {#sec-ch26-temporal-causality}
### Multi-Omics Causal Structure {#sec-ch26-multi-omics-causal}
## Stop and Think: Causal Structure Across Omics Layers
## Clinical Implications {#sec-ch26-clinical-implications}
### Drug Target Validation Evidence Hierarchy {#sec-ch26-target-validation}
## Practical Guidance: Communicating Causal Claims
### Regulatory Requirements for Causal Claims {#sec-ch26-regulatory-requirements}
## Looking Forward {#sec-ch26-conclusion}
## Chapter Summary

### part_6/p6-ch27-regulatory.qmd
# Regulatory and Governance {#sec-ch27-regulatory}
## Chapter Overview
## Regulatory Frameworks for Genomic AI {#sec-ch27-regulatory}
### Software as Medical Device Paradigm {#sec-ch27-samd}
## Worked Example: SaMD Classification for a Variant Classifier
## Stop and Think
## Key Insight: The Locked vs. Adaptive Dilemma
### European and Global Regulatory Landscapes {#sec-ch27-global-regulation}
### Validation Requirements for Clinical Genomic AI {#sec-ch27-validation}
## Knowledge Check
## Worked Example: Regulatory Submission for AlphaMissense
## Data Governance and Consent {#sec-ch27-governance}
### Consent Problem at Scale {#sec-ch27-consent}
## Difficulty Warning
### Biobank Governance Models {#sec-ch27-biobanks}
## Stop and Think
### Secondary Use and Data Futures {#sec-ch27-secondary-use}
## Privacy and Genomic Data {#sec-ch27-privacy}
## Key Insight: Genomes Are Their Own Identifiers
### Re-identification Challenge {#sec-ch27-reidentification}
### Family and Relational Privacy {#sec-ch27-family-privacy}
## Intellectual Property and Ownership {#sec-ch27-ip}
### Genomic Data Ownership {#sec-ch27-data-ownership}
## Knowledge Check
### Model Weights as Assets {#sec-ch27-model-weights}
### Prediction Ownership and Liability {#sec-ch27-liability}
## Practical Guidance: Navigating Liability in Model Deployment
## Responsible Development Practices {#sec-ch27-responsible}
### Transparency and Documentation {#sec-ch27-transparency}
### Fairness and Performance Equity {#sec-ch27-fairness}
## Key Insight: Bias Is Structural, Not Just Technical
### Human Oversight and Decision Support {#sec-ch27-oversight}
## Stop and Think
## Dual Use and Biosecurity {#sec-ch27-biosecurity}
### Generative Models and Pathogen Enhancement {#sec-ch27-pathogen}
## Difficulty Warning
### Access Controls and Responsible Release {#sec-ch27-access}
## Chapter Summary

### part_7/p7--applications.qmd
# Part VII: Applications & Frontiers {.unnumbered}
## Part VII at a Glance
## The Benchmark-Deployment Gap
## Connections to Other Parts

### part_7/p7-ch28-clinical-risk.qmd
# Clinical Risk Prediction {#sec-ch28-clinical-risk}
## Chapter Overview
## From Polygenic Scores to Foundation Model Features {#sec-ch28-pgs-to-fm}
## Stop and Think
## Key Insight: From Scalar Scores to Rich Representations
## Defining Clinical Risk Prediction {#sec-ch28-defining-risk}
## Feature Integration Architectures {#sec-ch28-feature-integration}
## Practical Guidance: Choosing a Fusion Architecture
## EHR Integration and Phenotype Embeddings {#sec-ch28-ehr-integration}
### EEPRS Framework {#sec-ch28-eeprs}
### Understanding When Embeddings Help {#sec-ch28-embeddings-help}
## Knowledge Check
### PRS-PheWAS for Clinical Interpretation {#sec-ch28-prs-phewas}
### Implementation Considerations {#sec-ch28-eeprs-implementation}
### Integration with Foundation Model Features {#sec-ch28-eeprs-fm}
## Temporal Modeling Architectures {#sec-ch28-temporal-modeling}
## Challenging Material Ahead
## Key Insight: Static Genetics, Dynamic Clinical Context
## Evaluation for Clinical Deployment {#sec-ch28-evaluation}
## Stop and Think
### Discrimination {#sec-ch28-discrimination}
### Calibration {#sec-ch28-calibration}
### Clinical Utility {#sec-ch28-clinical-utility}
### Validation Hierarchy {#sec-ch28-validation-hierarchy}
## Uncertainty Quantification {#sec-ch28-uncertainty}
## Knowledge Check
## Fairness and Health Equity {#sec-ch28-fairness}
## Key Insight: Bias Compounds Through the Pipeline
## Clinical Integration {#sec-ch28-clinical-integration}
### Workflow Integration Patterns {#sec-ch28-workflow-patterns}
## Practical Guidance: Integration Patterns by Use Case
### System Architecture {#sec-ch28-system-architecture}
### Post-Deployment Monitoring {#sec-ch28-monitoring}
## Regulatory and Quality Frameworks {#sec-ch28-regulatory}
## Case Studies {#sec-ch28-case-studies}
## Stop and Think
### Cardiometabolic Risk Stratification {#sec-ch28-case-cardio}
### Oncology Prognosis {#sec-ch28-case-oncology}
### Pharmacogenomic Adverse Event Prediction {#sec-ch28-case-pharmacogenomics}
## Translation as the Test {#sec-ch28-translation-test}
## Chapter Summary

### part_7/p7-ch29-rare-disease.qmd
# Rare Disease Diagnosis {#sec-ch29-rare-disease}
## Chapter Overview
## Variant Prioritization Funnel {#sec-ch29-prioritization-funnel}
## Stop and Think
### Quality and Technical Filters {#sec-ch29-quality-filters}
### Population Frequency Filters {#sec-ch29-frequency-filters}
## Key Insight: Frequency Thresholds Are Disease-Specific
### Consequence and Gene Filters {#sec-ch29-consequence-filters}
### Foundation Model Scoring {#sec-ch29-fm-scoring}
## ACMG-AMP Criteria and Computational Evidence {#sec-ch29-acmg-amp}
### Evidence Categories {#sec-ch29-evidence-categories}
## Knowledge Check
### PP3 and BP4: Computational Evidence {#sec-ch29-pp3-bp4}
## Challenging Concept: Evidence Strength Calibration
### Calibrating Predictions to Evidence Strength {#sec-ch29-calibration}
## Family-Based Analysis {#sec-ch29-family-analysis}
## Key Insight: Family Structure Multiplies Interpretive Power
### *De Novo* Variants {#sec-ch29-de-novo}
### Compound Heterozygosity and Phasing {#sec-ch29-compound-het}
### Segregation Analysis {#sec-ch29-segregation}
## Somatic Variant Interpretation in Cancer {#sec-ch29-somatic}
### Germline versus Somatic Distinction {#sec-ch29-germline-somatic}
## Knowledge Check
### Driver Classification {#sec-ch29-driver}
### Therapeutic Biomarkers {#sec-ch29-biomarkers}
## Practical Guidance: When FM Predictions Help with Novel Therapeutic Variants
## Laboratory Validation {#sec-ch29-validation}
### Types of Functional Assays {#sec-ch29-assay-types}
### Integrating Functional Evidence {#sec-ch29-functional-integration}
## Stop and Think
### Closing the VUS Loop {#sec-ch29-vus-loop}
## Practical Workflow Integration {#sec-ch29-workflow}
### Laboratory Workflow {#sec-ch29-lab-workflow}
## Practical Guidance: Documenting FM Predictions in Clinical Reports
### Clinical Decision-Making {#sec-ch29-clinical-decisions}
### Regulatory and Ethical Considerations {#sec-ch29-regulatory}
## Key Insight: Equity in Computational Predictions
## Interpretive Partnership {#sec-ch29-partnership}
## Chapter Summary

### part_7/p7-ch30-drug-discovery.qmd
# Drug Discovery {#sec-ch30-drug-discovery}
## Chapter Overview
## Case Study: PCSK9 and Genetic Target Validation
## Key Insight: The Genetic Validation Advantage
## Genetic Foundation of Target Selection {#sec-ch30-genetic-foundation}
### From Variant-Level Predictions to Gene-Level Evidence {#sec-ch30-variant-to-gene}
## Stop and Think
### Linking Genetics to Target Safety and Efficacy {#sec-ch30-safety-efficacy}
## Knowledge Check
## Network-Aware Target Discovery and Repurposing {#sec-ch30-network-discovery}
### Propagating Genetic Signals Through Networks {#sec-ch30-network-propagation}
## Key Insight: Single-Gene vs. Network Evidence
### Drug Repurposing Through Shared Representations {#sec-ch30-repurposing}
## Case Study: Metformin and Network-Based Repurposing
## Correlation vs. Causation in Repurposing
## Drug-Target Interaction Prediction {#sec-ch30-dti-prediction}
### Representing Targets for Binding Prediction {#sec-ch30-binding-prediction}
## Stop and Think
## Worked Example: DTI Prediction for a Novel Kinase Target
### Selectivity and Off-Target Prediction {#sec-ch30-selectivity}
## Toxicity Prediction from Genomic Context {#sec-ch30-toxicity}
### Genetic Evidence of Target Liabilities {#sec-ch30-genetic-liabilities}
## Practical Guidance: Genetic Safety Signals
### Expression-Based Toxicity Prediction {#sec-ch30-expression-toxicity}
## Worked Example: Predicting Hepatotoxicity from Perturbation Signatures
### Integrating Genomic Context with Chemical Properties {#sec-ch30-integrated-toxicity}
## Functional Genomics Screens and Perturbation Models {#sec-ch30-functional-screens}
### Designing Informative Perturbation Libraries {#sec-ch30-library-design}
## Knowledge Check
### Perturb-seq and Transcriptomic Readouts {#sec-ch30-perturb-seq}
### Closing the Loop: Lab-in-the-Loop Refinement {#sec-ch30-lab-in-loop}
## Advanced Topic
## Key Insight: The Bayesian Interpretation of Lab-in-the-Loop
## Biomarker Development and Patient Stratification {#sec-ch30-biomarkers}
### Foundation Model Features for Stratification {#sec-ch30-stratification-features}
## Stop and Think
## Worked Example: FM-Enhanced Stratification for Cardiovascular Risk
### Multi-Omic Biomarker Discovery {#sec-ch30-multi-omic-biomarkers}
### Trial Design and Endpoint Selection {#sec-ch30-trial-design}
## Industry Workflows and Infrastructure {#sec-ch30-industry-workflows}
### Building Model Infrastructure {#sec-ch30-model-infrastructure}
### Strategic Choices: Build, Buy, or Fine-Tune {#sec-ch30-build-buy-finetune}
### Industry Context: Timelines and Decision Gates {#sec-ch30-timelines}
## Practical Guidance: Aligning FM Work with Drug Development Gates
### Intellectual Property and Data Considerations {#sec-ch30-ip-data}
## Evaluation and Validation {#sec-ch30-evaluation}
### Benchmark Limitations {#sec-ch30-benchmark-limits}
### From Prediction to Validation {#sec-ch30-prediction-validation}
## Connections to Molecular Design {#sec-ch30-molecular-design}
## Prioritization, Not Automation {#sec-ch30-conclusion}
## Chapter Summary

### part_7/p7-ch31-design.qmd
# Sequence Design {#sec-ch31-design}
## Chapter Overview
## Design Formalism {#sec-ch31-formalism}
## Stop and Think
## Protein Design with Language Models {#sec-ch31-protein-design}
### Sequence Generation from Language Model Priors {#sec-ch31-plm-generation}
### Structure-Aware Design with Diffusion Models {#sec-ch31-structure-diffusion}
## Conceptual Difficulty
## Key Insight: Structure as Intermediate Representation
### Functional Conditioning and Multi-Objective Optimization {#sec-ch31-multi-objective}
## Knowledge Check
## Regulatory Sequence Design {#sec-ch31-regulatory-design}
### Promoter and Enhancer Engineering {#sec-ch31-promoter-enhancer}
## Stop and Think
### Splicing and RNA Processing Elements {#sec-ch31-splicing-design}
## mRNA Design and Optimization {#sec-ch31-mrna-design}
### Codon Optimization Principles {#sec-ch31-codon-optimization}
## Key Insight: The Hidden Complexity of Synonymous Mutations
### Stability Engineering and UTR Design {#sec-ch31-utr-design}
### Immunogenicity Considerations {#sec-ch31-mrna-immunogenicity}
## Antibody and Vaccine Design {#sec-ch31-antibody-vaccine}
### CDR Optimization and Humanization {#sec-ch31-cdr-optimization}
### Vaccine Antigen Design {#sec-ch31-vaccine-design}
## Closed-Loop Design-Build-Test-Learn Cycles {#sec-ch31-dbtl}
### Active Learning for Efficient Exploration {#sec-ch31-active-learning}
## Stop and Think
## Practical Guidance: Choosing an Active Learning Strategy
### High-Throughput Experimentation Integration {#sec-ch31-high-throughput}
## Validation Requirements and Failure Modes {#sec-ch31-validation}
### Validation Hierarchy {#sec-ch31-validation-hierarchy}
### Characteristic Failure Patterns {#sec-ch31-failure-patterns}
## Common Pitfalls
## Practical Design Constraints {#sec-ch31-practical-constraints}
### Manufacturing and Developability {#sec-ch31-manufacturing}
### Safety and Biosecurity Considerations {#sec-ch31-biosecurity}
## Algorithmic Search and Optimization {#sec-ch31-algorithms}
## Knowledge Check
## Evaluating Generative Design {#sec-ch31-generative-evaluation}
### Computational Quality Metrics {#sec-ch31-computational-metrics}
### Functional Assessment {#sec-ch31-functional-assessment}
### Benchmarking Generative Models {#sec-ch31-generative-benchmarks}
## From Understanding to Creating {#sec-ch31-conclusion}
## Chapter Summary

### part_7/p7-ch32-frontiers.qmd
# Frontiers and Synthesis {#sec-ch32-frontiers}
## Chapter Overview
## Open Technical Problems {#sec-ch32-technical}
## Stop and Think
### Scaling and Efficiency {#sec-ch32-scaling}
## Worked Example: Scaling Laws for Variant Effect Prediction
## Key Insight: Scaling Laws Are Not Universal
### Context and Multi-Scale Integration {#sec-ch32-multiscale}
## Knowledge Check
## Case Study: APOE ε4 Across Biological Scales
### Causality and Mechanism {#sec-ch32-causality}
## Key Insight: Correlation Versus Causation in Foundation Models
## Emerging Directions {#sec-ch32-emerging}
### Multimodal Integration {#sec-ch32-multimodal}
## Stop and Think
## Case Study: Multimodal Immunotherapy Response Prediction
## Practical Guidance: Starting with Multimodal Integration
### Agentic and Closed-Loop Systems {#sec-ch32-agentic}
## Governance Challenge: Agentic Autonomy
### Clinical Integration and Learning Health Systems {#sec-ch32-learning-health}
## Case Study: Geisinger DiscovEHR Learning Health System
## Knowledge Check
## Work Ahead {#sec-ch32-conclusion}
## Key Insight: The Translation Gap
## Stop and Think
## Chapter Summary

### preface.qmd
# Preface {.unnumbered}
## Why I Wrote This Book
## How This Book Came Together
## How to Read This Book
## Reader Pathways
## What This Book Assumes (and What It Does Not)
## A Note on Scope and Opinions
## Acknowledgements

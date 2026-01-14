Here are my comments from a detailed read-through of the book draft.

Also, synthesis the comments into list of meta patterns to address across the book.

Note that a lot of these are old, so a given comment may be outdated if the relevant section has been revised since I made the comment.

# Citations:
 - I thought this was address, but I still find 105 *[Citation Needed]* in the text. Please use the research agents fix.

# Introduction
 - add original publish date (12-01-2025) and latest update date.

# Part III: Learning & Evaluation {.unnumbered}
## 11 (was 21) Benchmark Landscape {#sec-ch11-benchmarks}
### Chapter Overview
### Protein Language Model Benchmarks {#sec-ch11-protein-benchmarks}
#### TAPE: Tasks Assessing Protein Embeddings {#sec-ch11-tape}
##### Key Insight: The Transfer Learning Evaluation Framework
#### FLIP: Function-Linked Protein Benchmark {#sec-ch11-flip}
##### Stop and Think: Splitting Strategy Implications
#### ProteinGym: Comprehensive Variant Effect Evaluation {#sec-ch11-proteingym}
#### Structure Prediction Benchmarks {#sec-ch11-structure-benchmarks}
### DNA and Regulatory Benchmarks {#sec-ch11-dna-benchmarks}
#### Classical Regulatory Prediction Tasks {#sec-ch11-classical-regulatory}
### Limitation Alert: Binary Classification Over Short Windows
#### Quantitative Regulatory Prediction {#sec-ch11-quantitative-regulatory}
#### Genomic Benchmarks {#sec-ch11-genomic-benchmarks}
#### BEND: Benchmark for DNA Language Models {#sec-ch11-bend}
#### Long-Range Benchmarks {#sec-ch11-long-range}
#### Cross-Species Evaluation {#sec-ch11-cross-species}
### Variant Effect Prediction Benchmarks {#sec-ch11-vep-benchmarks}
#### Clinical Variant Databases {#sec-ch11-clinical-databases}
### Critical Limitation: ClinVar Circularity
#### CAGI: Critical Assessment of Genome Interpretation {#sec-ch11-cagi}
##### Key Insight: The Value of Prospective Evaluation
#### Deep Mutational Scanning Benchmarks {#sec-ch11-dms-benchmarks}
#### Regulatory and Non-Coding Variant Benchmarks {#sec-ch11-noncoding-benchmarks}
 - MPRA - make a glossary word.  Update other uses for typography.
 - sidebar on DMS and MPRAs, if not one already.
### Trait and Population-Level Benchmarks {#sec-ch11-trait-benchmarks}
#### Polygenic Score Evaluation {#sec-ch11-pgs-evaluation}
 - In 2nd paragraph, better explain the metrics, such as "incremental R²" over non-genetic covariates. is there a classifier equivalent?
#### TraitGym {#sec-ch11-traitgym}
 - does it do population stratified eval?
 - reference it back to proteingym.
#### EmbedGEM Framework {#sec-ch11-embedgem}
 - x-ref heritability (ch3?)
 - add figure
### Benchmark Construction and Hidden Assumptions {#sec-ch11-benchmark-construction}
#### Data Sources and Label Provenance {#sec-ch11-label-provenance}
##### Stop and Think: Label Provenance
#### Splitting Strategies and Leakage {#sec-ch11-splitting}
#### Metric Selection and Aggregation {#sec-ch11-metrics}
#### Goodhart's Law and Benchmark Gaming {#sec-ch11-goodhart}
 - X-ref and cite CAGI from above.
### Benchmark Saturation and Staleness {#sec-ch11-saturation-staleness}
#### Saturation: When Benchmarks Stop Discriminating {#sec-ch11-saturation}
 - explain bayes error rate, irreducible error, replicate convergance of assay.  Relate do uncertainty chapter (ch 24) - especially aleotoric uncertainty.
#### Staleness: When Benchmarks Diverge from Practice {#sec-ch11-staleness}
#### Leakage from Scale {#sec-ch11-leakage-scale}
 - xref circularity and leakage sections.
### Benchmark-Deployment Gap {#sec-ch11-deployment-gap}
#### Distribution Shift {#sec-ch11-distribution-shift}
 - current xref does no tpoitn to
#### Calibration Requirements {#sec-ch11-calibration-requirements}
#### Metric Mismatch {#sec-ch11-metric-mismatch}
 - xref auROC and auPRC trade-offs for benchmarking.
#### Practical Constraints {#sec-ch11-practical-constraints}
### Systematic Gaps in Current Benchmarks {#sec-ch11-systematic-gaps}
### The Proxy Problem {#sec-ch11-proxy-problem}
### Chapter Summary

#### part_3/p3-ch12-evaluation.qmd
## 12 (was 22) Evaluation Methods {#sec-ch12-eval}
### Chapter Overview
### Difficulty Warning: Methodological Rigor
### Why Random Splits Fail {#sec-ch12-random-splits-fail}
##### Key Insight: The Independence Assumption
### Homology-Aware Splitting {#sec-ch12-homology-aware-splitting}
#### Clustering Tools and Workflows {#sec-ch12-clustering-tools}
 - I don't get this.  Why are the different evolutionary rates and why does this impact thresholds?
    > For nucleotide sequences, thresholds are typically higher (80-95%) due to different evolutionary rates.
### Practical Guidance: Choosing Identity Thresholds
#### Practical Considerations {#sec-ch12-homology-practical}
### Splitting by Biological Axis {#sec-ch12-splitting-biological-axis}
#### Splitting by Individual {#sec-ch12-splitting-individual}
#### Splitting by Genomic Region {#sec-ch12-splitting-genomic-region}
#### Splitting by Gene or Protein Family {#sec-ch12-splitting-gene-family}
##### Stop and Think: Choosing the Right Split
#### Splitting by Experimental Context {#sec-ch12-splitting-experimental-context}
#### Splitting by Ancestry {#sec-ch12-splitting-ancestry}
#### Splitting by Time {#sec-ch12-splitting-time}
### Leakage Taxonomy and Detection {#sec-ch12-leakage-detection}
#### Label Leakage {#sec-ch12-label-leakage}
 - can this be rephrased.  I'm having a hard time understanding what is meant.
    > Expression models face analogous challenges when trained on features derived from the same samples used to define expression labels. The information flow becomes circular: labels inform features, which predict labels, creating apparent performance that would not generalize to independent samples.
#### Feature Leakage {#sec-ch12-feature-leakage}
#### Temporal Leakage {#sec-ch12-temporal-leakage}
 - 1st and last paragraphs seems repetitive.
#### Benchmark Leakage {#sec-ch12-benchmark-leakage}
#### Detecting Leakage {#sec-ch12-detecting-leakage}
### Practical Guidance: Leakage Detection Checklist
### Metrics for Genomic Tasks {#sec-ch12-metrics-genomic-tasks}
#### Discrimination Metrics {#sec-ch12-discrimination-metrics}
 - have a sidebar about equivilent ML and stat terms (PPV, NPV, sensitivity, specificity, recall, precision, F1, etc)
 - we also have to address the issue of threshold selection for binary classifiers.  Maybe in practical guidance?
 - also issues with class imbalance and prevalence dependence of some metrics.  Discuss MCC, micro, cohen's kappa, and balanced accuracy
##### Key Insight: Why auROC Can Mislead
#### Regression and Correlation Metrics {#sec-ch12-regression-correlation-metrics}
#### Ranking and Prioritization Metrics {#sec-ch12-ranking-prioritization-metrics}
#### Clinical Utility Metrics {#sec-ch12-clinical-utility-metrics}
### Baseline Selection {#sec-ch12-baseline-selection}
#### Strong Baselines, Not Straw Men {#sec-ch12-strong-baselines}
#### Historical Baselines and Progress Tracking {#sec-ch12-historical-baselines}
#### Non-Deep-Learning Baselines {#sec-ch12-non-dl-baselines}
### Ablation Studies {#sec-ch12-ablation-studies}
#### Component Isolation {#sec-ch12-component-isolation}
#### Hyperparameter Sensitivity {#sec-ch12-hyperparameter-sensitivity}
 -  at some point in this chapter, we need to discuss "adaptive overfitting", model selection bias, and the multiple comparisons problem, "winner's curse", and holdout test "purity".  Reference other points of the book where this is discussed.  GWAS has a related topic on multiple hypothesis testing correction that we should x-ref. 
 - reference the uncertainy chapter (ch24) when discussing variance across random seed
 - actually, some of this is better for the statistical rigor section below.
 - do we cover model selection and comparision anywhere in the book?  If not, we should add a section on this topic.
#### Architecture Search Confounds {#sec-ch12-architecture-search-confounds}
 - these 3 subsections are all 1 paragraph.  Combine?  Expand?
 - this is a "lite" versien of model comparison.
#### Reporting Standards {#sec-ch12-reporting-standards}
### Statistical Rigor {#sec-ch12-statistical-rigor}
### Two Cultures: Inference vs. Prediction
#### Significance Testing {#sec-ch12-significance-testing}
 - this needs more depth:
    > Permutation tests shuffle predictions between models and measure how often shuffled differences exceed observed differences.
#### Effect Sizes {#sec-ch12-effect-sizes}
#### Confidence Intervals on Metrics {#sec-ch12-confidence-intervals}
#### Variance Across Random Seeds {#sec-ch12-variance-random-seeds}
### Evaluating Foundation Models {#sec-ch12-evaluating-fm}
#### Zero-Shot Evaluation {#sec-ch12-zero-shot-eval}
 -x-ref to zero-shot sections in earlier chapters.
#### Linear Probing {#sec-ch12-linear-probing}
#### Fine-Tuning Evaluation {#sec-ch12-fine-tuning-eval}
#### Transfer Across Tasks {#sec-ch12-transfer-tasks}
 - x-ref to transfer learning sections in earlier chapters.
### Calibration Essentials {#sec-ch12-calibration}
#### Assessing Calibration {#sec-ch12-assessing-calibration}
#### Recalibration Methods {#sec-ch12-recalibration-methods}
#### Calibration in Model Comparison {#sec-ch12-calibration-comparison}
### Putting It All Together {#sec-ch12-putting-together}
### Practical Guidance: Evaluation Design Checklist
### The Question Behind the Metric {#sec-ch12-question-behind-metric}
### Chapter Summary

#### part_3/p3-ch13-confounding.qmd
## 13 (was 23) Confounding and Data Leakage {#sec-ch13-confounding}
### Chapter Overview
### Confounding, Bias, and Leakage {#sec-ch13-terminology}
 - "confound" - add to glossary; same with "bias", "leakage", "distribution shift"
 - distribution shift - lay out different types (covariate, prior, concept), and x-ref to other sections of the book where this is discussed.
 - define "shortcut learning" here or x-ref to other sections.
 - "predict before you look" section copies examples from earlier.
##### Key Insight: The Confounder-Mechanism Distinction
### Sources of Confounding in Genomic Data {#sec-ch13-sources}
 - at some point, relate confounders to causality chapter and backdoor paths.  X-ref both directions.
##### Stop and Think
#### Population Structure and Relatedness {#sec-ch13-ancestry-confounding}
#### Technical Batch Effects {#sec-ch13-batch-effects}
#### Institutional and Recruitment Confounding {#sec-ch13-institutional-confounding}
#### Label Generation Bias {#sec-ch13-label-bias}
#### Temporal Drift {#sec-ch13-temporal-drift}
#### Resource Overlap and Indirect Leakage {#sec-ch13-resource-overlap}
### Population Structure as a Shortcut {#sec-ch13-population-shortcut}
##### Key Insight: Capacity Amplifies Confounding
 - note that all "knowledge check" sections format the answers weird.  Numeric list doesn't render properly.
   > 1. A confounder is a variable that affects both features and labels (e.g., ancestry affects allele frequencies and disease risk through healthcare access), while data leakage occurs when test information influences training (e.g., the same variant appearing in both train and test sets). Both inflate performance, but leakage involves information that shouldn’t exist at prediction time, while confounding involves real but non-causal associations. (2) Ancestry affects genomic features through population-specific allele frequencies and haplotype structure, while simultaneously affecting disease labels through environmental factors, healthcare access, socioeconomic status, and clinical ascertainment practices—creating a spurious association pathway the model can exploit. (3) Train a confounder-only baseline using just ancestry principal components with no genomic features. If this baseline achieves performance close to your full model (e.g., 0.80 vs 0.85 auROC), ancestry confounding drives most of the signal.
### Technical Artifacts as Biological Signal {#sec-ch13-technical-artifacts}
### Label Bias and Circularity {#sec-ch13-label-circularity}
### Data Splitting {#sec-ch13-data-splitting}
 - do we discuss case-control matching anywhere?  let's x-ref it here.
 - this section has 7 subsections, each 1 paragraph.  Combine?  Expand?
### Mathematical Foundations
#### Random Individual-Level Splits {#sec-ch13-random-splits}
#### Family-Aware Splits {#sec-ch13-family-splits}
#### Locus-Level Splits {#sec-ch13-locus-splits}
#### Region and Chromosome Splits {#sec-ch13-region-splits}
#### Cohort and Site Splits {#sec-ch13-cohort-splits}
#### Temporal Splits {#sec-ch13-temporal-splits}
#### Indirect Leakage Across Resources {#sec-ch13-indirect-leakage}
### Data Leakage as Confounding {#sec-ch13-leakage-confounding}
#### Causal Structure of Leakage {#sec-ch13-leakage-causal}
#### Compounding Effects {#sec-ch13-compounding}
##### Stop and Think: Compound Leakage
#### Implications for Confounding Analysis {#sec-ch13-leakage-implications}
### Detecting Confounding {#sec-ch13-detection}
#### Confounder-Only Baselines {#sec-ch13-confounder-baselines}
##### Key Insight: The Baseline Diagnostic
#### Stratified Performance Analysis {#sec-ch13-stratified-performance}
#### Residual Confounder Associations {#sec-ch13-residual-associations}
#### Split Sensitivity Analysis {#sec-ch13-split-sensitivity}
#### Negative Control Outcomes {#sec-ch13-negative-controls}
### Mitigation Strategies {#sec-ch13-mitigation}
 - not related, but we need the classic bias-variance-complexity trade-off discussion discussed in a sidebar.  I like how McElreath's Statistical Rethinking does it.
#### Study Design and Cohort Construction {#sec-ch13-study-design}
 - Call out maximum diverse sampling that allows dropping the most redundant samples, such as on ancestry PCs.  Similar to clusting approaches used in UniRef.
 - Propensity score - proper term for prediction only without treatment variable?  Add terms such as "caliper" and such.
#### Covariate Adjustment {#sec-ch13-covariate-adjustment}
 - We touch on hierarchical models (e.g. multilevel models) here, but we should expand this a bit.  Not sure if this discussion would fit better elsewhere.
   - Based on McElreath's Statistical Rethinking book.  Discuss ideas of pooling - complete pooling, no pooling, partial pooling.  How hierarchical models allow for partial pooling, which is a bias-variance trade-off.  How this relates to mixed effects models.
   - See if anyone has done research on hierarchical models for genomic prediction tasks; confounding; and/or deep learning.
#### Domain Adaptation and Invariance Learning {#sec-ch13-domain-adaptation}
 - x-ref domain adaptation sections in earlier chapters.
#### Data Curation and Benchmark Design {#sec-ch13-benchmark-design}
 - splitting strategies - x-ref to evaluation chapter.
 - current ch 11 spec - be more specific
#### Causal Inference Approaches {#sec-ch13-causal-inference}
 - x-ref causality chapter.  is this new content, or do we already cover this there?  Synchronize
 - define instrumental variables here or x-ref to causality chapter.  New term for majority of non-statisticians
 - mendelian inheritance - improve the pedagogy here.  Important concept, but explanation dense and not clear
 - add a figure of a dag (with backdoor?)
 - Cite/ref McElrath's Statistical Rethinking book for pedagogy on causality.
### Fairness and External Validity {#sec-ch13-fairness}
### A Practical Checklist {#sec-ch13-checklist}
### Practical Guidance: Using This Checklist
### Rigor as Response {#sec-ch13-rigor}
### Chapter Summary

#### part_4/p4--fm-families.qmd

# Part V: Cellular Context {.unnumbered}

## 19 (was 15) RNA Structure and Function {#sec-ch19-rna}
 - since we have a section of RNA function and prediction that is seperate from regulatory models; should we alse have a section on protein structure and function prediction in part 4?  Or maybe that is address by the Graph and Network Models chapter?
 - This is probably out of scope, but I wander if we should have a short section on proteomics and metabolomics, metagenomics.
 - We should make it more clear this chapter is about molecular RNA, not the transcriptome readout.  Maybe add a sentence or two on how transcriptome readout is covered in the single cell chapter?  
### RNA as Molecule Versus Transcriptome Readout {#sec-ch19-perspectives}
 - This seems to infere that protein doesn't have long-range contacts, which is not true.  rephrase
    > Secondary structure arises from Watson-Crick base pairing (A-U, G-C) and wobble pairs (G-U) that create stems, loops, bulges, and internal loops. Unlike protein secondary structure, where alpha helices and beta sheets are local motifs determined by nearby residues, RNA secondary structure involves long-range contacts
 - 
### Why Secondary Structure Creates a Distinct Modeling Challenge {#sec-ch19-structure-challenge}
#### Flat Energy Landscape Problem {#sec-ch19-energy-landscape}
#### Base Pairing and Long-Range Dependencies {#sec-ch19-base-pairing}
#### Pseudoknots and Tertiary Complexity {#sec-ch19-pseudoknots}
### Classical Approaches to Structure Prediction {#sec-ch19-classical}
#### Thermodynamic Folding Models {#sec-ch19-thermodynamic}
#### Comparative and Covariation Methods {#sec-ch19-comparative}
### Deep Learning for Secondary Structure Prediction {#sec-ch19-dl-structure}
#### From Thermodynamics to Learned Patterns {#sec-ch19-learned-patterns}
 - cite SPOT-RNA
#### Structure Probing as Supervision {#sec-ch19-structure-probing}
### RNA Foundation Models {#sec-ch19-foundation}
#### Scale Gap with Protein Language Models {#sec-ch19-scale-gap}
 - in the figure 19.3 caption, cite PDB.  Also verify protein and rna structure counts.  200k seems low.
    > Secondary structure arises from Watson-Crick base pairing (A-U, G-C) and wobble pairs (G-U) that create stems, loops, bulges, and internal loops. Unlike protein secondary structure, where alpha helices and beta sheets are local motifs determined by nearby residues, RNA secondary structure involves long-range contacts
 - verify counts of >65 millon and 23 million.  Fix claim of this being an order of magnitude difference.
    > The comparison with ESM illustrates the gap. ESM-2 trained on over 65 million protein sequences from UniRef, spanning the known diversity of protein families (Chapter 16). RNA-FM, one of the more successful RNA foundation models, trained on approximately 23 million noncoding RNA sequences from RNAcentral (Chen et al. 2022). While not a trivial corpus, this represents an order of magnitude fewer sequences, and the RNA sequences span a narrower range of structural and functional diversity than proteins. 
 - this is a weird claim that proteins have more evolutionary history than rna.  Also the main text repeats some of the "key insight".   Also molecular rna is a lot more diverse in moleclar use that protein (transcripts with intron exon structure, micro rnas, long non-coding rnas, reverse trascription, etc).  Review full section and rephrase.
   > The gap between RNA and protein foundation models is not primarily about architecture or training objectives—it’s about data. Proteins have accumulated over 4 billion years of evolution across all domains of life, with rich structural annotations from crystallography and cryo-EM. RNA databases are smaller, biased toward well-characterized families, and lack equivalent structural training sets. Until this data gap closes, RNA foundation models will struggle to achieve protein-like breakthroughs. 

#### Architectures and Objectives {#sec-ch19-architectures}
#### Downstream Applications {#sec-ch19-downstream}
### Codon-Level Models for Coding RNA {#sec-ch19-codon}
#### Beyond Nucleotide Tokenization {#sec-ch19-codon-tokenization}
 - Can we also cite the blog post by NVIDIA of CodonFM, the unpublish successor to EnCodon?  Or would this be inappropriate since it is not peer reviewed?  
 - [catalog.ngc.nvidia.com/orgs/nvidia/teams/clara/models/nv_codonfm_encodon?version=NV-CodonFM-Encodon-1B-v1]
#### What Codon Models Add {#sec-ch19-codon-advantages}
### UTR Models and Translation Regulation {#sec-ch19-utr}
#### Why UTRs Dominate Expression Control {#sec-ch19-utr-control}
 - expand terms a bit, like why is the Kozak sequence important?
#### Sequence-to-Expression Models {#sec-ch19-expression-models}
 - the names in the text don't match the paper:
    > Agarwal and Kelley trained models on endogenous mRNA stability measurements, demonstrating that 3’ UTR sequence features explain substantial variance in half-life across the transcriptome (Agarwal and Shendure 2020).
#### Integration with mRNA Design {#sec-ch19-utr-design}
 - how much of this is overlapping with part VII, such as chapter 30 and 31?  At least add some cross references.
### mRNA Design and Optimization {#sec-ch19-mrna-design}
 - how much of this is overlapping with part VII, such as chapter 30 and 31?  At least add some cross references.
#### Design Objectives and Trade-offs {#sec-ch19-design-objectives}
#### Lessons from COVID-19 Vaccines {#sec-ch19-covid-vaccines}
#### Model-Based Design Strategies {#sec-ch19-model-design}
 - explain:
    > adaptation indices like CAI or tAI, particularly for context-specific expression prediction
### Noncoding RNA Classification and Function {#sec-ch19-ncrna}
 - add a figure with visuals of different types of non-coding rnas (miRNA, lncRNA, snoRNA, etc)
#### Diversity of Noncoding RNA {#sec-ch19-ncrna-diversity}
#### From Handcrafted Features to Learned Representations {#sec-ch19-ncrna-features}
### miRNA Target Prediction {#sec-ch19-mirna}
 - what are "AntimiR oligonucleotides "
 - a tangent, but worth discussing DNA/RNA aptamers here or in ch31 on design?
### Splicing and Transcript Processing Models {#sec-ch19-splicing}
#### Beyond SpliceAI {#sec-ch19-beyond-spliceai} 
 - a visual of breakpoints would be helpful here
### Limitations and Open Challenges {#sec-ch19-limitations}
#### Sparse Structural Data {#sec-ch19-sparse-data}
#### Functional Annotation Gaps {#sec-ch19-annotation-gaps}
#### Maturity Gap {#sec-ch19-maturity-gap}
### Bridge Between Sequence and Cell {#sec-ch19-bridge}

#### part_5/p5-ch20-single-cell.qmd
## 20 (was 16) Single-Cell Models {#sec-ch20-single-cell}
 - Remove hard-coded "Part III" and x-ref the Part III intro.  Do same throughout book.
 - A good chapter.  Maybe too much biological details???  Let's discuss
### Chapter Overview
### Single-Cell Data Landscape {#sec-ch20-data}
#### From Bulk to Single-Cell Resolution {#sec-ch20-bulk-to-sc}
##### Stop and Think: The Averaging Problem
##### Key Insight: The Cell-as-Document Analogy
#### Technical Challenges and Data Characteristics {#sec-ch20-technical}
### Cellular Language Models {#sec-ch20-clm}
#### *Geneformer*: Learning Network Biology {#sec-ch20-geneformer}
##### Worked Example: Rank-Based Encoding
#### *scGPT*: Generative Pretraining for Single-Cell Analysis {#sec-ch20-scgpt}
##### Stop and Think: Multiple Pretraining Objectives
#### *scFoundation* and Scaling Single-Cell Models {#sec-ch20-scfoundation}
#### *TranscriptFormer*: Cross-Species Cellular Models {#sec-ch20-transcriptformer}
##### Key Insight: Cross-Species Transfer Reveals Conserved Regulatory Programs
### Perturbation Response Prediction {#sec-ch20-perturbation}
#### *In Silico* Experiment Promise {#sec-ch20-in-silico}
##### Stop and Think: From Correlation to Causation
#### Perturb-seq and Foundation Model Training {#sec-ch20-perturb-seq}
#### Limitations of Current Approaches {#sec-ch20-perturbation-limits}
### Practical Guidance: When to Trust Perturbation Predictions
### Epigenomic Foundation Models {#sec-ch20-epigenomic}
#### DNA Methylation and *CpGPT* {#sec-ch20-methylation}
#### Chromatin Accessibility Models {#sec-ch20-accessibility}
##### Knowledge Check: Epigenomic Data Types
### Cross-Modality Integration {#sec-ch20-integration}
#### Unpaired Integration Challenge {#sec-ch20-unpaired}
#### *GLUE*: Graph-Linked Unified Embedding {#sec-ch20-glue}
##### Key Insight: Biological Knowledge as Regularizer
#### Applications of Cross-Modal Integration {#sec-ch20-cross-modal-apps}
### Practical Challenges and Limitations {#sec-ch20-limitations}
#### Batch Effects and Technical Artifacts {#sec-ch20-batch-effects}
#### Cell Type Imbalance {#sec-ch20-imbalance}
#### Evaluation Complexity {#sec-ch20-evaluation}
##### Stop and Think: The Ground Truth Problem
#### Causality and Mechanism {#sec-ch20-causality}
### Practical Guidance: Responsible Use of Single-Cell Foundation Models
### From Sequence to State {#sec-ch20-conclusion}
### Chapter Summary

#### part_5/p5-ch21-3d-genome.qmd
## 21 (was 17) 3D Genome Organization {#sec-ch21-3d-genome}
### Chromatin Organization Hierarchy {#sec-ch21-chromatin-hierarchy}
#### Chromosome Territories and Compartments {#sec-ch21-territories-compartments}
 - Have a sidebar about Hi-C contact maps; terratories show up as checkboard or diagonal blocks (verify); TADs as triangles.
#### Topologically Associating Domains {#sec-ch21-tads}
#### Loop Extrusion Mechanism {#sec-ch21-loop-extrusion}
#### Fine-Scale Chromatin Loops {#sec-ch21-fine-scale-loops}
### Measuring the 3D Genome {#sec-ch21-3d-measurement}
#### Hi-C and Contact Matrices {#sec-ch21-hic-matrices}
#### Resolution and Data Resources {#sec-ch21-3d-data-resources}
### Predicting 3D Structure from Sequence {#sec-ch21-3d-prediction}
#### *Akita* and Dilated Convolutions {#sec-ch21-akita}
#### *Orca* and Multiscale Prediction {#sec-ch21-orca}
#### *C.Origami* and Cross-Cell-Type Transfer {#sec-ch21-c-origami}
#### Learned Sequence Determinants {#sec-ch21-3d-interpretability}
 - Micro-C vs Hi-C distinction?  Does Micro-C have more data than Hi-C?  Seems opposite of expectation.
### 3D Structure and Gene Regulation {#sec-ch21-3d-regulation}
#### Beyond One-Dimensional Models {#sec-ch21-beyond-1d}
#### Structural Variant Interpretation {#sec-ch21-sv-interpretation}
#### Causality and Permissive Architecture {#sec-ch21-3d-causality}
### Spatial Transcriptomics {#sec-ch21-spatial-transcriptomics}
#### Measurement Technologies {#sec-ch21-spatial-technologies}
#### Computational Challenges {#sec-ch21-spatial-computation}
#### Spatial Foundation Models {#sec-ch21-spatial-models}
### Limitations and Open Questions {#sec-ch21-3d-limitations}
### Structure as Context, Not Cause {#sec-ch21-structure-context}

#### part_5/p5-ch22-networks.qmd
## 22 (was 18) Graph and Network Models {#sec-ch22-networks}
### Chapter Overview
 - Explain more on graph topology basics in a sidebar.  This will be a new concept for most readers.
 - Add sections on types of graph prediction (local, global, representation learning, link prediction, node prediction, graph-prediciton, etc)
 - graph types (e.g. heterogenious, multi-graphs, etc.)
##### Key Insight: The Division of Labor
### Biological Networks and Data Resources {#sec-ch22-biological-networks}
#### Landscape of Biological Graphs {#sec-ch22-landscape}
- use "Topology" instead of "shape"???
- all the graph databases - move to database chapter (2), or keep here due to being specalized?
- Where is KEGG???
- Break into more subsectios?
- Add some depth here.  What do spacial interaciton graphs look like?
   > Spatially resolved transcriptomics and imaging data give rise to graphs capturing tissue organization invisible to bulk or even single-cell measurements (Chapter 20). In these spatial and cell-cell interaction graphs, nodes represent cells or spatial locations, while edges encode physical proximity or inferred ligand-receptor communication. Such graphs enable questions about how spatial context influences cell behavior. 
##### Knowledge Check: Network Bias
#### Biases and Limitations {#sec-ch22-network-biases}
### Graph Neural Network Fundamentals {#sec-ch22-gnn-fundamentals}
 - The CH06 and CH07 references are very late in the sentence, so it is hard to track what they refer to.  Rephrase.
    >  Where convolutional and transformer models operate on regular structures (sequences, grids), GNNs must handle irregular topology with variable-degree nodes, no inherent ordering, and arbitrary connectivity (Chapter 6, Chapter 7). 
#### Message Passing Principles {#sec-ch22-message-passing}
 - Previously the 1st paragraph match the paragram in @sect-ch22-gnn-fundamentals.  This seems resolved now, but verify.
##### Key Insight: Message Passing as Neural Diffusion
##### Knowledge Check
#### Canonical Architectures {#sec-ch22-canonical-architectures}
 - Explain this test:
  > The expressiveness of GNNs is bounded by their ability to distinguish different graph structures. Theoretical analysis connects standard message passing to the Weisfeiler-Lehman graph isomorphism test, revealing that certain graph structures remain indistinguishable regardless of the number of layers  
### Difficulty Warning: Over-Smoothing
### Foundation Model Embeddings as Node Features {#sec-ch22-fm-embeddings}
#### Integration Principle {#sec-ch22-integration-principle}
##### Stop and Think
#### Practical Integration Patterns {#sec-ch22-practical-patterns}
### Practical Guidance: Choosing an Integration Strategy
#### Evidence for the Integration Benefit {#sec-ch22-integration-evidence}
### Applications {#sec-ch22-applications}
#### Disease Gene Prioritization {#sec-ch22-disease-gene}
##### Key Insight: Beyond Guilt by Association
#### Drug-Target Interaction Prediction {#sec-ch22-drug-target}
##### Stop and Think
#### Knowledge Graph Reasoning and Drug Repurposing {#sec-ch22-kg-reasoning}
#### Pathway and Module Analysis {#sec-ch22-pathway-analysis}
#### Cell Type and State Annotation {#sec-ch22-cell-annotation}
### Practical Considerations {#sec-ch22-practical}
#### Graph Construction Quality {#sec-ch22-graph-construction}
### Practical Guidance: Graph Construction Checklist
#### Scalability and Mini-Batching {#sec-ch22-scalability}
#### Robustness to Noise and Missingness {#sec-ch22-robustness}
##### Knowledge Check
#### Interpretation and Validation {#sec-ch22-interpretation}
### Limitations and Open Challenges {#sec-ch22-limitations}
#### Study Bias Problem {#sec-ch22-study-bias}
#### Causality Versus Association {#sec-ch22-causality}
### Critical Limitation
#### Negative Data and Class Imbalance {#sec-ch22-negative-data}
#### Distribution Shift {#sec-ch22-distribution-shift}
### Sequence Encodes, Structure Connects {#sec-ch22-conclusion}
### Chapter Summary

#### part_5/p5-ch23-multi-omics.qmd
## 23 (was 19) Multi-Omics Integration {#sec-ch23-multi-omics}
 - Add refernec to Model-X knockoffs for high-dimensional integration with FDR control (also in Causality chapter).
 - Other items for high-dimensionality integration.
 - Is GraphSage relevent here for embeddings?
### Chapter Overview
### Limits of Single-Modality Models {#sec-ch23-limits}
 - Add GWAS x-ref. 
- Add citation and fix heritability gap claim of 10-20%, which seems very low for GWAS.
##### Stop and Think
### Integration Strategies and Their Tradeoffs {#sec-ch23-strategies}
#### Early Fusion {#sec-ch23-early-fusion}
#### Late Fusion {#sec-ch23-late-fusion}
 - Discuss late fusion vs ensemble learning a bit more.
#### Intermediate Fusion {#sec-ch23-intermediate-fusion}
##### Stop and Think
##### Key Insight
### Multi-Omics Foundation Models {#sec-ch23-foundation-models}
#### Factor-Based Integration {#sec-ch23-factor-integration}
#### Deep Generative Multi-Omics Models {#sec-ch23-deep-generative}
##### Knowledge Check
#### Contrastive Multi-Modal Learning {#sec-ch23-contrastive}
### Clinical Integration: EHR, Imaging, and Molecular Data {#sec-ch23-clinical-integration}
 - Maybe some notes here on dealing with the time series nature of EHR longitudinal data?
#### Electronic Health Records as a Modality {#sec-ch23-ehr}
##### Key Insight
#### Imaging Integration {#sec-ch23-imaging}
#### Multi-Modal Clinical Prediction Models {#sec-ch23-multimodal-clinical}
### Practical Guidance
### Systems View: From Variant to Phenotype {#sec-ch23-systems-view}
#### Information Cascade {#sec-ch23-information-cascade}
#### Bottleneck Modalities {#sec-ch23-bottleneck}
##### Stop and Think
##### Key Insight
#### Causal vs. Correlational Integration {#sec-ch23-causal-correlational}
### Handling Missing Modalities {#sec-ch23-missing-modalities}
### Challenging Section
#### Training with Incomplete Data {#sec-ch23-incomplete-training}
#### Cross-Modal Imputation {#sec-ch23-imputation}
#### Zero-Shot Cross-Modal Transfer {#sec-ch23-zero-shot}
### Practical Challenges {#sec-ch23-practical-challenges}
#### Batch Effects Across Modalities {#sec-ch23-batch-effects}
#### Sample Size and Power {#sec-ch23-sample-size}
#### Interpretability Across Modalities {#sec-ch23-interpretability}
#### Evaluation Complexity {#sec-ch23-evaluation}
##### Knowledge Check
### Integration as Means, Not End {#sec-ch23-conclusion}
### Chapter Summary

#### part_6/p6--responsible-deployment.qmd


# Part VI: Responsible Deployment {.unnumbered}

## 24 Uncertainty Quantification {#sec-ch24-uncertainty}
 - epitaph: fix with pedagogy agent.  It sounds more silly than profound.
   > A pathogenicity score of 0.73 means nothing unless we know what 0.73 means.
### Chapter Overview
### Types of Uncertainty in Genomic Prediction {#sec-ch24-types}
#### Why Uncertainty Matters {#sec-ch24-why-uncertainty}
##### Key Insight: Calibration vs. Accuracy
#### Epistemic Uncertainty {#sec-ch24-epistemic}
 - this is making me think of Bayesian optimization, gaussian processes, active learning, and exploration vs exploitation.  Maybe we can add a section on this later?  Maybe already covered in drug discovery chapter?
##### Stop and Think
#### Aleatoric Uncertainty {#sec-ch24-aleatoric}
 - relate to bayers error rate, irreducible error, replciate convergance of assay, etc.  See @sec-ch11-saturation
 - valitate use of heteroscedacitity.
 - this "irreducible error" concept seems too black-and-white.  Let's discuss practical items as well, such as process/tech improvent, imploved label qc, etc.  This can reduce aleatoric uncertainty in practice, so it is not truely "irreducible".
#### Decomposing Total Uncertainty {#sec-ch24-decomposition}
 - Let's add some math equations here for variance decomposition.
 - We touch on Heteroscedastisc neural networks, but we should expand this a bit.  Def add a citation or two.
### Difficulty Warning
### Calibration and Confidence Interpretation {#sec-ch24-calibration}
 - "This Chapter", "you", etc.  Let's try and avoid meta commentary.
 - Figure 24.2 has the old C&D diagrams. I thought we added the new ones?  Verify and fix across all figures with >2 panels.
#### The Calibration Problem {#sec-ch24-calibration-problem}
 - for example of perfect calibration and absolute no prediction, use example of predicting all variants as 0.5 pathogenicity, not 0.49 pos and 0.51 neg.  This is more clear cut.
##### Knowledge Check
#### Measuring Calibration {#sec-ch24-measuring-calibration}
#### Why Foundation Models Are Often Miscalibrated {#sec-ch24-fm-miscalibration}
#### Calibration Across Subgroups {#sec-ch24-subgroup-calibration}
##### Key Insight: Hidden Calibration Disparities
### Post-Hoc Calibration Methods {#sec-ch24-post-hoc-calibration}
##### Stop and Think
#### Temperature Scaling {#sec-ch24-temperature-scaling}
#### Platt Scaling {#sec-ch24-platt-scaling}
#### Isotonic Regression {#sec-ch24-isotonic-regression}
#### Calibrating Foundation Model Outputs {#sec-ch24-calibrating-fm}
### Practical Guidance: Calibration Workflow
### Uncertainty Quantification Methods for Foundation Models {#sec-ch24-uq-methods}
#### Deep Ensembles {#sec-ch24-deep-ensembles}
#### Monte Carlo Dropout {#sec-ch24-mc-dropout}
##### Stop and Think
#### Heteroscedastic Models {#sec-ch24-heteroscedastic}
#### Evidential Deep Learning {#sec-ch24-evidential}
#### Selecting Uncertainty Quantification Methods {#sec-ch24-selecting-uq}
### Conformal Prediction: Distribution-Free Guarantees {#sec-ch24-conformal}
##### Key Insight: Prediction Sets Convey Uncertainty Without Probabilities
#### Split Conformal Prediction {#sec-ch24-split-conformal}
### Difficulty Warning
#### Conformal Prediction for Variant Classification {#sec-ch24-conformal-variant}
#### Limitations and Practical Considerations {#sec-ch24-conformal-limitations}
#### Integration with Clinical Workflows {#sec-ch24-conformal-clinical}
### Out-of-Distribution Detection {#sec-ch24-ood-detection}
#### Out-of-Distribution Problem {#sec-ch24-ood-problem}
##### Knowledge Check
#### Likelihood-Based Detection and Its Failures {#sec-ch24-likelihood-ood}
#### Embedding-Based Detection {#sec-ch24-embedding-ood}
#### Practical OOD Detection for Genomic Applications {#sec-ch24-practical-ood}
### Practical Guidance: OOD Detection Pipeline
### Selective Prediction and Abstention {#sec-ch24-selective-prediction}
#### When to Abstain {#sec-ch24-when-abstain}
#### Selective Prediction Methods {#sec-ch24-selective-methods}
#### Evaluating Selective Prediction {#sec-ch24-selective-eval}
### Uncertainty for Specific Genomic Tasks {#sec-ch24-genomic-uq}
#### Variant Effect Prediction Uncertainty {#sec-ch24-vep-uncertainty}
#### Regulatory Variant Uncertainty {#sec-ch24-regulatory-uncertainty}
#### Uncertainty Across Populations {#sec-ch24-population-uncertainty}
### Communicating Uncertainty to End Users {#sec-ch24-communication}
#### Communication Challenge {#sec-ch24-communication-challenge}
#### Categorical Reporting {#sec-ch24-categorical-reporting}
#### Visual Communication {#sec-ch24-visual-communication}
#### Decision-Theoretic Framing {#sec-ch24-decision-framing}
### Necessary but Insufficient {#sec-ch24-conclusion}
### Chapter Summary

#### part_6/p6-ch25-interpretability.qmd
## 25 Interpretability {#sec-ch25-interpretability}
### Chapter Overview
### Attribution Methods and Input Importance {#sec-ch25-attribution}
#### *In Silico* Mutagenesis {#sec-ch25-ism}
##### Stop and Think: Attribution Method Tradeoffs
#### Gradient-Based Attribution {#sec-ch25-gradient}
##### Key Insight: The Saturation Problem
#### Reconciling Attribution Methods {#sec-ch25-reconciling}
### Interpreting Convolutional Filters {#sec-ch25-cnn-filters}
#### From Filters to Position Weight Matrices {#sec-ch25-filter-pwm}
##### Knowledge Check: CNN Filter Interpretation
#### Deeper Layers and Combinatorial Patterns {#sec-ch25-deeper-layers}
### Motif Discovery from Attributions {#sec-ch25-motif-discovery}
##### Key Insight: Why TF-MoDISco Works Better Than Traditional Motif Finding
### Probing Learned Representations {#sec-ch25-probing}
#### Probing Methodology {#sec-ch25-probing-methods}
##### Stop and Think: Probing and Confounding
#### Limitations of Probing {#sec-ch25-probing-limits}
##### Challenge Alert: The Selectivity-Accessibility Tradeoff
### Attention Patterns in Transformer Models {#sec-ch25-attention}
#### What Attention Patterns Reveal {#sec-ch25-attention-patterns}
#### Why Attention Weights Mislead {#sec-ch25-attention-caution}
##### Key Insight: Attention Is Not Explanation
### Regulatory Vocabularies and Global Interpretability {#sec-ch25-global}
#### Sequence Classes from *Sei* {#sec-ch25-sei}
##### Knowledge Check: Local vs. Global Interpretability
#### Embedding Geometry and Regulatory Programs {#sec-ch25-embedding-geometry}
### Mechanistic Interpretability {#sec-ch25-mechanistic}
##### Challenge Alert: Frontier Research Area
#### Circuits and Features {#sec-ch25-circuits}
#### Applications to Genomic Models {#sec-ch25-mechanistic-genomics}
### Validation: From Explanations to Experiments {#sec-ch25-validation}
#### Faithfulness Testing {#sec-ch25-faithfulness}
#### Experimental Validation {#sec-ch25-experimental}
##### Stop and Think: Designing Validation Experiments
### Interpretability in Clinical Variant Assessment {#sec-ch25-clinical}
### Practical Guidance: Communicating Interpretability in Clinical Reports
### Practical Approaches for Foundation Model Analysis {#sec-ch25-practical}
### Plausibility Is Not Faithfulness {#sec-ch25-conclusion}
### Chapter Summary

#### part_6/p6-ch26-causal.qmd
## 26 Causality {#sec-ch26-causal}
### Chapter Overview
### Prediction vs. Causation {#sec-ch26-prediction-vs-causation}
#### The Ladder of Causation {#sec-ch26-ladder}
##### Key Insight: The Rung Gap is Qualitative, Not Quantitative
#### Why Predictive Accuracy Does Not Equal Causal Understanding {#sec-ch26-prediction-not-causation}
##### Stop and Think: Diagnosing Causal Structure
#### The Clinical Stakes {#sec-ch26-clinical-stakes}
### Causal Methods in Genomics {#sec-ch26-causal-methods}
#### Mendelian Randomization {#sec-ch26-mendelian-randomization}
##### Conceptual Difficulty
#### Model-X Knockoffs for Controlled Variable Selection {#sec-ch26-knockoffs}
##### Worked Example: Mendelian Randomization for Drug Target Validation
#### Fine-Mapping for Causal Variants {#sec-ch26-fine-mapping}
#### From GWAS to Causal Genes {#sec-ch26-gwas-to-genes}
### Foundation Models and Causality {#sec-ch26-fm-causality}
#### Can Foundation Models Learn Causal Structure? {#sec-ch26-fm-causal-structure}
##### Knowledge Check: Observational vs. Interventional Learning
#### In-Silico Perturbation Prediction {#sec-ch26-in-silico-perturbation}
#### Counterfactual Reasoning Limitations {#sec-ch26-counterfactual-limits}
##### Key Insight: The Counterfactual Barrier
### Intervention Prediction {#sec-ch26-intervention-prediction}
#### CRISPR Screen Analysis with Foundation Models {#sec-ch26-crispr-screens}
#### Drug Response Prediction {#sec-ch26-drug-response}
##### Stop and Think: Validating Drug Response Predictions
#### Closed-Loop Experimental Validation {#sec-ch26-closed-loop}
### Causal Discovery {#sec-ch26-causal-discovery}
#### Learning Regulatory Networks {#sec-ch26-regulatory-networks}
#### Temporal Causality {#sec-ch26-temporal-causality}
#### Multi-Omics Causal Structure {#sec-ch26-multi-omics-causal}
##### Stop and Think: Causal Structure Across Omics Layers
### Clinical Implications {#sec-ch26-clinical-implications}
#### Drug Target Validation Evidence Hierarchy {#sec-ch26-target-validation}
### Practical Guidance: Communicating Causal Claims
#### Regulatory Requirements for Causal Claims {#sec-ch26-regulatory-requirements}
### Looking Forward {#sec-ch26-conclusion}
### Chapter Summary

#### part_6/p6-ch27-regulatory.qmd
## 27 Regulatory and Governance {#sec-ch27-regulatory}
### Chapter Overview
### Regulatory Frameworks for Genomic AI {#sec-ch27-regulatory}
#### Software as Medical Device Paradigm {#sec-ch27-samd}
##### Worked Example: SaMD Classification for a Variant Classifier
##### Stop and Think
##### Key Insight: The Locked vs. Adaptive Dilemma
#### European and Global Regulatory Landscapes {#sec-ch27-global-regulation}
#### Validation Requirements for Clinical Genomic AI {#sec-ch27-validation}
##### Knowledge Check
##### Worked Example: Regulatory Submission for AlphaMissense
### Data Governance and Consent {#sec-ch27-governance}
#### Consent Problem at Scale {#sec-ch27-consent}
### Difficulty Warning
#### Biobank Governance Models {#sec-ch27-biobanks}
##### Stop and Think
#### Secondary Use and Data Futures {#sec-ch27-secondary-use}
### Privacy and Genomic Data {#sec-ch27-privacy}
##### Key Insight: Genomes Are Their Own Identifiers
#### Re-identification Challenge {#sec-ch27-reidentification}
#### Family and Relational Privacy {#sec-ch27-family-privacy}
### Intellectual Property and Ownership {#sec-ch27-ip}
#### Genomic Data Ownership {#sec-ch27-data-ownership}
##### Knowledge Check
#### Model Weights as Assets {#sec-ch27-model-weights}
#### Prediction Ownership and Liability {#sec-ch27-liability}
### Practical Guidance: Navigating Liability in Model Deployment
### Responsible Development Practices {#sec-ch27-responsible}
#### Transparency and Documentation {#sec-ch27-transparency}
#### Fairness and Performance Equity {#sec-ch27-fairness}
##### Key Insight: Bias Is Structural, Not Just Technical
#### Human Oversight and Decision Support {#sec-ch27-oversight}
##### Stop and Think
### Dual Use and Biosecurity {#sec-ch27-biosecurity}
#### Generative Models and Pathogen Enhancement {#sec-ch27-pathogen}
### Difficulty Warning
#### Access Controls and Responsible Release {#sec-ch27-access}
### Chapter Summary

#### part_7/p7--applications.qmd

# Part VII: Applications & Frontiers {.unnumbered}

## 28 Clinical Risk Prediction {#sec-ch28-clinical-risk}
### Chapter Overview
### From Polygenic Scores to Foundation Model Features {#sec-ch28-pgs-to-fm}
##### Stop and Think
##### Key Insight: From Scalar Scores to Rich Representations
### Defining Clinical Risk Prediction {#sec-ch28-defining-risk}
### Feature Integration Architectures {#sec-ch28-feature-integration}
### Practical Guidance: Choosing a Fusion Architecture
### EHR Integration and Phenotype Embeddings {#sec-ch28-ehr-integration}
#### EEPRS Framework {#sec-ch28-eeprs}
#### Understanding When Embeddings Help {#sec-ch28-embeddings-help}
##### Knowledge Check
#### PRS-PheWAS for Clinical Interpretation {#sec-ch28-prs-phewas}
#### Implementation Considerations {#sec-ch28-eeprs-implementation}
#### Integration with Foundation Model Features {#sec-ch28-eeprs-fm}
### Temporal Modeling Architectures {#sec-ch28-temporal-modeling}
### Challenging Material Ahead
##### Key Insight: Static Genetics, Dynamic Clinical Context
### Evaluation for Clinical Deployment {#sec-ch28-evaluation}
##### Stop and Think
#### Discrimination {#sec-ch28-discrimination}
#### Calibration {#sec-ch28-calibration}
#### Clinical Utility {#sec-ch28-clinical-utility}
#### Validation Hierarchy {#sec-ch28-validation-hierarchy}
### Uncertainty Quantification {#sec-ch28-uncertainty}
##### Knowledge Check
### Fairness and Health Equity {#sec-ch28-fairness}
##### Key Insight: Bias Compounds Through the Pipeline
### Clinical Integration {#sec-ch28-clinical-integration}
#### Workflow Integration Patterns {#sec-ch28-workflow-patterns}
### Practical Guidance: Integration Patterns by Use Case
#### System Architecture {#sec-ch28-system-architecture}
#### Post-Deployment Monitoring {#sec-ch28-monitoring}
### Regulatory and Quality Frameworks {#sec-ch28-regulatory}
### Case Studies {#sec-ch28-case-studies}
##### Stop and Think
#### Cardiometabolic Risk Stratification {#sec-ch28-case-cardio}
#### Oncology Prognosis {#sec-ch28-case-oncology}
#### Pharmacogenomic Adverse Event Prediction {#sec-ch28-case-pharmacogenomics}
### Translation as the Test {#sec-ch28-translation-test}
### Chapter Summary

#### part_7/p7-ch29-rare-disease.qmd
## 29 Rare Disease Diagnosis {#sec-ch29-rare-disease}
### Chapter Overview
### Variant Prioritization Funnel {#sec-ch29-prioritization-funnel}
##### Stop and Think
#### Quality and Technical Filters {#sec-ch29-quality-filters}
#### Population Frequency Filters {#sec-ch29-frequency-filters}
##### Key Insight: Frequency Thresholds Are Disease-Specific
#### Consequence and Gene Filters {#sec-ch29-consequence-filters}
#### Foundation Model Scoring {#sec-ch29-fm-scoring}
### ACMG-AMP Criteria and Computational Evidence {#sec-ch29-acmg-amp}
#### Evidence Categories {#sec-ch29-evidence-categories}
##### Knowledge Check
#### PP3 and BP4: Computational Evidence {#sec-ch29-pp3-bp4}
### Challenging Concept: Evidence Strength Calibration
#### Calibrating Predictions to Evidence Strength {#sec-ch29-calibration}
### Family-Based Analysis {#sec-ch29-family-analysis}
##### Key Insight: Family Structure Multiplies Interpretive Power
#### *De Novo* Variants {#sec-ch29-de-novo}
#### Compound Heterozygosity and Phasing {#sec-ch29-compound-het}
#### Segregation Analysis {#sec-ch29-segregation}
### Somatic Variant Interpretation in Cancer {#sec-ch29-somatic}
#### Germline versus Somatic Distinction {#sec-ch29-germline-somatic}
##### Knowledge Check
#### Driver Classification {#sec-ch29-driver}
#### Therapeutic Biomarkers {#sec-ch29-biomarkers}
### Practical Guidance: When FM Predictions Help with Novel Therapeutic Variants
### Laboratory Validation {#sec-ch29-validation}
#### Types of Functional Assays {#sec-ch29-assay-types}
#### Integrating Functional Evidence {#sec-ch29-functional-integration}
##### Stop and Think
#### Closing the VUS Loop {#sec-ch29-vus-loop}
### Practical Workflow Integration {#sec-ch29-workflow}
#### Laboratory Workflow {#sec-ch29-lab-workflow}
### Practical Guidance: Documenting FM Predictions in Clinical Reports
#### Clinical Decision-Making {#sec-ch29-clinical-decisions}
#### Regulatory and Ethical Considerations {#sec-ch29-regulatory}
##### Key Insight: Equity in Computational Predictions
### Interpretive Partnership {#sec-ch29-partnership}
### Chapter Summary

#### part_7/p7-ch30-drug-discovery.qmd
## 30 Drug Discovery {#sec-ch30-drug-discovery}
### Chapter Overview
##### Case Study: PCSK9 and Genetic Target Validation
##### Key Insight: The Genetic Validation Advantage
### Genetic Foundation of Target Selection {#sec-ch30-genetic-foundation}
#### From Variant-Level Predictions to Gene-Level Evidence {#sec-ch30-variant-to-gene}
##### Stop and Think
#### Linking Genetics to Target Safety and Efficacy {#sec-ch30-safety-efficacy}
##### Knowledge Check
### Network-Aware Target Discovery and Repurposing {#sec-ch30-network-discovery}
#### Propagating Genetic Signals Through Networks {#sec-ch30-network-propagation}
##### Key Insight: Single-Gene vs. Network Evidence
#### Drug Repurposing Through Shared Representations {#sec-ch30-repurposing}
##### Case Study: Metformin and Network-Based Repurposing
### Correlation vs. Causation in Repurposing
### Drug-Target Interaction Prediction {#sec-ch30-dti-prediction}
#### Representing Targets for Binding Prediction {#sec-ch30-binding-prediction}
##### Stop and Think
##### Worked Example: DTI Prediction for a Novel Kinase Target
#### Selectivity and Off-Target Prediction {#sec-ch30-selectivity}
### Toxicity Prediction from Genomic Context {#sec-ch30-toxicity}
#### Genetic Evidence of Target Liabilities {#sec-ch30-genetic-liabilities}
### Practical Guidance: Genetic Safety Signals
#### Expression-Based Toxicity Prediction {#sec-ch30-expression-toxicity}
##### Worked Example: Predicting Hepatotoxicity from Perturbation Signatures
#### Integrating Genomic Context with Chemical Properties {#sec-ch30-integrated-toxicity}
### Functional Genomics Screens and Perturbation Models {#sec-ch30-functional-screens}
#### Designing Informative Perturbation Libraries {#sec-ch30-library-design}
##### Knowledge Check
#### Perturb-seq and Transcriptomic Readouts {#sec-ch30-perturb-seq}
#### Closing the Loop: Lab-in-the-Loop Refinement {#sec-ch30-lab-in-loop}
### Advanced Topic
##### Key Insight: The Bayesian Interpretation of Lab-in-the-Loop
### Biomarker Development and Patient Stratification {#sec-ch30-biomarkers}
#### Foundation Model Features for Stratification {#sec-ch30-stratification-features}
##### Stop and Think
##### Worked Example: FM-Enhanced Stratification for Cardiovascular Risk
#### Multi-Omic Biomarker Discovery {#sec-ch30-multi-omic-biomarkers}
#### Trial Design and Endpoint Selection {#sec-ch30-trial-design}
### Industry Workflows and Infrastructure {#sec-ch30-industry-workflows}
#### Building Model Infrastructure {#sec-ch30-model-infrastructure}
#### Strategic Choices: Build, Buy, or Fine-Tune {#sec-ch30-build-buy-finetune}
#### Industry Context: Timelines and Decision Gates {#sec-ch30-timelines}
### Practical Guidance: Aligning FM Work with Drug Development Gates
#### Intellectual Property and Data Considerations {#sec-ch30-ip-data}
### Evaluation and Validation {#sec-ch30-evaluation}
#### Benchmark Limitations {#sec-ch30-benchmark-limits}
#### From Prediction to Validation {#sec-ch30-prediction-validation}
### Connections to Molecular Design {#sec-ch30-molecular-design}
### Prioritization, Not Automation {#sec-ch30-conclusion}
### Chapter Summary

#### part_7/p7-ch31-design.qmd
## 31 Sequence Design {#sec-ch31-design}
### Chapter Overview
### Design Formalism {#sec-ch31-formalism}
##### Stop and Think
### Protein Design with Language Models {#sec-ch31-protein-design}
#### Sequence Generation from Language Model Priors {#sec-ch31-plm-generation}
#### Structure-Aware Design with Diffusion Models {#sec-ch31-structure-diffusion}
##### Conceptual Difficulty
##### Key Insight: Structure as Intermediate Representation
#### Functional Conditioning and Multi-Objective Optimization {#sec-ch31-multi-objective}
##### Knowledge Check
### Regulatory Sequence Design {#sec-ch31-regulatory-design}
#### Promoter and Enhancer Engineering {#sec-ch31-promoter-enhancer}
##### Stop and Think
#### Splicing and RNA Processing Elements {#sec-ch31-splicing-design}
### mRNA Design and Optimization {#sec-ch31-mrna-design}
#### Codon Optimization Principles {#sec-ch31-codon-optimization}
##### Key Insight: The Hidden Complexity of Synonymous Mutations
#### Stability Engineering and UTR Design {#sec-ch31-utr-design}
#### Immunogenicity Considerations {#sec-ch31-mrna-immunogenicity}
### Antibody and Vaccine Design {#sec-ch31-antibody-vaccine}
#### CDR Optimization and Humanization {#sec-ch31-cdr-optimization}
#### Vaccine Antigen Design {#sec-ch31-vaccine-design}
### Closed-Loop Design-Build-Test-Learn Cycles {#sec-ch31-dbtl}
#### Active Learning for Efficient Exploration {#sec-ch31-active-learning}
##### Stop and Think
### Practical Guidance: Choosing an Active Learning Strategy
#### High-Throughput Experimentation Integration {#sec-ch31-high-throughput}
### Validation Requirements and Failure Modes {#sec-ch31-validation}
#### Validation Hierarchy {#sec-ch31-validation-hierarchy}
#### Characteristic Failure Patterns {#sec-ch31-failure-patterns}
### Common Pitfalls
### Practical Design Constraints {#sec-ch31-practical-constraints}
#### Manufacturing and Developability {#sec-ch31-manufacturing}
#### Safety and Biosecurity Considerations {#sec-ch31-biosecurity}
### Algorithmic Search and Optimization {#sec-ch31-algorithms}
##### Knowledge Check
### Evaluating Generative Design {#sec-ch31-generative-evaluation}
#### Computational Quality Metrics {#sec-ch31-computational-metrics}
#### Functional Assessment {#sec-ch31-functional-assessment}
#### Benchmarking Generative Models {#sec-ch31-generative-benchmarks}
### From Understanding to Creating {#sec-ch31-conclusion}
### Chapter Summary

#### part_7/p7-ch32-frontiers.qmd
## 32 Frontiers and Synthesis {#sec-ch32-frontiers}
### Chapter Overview
### Open Technical Problems {#sec-ch32-technical}
##### Stop and Think
#### Scaling and Efficiency {#sec-ch32-scaling}
##### Worked Example: Scaling Laws for Variant Effect Prediction
##### Key Insight: Scaling Laws Are Not Universal
#### Context and Multi-Scale Integration {#sec-ch32-multiscale}
##### Knowledge Check
##### Case Study: APOE ε4 Across Biological Scales
#### Causality and Mechanism {#sec-ch32-causality}
##### Key Insight: Correlation Versus Causation in Foundation Models
### Emerging Directions {#sec-ch32-emerging}
#### Multimodal Integration {#sec-ch32-multimodal}
##### Stop and Think
##### Case Study: Multimodal Immunotherapy Response Prediction
### Practical Guidance: Starting with Multimodal Integration
#### Agentic and Closed-Loop Systems {#sec-ch32-agentic}
### Governance Challenge: Agentic Autonomy
#### Clinical Integration and Learning Health Systems {#sec-ch32-learning-health}
##### Case Study: Geisinger DiscovEHR Learning Health System
##### Knowledge Check
### Work Ahead {#sec-ch32-conclusion}
##### Key Insight: The Translation Gap
##### Stop and Think
### Chapter Summary


# Glossary (Core, ~245 terms)

This curated glossary is intended for an interdisciplinary audience with advanced degrees. It keeps terms that are:
- used repeatedly or central to the book’s arguments,
- easy to misinterpret across domains, or
- required for clinical translation (calibration, uncertainty, evaluation, reporting).

Domain tags:

- **[ML]** – Machine learning terms
- **[Genomics]** – Molecular biology, DNA/RNA concepts
- **[Clinical]** – Medical, diagnostic, therapeutic terms
- **[Statistics]** – Statistical methods, metrics
- **[Computation]** – Algorithms, data structures, computational concepts

## Terms (A–Z)

**A/B compartments** [Genomics]: Broad chromatin domains seen in Hi-C contact maps that separate active (A) from inactive (B) genome regions. They summarize large-scale 3D organization and often correlate with gene density and epigenomic state.

**ACMG/AMP guidelines (American College of Medical Genetics and Genomics / Association for Molecular Pathology)** [Clinical]: A widely used framework for interpreting genetic variants using standardized evidence categories and rules. In this book, model scores are often mapped to ACMG-style categories such as benign, VUS, or pathogenic to support clinical reporting.

**Actionability (clinical)** [Clinical]: The degree to which a result can change patient management, such as guiding surveillance, treatment, or family testing. Actionability is a key lens for deciding which model outputs to report.

**Adapter** [ML]: A small set of additional layers inserted into a pre-trained model so it can be specialized to a new task without updating all parameters. Useful for adapting large genomic foundation models while keeping compute and storage manageable. See also: **fine-tuning**, **LoRA**.

**ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity)** [Clinical]: A set of properties describing how a drug behaves in the body and whether it is safe. Early ADMET prediction helps reduce late-stage failures in drug discovery.

**Adverse drug reaction (ADR)** [Clinical]: An unintended and harmful response to a medication at normal doses. Predicting ADR risk can involve genetics, comedications, and clinical context.

**Analytical validity** [Clinical]: How accurately and reliably a test measures what it claims to measure (e.g., variant detection accuracy). Required before clinical validity and utility can be meaningfully assessed.

**ATAC-seq (Assay for Transposase-Accessible Chromatin using sequencing)** [Genomics]: A sequencing assay that measures chromatin accessibility by inserting adapters into open DNA with a transposase. Used to map regulatory elements and infer transcription factor activity.

**AUPRC (Area under precision–recall curve)** [Statistics]: A metric emphasizing performance on the positive class, especially informative when positives are rare. Common in variant and regulatory benchmarks with strong class imbalance.

**AUROC (Area under ROC curve)** [Statistics]: A threshold-free metric for binary classification measuring the probability a random positive is ranked above a random negative. Widely used in benchmarks but can be misleading under severe class imbalance. See also: **AUPRC**.

**Autoregressive language model (AR LM)** [ML]: A model that predicts the next token from previous tokens, learning a probability distribution over sequences. In genomics, AR objectives are used for DNA or protein sequence generation and likelihood-based scoring.

**Barcode (cell barcode)** [Genomics]: A short DNA sequence attached during library prep that labels reads from the same cell in droplet-based single-cell assays. Enables multiplexing and cell-level counting.

**Base quality score recalibration (BQSR)** [Computation]: A post-processing step (commonly in GATK pipelines) that corrects systematic biases in base quality scores reported by sequencers. Helps improve **variant calling** accuracy by better modeling sequencing error probabilities.

**Batch correction** [Statistics]: Methods that remove technical variation while preserving biological signal, often by aligning latent spaces or matching neighbors across datasets. Essential for integrating studies and avoiding spurious clusters.

**Batch effect** [Statistics]: Systematic differences introduced by processing samples in different experimental or computational batches. Batch effects can create spurious associations and must be addressed in **QC** and modeling.

**Benchmark suite** [Computation]: A curated collection of datasets, tasks, and scoring rules used to evaluate models consistently. A good suite documents data provenance, splits, metrics, and known failure modes.

**Benchmark circularity** [Statistics]: A fundamental problem in model evaluation where test labels were derived using methods that share information sources or features with evaluated models, inflating apparent performance differences. In variant effect prediction, benchmarks using SIFT/PolyPhen-derived labels can advantage methods with similar conservation features. Circularity includes label overlap (circular features), temporal issues (training on post-development classifications), and genetic overlap (variants in same genes as training data). Always verify label provenance and independence before accepting benchmark rankings. See also: **contamination (data leakage)**.

**Binary Alignment/Map (BAM)** [Computation]: A compressed binary format for storing aligned sequencing reads and their metadata. Typically produced from **FASTQ** reads after **alignment** and used as input for **variant calling**.

**Brier score** [Statistics]: A proper scoring rule that measures the mean squared error between predicted probabilities and binary outcomes. Commonly used to quantify probabilistic calibration. See also: **calibration**.

**CADD (Combined Annotation Dependent Depletion)** [ML]: A widely used variant prioritization score that integrates diverse genomic annotations to estimate how deleterious a variant is likely to be. Trained using an evolutionary proxy task contrasting simulated variants with variants observed in humans.

**Calibration** [Statistics]: The agreement between predicted probabilities (or risk scores mapped to probabilities) and observed outcome frequencies. Well-calibrated variant scores help clinicians interpret the meaning of ‘0.9 pathogenic’ as a real-world risk.

**Calibration drift** [Statistics]: Degradation of calibration over time or across sites as data distributions change. Monitoring drift is important for long-lived clinical deployments.

**Calibration-in-the-large** [Statistics]: A calibration check comparing the average predicted risk to the observed event rate. Useful for detecting systematic over- or underestimation after deployment.

**Canonical correlation analysis (CCA)** [Statistics]: A technique that finds linear projections of two datasets that are maximally correlated. Used in multi-omic and batch integration to align shared structure across modalities or batches.

**CDS (Clinical decision support)** [Clinical]: Software that provides patient-specific recommendations or alerts in clinical workflows. Genomic AI often reaches clinicians via CDS rather than standalone reports.

**Channel (CNN)** [ML]: A feature dimension in convolutional inputs/outputs (e.g., number of filters) analogous to color channels in images. In genomics, channels often represent A/C/G/T in **one-hot encoding**.

**Chinchilla-style compute-optimal training** [ML]: A scaling-law insight that, for a fixed compute budget, there is an optimal balance between model size and number of training tokens. Helps decide whether to train a bigger genomic model or train longer on more sequence data. See also: **scaling laws**.

**Chromatin accessibility** [Genomics]: How open or closed DNA is in the nucleus, influencing whether transcription factors can bind regulatory sites. Often measured by ATAC-seq or DNase-seq and modeled by sequence-to-function foundation models.

**Chromatin loop** [Genomics]: A focal 3D contact between two genomic loci, often connecting enhancers to promoters or demarcating domains. Loops can be detected in Hi-C/Micro-C and are important for regulatory interpretation.

**Cis-regulatory element (CRE)** [Genomics]: A DNA region that regulates nearby genes, such as promoters, enhancers, silencers, and insulators. Regulatory foundation models aim to predict CRE activity from sequence and context.

**Class imbalance** [Statistics]: A setting where one label is much rarer than the other. Requires appropriate metrics (AUPRC), sampling, and calibration to avoid misleading conclusions.

**CLIA (Clinical Laboratory Improvement Amendments)** [Clinical]: U.S. regulations governing laboratory testing quality. Clinical genomic pipelines often require CLIA-compliant validation and documentation.

**Clinical category mapping** [Clinical]: A procedure that converts model outputs (continuous scores) into discrete clinical labels such as benign, VUS, likely pathogenic, or pathogenic. Requires calibration and careful threshold selection.

**Clinical utility** [Clinical]: Evidence that using a test or model improves meaningful outcomes (health, decisions, cost) compared to standard care. Utility is often the hardest and most important bar for translation.

**ClinVar** [Clinical]: A public archive of variant interpretations and supporting evidence linking genetic variants to clinical phenotypes. Widely used in clinical variant interpretation and to label variants for benchmarking.

**Closed-world assumption** [Statistics]: Assuming the deployment environment matches the training/test distribution and all relevant classes are known. Often violated in genomics, motivating OOD detection and robustness tests.

**Clumping and thresholding (C+T)** [Statistics]: A simple polygenic score construction method that selects variants passing a p-value threshold and prunes correlated variants using **linkage disequilibrium**. Often used as a baseline against more complex methods like LD-aware shrinkage.

**Co-assay (paired multi-omics)** [Genomics]: A protocol that measures multiple modalities from the same cell (e.g., RNA + ATAC). Enables direct linking of regulatory state to gene expression without relying solely on computational alignment.

**Cohesin** [Genomics]: A protein complex that helps form chromatin loops and organize 3D genome structure, often working with CTCF. Cohesin dynamics influence enhancer–promoter interactions.

**Conformal prediction** [Statistics]: A method that wraps a predictive model to provide prediction sets or intervals with statistical coverage guarantees under mild assumptions. Useful for communicating uncertainty in variant interpretation.

**Confounder** [Statistics]: A variable that influences both inputs and outcomes, creating spurious associations. Confounders are common in biomedical data (batch, ancestry, site) and must be addressed in design and evaluation.

**Contamination** [Clinical]: Unintended mixing of DNA from different samples, leading to incorrect genotypes and false variants. Detected during **sample-level QC** and can severely distort downstream analyses.

**Contamination (data leakage)** [Statistics]: Accidental overlap between training and test information, such as shared individuals, highly similar sequences, or duplicated labels. Forms include temporal leakage (training on post-deployment data), gene-level leakage (variants from the same gene as training examples), and label leakage (test labels derived from training features). Leakage can yield unrealistically high benchmark performance. See also: **benchmark circularity**.

**Context length** [ML]: The maximum sequence length a model can process in one forward pass. In genomics, longer context enables modeling distal regulatory interactions and haplotype-level effects.

**Contrastive learning** [ML]: A representation-learning approach that brings related examples closer in embedding space while pushing unrelated ones apart. Used to align sequences with functional assays or to learn robust embeddings. See also: **embedding**.

**Convolutional neural network (CNN)** [ML]: A neural network that uses convolutions to learn local patterns with weight sharing and translation equivariance. In genomics, CNNs often learn sequence motifs and local regulatory signatures.

**Copy number variant (CNV)** [Genomics]: A structural change where a DNA segment is deleted or duplicated, altering the number of copies. CNVs can have large phenotypic effects but are harder to detect than SNPs in short-read data.

**Coverage (Depth)** [Genomics]: The number of sequencing reads overlapping a genomic position. Higher depth generally improves confidence in genotype calls, especially for rare variants or low-quality regions.

**Coverage (single-cell)** [Statistics]: The number of reads or unique molecules observed per cell. Low coverage increases dropout and uncertainty, affecting clustering and differential expression.

**CTCF** [Genomics]: A DNA-binding protein strongly associated with insulators and TAD boundaries. Frequently used as an anchor for interpreting 3D genome structure and loop formation.

**Curation** [Clinical]: Manual or semi-automated review of evidence to produce trusted annotations (variant classification, gene–disease validity). Curation quality strongly affects downstream AI.

**Data governance** [Clinical]: Policies and processes for data access, privacy, consent, and stewardship. Essential for sharing multi-institutional clinical genomics data responsibly.

**Decision threshold** [Clinical]: A cutoff on risk or score that triggers an action, balancing false positives and false negatives under real clinical costs. Thresholds should be validated and monitored, not chosen only on internal benchmarks.

**Degree (node degree)** [Statistics]: The number of edges connected to a node in a graph (or the sum of edge weights). Used as a basic measure of connectivity in biological networks.

**Deleteriousness score** [ML]: A model-derived score intended to rank variants by likelihood of harmful biological impact. Deleteriousness scores are used for variant prioritization but should not be interpreted as direct clinical risk. See also: **CADD**.

**Differential expression (DE)** [Statistics]: Testing whether gene expression differs between groups of cells or conditions. Requires models that handle count noise and multiple testing. See also: **false discovery rate (FDR)**.

**Digital biomarker** [Clinical]: A biomarker derived from digital sources such as wearables, images, or EHR signals. Can complement genomics for risk prediction and monitoring.

**Dilation (dilated convolution)** [ML]: A convolution variant that spaces kernel elements apart, expanding receptive field without increasing parameter count. Helps CNNs capture longer-range dependencies; see also: **receptive field**.

**Dimensionality reduction** [ML]: Methods that map high-dimensional omics data to fewer dimensions for visualization or modeling. Common choices include PCA (linear) and UMAP/t-SNE (nonlinear).

**Distribution shift** [Statistics]: A mismatch between the data distribution seen during training and the distribution at deployment. Can degrade variant scoring when moving across ancestries, assays, tissues, or sequencing technologies. See also: **out-of-distribution detection**.

**DMS (Deep mutational scanning)** [Genomics]: A high-throughput experimental technique that systematically introduces all possible single amino acid substitutions in a protein and measures their functional effects in parallel. DMS datasets provide comprehensive variant effect measurements that serve as ground truth for training and evaluating variant effect prediction models. See also: **MPRA**, **variant effect prediction**.

**DNA language model (DNA LM)** [ML]: A language model trained on DNA sequences to learn general-purpose representations or likelihoods, often using masked or autoregressive objectives. Can be adapted to tasks like regulatory prediction or variant effect scoring. See also: **tokenization**.

**Doublet** [Genomics]: An artifact where two cells are captured together and profiled as one, producing mixed expression. Doublets can form spurious clusters if not detected and filtered.

**Dropout (single-cell)** [Statistics]: Zero counts caused by limited capture efficiency and sampling, not true absence of expression. Dropout complicates interpretation and motivates models that treat zeros probabilistically.

**Drug–gene interaction** [Clinical]: A relationship where genetic variation affects drug response, efficacy, or toxicity. Central to pharmacogenomics and precision prescribing.

**Effect size (beta)** [Statistics]: A quantitative estimate of how much a variant changes a trait (for continuous traits) or the log-odds of disease (for binary traits). Effect sizes from **GWAS** are the weights used in many **polygenic scores**.

**EHR (Electronic health record)** [Clinical]: A system storing patient clinical data, including diagnoses, labs, medications, and notes. EHR integration is key for deploying risk models and monitoring real-world performance.

**Embedding** [ML]: A learned continuous vector representation of discrete inputs such as tokens, k-mers, or amino acids. Embeddings capture similarity and enable neural models to operate in continuous space; see also: **token**.

**ENCODE** [Genomics]: The Encyclopedia of DNA Elements project providing large-scale functional genomics datasets (e.g., **ChIP-seq**, accessibility) used to annotate regulatory elements. Central to building training targets and features for genomic models.

**Enhancer** [Genomics]: A regulatory DNA element that can increase transcription of a target gene when bound by transcription factors, often acting at a distance. Enhancers are frequently identified via **chromatin accessibility** and histone mark data.

**Enhancer–promoter interaction** [Genomics]: A functional relationship where an enhancer influences transcription at a promoter, often facilitated by 3D looping. Multi-scale models aim to predict these interactions from sequence and context.

**Epistemic uncertainty** [Statistics]: Uncertainty due to limited data or model knowledge, which can often be reduced with more data. Important for identifying when a model is extrapolating beyond training coverage.

**eQTL (expression quantitative trait locus)** [Genomics]: A genetic variant associated with changes in gene expression levels, often in a tissue-specific manner. eQTL maps (e.g., from **GTEx**) help link noncoding variants to candidate genes.

**Evidence code** [Clinical]: A standardized label used in ACMG/AMP-style variant interpretation (e.g., strong, moderate, supporting evidence categories). Model outputs can provide quantitative evidence that must be integrated with other clinical data.

**Evidence synthesis** [Statistics]: Combining multiple evidence sources—studies, assays, clinical reports—into a single conclusion. In variant interpretation, synthesis supports consistent classifications and updates.

**Evolutionary proxy task** [ML]: A training strategy that uses evolutionary patterns as labels, such as contrasting simulated variants with variants observed in humans, to learn a deleteriousness signal without direct clinical labels. Used by **CADD** to scale training.

**Exome sequencing (WES)** [Genomics]: Sequencing focused on protein-coding regions (exons), typically using **capture sequencing**. Provides high depth in coding regions at lower cost than **whole-genome sequencing**, but misses most regulatory DNA.

**Expected calibration error (ECE)** [Statistics]: A summary statistic of calibration that averages the gap between predicted confidence and observed accuracy across bins. Useful but sensitive to binning choices.

**External validation** [Clinical]: Testing a model on data from a different site, cohort, or time period than training. Stronger evidence of real-world generalization than internal splits.

**False negative (FN)** [Statistics]: A missed positive case (e.g., a pathogenic variant labeled benign). In clinical genetics, false negatives can delay diagnosis and appropriate care.

**False positive (FP)** [Statistics]: An incorrect positive prediction (e.g., benign variant flagged pathogenic). FPs can trigger unnecessary anxiety, testing, or treatment.

**Family segregation** [Clinical]: Evaluating whether a variant tracks with disease within a family. Strong segregation evidence can support pathogenicity classification in rare disease.

**FASTQ** [Computation]: A text file format that stores raw sequencing reads along with per-base quality scores. FASTQ is typically the starting point for **alignment** and **variant calling** pipelines.

**FDA SaMD (Software as a Medical Device)** [Clinical]: A regulatory category for software intended for medical purposes without being part of a hardware device. Some clinical AI tools may be regulated as SaMD depending on claims and use.

**Few-shot learning** [ML]: A regime where a model adapts to a new task using only a small number of labeled examples. Foundation models often improve few-shot performance via transferable representations.

**Fine-tuning** [ML]: Updating a pre-trained model’s parameters on a downstream task, usually with a smaller learning rate and fewer steps than pretraining. Common for adapting DNA/protein LMs to assays or clinical labels.

**Foundation model (FM)** [ML]: A large pre-trained model trained on broad data (often self-supervised) that can be adapted to many tasks. In genomics, FMs can operate on sequences, multi-omic profiles, or sequence-to-function mappings.

**Frameshift variant** [Genomics]: An insertion or deletion whose length is not a multiple of three, shifting the reading frame of a coding sequence. Often has large effects on protein sequence and is frequently pathogenic.

**Fully connected layer (dense layer)** [ML]: A layer that applies a learned linear transformation to all input features, often followed by a nonlinearity. Used in classifier heads or MLP blocks; see also: **MLP**.

**Functionally annotated variant** [Clinical]: A genetic variant supported by evidence from functional assays or model-based predictions. Functional annotation can help resolve VUS and prioritize variants for follow-up.

**Gated Linear Unit (GLU)** [ML]: A neural network block that multiplies one linear projection by a learned gate from another projection, improving expressiveness. Variants (e.g., SwiGLU) are common in modern transformers.

**GATK (Genome Analysis Toolkit)** [Computation]: A widely used software suite for variant discovery and genotyping from sequencing data. Includes steps like **BQSR** and **VQSR** in many classical pipelines.

**GELU** [ML]: Gaussian Error Linear Unit, an activation function that smoothly gates inputs based on a Gaussian curve. Common in transformer MLPs; see also: **activation function**.

**Gene regulatory network (GRN)** [Genomics]: A model of how transcription factors and other regulators interact to control gene expression. Learned or approximated using multi-omic data and sometimes foundation model embeddings.

**Gene set enrichment analysis (GSEA)** [Statistics]: A method that tests whether predefined gene sets (pathways) are overrepresented among up- or down-regulated genes. Helps interpret DE results in biological terms.

**Generative model** [ML]: A model that can sample new data points (e.g., sequences) from a learned distribution. DNA/protein LMs are generative and can be used for design or likelihood scoring.

**Genetic counseling** [Clinical]: Clinical support that explains genetic results, uncertainty, and implications to patients and families. Even strong models require counseling to communicate limitations and next steps.

**Gene–disease validity** [Clinical]: The strength of evidence that a gene is causally associated with a disease. High validity supports diagnosis; low validity cautions against overinterpretation of variants in that gene.

**Genome sequencing (WGS)** [Genomics]: Sequencing most of the genome, including non-coding regions. Increases diagnostic yield for some cases (SVs, regulatory variants) but adds interpretation complexity.

**Genome-wide association study (GWAS)** [Statistics]: A study design that scans the genome for variants associated with a trait by testing each variant for statistical association across many individuals. GWAS identifies correlated signals that typically require **fine-mapping** to suggest causality.

**Genomic holdout (gene/locus holdout)** [Statistics]: A split that withholds entire genes, chromosomes, or loci to test extrapolation to unseen genomic regions. Helps reduce local-sequence leakage that can inflate performance.

**Genomic inflation factor (λGC)** [Statistics]: A diagnostic statistic summarizing inflation of GWAS test statistics relative to expectation, often used to detect residual confounding or polygenicity. Interpreted alongside QQ plots and study design details.

**Genotype–phenotype correlation** [Clinical]: Relationships between genetic variants and observable traits or disease manifestations. Improves diagnosis, prognosis, and therapeutic targeting.

**GERP** [Genomics]: A conservation-based score (Genomic Evolutionary Rate Profiling) that estimates evolutionary constraint by comparing observed substitutions to an expected neutral rate. Often used as an input feature in variant prioritization models.

**GIAB (Genome in a Bottle)** [Genomics]: A consortium that provides high-confidence benchmark genomes and variant call sets for evaluating sequencing and **variant calling** accuracy. Frequently used to quantify performance of new callers like **DeepVariant**.

**Graph attention network (GAT)** [ML]: A GNN that learns attention weights over neighbors during message passing. Useful when different neighbors contribute unequally, such as in heterogeneous biological graphs.

**Graph convolutional network (GCN)** [ML]: A graph neural network that updates node features by aggregating information from neighbors. Used for tasks like gene function prediction or disease-gene prioritization.

**Graph neural network (GNN)** [ML]: A neural model that operates on graphs by iteratively passing and aggregating messages along edges. Enables learning from biological networks such as PPIs or cell–cell interaction graphs.

**gRNA (guide RNA)** [Genomics]: An RNA sequence that directs CRISPR systems to a target DNA locus. Used in functional screens and genome editing experiments that generate training data.

**GTEx (Genotype-Tissue Expression)** [Genomics]: A consortium resource linking genetic variation to gene expression across many human tissues. Central for **eQTL** discovery and interpreting regulatory variants.

**Hallucination (model output)** [ML]: Producing confident but incorrect outputs or explanations. In interpretability and reporting, hallucinations can mislead users if not constrained by evidence.

**Hardy–Weinberg equilibrium (HWE)** [Statistics]: A population genetics expectation relating genotype frequencies to allele frequencies under random mating and no selection. Deviations can indicate genotyping artifacts or population structure; often used in **sample-level QC**.

**HGMD (Human Gene Mutation Database)** [Clinical]: A curated database of published gene lesions associated with human disease. Often used historically for variant interpretation, though access and curation practices differ from open resources like **ClinVar**.

**Hi-C** [Genomics]: A chromosome conformation capture assay that measures 3D contacts between genomic loci. Provides information about long-range regulatory interactions and domain structure.

**High-throughput screening (HTS)** [Clinical]: Testing large numbers of compounds or perturbations in parallel to identify hits. ML often prioritizes what to screen and how to learn from results.

**Highly variable genes (HVGs)** [Statistics]: Genes with higher-than-expected variance across cells, often used as features for clustering and integration. HVG selection helps focus on biological signal but can miss subtle programs.

**Horizon (prediction horizon)** [Clinical]: The time window over which a model predicts an outcome, such as 5-year risk or time-to-progression. Horizon choice affects labels, censoring, and clinical utility.

**HPO (Human Phenotype Ontology)** [Clinical]: A standardized vocabulary for phenotypic abnormalities used to represent patient features in rare disease. Enables phenotype matching and computational diagnostics.

**Human-in-the-loop** [Clinical]: A deployment pattern where clinicians or curators review model outputs before action. Common for early clinical adoption to manage risk and build trust.

**Imputation (single-cell)** [Statistics]: Methods that estimate missing or dropped-out expression values. Can improve visualization but may distort variance and inflate confidence if used uncritically.

**In silico saturation mutagenesis (ISM)** [ML]: A technique that measures a model’s sensitivity by systematically mutating each position and observing changes in predictions. Used to interpret regulatory and variant models. See also: **saliency map**.

**In-context learning (ICL)** [ML]: A capability where a model adapts its behavior from examples provided in the prompt without updating weights. Often associated with large auto-regressive transformers; see also: **prompting**.

**Indel** [Genomics]: A small insertion or deletion of DNA bases relative to the reference sequence. Indels are generally harder to call than SNPs, especially in repetitive regions.

**Informed consent** [Clinical]: A process ensuring patients understand what data are collected, how results are used, and what risks exist. Consent scope can limit data use for model training and sharing.

**Interpretability** [ML]: Methods that help explain model behavior in human-understandable terms, such as motifs, salient residues, or feature attributions. Supports debugging, trust calibration, and biological insight.

**IRB (Institutional Review Board)** [Clinical]: A committee that reviews research involving human subjects for ethics and participant protections. Clinical ML studies often require IRB review even for retrospective analyses.

**Kernel (CNN filter)** [ML]: A small set of learned weights applied in a convolution to detect a specific local pattern. In genomics, kernels often learn motif-like detectors.

**Label adjudication** [Clinical]: A process where disagreements in labels (e.g., variant classifications) are resolved by expert review or consensus rules. Reduces noise and improves clinical-grade datasets.

**Label noise** [Statistics]: Errors or uncertainty in the target labels used for training and evaluation. Common in biomedical outcomes and variant labels, and can cap achievable performance.

**Layer normalization (LayerNorm)** [ML]: A normalization technique that normalizes activations within each example across features, stabilizing training in transformers. Unlike BatchNorm, it does not rely on batch statistics.

**Lead compound** [Clinical]: A chemically optimized hit with improved potency, selectivity, and drug-like properties. Leads progress into preclinical development.

**Linkage disequilibrium (LD)** [Genomics]: Non-random association of alleles at nearby loci, common in human genomes. LD can create confounding in variant benchmarks if splits do not separate correlated regions.

**Linkage disequilibrium (LD)** [Statistics]: Non-random correlation between alleles at nearby loci caused by shared ancestry and limited recombination. LD is central to interpreting **GWAS** peaks and constructing **polygenic scores**.

**Longitudinal data** [Clinical]: Measurements collected over time, such as repeated labs or outcomes. Enables risk prediction, progression modeling, and monitoring of post-deployment drift.

**LoRA (Low-Rank Adaptation)** [ML]: A parameter-efficient fine-tuning method that learns low-rank updates to weight matrices while keeping original weights frozen. Often used to adapt large foundation models on limited compute. See also: **adapter**.

**Masked language modeling (MLM)** [ML]: A self-supervised objective where random tokens are masked and the model predicts them from surrounding context. Widely used for DNA and protein foundation models to learn rich embeddings.

**Mechanistic interpretability** [ML]: Methods that aim to understand internal model computations (circuits, attention patterns, neurons) rather than only correlational feature importance. In genomics, used to connect learned features to motifs, domains, or pathways.

**Mendelian disease** [Clinical]: A disorder primarily caused by variants in a single gene with strong effects, often following dominant or recessive inheritance. Many rare diseases are Mendelian, making them targets for genomic diagnosis.

**Minimal clinically important difference (MCID)** [Clinical]: The smallest change in an outcome that patients perceive as beneficial and that would justify a change in care. Helps translate statistical improvements into meaningful utility.

**Minor allele frequency (MAF)** [Genomics]: The frequency of the less common allele at a biallelic locus. MAF thresholds are used in QC, filtering, and defining rare vs common variants.

**miRNA (microRNA)** [Genomics]: A short non-coding RNA that regulates gene expression post-transcriptionally, typically by binding target mRNAs and reducing translation or stability. Important in development and disease.

**Missense variant** [Genomics]: A single-nucleotide change that alters the amino acid at a position in a protein. Effects vary widely, making missense interpretation a central VEP challenge.

**MLOps (machine learning operations)** [Computation]: Practices for deploying, monitoring, and maintaining models in production. In clinical settings, MLOps includes audit trails, versioning, drift monitoring, and governance.

**MLP (Multi-Layer Perceptron)** [ML]: A feed-forward block composed of one or more dense layers with nonlinearities, often used inside transformer blocks. Provides token-wise feature mixing; see also: **GELU**, **GLU**.

**Model monitoring** [Clinical]: Ongoing tracking of model inputs, outputs, calibration, and outcomes after deployment. Detects drift, bias, and performance degradation in real-world use.

**Model updating** [Clinical]: Changing a deployed model using new data, recalibration, or retraining. Requires governance because updates can change clinical behavior and may trigger regulatory review.

**MOFA (Multi-Omics Factor Analysis)** [Statistics]: A factor model for jointly analyzing multiple omics modalities to identify shared and modality-specific sources of variation. Useful for interpretability in multi-omic integration.

**Monte Carlo dropout (MC dropout)** [Statistics]: Using dropout at inference time to generate multiple predictions and estimate uncertainty from their variability. A practical approximation to Bayesian uncertainty in deep nets.

**Motif** [Genomics]: A short recurring sequence pattern that is biologically meaningful, often representing a transcription factor binding preference. CNN kernels and attention heads can learn motif-like detectors; see also: **transcription factor**.

**MPRA (Massively parallel reporter assay)** [Genomics]: A high-throughput experimental technique that tests thousands of DNA sequences for regulatory activity in parallel by coupling each sequence to a unique barcode and measuring reporter expression. MPRAs provide functional labels for training regulatory sequence models and validating model predictions. See also: **DMS**, **enhancer**.

**Multiome (scRNA+scATAC)** [Genomics]: Single-cell protocols that measure transcriptome and chromatin accessibility in the same cell. Supports direct regulatory-to-expression linking and improved cell-state resolution.

**Mutual nearest neighbors (MNN)** [ML]: An integration idea that matches cells across datasets by identifying pairs that are nearest neighbors of each other in embedding space. Helps align batches or modalities while preserving local structure.

**Net benefit** [Clinical]: A decision-analytic quantity balancing true positives against false positives at a given threshold. Used in decision curve analysis to compare clinical utility.

**Net reclassification improvement (NRI)** [Statistics]: A metric assessing whether a new model more appropriately moves people across clinically meaningful risk categories compared to a baseline model. Useful when categories drive actions.

**Next-token prediction (NTP)** [ML]: A self-supervised objective where the model predicts the next token in a sequence, typically with a causal mask. Used for many generative language models and adapted for biological sequences.

**Non-coding RNA (ncRNA)** [Genomics]: RNA molecules that are not translated into proteins, including lncRNA and miRNA. ncRNAs often regulate gene expression and can be disease-relevant.

**Nonsense variant** [Genomics]: A nucleotide change that introduces a premature stop codon, truncating the protein. Often strongly disruptive and frequently classified as pathogenic, depending on context.

**Normalization (single-cell)** [Statistics]: Transformations that make expression counts comparable across cells, often correcting for library size and technical effects. Choices strongly affect downstream clustering and DE.

**Number needed to treat (NNT)** [Clinical]: How many patients must receive an intervention to prevent one adverse outcome. Helps translate risk prediction and treatment decisions into intuitive clinical impact.

**Odds ratio (OR)** [Statistics]: A measure of association for binary outcomes, comparing odds of disease between genotypes or exposure groups. Often reported for case-control GWAS; related to the **effect size** on the log-odds scale.

**OOD detection (out-of-distribution detection)** [Statistics]: Methods that identify inputs unlike the training data where predictions may be unreliable. Important for genomic models deployed across species, assays, ancestries, or sequencing pipelines. See also: **distribution shift**.

**Open set recognition** [ML]: Recognizing when an input belongs to a class not seen during training. Relevant for clinical settings where rare diseases or novel variant mechanisms appear.

**Out-of-distribution (OOD)** [Statistics]: Inputs that differ substantially from training data, where predictions may be unreliable. Evaluations often include OOD tests across sites, assays, species, or ancestries.

**Outcome definition** [Clinical]: Operationalizing a clinical endpoint from data (often EHR), such as defining ‘myocardial infarction’ by codes and labs. Poor definitions create label noise and confounding.

**Parameter-efficient fine-tuning (PEFT)** [ML]: A family of methods that adapt a pre-trained model by training only a small subset of parameters (adapters, LoRA, prompt tuning). Reduces compute and storage while preserving base model weights.

**Pathogenic** [Clinical]: A clinical classification indicating strong evidence that a variant contributes to disease. Common classification schemes also include likely pathogenic, VUS, likely benign, and benign.

**Pathogenicity score** [Clinical]: A numeric output estimating how likely a variant is to be disease-causing. For clinical utility, the score must be calibrated and validated in representative cohorts.

**Patient stratification** [Clinical]: Grouping patients into clinically meaningful subgroups, such as responders vs non-responders or high vs low risk. Stratification can improve trial design and personalized care.

**Peak (chromatin peak)** [Genomics]: A genomic region with elevated signal in an accessibility or binding assay (e.g., ATAC-seq peak). Peaks approximate regulatory elements used as features in scATAC-seq.

**Performance stratification** [Statistics]: Reporting metrics separately by subgroup (ancestry, tissue, site, gene class) rather than only overall averages. Reveals inequities and hidden failure modes.

**Pharmacodynamics (PD)** [Clinical]: What a drug does to the body, including biological effects and biomarker changes. PD helps connect target engagement to outcomes.

**Pharmacogenomics (PGx)** [Clinical]: The study of how genetic variation influences drug response and toxicity. Supports dose adjustments and drug selection to improve safety and efficacy.

**Pharmacokinetics (PK)** [Clinical]: What the body does to a drug, including absorption and clearance. PK informs dosing and is a major cause of trial failure when misestimated.

**Phenotyping (computational)** [ML]: Extracting structured phenotypes from EHR data, including diagnoses, labs, and notes. Accurate phenotyping is essential for training and evaluating clinical risk models.

**Platt scaling** [Statistics]: A calibration method that fits a logistic regression mapping from model scores to probabilities. Often used to calibrate classifiers, including variant effect predictors. See also: **temperature scaling**.

**Pointwise convolution (1×1 convolution)** [ML]: A convolution with kernel size 1 that mixes information across channels at each position. Often used after depthwise convolutions; see also: **depthwise separable convolution**.

**Polygenic risk score (PRS)** [Clinical]: A weighted sum of many genetic variants estimating genetic predisposition to a complex trait. PRS can inform screening and prevention but must be evaluated for calibration and fairness across ancestries.

**Polygenic risk score (PRS)** [Statistics]: A polygenic score for a disease outcome, usually reported as a relative risk indicator rather than a diagnosis. Often used interchangeably with **PGS**, though PRS emphasizes clinical risk contexts.

**Polygenic score (PGS)** [Statistics]: A weighted sum of many genetic variants used to predict a trait or disease risk. Weights typically come from **GWAS** effect sizes and may be adjusted for **LD** and ancestry.

**Post-market surveillance** [Clinical]: Monitoring safety and effectiveness after approval or deployment, using real-world data. Critical for identifying rare adverse events and model drift.

**Posterior inclusion probability (PIP)** [Statistics]: In Bayesian fine-mapping, the probability that a given variant is causal (or included) in the model explaining an association signal. Used to prioritize variants within a **credible set**.

**Predictive interval** [Statistics]: A range expected to contain a future observation with a specified probability. For clinical risk, intervals can communicate uncertainty beyond point estimates.

**Pretest probability** [Clinical]: The probability of disease before considering a test result, based on prevalence and clinical presentation. Determines how strongly a result shifts belief and impacts PPV/NPV.

**Principal components (genetic PCs)** [Statistics]: Low-dimensional axes summarizing genetic variation patterns across individuals. Included as covariates in **GWAS** to reduce confounding from population structure.

**Promoter** [Genomics]: A regulatory region near a gene’s transcription start site that helps initiate transcription. Promoter activity is often measured via **ChIP-seq** and **chromatin accessibility** assays.

**Prospective study** [Clinical]: A study where outcomes are measured after model deployment or enrollment, reducing certain biases in retrospective datasets. Strong evidence for clinical utility.

**Prospective validation** [Clinical]: Evaluating a model in a forward-looking setting where outcomes occur after deployment or enrollment. Stronger evidence than retrospective evaluation for clinical utility.

**Protein language model (protein LM)** [ML]: A language model trained on amino acid sequences to learn representations related to structure and function. Used for tasks like mutation effect prediction, annotation transfer, and protein design.

**Protein–protein interaction (PPI)** [Genomics]: A physical interaction between proteins, often represented as a network. PPIs provide priors for pathway analysis and graph-based prediction.

**Proxy endpoint (surrogate endpoint)** [Clinical]: A biomarker or intermediate outcome used in place of a direct clinical outcome. Can speed trials but may fail if not causally linked to patient benefit.

**Quality control (QC)** [Computation]: Procedures to detect and remove low-quality samples, reads, or variants (e.g., contamination, batch effects, low call rate). QC is essential to avoid spurious associations in **GWAS** and errors in **variant calling**.

**Quality management system (QMS)** [Clinical]: A formal system of processes and documentation to ensure consistent quality in clinical products. Many regulated clinical tools require a QMS to manage changes and audits.

**Query–Key–Value (QKV)** [ML]: The three learned projections used in attention: queries decide what to look for, keys index what is available, and values carry information to be aggregated. Core to transformer self-attention.

**Real-world evidence (RWE)** [Clinical]: Evidence derived from real-world data such as EHRs, claims, and registries. RWE supports post-market surveillance and can complement randomized trials.

**Recalibration** [Statistics]: Updating the mapping from scores to probabilities when deploying in a new setting or after drift. Often required for safe clinical use across sites.

**Reliability diagram** [Statistics]: A plot that compares predicted probabilities to observed frequencies across bins to assess calibration. In well-calibrated models, points lie near the diagonal; see also: **calibration**.

**Repetitive region** [Genomics]: DNA sequences with many similar copies (e.g., STRs, segmental duplications) that are difficult to map with short reads. Such regions increase uncertainty in **alignment** and **variant calling**.

**Representation learning** [ML]: Learning features (embeddings) from data that capture useful structure for many tasks. Self-supervised DNA/protein models are primarily representation learners.

**Residual connection (skip connection)** [ML]: A connection that adds a layer’s input to its output, easing optimization and enabling very deep networks. Standard in transformers and modern CNNs; see also: **layer normalization**.

**Risk model** [Clinical]: A model that estimates probability of a future clinical event, such as disease onset or progression. For use in care, it must be calibrated, validated externally, and tied to actions.

**rRNA (ribosomal RNA)** [Genomics]: RNA components of ribosomes that are highly abundant in cells. rRNA is often depleted in RNA-seq library prep to focus sequencing on informative transcripts.

**Safety margin (therapeutics)** [Clinical]: The gap between effective and toxic dose levels. A narrow safety margin increases the importance of accurate dosing and careful monitoring.

**Saliency map** [ML]: An interpretation method that highlights which input positions most influence a model’s prediction, typically using gradients. In genomics, saliency often aligns with motifs or critical residues. See also: **ISM**.

**SaMD change control** [Clinical]: A governance process managing software updates that might affect clinical performance. Important for maintaining compliance and safety when models are updated.

**Scaling laws** [ML]: Empirical relationships showing how model performance changes with model size, dataset size, and compute, often following power laws. Used to plan compute-optimal training and forecast returns from scaling.

**Shortcut learning** [ML]: When a model achieves high performance by exploiting spurious correlations or artifacts in the training data rather than learning the intended causal relationship. In genomics, models may learn shortcuts based on batch effects, ancestry structure, or sequence composition biases that do not generalize to new data. See also: **confounder**, **distribution shift**.

**scATAC-seq (single-cell ATAC-seq)** [Genomics]: Single-cell assay that measures chromatin accessibility per cell. Complements scRNA-seq by reflecting regulatory potential and transcription factor activity.

**scRNA-seq (single-cell RNA sequencing)** [Genomics]: Single-cell assay measuring transcript abundance per cell. Enables discovery of cell types and states and characterization of heterogeneity in tissues.

**Sequence length (context length)** [ML]: The number of tokens processed in a single model input. Longer contexts capture more information but increase compute, especially for quadratic-time attention; see also: **FlashAttention**.

**Sequence-to-function model** [ML]: A model that predicts functional outputs (e.g., accessibility, expression, binding) directly from DNA sequence, often conditioned on cell type or assay. Bridges sequence and phenotype-relevant measurements.

**SHAP (SHapley Additive exPlanations)** [ML]: A feature-attribution approach based on Shapley values that estimates each feature’s contribution to a prediction. Common for tabular clinical models; expensive at scale.

**SIFT** [Genomics]: A missense variant effect predictor that estimates whether an amino acid substitution is likely to affect protein function based on sequence conservation. Often used as a baseline comparator to learned scores.

**Single nucleotide polymorphism (SNP)** [Genomics]: A common single-base variant in a population, often used to refer to biallelic SNVs in GWAS arrays. SNPs are the most common variant type in many association studies.

**Single nucleotide variant (SNV)** [Genomics]: A change of a single nucleotide at a specific position relative to the reference genome. SNV is a general term; SNP typically implies the variant is common in a population.

**Splice variant** [Genomics]: A variant that disrupts RNA splicing signals (e.g., donor/acceptor sites), potentially causing exon skipping or intron retention. Splicing effects can be modeled by sequence-based predictors.

**State space model (SSM)** [Computation]: A sequence modeling architecture that can scale to long contexts with different compute trade-offs than attention. Sometimes explored as an alternative backbone for long-genome modeling.

**Structural variant (SV)** [Genomics]: A larger genomic alteration such as deletions, duplications, inversions, translocations, or mobile element insertions. SVs can have large functional effects but are challenging to detect and represent.

**T2T-CHM13** [Genomics]: A telomere-to-telomere human genome assembly that improves representation of previously unresolved regions. Highlights how reference improvements can change mapping and variant interpretation.

**TAD (Topologically associating domain)** [Genomics]: A genomic region with elevated internal contact frequency in 3D genome assays. TAD boundaries constrain enhancer–promoter interactions and can be affected by structural variation.

**Target engagement** [Clinical]: Evidence that a drug binds or modulates its intended biological target in vivo. Target engagement is necessary but not sufficient for clinical benefit.

**Target validation** [Clinical]: Experimental and clinical evidence confirming that modulating a target affects disease-relevant outcomes. Validation reduces attrition in drug programs.

**TF (transcription factor)** [Genomics]: A protein that binds DNA motifs to regulate gene transcription. TF activity is often inferred from accessibility and expression rather than measured directly.

**Threshold selection** [Clinical]: Choosing score cutoffs that balance false positives and false negatives given clinical costs and resources. Should be justified with decision analysis and validated externally.

**Token** [ML]: A discrete unit of input to a model, such as a character, k-mer, or subword. Tokenization choices trade off biological resolution, sequence length, and compute; see also: **vocabulary**.

**Tokenization** [ML]: The process of converting raw sequences into tokens (characters, k-mers, or learned units) for model input. In genomics, tokenization controls resolution and computational cost. See also: **k-mer**, **context length**.

**Topic model (gene program)** [ML]: A model that represents cells as mixtures of latent topics/programs, each involving a set of genes or peaks. Useful for capturing continuous variation and shared programs across cell types.

**Topologically associating domain (TAD)** [Genomics]: A 3D genomic region with higher internal contact frequency than contacts across its boundaries. TADs help constrain enhancer–promoter interactions and can influence regulatory variant effects.

**TPM (transcripts per million)** [Statistics]: A normalization unit that scales transcript counts by gene length and library size to approximate relative abundance. Used primarily in bulk RNA-seq; in single-cell, UMI counts are often preferred.

**Transcription factor (TF)** [Genomics]: A protein that binds specific DNA motifs to regulate gene expression. Many genomics models aim to predict TF binding or learn TF-like motif detectors; see also: **motif**.

**Transformer** [ML]: A neural network architecture built around self-attention and feed-forward blocks, enabling flexible modeling of long-range dependencies. Widely used for language and increasingly for biological sequences.

**Triage model** [Clinical]: A model used to prioritize cases for further review or testing rather than making final decisions. Often the safest initial deployment pattern for genomic AI.

**UMAP (Uniform Manifold Approximation and Projection)** [ML]: A nonlinear embedding method widely used for single-cell visualization that preserves neighborhood structure and can reflect some global geometry. Typically built on a kNN graph.

**UMI (Unique molecular identifier)** [Genomics]: A short random sequence attached to molecules before amplification to identify duplicates. UMIs enable more accurate molecule counting and reduce PCR bias in scRNA-seq.

**Uncertainty communication** [Clinical]: Presenting uncertainty in a way clinicians and patients can act on, such as confidence categories or calibrated probabilities. Essential when reporting VUS or borderline risk.

**Uncertainty quantification (UQ)** [Statistics]: Methods for estimating how reliable a prediction is, including epistemic uncertainty (model uncertainty) and aleatoric uncertainty (data noise). Critical for clinical deployment of variant predictors.

**VAE (variational autoencoder)** [ML]: A generative latent-variable model that learns a probabilistic latent space for high-dimensional data. VAEs underpin many single-cell tools for denoising, integration, and batch correction.

**Variance (metric variance)** [Statistics]: The variability of an evaluation metric due to finite sample size or randomness (initialization, sampling). Reporting variance or CIs prevents overclaiming small differences.

**Variant Call Format (VCF)** [Computation]: A standard text format for storing variant sites, genotypes, and associated annotations/quality fields across one or more samples. Common output of **variant calling** and common input to downstream analyses.

**Variant effect prediction (VEP)** [Clinical]: Estimating how a genetic variant changes molecular function or disease risk using computational models and evidence. Foundation models contribute by improving coverage and transfer, but still require validation and calibration.

**Variant interaction (epistasis)** [Genomics]: A non-additive effect where the impact of one variant depends on another variant. Long-context and haplotype-aware models aim to capture epistatic patterns.

**Variant of uncertain significance (VUS)** [Clinical]: A variant whose relationship to disease cannot be confidently classified as benign or pathogenic from available evidence. A major challenge for translating genomic data into clinical decisions.

**Variant prioritization** [Clinical]: The process of ranking candidate variants for follow-up or interpretation based on predicted functional impact, frequency, inheritance, and phenotype match. Tools like **CADD** provide one layer of evidence, not a final diagnosis.

**Variant quality score recalibration (VQSR)** [Computation]: A statistical modeling step (commonly in GATK pipelines) that assigns calibrated quality scores to variant calls based on multiple annotation features. Used to separate likely true variants from artifacts.

**Warmup (learning-rate warmup)** [ML]: A training schedule that gradually increases the learning rate during early steps to stabilize optimization, especially for transformers. Commonly followed by decay; see also: **optimization**.

**Weighted nearest neighbors (WNN)** [ML]: An integration approach that constructs a neighbor graph using modality-specific similarities combined with learned weights. Often used to integrate RNA with protein or ATAC signals.

**Whole-exome sequencing (WES)** [Genomics]: See **Exome sequencing (WES)**.

**Whole-genome sequencing (WGS)** [Genomics]: Sequencing of (nearly) the entire genome, including coding and noncoding regions. Provides the most comprehensive variant discovery but is more expensive and data-intensive than targeted approaches.

**Worst-group performance** [Statistics]: A robustness/fairness summary that reports the lowest performance across defined subgroups. Helps prevent good average performance from hiding harmful failures.

**Zero-shot prediction** [ML]: Making predictions on a new task or dataset without task-specific training, often by using a pre-trained model’s likelihood or embeddings. Common for mutation effect scoring from protein LMs.

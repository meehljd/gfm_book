# Academic References for Confounders and Data Leakage in Genomic Foundation Models

Genomic foundation models face systematic challenges from confounders that inflate benchmark performance and undermine clinical generalization. This reference guide provides **80+ carefully selected papers** across seven thematic areas, with full citations, relevance descriptions, and chapter section mappings. Papers are organized by methodological focus, spanning foundational works (2007–2015) and recent advances (2015–2025).

---

## 1. Batch effects and technical confounding in sequencing

Batch effects represent technical variation arising from laboratory conditions, reagent lots, and processing dates that can dominate biological signal. When correlated with outcomes, batch effects create spurious associations that foundation models readily exploit.

### Foundational correction methods

**Johnson WE, Li C, Rabinovic A.** "Adjusting batch effects in microarray expression data using empirical Bayes methods." *Biostatistics* 2007; 8(1):118–127.
*Introduces ComBat using empirical Bayes to borrow information across genes for robust batch correction even with small batches (<10 samples). The most widely cited batch correction method.*

**Leek JT, Storey JD.** "Capturing heterogeneity in gene expression studies by surrogate variable analysis." *PLoS Genetics* 2007; 3(9):e161.
*Introduces SVA to identify and adjust for unknown sources of expression heterogeneity. Critical for foundation models where latent technical factors may not be explicitly labeled.*

**Leek JT, Johnson WE, Parker HS, Jaffe AE, Storey JD.** "The sva package for removing batch effects and other unwanted variation in high-throughput experiments." *Bioinformatics* 2012; 28(6):882–883.
*Describes the comprehensive R/Bioconductor package combining SVA and ComBat functionality.*

**Zhang Y, Parmigiani G, Johnson WE.** "ComBat-seq: batch effect adjustment for RNA-seq count data." *NAR Genomics and Bioinformatics* 2020; 2(3):lqaa078.
*Extends ComBat to RNA-seq using negative binomial regression, preserving integer nature of counts.*

### Single-cell era methods

**Haghverdi L, Lun ATL, Morgan MD, Marioni JC.** "Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors." *Nature Biotechnology* 2018; 36(5):421–427.
*Introduces MNN correction that does not require predefined population compositions across batches—important when cell type compositions differ between training datasets.*

**Korsunsky I, Millard N, Fan J, et al.** "Fast, sensitive and accurate integration of single-cell data with Harmony." *Nature Methods* 2019; 16(12):1289–1296.
*Presents Harmony using iterative soft clustering and linear correction in PCA space. The leading batch correction method for single-cell atlas integration.*

**Lopez R, Regier J, Cole MB, Jordan MI, Yosef N.** "Deep generative modeling for single-cell transcriptomics." *Nature Methods* 2018; 15(12):1053–1058.
*Introduces scVI using variational autoencoders with negative binomial likelihood. Foundational deep learning approach showing how neural networks can inherently account for technical variation.*

### Reviews and impact documentation

**Leek JT, Scharpf RB, Bravo HC, et al.** "Tackling the widespread and critical impact of batch effects in high-throughput data." *Nature Reviews Genetics* 2010; 11(10):733–739.
*Essential review documenting that batch effects are ubiquitous and provides historical examples of incorrect biological conclusions from uncorrected batch effects.*

**Goh WWB, Wang W, Wong L.** "Why batch effects matter in omics data, and how to avoid them." *Trends in Biotechnology* 2017; 35(6):498–507.
*Reviews how batch effects confound clinical applications and can skew cross-validation optimistically—even small batch effects inflate performance estimates.*

**Goh WWB, Foo LWR, Wong L.** "Are batch effects still relevant in the age of big data?" *Trends in Biotechnology* 2022; 40(11):1327–1340.
*Contemporary perspective on batch effects in ML/AI contexts, including evidence that batch effects specifically inflate cross-validation accuracy.*

### Batch effects confounding ML predictions

**Soneson C, Matthes KL, Nober M, Beerenwinkel N, Robinson MD.** "Batch effect confounding leads to strong bias in performance estimates obtained by cross-validation." *PLoS ONE* 2014; 9(6):e100335.
*Critical demonstration that even moderate batch-class confounding leads to highly biased (overly optimistic) internal performance estimates that do not generalize externally.*

**Tran HTN, Ang KS, Chevrier M, et al.** "A benchmark of batch-effect correction methods for single-cell RNA sequencing data." *Genome Biology* 2020; 21(1):12.
*Comprehensive benchmark comparing 14 methods across 10 datasets. Recommends Harmony, LIGER, and Seurat 3 as top performers.*

**Yu Y, Miao Z, He J, Huang L.** "Assessing and mitigating batch effects in large-scale omics studies." *Genome Biology* 2024; 25:254.
*Most recent comprehensive framework organizing correction algorithms into four categories: location-scale, matrix-factorization, distance-neighborhood, and deep-learning methods.*

---

## 2. Domain adaptation and invariance learning

Distribution shift between training and deployment data causes foundation models to fail silently in new contexts. Domain adaptation methods learn representations that transfer across technical and biological domains.

### Foundational algorithmic methods

**Ganin Y, Ustinova E, Ajakan H, et al.** "Domain-adversarial training of neural networks." *Journal of Machine Learning Research* 2016; 17(59):1–35.
*The foundational DANN paper introducing gradient reversal for learning domain-invariant representations. Applicable to handling batch effects and technical artifacts as domain shifts.*

**Sagawa S, Koh PW, Hashimoto TB, Liang P.** "Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization." *International Conference on Learning Representations (ICLR)* 2020.
*Introduces Group DRO minimizing worst-case loss over pre-defined groups. Achieves **10–40 percentage point improvements** on minority subgroups through strong regularization.*

**Arjovsky M, Bottou L, Gulrajani I, Lopez-Paz D.** "Invariant risk minimization." *arXiv:1907.02893* 2019.
*Introduces IRM for learning representations where the optimal classifier matches across training environments. Framework for identifying causal rather than spurious correlations.*

**Ben-David S, Blitzer J, Crammer K, et al.** "A theory of learning from different domains." *Machine Learning* 2010; 79(1–2):151–175.
*Seminal theoretical paper providing formal bounds on target domain error in terms of source error, domain divergence, and joint error. Theoretical foundation for DANN.*

### Benchmarks and evaluation

**Koh PW, Sagawa S, Marklund H, et al.** "WILDS: A benchmark of in-the-wild distribution shifts." *Proceedings of the 38th International Conference on Machine Learning (ICML)* 2021; 139:5637–5664.
*Curated benchmark including tumor identification across hospitals and molecular property prediction. Demonstrates that existing methods show significant OOD performance gaps.*

### Applications to genomics and medicine

**Cochran K, Srivastava D, Shrikumar A, Kundaje A.** "Unsupervised domain adaptation methods for cross-species transfer of regulatory code signals." *Frontiers in Big Data* 2023; 6:1140663.
*Tests nine UDA methods for cross-species prediction of histone marks. Found non-adversarial methods (Minimum Class Confusion, Deep Adaptation Network) outperformed adversarial approaches for genomic predictions.*

**Mourragui S, Loog M, van de Wiel MA, Reinders MJT, Wessels LFA.** "PRECISE: A domain adaptation approach to transfer predictors of drug response from pre-clinical models to tumors." *Bioinformatics* 2019; 35(14):i510–i519.
*Domain adaptation for translating drug response predictions from cell lines to patient tumors—addresses the fundamental problem of model systems versus clinical data.*

**Sheridan DA, Thomas RS, Bundy JG, Webb SD.** "Application of transfer learning to predict drug-induced human in vivo gene expression changes using rat in vitro and in vivo data." *PLoS ONE* 2023; 18(10):e0292030.
*Applies DANN-style domain adversarial learning to cross-species transcriptomic prediction.*

**Guan H, Liu M.** "Domain adaptation for medical image analysis: A survey." *IEEE Transactions on Medical Imaging* 2022; 41(8):1949–1962.
*Comprehensive survey of domain adaptation methods in medical imaging, demonstrating successful applications of DANN-based architectures.*

### Distribution shift in healthcare

**Varoquaux G, Cheplygina V.** "Preventing dataset shift from breaking machine-learning biomarkers." *GigaScience* 2021; 10(9):giab055.
*Reviews impact of dataset shift on ML biomarkers including gene expression. Emphasizes that cross-validation scores on single datasets do not guarantee clinical generalization.*

**Ye N, Li K, Bai H, et al.** "Spurious correlations in machine learning: A survey." *arXiv:2402.12715* 2024.
*Comprehensive survey connecting spurious correlations, shortcuts, and confounders. Notes that models easily identify site-specific signatures in TCGA data.*

---

## 3. Data splitting and leakage in genomics

Improper train-test splits cause models to learn identity matching rather than biological patterns. Genomic data requires special splitting strategies that account for sequence homology, family structure, and population stratification.

### Foundational ML papers on data leakage

**Kaufman S, Rosset S, Perlich C, Stitelman O.** "Leakage in data mining: Formulation, detection, and avoidance." *ACM Transactions on Knowledge Discovery from Data* 2012; 6(4):1–21.
*The foundational paper formally defining data leakage as "introduction of information about the target which should not be legitimately available." Proposes "learn-predict separation" framework.*

**Kapoor S, Narayanan A.** "Leakage and the reproducibility crisis in machine-learning-based science." *Patterns* 2023; 4(9):100804.
*Systematic investigation finding data leakage affects at least **294 studies across 17 scientific fields**. Introduces taxonomy of eight leakage types.*

### Biological and genomic ML leakage

**Bernett J, Blumenthal DB, Grimm DG, et al.** "Guiding questions to avoid data leakage in biological machine learning applications." *Nature Methods* 2024; 21(8):1444–1453.
*Presents seven guiding questions specifically designed to prevent leakage in biological ML. Addresses complex dependencies that make leakage difficult to detect.*

**Whalen S, Schreiber J, Noble WS, Pollard KS.** "Navigating the pitfalls of applying machine learning in genomics." *Nature Reviews Genetics* 2022; 23(3):169–181.
*Essential review illustrating how genomics data structure biases performance evaluations. Covers train-test contamination, confounding, and inappropriate metrics.*

**Schreiber J, Singh R, Bilmes J, Noble WS.** "A pitfall for machine learning methods aiming to predict across cell types." *Genome Biology* 2020; 21:282.
*Demonstrates that when train and test sets share genomic loci, models memorize average activity at each locus across training cell types. Motivates chromosome holdout strategies.*

### Performance inflation from improper splits

**Rosenblatt M, Tejavibulya L, Jiang R, Noble S, Scheinost D.** "Data leakage inflates prediction performance in connectome-based machine learning models." *Nature Communications* 2024; 15(1):1829.
*Quantifies effects of five leakage forms across four datasets. Shows leakage via feature selection and repeated subjects "drastically inflates prediction performance."*

**Ellis CA, Oliver KL, Harris RV, et al.** "Inflation of polygenic risk scores caused by sample overlap and relatedness: Examples of a major risk of bias." *American Journal of Human Genetics* 2024; 111(9):1805–1809.
*Demonstrates with real-world examples that sample overlap and relatedness between GWAS and PRS cohorts is "not a minor or theoretical concern but an important potential source of bias."*

**Choi SW, Mak TSH, Hoggart CJ, O'Reilly PF.** "EraSOR: A software tool to eliminate inflation caused by sample overlap in polygenic score analyses." *GigaScience* 2023; 12:giad043.
*First comprehensive investigation quantifying the sample overlap problem. Introduces EraSOR method for correction.*

### Kinship and relatedness-aware methods

**Manichaikul A, Mychaleckyj JC, Rich SS, et al.** "Robust relationship inference in genome-wide association studies." *Bioinformatics* 2010; 26(22):2867–2873.
*Presents KING framework for relationship inference robust to population substructure. Enables kinship-aware data splitting by identifying relatives up to third-degree.*

**Roberts DR, Bahn V, Ciuti S, et al.** "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure." *Ecography* 2017; 40(8):913–929.
*Demonstrates blocking as effective strategy for estimating ML performance on data with complex dependency structures. Theoretical framework for family-aware splitting.*

**Runcie DE, Cheng H.** "Pitfalls and remedies for cross validation with multi-trait genomic prediction methods." *G3: Genes, Genomes, Genetics* 2019; 9(11):3727–3741.
*Demonstrates naive cross-validation for multi-trait prediction is "severely biased." Proposes CV2* validating against genetically related individuals not in training.*

### Chromosome holdout and locus-level splitting

**Mbatchou J, Barnard L, Backman J, et al.** "Computationally efficient whole-genome regression for quantitative and binary traits." *Nature Genetics* 2021; 53:1097–1103.
*REGENIE paper using leave-one-chromosome-out (LOCO) predictions for biobank-scale GWAS with proper separation of test variants from training predictors.*

**Robinson MR, Moser G, Zeng J, et al.** "Improving GWAS discovery and genomic prediction accuracy in biobank data." *Proceedings of the National Academy of Sciences* 2022; 119(31):e2121279119.
*Modified approach combining LOCO with first-degree relative exclusion for proper GWAS evaluation.*

**Teschendorff AE.** "Avoiding common pitfalls in machine learning omic data science." *Nature Materials* 2019; 18:422–427.
*Accessible overview of key pitfalls with practical solutions for omic data.*

---

## 4. PRS and variant effect predictor transferability

Polygenic risk scores developed in European populations show **2–5 fold accuracy decay** in non-European populations. Variant effect predictors trained on databases with European overrepresentation inherit these biases.

### Foundational PRS transferability papers

**Martin AR, Kanai M, Kamatani Y, Okada Y, Neale BM, Daly MJ.** "Clinical use of current polygenic risk scores may exacerbate health disparities." *Nature Genetics* 2019; 51(4):584–591.
*Landmark paper demonstrating PRS accuracy is several-fold higher in Europeans than other populations. Shows prediction accuracy decays with genetic distance across 17 traits in 5 continental populations.*

**Kachuri L, Chatterjee N, Hirbo J, et al.** "Principles and methods for transferring polygenic risk scores across global populations." *Nature Reviews Genetics* 2024; 25(1):8–25.
*Most current comprehensive review covering genetic and non-genetic factors affecting PRS transferability and strengths/weaknesses of construction methods.*

**Wang Y, Tsuo K, Kanai M, Neale BM, Martin AR.** "Challenges and opportunities for developing more generalizable polygenic risk scores." *Annual Review of Biomedical Data Science* 2022; 5:293–320.
*Comprehensive review from field leaders covering factors affecting generalizability (LD patterns, allele frequencies, genetic architecture).*

### Quantifying portability decay

**Ding Y, Hou K, Burch KS, et al.** "Polygenic scoring accuracy varies across the genetic ancestry continuum." *Nature* 2023; 618:774–781.
*Critical finding: PGS accuracy decreases individual-to-individual along the ancestry continuum, even within "homogeneous" groups. Shows **−0.95 correlation** between genetic distance and PGS accuracy across 84 traits.*

**Privé F, Aschard H, Carmi S, et al.** "Portability of 245 polygenic scores when derived from the UK Biobank and applied to 9 ancestry groups from the same cohort." *American Journal of Human Genetics* 2022; 109(1):12–23.
*Systematic analysis showing dramatic portability reduction: **64.7%** in South Asians, **48.6%** in East Asians, **18%** in West Africans relative to Northwestern Europeans.*

**Moreno-Grau S, Vernekar M, Lopez-Pineda A, et al.** "Polygenic risk score portability for common diseases across genetically diverse populations." *Human Genomics* 2024; 18:93.
*Recent empirical validation across 14 clinically relevant traits with multiple PRS methods.*

### Methodological improvements

**Ruan Y, Lin YF, Feng YCA, et al.** "Improving polygenic prediction in ancestrally diverse populations." *Nature Genetics* 2022; 54:573–580.
*Introduces PRS-CSx integrating GWAS from multiple populations. Demonstrates improved prediction in non-European populations.*

**Ding Y, Powe CE, Batra P, et al. (BridgePRS team).** "BridgePRS leverages shared genetic effects across ancestries to increase polygenic risk score portability." *Nature Genetics* 2024; 56:180–186.
*Novel Bayesian method achieving **61% larger average R²** than PRS-CSx for African ancestry prediction.*

### Variant effect prediction

**Cheng J, Novati G, Pan J, et al. (DeepMind).** "Accurate proteome-wide missense variant effect prediction with AlphaMissense." *Science* 2023; 381(6664):eadg7492.
*AlphaMissense adapts AlphaFold for pathogenicity prediction, trained on population frequencies. Classifies 89% of human missense variants. Training on population data may propagate ancestry biases.*

**Brandes N, Goldman G, Wang CH, Ye CJ, Ntranos V.** "Genome-wide prediction of disease variant effects with a deep protein language model." *Nature Genetics* 2023; 55:1512–1522.
*ESM1b (650M-parameter model) predicts all ~450 million possible missense variants. Models trained on evolutionary data reflect specific population histories.*

**Koenig Z, Patel SG, Engel K, et al.** "Benchmarking computational variant effect predictors by their ability to infer human traits." *Genome Biology* 2024; 25:168.
*Compared 24 VEPs in UK Biobank and diverse All of Us cohort. AlphaMissense performed consistently across populations.*

### ClinVar and database ancestry bias

**Harrison SM, Rehm HL, Chen C, et al.** "ClinVar and HGMD genomic variant classification accuracy has improved over time, as measured by implied disease burden." *Genome Medicine* 2023; 15:52.
*African ancestry individuals had significantly increased chance of being incorrectly indicated to be affected when HGMD variants used.*

**Deng N, Chen CY, Patterson C, et al.** "ClinVar database evolution and impact on potential pathogenic germline variant reporting from tumor comprehensive genomic profiling." *Cancer Research Communications* 2025; 5:1282–1290.
*Most recent (2025) evidence of persistent ancestry disparities in ClinVar affecting clinical interpretation.*

**Gudmundsson S, Singer-Berk M, Watts NA, et al.** "Variant interpretation using population databases: Lessons from gnomAD." *Human Mutation* 2022; 43:1012–1030.
*Individuals carry more novel variants if from underrepresented populations. Emphasizes need for diverse representation.*

---

## 5. EHR phenotyping and label quality

EHR-derived phenotypes used as training labels contain systematic biases from coding practices, healthcare access disparities, and temporal drift in documentation standards.

### ICD code accuracy and limitations

**O'Malley KJ, Cook KF, Price MD, et al.** "Measuring diagnoses: ICD code accuracy." *Health Services Research* 2005; 40(5 Pt 2):1620–1639.
*Foundational paper examining ICD coding errors along "patient trajectory" and "paper trail." Error rates historically ranged **20–80%** depending on disease and setting.*

**Yin Y, Shao Y, Ma P, Zeng-Treitler Q, Nelson SJ.** "Are ICD codes reliable for observational studies? Assessing coding consistency for data quality." *Journal of the American Medical Informatics Association* 2024.
*Found coding variability across time and location suggests ICD codes are insufficient for semantically reliable cohorts.*

**Wei WQ, Bastarache LA, Carroll RJ, et al.** "Evaluating phecodes, clinical classification software, and ICD-9-CM codes for phenome-wide association studies." *PLoS ONE* 2017; 12(4):e0175508.
*Compared three ICD grouping systems for PheWAS. Phecodes provided most accurate groupings but positive/negative predictive values still vary greatly.*

### Temporal drift in clinical prediction

**Davis SE, Greevy RA Jr, Lasko TA, Walsh CG, Matheny ME.** "Detection of calibration drift in clinical prediction models to inform model updating." *Journal of Biomedical Informatics* 2020; 112:103611.
*Developed calibration drift detection using adaptive sliding windows. Found significant drift from changing populations, evolving practices, and improving measurement accuracy.*

**Feng J, Phillips RV, Malenica I, et al.** "A transfer learning approach to correct the temporal performance drift of clinical prediction models." *JMIR Medical Informatics* 2022; 10(11):e38053.
*Models trained on 2010–2011 data showed significant degradation on 2012–2017 data. Transfer learning can maintain stable performance.*

### Biobank phenotyping challenges

**Schoeler T, Pingault JB, Dudbridge F, et al.** "The impact of self-report inaccuracy in the UK Biobank and its interplay with selective participation." *Nature Human Behaviour* 2025; 9:577–590.
*Found repeatability as low as **47%** for some traits. Poor phenotype ascertainment contributes to "missing heritability" problem with relative SNP heritability attenuation up to **21%**.*

**Schoeler T, Speed D, Porcu E, et al.** "Participation bias in the UK Biobank distorts genetic associations and downstream analyses." *Nature Human Behaviour* 2023; 7(7):1216–1227.
*Participation bias distorts behavioral GWAS and Mendelian randomization findings. Healthier, better-educated volunteers create systematic biases.*

**Burstein D, Hoffman G, Mathur D, et al.** "Detecting and adjusting for hidden biases due to phenotype misclassification in genome-wide association studies." *American Journal of Human Genetics* 2023; 110(2):336–352.
*Developed PheMED quantifying phenotype misclassification. Healthcare-based biobanks introduce noisier phenotypes; African American patients face higher misdiagnosis rates.*

### ML/AI bias in EHR data

**Obermeyer Z, Powers B, Vogeli C, Mullainathan S.** "Dissecting racial bias in an algorithm used to manage the health of populations." *Science* 2019; 366(6464):447–453.
*Landmark paper finding significant racial bias in widely-used healthcare algorithm. Bias arose because algorithm predicted costs rather than illness, and unequal access meant less spending on Black patients.*

**Gianfrancesco MA, Tamang S, Yazdany J, Schmajuk G.** "Potential biases in machine learning algorithms using electronic health record data." *JAMA Internal Medicine* 2018; 178(11):1544–1547.
*Concise perspective on how EHR biases (missing data in minorities, under-documentation, differential access) propagate into ML models.*

**Yang S, Varghese P, Stephenson E, Tu K, Gronsbell J.** "Machine learning approaches for electronic health records phenotyping: A methodical review." *Journal of the American Medical Informatics Association* 2023; 30(2):367–381.
*Review of 100 ML phenotyping studies found only **1 of 106 articles** evaluated algorithmic fairness.*

**Abràmoff MD, et al.** "Inherent bias in electronic health records: A scoping review of sources of bias." *npj Digital Medicine* 2024; 7:98.
*Identifies six main bias sources: clinical trial-induced, missing/incomplete labeling, implicit clinician biases, referral/admission biases, diagnosis disparities, and informative presence bias.*

---

## 6. Deep learning confounding in genomics

Genomic deep learning models are particularly vulnerable to shortcut learning through sequence homology, benchmark contamination, and evaluation on data that shares structure with training sets.

### Foundational shortcut learning

**Geirhos R, Jacobsen JH, Michaelis C, et al.** "Shortcut learning in deep neural networks." *Nature Machine Intelligence* 2020; 2(11):665–673.
*Seminal perspective defining shortcut learning—when models learn decision rules that perform well on benchmarks but fail in real-world conditions. Widely cited in biology ML papers.*

### Data leakage in genomic and protein benchmarks

**Bushuiev A, Bushuiev R, Kouba P, et al.** "Revealing data leakage in protein interaction benchmarks." *arXiv:2404.10457* 2024.
*Demonstrates conventional protein interaction benchmarks test overfitting capacity rather than generalization. Recommends 3D structural similarity-based splits.*

**[Authors].** "Detecting and avoiding homology-based data leakage in genome-trained sequence models." *bioRxiv* 2025; doi:10.1101/2025.01.22.634321.
*Shows that homology-based data leakage rewards overfitting—even maximally overfit models with no understanding of gene regulation can predict expression of similar sequences.*

**Pereira F, Nielsen H, Nielsen M, Winther O, et al.** "GraphPart: Homology partitioning for biological sequence analysis." *NAR Genomics and Bioinformatics* 2023; 5(4):lqad088.
*Proposes algorithm ensuring closely related sequences end up in same partition. Random splitting leads to homologs in different partitions, overestimating performance.*

### Foundation model benchmark contamination

**Dobson L, Tusnády GE, Tompa P.** "Regularly updated benchmark sets for statistically correct evaluations of AlphaFold applications." *Briefings in Bioinformatics* 2025; 26(2):bbaf104.
*Documents how data leakage between AlphaFold training and test sets compromises downstream applications. Provides BETA benchmarking tool with predefined datasets.*

**Rong D, Chen Z, Jia Q, et al.** "LiveProteinBench: A contamination-free benchmark for assessing models' specialized capabilities in protein science." *arXiv:2512.22257* 2024.
*Introduces benchmark using test sets exclusively from proteins validated after January 2025. Model for avoiding contamination.*

**[Multiple authors].** "Benchmarking DNA foundation models for genomic and genetic tasks." *Nature Communications* 2025; doi:10.1038/s41467-025-65823-8.
*Comprehensive benchmark noting most current evaluations are biased from fine-tuning. Evaluates using zero-shot embeddings to mitigate confounds.*

### Systematic benchmarking

**Rao R, Bhattacharya N, Thomas N, et al.** "Evaluating protein transfer learning with TAPE." *Advances in Neural Information Processing Systems* 2019; 32:9689–9701.
*Introduces Tasks Assessing Protein Embeddings with careful train/validation/test splits to test biologically relevant generalization.*

**Liu Z, Li J, Li S, et al.** "GenBench: A benchmarking suite for systematic evaluation of genomic foundation models." *arXiv:2406.01627* 2024.
*Notes current evaluations lack standardization making comparative analyses unreliable. Provides modular framework.*

**Grešová K, Martinek V, Čechák D, Šimeček P, Alexiou P.** "Genomic Benchmarks: A collection of datasets for genomic sequence classification." *BMC Genomic Data* 2023; 24:25.
*Curated benchmark datasets for genomic sequence classification.*

**Xu C, Guan J, Wu S, Xu C.** "Benchmark data contamination of large language models: A survey." *arXiv:2406.04244* 2024.
*Comprehensive survey on benchmark contamination categorizing four levels: semantic, information, and data level exposure. Framework applicable to genomic foundation models.*

**[Multiple authors].** "OmniGenBench: Automating large-scale in-silico benchmarking for genomic foundation models." *arXiv:2410.01784* 2024.
*Uses CD-HIT and BLASTN to eliminate sequences with homologs in training databases. Practical methodology for avoiding sequence leakage.*

---

## 7. Causal inference methods beyond standard approaches

Causal inference frameworks provide principled approaches for identifying confounders, distinguishing causal from spurious associations, and designing analyses robust to hidden confounding.

### Negative controls in genetic epidemiology

**Lipsitch M, Tchetgen Tchetgen E, Cohen T.** "Negative controls: A tool for detecting confounding and bias in observational studies." *Epidemiology* 2010; 21(3):383–388.
*Foundational paper introducing formal framework for negative controls, distinguishing exposure controls and outcome controls.*

**Davey Smith G.** "Negative control exposures in epidemiologic studies (Letter)." *Epidemiology* 2012; 23(2):350–351.
*Extends framework with examples of paternal exposures as negative controls for maternal intrauterine influences.*

**Sanderson E, Richardson TG, Hemani G, Davey Smith G.** "The use of negative control outcomes in Mendelian randomization to detect potential population stratification." *International Journal of Epidemiology* 2021; 50(4):1350–1361.
*Proposes using phenotypes determined before exposure/outcome as negative controls to detect population stratification in GWAS.*

**Arnold BF, Ercumen A, Benjamin-Chung J, Colford JM Jr.** "Negative controls to detect selection bias and measurement bias in epidemiologic studies." *Epidemiology* 2016; 27(5):637–641.
*Extends negative control methodology to selection bias using DAGs.*

### DAG applications in genetic studies

**Greenland S, Pearl J, Robins JM.** "Causal diagrams for epidemiologic research." *Epidemiology* 1999; 10(1):37–48.
*Landmark paper introducing formal causal diagram theory to epidemiology. Provides rigorous introduction to d-separation rules.*

**Hernán MA, Robins JM.** *Causal Inference: What If.* Boca Raton: Chapman & Hall/CRC; 2020 (2025 revision). 350 pages.
*The definitive modern textbook on causal inference (freely available at miguelhernan.org/whatifbook). Covers counterfactuals, DAGs, confounding, selection bias, and instrumental variables.*

**Suzuki E, Shinozaki T, Yamamoto E.** "Causal diagrams: Pitfalls and tips." *Journal of Epidemiology* 2020; 30(4):153–162.
*Practical guidance on using DAGs correctly, including compatibility assumptions and distinguishing confounding from effect modification.*

### Instrumental variables and Mendelian randomization

**Davey Smith G, Ebrahim S.** "'Mendelian randomization': Can genetic epidemiology contribute to understanding environmental determinants of disease?" *International Journal of Epidemiology* 2003; 32(1):1–22.
*Seminal paper formalizing Mendelian randomization concept. Explains how genetic variants serve as instrumental variables to avoid confounding and reverse causation.*

**Lawlor DA, Harbord RM, Sterne JAC, Timpson N, Davey Smith G.** "Mendelian randomization: Using genes as instruments for making causal inferences in epidemiology." *Statistics in Medicine* 2008; 27(8):1133–1163.
*Comprehensive review covering statistical foundations, assumptions for valid instruments, and sources of bias.*

**Burgess S, Small DS, Thompson SG.** "A review of instrumental variable estimators for Mendelian randomization." *Statistical Methods in Medical Research* 2017; 26(5):2333–2355.
*Technical review comparing estimation methods: ratio method, two-stage methods, likelihood-based, and semi-parametric methods.*

**Didelez V, Sheehan N.** "Mendelian randomization as an instrumental variable approach to causal inference." *Statistical Methods in Medical Research* 2007; 16(4):309–330.
*Presents formal causal inference framework using DAGs to verify IV assumptions visually.*

**Sanderson E, Glymour MM, Holmes MV, et al.** "Mendelian randomization." *Nature Reviews Methods Primers* 2022; 2:6.
*Most current authoritative reference covering estimands, identification, sensitivity analyses for pleiotropy, and extensions.*

### Population stratification as confounding

**Price AL, Zaitlen NA, Reich D, Patterson N.** "New approaches to population stratification in genome-wide association studies." *Nature Reviews Genetics* 2010; 11(7):459–463.
*Essential review of methods including EIGENSTRAT, genomic control, and linear mixed models for addressing population structure as confounding.*

---

## Summary of key citations by chapter section

| Chapter Section | Essential Papers |
|-----------------|------------------|
| **Population structure** | Price 2010; Martin 2019; Ding 2023; Sanderson 2021 |
| **Batch effects** | Johnson 2007 (ComBat); Leek 2010 review; Soneson 2014; Whalen 2022 |
| **Label bias** | Obermeyer 2019; O'Malley 2005; Burstein 2023; Schoeler 2023 |
| **Data splitting** | Kaufman 2012; Kapoor 2023; Bernett 2024; Roberts 2017 |
| **Deep learning confounding** | Geirhos 2020; Schreiber 2020; GraphPart 2023; TAPE 2019 |
| **Mitigation strategies** | Ganin 2016 (DANN); Sagawa 2020 (Group DRO); Arjovsky 2019 (IRM); Hernán 2020 |
| **PRS/VEP transferability** | Privé 2022; Kachuri 2024; AlphaMissense 2023; Harrison 2023 |

This collection provides comprehensive coverage for all major themes in confounding and data leakage in genomic foundation models, spanning foundational methods through cutting-edge 2024–2025 work.
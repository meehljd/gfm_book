# Academic Citations for Genomic Foundation Model Evaluation Methodology

Machine learning evaluation in genomics requires rigorous methodology to avoid inflated performance estimates from data leakage, population stratification, and benchmark contamination. This compilation provides **60+ foundational citations** organized by topic for a textbook chapter on evaluation methodology for genomic foundation models. Papers are prioritized by their methodological contributions rather than simple application of methods.

---

## 1. Data leakage and splitting problems in genomics ML

The most pervasive problem in genomic ML evaluation is **sequence homology causing train-test leakage**, leading to systematically overestimated performance.

### Comprehensive reviews documenting the problem

**Whalen S, Schreiber J, Noble WS, Pollard KS.** "Navigating the pitfalls of applying machine learning in genomics." *Nature Reviews Genetics* 23, 169–181 (2022).
> The premier review article on ML pitfalls in genomics. Provides comprehensive taxonomy of pitfalls including homology-based leakage, confounding, and proper evaluation methodology. Essential reading.

**Bernett J, Blumenthal DB, Grimm DG, et al.** "Guiding questions to avoid data leakage in biological machine learning applications." *Nature Methods* 21, 1444–1453 (2024).
> Presents a formal framework of **7 guiding questions** to detect and prevent data leakage. Covers homology-based leakage, circularity in benchmarks, and protein-protein interaction prediction pitfalls.

### Papers on benchmark circularity

**Grimm DG, Azencott CA, Aicheler F, et al.** "The evaluation of tools used to predict the impact of missense variants is hindered by two types of circularity." *Human Mutation* 36, 513–523 (2015).
> Seminal paper defining **two types of circularity**: Type I (variant-level train/test overlap) and Type II (gene-level leakage where predictors learn gene identity). Demonstrates dramatic performance degradation when circularity is removed.

**Park Y, Marcotte EM.** "Flaws in evaluation schemes for pair-input computational predictions." *Nature Methods* 9, 1134–1136 (2012).
> Classic paper showing standard cross-validation gives misleading results for pair-input predictions (e.g., protein-protein interactions) due to shared entities between train/test sets.

---

## 2. Homology-aware splitting methodology

### The twilight zone and sequence identity thresholds

**Rost B.** "Twilight zone of protein sequence alignments." *Protein Engineering* 12, 85–94 (1999).
> **The foundational paper** defining the "twilight zone" of sequence similarity. Establishes the **30% sequence identity threshold**: above ~30% identity, 90% of pairs are homologous; below 25%, less than 10% show homology. Over 2,000 citations.

**AlQuraishi M.** "ProteinNet: a standardized data set for machine learning of protein structure." *BMC Bioinformatics* 20, 311 (2019).
> Establishes gold-standard methodology for train/validation/test splits in protein ML. Creates validation sets at multiple identity thresholds (<10%, 20%, 30%, 40%, 50%, 70%, 90%) using MSA-based clustering to detect remote homology.

### Clustering tools for homology-reduced datasets

**Li W, Godzik A.** "CD-HIT: a fast program for clustering and comparing large sets of protein or nucleotide sequences." *Bioinformatics* 22, 1658–1659 (2006).
> The most widely used tool for sequence clustering. Foundation for homology reduction in nearly all protein ML studies. Supports 40–100% identity thresholds.

**Fu L, Niu B, Zhu Z, Wu S, Li W.** "CD-HIT: accelerated for clustering the next-generation sequencing data." *Bioinformatics* 28, 3150–3152 (2012).
> Major update adding PSI-CD-HIT for clustering below **40% identity** using BLAST.

**Steinegger M, Söding J.** "Clustering huge protein sequence sets in linear time." *Nature Communications* 9, 2542 (2018).
> Introduces MMseqs2/Linclust enabling clustering at **20–30% identity** on massive datasets—2–3 orders of magnitude faster than CD-HIT.

**Hauser M, Mayer CE, Söding J.** "kClust: fast and sensitive clustering of large protein sequence databases." *BMC Bioinformatics* 14, 248 (2013).
> Achieves sensitive clustering down to 20–30% identity. Demonstrates CD-HIT produces more corrupted clusters at <50% identity.

### Partitioning algorithms

**Teufel F, et al.** "GraphPart: homology partitioning for biological sequence analysis." *NAR Genomics and Bioinformatics* 5, lqad088 (2023).
> Introduces **homology partitioning** algorithm using graph theory to ensure no close homologs span partitions while retaining more sequences than simple homology reduction.

---

## 3. Population structure and ancestry in genomic ML

### Performance degradation across ancestry groups

**Martin AR, Kanai M, Kamatani Y, Okada Y, Neale BM, Daly MJ.** "Clinical use of current polygenic risk scores may exacerbate health disparities." *Nature Genetics* 51, 584–591 (2019).
> **The landmark paper** documenting that PRS accuracy is **4–5 fold lower** in African ancestry versus European ancestry individuals. Shows 78% of GWAS participants are European despite global population distribution. Over 2,500 citations.

**Martin AR, Gignoux CR, Walters RK, et al.** "Human demographic history impacts genetic risk prediction across diverse populations." *American Journal of Human Genetics* 100, 635–649 (2017).
> First systematic demonstration using coalescent simulations that European GWAS-derived scores are biased by genetic drift in other populations.

**Ding Y, Hou K, Burch KS, et al.** "Polygenic scoring accuracy varies across the genetic ancestry continuum." *Nature* 618, 774–781 (2023).
> Shows PRS accuracy decreases **continuously** along the genetic ancestry spectrum (Pearson r = −0.95 with genetic distance from training data), challenging discrete ancestry labeling.

**Wang Y, Guo J, Ni G, et al.** "Theoretical and empirical quantification of the accuracy of polygenic scores in ancestry divergent populations." *Nature Communications* 11, 3865 (2020).
> Provides mathematical framework predicting PRS accuracy decay with population divergence. LD and MAF differences explain 70–80% of accuracy loss in African ancestry.

### Methodological reviews and solutions

**Kachuri L, Chatterjee N, Hirbo J, et al.** "Principles and methods for transferring polygenic risk scores across global populations." *Nature Reviews Genetics* 25, 8–25 (2024).
> Comprehensive methodological review covering genetic and non-genetic factors affecting PRS transferability and emerging multi-ancestry methods.

**Ruan Y, Lin YF, Feng YCA, et al.** "Improving polygenic prediction in ancestrally diverse populations." *Nature Genetics* 54, 573–580 (2022).
> Introduces **PRS-CSx** for multi-ancestry prediction by integrating GWAS summary statistics across populations.

### Population stratification methodology

**Sul JH, Martin LS, Eskin E.** "Population structure in genetic studies: confounding factors and mixed models." *PLOS Genetics* 14, e1007309 (2018).
> Comprehensive review on how population structure confounds genetic studies. Establishes linear mixed models for controlling stratification and kinship.

**Price AL, Zaitlen NA, Reich D, Patterson N.** "New approaches to population stratification in genome-wide association studies." *Nature Reviews Genetics* 11, 459–463 (2010).
> Classic paper establishing PCA and mixed models as standard for stratification correction. Introduces genomic control λ metric.

---

## 4. Evaluation metrics for genomic tasks

### auROC versus auPRC for imbalanced data

**Saito T, Rehmsmeier M.** "The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets." *PLoS ONE* 10, e0118432 (2015).
> **The foundational bioinformatics paper** (3,300+ citations) establishing when to use precision-recall over ROC curves. Shows ROC can be deceptive with severe class imbalance common in genomics.

**Davis J, Goadrich M.** "The relationship between precision-recall and ROC curves." *Proceedings of ICML* 2006, 233–240.
> Proves mathematical isomorphism between ROC and PR space. Establishes that curve dominance in ROC space implies dominance in PR space.

**McDermott MB, Hansen LH, Zhang H, Angelotti G, Gallifant J.** "A closer look at AUROC and AUPRC under class imbalance." *NeurIPS* 2024.
> Important counterpoint showing AUPRC can introduce biases favoring higher-prevalence subpopulations. Provides nuanced guidance on metric selection.

### Clinical utility metrics

**Vickers AJ, Elkin EB.** "Decision curve analysis: a novel method for evaluating prediction models." *Medical Decision Making* 26, 565–574 (2006).
> **The original paper** introducing decision curve analysis and "net benefit" concept. Essential for assessing whether predictions do more good than harm across threshold probabilities.

**Vickers AJ, Van Calster B, Steyerberg EW.** "A simple, step-by-step guide to interpreting decision curve analysis." *Diagnostic and Prognostic Research* 3, 18 (2019).
> Authoritative interpretation guide from DCA's creators addressing widespread misunderstandings.

**Pencina MJ, D'Agostino RB Sr, Steyerberg EW.** "Extensions of net reclassification improvement calculations to measure usefulness of new biomarkers." *Statistics in Medicine* 30, 11–21 (2011).
> Extends NRI methodology to category-free (continuous) NRI and survival data.

**Leening MJG, Vedder MM, Witteman JCM, Pencina MJ, Steyerberg EW.** "Net reclassification improvement: computation, interpretation, and controversies." *Annals of Internal Medicine* 160, 122–131 (2014).
> Reviews 67 publications using NRI; identifies common errors and misinterpretations.

### Calibration assessment

**Guo C, Pleiss G, Sun Y, Weinberger KQ.** "On calibration of modern neural networks." *Proceedings of ICML* 2017, 1321–1330.
> **Essential paper** (4,400+ citations) establishing that modern deep networks are poorly calibrated. Introduces expected calibration error (ECE) and temperature scaling for recalibration.

**Van Calster B, Nieboer D, Vergouwe Y, De Cock B, Pencina MJ, Steyerberg EW.** "A calibration hierarchy for risk models was defined: from utopia to empirical data." *Journal of Clinical Epidemiology* 74, 167–176 (2016).
> Defines theoretical framework with four calibration levels: mean, weak, moderate, and strong.

**Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW.** "Calibration: the Achilles heel of predictive analytics." *BMC Medicine* 17, 230 (2019).
> From the STRATOS initiative. Argues calibration is neglected and potentially harmful when ignored.

**Huang Y, Li W, Macheret F, Gabriel RA, Ohno-Machado L.** "A tutorial on calibration measurements and calibration models for clinical prediction models." *JAMIA* 27, 621–633 (2020).
> Practical tutorial with R code for calibration measurement and recalibration methods.

---

## 5. Foundation model evaluation paradigms

### Zero-shot evaluation methodology

**Meier J, Rao R, Verkuil R, Liu J, Sercu T, Rives A.** "Language models enable zero-shot prediction of the effects of mutations on protein function." *NeurIPS* 2021, 29287–29303.
> Establishes the paradigm for **zero-shot variant effect prediction** using masked marginal scoring (log-odds ratios). Evaluated on 41 deep mutational scanning datasets.

**Rives A, Meier J, Sercu T, et al.** "Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences." *PNAS* 118, e2016239118 (2021).
> First large-scale demonstration that protein language models encode biologically meaningful representations. Introduces **linear probing methodology** for evaluating learned representations.

### Benchmark datasets for foundation models

**Rao R, Bhattacharya N, Thomas N, et al.** "Evaluating protein transfer learning with TAPE." *NeurIPS* 2019, 9689–9701.
> Established the first comprehensive **multi-task benchmark** for protein representation learning (analogous to GLUE for NLP). Five biologically relevant tasks with standardized splits.

**Notin P, Kollasch AW, Ritter D, et al.** "ProteinGym: large-scale benchmarks for protein fitness prediction and design." *NeurIPS Datasets and Benchmarks* 2023.
> Standard large-scale benchmark with **217+ deep mutational scanning assays** (~2.7M variants). Primary resource for zero-shot protein model evaluation.

**Ji Y, Zhou Z, Liu H, Davuluri RV.** "DNABERT: pre-trained bidirectional encoder representations from transformers model for DNA-language in genome." *Bioinformatics* 37, 2112–2120 (2021).
> First foundational DNA language model establishing transfer learning evaluation paradigm for genomics.

**Zhou Z, Ji Y, Li W, Dutta P, Davuluri R, Liu H.** "DNABERT-2: efficient foundation model and benchmark for multi-species genome." *ICLR* 2024.
> Introduces **GUE (Genome Understanding Evaluation)** benchmark: 36 datasets across 9 tasks with standardized preprocessing.

**Dalla-Torre H, Gonzalez L, Mendoza-Revilla J, et al.** "The Nucleotide Transformer: building and evaluating robust foundation models for human genomics." *Nature Methods* 2024.
> Systematic methodology for DNA foundation model evaluation including probing, fine-tuning, and attention analysis across 18 genomic tasks.

### Data efficiency and transfer learning

**Brandes N, Goldman G, Wang CH, Ye CJ, Ntranos V.** "Cross-protein transfer learning substantially improves disease variant prediction." *Genome Biology* 24, 182 (2023).
> Demonstrates transfer learning from only 5 proteins generalizes to proteome-wide variant prediction using leave-protein-out cross-validation.

**Xu Q, Zhang C, Wu Y, Li M, Zitnik M.** "Enhancing efficiency of protein language models with minimal wet-lab data through few-shot learning." *Nature Communications* 15, 49798-6 (2024).
> Establishes methodology for evaluating few-shot learning with **data efficiency curves** across training sizes (20, 40, 60, 80, 100 samples).

---

## 6. Statistical methods for model comparison

### Bootstrap and confidence intervals

**Efron B, Tibshirani RJ.** *An Introduction to the Bootstrap.* Chapman & Hall, 1993.
> **Definitive reference** for bootstrap methodology. Establishes BCa (bias-corrected and accelerated) confidence intervals applicable to any ML metric.

**LeDell E, Petersen M, van der Laan M.** "Computationally efficient confidence intervals for cross-validated area under the ROC curve estimates." *Electronic Journal of Statistics* 9, 1583–1607 (2015).
> Develops influence curve-based confidence intervals for cross-validated AUC. Provides cvAUC R package.

**DeLong ER, DeLong DM, Clarke-Pearson DL.** "Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach." *Biometrics* 44, 837–845 (1988).
> Standard method for comparing AUCs from correlated ROC curves using U-statistic theory.

**Hanley JA, McNeil BJ.** "The meaning and use of the area under a receiver operating characteristic (ROC) curve." *Radiology* 143, 29–36 (1982).
> Establishes AUC interpretation as probability of correct ranking (Wilcoxon equivalence).

### Cross-validation variance estimation

**Nadeau C, Bengio Y.** "Inference for the generalization error." *Machine Learning* 52, 239–281 (2003).
> **Seminal paper** showing standard tests underestimate variance due to training set overlap. Proposes corrected paired t-test and "5×2cv" methodology.

**Grandvalet Y, Bengio Y.** "No unbiased estimator of the variance of K-fold cross-validation." *JMLR* 5, 1089–1105 (2004).
> Proves theoretical impossibility of unbiased variance estimation for K-fold CV.

### Multiple classifier comparison

**Demšar J.** "Statistical comparisons of classifiers over multiple data sets." *JMLR* 7, 1–30 (2006).
> **The standard reference** (10,000+ citations) for comparing ML algorithms across multiple datasets. Introduces critical difference (CD) diagrams. Recommends Friedman test + Nemenyi post-hoc tests.

**García S, Herrera F.** "An extension on 'Statistical comparisons of classifiers over multiple data sets' for all pairwise comparisons." *JMLR* 9, 2677–2694 (2008).
> Extends Demšar's framework with more powerful post-hoc procedures (Holm, Hochberg, Hommel).

**Benjamini Y, Hochberg Y.** "Controlling the false discovery rate: a practical and powerful approach to multiple testing." *JRSS-B* 57, 289–300 (1995).
> Introduces **FDR control** as alternative to Bonferroni. Standard in genomics benchmark evaluation.

### Bayesian approaches and effect sizes

**Benavoli A, Corani G, Demšar J, Zaffalon M.** "Time for a change: a tutorial for comparing multiple classifiers through Bayesian analysis." *JMLR* 18, 1–36 (2017).
> Proposes Bayesian alternatives to NHST. Introduces **ROPE** (Region of Practical Equivalence) for practical significance testing.

**Cohen J.** *Statistical Power Analysis for the Behavioral Sciences*, 2nd ed. Lawrence Erlbaum, 1988.
> Establishes effect size conventions (small=0.2, medium=0.5, large=0.8 for Cohen's d). Foundation for practical significance assessment.

---

## 7. Benchmark design and temporal evaluation

### Temporal split methodology

**Radivojac P, Clark WT, Oron TR, et al.** "A large-scale evaluation of computational protein function prediction." *Nature Methods* 10, 221–227 (2013).
> Established **time-delayed evaluation methodology** for CAFA challenges. Predictions submitted before deadline, evaluated against annotations accumulating afterward.

**Zhou N, Jiang Y, Bergquist TR, et al.** "The CAFA challenge reports improved protein function prediction and new functional annotations for hundreds of genes through experimental screens." *Genome Biology* 20, 244 (2019).
> Extends CAFA temporal evaluation to include "no-knowledge" and "limited-knowledge" benchmark categories.

**Kryshtafovych A, Schwede T, Topf M, Fidelis K, Moult J.** "Critical assessment of methods of protein structure prediction (CASP)—Round XIV." *Proteins* 89, 1607–1617 (2021).
> Documents CASP's **blind prediction methodology**—gold standard since 1994 for avoiding temporal leakage.

### Benchmark contamination detection

**Deng C, Zhao Y, Tang X, Gerstein M, Cohan A.** "Investigating data contamination in modern benchmarks for large language models." *NAACL* 2024, 8706–8719.
> Introduces **Testset Slot Guessing** method for detecting benchmark contamination in black-box models. Applicable to genomic foundation models.

**Shi W, Ajith A, Xia M, et al.** "Detecting pretraining data from large language models." *ICLR* 2024.
> Develops **Min-K% Prob** method for membership inference without knowing pretraining corpus.

### Label circularity in variant pathogenicity

**Grimm DG, Azencott CA, Aicheler F, et al.** "The evaluation of tools used to predict the impact of missense variants is hindered by two types of circularity." *Human Mutation* 36, 513–523 (2015).
> **The seminal paper** defining Type 1 (variant-level) and Type 2 (gene-level) circularity in variant effect prediction.

**Cheng J, Novati G, Pan J, et al.** "Accurate proteome-wide missense variant effect prediction with AlphaMissense." *Science* 381, eadg7492 (2023).
> Explicitly addresses circularity by **not training on ClinVar**—uses population frequencies as weak labels. Demonstrates unsupervised approaches can beat supervised methods confounded by circularity.

**Livesey BJ, Marsh JA.** "Using deep mutational scanning to benchmark variant effect predictors and identify disease mutations." *Molecular Systems Biology* 16, e9380 (2020).
> Uses **DMS data as circularity-free benchmark**. Found unsupervised methods outperformed supervised methods attributed to circularity confounding.

**Livesey BJ, Marsh JA.** "Variant effect predictor correlation with functional assays is reflective of clinical classification performance." *Genome Biology* 26, 54 (2025).
> Most comprehensive VEP benchmark (97 predictors, 36 proteins). Classifies methods into three circularity risk tiers.

**Wu Y, Li R, Sun S, et al.** "Improved pathogenicity prediction for rare human missense variants." *American Journal of Human Genetics* 108, 1891–1906 (2021).
> VARITY predictor designed to **explicitly minimize circularity** by excluding features informed by variant annotation.

**Scott HA, et al.** "ClinVar and HGMD genomic variant classification accuracy has improved over time, as measured by implied disease burden." *Genome Medicine* 15, 51 (2023).
> Uses ClinVar temporal archives to track label quality evolution—methodology for understanding the bootstrap problem in variant interpretation.

---

## Quick reference by methodology type

| Methodology | Key Citation |
|-------------|--------------|
| Sequence homology leakage | Whalen et al. 2022, Nat Rev Genet |
| Twilight zone threshold | Rost 1999, Protein Eng |
| Clustering tools | Li & Godzik 2006 (CD-HIT), Steinegger & Söding 2018 (MMseqs2) |
| Ancestry bias in PRS | Martin et al. 2019, Nat Genet |
| auROC vs auPRC | Saito & Rehmsmeier 2015, PLoS ONE |
| Decision curve analysis | Vickers & Elkin 2006, Med Decis Making |
| Neural network calibration | Guo et al. 2017, ICML |
| Zero-shot protein LM evaluation | Meier et al. 2021, NeurIPS |
| Protein benchmark | Notin et al. 2023 (ProteinGym), Rao et al. 2019 (TAPE) |
| DNA benchmark | Zhou et al. 2024 (GUE/DNABERT-2) |
| CV variance estimation | Nadeau & Bengio 2003, Machine Learning |
| Multiple classifier comparison | Demšar 2006, JMLR |
| FDR correction | Benjamini & Hochberg 1995, JRSS-B |
| Temporal evaluation | Radivojac et al. 2013 (CAFA), CASP series |
| Label circularity | Grimm et al. 2015, Human Mutation |

This compilation provides foundational references establishing best practices rather than simply applying methods, making them suitable for citation in a methodological textbook chapter.
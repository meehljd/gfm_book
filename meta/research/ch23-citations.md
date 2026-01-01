# Foundational and Applied Papers for Uncertainty Quantification in Genomic Foundation Models

This compilation provides **verified academic citations** organized by the chapter's topical priorities, covering foundational machine learning methods through genomic-specific applications.

---

## Priority 1: Papers for explicit [Citation Needed] tags

### Evidential deep learning

**Sensoy M, Kaplan L, Kandemir M.** "Evidential Deep Learning to Quantify Classification Uncertainty." *Advances in Neural Information Processing Systems* 31 (NeurIPS 2018), pp. 3179-3193, 2018. arXiv: 1806.01768

*The seminal paper introducing evidential deep learning for classification, placing a Dirichlet distribution on class probabilities using subjective logic theory. Enables single-forward-pass uncertainty quantification without sampling.*

**Amini A, Schwarting W, Soleimany A, Rus D.** "Deep Evidential Regression." *Advances in Neural Information Processing Systems* 33 (NeurIPS 2020), pp. 14927-14937, 2020. arXiv: 1910.02600

*Extends EDL to regression using Normal Inverse-Gamma priors, enabling both aleatoric and epistemic uncertainty estimation without OOD training data.*

#### Critical papers questioning EDL reliability

**Bengs V, Hüllermeier E, Waegeman W.** "Pitfalls of Epistemic Uncertainty Quantification through Loss Minimisation." *Advances in Neural Information Processing Systems* 35 (NeurIPS 2022), pp. 29205-29216, 2022. arXiv: 2203.06102

*Shows loss minimization does not incentivize faithful epistemic uncertainty representation—a fundamental theoretical flaw where uncertainty may not vanish even with infinite samples.*

**Bengs V, Hüllermeier E, Waegeman W.** "On Second-Order Scoring Rules for Epistemic Uncertainty Quantification." *Proceedings of ICML 2023*, PMLR vol. 202, pp. 2078-2091, 2023.

*Demonstrates no proper scoring rules exist for second-order learners, undermining the theoretical foundations of EDL training objectives.*

**Jürgens M, Meinert N, Bengs V, Hüllermeier E, Waegeman W.** "Is Epistemic Uncertainty Faithfully Represented by Evidential Deep Learning Methods?" *Proceedings of ICML 2024*, PMLR vol. 235, pp. 22624-22642, 2024. arXiv: 2402.09056

*Comprehensive analysis showing EDL epistemic uncertainty is only relatively interpretable and does not faithfully decrease with increasing data.*

**Shen M, Ryu JJ, Ghosh S, Bu Y, Sattigeri P, Das S, Wornell GW.** "Are Uncertainty Quantification Capabilities of Evidential Deep Learning a Mirage?" *Advances in Neural Information Processing Systems* 37 (NeurIPS 2024), pp. 107830-107864, 2024. arXiv: 2402.06160

*Argues EDL methods are better understood as energy-based OOD detectors rather than true uncertainty quantifiers, producing spurious epistemic uncertainty that never vanishes.*

### Likelihood-based OOD detection failures

**Nalisnick E, Matsukawa A, Teh YW, Gorur D, Lakshminarayanan B.** "Do Deep Generative Models Know What They Don't Know?" *International Conference on Learning Representations (ICLR 2019)*, 2019. arXiv: 1810.09136

*Landmark paper demonstrating deep generative models (VAEs, flows, PixelCNNs) assign higher likelihood to OOD data than training data—e.g., CIFAR-10-trained models give higher likelihood to SVHN images. Essential citation for the known failure of likelihood-based OOD detection.*

**Nalisnick E, Matsukawa A, Teh YW, Lakshminarayanan B.** "Detecting Out-of-Distribution Inputs to Deep Generative Models Using Typicality." arXiv: 1906.02994, 2019.

*Explains the likelihood paradox via mismatch between model's typical set and high-density regions; proposes typicality-based OOD detection.*

**Ren J, Liu PJ, Fertig E, Snoek J, Poplin R, DePristo MA, Dillon JV, Lakshminarayanan B.** "Likelihood Ratios for Out-of-Distribution Detection." *Advances in Neural Information Processing Systems* 32 (NeurIPS 2019), 2019. arXiv: 1906.02845

*Proposes likelihood ratio method using background models. Introduces a **genomics OOD benchmark** showing raw likelihood achieves only 0.626 AUROC on genomic sequences—directly relevant to genomic foundation models.*

---

## Priority 2: Foundational ML papers for methods

### Deep ensembles

**Lakshminarayanan B, Pritzel A, Blundell C.** "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles." *Advances in Neural Information Processing Systems* 30 (NeurIPS 2017), pp. 6402-6413, 2017. DOI: 10.5555/3295222.3295387. arXiv: 1612.01474

*The seminal paper introducing deep ensembles as a practical alternative to Bayesian neural networks. Combines multiple randomly-initialized networks using proper scoring rules for training, achieving state-of-the-art uncertainty quantification.*

### Conformal prediction foundations

**Vovk V, Gammerman A, Shafer G.** *Algorithmic Learning in a Random World*. Springer, 2005 (Second Edition: 2022). DOI: 10.1007/b106715

*The definitive theoretical foundation for conformal prediction, establishing validity guarantees under exchangeability assumptions.*

**Shafer G, Vovk V.** "A Tutorial on Conformal Prediction." *Journal of Machine Learning Research* 9(12):371-421, 2008. arXiv: 0706.3188

*Comprehensive self-contained tutorial with theoretical foundations and numerical examples explaining nonconformity measures and online validity.*

**Angelopoulos AN, Bates S.** "Conformal Prediction: A Gentle Introduction." *Foundations and Trends® in Machine Learning*, Vol. 16, No. 4, pp. 494-591, 2023. DOI: 10.1561/2200000101. arXiv: 2107.07511

*The most accessible modern tutorial with Python code. Covers conformalized quantile regression, distribution shift handling, and practical extensions for deep learning—essential for practitioners.*

### Heteroscedastic neural networks

**Nix DA, Weigend AS.** "Estimating the Mean and Variance of the Target Probability Distribution." *Proceedings of IEEE International Conference on Neural Networks (ICNN'94)*, Vol. 1, pp. 55-60, 1994. DOI: 10.1109/ICNN.1994.374138

*Foundational paper on Mean Variance Estimation (MVE) networks that output input-dependent variance estimates trained via negative log-likelihood—the core method for heteroscedastic aleatoric uncertainty.*

**Kendall A, Gal Y.** "What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?" *Advances in Neural Information Processing Systems* 30 (NeurIPS 2017), pp. 5574-5584, 2017. DOI: 10.5555/3295222.3295309. arXiv: 1703.04977

*Highly influential paper unifying aleatoric and epistemic uncertainty modeling. Clearly distinguishes aleatoric uncertainty (irreducible observation noise) from epistemic uncertainty (reducible model uncertainty) with practical loss functions.*

### Calibration metrics and methods

**Naeini MP, Cooper GF, Hauskrecht M.** "Obtaining Well Calibrated Probabilities Using Bayesian Binning." *Proceedings of AAAI 2015*, pp. 2901-2907, 2015. DOI: 10.1609/aaai.v29i1.9602

*Formalizes Expected Calibration Error (ECE), the most widely-used calibration metric measuring weighted average discrepancy between predicted confidence and actual accuracy.*

**DeGroot MH, Fienberg SE.** "The Comparison and Evaluation of Forecasters." *Journal of the Royal Statistical Society: Series D (The Statistician)*, 32(1-2):12-22, 1983. DOI: 10.2307/2987588

*Foundational paper introducing reliability diagrams (calibration curves) for visualizing forecast calibration and formalizing calibration/refinement concepts.*

**Guo C, Pleiss G, Sun Y, Weinberger KQ.** "On Calibration of Modern Neural Networks." *Proceedings of ICML 2017*, PMLR Vol. 70, pp. 1321-1330, 2017. arXiv: 1706.04599

*Demonstrates modern DNNs are poorly calibrated despite high accuracy. Introduces temperature scaling—a single-parameter post-hoc calibration method dividing logits by learned temperature before softmax.*

**Platt JC.** "Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods." *Advances in Large Margin Classifiers*, MIT Press, pp. 61-74, 1999.

*Original paper on Platt scaling, fitting a sigmoid function to classifier outputs for post-hoc probability calibration—remains one of the most widely-used parametric methods.*

**Brier GW.** "Verification of Forecasts Expressed in Terms of Probability." *Monthly Weather Review*, 78(1):1-3, 1950. DOI: 10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2

*Original definition of the Brier score, a strictly proper scoring rule measuring mean squared error between predicted probabilities and outcomes, capturing both calibration and discrimination.*

**Niculescu-Mizil A, Caruana R.** "Predicting Good Probabilities with Supervised Learning." *Proceedings of ICML 2005*, pp. 625-632, 2005. DOI: 10.1145/1102351.1102430

*Comprehensive comparison of Platt scaling and isotonic regression across classifiers. Shows isotonic regression (non-parametric monotonic step function) outperforms Platt scaling with sufficient calibration data (>1000 samples).*

---

## Priority 3: Clinical and genomics standards

### ACMG-AMP variant classification

**Richards S, Aziz N, Bale S, Bick D, Das S, Gastier-Foster J, Grody WW, Hegde M, Lyon E, Spector E, Voelkerding K, Rehm HL; ACMG Laboratory Quality Assurance Committee.** "Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology." *Genetics in Medicine*, 17(5):405-424, 2015. DOI: 10.1038/gim.2015.30

*The foundational paper establishing the 5-tier variant classification system (pathogenic, likely pathogenic, VUS, likely benign, benign) with 28 evidence criteria. Defines pathogenic as ~99% certainty and likely pathogenic as ~90% certainty.*

**Tavtigian SV, Greenblatt MS, Harrison SM, Nussbaum RL, Prabhu SA, Boucher KM, Biesecker LG; ClinGen Sequence Variant Interpretation Working Group.** "Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework." *Genetics in Medicine*, 20(9):1054-1060, 2018. DOI: 10.1038/gim.2017.210

*Provides mathematical foundation for ACMG/AMP guidelines by translating qualitative criteria into quantitative Bayesian probabilities—essential for calibrating computational tools to clinical standards.*

**Tavtigian SV, Harrison SM, Boucher KM, Biesecker LG.** "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines." *Human Mutation*, 41(10):1734-1737, 2020. DOI: 10.1002/humu.24088

*Abstracts ACMG/AMP evidence strength into an additive point system (Supporting=1, Moderate=2, Strong=4, Very Strong=8 points) enabling practical calibration.*

### ClinGen framework

**Rehm HL, Berg JS, Brooks LD, Bustamante CD, Evans JP, Landrum MJ, Ledbetter DH, Maglott DR, Martin CL, Nussbaum RL, Plon SE, Ramos EM, Sherry ST, Watson MS.** "ClinGen—the Clinical Genome Resource." *New England Journal of Medicine*, 372(23):2235-2242, 2015. DOI: 10.1056/NEJMsr1406261

*Establishes ClinGen as the NIH-funded consortium for defining clinical relevance of genes and variants through standardized curation via ClinVar.*

**Brnich SE, Abou Tayoun AN, Couch FJ, Cutting GR, Greenblatt MS, et al.; ClinGen SVI Working Group.** "Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework." *Genome Medicine*, 12:3, 2019. DOI: 10.1186/s13073-019-0690-2

*Structured four-step framework for assessing functional assay evidence strength in variant interpretation.*

### Risk communication and uncertainty

**Han PKJ, Umstead KL, Bernhardt BA, Green RC, Joffe S, Koenig B, Krantz I, Waterston LB, Biesecker LG, Biesecker BB.** "A taxonomy of medical uncertainties in clinical genome sequencing." *Genetics in Medicine*, 19(8):918-925, 2017. DOI: 10.1038/gim.2016.212

*Establishes a three-dimensional taxonomy (source, issue, locus) for classifying genomic testing uncertainties, distinguishing probability, ambiguity, and complexity as uncertainty sources.*

**Hoffman-Andrews L.** "The challenge of genetic variants of uncertain clinical significance: A narrative review." *Annals of Internal Medicine*, 2023.

*Reviews that ~20% of genetic tests identify VUS, only 7.7% are resolved over 10 years, and VUS results can lead to unnecessary procedures and decisional regret.*

**Makhnoon S, Shirts BH, Bowen DJ.** "Patients' perspectives of variants of uncertain significance and strategies for uncertainty management." *Genetics in Medicine*, 21(2):415-421, 2019. DOI: 10.1038/s41436-018-0058-2

*First structured analysis using Han's taxonomy to understand patient VUS experiences, finding between-provider discordance is a major uncertainty contributor.*

---

## Priority 4: Genomic foundation model uncertainty

### AlphaMissense

**Cheng J, Novati G, Pan J, Bycroft C, Žemgulytė A, Applebaum T, Pritzel A, Wong LH, Zielinski M, Sargeant T, Schneider RG, Senior AW, Jumper J, Hassabis D, Kohli P, Avsec Ž.** "Accurate proteome-wide missense variant effect prediction with AlphaMissense." *Science*, 381(6664):eadg7492, 2023. DOI: 10.1126/science.adg7492

*AlphaFold-derived model classifying 89% of human missense variants as likely benign or likely pathogenic, fundamentally changing variant effect prediction capabilities.*

### ESM protein language models

**Rives A, Meier J, Sercu T, Goyal S, Lin Z, Liu J, Guo D, Ott M, Zitnick CL, Ma J, Fergus R.** "Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences." *PNAS*, 118(15):e2016239118, 2021. DOI: 10.1073/pnas.2016239118

*Original ESM-1b paper demonstrating protein language models learn structure/function without explicit supervision from evolutionary sequences.*

**Lin Z, Akin H, Rao R, Hie B, Zhu Z, Lu W, dos Santos Costa A, Fazel-Zarandi M, Sercu T, Candido S, Rives A.** "Evolutionary-scale prediction of atomic-level protein structure with a language model." *Science*, 379(6637):1123-1130, 2023. DOI: 10.1126/science.ade2574

*Introduces ESM-2 (up to 15B parameters) and ESMFold, demonstrating structure emerges from language model representations alone.*

**Brandes N, Goldman G, Wang CH, Ye CJ, Ntranos V.** "Genome-wide prediction of disease variant effects with a deep protein language model." *Nature Genetics*, 55:1512-1522, 2023. DOI: 10.1038/s41588-023-01465-0

*Uses ESM-1b to predict all ~450 million possible human missense variants. Shows well-calibrated predictions with consistent distributions across pathogenic/benign classes—directly relevant to calibration discussions.*

### Enformer and expression models

**Avsec Ž, Agarwal V, Visentin D, Ledsam JR, Grabska-Barwinska A, Taylor KR, Assael Y, Jumper J, Kohli P, Kelley DR.** "Effective gene expression prediction from sequence by integrating long-range interactions." *Nature Methods*, 18:1196-1203, 2021. DOI: 10.1038/s41592-021-01252-x

*Introduces Enformer, a transformer predicting gene expression from 200kb DNA sequences, improving variant effect prediction on eQTLs and learning enhancer-promoter interactions.*

**Karollus A, Mayr T, Gagneur J.** "Current sequence-based models capture gene expression determinants in promoters but mostly ignore distal enhancers." *Genome Biology*, 24:56, 2023. DOI: 10.1186/s13059-023-02899-9

*Benchmarks Enformer limitations—important for understanding model uncertainty and calibration issues in regulatory genomics.*

### Calibration of computational variant effect predictors (KEY PAPERS)

**Pejaver V, Byrne AB, Feng BJ, Pagel KA, Mooney SD, Karchin R, O'Donnell-Luria A, Harrison SM, Tavtigian SV, Greenblatt MS, Biesecker LG, Radivojac P, Brenner SE; ClinGen SVI Working Group.** "Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria." *American Journal of Human Genetics*, 109(12):2163-2177, 2022. DOI: 10.1016/j.ajhg.2022.10.013

*Establishes framework for calibrating VEPs to ACMG/AMP clinical guidelines using local posterior probability. Calibrates 13 tools (REVEL, CADD, PrimateAI)—foundational for clinical variant interpretation.*

**Bergquist T, Stenton SL, Nadeau EAW, Byrne AB, et al.** "Calibration of additional computational tools expands ClinGen recommendation options for variant classification with PP3/BP4 criteria." *Genetics in Medicine*, 27(6):101402, 2025. DOI: 10.1016/j.gim.2025.101402

*Extends calibration to AlphaMissense, ESM-1b, and VARITY. All three achieve Strong evidence level for pathogenicity prediction—critical for using foundation models clinically.*

### Other variant effect predictors

**Frazer J, Notin P, Dias M, Gomez A, Min JK, Brock K, Gal Y, Marks DS.** "Disease variant prediction with deep generative models of evolutionary data." *Nature*, 599:91-95, 2021. DOI: 10.1038/s41586-021-04043-8

*Introduces EVE (Evolutionary model of Variant Effect), an unsupervised VAE predicting pathogenicity for 36M+ variants without clinical labels—performs on par with high-throughput experiments.*

**Kircher M, Witten DM, Jain P, O'Roak BJ, Cooper GM, Shendure J.** "A general framework for estimating the relative pathogenicity of human genetic variants." *Nature Genetics*, 46(3):310-315, 2014. DOI: 10.1038/ng.2892

*Original CADD paper establishing integrative machine learning framework for genome-wide variant deleteriousness scoring.*

**Livesey BJ, Marsh JA.** "Updated benchmarking of variant effect predictors using deep mutational scanning." *Molecular Systems Biology*, 19(8):e11474, 2023. DOI: 10.15252/msb.202211474

*Benchmark using 26 human proteins and 55 VEPs. ESM-1v ranks first overall; addresses data circularity issues in VEP evaluation.*

### Population-specific performance disparities

**Martin AR, Kanai M, Kamatani Y, Okada Y, Neale BM, Daly MJ.** "Clinical use of current polygenic risk scores may exacerbate health disparities." *Nature Genetics*, 51:584-591, 2019. DOI: 10.1038/s41588-019-0379-x

*Demonstrates PRS from European GWAS have lower predictive accuracy in non-European populations, warning of potential to worsen health disparities—essential for population-specific uncertainty discussions.*

**Popejoy AB, Fullerton SM.** "Genomics is failing on diversity." *Nature*, 538:161-164, 2016. DOI: 10.1038/538161a

*Landmark commentary documenting European ancestry bias (78% of GWAS samples despite ~16% of global population).*

**Sirugo G, Williams SM, Tishkoff SA.** "The Missing Diversity in Human Genetic Studies." *Cell*, 177(1):26-31, 2019. DOI: 10.1016/j.cell.2019.02.048

*Comprehensive review on why genetic studies have limited utility across populations and implications for precision medicine.*

**Kessler MD, Taub MA, Shetty AC, Levin AM, et al.; CAAPA.** "Challenges and disparities in the application of personalized genomic medicine to populations with African ancestry." *Nature Communications*, 7:12521, 2016. DOI: 10.1038/ncomms12521

*Uses 642 whole genomes demonstrating ancestry-related biases in ClinVar and HGMD databases.*

---

## Priority 5: Conformal prediction in biology/genomics

**Boger R, et al.** "Functional protein mining with conformal guarantees." *Nature Communications*, 2024. DOI: 10.1038/s41467-024-55676-y

*Applies conformal prediction to protein homology search providing statistical guarantees (FDR control) for protein retrieval—highly relevant for protein function prediction with calibrated uncertainty.*

**Kartsonaki C, et al.** "Reliable machine learning models in genomic medicine using conformal prediction." *Frontiers in Bioinformatics*, 2025. DOI: 10.3389/fbinf.2025.1507448

*Comprehensive exploration covering variant calling uncertainty, antimicrobial resistance prediction, and tumor mutational burden estimation with conformal prediction.*

**Guan J, et al.** "Translating polygenic risk scores for clinical use by estimating the confidence bounds of risk prediction." *Nature Communications*, 2021. DOI: 10.1038/s41467-021-25014-7

*Introduces Mondrian Cross-Conformal Prediction (MCCP) for polygenic risk score calibration with individual-level risk probability and user-specified error rates.*

**Laghuvarapu S, et al.** "CoDrug: Conformal Drug Property Prediction with Density Estimation under Covariate Shift." *NeurIPS 2023*. arXiv: 2310.12033

*Addresses covariate shift in drug discovery conformal prediction using density estimation, reducing coverage gap by 35%.*

**Stafford A, et al.** "An Analysis of Proteochemometric and Conformal Prediction Machine Learning Protein-Ligand Binding Affinity Models." *Frontiers in Molecular Biosciences*, 2020. DOI: 10.3389/fmolb.2020.00093

*Evaluates conformal prediction for protein-ligand binding affinity (pIC50) prediction with well-calibrated prediction intervals.*

---

## Priority 6: OOD detection methods

### Foundational methods

**Hendrycks D, Gimpel K.** "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks." *International Conference on Learning Representations (ICLR 2017)*, 2017. arXiv: 1610.02136

*The foundational OOD detection paper proposing Maximum Softmax Probability (MSP) as a simple baseline—correctly classified examples have higher max softmax than OOD examples.*

**Lee K, Lee K, Lee H, Shin J.** "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks." *Advances in Neural Information Processing Systems* 31 (NeurIPS 2018), 2018. arXiv: 1807.03888

*Mahalanobis distance paper using class-conditional Gaussian distributions on deep features with Gaussian discriminant analysis—state-of-the-art for both OOD and adversarial detection.*

**Liang S, Li Y, Srikant R.** "Enhancing The Reliability of Out-of-distribution Image Detection in Neural Networks" (ODIN). *International Conference on Learning Representations (ICLR 2018)*, 2018. arXiv: 1706.02690

*Temperature scaling + input perturbation method separating in/out-distribution softmax scores. Reduces FPR from 34.7% to 4.3% at 95% TPR.*

**Liu W, Wang X, Owens J, Li Y.** "Energy-based Out-of-distribution Detection." *Advances in Neural Information Processing Systems* 33 (NeurIPS 2020), 2020. arXiv: 2010.03759

*Proposes energy function (log-sum-exp of logits) theoretically aligned with input density. Reduces average FPR by 18% compared to softmax—can be used post-hoc or with fine-tuning.*

### Genomics-specific OOD detection

**Ren J, Fort S, Liu J, Roy AG, Padhy S, Lakshminarayanan B.** "A Simple Fix to Mahalanobis Distance for Improving Near-OOD Detection." *ICML 2021*. arXiv: 2106.09022

*Proposes Relative Mahalanobis Distance (RMD). Explicitly evaluates on **Genomics OOD benchmark** achieving SOTA 66% AUROC.*

**Fort S, Ren J, Lakshminarayanan B.** "Exploring the Limits of Out-of-Distribution Detection." *NeurIPS 2021*.

*Includes genomics experiments showing pre-training + fine-tuning dramatically improves OOD detection. Tests MSP and Mahalanobis on genomic sequences using transformers, demonstrating correlation between genetic distance and AUROC.*

**Chen X, et al.** "Out of distribution learning in bioinformatics: advancements and challenges." *PMC*, 2024.

*Comprehensive review of OOD learning in bioinformatics covering genomics, proteomics, single-cell analysis, and drug discovery.*

**Benegas G, et al.** "Genomic Language Models: Opportunities and Challenges." arXiv: 2407.11435, 2024.

*Review discussing distribution shift challenges for genomic language models including transfer learning and cross-species generalization issues.*

---

## Quick reference table by chapter section

| Chapter Section | Key Papers |
|----------------|------------|
| Epistemic vs aleatoric uncertainty | Kendall & Gal 2017 |
| Temperature scaling | Guo et al. 2017 |
| Platt scaling | Platt 1999 |
| Isotonic regression | Niculescu-Mizil & Caruana 2005 |
| Reliability diagrams/ECE | DeGroot & Fienberg 1983; Naeini et al. 2015 |
| Brier score | Brier 1950 |
| Deep ensembles | Lakshminarayanan et al. 2017 |
| MC dropout | Kendall & Gal 2017 |
| Heteroscedastic networks | Nix & Weigend 1994 |
| Evidential deep learning | Sensoy et al. 2018; Bengs et al. 2022-2024 (critiques) |
| Conformal prediction | Vovk et al. 2005; Angelopoulos & Bates 2023 |
| OOD detection | Hendrycks & Gimpel 2017; Lee et al. 2018; Liang et al. 2018; Liu et al. 2020 |
| Likelihood OOD failures | Nalisnick et al. 2019; Ren et al. 2019 |
| Variant effect prediction | Cheng et al. 2023 (AlphaMissense); Brandes et al. 2023 (ESM) |
| Clinical VEP calibration | Pejaver et al. 2022; Bergquist et al. 2025 |
| ACMG-AMP guidelines | Richards et al. 2015; Tavtigian et al. 2018 |
| Population disparities | Martin et al. 2019; Popejoy & Fullerton 2016 |
| Communicating uncertainty | Han et al. 2017 |
| Conformal in genomics | Kartsonaki et al. 2025; Guan et al. 2021 |

This compilation provides verified citations with DOIs where available, covering the complete scope of the textbook chapter from foundational ML theory through genomic-specific applications.
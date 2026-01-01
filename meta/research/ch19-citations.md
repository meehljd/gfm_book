# Essential Citations for Multi-Omics Integration in Genomic Foundation Models

This comprehensive citation guide provides **25+ key papers** organized by topic area, with full bibliographic details and placement recommendations for a textbook chapter on multi-omics integration for genomic foundation models.

---

## Multi-omics factor analysis methods

### MOFA (Original Method)

**Citation:** Argelaguet R, Velten B, Arnol D, Dietrich S, Zenz T, Marioni JC, Buettner F, Huber W, Stegle O. Multi-Omics Factor Analysis—a framework for unsupervised integration of multi-omics data sets. *Molecular Systems Biology*. 2018;14(6):e8124.

**DOI:** 10.15252/msb.20178124

**Contribution:** Introduces Bayesian factor analysis for unsupervised discovery of principal variation sources in multi-omics datasets. Disentangles shared and modality-specific factors, enabling downstream sample clustering, data imputation, and outlier detection. Demonstrated on chronic lymphocytic leukemia cohort with **200 patients** across molecular modalities.

**Chapter placement:** Core methods section on classical statistical approaches to multi-omics integration.

---

### MOFA+

**Citation:** Argelaguet R, Arnol D, Bredikhin D, Deloro Y, Velten B, Marioni JC, Stegle O. MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data. *Genome Biology*. 2020;21:111.

**DOI:** 10.1186/s13059-020-02015-1

**Contribution:** Extends MOFA to single-cell scale with **GPU acceleration** and stochastic optimization, enabling analysis of millions of cells. Adds flexible sparsity constraints and multi-group modeling for batch correction. Key methodological bridge between bulk and single-cell multi-omics integration.

**Chapter placement:** Immediately following MOFA; section on scaling classical methods to single-cell resolution.

---

## Single-cell variational inference methods

### totalVI

**Citation:** Gayoso A*, Steier Z*, Lopez R, Regier J, Nazor KL, Streets A, Yosef N. Joint probabilistic modeling of single-cell multi-omic data with totalVI. *Nature Methods*. 2021;18(3):272-282. (*equal contribution)

**DOI:** 10.1038/s41592-020-01050-x

**Contribution:** Hierarchical Bayesian deep generative model for end-to-end **CITE-seq analysis** (RNA + protein). Jointly models biological and technical variation including protein background signal. Enables batch integration even across datasets with different protein panels, plus differential expression testing across modalities.

**Chapter placement:** Section on deep generative models for multi-modal single-cell data.

---

### MultiVI

**Citation:** Ashuach T*, Gabitto MI*, Koodli RV, Saldi G-A, Jordan MI, Yosef N. MultiVI: deep generative model for the integration of multimodal data. *Nature Methods*. 2023;20(8):1222-1231. (*equal contribution)

**DOI:** 10.1038/s41592-023-01909-9

**Contribution:** Extends scvi-tools ecosystem to integrate **RNA + ATAC-seq** (and optionally protein). Creates joint latent representation supporting imputation of missing modalities with calibrated uncertainty. Critical for combining paired multiome data with larger unpaired single-modality datasets.

**Chapter placement:** Following totalVI; demonstrates extension paradigm for modality expansion.

---

## Contrastive learning foundations

### CLIP

**Citation:** Radford A, Kim JW, Hallacy C, Ramesh A, Goh G, Agarwal S, Sastry G, Askell A, Mishkin P, Clark J, Krueger G, Sutskever I. Learning Transferable Visual Models From Natural Language Supervision. In: *Proceedings of the 38th International Conference on Machine Learning (ICML)*. PMLR. 2021;139:8748-8763.

**arXiv:** 2103.00020

**Contribution:** Foundational demonstration that **contrastive objectives align embeddings from fundamentally different data types** (images and text) in shared representation space. Trained on **400 million** image-text pairs, enabling zero-shot transfer across 30+ vision tasks. Established paradigm now applied to multi-omics alignment.

**Chapter placement:** Background section on contrastive learning theory; motivation for cross-modal alignment in biology.

---

## Radiogenomics: Glioblastoma

### TCGA-VASARI Study (Gutman et al.)

**Citation:** Gutman DA, Cooper LAD, Hwang SN, Holder CA, Gao J, Aurora TD, Dunn WD Jr, Scarpace L, Mikkelsen T, Jain R, Wintermark M, Jilwan H, Raghavan P, Huang E, Clifford RJ, Mongkolwat P, Kleper V, Freymann J, Kirby J, Zinn PL, Moreno CS, Jaffe C, Colen R, Rubin DL, Saltz J, Flanders A, Brat DJ. MR Imaging Predictors of Molecular Profile and Survival: Multi-institutional Study of the TCGA Glioblastoma Data Set. *Radiology*. 2013;267(2):560-569.

**DOI:** 10.1148/radiol.13120118

**Contribution:** Landmark study correlating standardized **VASARI imaging features** with Verhaak gene expression subtypes in GBM. Established that **proneural subtype** associates with low contrast enhancement, while **mesenchymal subtype** shows reduced non-enhanced tumor. Foundation for imaging-molecular correlations.

**Chapter placement:** Radiogenomics section; historical foundation for imaging-genomic integration.

---

### Machine Learning Radiogenomics (Kickingereder et al.)

**Citation:** Kickingereder P, Bonekamp D, Nowosielski M, Kratz A, Sill M, Burth S, Wick A, Eidel O, Schlemmer H-P, Radbruch A, Debus J, Herold-Mende C, Unterberg A, Jones D, Pfister S, Wick W, von Deimling A, Bendszus M, Capper D. Radiogenomics of Glioblastoma: Machine Learning-based Classification of Molecular Characteristics by Using Multiparametric and Multiregional MR Imaging Features. *Radiology*. 2016;281(3):907-918.

**DOI:** 10.1148/radiol.2016161382

**Contribution:** Correlates **31 multiparametric MRI features** with DNA methylation subgroups, MGMT promoter status, and copy number variations (EGFR, PDGFRA, CDK4 amplifications; PTEN, CDKN2A losses). Demonstrates machine learning prediction of molecular features from imaging alone.

**Chapter placement:** Following Gutman; shows progression to ML-based imaging-genomic prediction.

---

## Radiogenomics: Lung cancer

### CD8 Infiltration and Immunotherapy Response (Sun et al.)

**Citation:** Sun R, Limkin EJ, Vakalopoulou M, Dercle L, Champiat S, Han SR, Verlingue L, Brandao D, Lancia A, Ammari S, Hollebecque A, Scoazec J-Y, Marabelle A, Massard C, Soria J-C, Robert C, Paragios N, Deutsch E, Ferté C. A radiomics approach to assess tumour-infiltrating CD8 cells and response to anti-PD-1 or anti-PD-L1 immunotherapy: an imaging biomarker, retrospective multicohort study. *The Lancet Oncology*. 2018;19(9):1180-1191.

**DOI:** 10.1016/S1470-2045(18)30413-3

**Contribution:** Develops CT-based radiomics signature to estimate **tumor-infiltrating CD8 cells** and predict immunotherapy response. Five radiomic features distinguished high/low CD8 infiltration with **74% accuracy**. In immunotherapy cohort, high radiomics score predicted **48% reduced mortality risk**.

**Chapter placement:** Radiogenomics section; demonstrates clinical utility of imaging-immune correlation.

---

### Tumor Mutational Burden Prediction (He et al.)

**Citation:** He B, Dong D, She Y, Zhou C, Fang M, Zhu Y, Zhang H, Huang Z, Jiang T, Tian J, Chen C. Predicting response to immunotherapy in advanced non-small-cell lung cancer using tumor mutational burden radiomic biomarker. *Journal for ImmunoTherapy of Cancer*. 2020;8(2):e000550.

**DOI:** 10.1136/jitc-2020-000550

**Contribution:** Deep learning (3D-DenseNet) on CT images from **327 NSCLC patients** creates Tumor Mutational Burden Radiomic Biomarker (TMBRB). Successfully stratifies TMB levels and predicts immunotherapy response non-invasively—key example of **imaging-genomic surrogate markers**.

**Chapter placement:** Following Sun et al.; progression to deep learning approaches.

---

## Foundation models for medical imaging

### UNI - Pathology Foundation Model

**Citation:** Chen RJ, Ding T, Lu MY, Williamson DFK, Jaume G, Song AH, Chen B, Zhang A, Shao D, Shaban M, Williams M, Oldenburg L, Weishaupt LL, Wang JJ, Vaidya A, Le LP, Gerber G, Sahai S, Williams W, Mahmood F. Towards a general-purpose foundation model for computational pathology. *Nature Medicine*. 2024;30:850-862.

**DOI:** 10.1038/s41591-024-02857-3

**Contribution:** Foundation model trained on **\>100 million tissue patches** from \>100,000 H&E whole-slide images using DINOv2 self-supervision. Evaluated on **34 clinical pathology tasks**, enabling few-shot learning across 108 cancer types. Demonstrates scalable self-supervised pretraining for pathology.

**Chapter placement:** Foundation models section; pathology domain exemplar.

---

### CONCH - Vision-Language Pathology Model

**Citation:** Lu MY*, Chen B*, Williamson DFK*, Chen RJ, Liang I, Ding T, Jaume G, Odintsov I, Le LP, Gerber G, Parwani AV, Zhang A, Mahmood F. A visual-language foundation model for computational pathology. *Nature Medicine*. 2024;30:863-874. (*equal contribution)

**DOI:** 10.1038/s41591-024-02856-4

**Contribution:** Multimodal foundation model trained on **1.17 million histopathology image-caption pairs** using contrastive learning. Achieves zero-shot and few-shot capabilities across 14 benchmarks including image-to-text retrieval. Bridges CLIP paradigm to pathology domain.

**Chapter placement:** Following UNI; demonstrates multimodal extension of foundation model paradigm.

---

### Virchow - Clinical-Grade Pathology Model

**Citation:** Vorontsov E, Bozkurt A, Casson A, Shaikovski G, Zelechowski M, Liu S, Mathieu P, van Eck A, Lee D, Viber J, Ber K, Rosenberg RA, Weishaupt L, Ding T, Yousfi R, Iacobuzio-Donahue CA, Klimstra DS, Patel R, Panageas KS, Vanderbilt C, Carlson J, Campanella G, Fuchs TJ. A foundation model for clinical-grade computational pathology and rare cancers detection. *Nature Medicine*. 2024.

**DOI:** 10.1038/s41591-024-03141-0

**Contribution:** Trained on **~1.5 million whole-slide images** from Memorial Sloan Kettering using DINOv2. Vision Transformer with **632 million parameters** achieves **0.949 AUC** for pan-cancer detection across 17 types and **0.937 AUC** on rare cancers—demonstrating clinical-grade performance.

**Chapter placement:** Following CONCH; emphasizes clinical validation and rare disease detection.

---

### BiomedCLIP

**Citation:** Zhang S, Xu Y, Usuyama N, Bagga J, Tinn R, Preston S, Rao R, Wei M, Valluri N, Wong C, Lungren M, Naumann T, Poon H. BiomedCLIP: a multimodal biomedical foundation model pretrained from fifteen million scientific image-text pairs. *arXiv preprint arXiv:2303.00915*. 2023.

**DOI:** 10.48550/arXiv.2303.00915

**Contribution:** CLIP-style model trained on **PMC-15M dataset** (15 million biomedical image-text pairs from 4.4 million PubMed Central articles). Spans radiology, pathology, microscopy. State-of-the-art on 8+ biomedical benchmarks. **Fully open-access**—important for reproducibility.

**Chapter placement:** Foundation models section; cross-domain biomedical model.

---

## Missing heritability and GWAS

### Seminal "Missing Heritability" Paper

**Citation:** Manolio TA, Collins FS, Cox NJ, Goldstein DB, Hindorff LA, Hunter DJ, McCarthy MI, Ramos EM, Cardon LR, Chakravarti A, Cho JH, Guttmacher AE, Kong A, Kruglyak L, Mardis E, Rotimi CN, Slatkin M, Valle D, Whittemore AS, Boehnke M, Clark AG, Eichler EE, Gibson G, Haines JL, Mackay TFC, McCarroll SA, Visscher PM. Finding the missing heritability of complex diseases. *Nature*. 2009;461:747-753.

**DOI:** 10.1038/nature08494

**Contribution:** The **foundational paper** defining the missing heritability problem with **\>15,000 citations**. Documents that GWAS variants explain only small proportions of heritability with typical risk increments of **1.1–1.5-fold**. Proposes explanations including rare variants, structural variants, and gene-gene interactions.

**Chapter placement:** Motivation section; justifies need for multi-omics integration beyond common variants.

---

### SNP Heritability Estimation (Yang et al.)

**Citation:** Yang J, Benyamin B, McEvoy BP, Gordon S, Henders AK, Nyholt DR, Madden PA, Heath AC, Martin NG, Montgomery GW, Goddard ME, Visscher PM. Common SNPs explain a large proportion of the heritability for human height. *Nature Genetics*. 2010;42(7):565-569.

**DOI:** 10.1038/ng.608

**Contribution:** Introduced GCTA methodology showing **~45% of height variance** explained by all common SNPs simultaneously, versus only ~10% from GWAS-significant variants. Demonstrates heritability is "not missing but undetected" due to stringent significance thresholds—**3,000+ citations**.

**Chapter placement:** Following Manolio; quantitative framework for understanding variant contributions.

---

### Phantom Heritability (Zuk et al.)

**Citation:** Zuk O, Hechter E, Sunyaev SR, Lander ES. The mystery of missing heritability: Genetic interactions create phantom heritability. *Proceedings of the National Academy of Sciences*. 2012;109(4):1193-1198.

**DOI:** 10.1073/pnas.1119675109

**Contribution:** Proposes that genetic interactions inflate heritability estimates—part of "missing" heritability may be "phantom heritability." Notes GWAS explain **20-30% in well-studied cases**, but majority remains unexplained for most traits. Important methodological caveat.

**Chapter placement:** Nuanced discussion of heritability estimation limitations.

---

## Additional multi-omics integration methods

### SCENIC+

**Citation:** Bravo González-Blas C*, De Winter S*, Hulselmans G, Hecker N, Matetovici I, Christiaens V, Poovathingal S, Wouters J, Aibar S, Aerts S. SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks. *Nature Methods*. 2023;20:1355-1367. (*co-first authors)

**DOI:** 10.1038/s41592-023-01938-4

**Contribution:** Combines single-cell chromatin accessibility and expression with **\>30,000 TF motifs** to infer enhancer-driven gene regulatory networks (eGRNs). Predicts differentiation trajectories and TF perturbation effects. From the Aerts lab (VIB-KU Leuven).

**Chapter placement:** Gene regulatory network inference section.

---

### GLUE

**Citation:** Cao Z-J, Gao G. Multi-omics single-cell data integration and regulatory inference with graph-linked embedding. *Nature Biotechnology*. 2022;40:1458-1469.

**DOI:** 10.1038/s41587-022-01284-4

**Contribution:** Framework for integrating **unpaired** single-cell multi-omics using knowledge-based "guidance graph" modeling cross-layer regulatory interactions. Combines prior knowledge with adversarial learning for alignment. Scales to millions of cells.

**Chapter placement:** Section on unpaired multi-omics integration; contrasts with totalVI/MultiVI paired approaches.

---

### Seurat v5

**Citation:** Hao Y, Stuart T, Kowalski MH, Choudhary S, Hoffman P, Hartman A, Srivastava A, Molla G, Madad S, Fernandez-Granda C, Satija R. Dictionary learning for integrative, multimodal and scalable single-cell analysis. *Nature Biotechnology*. 2024;42:293-304.

**DOI:** 10.1038/s41587-023-01767-y

**Contribution:** Introduces "bridge integration" using multiome datasets as molecular bridges to connect unimodal measurements (RNA ↔ ATAC ↔ methylation ↔ protein). "Atomic sketch integration" enables scaling to **8.6 million cells**. Dominant toolkit in single-cell analysis.

**Chapter placement:** Practical methods section; widely-used integration toolkit.

---

### ArchR

**Citation:** Granja JM, Corces MR, Pierce SE, Bagdatli ST, Choudhry H, Chang HY, Greenleaf WJ. ArchR is a scalable software package for integrative single-cell chromatin accessibility analysis. *Nature Genetics*. 2021;53:403-411.

**DOI:** 10.1038/s41588-021-00790-6

**Contribution:** Comprehensive R toolkit for end-to-end scATAC-seq analysis including peak calling, trajectory inference, TF footprinting, and RNA integration. Analyzes **\>1.2 million cells in 8 hours** on standard laptop.

**Chapter placement:** Practical methods section for chromatin accessibility analysis.

---

## Single-cell foundation models

### scGPT

**Citation:** Cui H, Wang C, Maan H, Pang K, Luo F, Duan N, Wang B. scGPT: toward building a foundation model for single-cell multi-omics using generative AI. *Nature Methods*. 2024;21:1470-1480.

**DOI:** 10.1038/s41592-024-02201-0

**Contribution:** Generative pretrained transformer trained on **\>33 million single-cell transcriptomes**. Enables cell type annotation, multi-batch/multi-omic integration, perturbation prediction, and gene network inference. Key example of foundation model paradigm applied to single-cell biology.

**Chapter placement:** Foundation models section; single-cell domain.

---

### Geneformer

**Citation:** Theodoris CV, Xiao L, Chopra A, Chaffin MD, Al Sayed ZR, Hill MC, Mantineo H, Brydon E, Zeng Z, Liu XS, Ellinor PT. Transfer learning enables predictions in network biology. *Nature*. 2023;618:616-624.

**DOI:** 10.1038/s41586-023-06139-9

**Contribution:** Context-aware attention model pretrained on **~30 million cells** (expanded to \>100 million). Encodes network hierarchy through self-supervision. Validated for therapeutic target identification in cardiomyopathy. Published in *Nature*—high-impact foundation model paper.

**Chapter placement:** Foundation models section; emphasizes biological interpretation and clinical translation.

---

## Key review articles

### Single-Cell Multi-Omics Technologies Review

**Citation:** Baysoy A, Bai Z, Satija R, Fan R. The technological landscape and applications of single-cell multi-omics. *Nature Reviews Molecular Cell Biology*. 2023;24:695-713.

**DOI:** 10.1038/s41580-023-00615-w

**Contribution:** Comprehensive review covering transcriptome, genome, epigenome, proteome, and metabolome profiling technologies. Discusses throughput improvements, modality integration, and applications in cell atlases and tumor immunology.

**Chapter placement:** Background/introduction; technology overview.

---

### Multi-Omics Integration Review (Argelaguet et al.)

**Citation:** Argelaguet R, Cuomo C, Stegle O, Marioni JC. Multi-omics integration in the age of million single-cell data. *Nature Reviews Nephrology*. 2021;17:615-629.

**DOI:** 10.1038/s41581-021-00463-x

**Contribution:** Reviews integration principles for matched (same cells) versus unmatched (different cells) multimodal data. From MOFA developers—authoritative methodological perspective.

**Chapter placement:** Methods overview section; framework for understanding integration approaches.

---

## Citation summary by chapter section

| Section | Recommended Citations |
|---------|----------------------|
| **Introduction/Motivation** | Manolio 2009, Yang 2010, Baysoy 2023 review |
| **Classical Statistical Methods** | MOFA 2018, MOFA+ 2020 |
| **Deep Generative Models** | totalVI 2021, MultiVI 2023, GLUE 2022 |
| **Contrastive Learning** | CLIP 2021 |
| **Single-Cell Foundation Models** | scGPT 2024, Geneformer 2023 |
| **Medical Imaging Foundation Models** | UNI 2024, CONCH 2024, Virchow 2024, BiomedCLIP 2023 |
| **Radiogenomics** | Gutman 2013, Kickingereder 2016, Sun 2018, He 2020 |
| **Gene Regulatory Networks** | SCENIC+ 2023, ArchR 2021 |
| **Practical Toolkits** | Seurat v5 2024, ArchR 2021 |
| **Methods Review** | Argelaguet 2021 review |

This collection provides **comprehensive coverage** of the multi-omics integration field from classical statistical methods through modern foundation models, with appropriate citations for each methodological approach and application domain discussed in the chapter.
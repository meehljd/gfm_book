# Citation Guide for Genomic Foundation Models in Drug Discovery

Drug discovery increasingly relies on genomic data and foundation models across the therapeutic development pipeline. This guide provides **32 peer-reviewed papers** organized by topic, covering target identification through patient stratification. Each citation includes full bibliographic details, key findings, and relevance to genomic AI applications.

---

## 1. Genetic evidence doubles drug target success rates

The landmark finding that genetically-supported targets succeed **2-2.6 times more often** in clinical trials has fundamentally reshaped pharmaceutical target selection strategies. Four papers establish and validate this claim.

**Nelson MR, Tipney H, Painter JL, et al.** "The support of human genetic evidence for approved drug indications." *Nature Genetics* 47(8):856-860 (2015). DOI: 10.1038/ng.3314

This GlaxoSmithKline study analyzed **22,270 drugs** modulating 1,824 targets across 705 indications. Drug mechanisms with direct genetic support increased from 2.0% at preclinical stage to **8.2% for approved compounds**—the original foundation for the "2x success rate" claim. Citation count exceeds 1,500.

**King EA, Davis JW, Degner JF.** "Are drug targets with genetic support twice as likely to be approved? Revised estimates of the impact of genetic support for drug mechanisms on the probability of drug approval." *PLOS Genetics* 15(12):e1008489 (2019). DOI: 10.1371/journal.pgen.1008489

AbbVie's independent validation confirmed the Nelson findings using 2013-2018 data. Mendelian genetic evidence showed the strongest predictive effect (>2-fold), establishing that the benefit concentrates where causal genes are clearly identified.

**Minikel EV, Painter JL, Dong CC, Nelson MR.** "Refining the impact of genetic evidence on clinical success." *Nature* 629:624-629 (2024). DOI: 10.1038/s41586-024-07316-0

The definitive update from Broad Institute and Deerfield analyzed **29,476 target-indication pairs**, revising the success rate advantage to **2.6-fold**. Therapeutic areas including hematology, metabolic, respiratory, and endocrine showed >3x relative success. Critically, only 1.1% of genetically-supported targets have been clinically explored.

**Trajanoska K, et al.** "From target discovery to clinical drug development with human genetics." *Nature* 620:737-745 (2023). DOI: 10.1038/s41586-023-06388-8

This comprehensive review documents how genetic evidence informs dose-response relationships, safety predictions, and the **13-year average lag** from genetic association to first clinical trial.

---

## 2. Network proximity methods identify repurposing opportunities

Network medicine provides a principled framework for drug repurposing by measuring how drug targets relate to disease modules within protein-protein interaction networks.

**Guney E, Menche J, Vidal M, Barabási AL.** "Network-based in silico drug efficacy screening." *Nature Communications* 7:10331 (2016). DOI: 10.1038/ncomms10331

The foundational network proximity paper introduced the **closest distance metric (dc)** measuring drug target proximity to disease proteins in the human interactome (141,150 PPIs, 13,329 proteins). Key insight: drugs need not directly target disease proteins—therapeutic effect localizes within **2 network steps** of the disease module. Achieved AUC ~67% for discriminating known drug-disease pairs.

**Cheng F, Desai RJ, Handy DE, et al.** "Network-based approach to prediction and population-based validation of in silico drug repurposing." *Nature Communications* 9:2691 (2018). DOI: 10.1038/s41467-018-05116-5

Cheng and Barabási extended network proximity to **984 FDA-approved drugs** across 23 cardiovascular disease types using an improved interactome (243,603 PPIs). Validated predictions in healthcare databases with **>220 million patients**—the first paper combining network predictions, real-world evidence, and mechanistic validation.

**Morselli Gysi D, Do Valle Í, Zitnik M, et al.** "Network medicine framework for identifying drug-repurposing opportunities for COVID-19." *PNAS* 118(19):e2025581118 (2021). DOI: 10.1073/pnas.2025581118

Compared three complementary algorithms (AI/ML, network diffusion, network proximity) on **6,340 drugs** for SARS-CoV-2 repurposing. Critical finding: 76 of 77 drugs reducing viral infection do NOT directly bind viral proteins—they work through network-mediated mechanisms.

**Ruiz C, Zitnik M, Leskovec J.** "Identification of disease treatment mechanisms through the multiscale interactome." *Nature Communications* 12:1796 (2021). DOI: 10.1038/s41467-021-21770-8

Introduced **multiscale network diffusion** integrating 17,660 proteins with 9,798 biological functions from Gene Ontology. Biased random walks through functional hierarchies predict drug-disease treatment **40% more effectively** than molecular-scale approaches alone.

---

## 3. Deep learning advances drug-target interaction prediction

DTI prediction has evolved from sequence-based CNNs to foundation models leveraging pretrained protein language models.

**Öztürk H, Özgür A, Ozkirimli E.** "DeepDTA: Deep drug–target binding affinity prediction." *Bioinformatics* 34(17):i821-i829 (2018). DOI: 10.1093/bioinformatics/bty593

The pioneering end-to-end deep learning method for drug-target affinity using **1D sequence representations only**—no 3D structures required. Architecture: dual CNNs process SMILES strings and amino acid sequences, achieving concordance index 0.878 on Davis dataset and 0.863 on KIBA. This paper transitioned the field from traditional ML to deep learning.

**Nguyen T, Le H, Quinn TP, et al.** "Predicting drug–target binding affinity with graph neural networks." *Bioinformatics* 37(8):1140-1147 (2021). DOI: 10.1093/bioinformatics/btaa921

GraphDTA introduced **molecular graph representations** for drugs, treating atoms as nodes and bonds as edges. Tested GCN, GAT, GIN, and GAT-GCN architectures; GIN showed best performance. Outperformed DeepDTA while learning domain-specific features automatically.

**Lam HYI, Guan JS, Ong XE, Pincket R, Mu Y.** "BIND: Protein Language Models for Structure-Free Virtual Screening." *Briefings in Bioinformatics* 25(6):bbae480 (2024). DOI: 10.1093/bib/bbae480

Leverages pretrained **ESM-2 (650M parameters)** for structure-free virtual screening with only 9.26M trainable parameters. Novel graph-to-transformer cross-attention enables ligand to "query" protein regions. Achieved state-of-the-art enrichment factors on DEKOIS 2.0 (EF1%=24.46) and DUD-E (EF1%=46.35, AUROC=0.944)—**2-3 orders of magnitude faster** than structure-based methods.

**Key benchmark datasets:** Davis dataset (Davis MI et al., *Nature Biotechnology* 2011: 442 kinases × 68 ligands); KIBA dataset (Tang J et al., *J Chem Inf Model* 2014: integrated Ki/Kd/IC50 scores); BindingDB (Liu T et al., *Nucleic Acids Research* 2007: experimentally determined affinities).

---

## 4. Perturbation foundation models predict cellular responses

Foundation models trained on Perturb-seq data now predict transcriptional outcomes of untested perturbations, enabling virtual screening of combinatorial interventions.

**Roohani Y, Huang K, Leskovec J.** "Predicting transcriptional outcomes of novel multigene perturbations with GEARS." *Nature Biotechnology* 42:927-935 (2024). DOI: 10.1038/s41587-023-01905-6

GEARS integrates **graph neural networks with Gene Ontology knowledge graphs** to predict outcomes of gene combinations never experimentally tested. Achieves **40% higher precision** in predicting genetic interaction subtypes (synergy, suppression, neomorphism, redundancy, epistasis). Enables prioritization of combinatorial perturbations for target validation.

**Cui H, Wang C, Maan H, et al.** "scGPT: toward building a foundation model for single-cell multi-omics using generative AI." *Nature Methods* 21:1470-1480 (2024). DOI: 10.1038/s41592-024-02201-0

Foundation model pretrained on **33 million single-cell RNA-seq profiles** from CZ CELLxGENE. Treats genes as tokens; uses masked expression prediction. Performs perturbation response prediction, cell type annotation, multi-batch integration, and gene regulatory network inference.

**Lotfollahi M, Klimovskaia Susmelj A, De Donno C, et al.** "Predicting cellular responses to complex perturbations in high-throughput screens." *Molecular Systems Biology* 19:e11517 (2023). DOI: 10.15252/msb.202211517

CPA (Compositional Perturbation Autoencoder) learns **factorized latent representations** separating basal cell state, perturbation effects, and covariates. Predicts dose-response curves and out-of-distribution drug combinations. Imputed **97.6% of missing combinations** in Perturb-seq data.

**Dixit A, Parnas O, Li B, et al.** "Perturb-Seq: Dissecting Molecular Circuits with Scalable Single-Cell RNA Profiling of Pooled Genetic Screens." *Cell* 167(7):1853-1866 (2016). DOI: 10.1016/j.cell.2016.11.038

The original Perturb-seq method combining pooled CRISPR screening with single-cell RNA-seq. Developed MIMOSCA computational framework; analyzed 200,000 cells studying transcription factors in immune response.

**Datlinger P, Rendeiro AF, Schmidl C, et al.** "Pooled CRISPR screening with single-cell transcriptome readout." *Nature Methods* 14(3):297-301 (2017). DOI: 10.1038/nmeth.4177

CROP-seq optimized vector design making guide RNA **directly detectable** in single-cell RNA-seq without separate barcodes. Compatible with Drop-seq and 10x Genomics platforms.

---

## 5. Transcriptomic signatures predict drug toxicity

The Connectivity Map paradigm enables toxicity prediction by comparing drug-induced expression signatures to reference profiles.

**Lamb J, Crawford ED, Peck D, et al.** "The Connectivity Map: Using Gene-Expression Signatures to Connect Small Molecules, Genes, and Disease." *Science* 313(5795):1929-35 (2006). DOI: 10.1126/science.1132939

The foundational CMap paper created reference expression profiles from **164 drugs** in MCF7, PC3, and HL60 cells. Introduced GSEA-based signature matching to find functional connections among drugs, genes, and diseases.

**Subramanian A, Narayan R, Corsello SM, et al.** "A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles." *Cell* 171(6):1437-1452.e17 (2017). DOI: 10.1016/j.cell.2017.10.049

1,000-fold scale-up of CMap through the NIH LINCS Consortium. L1000 measures **978 landmark genes** and computationally infers 11,350 additional genes. Generated **1.3 million profiles** covering ~25,200 perturbagens across ~77 cell lines. Platform available at clue.io.

**Kohonen P, Parkkinen JA, Willighagen EL, et al.** "A transcriptomics data-driven gene space accurately predicts liver cytopathology and drug-induced liver injury." *Nature Communications* 8:15932 (2017). DOI: 10.1038/ncomms15932

Developed Predictive Toxicogenomics Space (PTGS)—**1,331 genes in 14 components**—using CMap and NCI-60 data fusion. Predicts DILI from hepatocyte experiments with **72-86% sensitivity** without specificity loss, outperforming QSAR approaches.

**Wang Z, Clark NR, Ma'ayan A.** "Drug-induced adverse events prediction with the LINCS L1000 data." *Bioinformatics* 32(15):2338-2345 (2016). DOI: 10.1093/bioinformatics/btw168

Machine learning classifier integrating chemical structure with L1000 gene expression features. Transforming expression to **Gene Ontology enrichment vectors** improves ADR prediction. SEP-L1000 portal provides predictions for 20,413 LINCS compounds.

---

## 6. Polygenic scores enable clinical trial enrichment

PRS-based stratification can achieve **>90% reductions** in required trial sample sizes through prognostic and predictive enrichment.

**Fahed AC, Philippakis AA, Khera AV.** "The potential of polygenic scores to improve cost and efficiency of clinical trials." *Nature Communications* 13:2922 (2022). DOI: 10.1038/s41467-022-30675-z

Methodological framework demonstrating that enrolling only top-quintile PGS participants in FOURIER could have required **2,360 participants—a >90% reduction**—while demonstrating 31% vs 20% relative risk reduction.

**Marston NA, Kamanu FK, Nordio F, et al.** "Predicting Benefit From Evolocumab Therapy in Patients With Atherosclerotic Disease Using a Genetic Risk Score: Results From the FOURIER Trial." *Circulation* 141(8):616-623 (2020). DOI: 10.1161/CIRCULATIONAHA.119.043805

Analyzed 14,298 FOURIER patients using 27-SNP and genome-wide PRS. High genetic risk patients (top quintile) showed HR 1.65 for MACE and derived **greatest absolute and relative benefit** from evolocumab. Patients with combined high clinical and genetic risk achieved **6.3% absolute risk reduction**.

**Damask A, Steg PG, Schwartz GG, et al.** "Patients With High Genome-Wide Polygenic Risk Scores for Coronary Artery Disease May Receive Greater Clinical Benefit From Alirocumab Treatment in the ODYSSEY OUTCOMES Trial." *Circulation* 141(8):624-636 (2020). DOI: 10.1161/CIRCULATIONAHA.119.044434

Independent replication using genome-wide PRS (>6 million variants) in ODYSSEY OUTCOMES. High PRS patients (HR 1.59 for MACE) showed greater benefit from alirocumab, while low/intermediate genetic risk patients showed minimal benefit over trial duration.

**German J, Yang Z, Urbut S, et al.** "Incorporating genetic data improves target trial emulations and informs the use of polygenic scores in randomized controlled trial design." *Nature Genetics* 57:1620-1627 (2025). DOI: 10.1038/s41588-025-02229-8

Emulated 4 major cardiometabolic RCTs (EMPA-REG, TECOS, ARISTOTLE, ROCKET-AF) using FinnGen biobank. Top 25% CHD PGS enrichment reduces required sample sizes by **8.6-26%**. Critically demonstrates that PGS performance in general populations may not translate to trial-eligible populations.

---

## 7. Regulatory frameworks guide genomic biomarker implementation

FDA has established clear pathways for pharmacogenomic labeling and companion diagnostic approval, with **threefold increase** in PGx-labeled drugs from 2000 to 2020.

**Kim JA, Ceccarelli R, Lu CY.** "Pharmacogenomic Biomarkers in US FDA-Approved Drug Labels (2000–2020)." *Journal of Personalized Medicine* 11(3):179 (2021). DOI: 10.3390/jpm11030179

Documented increase from 10.3% (2000) to **28.2% (2020)** in new drug approvals with PGx labeling. Of 258 biomarker-drug pairs, **61.6% are clinically actionable**; cancer therapies comprise 75.5% of required-testing pairs.

**Drozda K, Pacanowski MA, Grimstein C, Zineh I.** "Pharmacogenetic Labeling of FDA-Approved Drugs: A Regulatory Retrospective." *JACC: Basic to Translational Science* 3(4):545-549 (2018). DOI: 10.1016/j.jacbts.2018.06.001

FDA officials outline regulatory principles under **21 CFR 201.57**, using warfarin, carbamazepine, abacavir, and clopidogrel as case studies. Discusses evidence standards for retrospective vs prospective pharmacogenomic studies.

**Fridlyand J, Simon RM, Walrath JC, et al.** "Considerations for the successful co-development of targeted cancer therapies and companion diagnostics." *Nature Reviews Drug Discovery* 12(10):743-755 (2013). DOI: 10.1038/nrd4101

Multi-stakeholder perspective on FDA's 2011 companion diagnostic guidance. Addresses when trials should enroll biomarker-positive patients only, Investigational Device Exemption pathways, and Laboratory-Developed Tests regulatory status.

**Jørgensen JT.** "The current landscape of the FDA approved companion diagnostics." *Translational Oncology* 14(6):101063 (2021). DOI: 10.1016/j.tranon.2021.101063

Comprehensive review of **44 CDx assays** approved since 1998's HercepTest. Details Class II/III device pathways (PMA, 510(k), HDE), including 9 LDT-derived CDx with PMA approval. Documents evolution from single-marker paradigm to NGS panels and tumor-agnostic approvals.

---

## 8. Active learning optimizes genomic experimental design

Lab-in-the-loop approaches use Bayesian optimization and adaptive sampling to maximize information from costly perturbation experiments.

**Lyle C, Mehrjou A, Notin P, et al.** "DiscoBAX: Discovery of optimal intervention sets in genomic experiment design." *ICML 2023*, PMLR 202:23170-23189 (2023). URL: proceedings.mlr.press/v202/lyle23a.html

Sample-efficient Bayesian optimization for perturbation experiments that maximizes discovery rate while probing **diverse mechanisms**. Provides theoretical optimality guarantees; tested on CRISPR screen design tasks.

**Qin J, et al.** "Active learning for efficient discovery of optimal gene combinations in the combinatorial perturbation space." *arXiv:2411.12010* (2024).

NAIAD framework for discovering optimal gene pairs using **Maximum Predicted Effect acquisition**. Outperforms existing models by 40% on small datasets; identified **>2x more strong perturbations** by 4th iteration compared to random sampling. Explicitly designed for iterative lab-in-the-loop workflows.

**Li Y, Cui T, et al.** "BioBO: Biology-informed Bayesian Optimization for Perturbation Design." *arXiv:2509.19988* (2025).

Integrates Bayesian optimization with **multimodal gene embeddings** (sequence, functional, network-based). Incorporates enrichment analysis for biological interpretability; improves labeling efficiency by **25-40%** over conventional BO.

**Mehrjou A, et al.** "GeneDisco: A Benchmark for Experimental Design in Drug Discovery." *ICLR 2022*.

Standardized benchmark for evaluating active learning methods in genetic intervention experiments, enabling systematic comparison of acquisition functions and surrogate models.

---

## Summary by chapter section

| Chapter Section | Key Papers | Core Citations |
|-----------------|------------|----------------|
| Target identification | Genetic evidence | Nelson 2015, Minikel 2024 |
| Target identification | Network repurposing | Guney 2016, Cheng 2018 |
| Drug-target interaction | Deep learning DTI | DeepDTA 2018, BIND 2024 |
| Perturbation biology | Foundation models | GEARS 2024, scGPT 2024, CPA 2023 |
| Toxicity prediction | Expression signatures | CMap 2006, L1000 2017, PTGS 2017 |
| Biomarker development | PRS stratification | Marston 2020, Damask 2020, Fahed 2022 |
| Patient stratification | Regulatory | Kim 2021, Jørgensen 2021 |
| Experimental design | Active learning | DiscoBAX 2023, NAIAD 2024 |

This collection provides foundational methods papers, validation studies, and recent foundation model advances across the genomic drug discovery pipeline.
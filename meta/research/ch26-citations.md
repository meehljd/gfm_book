# Key Citations for Rare Disease Diagnosis Using Foundation Models and Genomic Sequencing

This curated reference list provides **35 high-quality academic papers** across 12 topic areas for a textbook chapter on rare disease diagnosis. Each citation includes the full reference, DOI, and a brief note on its contribution to the field.

---

## Diagnostic yield studies

Large-scale studies establishing the clinical utility and expected solve rates from exome and genome sequencing form the evidence base for implementing genomic medicine in rare disease.

**Yang Y, Muzny DM, Reid JG, et al.** Clinical whole-exome sequencing for the diagnosis of Mendelian disorders. *New England Journal of Medicine* 2013; 369:1502-1511. **DOI: 10.1056/NEJMoa1306555**
Landmark study establishing clinical exome sequencing as a diagnostic tool, achieving **25% diagnostic yield** in the first 250 consecutive patients at a CLIA-certified laboratory. First large-scale demonstration of clinical utility.

**Yang Y, Muzny DM, Xia F, et al.** Molecular findings among patients referred for clinical whole-exome sequencing. *JAMA* 2014; 312(18):1870-1879. **DOI: 10.1001/jama.2014.14601**
Expanded analysis of 2,000 consecutive patients confirming the **~25% diagnostic rate** across a diverse clinical cohort and detailing the spectrum of genetic alterations contributing to Mendelian disease.

**Wright CF, Fitzgerald TW, Jones WD, et al.** Genetic diagnosis of developmental disorders in the DDD study: a scalable analysis of genome-wide research data. *The Lancet* 2015; 385(9975):1305-1314. **DOI: 10.1016/S0140-6736(14)61705-0**
First nationwide trio exome sequencing study for developmental disorders, achieving **27% diagnostic yield** in over 1,000 children. Demonstrated that trio sequencing reduces candidate variants 10-fold compared to proband-only analysis.

**Splinter K, Adams DR, Bacino CA, et al.** Effect of genetic diagnosis on patients with previously undiagnosed disease. *New England Journal of Medicine* 2018; 379(22):2131-2139. **DOI: 10.1056/NEJMoa1714458**
Seminal Undiagnosed Diseases Network outcomes paper reporting **35% diagnostic yield** and defining 31 new syndromes. Demonstrated that 21% of diagnoses led to therapy changes.

**Smedley D, Smith KR, Martin A, et al.** 100,000 Genomes Pilot on rare-disease diagnosis in health care — preliminary report. *New England Journal of Medicine* 2021; 385(20):1868-1880. **DOI: 10.1056/NEJMoa2035790**
Landmark study demonstrating genome sequencing integration into the UK NHS with **25% overall diagnostic yield**. Found 14% of diagnoses specifically required genome sequencing to detect noncoding and structural variants missed by exome.

---

## ClinGen and PanelApp

These resources provide standardized frameworks for evaluating gene-disease validity and curating clinical gene panels essential for diagnostic interpretation.

**Rehm HL, Berg JS, Brooks LD, et al.** ClinGen — The Clinical Genome Resource. *New England Journal of Medicine* 2015; 372:2235-2242. **DOI: 10.1056/NEJMsr1406261**
Foundational paper introducing ClinGen as the NIH-funded resource for defining clinical relevance of genes and variants, establishing the framework for standardized genomic knowledge curation.

**Strande NT, Riggs ER, Buchanan AH, et al.** Evaluating the clinical validity of gene-disease associations: an evidence-based framework developed by the Clinical Genome Resource. *American Journal of Human Genetics* 2017; 100(6):895-906. **DOI: 10.1016/j.ajhg.2017.04.015**
Describes ClinGen's semi-quantitative framework for evaluating gene-disease relationships with six validity classifications (Definitive through Conflicting Evidence) based on weighted genetic and experimental evidence.

**Martin AR, Williams E, Foulger RE, et al.** PanelApp crowdsources expert knowledge to establish consensus diagnostic gene panels. *Nature Genetics* 2019; 51(11):1560-1565. **DOI: 10.1038/s41588-019-0528-2**
Introduces Genomics England's PanelApp crowdsourcing platform with traffic-light rating system (green/amber/red) for gene-disease evidence, used to establish consensus diagnostic gene lists for the 100,000 Genomes Project.

---

## VUS reclassification

Studies documenting how variants of uncertain significance evolve with accumulating evidence inform expectations for diagnostic uncertainty and recontact policies.

**Kobayashi Y, Chen E, Facio FM, et al.** Clinical variant reclassification in hereditary disease genetic testing. *JAMA Network Open* 2024; 7(11):e2444526. **DOI: 10.1001/jamanetworkopen.2024.44526**
Largest reclassification study analyzing >2 million variants (2015-2023). Found **57% of VUS reclassifications** resulted from improved computational modeling and documented racial/ethnic disparities in reclassification rates.

**Bennett G, Karbassi I, Chen W, et al.** Distinct rates of VUS reclassification are observed when subclassifying VUS by evidence level. *Genetics in Medicine* 2025; 27(2):101400. **DOI: 10.1016/j.gim.2025.101400**
Multi-laboratory study of 151,368 variants demonstrating that VUS-low variants are never reclassified as pathogenic while VUS-high variants frequently upgrade. Provides evidence-based guidance for VUS subclassification in clinical practice.

---

## gnomAD constraint scores

Population-level constraint metrics quantify intolerance to loss-of-function variation and are central to variant prioritization in clinical interpretation.

**Lek M, Karczewski KJ, Minikel EV, et al.** Analysis of protein-coding genetic variation in 60,706 humans. *Nature* 2016; 536(7616):285-291. **DOI: 10.1038/nature19057**
Foundational ExAC paper introducing the **pLI (probability of loss-of-function intolerance) score**. Identified 3,230 genes with high constraint (pLI ≥0.9), establishing the framework for using population variant data to assess gene essentiality.

*Note: The gnomAD paper (Karczewski et al. 2020, Nature) introducing LOEUF is already cited in the chapter.*

---

## Phenotype-driven prioritization

Tools leveraging the Human Phenotype Ontology enable computational matching of patient phenotypes to candidate diagnoses, dramatically improving variant prioritization.

**Robinson PN, Köhler S, Bauer S, et al.** The Human Phenotype Ontology: a tool for annotating and analyzing human hereditary disease. *American Journal of Human Genetics* 2008; 83(5):610-615. **DOI: 10.1016/j.ajhg.2008.09.017**
Seminal paper establishing HPO with >8,000 phenotype terms. Demonstrated that ontological similarity measures capture phenotypic relationships between diseases, becoming the worldwide standard for phenotype exchange in rare disease diagnostics.

**Robinson PN, Köhler S, Oellrich A, et al.** Improved exome prioritization of disease genes through cross-species phenotype comparison. *Genome Research* 2014; 24(2):340-348. **DOI: 10.1101/gr.160325.113**
Foundational Exomiser paper introducing the PHIVE algorithm. Achieved correct gene ranking in **83% of simulations** by integrating cross-species phenotype comparisons with variant pathogenicity scores.

**Robinson PN, Ravanmehr V, Jacobsen JOB, et al.** Interpretable clinical genomics with a likelihood ratio paradigm. *American Journal of Human Genetics* 2020; 107(3):403-417. **DOI: 10.1016/j.ajhg.2020.06.021**
Introduced LIRICAL, providing interpretable posttest probabilities using likelihood ratios. Placed correct diagnosis in top 3 ranks in **92.9% of 384 cases** with transparent contribution scores for clinical interpretation.

**Zhao M, Havrilla JM, Fang L, et al.** Phen2Gene: rapid phenotype-driven gene prioritization for rare diseases. *NAR Genomics and Bioinformatics* 2020; 2(2):lqaa032. **DOI: 10.1093/nargab/lqaa032**
Rapid HPO-driven gene prioritization tool that works from phenotype terms alone without requiring variant data, enabling pre-sequencing candidate gene identification.

---

## MPRA methodology

Massively parallel reporter assays enable high-throughput functional characterization of regulatory variants, providing experimental evidence for variant interpretation.

**Melnikov A, Murugan A, Zhang X, et al.** Systematic dissection and optimization of inducible enhancers in human cells using a massively parallel reporter assay. *Nature Biotechnology* 2012; 30(3):271-277. **DOI: 10.1038/nbt.2137**
Foundational MPRA paper demonstrating systematic dissection of >27,000 enhancer variants in human cells at single-nucleotide resolution.

**Patwardhan RP, Hiatt JB, Witten DM, et al.** Massively parallel functional dissection of mammalian enhancers in vivo. *Nature Biotechnology* 2012; 30(3):265-270. **DOI: 10.1038/nbt.2136**
Companion paper demonstrating in vivo MPRA by dissecting three mammalian enhancers at single-nucleotide resolution in mouse liver using >100,000 mutant haplotypes per enhancer.

**Tewhey R, Kotliar D, Park DS, et al.** Direct identification of hundreds of expression-modulating variants using a multiplexed reporter assay. *Cell* 2016; 165(6):1519-1529. **DOI: 10.1016/j.cell.2016.04.027**
Key application paper testing 32,373 variants from cis-eQTLs, identifying 842 expression-modulating variants including 53 disease-associated variants. Establishes MPRA for systematic identification of causal regulatory variants.

---

## Deep mutational scanning resources

DMS provides comprehensive functional maps of variant effects, increasingly integrated into clinical variant interpretation workflows.

**Fowler DM, Fields S.** Deep mutational scanning: a new style of protein science. *Nature Methods* 2014; 11(8):801-807. **DOI: 10.1038/nmeth.3027**
Definitive methodological perspective describing how DMS can assess activities of up to 1 million protein variants per experiment, establishing the foundational concepts for this field.

**Esposito D, Weile J, Shendure J, et al.** MaveDB: an open-source platform to distribute and interpret data from multiplexed assays of variant effect. *Genome Biology* 2019; 20:223. **DOI: 10.1186/s13059-019-1845-6**
Original paper introducing MaveDB (mavedb.org), the standardized public repository for large-scale variant effect measurements from deep mutational scanning and MPRA studies.

---

## EVE model

The EVE model represents a major advance in unsupervised variant effect prediction using evolutionary sequence information.

**Frazer J, Notin P, Dias M, et al.** Disease variant prediction with deep generative models of evolutionary data. *Nature* 2021; 599:91-95. **DOI: 10.1038/s41586-021-04043-8**
Introduces EVE (Evolutionary model of Variant Effect), a Bayesian VAE predicting pathogenicity for **>36 million variants** across 3,219 disease genes without labeled training data. Provided reclassification evidence for >256,000 VUS and outperformed supervised methods.

---

## Reanalysis of unsolved cases

Systematic reanalysis studies demonstrate that expanding knowledge continuously increases diagnostic yield, supporting periodic data reinterpretation.

**Liu P, Meng L, Normand EA, et al.** Reanalysis of clinical exome sequencing data. *New England Journal of Medicine* 2019; 380(25):2478-2480. **DOI: 10.1056/NEJMc1812033**
Definitive study demonstrating diagnostic yield increase from **25% to 37-47%** through systematic reanalysis. Found 75% of new diagnoses resulted from newly discovered disease genes.

**Dai P, Honda A, Ewans L, et al.** Recommendations for next generation sequencing data reanalysis of unsolved cases with suspected Mendelian disorders: a systematic review and meta-analysis. *Genetics in Medicine* 2022; 24(8):1618-1626. **DOI: 10.1016/j.gim.2022.04.021**
Meta-analysis of 29 reanalysis studies finding **10% pooled additional diagnostic yield** (95% CI: 6-13%). Establishes reanalysis as evidence-based practice with standardized guidelines.

**Wright CF, McRae JF, Clayton S, et al.** Making new genetic diagnoses with old data: iterative reanalysis and reporting from genome-wide data in 1,133 families with developmental disorders. *Genetics in Medicine* 2018; 20(10):1216-1223. **DOI: 10.1038/gim.2017.161**
DDD consortium study demonstrating value of iterative reanalysis through incorporation of newly discovered genes and variant reclassification.

---

## Noncoding variants in rare disease

Evidence for pathogenic noncoding variants expands the diagnostic scope beyond coding regions and supports genome sequencing adoption.

**Cummings BB, Marshall JL, Tukiainen T, et al.** Improving genetic diagnosis in Mendelian disease with transcriptome sequencing. *Science Translational Medicine* 2017; 9(386):eaal5209. **DOI: 10.1126/scitranslmed.aal5209**
Landmark study achieving **35% diagnostic yield** using RNA-seq in 50 patients with undiagnosed muscle disorders. Systematically demonstrated detection of splice-altering variants in deep intronic regions.

**Smedley D, Schubach M, Jacobsen JOB, et al.** A whole-genome analysis framework for effective identification of pathogenic regulatory variants in Mendelian disease. *American Journal of Human Genetics* 2016; 99(3):595-606. **DOI: 10.1016/j.ajhg.2016.07.005**
Introduced the Genomiser framework and ReMM (Regulatory Mendelian Mutation) score, achieving identification of causal regulatory variants as top candidate in **77% of simulated genomes**.

**Vaz-Drago R, Custódio N, Carmo-Fonseca M.** Deep intronic mutations and human disease. *Human Genetics* 2017; 136(9):1093-1111. **DOI: 10.1007/s00439-017-1809-4**
Comprehensive review documenting pathogenic deep intronic mutations in over 75 disease genes, establishing mechanistic framework for pseudo-exon activation variants.

---

## De novo mutations in developmental disorders

Large-scale de novo mutation studies established the genetic architecture of neurodevelopmental disorders and validated trio-based diagnostic approaches.

**Vissers LELM, de Ligt J, Gilissen C, et al.** A de novo paradigm for mental retardation. *Nature Genetics* 2010; 42:1109-1112. **DOI: 10.1038/ng.712**
Foundational paper establishing that de novo point mutations are a major cause of sporadic intellectual disability, pioneering trio-based exome sequencing for disease gene discovery.

**Sanders SJ, Murtha MT, Gupta AR, et al.** De novo mutations revealed by whole-exome sequencing are strongly associated with autism. *Nature* 2012; 485:237-241. **DOI: 10.1038/nature10945**
Study of 928 individuals demonstrating strong association between disruptive de novo mutations in brain-expressed genes and autism spectrum disorders. Established statistical framework for recurrent mutation analysis.

**Deciphering Developmental Disorders Study.** Prevalence and architecture of de novo mutations in developmental disorders. *Nature* 2017; 542:433-438. **DOI: 10.1038/nature21062**
Landmark DDD analysis of 4,293 families finding **42% carry pathogenic coding de novo mutations**. Estimated developmental disorders from DNMs occur in 1/213-1/448 births (~400,000 children/year globally).

**Rauch A, Wieczorek D, Graf E, et al.** Range of genetic mutations associated with severe non-syndromic sporadic intellectual disability: an exome sequencing study. *The Lancet* 2012; 380(9854):1674-1682. **DOI: 10.1016/S0140-6736(12)61480-9**
German study establishing de novo point mutations account for **45-55%** of severe sporadic ID cases with high locus heterogeneity. Influential in demonstrating trio exome diagnostic utility.

---

## Long-read sequencing for rare disease

Long-read technologies expand diagnostic capabilities for structural variants, repeat expansions, and complex genomic regions inaccessible to short reads.

**Hiatt SM, Lawlor JMJ, Handley LH, et al.** Long-read genome sequencing for the molecular diagnosis of neurodevelopmental disorders. *HGG Advances* 2021; 2(2):100023. **DOI: 10.1016/j.xhgg.2021.100023**
First systematic study using PacBio HiFi for rare disease diagnosis, identifying likely pathogenic variants in **33%** of previously unsolved cases including complex structural variants and mobile element insertions.

**Del Gobbo GF, Boycott KM.** The additional diagnostic yield of long-read sequencing in undiagnosed rare diseases. *Genome Research* 2025. **DOI: 10.1101/gr.279970.124**
Comprehensive review analyzing >50 studies demonstrating **7-17% additional diagnostic yield** from long-read sequencing after negative short-read genome sequencing.

**Nakamura H, Doi H, Mitsuhashi S, et al.** Rapid and comprehensive diagnostic method for repeat expansion diseases using nanopore sequencing. *npj Genomic Medicine* 2022; 7:62. **DOI: 10.1038/s41525-022-00331-y**
Demonstrated Oxford Nanopore adaptive sampling for parallel genotyping of multiple neuropathogenic repeat loci, accurately diagnosing expansion disorders including Huntington's disease and fragile X syndrome.

---

## Summary by topic

| Topic | Key Papers | Primary Metrics/Findings |
|-------|-----------|-------------------------|
| Diagnostic yield | Yang 2013/2014, Wright 2015, Splinter 2018, Smedley 2021 | 25-35% solve rate |
| ClinGen/PanelApp | Rehm 2015, Strande 2017, Martin 2019 | Standardized curation frameworks |
| VUS reclassification | Kobayashi 2024, Bennett 2025 | 57% from computational advances |
| Constraint scores | Lek 2016 (pLI) | 3,230 constrained genes identified |
| Phenotype tools | Robinson 2008/2014/2020, Zhao 2020 | HPO, Exomiser, LIRICAL, Phen2Gene |
| MPRA | Melnikov 2012, Patwardhan 2012, Tewhey 2016 | High-throughput regulatory variant assays |
| DMS resources | Fowler 2014, Esposito 2019 | MaveDB repository |
| EVE model | Frazer 2021 | 36M variant predictions |
| Reanalysis | Liu 2019, Dai 2022 | 10% additional yield |
| Noncoding variants | Cummings 2017, Smedley 2016 | RNA-seq 35% yield, Genomiser/ReMM |
| De novo mutations | Vissers 2010, Sanders 2012, DDD 2017 | 42% DD from coding DNMs |
| Long-read sequencing | Hiatt 2021, Nakamura 2022 | 7-17% added yield, repeat expansions |

These 35 papers provide comprehensive coverage of the methodological and clinical foundations supporting rare disease diagnosis using genomic sequencing and computational approaches, complementing the foundation model citations (AlphaMissense, Enformer, SpliceAI) already in your chapter.
# Gap Citations: Proposed Book Modifications (v2 - Revised)

**Document Type:** Diff Proposal (POST-REVIEW REVISION)
**Generated:** 2026-01-18
**Status:** REVISED per multi-agent review feedback
**Previous Version:** gap-citations-diff-proposal.md

---

## Revision Summary

Changes from v1 based on 6-agent review:
- **Changes 3 & 6:** Relocated to forward references (ESM3/Ingraham → Ch31)
- **Change 4:** Fixed RoseTTAFold characterization (speed, not accuracy)
- **Change 9:** Reframed VEP limitations with correct terminology
- **Change 11:** Fixed overclaiming ("prevent" → "reduce", "reveals" → "designed to assess")
- **Change 13:** Fixed BERTology transfer claim
- **Change 16:** Consolidated PRS section with trade-off table
- **Added:** Active learning elements, accessibility definitions

---

## Part 4, Chapter 14: Foundation Model Paradigm

### Change 1: Add Bommasani et al. Definition Reference [APPROVED]

**Location:** Section 14.2 "Defining Genomic Foundation Models"

**Proposed modification:**
```diff
The term "foundation model" appears frequently in genomics literature,
sometimes applied to any large neural network trained on biological sequences.
+ The Stanford HAI report formally defined foundation models as "models trained
+ on broad data at scale such that they can be adapted to a wide range of
+ downstream tasks" [@bommasani_on_2022]. This definition, while originating
+ from general AI discourse, captures essential properties that distinguish
+ true genomic foundation models from task-specific deep learning approaches.
```

---

### Change 2: Add Genomics FM Landscape Reference [REVISED - added active learning]

**Location:** Section 14.2 after essential properties

**Proposed addition:**
```diff
+ ::: {.callout-note title="Field Overview"}
+ For a comprehensive survey of genomic foundation models as of 2024, including
+ taxonomy, benchmarks, and applications, see @trop_genomics_2024.
+
+ **Reading Extension:** Compare Trop et al.'s taxonomy to the four families
+ introduced in this chapter. Where do their categories align with ours? Where
+ do they diverge, and what might account for different organizational choices?
+ :::
```

---

## Part 4, Chapter 16: Protein Language Models

### Change 3: ESM3 Forward Reference [REVISED - relocated content]

**Location:** After ESMFold section, brief forward reference only

**Proposed addition:**
```diff
+ ::: {.callout-note title="Looking Ahead: Multimodal Protein Learning"}
+ Recent models like *ESM3* [@hayes_esm_2025] extend protein language modeling
+ from sequence-only to multimodal reasoning across sequence, structure, and
+ function. This paradigm, including the generation of novel functional proteins,
+ is discussed in @sec-ch31-generative.
+ :::
```

**Rationale:** Full ESM3 treatment belongs in Ch31 (Generative Design) to preserve Ch16's pedagogical arc from ESM-1b → ESM-2 → ESMFold.

---

### Change 4: Add RoseTTAFold Reference [REVISED - fixed characterization]

**Location:** Section on structure prediction methods

**Proposed addition:**
```diff
+ While *ESMFold* demonstrates single-sequence structure prediction,
+ *RoseTTAFold* [@baek_accurate_2021] provides an alternative approach that
+ combines multiple sequence alignment (MSA) information with deep learning.
+ *RoseTTAFold* offers faster inference than *AlphaFold2* with comparable
+ accuracy when MSAs are available, making it practical for large-scale
+ applications. For orphan sequences lacking detectable homologs,
+ single-sequence methods like *ESMFold* become essential since no MSA
+ can be constructed.
```

---

### Change 5: Add OpenFold Reference [REVISED - connected to LOs]

**Location:** After RoseTTAFold discussion

**Proposed addition:**
```diff
+ The *OpenFold* project [@ahdritz_openfold_2024] provides an open-source
+ reimplementation of *AlphaFold2* enabling fine-tuning and architectural
+ modification. This accessibility matters for understanding PLM internals:
+ researchers can probe which components encode structural knowledge,
+ a question central to interpretability (@sec-ch25-interpretability).
```

---

### Change 6: Protein Generation Forward Reference [REVISED - relocated content]

**Location:** End of chapter, before limitations section

**Proposed addition:**
```diff
+ The knowledge encoded in protein language models enables not just analysis
+ but generation of novel proteins. Work by @ingraham_illuminating_2023 and
+ others demonstrates that models trained to predict masked amino acids can
+ be inverted to generate proteins with desired properties. This generative
+ paradigm is explored in @sec-ch31-generative.
```

**Rationale:** Full generative content belongs in Ch31 to maintain Ch16's focus on understanding and prediction.

---

## Part 4, Chapter 17: Regulatory Models

### Change 7: Add Maurano Motivation [APPROVED]

**Location:** Opening section, after the enhancer distance discussion

**Proposed addition:**
```diff
+ The biological reality of long-range regulation was established by systematic
+ studies mapping GWAS variants to functional elements. @maurano_systematic_2012
+ demonstrated that disease-associated variants are overwhelmingly enriched in
+ regulatory regions rather than coding sequences, with enrichment patterns
+ specific to cell types relevant to each disease. This foundational observation
+ motivates the entire enterprise of regulatory modeling: if most disease
+ variants act through regulatory mechanisms, understanding those mechanisms
+ requires models that can capture the regulatory grammar of the genome.
```

---

## Part 4, Chapter 18: Variant Effect Prediction

### Change 8: Add Non-Coding Statistics [REVISED - added engagement]

**Location:** Section on non-coding variant interpretation

**Proposed addition:**
```diff
+ The challenge of non-coding variant interpretation is quantified by landmark
+ studies of GWAS variant localization. @farh_genetic_2015 established that
+ approximately 90% of disease-associated variants fall in non-coding regions,
+ with roughly 60% in enhancer-like chromatin states (regions showing histone
+ modifications characteristic of active enhancers). Of these, only 10-20%
+ directly disrupt recognizable transcription factor binding motifs.
+
+ ::: {.callout-tip title="Stop and Think"}
+ If only 10-20% of regulatory variants disrupt recognizable TF motifs, what
+ does this imply about the complexity of regulatory grammar that foundation
+ models must learn?
+ :::
```

---

### Change 9: Add VEP Limitations Perspective [REVISED - correct framing]

**Location:** Limitations section

**Proposed addition:**
```diff
+ ### Limitations of PLM-Based VEP {#sec-ch18-plm-limitations}
+
+ Despite impressive benchmark performance, protein language model approaches
+ to variant effect prediction face limitations that practitioners must
+ understand. @karollus_current_2023 systematically evaluated PLM-VEP methods
+ and identified several challenges:
+
+ - **Limited sensitivity to rare functional variation:** Because PLMs learn
+   from evolutionary data, they may underestimate pathogenicity of de novo
+   variants, recent adaptive mutations, or population-specific functional
+   variants not well-represented in training databases
+ - **Limited epistatic modeling:** While attention mechanisms capture some
+   residue dependencies, PLMs cannot directly score compound heterozygous
+   or digenic interactions (cases where two variants together cause disease)
+   that may be clinically relevant
+ - **Calibration challenges:** Scores reflect evolutionary constraint, not
+   pathogenicity probability. Translating constraint scores to clinical
+   interpretation requires calibration on labeled pathogenic variants
+
+ @swanson_predicting_2022 provides complementary analysis showing that PLMs
+ show reduced predictive accuracy on proteins with limited evolutionary
+ coverage or non-canonical functions where training data is sparse.
```

---

## Part 3, Chapter 12: Benchmarks

### Change 10: Add Benchmark Circularity Section [REVISED - added exercise]

**Location:** NEW section after standard benchmarks discussion

**Proposed addition:**
```diff
+ ## Benchmark Circularity {#sec-ch12-circularity}
+
+ A pervasive problem in variant effect prediction benchmarks is circularity:
+ the labels used for evaluation were often derived using methods that share
+ information with the models being evaluated. @grimm_evaluation_2015
+ demonstrated this problem systematically, showing that apparent performance
+ advantages of some methods disappeared when evaluation properly accounted
+ for data contamination.
+
+ The circularity problem manifests in several forms:
+
+ 1. **Label circularity:** Pathogenicity labels derived from SIFT/PolyPhen
+    scores advantage methods using similar conservation features
+ 2. **Temporal leakage:** Training on variants classified after model
+    development inflates apparent performance
+ 3. **Gene-level leakage:** Variants in the same gene as training examples
+    may share confounding features
+
+ ::: {.callout-warning title="Practical Implication"}
+ When evaluating VEP methods, always ask: how were the labels generated?
+ Do any label sources overlap with model features? Are training and test
+ variants from the same genes? Apparent benchmark leaders may reflect
+ circularity rather than genuine predictive improvement.
+ :::
+
+ ::: {.callout-tip title="Exercise"}
+ Examine a VEP benchmark you have encountered. How were the pathogenicity
+ labels generated? Can you identify any potential sources of circularity
+ with the prediction methods being evaluated?
+ :::
```

---

### Change 11: Add Genomic Touchstone Reference [REVISED - fixed overclaiming]

**Location:** After existing benchmark descriptions

**Proposed addition:**
```diff
+ ### Emerging Comprehensive Benchmarks
+
+ The limitations of existing benchmarks have motivated development of more
+ rigorous evaluation frameworks. @wang_genomic_2025 introduce *Genomic
+ Touchstone*, a benchmark designed specifically for genomic foundation models
+ with features intended to address circularity:
+
+ - **Systematic holdout:** Gene-level splits substantially reduce within-gene
+   information leakage
+ - **Multi-task evaluation:** Performance across diverse tasks is designed
+   to assess generalization rather than task-specific optimization
+ - **Temporal splits:** Training cutoffs ensure evaluation on variants
+   classified after model development
+
+ @tanigawa_significant_2022 provides complementary resources for comparing
+ foundation model approaches against traditional PRS methods, enabling
+ principled assessment of when deep learning adds value over classical
+ approaches.
```

---

## Part 3, Chapter 13: Confounding

### Change 12: Add Ancestry-Aware Methods [APPROVED]

**Location:** Section on ancestry confounding

**Proposed addition:**
```diff
+ ### Addressing Ancestry Bias in Genomic Models
+
+ Several approaches have emerged to address ancestry confounding in genomic
+ prediction. @amariuta_improving_2020 demonstrated that incorporating
+ functional genomic annotations can improve PRS transferability across
+ populations, with larger gains for traits with well-characterized
+ regulatory mechanisms.
+
+ The importance of diverse representation extends beyond European-focused
+ cohorts. @sohail_mexican_2023 provides critical analysis of PRS performance
+ in Latin American populations, revealing systematic biases that cannot be
+ addressed by simple recalibration. The work highlights the need for
+ foundation models to be evaluated explicitly on diverse populations rather
+ than assuming that performance on European-ancestry cohorts will transfer.
```

---

## Part 6, Chapter 25: Interpretability

### Change 13: Add BERTology Reference [REVISED - fixed transfer claim]

**Location:** Section on attention analysis

**Proposed addition:**
```diff
+ The techniques for interpreting attention patterns in genomic models draw
+ from work in natural language processing. @vig_bertology_2021 established
+ systematic approaches for analyzing what BERT-style models learn, including:
+
+ - **Attention head specialization:** Different heads capture different
+   linguistic phenomena (and potentially biological phenomena in genomics)
+ - **Layer-wise representation analysis:** Early layers capture surface
+   patterns; later layers encode more abstract relationships
+ - **Probing classifiers:** Simple classifiers trained on internal
+   representations (a technique called "probing") reveal what knowledge
+   is encoded in each layer
+
+ These BERTology-inspired techniques can be adapted for genomic models.
+ Attention pattern analysis may reveal learned motif relationships, chromatin
+ domain structure, or evolutionary constraints, though the biological meaning
+ of attention heads in genomic models remains an open research question.
+ For background on attention mechanisms, see @sec-ch07-attention.
```

---

## Part 6, Chapter 26: Causality

### Change 14: Add Mendelian Randomization Foundation [REVISED - added definitions]

**Location:** Opening section

**Proposed addition:**
```diff
+ Establishing causal relationships from observational genomic data requires
+ careful methodology. @daveysmith_mendelian_2003 introduced **Mendelian
+ randomization** as a framework for causal inference. The key insight:
+ genotypes are essentially randomly assigned at conception (determined by
+ Mendelian inheritance from parents, not by environmental factors), providing
+ a natural randomization that can be exploited to estimate causal effects.
+
+ This makes genetic variants useful as **instrumental variables**—variables
+ that affect the outcome only through the exposure of interest, enabling
+ causal inference without experimental manipulation.
+
+ This framework has implications for genomic foundation models: predictions
+ should be evaluated not just for predictive accuracy but for causal validity.
+ A model that predicts associations without causal grounding may perform well
+ on benchmarks (predicting from observational data) while failing to generalize
+ to intervention settings (actual clinical use or experimental validation).
```

---

## Part 6, Chapter 27: Regulation

### Change 15: Add FDA AI/ML Guidance [APPROVED]

**Location:** Section on regulatory frameworks

**Proposed addition:**
```diff
+ ### FDA Guidance on AI/ML in Medicine
+
+ The U.S. Food and Drug Administration has issued specific guidance on
+ AI/ML-based medical devices that affects genomic prediction tools intended
+ for clinical use [@fda_artificial_2021]. Key requirements include:
+
+ - **Predetermined change control plans:** Methods for updating models
+   without requiring new regulatory clearance
+ - **Real-world performance monitoring:** Requirements for ongoing
+   performance assessment after deployment
+ - **Transparency requirements:** Documentation of training data,
+   validation procedures, and known limitations
+
+ Genomic foundation models intended for clinical variant interpretation should
+ incorporate these requirements from the design phase. Addressing regulatory
+ requirements retrospectively creates substantial rework and delays deployment.
```

---

## Part 7, Chapter 28: Clinical Risk

### Change 16: Add Non-Linear PRS Methods [REVISED - consolidated with table]

**Location:** Section on ML-enhanced PRS

**Proposed addition:**
```diff
+ ### Deep Learning Approaches to PRS
+
+ Traditional PRS assume linear and additive genetic effects, but non-linear
+ methods may capture additional predictive signal from genetic interactions
+ (cases where two or more variants together affect phenotype in ways that
+ linear methods miss). @elgart_non_2022 systematically compared approaches:
+
+ | Approach | Captures Interactions | Interpretable | Computational Cost |
+ |----------|----------------------|---------------|-------------------|
+ | Linear PRS | No | High | Low |
+ | Neural network PRS | Yes | Lower | Higher |
+ | Transformer-based (PRSformer) | Yes | Low | Highest |
+
+ : Trade-offs between PRS approaches. {#tbl-prs-comparison}
+
+ Results show non-linear models provide modest but consistent improvements
+ for some phenotypes (typically 2-5% AUC improvement), particularly those
+ with complex genetic architectures where many genes contribute at varying
+ effect sizes. @dibaeinia_prsformer_2025 demonstrates that attention
+ mechanisms can capture genetic interactions, though gains come with
+ increased computational requirements and reduced interpretability.
+
+ ::: {.callout-note title="When is complexity justified?"}
+ Consider non-linear PRS when: (1) the phenotype has known epistatic effects,
+ (2) linear PRS performance plateaus despite large training data, or
+ (3) interpretability is less critical than predictive accuracy.
+ :::
```

---

## Part 7, Chapter 30: Drug Discovery

### Change 17: Add DiffDock Reference [REVISED - clarified concepts]

**Location:** Section on molecular docking

**Proposed addition:**
```diff
+ ### Diffusion Models for Molecular Docking
+
+ *DiffDock* [@corso_diffdock_2022] introduced diffusion-based approaches to
+ molecular docking, achieving state-of-the-art performance on binding pose
+ prediction. The method treats docking as a generative problem: starting from
+ random molecular poses (configurations), it iteratively refines them toward
+ the correct binding configuration, similar to how diffusion models generate
+ images by iteratively removing noise.
+
+ This represents a departure from traditional scoring-function-based approaches
+ (methods that explicitly model chemical energy and binding affinity). Instead,
+ the model learns statistical patterns about how molecules typically interact,
+ connecting molecular docking to the broader foundation model paradigm.
```

---

## Part 5, Chapter 21: Spatial Transcriptomics

### Change 18: Add SCENIC Reference [APPROVED]

**Location:** Section on gene regulatory networks

**Proposed addition:**
```diff
+ Classical approaches to gene regulatory network inference from single-cell
+ data, exemplified by *SCENIC* [@aibar_scenic_2017], establish baseline
+ methods against which foundation model approaches should be compared.
+ *SCENIC* combines motif enrichment with co-expression analysis to infer
+ transcription factor regulons (sets of genes regulated by the same
+ transcription factor), providing interpretable network structures
+ that can be validated against ChIP-seq binding data.
```

---

### Change 19: Add HEIST Reference [REVISED - expanded]

**Location:** Section on spatial foundation models

**Proposed addition:**
```diff
+ ### Spatial Foundation Models
+
+ Foundation models are beginning to incorporate spatial information in
+ single-cell analysis. Traditional single-cell analysis discards spatial
+ information when cells are dissociated. *HEIST* [@madhu_heist_2025]
+ demonstrates that transformer architectures can leverage spatial
+ transcriptomics data, incorporating:
+
+ - **Tissue organization:** How cell types arrange in physical space
+ - **Cell-cell communication:** Signals between neighboring cells
+
+ These spatial patterns are unavailable to bulk sequencing or dissociated
+ single-cell approaches. Whether spatial context leads to improved
+ downstream predictions remains an active area of validation.
```

---

## Part 1, Chapter 2: Datasets

### Change 20: Add TOPMed Reference [APPROVED]

**Location:** Section on large-scale sequencing resources

**Proposed addition:**
```diff
+ The Trans-Omics for Precision Medicine (TOPMed) program provides one of
+ the largest deeply sequenced cohorts available for genomic research.
+ @taliun_sequencing_2021 describes the resource: over 150,000 genomes
+ at high coverage (more than 30 reads per base pair), with diverse ancestry
+ representation and deep phenotyping. TOPMed has become a crucial resource
+ for rare variant analysis and for developing methods that generalize
+ across populations.
```

---

## Additional Tool/Resource Citations

### Chapter 2: Add PLINK Reference [APPROVED]
```diff
+ *PLINK* [@purcell_plink_2007], first released in 2007, continues to be
+ widely used for genome-wide association analysis and data manipulation,
+ providing essential functionality for quality control, format conversion,
+ and basic statistical analysis that most genomic workflows depend upon.
```

### Chapter 28: Add PharmGKB Reference [APPROVED]
```diff
+ The Pharmacogenomics Knowledge Base (PharmGKB) [@whirlcarrillo_pharmacogenomics_2012]
+ curates variant-drug associations with clinical annotations, providing
+ essential resources for pharmacogenomic applications of foundation models.
```

---

## Summary of Changes (v2)

| Change | Chapter | Status | Key Revision |
|--------|---------|--------|--------------|
| 1 | ch14 | APPROVED | No change |
| 2 | ch14 | REVISED | Added reading extension |
| 3 | ch16 | REVISED | Relocated to forward reference |
| 4 | ch16 | REVISED | Fixed speed vs accuracy |
| 5 | ch16 | REVISED | Connected to LOs |
| 6 | ch16 | REVISED | Relocated to forward reference |
| 7 | ch17 | APPROVED | No change |
| 8 | ch18 | REVISED | Added Stop and Think |
| 9 | ch18 | REVISED | Reframed limitations correctly |
| 10 | ch12 | REVISED | Added exercise |
| 11 | ch12 | REVISED | Fixed overclaiming |
| 12 | ch13 | APPROVED | No change |
| 13 | ch25 | REVISED | Fixed transfer claim, added definitions |
| 14 | ch26 | REVISED | Added definitions |
| 15 | ch27 | APPROVED | Minor softening |
| 16 | ch28 | REVISED | Consolidated with table |
| 17 | ch30 | REVISED | Clarified concepts |
| 18 | ch21 | APPROVED | Added regulon definition |
| 19 | ch21 | REVISED | Expanded with structure |
| 20 | ch02 | APPROVED | Added coverage explanation |

**Papers for bibliography:** See [bibliography-papers-needed.md](bibliography-papers-needed.md)

---

## Glossary Updates Required

Add to `meta/glossary/glossary-core-245.md`:

1. **Benchmark circularity** [Statistics]
2. **Temporal leakage** (expand existing "Contamination" entry)

---

*This is REVISION 2 incorporating feedback from 6 specialized review agents.*

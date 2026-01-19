# Gap Citations: Round 2 Proposal

**Document Type:** Diff Proposal
**Generated:** 2026-01-18
**Status:** DRAFT - For review
**Prerequisite:** Round 1 (v2) implemented

---

## Overview

This proposal covers:
1. **3 papers from v2 not yet implemented** (HEIST, DiffDock, Elgart)
2. **12 HIGH priority papers from routing manifest** deferred from Round 1

Total: ~15 papers across 10 chapters

---

## Part 1: Remaining v2 Papers

### Change R2-1: HEIST Spatial Foundation Models (Ch21)

**Location:** Section on spatial transcriptomics foundation models

**Proposed addition:**
```markdown
### Spatial Foundation Models {#sec-ch21-spatial-fm}

Foundation models are beginning to incorporate spatial information in
single-cell analysis. Traditional single-cell analysis discards spatial
information when cells are dissociated for sequencing. *HEIST*
[@madhu_heist_2025] demonstrates that transformer architectures can
leverage spatial transcriptomics data, learning:

- **Tissue organization:** How cell types arrange in physical space
- **Cell-cell communication:** Signals between neighboring cells
  based on spatial proximity

These spatial patterns are unavailable to bulk sequencing or dissociated
single-cell approaches. Whether spatial context leads to improved
downstream predictions remains an active area of validation.
```

---

### Change R2-2: DiffDock Molecular Docking (Ch30)

**Location:** Section on molecular docking (after Hie learned priors)

**Proposed addition:**
```markdown
### Diffusion Models for Molecular Docking {#sec-ch30-diffdock}

*DiffDock* [@corso_diffdock_2022] introduced diffusion-based approaches
to molecular docking, achieving state-of-the-art performance on binding
pose prediction. The method treats docking as a generative problem:
starting from random molecular poses (configurations), it iteratively
refines them toward the correct binding configuration, similar to how
image diffusion models generate images by iteratively removing noise.

This represents a departure from traditional scoring-function-based
approaches (methods that explicitly model chemical energy and binding
affinity). Instead, the model learns statistical patterns about how
molecules typically interact, connecting molecular docking to the
broader foundation model paradigm of learned priors discussed above.
```

---

### Change R2-3: Elgart Non-Linear PRS Comparison (Ch28)

**Location:** After PRSformer section, expand comparison

**Proposed modification:**
```markdown
@elgart_non_2022 systematically compared linear and non-linear PRS
approaches across multiple phenotypes, finding that non-linear models
provide modest but consistent improvements (typically 2-5% AUC gain)
for phenotypes with complex genetic architectures. The comparison
established important baselines: improvements from deep learning must
exceed well-tuned linear methods to justify increased complexity.
```

---

## Part 2: Deferred HIGH Priority Papers

### Change R2-4: GNN Foundations (Ch06)

**Location:** Section on graph neural networks

**Proposed addition:**
```markdown
Graph neural networks extend deep learning to non-Euclidean data where
relationships between entities matter as much as entity features.
@kipf_semi_2017 introduced spectral graph convolutions that aggregate
information from neighboring nodes, enabling models that respect graph
structure. In genomics, GNNs model protein-protein interaction networks,
gene regulatory networks, and molecular graphs (@sec-ch22-networks).
```

---

### Change R2-5: SimCLR Contrastive Learning (Ch08)

**Location:** Section on contrastive pretraining objectives

**Proposed addition:**
```markdown
Contrastive learning provides an alternative to masked prediction for
self-supervised pretraining. @chen_simple_2020 demonstrated with SimCLR
that learning to distinguish positive pairs (augmented views of the same
example) from negative pairs (different examples) produces representations
that transfer effectively to downstream tasks. In genomics, contrastive
objectives appear in multi-modal learning (@sec-ch23-multiomics) where
the same biological entity measured by different technologies provides
natural positive pairs.
```

---

### Change R2-6: PheWAS Methodology (Ch03)

**Location:** Section on phenome-wide studies

**Proposed addition:**
```markdown
While GWAS tests genetic variants against a single phenotype,
**phenome-wide association studies (PheWAS)** invert this design:
testing a single variant against thousands of phenotypes simultaneously.
@denny_phewas_2010 established the methodology using electronic health
record data, revealing that variants often affect multiple traits
(pleiotropy). This approach identifies unexpected phenotype connections
and informs whether foundation model predictions generalize across
the phenome or remain trait-specific.
```

---

### Change R2-7: Pharmacogenomics Ancestry (Ch13)

**Location:** Section on ancestry in clinical applications

**Proposed addition:**
```markdown
Ancestry effects in pharmacogenomics illustrate how population structure
affects clinical utility. @chung_marker_2004 demonstrated that CYP2D6
metabolizer phenotypes vary substantially across populations, with
allele frequencies differing by orders of magnitude between African,
Asian, and European ancestry groups. Foundation models for drug response
prediction must account for these population-specific patterns or risk
systematic errors in underrepresented groups.
```

---

### Change R2-8: Nucleotide Transformer v3 (Ch15)

**Location:** Section on NT model family

**Proposed addition:**
```markdown
The Nucleotide Transformer family has evolved through multiple versions.
@boshar_foundational_2024 describe architectural improvements in recent
iterations, including expanded context windows and improved tokenization
strategies. These updates demonstrate how DNA language models continue
to mature, with each generation addressing limitations identified in
prior versions.
```

---

### Change R2-9: PoET Evolutionary Methods (Ch16)

**Location:** Section on evolutionary protein methods

**Proposed addition:**
```markdown
*PoET* [@jr_poet_2023] takes an alternative approach to protein
language modeling by explicitly modeling evolutionary trajectories
rather than treating sequences as independent samples. The method
learns from multiple sequence alignments directly, capturing how
proteins evolve over time. This evolutionary framing provides
complementary signal to single-sequence PLMs like ESM-2.
```

---

### Change R2-10: Tranception Retrieval VEP (Ch18)

**Location:** Section on retrieval-augmented VEP

**Proposed addition:**
```markdown
### Retrieval-Augmented Variant Prediction {#sec-ch18-retrieval-vep}

*Tranception* [@notin_tranception_2022] demonstrates that retrieval
augmentation can improve variant effect prediction. Rather than relying
solely on learned parameters, the model retrieves evolutionarily related
sequences at inference time, providing context-specific information
about which positions tolerate variation. This approach bridges
classical MSA-based methods and modern language models, potentially
offering the best of both paradigms.
```

---

### Change R2-11: Primate Constraint Evidence (Ch18)

**Location:** Section on evolutionary evidence for VEP

**Proposed addition:**
```markdown
@gao_landscape_2023 provides large-scale primate constraint data that
complements traditional cross-species conservation. Because primates
are evolutionarily close to humans, variants tolerated in primate
genomes provide stronger evidence of benignity than variants tolerated
only in distant species. This primate-specific constraint signal
can calibrate PLM-based VEP predictions.
```

---

### Change R2-12: GPT4Mol Multi-Modal (Ch23)

**Location:** Section on unified molecular representations

**Proposed addition:**
```markdown
*GPT4Mol* [@zhu_gpt_2024] demonstrates unified language modeling across
molecular modalities, treating SMILES strings (chemical structures),
protein sequences, and genomic sequences within a single architecture.
This multi-modal approach enables cross-domain transfer: knowledge
learned from chemical structures can inform predictions about
protein-ligand interactions relevant to drug discovery (@sec-ch30).
```

---

### Change R2-13: REGLE Phenotype Embeddings (Ch28)

**Location:** Section on deep phenotyping

**Proposed addition:**
```markdown
Beyond genetic embeddings, phenotype representations can improve
prediction. @yun_regle_2023 introduce REGLE, which learns embeddings
of phenotypes from their genetic architecture. Phenotypes with similar
genetic bases cluster in embedding space, enabling transfer learning
across related traits and improving prediction for phenotypes with
limited training data.
```

---

### Change R2-14: Scientific LLMs (Ch32)

**Location:** Section on frontier directions

**Proposed addition:**
```markdown
Large language models trained on scientific text provide complementary
capabilities to sequence-based foundation models. @zhang_scientific_2024
survey scientific LLMs that can retrieve literature, answer domain
questions, and assist with experimental design. Integration of
scientific LLMs with genomic foundation models represents a frontier
where natural language understanding meets biological sequence analysis.
```

---

### Change R2-15: GFP Fitness Benchmark (Ch12)

**Location:** Section on protein benchmarks

**Proposed addition:**
```markdown
Deep mutational scanning of green fluorescent protein (GFP) provides
a gold-standard benchmark for variant effect prediction.
@sarkisyan_local_2016 systematically measured fitness effects of
thousands of GFP variants, creating a dense landscape that tests
whether models capture epistatic interactions between mutations.
The dataset remains a key benchmark in ProteinGym and related
evaluation suites.
```

---

## Summary

| Change | Chapter | Paper | Priority | Status |
|--------|---------|-------|----------|--------|
| R2-1 | ch21 | madhu_heist_2025 | v2 remaining | ✅ Implemented (revised) |
| R2-2 | ch30 | corso_diffdock_2022 | v2 remaining | ✅ Implemented (revised) |
| R2-3 | ch28 | elgart_non_2022 | v2 remaining | ✅ Implemented |
| R2-4 | **ch22** | kipf_semi_2017 | HIGH deferred | ✅ Implemented (moved from ch06) |
| R2-5 | ch08 | chen_simple_2020 | HIGH deferred | ✅ Implemented (revised) |
| R2-6 | ch03 | denny_phewas_2010 | HIGH deferred | ✅ Implemented |
| R2-7 | ch13 | chung_marker_2004 | HIGH deferred | ✅ Implemented (revised) |
| R2-8 | ch15 | boshar_foundational_2024 | HIGH deferred | ✅ Implemented (revised) |
| R2-9 | ch16 | jr_poet_2023 | HIGH deferred | ✅ Implemented (revised) |
| R2-10 | ch18 | notin_tranception_2022 | HIGH deferred | ✅ Implemented (revised) |
| R2-11 | ch18 | gao_landscape_2023 | HIGH deferred | ✅ Implemented (revised) |
| R2-12 | ch23 | zhu_gpt_2024 | HIGH deferred | ❌ SKIPPED (unverifiable) |
| R2-13 | ch28 | yun_regle_2023 | HIGH deferred | ✅ Implemented (revised) |
| R2-14 | ch32 | zhang_scientific_2024 | HIGH deferred | ✅ Implemented (revised) |
| R2-15 | ch12 | sarkisyan_local_2016 | Tool citation | ✅ Implemented |

---

## Papers for Bibliography (14 total)

```
madhu_heist_2025
corso_diffdock_2022
elgart_non_2022
kipf_semi_2017
chen_simple_2020
denny_phewas_2010
chung_marker_2004
boshar_foundational_2024
jr_poet_2023
notin_tranception_2022
gao_landscape_2023
yun_regle_2023
zhang_scientific_2024
sarkisyan_local_2016
```

**Removed:** `zhu_gpt_2024` (GPT4Mol) - paper unverifiable per domain accuracy review

---

## Implementation Notes

1. ✅ All citations use `_PLACEHOLDER` suffix pending Zotero export
2. Several papers require publication verification (2024-2025 dates)
3. ✅ Ch21 HEIST: Integrated into existing spatial models section
4. ✅ Ch32 Scientific LLMs: Added after agentic systems section
5. **R2-4 relocated:** GNN (Kipf) moved from ch06 to ch22 per pedagogy review
6. **R2-12 skipped:** GPT4Mol paper not verifiable per domain accuracy review

---

## Implementation Summary (2026-01-18)

**Implemented:** 14 of 15 changes
**Skipped:** 1 (R2-12 GPT4Mol - unverifiable paper)

**Key revisions based on review agent feedback:**
- R2-1 (HEIST): Corrected architecture to "hierarchical graph transformer"
- R2-2 (DiffDock): Changed "state-of-the-art" to "competitive performance"
- R2-4 (Kipf): Relocated to Ch22 (networks) instead of Ch06 (CNNs)
- R2-9 (PoET): Reframed as "sequences-of-sequences" not "evolutionary trajectories"
- R2-11 (Primate): Softened "stronger evidence" to "may provide more relevant evidence"
- R2-13 (REGLE): Corrected to "clinical data embeddings" (spirograms, ECGs)
- R2-14 (Scientific LLMs): Added caveat about accuracy variance

---

*Round 2 implementation complete. 14 papers added across 11 chapters.*

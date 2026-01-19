# Book-Literature Gap Analysis Report

**Generated:** 2026-01-18
**Method:** Cross-reference of science-paper-critic routing manifests vs book bibliography

## Executive Summary

| Metric | Count |
|--------|-------|
| Papers routed to book (HIGH priority) | 233 |
| Citation keys in `references.bib` | 382 |
| **Gaps** (routed but not cited) | 62 |
| LOW priority papers in book | 10 |
| MEDIUM priority papers in book | 111 |
| Foundational papers to keep | 50 |

---

## Part 1: GAPS - Papers That Should Be Added

These 62 papers were evaluated as HIGH priority for the book but are not currently cited.

### Critical Additions (Score ≥9.5)

| Paper | Score | Year | Recommended Action |
|-------|-------|------|-------------------|
| `maurano_systematic_2012` | 10.0 | pre-2015 | Key motivation for regulatory models chapter |
| `bommasani_on_2022` | 10.0 | 2022 | Key citation for Chapter 14 (FM Principles) |
| `grimm_evaluation_2015` | 9.5 | 2015 | Key citation in ch12 (Benchmarks) - VEP circularity |
| `outeiral_codon_2024` | 9.5 | 2024 | Key citation for codon FM paradigm (CaLM) |
| `wang_genomic_2025` | 9.5 | 2025 | Update ch12 with Genomic Touchstone benchmark |
| `hayes_esm_2025` | 9.5 | 2025 | Major update to ch16; esmGFP in ch32 protein design |

### High Priority Additions (Score 9.0)

| Paper | Year | Topic |
|-------|------|-------|
| `daveysmith_mendelian_2003` | pre-2015 | Causality chapter foundation |
| `purcell_plink_2007` | pre-2015 | Key tool citation for data chapters |
| `whirlcarrillo_pharmacogenomics_2012` | pre-2015 | Clinical applications |
| `farh_genetic_2015` | 2015 | Non-coding variant statistics (90%/60%/10-20%) |
| `sarkisyan_local_2016` | 2016 | Protein LM and benchmarking |
| `kipf_semi_2017` | 2017 | Foundational GNN citation (p2-ch06) |
| `eraslan_deep_2019` | 2019 | Architecture and evaluation chapters |
| `amariuta_improving_2020` | 2020 | Fairness and ancestry chapters |
| `chen_simple_2020` | 2020 | Pretraining chapter (SimCLR) |
| `dey_evaluating_2020` | 2020 | Evaluation methodology chapter |
| `vig_bertology_2021` | 2021 | Chapter 25 (Interpretability) |
| `fda_artificial_2021` | 2021 | Chapter 27 (Regulation) |
| `elgart_non_2022` | 2022 | Fairness chapter - non-linear PRS |
| `notin_tranception_2022` | 2022 | VEP chapter |
| `ingraham_illuminating_2023` | 2023 | Protein generative models (ch16, ch31) |
| `karollus_current_2023` | 2023 | Model limitations evaluation |
| `trop_genomics_2024` | 2024 | FM introduction - field overview |

### Additional HIGH Priority Gaps (Score 8.0-8.9)

- `denny_phewas_2010` - GWAS/biobank chapter
- `chung_marker_2004` - PGx and ancestry
- `aibar_scenic_2017` - GRN inference (p5-ch21)
- `taliun_sequencing_2021` - Chapter 2 (Data)
- `baek_accurate_2021` - RoseTTAFold
- `swanson_predicting_2022` - PLM limitations perspective
- `tanigawa_significant_2022` - GFM vs PRS comparison
- `gao_landscape_2023` - Primate evidence
- `jr_poet_2023` - Protein LM chapter
- `sohail_mexican_2023` - Ancestry/fairness chapters
- `ahdritz_openfold_2024` - Chapter 16 protein structure
- `zhang_scientific_2024` - Scientific LLM overview
- `zhu_gpt_2024` - Unified molecular modeling
- `corso_diffdock_2022` - Chapter 30/31 (Drug Discovery/Generative)
- `consens_transformers_2023` - Landscape overview
- `jagota_cross_2023` - DMS transfer
- `yun_regle_2023` - Clinical genomics
- `boshar_foundational_2024` - NT v3 update (Chapter 15)
- `cornman_glm_2024` - Mixed-modality embeddings
- `madhu_heist_2025` - Spatial transcriptomics FM
- `dibaeinia_prsformer_2025` - Clinical risk prediction

---

## Part 2: REMOVAL CANDIDATES - Low Priority Papers Currently in Book

These 10 papers received LOW priority during triage but are currently cited. **Review for potential removal** unless they provide essential historical context.

### True Removal Candidates (Non-Foundational)

| Paper | Year | Notes |
|-------|------|-------|
| `liu_life-code_2025` | 2025 | Recent, probably not foundational |
| `yu_assessing_2024` | 2024 | Recent, specific application |
| `zhu_deep_2019` | 2019 | Review for relevance |
| `steinegger_protein-level_2019` | 2019 | MMseqs2 - **may need to keep** (clustering methods) |

### Review Before Removal (May Need Historical Context)

| Paper | Year | Notes |
|-------|------|-------|
| `lee_biobert_2019` | 2019 | BioBERT - domain adaptation example (MEDIUM triage) |
| `loh_reference-based_2016` | 2016 | Reference-based phasing - foundational for phasing chapter |
| `benner_finemap_2016` | 2016 | FINEMAP - important for GWAS fine-mapping discussion |
| `gudbjartsson_sequence_2015` | 2015 | Sequencing methods - may be historical context |
| `li_towards_2014` | pre-2015 | May provide historical context |

### Key Observations

1. **ESM-2 (`lin_esm-2_2022`)** appears in this list due to key naming mismatch, but IS correctly cited and is HIGH priority. No action needed.

2. Several "LOW priority" papers may actually be legitimate supporting citations:
   - `steinegger_protein-level_2019` - MMseqs2 for redundancy removal
   - `benner_finemap_2016` - Important GWAS fine-mapping method
   - `loh_reference-based_2016` - Reference-based phasing

---

## Part 3: MEDIUM Priority Papers to Review

111 papers marked as MEDIUM priority during triage are currently in the book. These are not removal candidates but could be reviewed for potential trimming if the book becomes too long.

### Categories of MEDIUM Priority Papers

1. **Tool/Resource Papers** (legitimate supporting citations):
   - Database resources (UniProt, STRING, BioGRID)
   - Method tools (SMOTE, calibration methods)
   - Standards (GENCODE, ClinGen)

2. **Domain Adaptation Examples** (valuable context):
   - BioBERT, domain-specific models
   - Cross-domain transfer papers

3. **Supporting Methods** (review case-by-case):
   - Statistical methods
   - Evaluation frameworks
   - Architecture variants

### Recommendation

Do NOT mass-remove MEDIUM priority papers. Instead:
1. Review individual citations in context
2. Keep tool/resource papers as supporting citations
3. Consider consolidating redundant method citations

---

## Part 4: Foundational Papers to KEEP

These 50 papers (pre-2017, HIGH priority) provide essential historical context and should NOT be removed:

### Must-Keep Foundational Papers (Score 10.0)

| Paper | Year | Topic |
|-------|------|-------|
| `lander_initial_2001` | 2001 | Human genome - historical intro |
| `manolio_finding_2009` | 2009 | Missing heritability - motivation |
| `visscher_heritability_2008` | 2008 | Heritability concepts |
| `yang_common_2010` | 2010 | Missing heritability resolution |
| `price_principal_2006` | 2006 | Ancestry confounding (PCA) |
| `kircher_general_2014` | 2014 | CADD - classical VEP |
| `maurano_systematic_2012` | 2012 | Regulatory variant enrichment |

### Key Method Papers (Score 9.0-9.5)

- `ng_sift_2003` - SIFT conservation paradigm
- `adzhubei_method_2010` - PolyPhen method
- `hochreiter_long_1997` - LSTM architecture
- `henikoff_amino_1992` - BLOSUM matrices
- `berman_protein_2000` - PDB resource
- `breiman_statistical_2001` - Methodology philosophy
- `fowler_deep_2014` - DMS benchmark

---

## Action Items

### Immediate (Before Next Book Revision)

1. **Add 6 critical citations** (Score ≥9.5 gaps)
2. **Review 10 LOW priority papers** for removal
3. **Add foundational paper `maurano_systematic_2012`** - missing key motivation

### Medium Term

1. Add remaining 56 HIGH priority gap citations
2. Review MEDIUM priority papers during chapter edits
3. Update routing manifests as new citations are added

### Ongoing

1. Re-run gap analysis after major book updates
2. Update triage results when papers are added
3. Maintain consistent citation key naming convention

---

## Script Location

The analysis was performed using:
```
/root/gfm-literature/papers/scripts/gap_analysis.py
```

Re-run with:
```bash
cd /root/gfm-literature/papers && python3 scripts/gap_analysis.py
```

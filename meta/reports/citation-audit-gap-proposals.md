# Citation Audit: Gap Citations Diff Proposal

**Document:** `/root/gfm-book/meta/reports/gap-citations-diff-proposal.md`
**Audit Date:** 2026-01-18
**Auditor:** Citation-Needs-Detector
**Status:** CRITICAL ISSUES IDENTIFIED

---

## Executive Summary

The proposed changes introduce **27 papers** into the textbook, with the following audit results:

| Category | Count | Status |
|----------|-------|--------|
| **Critical Issues** | 3 | Unsupported claims about paper contributions |
| **Bibliography Integration** | 27 | ALL papers missing from `references.bib` |
| **Claim Coverage** | 20 | Appropriate citations for factual/statistical claims |
| **Potential Over-Citation** | 2 | Consider whether necessary |
| **Verification Required** | 5 | Claims about paper content need verification |

**Verdict:** The proposal CORRECTLY identifies claims needing citations, but introduces significant execution risks:
1. **All proposed papers lack BibTeX entries** - bibliography must be updated first
2. **Some paper characterizations need verification** - especially 2025 papers
3. **A few claims remain unsupported even with proposed citations**

---

## CRITICAL: Bibliography Integration Issue

### Finding 1: All 27 Proposed Papers Missing from `references.bib`

**Impact:** HIGH - Blocking issue for implementation

Current bibliography has **395 entries**, but ALL 27 proposed papers are absent:

```
Missing papers:
✗ bommasani_on_2022          (Foundation Model definition)
✗ trop_genomics_2024         (FM Landscape)
✗ hayes_esm_2025             (ESM3 multimodal protein)
✗ baek_accurate_2021         (RoseTTAFold)
✗ ahdritz_openfold_2024      (OpenFold)
✗ ingraham_illuminating_2023 (Generative protein design)
✗ maurano_systematic_2012    (Disease variant enrichment)
✗ farh_genetic_2015          (Non-coding variants)
✗ karollus_current_2023      (PLM-VEP limitations)
✗ swanson_predicting_2022    (PLM performance gaps)
✗ notin_tranception_2022     (Tranception methods)
✗ grimm_evaluation_2015      (Benchmark circularity)
✗ wang_genomic_2025          (Genomic Touchstone)
✗ tanigawa_significant_2022  (Foundation model vs PRS)
✗ amariuta_improving_2020    (PRS transferability)
✗ sohail_mexican_2023        (Latin American PRS bias)
✗ vig_bertology_2021         (BERTology interpretability)
✗ daveysmith_mendelian_2003  (Mendelian randomization)
✗ fda_artificial_2021        (FDA AI/ML guidance)
✗ elgart_non_2022            (Non-linear PRS)
✗ dibaeinia_prsformer_2025   (PRS transformers)
✗ yun_regle_2023             (Phenotype embeddings)
✗ corso_diffdock_2022        (DiffDock molecular docking)
✗ aibar_scenic_2017          (SCENIC GRN inference)
✗ madhu_heist_2025           (Spatial foundation models)
✗ taliun_sequencing_2021     (TOPMed dataset)
✗ purcell_plink_2007         (PLINK tool)
```

**Required Action:** Before implementing ANY changes, the bibliography must be updated with complete BibTeX entries for all 27 papers. Currently, all proposed citations will generate compilation errors.

---

## CRITICAL: Unsupported Claims (Even With Proposed Additions)

### Claim 1: ESM3 Functional Capability (Ch. 16, Change 3)

**Text:**
> "the model generated a fluorescent protein with only ~60% sequence identity to any known GFP, yet it folded correctly and exhibited fluorescence. This demonstrates that protein language models can extrapolate beyond their training distribution to discover novel functional solutions"

**Issues:**
1. **Exaggerated causality claim** - Cites Hayes et al. (2025) but the citation alone doesn't fully support "demonstrates novel functional solutions" without discussion of validation methodology
2. **Missing experimental validation detail** - How was fluorescence verified? In vitro? In vivo?
3. **Generalization claim unsupported** - Single example doesn't warrant "demonstrates capability"

**Suggested Addition:**
Include mention of experimental validation methodology: "This demonstrates protein design capability, validated through in vitro fluorescence assays [cite validation protocol/results]"

---

### Claim 2: Benchmark Circularity (Ch. 12, Change 10)

**Text:**
> "Grimm et al. (2015) demonstrated this problem systematically, showing that apparent performance advantages of some methods disappeared when evaluation accounted for data contamination."

**Issues:**
1. **Circularity claim itself is meta-claim** - The text claims Grimm demonstrated a problem, but no citation confirms HOW MANY methods lost advantages or by what magnitude
2. **No supporting evidence for severity** - Did all methods lose advantages? Some? The claim "apparent performance advantages... disappeared" is strong language needing quantitative backing

**Suggested Modification:**
> "Grimm et al. (2015) demonstrated this problem systematically, showing that [specific % of methods / example methods] had apparent performance advantages disappear when accounting for data contamination."

---

### Claim 3: FDA Guidance Applicability (Ch. 27, Change 15)

**Text:**
> "Genomic foundation models intended for clinical variant interpretation must consider these requirements from the design phase"

**Issues:**
1. **Normative claim without evidence** - The text asserts what models "must" consider, but doesn't cite any literature showing this is standard practice or requirement
2. **FDA guidance citation alone insufficient** - FDA guidance exists, but separate evidence needed for applicability to genomic FMs

**Suggested Addition:**
> "Genomic foundation models intended for clinical variant interpretation should consider these requirements from the design phase. Recent FDA guidance [@fda_artificial_2021] and domain analyses [NEEDS CITATION: genomic FM clinical deployment papers] indicate these are emerging standards."

---

## HIGH PRIORITY: Claims Needing Citation Verification

### Finding 2: Papers Not Yet Independently Verified (2025 Publications)

Three papers with 2025 publication dates appear in the proposal but may have verification issues:

| Paper | Issue | Action |
|-------|-------|--------|
| `hayes_esm_2025` | Recent publication; verify ESM3 results independently | Cross-check with Nature/bioRxiv version |
| `wang_genomic_2025` | "Genomic Touchstone" - verify this benchmark exists & is released | Check if peer-reviewed or preprint |
| `dibaeinia_prsformer_2025` | PRS transformer architecture - verify performance claims | Check experimental protocols |
| `madhu_heist_2025` | HEIST spatial models - verify implementation availability | Check if code/model released |

**Suggestion:** Flag 2025 papers for verification before citation. Consider noting preprint status in text.

---

## APPROPRIATE CITATIONS (Well-Supported Claims)

The following proposed additions correctly identify claims needing citations:

### Category A: Foundational Definitions (ESSENTIAL)

| Paper | Claim | Assessment |
|-------|-------|-----------|
| `bommasani_on_2022` | Defining "foundation model" | CRITICAL - Seminal definition paper |
| `trop_genomics_2024` | Genomic FM landscape/survey | ESSENTIAL - Field overview |
| `daveysmith_mendelian_2003` | Mendelian randomization framework | CRITICAL - Foundational methodology |

**Status:** Well-motivated. These claims require citations for conceptual grounding.

---

### Category B: Historical/Chronological Claims (HIGH PRIORITY)

| Paper | Claim | Assessment |
|-------|-------|-----------|
| `maurano_systematic_2012` | GWAS variants enriched in regulatory regions | IMPORTANT - Motivates regulatory modeling |
| `farh_genetic_2015` | 90% disease variants non-coding; 60% in enhancers | STATISTICAL - Needs source |
| `baek_accurate_2021` | RoseTTAFold structure prediction | LEGITIMATE - Adds context to ESM-2 discussion |
| `aibar_scenic_2017` | SCENIC as baseline GRN method | APPROPRIATE - Historical context |

**Status:** Appropriately cited. Statistical claims paired with sources.

---

### Category C: Methodological/Technical Context (APPROPRIATE)

| Paper | Claim | Assessment |
|-------|-------|-----------|
| `karollus_current_2023` | PLM-VEP limitations (conservation bias, epistasis) | CRITICAL - Counterbalances positive framing |
| `swanson_predicting_2022` | PLM performance gaps on orphan sequences | IMPORTANT - Practical limitations |
| `grimm_evaluation_2015` | Benchmark circularity problems | IMPORTANT - Meta-scientific concern |
| `tanigawa_significant_2022` | When deep learning adds value over PRS | HELPFUL - Comparative framing |

**Status:** Well-chosen. These add nuance and critical perspective.

---

### Category D: Tool/Resource References (APPROPRIATE)

| Paper | Claim | Assessment |
|-------|-------|-----------|
| `purcell_plink_2007` | PLINK standard tool for GWAS | STANDARD - Tool reference |
| `taliun_sequencing_2021` | TOPMed resource description | RESOURCE - Dataset reference |

**Status:** Standard practices for tool/resource citations.

---

## MEDIUM PRIORITY: Potential Over-Citation

### Finding 3: BERTology Transfer (Ch. 25, Change 13)

**Text:**
> "These 'BERTology' techniques translate directly to genomic models..."

**Assessment:** Citation to `vig_bertology_2021` is appropriate for NLP background, but **redundant with existing coverage**. Genome models section likely already cites attention interpretation papers. Consider:

- **Keep if:** BERTology has NOT been mentioned elsewhere in book
- **Remove if:** Chapter 25 or earlier chapters already discuss attention analysis techniques

**Recommendation:** Check `meta/qmd_headings.md` for existing attention interpretation sections before adding this citation.

---

### Finding 4: Mendelian Randomization (Ch. 26, Change 14)

**Text:**
> "genotypes are assigned randomly at conception (conditional on parental genotypes)"

**Assessment:** This is a **well-established concept** (30+ years old). Citation to `daveysmith_mendelian_2003` is appropriate for historical grounding, but the conceptual point may be over-cited for a textbook audience already familiar with genetics.

**Recommendation:** KEEP citation (essential for genomic FM context) but consider whether explanation needs shortening - the intuition is simple, just needs one exemplar paper.

---

## MISSING CITATIONS (Claims Still Unsupported)

### Finding 5: Comparative Performance Claims

**Location:** Ch. 28, Change 16 (PRS deep learning)

**Text:**
> "non-linear models provide modest but consistent improvements for some phenotypes, particularly those with complex genetic architectures"

**Issues:**
1. `elgart_non_2022` provides systematic comparison
2. But "complex genetic architectures" is undefined - which phenotypes?
3. "Modest but consistent" is vague - what magnitude of improvement?

**Suggested Addition:**
Quantify: "improvements of X-Y% for phenotypes with [specific architecture characteristic], particularly visible for [example phenotypes]"

---

### Finding 6: FDA Guidance Scope

**Location:** Ch. 27, Change 15

**Text:**
> "predetermined change control plans", "real-world performance monitoring"

**Issue:** These are FDA requirements, but **no evidence given** that genomic FM developers are actually implementing these or that they're clinically relevant yet.

**Suggested Addition:**
> "These emerging regulatory requirements [@fda_artificial_2021] are beginning to shape genomic FM development, though clinical deployment of deep learning-based variant interpreters remains limited to specialized research settings [CITE: DeepRare clinical trial, etc.]"

---

## VERIFICATION CHECKLIST FOR IMPLEMENTATION

Before implementing the proposed changes, verify:

- [ ] **Bibliography Updated:** All 27 papers added to `references.bib` with complete BibTeX entries
- [ ] **2025 Papers Verified:** Cross-check Hayes, Wang, Dibaeinia, Madhu papers against published versions
- [ ] **Claim Accuracy:** Verify paper characterizations (esp. performance numbers, mechanisms)
- [ ] **Cross-References:** Check proposed additions don't duplicate existing citations elsewhere in book
- [ ] **Terminology:** Confirm paper names match bibliography keys exactly (case-sensitive)
- [ ] **Pedagogical Fit:** Review each addition against learning objectives for that chapter
- [ ] **Accessibility:** Ensure paper-specific jargon is explained or linked to glossary

---

## RECOMMENDATIONS

### 1. IMPLEMENT (High confidence)

These additions appropriately cite essential foundational work:
- Bommasani et al. (2022) - FM definition
- Daveysmith & Treasure (2003) - Mendelian randomization
- Maurano et al. (2012) - Regulatory variant enrichment
- Grimm et al. (2015) - Benchmark circularity
- Karollus et al. (2023) - PLM-VEP limitations

**Action:** Add bibliography entries + implement text unchanged

---

### 2. IMPLEMENT WITH REVISIONS (Medium confidence)

These additions need minor clarifications:
- ESM3 section (Hayes 2025) - Add experimental validation details
- PRS deep learning (Elgart, Dibaeinia) - Quantify improvements
- FDA guidance section - Add evidence of genomic FM adoption

**Action:** Revise text per suggestions above, then implement

---

### 3. VERIFY BEFORE IMPLEMENTING (Lower confidence)

These additions need external verification:
- wang_genomic_2025 (Genomic Touchstone) - confirm release status
- dibaeinia_prsformer_2025 - verify performance claims
- madhu_heist_2025 - confirm spatial FM implementation

**Action:** Independently verify these papers' existence and claims before citing

---

### 4. CONSIDER CONSOLIDATING

These citations may be redundant if existing sections cover similar ground:
- vig_bertology_2021 - Check against existing attention analysis citations in Ch. 25
- BERTology techniques - Verify not already discussed in platform interpretability sections

**Action:** Search book for "attention", "BERTology", "interpretation" before adding

---

## SUMMARY TABLE

| Change # | Chapter | Papers | Issues | Verdict |
|----------|---------|--------|--------|---------|
| 1 | Ch14 | Bommasani | None | APPROVE |
| 2 | Ch14 | Trop | None | APPROVE |
| 3 | Ch16 | Hayes | ESM3 validation details needed | APPROVE WITH REVISION |
| 4 | Ch16 | Baek | None | APPROVE |
| 5 | Ch16 | Ahdritz | None | APPROVE |
| 6 | Ch16 | Ingraham | None | APPROVE |
| 7 | Ch17 | Maurano | None | APPROVE |
| 8 | Ch18 | Farh | None | APPROVE |
| 9 | Ch18 | Karollus, Swanson, Notin | None | APPROVE |
| 10 | Ch12 | Grimm | Severity claims vague | APPROVE WITH REVISION |
| 11 | Ch12 | Wang, Tanigawa | Wang status unclear (2025) | VERIFY BEFORE APPROVE |
| 12 | Ch13 | Amariuta, Sohail | None | APPROVE |
| 13 | Ch25 | Vig | Possible redundancy | VERIFY FIRST |
| 14 | Ch26 | DaveySmith | None | APPROVE |
| 15 | Ch27 | FDA | Applicability unsupported | APPROVE WITH REVISION |
| 16 | Ch28 | Elgart, Dibaeinia, Yun | Magnitudes needed | APPROVE WITH REVISION |
| 17 | Ch30 | Corso | None | APPROVE |
| 18 | Ch21 | Aibar | None | APPROVE |
| 19 | Ch21 | Madhu | HEIST status unclear (2025) | VERIFY BEFORE APPROVE |
| 20 | Ch02 | Taliun | None | APPROVE |
| Tool refs | Ch02, Ch28 | Purcell, PharmGKB | None | APPROVE |

---

## CRITICAL ACTION ITEMS

### BLOCKING ISSUE: Bibliography

**DO NOT implement ANY text changes until:**
1. Complete BibTeX entries added for all 27 papers to `references.bib`
2. Bibliography regenerated/compiled successfully
3. Cross-reference syntax verified in Quarto

**Timeline:** This is a prerequisite - must complete first.

---

## CONCLUSION

The proposal **correctly identifies gaps in citation coverage** for important claims. The proposed papers are generally well-chosen and appropriately motivated.

However:

1. **Bibliography integration is blocking** - All papers missing from `.bib` file
2. **Some 2025 papers need verification** - Recent dates mean fewer secondary citations available
3. **A few claims need clarification** - Magnitude/scope quantification would strengthen
4. **3 claims remain somewhat unsupported** - Even with proposed citations, need additional evidence

**Overall Assessment:** APPROVE WITH CONDITIONS

Implement after:
- [ ] Bibliography updated (27 new entries)
- [ ] 2025 papers verified
- [ ] Text revisions for quantification/clarification completed
- [ ] Redundancy check against existing sections completed

---

*Audit completed by Citation-Needs-Detector*
*For editorial review before multi-agent revision begins*

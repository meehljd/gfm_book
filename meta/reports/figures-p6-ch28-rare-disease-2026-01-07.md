# Figure Report: Chapter 28 - Rare Disease Diagnosis

**Chapter:** p6-ch28-rare-disease.qmd
**Date:** 2026-01-07
**Total Figures:** 6 (9 files)
**Format:** SVG (for scalability)

---

## Figure 1: Rare Disease Variant Filtering Funnel

### Files
- `figs/part_6/ch28/01-fig-rare-disease-funnel.svg`

### Priority
**Essential** - Core diagnostic workflow

### Content Description
Inverted funnel showing progressive filtering from raw variants to candidates for expert review, with FM contribution highlighted.

### DALL-E Prompt
```
Scientific illustration of rare disease variant filtering pipeline as inverted funnel. Single panel.

FUNNEL STAGES (top to bottom, narrowing):

STAGE 1 (TOP - Widest):
- "Raw Variants" - ~25,000
- All called variants from WGS/WES
- Minimal filtering

STAGE 2:
- "Quality Filtered" - ~22,000
- Remove low confidence calls
- Annotation: 10-15% removed

STAGE 3:
- "Population Frequency Filtered" - ~500-1,000
- Remove common variants (>0.1% in gnomAD)
- Annotation: 95%+ removed (most aggressive filter)

STAGE 4:
- "Consequence Filtered" - ~100-200
- Keep coding, splice, regulatory
- Remove synonymous, intronic
- Annotation: 80% removed

STAGE 5 (FM CONTRIBUTION highlighted):
- "Foundation Model Scored" - ~20-50
- Pathogenicity predictions
- Regulatory effect predictions
- Prioritization ranking
- Box: "FMs contribute here - after basic filtering, before expert review"

STAGE 6 (BOTTOM - Narrowest):
- "Expert Review Candidates" - ~5-10
- Manual curation required
- ACMG classification
- Final diagnostic decision

SIDE ANNOTATIONS:
- Time/compute cost increasing downward
- Human effort concentrated at bottom
- Numbers are approximate, vary by case

Professional clinical genomics style, funnel visualization, blue gradient, white background.

Save as: 01-fig-rare-disease-funnel.svg
```

### Post-Processing Notes
- Add specific filter criteria
- Include compute time estimates
- Show inheritance pattern filtering

### Fallback Description
"Rare disease filtering funnel: from ~25,000 raw variants through quality filtering (~22,000), population frequency filtering (~1,000), consequence filtering (~200), FM scoring (~50), to expert review candidates (~5-10). Foundation models contribute after basic filtering, before expert review, reducing manual curation burden."

### Caption Recommendation
"Variant filtering pipeline for rare disease diagnosis. Starting with ~25,000 variants from whole-genome sequencing, progressive filters remove low-quality calls, common population variants, and non-consequential changes. Foundation model scoring (~50 candidates) prioritizes variants for expert review (~5-10). The key insight: FMs contribute most effectively after basic filtering removes obvious noise but before expensive expert curation."

---

## Figure 2: ACMG-AMP Classification Framework

### Files
- `figs/part_6/ch28/02-fig-acmg-amp.svg`

### Priority
**Essential** - Regulatory framework

### Content Description
ACMG-AMP evidence framework showing evidence types, strengths, and how they combine for classification.

### DALL-E Prompt
```
Scientific illustration of ACMG-AMP variant classification framework. Single panel with structured layout.

TOP: Five classification categories (left to right):
- Pathogenic (red)
- Likely Pathogenic (orange)
- VUS - Variant of Uncertain Significance (gray)
- Likely Benign (light green)
- Benign (green)

MIDDLE: Evidence categories grid

PATHOGENIC EVIDENCE (supporting pathogenic):
- PVS1 (Very Strong): Null variant in LOF-intolerant gene
- PS1-4 (Strong): Same AA change known pathogenic, functional studies, etc.
- PM1-6 (Moderate): Hot spot, absence in controls, etc.
- PP1-5 (Supporting): Co-segregation, computational (PP3), etc.

BENIGN EVIDENCE (supporting benign):
- BA1 (Stand-alone): >5% population frequency
- BS1-4 (Strong): High frequency, functional studies show benign
- BP1-7 (Supporting): Computational benign (BP4), etc.

COMBINATION RULES (bottom):
Flow chart showing how evidence combines:
- Pathogenic: 1 Very Strong + 1 Strong OR 2 Strong + 1 Moderate, etc.
- Visual logic gates

COMPUTATIONAL EVIDENCE highlighted:
- PP3/BP4 box emphasized
- "FM predictions inform these criteria"
- Note: Requires validated algorithms

Professional clinical genetics style, evidence grid layout, color-coded, white background.

Save as: 02-fig-acmg-amp.svg
```

### Post-Processing Notes
- Add specific evidence codes
- Include combination rule details
- Show FM contribution (PP3/BP4)

### Fallback Description
"ACMG-AMP classification framework: five categories from Pathogenic to Benign, evidence types at different strengths (Very Strong, Strong, Moderate, Supporting), and combination rules determining final classification. Foundation model predictions contribute to PP3 (computational pathogenic) and BP4 (computational benign) criteria."

### Caption Recommendation
"ACMG-AMP variant classification framework. Variants are classified into five categories based on accumulated evidence. Pathogenic evidence ranges from Very Strong (PVS1: null variants) to Supporting (PP1-5). Benign evidence similarly ranges from Stand-alone (BA1: high population frequency) to Supporting (BP1-7). Foundation model predictions contribute to computational evidence criteria (PP3, BP4), but provide only Supporting-level evidence without additional validation."

---

## Figure 3: Family-Based Analysis

### Files
- `figs/part_6/ch28/03-A-fig-family-analysis.svg`
- `figs/part_6/ch28/03-B-fig-family-analysis.svg`
- `figs/part_6/ch28/03-C-fig-family-analysis.svg`

### Priority
**High** - Key diagnostic strategy

### Content Description
Three-panel figure on family analysis: inheritance patterns, de novo variant detection, and segregation analysis.

### DALL-E Prompt
```
Scientific illustration of family-based analysis for rare disease. Three panels.

PANEL A (Inheritance Patterns):
Four pedigrees showing different inheritance:
1) Autosomal Dominant: vertical transmission, 50% affected
2) Autosomal Recessive: horizontal pattern, carrier parents
3) X-linked: affected males, carrier females
4) De novo: affected child, unaffected parents
For each: expected variant patterns labeled

PANEL B (Trio Analysis for De Novo):
Three-generation pedigree with proband (affected child) and unaffected parents. Variant call table showing:
- Proband: variant present (het)
- Mother: variant absent
- Father: variant absent
→ De novo confirmed
Statistical annotation: "De novos enriched in developmental disorders"
FM contribution: "Prioritize de novos in constrained genes"

PANEL C (Segregation Analysis):
Extended pedigree with multiple affected and unaffected members. Variant tracking through family. LOD score calculation hint. Table showing:
- Affected members: all have variant
- Unaffected members: none have variant
→ Strong segregation evidence
ACMG criteria: PP1 (co-segregation)

Professional clinical genetics style, pedigree symbols, white background.

Save as: 03-A-fig-family-analysis.svg through 03-C-fig-family-analysis.svg
```

### Post-Processing Notes
- Use standard pedigree symbols
- Add specific inheritance examples
- Include statistical measures

### Fallback Description
"Family-based analysis: inheritance patterns (AD, AR, X-linked, de novo) with expected variant patterns, trio analysis confirming de novo variants in affected children with unaffected parents, and segregation analysis tracking variants through extended pedigrees to provide co-segregation evidence."

### Caption Recommendation
"Family-based analysis for rare disease diagnosis. (A) Inheritance patterns: autosomal dominant, autosomal recessive, X-linked, and de novo mutations each produce characteristic pedigree patterns. (B) Trio analysis: comparing proband to parents identifies de novo variants—particularly valuable for developmental disorders where FMs prioritize de novos in constrained genes. (C) Segregation analysis: tracking variants through extended families provides co-segregation evidence (ACMG PP1) when the variant consistently tracks with disease status."

---

## Figure 4: Somatic vs Germline Distinction

### Files
- `figs/part_6/ch28/04-A-fig-somatic-germline.svg`
- `figs/part_6/ch28/04-B-fig-somatic-germline.svg`

### Priority
**High** - Critical distinction

### Content Description
Two-panel figure distinguishing germline (constitutional) from somatic variants in diagnostic contexts.

### DALL-E Prompt
```
Scientific illustration distinguishing germline from somatic variants. Two panels.

PANEL A (Germline vs Somatic Origins):
Split diagram:
LEFT (Germline): Sperm + egg → fertilized egg → all body cells contain variant. Annotation "Present from conception, all tissues affected, heritable."
RIGHT (Somatic): Normal development → mutation in one cell → clonal expansion → subset of cells affected. Annotation "Acquired post-conception, tissue-specific, not heritable."

Center comparison:
- Germline: constitutional, rare disease causation, family implications
- Somatic: acquired, cancer driver, individual patient impact

PANEL B (Diagnostic Implications):
Two clinical scenarios:

Scenario 1 (Inherited Cancer Risk):
Patient with germline BRCA1 mutation.
- Present in blood (where tested)
- Surveillance for multiple cancers
- Family cascade testing recommended
FM contribution: Pathogenicity scoring

Scenario 2 (Tumor Profiling):
Patient with somatic KRAS mutation.
- Present only in tumor
- Targeted therapy selection
- No family testing indicated
FM contribution: Therapeutic response prediction

WARNING BOX: "Germline finding in tumor testing → requires confirmation in blood, genetic counseling, family implications"

Professional clinical genetics/oncology style, developmental biology visualization, white background.

Save as: 04-A-fig-somatic-germline.svg, 04-B-fig-somatic-germline.svg
```

### Post-Processing Notes
- Add specific gene examples
- Include VAF considerations
- Show mosaic scenario

### Fallback Description
"Germline vs somatic variants: germline present from conception in all cells (heritable, rare disease), somatic acquired post-conception in subset of cells (cancer, individual-specific). Diagnostic implications differ: germline findings require family cascade testing while somatic findings guide individual therapy."

### Caption Recommendation
"Distinguishing germline from somatic variants. (A) Origins: germline variants are present from conception in all cells and are heritable; somatic variants arise post-conception in specific tissues. (B) Diagnostic implications: germline findings (e.g., BRCA1) affect surveillance and family testing; somatic findings (e.g., KRAS) guide therapy without family implications. Critical warning: germline findings incidentally discovered in tumor testing require blood confirmation and genetic counseling."

---

## Figure 5: Functional Validation Hierarchy

### Files
- `figs/part_6/ch28/05-fig-functional-validation.svg`

### Priority
**High** - Evidence integration

### Content Description
Hierarchy of functional evidence from computational predictions through experimental assays.

### DALL-E Prompt
```
Scientific illustration of functional validation evidence hierarchy. Single panel with pyramid/levels structure.

HIERARCHY (bottom to top, weakest to strongest):

LEVEL 1 (BOTTOM - Computational):
- Foundation model predictions
- Conservation scores
- Structural modeling
- Splicing predictors
- Annotation "ACMG: Supporting evidence only (PP3/BP4)"
- Color: Light blue

LEVEL 2 (In Vitro Biochemical):
- Protein functional assays
- Enzyme activity measurements
- Binding assays
- Annotation "Direct functional readout, artificial context"
- Color: Medium blue

LEVEL 3 (Cellular):
- Reporter assays
- Minigene splicing assays
- MPRA (massively parallel)
- Patient-derived cells
- Annotation "Cellular context, scalable"
- Color: Darker blue

LEVEL 4 (Organismal):
- Animal models (mouse, zebrafish)
- Phenotype recapitulation
- Annotation "In vivo validation, expensive"
- Color: Dark blue

LEVEL 5 (TOP - Human):
- Natural history studies
- Genotype-phenotype correlation
- Segregation in families
- Annotation "Ultimate validation, observational"
- Color: Darkest blue

SIDE: FM contribution spans Levels 1-3
- Level 1: Direct predictions
- Level 2-3: Prioritize variants for testing, interpret results

ACMG evidence codes mapped to each level.

Professional scientific style, evidence pyramid, blue gradient, white background.

Save as: 05-fig-functional-validation.svg
```

### Post-Processing Notes
- Add specific assay examples
- Include ACMG code mappings
- Show throughput considerations

### Fallback Description
"Functional validation hierarchy: from computational predictions (supporting evidence only) through in vitro biochemical assays, cellular assays (reporter, MPRA), organismal models (animal), to human natural history (ultimate validation). FM predictions contribute at computational level and prioritize variants for higher-level validation."

### Caption Recommendation
"Functional validation evidence hierarchy. Computational predictions (Level 1) from foundation models provide only supporting ACMG evidence. In vitro biochemical assays (Level 2) offer direct functional readout but artificial context. Cellular assays (Level 3: reporters, MPRA) provide cellular context at scale. Organismal models (Level 4) enable in vivo validation. Human natural history studies (Level 5) provide ultimate but observational evidence. Foundation models contribute at Level 1 directly and Levels 2-3 by prioritizing variants for experimental validation."

---

## Figure 6: Human-AI Interpretive Partnership

### Files
- `figs/part_6/ch28/06-fig-interpretive-partnership.svg`

### Priority
**Enhancing** - Vision for integration

### Content Description
Model of productive human-AI collaboration in variant interpretation, showing respective strengths.

### DALL-E Prompt
```
Scientific illustration of human-AI partnership in variant interpretation. Single panel with complementary roles.

CENTER: Venn diagram or side-by-side comparison

AI/FOUNDATION MODEL STRENGTHS (left side, blue):
- Pattern recognition at scale
- Processing thousands of variants
- Consistent application of rules
- Integration of diverse data types
- Never fatigued, always available
- Quantitative scoring with uncertainty
Icon: Neural network

HUMAN EXPERT STRENGTHS (right side, green):
- Clinical context integration
- Phenotype-genotype reasoning
- Family communication
- Novel case judgment
- Ethical considerations
- Accountability and trust
Icon: Clinician/geneticist

OVERLAP/PARTNERSHIP ZONE (center):
- FM scores + expert interpretation
- Prioritization enables focus
- Uncertainty flags for human attention
- Iterative refinement

WORKFLOW BELOW:
25,000 variants → [FM] → 50 candidates → [Human] → 1-5 diagnoses
Annotation "AI handles scale, humans handle judgment"

BOTTOM MESSAGE: "Partnership, not replacement. FMs extend human capacity; humans provide judgment and accountability."

Professional collaborative style, complementary visualization, white background.

Save as: 06-fig-interpretive-partnership.svg
```

### Post-Processing Notes
- Add specific task examples
- Include efficiency metrics
- Show feedback loops

### Fallback Description
"Human-AI interpretive partnership: FMs provide pattern recognition at scale, consistent scoring, and prioritization; human experts provide clinical context, phenotype reasoning, communication, and accountability. Partnership enables FMs to handle variant volume while humans focus on judgment and decisions."

### Caption Recommendation
"Human-AI partnership in variant interpretation. Foundation models excel at pattern recognition across thousands of variants, consistent rule application, and quantitative scoring with uncertainty. Human experts provide clinical context integration, phenotype-genotype reasoning, family communication, and ethical judgment. The productive partnership: FMs reduce 25,000 variants to ~50 prioritized candidates, freeing experts to focus their judgment on cases that matter. This is partnership, not replacement—FMs extend human capacity while humans provide the accountability that clinical decisions require."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Filtering Funnel | 1 | Essential | Low |
| ACMG-AMP Framework | 1 | Essential | Medium |
| Family Analysis | 3 | High | Medium |
| Somatic vs Germline | 2 | High | Low |
| Functional Validation | 1 | High | Medium |
| Interpretive Partnership | 1 | Enhancing | Low |

## Recommended Generation Order
1. Filtering Funnel (diagnostic workflow)
2. ACMG-AMP Framework (regulatory context)
3. Family Analysis (diagnostic strategy)
4. Functional Validation (evidence hierarchy)
5. Somatic vs Germline (critical distinction)
6. Interpretive Partnership (vision)

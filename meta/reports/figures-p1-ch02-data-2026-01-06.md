# Figure Report: Chapter 2 - Data Landscape

**Chapter:** Part 1, Chapter 2 - Data Landscape
**Date:** 2026-01-06
**Figures:** 4 conceptual figures (6 files)

---

## Figure 2.1: Data Ecosystem Map

**File:** `figs/part_1/ch02/01-fig-data-ecosystem.png`
**Priority:** Essential
**Type:** Conceptual diagram / Information architecture

### Content Description

Layered conceptual map showing how major genomic data resources interconnect and flow into downstream applications. Four layers organized vertically:

1. **Foundation Layer** (bottom): Reference genomes (GRCh38, T2T-CHM13) and gene annotations (GENCODE, RefSeq, MANE)
2. **Population Layer**: Variant catalogs (gnomAD, 1000 Genomes) and biobanks (UK Biobank, All of Us, FinnGen)
3. **Functional Layer**: ENCODE, Roadmap Epigenomics, Cistrome, GTEx
4. **Clinical Layer** (top): ClinVar, ClinGen, OMIM, PharmGKB

Arrows show dependencies between layers. Labels indicate data type contributions: "coordinates," "frequencies," "functions," "labels."

### DALL-E Prompt

```
Scientific diagram showing a four-tier data ecosystem for genomics research. Bottom layer shows DNA double helix icon with text labels for reference genomes. Second layer shows population database icons with human silhouettes representing diversity. Third layer shows heatmap-style functional genomics data with colored matrices. Top layer shows clinical symbols including medical crosses and documentation icons. Connecting arrows flow upward between layers showing data dependencies. Clean scientific illustration style with blue, green, and orange color palette. White background with subtle grid lines. Professional data visualization suitable for academic textbook. No text labels in the actual image, just icons and connecting lines.
```

### Post-Processing Notes

- Add text labels for each database/resource after generation
- Add legend explaining arrow meanings (provides coordinates, provides frequencies, etc.)
- Consider using institution logos or standardized icons for each database
- Layer backgrounds should be subtly differentiated

### Fallback Description

If AI generation fails, create a flowchart-style diagram in diagramming software (Lucidchart, draw.io) with:
- Four horizontal bands representing each layer
- Database names as boxes within each band
- Arrows connecting dependent resources
- Color coding by data type

### Caption

**Recommended Caption:**
"The genomic data ecosystem. Major resources are organized into four functional layers: reference assemblies and gene annotations provide the coordinate foundation; population catalogs and biobanks supply variant frequencies and phenotype associations; functional genomics consortia map biochemical activity across cell types; clinical databases aggregate pathogenicity interpretations. Arrows indicate data dependencies, with each layer building on those below. Every machine learning model in genomics inherits both the signal and the systematic gaps of resources in this ecosystem."

---

## Figure 2.2: Ancestry Representation Disparity

**File:** `figs/part_1/ch02/02-fig-ancestry-representation.png`
**Priority:** High
**Type:** Data visualization (bar chart or waffle plot)

### Content Description

Comparative visualization showing ancestry composition across key genomic resources, highlighting persistent European overrepresentation. Resources to compare:
- gnomAD v4
- UK Biobank
- ClinVar submissions
- GTEx donors
- GWAS Catalog participants

Include world map inset showing which continental ancestries are represented vs. underrepresented. Key statistic: ~78% of GWAS participants are European despite Europeans comprising ~16% of global population.

### DALL-E Prompt

```
Scientific data visualization showing ancestry representation in genomic research. Five stacked bar charts arranged horizontally, each showing population composition with color segments for European (large blue portion ~70-80%), African (small orange), East Asian (small green), South Asian (small purple), and other ancestries. A small world map in the corner with colored regions showing underrepresented populations. Clean academic style with muted scientific color palette. White background with subtle gridlines. Professional infographic style suitable for medical textbook. Modern minimalist data visualization design.
```

### Post-Processing Notes

- Add exact percentages from literature (Sirugo et al. 2019)
- Add database labels on x-axis
- Add legend for ancestry categories
- World map should highlight Africa, Latin America, Indigenous populations as underrepresented
- Include annotation arrow pointing to the disparity

### Fallback Description

Create in matplotlib or R ggplot2:
- Stacked horizontal bar chart with ancestry proportions
- Reference line showing global population proportions for comparison
- Inset world map with choropleth showing representation levels

### Caption

**Recommended Caption:**
"Ancestry representation across major genomic resources. Stacked bars show the proportion of samples from different ancestral backgrounds in key databases. European-ancestry individuals (blue) comprise approximately 78% of GWAS participants despite representing roughly 16% of the global population. This overrepresentation propagates through variant interpretation databases, functional genomics atlases, and polygenic score development, creating systematic gaps in genomic medicine for underrepresented populations. Inset map highlights continental regions with the largest representation deficits relative to population size."

---

## Figure 2.3: Functional Genomics Data Matrix

**File:** `figs/part_1/ch02/03-fig-functional-genomics-matrix.png`
**Priority:** High
**Type:** Heatmap visualization

### Content Description

Heatmap showing the ENCODE/Roadmap Epigenomics data compendium structure:
- **Rows:** Cell types or tissues (grouped by category: cell lines, primary cells, tissues)
- **Columns:** Assay types (ChIP-seq for various TFs and histone marks, DNase-seq, ATAC-seq, RNA-seq)
- **Color intensity:** Data availability (present/absent or coverage depth)

Annotations highlighting:
- Well-profiled cell types: K562, GM12878, HepG2 (tier 1 ENCODE cell lines)
- Disease-relevant tissues that remain undersampled
- Assay categories (accessibility, histone marks, TF binding, expression)

### DALL-E Prompt

```
Scientific heatmap visualization showing a data matrix for functional genomics experiments. Rectangular grid with approximately 50 rows and 20 columns. Color gradient from white (no data) through light blue to dark blue (complete data). Some rows have nearly complete coverage shown as dark horizontal bands. Other rows are sparse with scattered colored cells. Left side shows hierarchical clustering dendrogram. Column labels at top are grouped into categories. Clean academic scientific visualization style with gray borders between cells. White background. Professional bioinformatics data visualization suitable for research publication.
```

### Post-Processing Notes

- Add cell type labels on y-axis (grouped by tissue origin)
- Add assay type labels on x-axis (grouped by category)
- Highlight the "Tier 1" cell lines (K562, GM12878) with bracket
- Add annotations for undersampled but disease-relevant tissues
- Consider adding marginal bar plots showing row/column totals

### Fallback Description

Create in Python/R using actual ENCODE metadata:
- Query ENCODE portal for assay availability matrix
- Generate clustered heatmap with seaborn or ComplexHeatmap
- Add annotations programmatically

### Caption

**Recommended Caption:**
"Coverage of the ENCODE and Roadmap Epigenomics data compendium. Each row represents a cell type or tissue; each column represents an assay type (chromatin accessibility, histone modifications, transcription factor binding, gene expression). Color intensity indicates data availability, from absent (white) to comprehensively profiled (dark blue). Tier 1 cell lines (K562, GM12878, HepG2) show near-complete coverage across assay types, while many disease-relevant primary tissues remain sparsely profiled. Models trained on this compendium inherit its coverage biases, performing best for well-characterized cell types and potentially failing for undersampled contexts."

---

## Figure 2.4: ClinVar Landscape (Three-Panel)

**Files:**
- `figs/part_1/ch02/04-A-fig-clinvar-landscape.png`
- `figs/part_1/ch02/04-B-fig-clinvar-landscape.png`
- `figs/part_1/ch02/04-C-fig-clinvar-landscape.png`

**Priority:** High
**Type:** Multi-panel statistical visualization

### Panel A: Classification Distribution

**Content:** Pie chart or bar chart showing distribution of ClinVar classifications:
- Pathogenic
- Likely Pathogenic
- Variant of Uncertain Significance (VUS) - largest category
- Likely Benign
- Benign
- Conflicting Interpretations

**DALL-E Prompt:**
```
Scientific pie chart showing clinical variant classification distribution. Large gray segment (approximately 50%) dominates representing uncertain variants. Smaller red segment for pathogenic (~15%), orange for likely pathogenic (~10%), green for benign (~10%), light green for likely benign (~8%), and purple for conflicting (~7%). Clean minimalist scientific style with white background. Professional medical data visualization with muted clinical color palette. No text labels, just colored segments with clean borders.
```

**Caption for Panel A:**
"Distribution of clinical significance classifications in ClinVar. Variants of uncertain significance (VUS, gray) constitute the majority of entries, reflecting genuine evidential limitations for most rare variants. The dominance of VUS highlights both the scale of the variant interpretation challenge and the opportunity for computational methods to assist reclassification."

### Panel B: Gene Coverage Heatmap

**Content:** Heatmap showing classification density by gene, with:
- Well-studied genes (*BRCA1*, *BRCA2*, *CFTR*, *LDLR*) having many submissions
- Long tail of genes with sparse coverage
- Color intensity = number of classified variants

**DALL-E Prompt:**
```
Scientific heatmap showing gene coverage for clinical variant databases. Vertical bars of varying heights and colors arranged horizontally representing different genes. Few tall dark blue bars on the left (heavily studied genes) transitioning to many short light blue bars on the right (rarely studied genes). Follows power-law distribution pattern. Clean bioinformatics visualization style with white background and gray axis lines. Professional medical genetics data visualization. Minimalist academic style.
```

**Caption for Panel B:**
"Classification density across genes in ClinVar. Well-studied disease genes such as *BRCA1*, *BRCA2*, and *CFTR* contain thousands of classified variants (dark blue), while the majority of genes have sparse representation (light blue). This uneven coverage creates feedback loops: genes with more data train better models, which encourages further study, while rarely-studied genes remain difficult to interpret computationally."

### Panel C: Classification Evolution Timeline

**Content:** Timeline/trajectory showing how variant classifications evolve:
- Example variant trajectory from VUS to Likely Pathogenic to Pathogenic
- Illustrates version sensitivity of ClinVar
- Shows temporal instability of classifications

**DALL-E Prompt:**
```
Scientific timeline diagram showing clinical variant reclassification over time. Horizontal timeline from 2015 to 2024 with a trajectory line that starts in a gray zone (uncertain), moves through an orange zone (likely pathogenic), and ends in a red zone (pathogenic). Small circular nodes mark classification changes at specific years. Background has subtle horizontal bands showing classification zones. Clean medical informatics visualization style with white background. Professional academic diagram suitable for clinical genetics textbook.
```

**Caption for Panel C:**
"Temporal evolution of variant classifications in ClinVar. This schematic illustrates how a single variant's classification can change over time as new evidence accumulates. A variant initially classified as VUS (gray zone) may be reclassified as likely pathogenic (orange) and eventually pathogenic (red) as functional studies, family segregation data, or additional case reports emerge. Models trained on ClinVar snapshots must account for this temporal instability; a variant labeled benign in 2018 training data may be reclassified as pathogenic by 2024."

### Combined Caption

**Full Figure Caption:**
"The ClinVar variant interpretation landscape. (A) Distribution of clinical significance classifications, highlighting that variants of uncertain significance dominate the database. (B) Classification density across genes, showing that well-studied genes have orders of magnitude more classified variants than the long tail of rarely-studied genes. (C) Temporal evolution of classifications, illustrating how variant interpretations change as evidence accumulates. Together, these panels reveal why computational variant interpretation remains challenging: most variants lack confident classifications, coverage is highly uneven across genes, and ground truth labels are themselves unstable over time."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 2.1 Data Ecosystem | 1 | Essential | High (conceptual) |
| 2.2 Ancestry | 1 | High | Medium (data viz) |
| 2.3 Functional Matrix | 1 | High | Medium (heatmap) |
| 2.4 ClinVar | 3 | High | Medium (multi-panel) |

**Total files:** 6
**Recommended generation order:** 2.2 (data-driven), 2.3 (data-driven), 2.4A-C (statistical), 2.1 (conceptual last, most complex)

# Figure Report: Chapter 1 - From Reads to Variants

**Chapter:** Part 1, Chapter 1 - From Reads to Variants
**Date:** 2026-01-06
**Figures:** 5 conceptual figures (9 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 1.1: Variant Calling Pipeline

**File:** `figs/part_1/ch01/01-fig-variant-pipeline.svg`
**Priority:** Essential
**Type:** Pipeline flowchart

### Content Description

End-to-end schematic showing the journey from DNA sample to VCF file, with data formats annotated at each stage. Shows both short-read and long-read paths converging at alignment.

### DALL-E Prompt

```
Create a scientific pipeline diagram showing DNA sequencing variant calling workflow. Save as: 01-fig-variant-pipeline.svg

Clean technical illustration, white background, left-to-right flow.

Main stages as rounded rectangles connected by arrows:
1. "DNA Sample" (icon: double helix)
2. "Library Prep" (icon: fragmented DNA pieces)
3. "Sequencing" - split into two paths:
   - Upper: "Short-read (Illumina)" with small rectangle icon
   - Lower: "Long-read (PacBio/ONT)" with wavy line icon
4. "Base Calling" producing "FASTQ"
5. "Alignment" showing reads stacking against reference bar, producing "BAM/CRAM"
6. "Post-processing" (duplicate marking, BQSR)
7. "Variant Calling" producing "gVCF"
8. "Joint Genotyping" (multiple samples merging)
9. "Filtering" producing final "VCF"

Data format labels in monospace font boxes at each arrow: FASTQ, BAM, gVCF, VCF.

Color scheme: DNA elements in blue (#1f77b4), processing steps in gray (#7f7f7f), output files in green (#2ca02c).

Style: Publication-quality scientific diagram, vector-style clean lines, no gradients, no 3D effects, minimal decoration. Suitable for textbook figure.
```

### Post-Processing Notes

- Add file size annotations (e.g., "~100 GB FASTQ", "~50 GB BAM", "~5 GB VCF")
- Ensure arrows show clear directionality
- Add small "30x coverage" annotation near alignment step
- May need to manually add monospace font for file format labels

### Fallback Description

Create horizontal flowchart with 9 boxes representing stages from DNA sample to VCF using BioRender or draw.io. Include icons for each sequencing platform. Label data formats at transitions. Show reads as horizontal lines stacking against a reference bar in the alignment stage.

### Caption

**Recommended Caption:**
"The variant calling pipeline transforms raw sequencing data into genotype calls through multiple processing stages. DNA samples undergo fragmentation and library preparation before sequencing on short-read (Illumina) or long-read (PacBio, ONT) platforms. Base calling produces FASTQ files containing reads and quality scores. Alignment maps reads to a reference genome (GRCh38 or T2T-CHM13), generating BAM/CRAM files. Post-alignment processing marks PCR duplicates and recalibrates base quality scores. Per-sample variant calling produces genomic VCF (gVCF) files encoding genotype likelihoods at all positions. Joint genotyping across a cohort merges samples and applies population-informed priors. Final filtering separates high-confidence variants from probable artifacts. File sizes shown are approximate for 30× whole-genome sequencing."

---

## Figure 1.2: Phasing and Compound Heterozygosity (Three-Panel)

**Files:**
- `figs/part_1/ch01/02-A-fig-phasing-compound-het.svg`
- `figs/part_1/ch01/02-B-fig-phasing-compound-het.svg`
- `figs/part_1/ch01/02-C-fig-phasing-compound-het.svg`

**Priority:** High
**Type:** 3-panel conceptual diagram

### Panel A: Base Setup

**Content:** Two chromosomes side by side representing maternal (pink/red tint) and paternal (blue tint) copies of CFTR gene region with two variant positions marked.

**DALL-E Prompt:**
```
Create a scientific diagram showing chromosome pair with variant positions. Save as: 02-A-fig-phasing-compound-het.svg

Two chromosomes side by side representing maternal (pink/red tint, #d62728 at 30% opacity) and paternal (blue tint, #1f77b4 at 30% opacity) copies of CFTR gene region.

Each chromosome shown as horizontal bar approximately 3cm long. Gene region marked with arrow showing transcription direction. Two variant positions marked as stars or diamonds at specific locations along each chromosome, positions aligned vertically between chromosomes.

Labels: "Maternal chromosome" and "Paternal chromosome" on left side. "CFTR gene" label with arrow. "Variant 1" and "Variant 2" labels pointing to marked positions.

Clean white background, publication-quality scientific illustration, minimal style, no 3D effects.
```

**Caption for Panel A:**
"Two chromosomes carry the CFTR gene, with two pathogenic variant positions indicated. Standard VCF genotypes (0/1 at each site) cannot distinguish the cis and trans configurations."

### Panel B: Cis Configuration

**Content:** Both variant markers on the MATERNAL chromosome only. Paternal chromosome has NO variants (functional copy). Shows child as carrier (unaffected).

**DALL-E Prompt:**
```
Create a scientific diagram showing compound heterozygosity in CIS configuration. Save as: 02-B-fig-phasing-compound-het.svg

Two horizontal chromosome bars (maternal=red tint #d62728 at 30% opacity, paternal=blue tint #1f77b4 at 30% opacity).

CRITICAL: Both variant markers (stars) are on the MATERNAL chromosome only. Paternal chromosome has NO variants (shows as "functional copy").

Annotations:
- Arrow pointing to maternal: "Both variants on same chromosome (cis)"
- Arrow pointing to paternal: "Functional copy intact"
- Bottom text box: "Child is carrier (unaffected)"
- Small VCF notation showing: "0|1" and "0|1" (both variants phased to same haplotype)

Green checkmark icon near paternal chromosome indicating functional. Clean scientific illustration style, white background, publication quality.
```

**Caption for Panel B:**
"Cis configuration: both variants reside on the maternal chromosome, leaving the paternal copy functional. The child is an unaffected carrier."

### Panel C: Trans Configuration

**Content:** Variant 1 on maternal chromosome, Variant 2 on paternal chromosome. Each chromosome has exactly one variant. Shows child has cystic fibrosis.

**DALL-E Prompt:**
```
Create a scientific diagram showing compound heterozygosity in TRANS configuration. Save as: 02-C-fig-phasing-compound-het.svg

Two horizontal chromosome bars (maternal=red tint #d62728 at 30% opacity, paternal=blue tint #1f77b4 at 30% opacity).

CRITICAL: Variant 1 on maternal chromosome, Variant 2 on paternal chromosome. Each chromosome has exactly one variant.

Annotations:
- Arrow: "Variants on opposite chromosomes (trans)"
- Red X marks on both chromosomes indicating "No functional copy"
- Bottom text box: "Child has cystic fibrosis"
- Small VCF notation showing: "1|0" and "0|1" (variants on different haplotypes)

Red warning indicator. Clean scientific illustration style, white background, publication quality. Same chromosome styling as panels A and B for consistency.
```

**Caption for Panel C:**
"Trans configuration: one variant on each parental chromosome eliminates all functional copies. The child has cystic fibrosis."

### Combined Caption

**Full Figure Caption:**
"Haplotype phase determines clinical outcome in compound heterozygosity. (A) Two chromosomes carry the *CFTR* gene, with two pathogenic variant positions indicated. Standard VCF genotypes (0/1 at each site) cannot distinguish the configurations shown in (B) and (C). (B) *Cis* configuration: both variants reside on the maternal chromosome, leaving the paternal copy functional. The child is an unaffected carrier. (C) *Trans* configuration: one variant on each parental chromosome eliminates all functional copies. The child has cystic fibrosis. Phased VCF notation (using | delimiter) encodes this distinction: 0|1, 0|1 indicates both alternate alleles on the same haplotype (cis), while 1|0, 0|1 indicates alternate alleles on opposite haplotypes (trans)."

---

## Figure 1.3: Error Sources Taxonomy

**File:** `figs/part_1/ch01/03-fig-error-sources.svg`
**Priority:** High
**Type:** Taxonomy/hierarchy diagram

### Content Description

Hierarchical taxonomy diagram organizing variant calling errors into three major categories (Sequencing Artifacts, Alignment Artifacts, Biological Complexity) with subdivisions and FP/FN labels.

### DALL-E Prompt

```
Create a scientific taxonomy diagram showing sources of variant calling errors. Save as: 03-fig-error-sources.svg

Tree/hierarchy structure flowing from top to bottom.

ROOT NODE: "Variant Calling Errors" (large box at top)

THREE MAIN BRANCHES:

BRANCH 1: "Sequencing Artifacts" (orange/red color family #d62728)
Subdivisions as smaller connected boxes:
- "Homopolymer errors" (FP)
- "PCR duplicates" (FP)
- "Index hopping" (FP)
- "Strand bias" (FP)
- "Quality miscalibration" (Both)

BRANCH 2: "Alignment Artifacts" (blue color family #1f77b4)
Subdivisions:
- "Mapping ambiguity in repeats" (Both)
- "Reference bias" (FN)
- "Paralog misalignment" (FP)

BRANCH 3: "Biological Complexity" (green color family #2ca02c)
Subdivisions:
- "Somatic mosaicism" (FN)
- "Low allele fraction" (FN)
- "Complex variants (MNVs)" (Both)

Each leaf node has small tag: "FP" (false positive), "FN" (false negative), or "Both"

Clean scientific diagram style, white background, clear hierarchy with connecting lines. Color-coded branches. Publication quality, no 3D effects, vector style.
```

### Post-Processing Notes

- Add one-sentence descriptions for each leaf node (may need to be in caption)
- Ensure FP/FN tags are clearly visible
- Consider adding small icons for each error type
- Balance visual weight across three branches

### Fallback Description

Create tree diagram in draw.io or Lucidchart. Three main branches from central node. Each branch has 3-5 leaf nodes. Color code by branch. Add FP/FN indicators. Can also be done as nested boxes if tree structure doesn't work well.

### Caption

**Recommended Caption:**
"Variant calling errors arise from three distinct sources with different consequences. Sequencing artifacts from instrument noise and library preparation create false positive (FP) variant calls. Alignment artifacts from ambiguous mapping in repetitive regions cause both false positives (variants called at wrong locations) and false negatives (FN, true variants missed due to mapping uncertainty). Biological complexity including mosaicism and low allele fractions primarily causes false negatives, as genuine variants fail to meet detection thresholds. Understanding error sources is essential for interpreting callset limitations and designing robust training strategies for downstream models."

---

## Figure 1.4: Difficult Genomic Regions

**File:** `figs/part_1/ch01/04-fig-difficult-regions.svg`
**Priority:** Enhancing
**Type:** Ideogram/genome view

### Content Description

Ideogram-style genome overview highlighting regions where short-read variant calling systematically fails: segmental duplications, HLA complex, centromeres, tandem repeats. Include insets for pie chart of difficulty classes and long-read advantage illustration.

### DALL-E Prompt

```
Create a scientific genome ideogram showing difficult regions for variant calling. Save as: 04-fig-difficult-regions.svg

Ideogram showing all 22 autosomes plus X and Y as horizontal banded bars arranged in two columns. Chromosomes shown in standard cytogenetic banding pattern (light and dark bands).

HIGHLIGHTED REGIONS (use bright overlay colors):

1. SEGMENTAL DUPLICATIONS (yellow #ffbb78 highlights):
   - Chr22q11 region (mark "CYP2D6" label)
   - Scattered regions on multiple chromosomes

2. HLA COMPLEX (red/orange #d62728 highlight):
   - Chr6p21 - large highlighted block labeled "HLA region"

3. CENTROMERES (gray shading):
   - Center of each chromosome marked

4. SUBTELOMERIC REGIONS (purple #9467bd highlights):
   - Chromosome ends

5. TANDEM REPEAT EXAMPLES (green #2ca02c markers):
   - Chr4p16 labeled "HTT"
   - ChrXq27 labeled "FMR1"

INSET BOX 1 (lower right): Pie chart showing "% of genome in each difficulty class"
- Easy regions: ~85%
- Segmental dups: ~5%
- Repeats: ~5%
- Other difficult: ~5%

INSET BOX 2 (lower left): Small diagram showing "Long reads span difficult region" - short reads shown as small fragments that don't span, long read as single line spanning entire region.

Clean scientific illustration, white background, publication quality.
```

### Post-Processing Notes

- Ensure chromosome banding is accurate (can use standard ideogram templates)
- Add legend for color coding
- Verify gene positions are approximately correct
- May need to manually add percentage labels in inset

### Fallback Description

Use standard chromosome ideogram template from UCSC or Ensembl. Overlay colored regions using vector graphics software. Add two inset boxes manually. Consider using matplotlib/seaborn for the pie chart inset.

### Caption

**Recommended Caption:**
"Genomic regions where short-read variant calling systematically fails. Ideogram showing the human genome with difficult regions highlighted. Segmental duplications (yellow) including the *CYP2D6* pharmacogene region on chromosome 22q11 create mapping ambiguity. The HLA complex (orange) on chromosome 6p21 contains extreme polymorphism that confounds reference-based alignment. Centromeric and pericentromeric regions (gray) lack unique sequence. Tandem repeat disorder loci including *HTT* (Huntington disease, 4p16) and *FMR1* (fragile X, Xq27) resist accurate short-read genotyping. Inset (lower right) shows approximate genome fraction in each difficulty class. Inset (lower left) illustrates how long reads spanning entire difficult regions resolve ambiguities invisible to short reads."

---

## Figure 1.5: DeepVariant Pileup Tensor

**File:** `figs/part_1/ch01/05-fig-deepvariant-pileup.svg`
**Priority:** Essential
**Type:** Technical diagram

### Content Description

Annotated example of a DeepVariant-style pileup image showing how reads are encoded as a multi-channel tensor for CNN input. Shows grid of reads with channel annotations and genotype probability output.

### DALL-E Prompt

```
Create a scientific technical diagram showing DeepVariant pileup tensor visualization. Save as: 05-fig-deepvariant-pileup.svg

MAIN PILEUP DISPLAY (center):
- Grid approximately 30 rows (reads) × 50 columns (positions)
- Each row represents one sequencing read
- Center column highlighted as "candidate variant position"
- Color coding:
  - Gray cells: matches to reference
  - Colored cells (A=green #2ca02c, T=red #d62728, G=yellow #ffbb78, C=blue #1f77b4): mismatches
  - At candidate position: ~15 reads show reference, ~15 show alternate allele
  - Shows heterozygous pattern (roughly 50:50 split)

CHANNEL ANNOTATIONS (as labeled strips on right side):
- Channel 1: "Base identity" (nucleotide letters)
- Channel 2: "Base quality" (gradient from dark to light)
- Channel 3: "Mapping quality" (separate intensity scale)
- Channel 4: "Strand" (two colors for forward/reverse)
- Channel 5: "Allele support" (ref vs alt coloring)

TOP ROW: Reference sequence shown as letters "...ACGTACGTACGT..."

BOTTOM: Output box showing:
"Genotype posteriors:
P(0/0) = 0.02
P(0/1) = 0.96  ← Called genotype
P(1/1) = 0.02"

Clean technical illustration style, white background, grid lines visible, publication quality. No artistic interpretation, precise scientific diagram.
```

### Post-Processing Notes

- Ensure the heterozygous pattern is clearly visible (mix of ref and alt supporting reads)
- Add position numbers along x-axis
- May need to manually add the probability output box
- Consider adding arrows from pileup to "CNN" box to "Output" for flow

### Fallback Description

Create grid in matplotlib or specialized visualization. Generate synthetic pileup data showing het variant. Use imshow() with custom colormap. Add channel labels as text annotations. Create as multi-panel figure with main pileup and channel decomposition.

### Caption

**Recommended Caption:**
"DeepVariant encodes read evidence as a multi-channel pileup tensor for CNN-based genotype classification. Each row represents a sequencing read overlapping the candidate variant position (center column). Multiple channels encode: base identity (matches in gray, mismatches color-coded by nucleotide), base quality (intensity gradient), mapping quality, strand orientation, and allele support. The reference sequence appears at top. This example shows a heterozygous SNV with approximately half of reads supporting each allele. The CNN processes this tensor representation and outputs posterior probabilities over three genotype classes. The called genotype (0/1) corresponds to the highest posterior probability (0.96)."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 1.1 Variant Pipeline | 1 | Essential | High (multi-stage flow) |
| 1.2 Phasing | 3 | High | Medium (three panels) |
| 1.3 Error Sources | 1 | High | Medium (hierarchy) |
| 1.4 Difficult Regions | 1 | Enhancing | High (genome view + insets) |
| 1.5 DeepVariant Pileup | 1 | Essential | High (technical detail) |

**Total files:** 7 (not 9 as originally stated - corrected count)
**Recommended generation order:** 1.1 (pipeline, essential), 1.5 (DeepVariant, essential), 1.2A-C (phasing), 1.3 (errors), 1.4 (genome view, most complex)
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
# Figure Report: Chapter 3 - GWAS and Polygenic Scores

**Chapter:** Part 1, Chapter 3 - GWAS and Polygenic Scores
**Date:** 2026-01-06
**Figures:** 5 conceptual figures (8 files)

---

## Figure 3.1: Manhattan Plot Anatomy

**File:** `figs/part_1/ch03/01-fig-manhattan-anatomy.png`
**Priority:** Essential
**Type:** Annotated data visualization

### Content Description

Annotated Manhattan plot from a real or realistic GWAS (height or coronary artery disease). Key annotations required:

1. Genome-wide significance threshold at -log10(5 x 10^-8) ~ 7.3 (horizontal red dashed line)
2. Example peak with lead SNP labeled (rs number)
3. Width of peak showing LD extent (many correlated variants, not just one)
4. Chromosomes color-alternated along x-axis
5. Inset zoom on one peak showing how multiple variants exceed threshold
6. Q-Q plot inset showing expected vs observed p-value distribution
7. Genomic inflation factor lambda annotated on Q-Q plot

### DALL-E Prompt

```
Scientific Manhattan plot from genome-wide association study. Scattered dots arranged in columns representing 22 chromosomes plus X, alternating between blue and gray colors. Most dots cluster near bottom (y-axis shows -log10 p-value from 0 to 15). Several prominent peaks rise high above a red horizontal dashed line at y=7.3 representing the significance threshold. The peaks have characteristic skyline shape with many dots clustered together. Small inset box in upper right corner shows a Q-Q plot with dots along a diagonal line. Clean academic scientific visualization style with white background and black axis lines. Professional statistical genetics figure suitable for medical textbook.
```

### Post-Processing Notes

- Add chromosome labels on x-axis (1-22, X)
- Add -log10(p) scale on y-axis
- Add horizontal red dashed line at 7.3 with label "P = 5 x 10^-8"
- Add callout boxes pointing to key features:
  - "Lead SNP: rs12345" pointing to peak apex
  - "LD block: ~200 correlated variants" bracket spanning peak width
- Add zoomed inset showing single peak in detail
- Add Q-Q plot inset with lambda annotation

### Fallback Description

Generate using actual GWAS summary statistics:
- Download height GWAS from GWAS Catalog
- Use qqman package in R or matplotlib in Python
- Annotate programmatically with known loci

### Caption

**Recommended Caption:**
"Anatomy of a Manhattan plot from genome-wide association study. Each point represents a tested genetic variant, with genomic position along the x-axis (chromosomes color-alternated) and statistical significance (-log10 p-value) on the y-axis. The horizontal dashed line marks the genome-wide significance threshold (P = 5 x 10^-8). Prominent peaks identify associated loci, but each peak typically contains dozens to hundreds of correlated variants in linkage disequilibrium (LD) rather than a single causal nucleotide. The width of peaks reflects local LD structure. Inset: quantile-quantile (Q-Q) plot comparing observed to expected p-value distributions, with genomic inflation factor (lambda) indicating adequate control of population stratification when near 1.0."

---

## Figure 3.2: Heritability Decomposition

**File:** `figs/part_1/ch03/02-fig-heritability-decomposition.png`
**Priority:** High
**Type:** Nested ring/partition diagram

### Content Description

Conceptual diagram showing nested components of phenotypic variance:

1. **Outer ring:** Total phenotypic variance (100%)
2. **First partition:** Genetic vs Environmental components (e.g., 80/20 for height)
3. **Within genetic:**
   - Additive (narrow-sense h^2) vs Non-additive (dominance, epistasis)
4. **Within additive:**
   - SNP-heritability (what GWAS can capture)
   - "Missing heritability" components:
     - Rare variants
     - Structural variants
     - Imperfect tagging

Annotate with approximate values for height as the example trait.

### DALL-E Prompt

```
Scientific nested ring diagram showing heritability decomposition. Concentric circles partitioned like a sunburst chart. Outermost ring is complete circle (100% phenotypic variance). First partition divides into large blue section (80% genetic) and smaller green section (20% environmental). The blue genetic section is further subdivided into additive and non-additive portions. The additive section is further divided into captured by GWAS (medium blue) and missing heritability (light blue with diagonal stripes). Clean scientific illustration with labeled sections. White background with professional academic diagram style suitable for genetics textbook.
```

### Post-Processing Notes

- Add percentage labels for each partition
- Add descriptive labels: "Genetic (h^2 = 0.80)", "Environmental", "Additive", "SNP-heritability", etc.
- Add legend explaining the missing heritability components
- Consider using example values from height GWAS literature
- Use consistent color scheme: blues for genetic, greens for environmental

### Fallback Description

Create in Python matplotlib using nested pie charts or sunburst plot:
- Use plotly for interactive sunburst
- Or matplotlib nested pie charts
- Add annotations programmatically

### Caption

**Recommended Caption:**
"Decomposition of phenotypic variance for a highly heritable trait (height). The outermost ring represents total phenotypic variance. The first partition separates genetic (blue, ~80%) from environmental (green, ~20%) contributions. Within the genetic component, additive effects (narrow-sense heritability) dominate over non-additive effects (dominance, epistasis). Within additive heritability, SNP-heritability (~50-60% for height) represents variance captured by common variants on genotyping arrays, while the remainder reflects 'missing heritability': rare variants, structural variants, and imperfect tagging of causal alleles. This nested structure explains why GWAS-significant hits explain only a fraction of trait heritability and why polygenic scores built on common variants face a performance ceiling."

---

## Figure 3.3: Linkage Disequilibrium and Tag-Causal Distinction (Three-Panel)

**Files:**
- `figs/part_1/ch03/03-A-fig-ld-tag-causal.png`
- `figs/part_1/ch03/03-B-fig-ld-tag-causal.png`
- `figs/part_1/ch03/03-C-fig-ld-tag-causal.png`

**Priority:** Essential
**Type:** Multi-panel conceptual diagram

### Panel A: Haplotype Diagram

**Content:** Diagram showing how LD creates correlation between variants on the same chromosome segment:
- Multiple horizontal lines representing haplotypes in a population
- Variant positions shown as colored blocks (alleles)
- Causal variant marked with a star
- Tag variants traveling together with causal variant
- Recombination breakpoint shown dividing haplotype blocks

**DALL-E Prompt:**
```
Scientific diagram showing genetic haplotypes for linkage disequilibrium. Six horizontal lines representing different haplotypes in a population. Each line has colored blocks at specific positions representing genetic variants - some blue, some orange. One position marked with a star symbol indicates the causal variant. Variants near the causal variant show the same color pattern across haplotypes (traveling together). A vertical dashed line shows where recombination has broken the pattern. Clean molecular genetics illustration style with white background. Professional academic diagram suitable for genetics textbook.
```

**Caption for Panel A:**
"Haplotype structure and linkage disequilibrium. Each horizontal line represents a haplotype in the population. Variants (colored blocks) at nearby positions tend to travel together on the same ancestral chromosome segments. The causal variant (starred) is correlated with neighboring tag variants because they co-occur on the same haplotypes. Recombination (dashed line) breaks these associations over evolutionary time, but nearby variants remain correlated within haplotype blocks."

### Panel B: LD Matrix (r^2)

**Content:** Triangular heatmap showing pairwise LD (r^2) values for a genomic region:
- Diagonal represents individual variants
- Off-diagonal shows r^2 between variant pairs
- Block structure visible (high LD within blocks, low between)
- Color scale from 0 (white) to 1 (red/dark)

**DALL-E Prompt:**
```
Scientific triangular heatmap showing linkage disequilibrium matrix. Triangle-shaped correlation matrix with variants along the diagonal edge. Color gradient from white (r-squared = 0) to dark red (r-squared = 1). Clear block structure visible with clusters of high correlation (dark red squares) separated by regions of low correlation (white). Several distinct LD blocks visible as dark triangular regions. Clean bioinformatics visualization style with color bar legend. White background with black axis lines. Professional population genetics figure suitable for academic textbook.
```

**Caption for Panel B:**
"Linkage disequilibrium structure across a genomic region. The triangular heatmap displays pairwise r^2 values between variants, with dark red indicating high correlation (r^2 approaching 1) and white indicating low correlation. Haplotype blocks appear as triangular regions of high LD, separated by recombination hotspots where correlation decays rapidly. Fine-mapping must distinguish the causal variant from the many correlated variants within each block."

### Panel C: Population-Specific LD

**Content:** Same causal variant shown in two populations with different LD structure:
- Top: European population with extended LD block, many tags correlated with causal
- Bottom: African population with shorter LD, fewer correlated tags
- Illustrates why PGS portability fails across ancestries

**DALL-E Prompt:**
```
Scientific comparison diagram showing linkage disequilibrium differences between populations. Two horizontal panels stacked vertically. Top panel labeled shows a genomic region with a large red block spanning many variants (extended LD in European population). Bottom panel shows same region with a smaller red block around the causal variant (shorter LD in African population). Both panels have the same causal variant marked with a star in the center. Surrounding variant correlation shown by connecting lines - many in top panel, few in bottom. Clean population genetics illustration with white background. Professional scientific diagram style.
```

**Caption for Panel C:**
"Population-specific linkage disequilibrium affects polygenic score portability. The same causal variant (starred) shows different correlation patterns in populations with distinct demographic histories. In populations with smaller historical effective size (top), extended LD means many tag variants are correlated with the causal allele; polygenic scores using these tags perform well. In populations with larger effective size and shorter LD blocks (bottom), fewer variants remain correlated with the causal allele; tag-based scores lose predictive power because the tag-causal correlation is attenuated or absent."

### Combined Caption

**Full Figure Caption:**
"Linkage disequilibrium and the distinction between causal and tag variants. (A) Haplotype structure showing how nearby variants co-segregate on ancestral chromosome segments. The causal variant (star) is statistically correlated with neighboring tag variants, making them indistinguishable in GWAS. (B) LD matrix displaying pairwise correlations (r^2) across a genomic region, revealing block structure where many variants within blocks show high correlation. (C) Population-specific LD patterns: the same causal variant shows different correlation structures in populations with different demographic histories, explaining why polygenic scores derived in one population transfer poorly to others with different LD patterns."

---

## Figure 3.4: Polygenic Score Construction (Two-Panel)

**Files:**
- `figs/part_1/ch03/04-A-fig-pgs-construction.png`
- `figs/part_1/ch03/04-B-fig-pgs-construction.png`

**Priority:** High
**Type:** Comparative workflow diagram

### Panel A: Clumping and Thresholding (C+T)

**Content:** Workflow showing C+T approach:
1. Start with GWAS summary statistics (Manhattan plot sketch)
2. Apply p-value threshold (variants above line retained)
3. Clump by LD (remove correlated variants, keep lead SNPs)
4. Retain independent lead SNPs only
5. Weight by effect size for final score

Visual emphasis: most variants are discarded.

**DALL-E Prompt:**
```
Scientific workflow diagram showing polygenic score construction using clumping and thresholding. Five connected boxes flowing left to right with arrows. Box 1: Mini Manhattan plot with many dots. Box 2: Same plot with horizontal line, dots below line crossed out. Box 3: Clustered dots with only center dots highlighted, surrounding dots faded. Box 4: Sparse scatter of remaining dots. Box 5: Simple equation showing weighted sum. Large red X symbols over discarded variants. Clean flowchart style with blue boxes and gray arrows. White background. Professional bioinformatics workflow diagram.
```

**Caption for Panel A:**
"Clumping and thresholding (C+T) for polygenic score construction. Starting from GWAS summary statistics, variants failing a p-value threshold are discarded. Remaining variants are clumped by linkage disequilibrium, retaining only the lead SNP from each correlated group. The final score weights retained variants by their GWAS effect sizes. This approach is computationally simple but discards substantial information: most variants are excluded, and the polygenic signal distributed across correlated variants is reduced to sparse independent representatives."

### Panel B: LD-Aware Bayesian Methods (LDpred/PRS-CS)

**Content:** Workflow showing Bayesian approach:
1. Start with same GWAS summary statistics
2. Model LD structure jointly (show LD matrix)
3. Apply shrinkage prior (variants pulled toward zero)
4. Retain all variants with modulated weights
5. Final score uses full variant set

Visual emphasis: information is modeled, not discarded.

**DALL-E Prompt:**
```
Scientific workflow diagram showing Bayesian polygenic score construction. Five connected boxes flowing left to right with arrows. Box 1: Mini Manhattan plot with many dots (same as C+T start). Box 2: Triangular LD correlation matrix. Box 3: Prior distribution curve with arrows pulling effect sizes toward zero. Box 4: All variants retained but with varying sized dots (modulated weights). Box 5: Equation showing sum over all variants. Green checkmarks indicating variants are retained. Clean flowchart style with blue boxes and gray arrows. White background. Professional bioinformatics workflow diagram.
```

**Caption for Panel B:**
"LD-aware Bayesian methods for polygenic score construction (LDpred, PRS-CS). Starting from the same GWAS summary statistics, these methods explicitly model the LD correlation structure using reference panels. Effect size estimates are shrunk toward zero according to a prior distribution, with the degree of shrinkage informed by local LD patterns. All variants contribute to the final score with modulated weights, preserving information that C+T discards. By modeling LD rather than pruning it away, these methods typically achieve higher prediction accuracy for polygenic traits."

### Combined Caption

**Full Figure Caption:**
"Comparison of polygenic score construction approaches. (A) Clumping and thresholding (C+T) applies successive filters to GWAS summary statistics, discarding variants below a p-value threshold and pruning correlated variants to retain only independent lead SNPs. While computationally simple, this approach discards substantial genetic signal. (B) LD-aware Bayesian methods (LDpred, PRS-CS) model the correlation structure explicitly, applying shrinkage priors that modulate effect sizes based on local LD patterns while retaining contributions from all variants. The Bayesian approach preserves information distributed across correlated variants, typically improving prediction accuracy for highly polygenic traits where many variants each contribute small effects."

---

## Figure 3.5: Polygenic Score Portability

**File:** `figs/part_1/ch03/05-fig-pgs-portability.png`
**Priority:** High
**Type:** Bar chart with error bars

### Content Description

Bar chart showing relative prediction accuracy (R^2 or AUC ratio) of European-derived PGS when applied to different ancestry groups:
- European as reference (100% or 1.0)
- East Asian (~70-80%)
- South Asian (~60-70%)
- Hispanic/Latino (~50-60%)
- African ancestry (~25-40%)

Error bars showing uncertainty. Annotations explaining contributing factors:
- LD differences
- Allele frequency differences
- Potential effect heterogeneity
- Training sample size disparities

### DALL-E Prompt

```
Scientific bar chart showing polygenic score prediction accuracy across ancestry groups. Five vertical bars decreasing in height from left to right. First bar (European, reference) is tallest at 100%. Subsequent bars show decreasing accuracy: second bar ~75%, third ~65%, fourth ~55%, fifth ~35%. Each bar has error bars. Horizontal dashed line at 100% for reference. Bars colored in gradient from dark blue (European) to lighter blues. Clean statistical visualization with white background and black axis lines. Professional medical genetics figure suitable for clinical research publication.
```

### Post-Processing Notes

- Add ancestry group labels on x-axis
- Add relative accuracy (%) on y-axis
- Add reference line at 100%
- Add callout annotations explaining factors:
  - "LD structure differences"
  - "Allele frequency divergence"
  - "Effect size heterogeneity"
  - "Training data composition"
- Consider adding world map inset or ancestry icons
- Use color scheme consistent with ancestry representation figure

### Fallback Description

Generate from published meta-analysis data:
- Use data from Martin et al. 2019 or Duncan et al. 2019
- Plot in R ggplot2 or Python seaborn
- Add annotations programmatically

### Caption

**Recommended Caption:**
"Portability of polygenic scores across ancestry groups. Bar heights show relative prediction accuracy when European-derived polygenic scores are applied to individuals of different ancestries, with European performance as the reference (100%). Accuracy declines substantially for non-European populations, with African-ancestry individuals experiencing 40-75% reductions in predictive power. Multiple factors contribute to this portability gap: differences in linkage disequilibrium structure between populations, divergent allele frequencies that alter variant informativeness, potential heterogeneity in effect sizes across genetic backgrounds, and the overwhelming European composition of GWAS training data. These disparities raise fundamental questions about equitable deployment of polygenic risk prediction in diverse clinical populations."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 3.1 Manhattan | 1 | Essential | High (annotated) |
| 3.2 Heritability | 1 | High | Medium (nested diagram) |
| 3.3 LD/Tag-Causal | 3 | Essential | Medium (conceptual) |
| 3.4 PGS Construction | 2 | High | Medium (workflow) |
| 3.5 Portability | 1 | High | Low-Medium (bar chart) |

**Total files:** 8
**Recommended generation order:** 3.5 (data-driven, simplest), 3.2 (conceptual), 3.4A-B (workflow), 3.3A-C (conceptual), 3.1 (most complex, annotated)
# Figure Report: Chapter 4 - Classical Variant Prediction

**Chapter:** Part 1, Chapter 4 - Classical Variant Prediction
**Date:** 2026-01-06
**Figures:** 6 conceptual figures (11 files)

---

## Figure 4.1: Variant Filtering Funnel

**File:** `figs/part_1/ch04/01-fig-variant-funnel.png`
**Priority:** Essential
**Type:** Funnel diagram / Sankey flow

### Content Description

Funnel diagram showing progressive reduction of variant burden through computational filters. Stages with approximate numbers:

1. **Raw variants from WGS:** ~4-5 million
2. **After common variant filter** (gnomAD AF > 1%): ~100,000
3. **After consequence filter** (coding, splice, UTR): ~25,000
4. **After conservation filter** (phyloP > 2): ~5,000
5. **After ensemble predictor** (CADD >= 20): ~500-1,000
6. **Expert review candidates:** ~50-100

Annotations indicating which tools/resources apply at each stage.

### DALL-E Prompt

```
Scientific funnel diagram showing variant filtering in genomic analysis. Inverted triangle shape with six horizontal layers decreasing in width from top to bottom. Top layer is widest (millions of variants). Each subsequent layer is narrower. Numbers decrease at each level: 4 million at top, down to 50 at bottom. Arrows pointing into funnel from left side indicate filtering tools at each stage. Clean infographic style with blue gradient coloring from light (top) to dark (bottom). White background with professional medical genetics visualization style. Labels showing variant counts at each level.
```

### Post-Processing Notes

- Add variant counts at each funnel stage
- Add tool/resource labels on left side:
  - Stage 2: "gnomAD frequency filter"
  - Stage 3: "VEP consequence annotation"
  - Stage 4: "phyloP, GERP conservation"
  - Stage 5: "CADD, REVEL ensemble scores"
  - Stage 6: "Clinical review"
- Add percentage retained at each stage
- Consider color gradient from light (raw) to dark (final candidates)

### Fallback Description

Create in Python/R or diagramming software:
- Use plotly funnel chart
- Or PowerPoint/Keynote with shape tools
- Add annotations programmatically or manually

### Caption

**Recommended Caption:**
"The variant interpretation funnel. Whole-genome sequencing identifies approximately 4-5 million variants per individual. Successive computational filters progressively reduce this burden to a manageable set for expert review. Common variants (allele frequency >1% in gnomAD) are typically excluded as likely benign, reducing the set to ~100,000. Filtering for protein-coding or splice-relevant consequences yields ~25,000 candidates. Conservation filters (phyloP > 2) reduce this to ~5,000, and ensemble predictor thresholds (CADD >= 20) produce several hundred high-priority candidates. The final set for clinical review typically numbers 50-100 variants. Each filter stage applies different resources and reflects different assumptions about which variants merit attention."

---

## Figure 4.2: Conservation Scores (Three-Panel)

**Files:**
- `figs/part_1/ch04/02-A-fig-conservation-scores.png`
- `figs/part_1/ch04/02-B-fig-conservation-scores.png`
- `figs/part_1/ch04/02-C-fig-conservation-scores.png`

**Priority:** High
**Type:** Multi-panel conceptual/statistical

### Panel A: Multiple Sequence Alignment

**Content:** Comparison of:
- Highly conserved position (same nucleotide across 30+ species)
- Neutrally evolving position (variable nucleotides)

Show phylogenetic tree alongside alignment to indicate evolutionary relationships.

**DALL-E Prompt:**
```
Scientific diagram showing multiple sequence alignment for evolutionary conservation. Two side-by-side alignment columns. Left column shows identical letters (all A or all G) across approximately 20 species rows representing high conservation. Right column shows variable letters (mix of A, T, G, C) across the same species representing neutral evolution. Small phylogenetic tree on the left side connecting the species rows. Species names like Human, Chimp, Mouse, Dog etc listed. Clean bioinformatics visualization with monospace font styling. White background with colored nucleotide letters (A=green, T=red, G=yellow, C=blue). Professional molecular evolution figure.
```

**Caption for Panel A:**
"Multiple sequence alignment revealing evolutionary conservation. Each row represents a species, with the phylogenetic tree (left) indicating evolutionary relationships. At the conserved position (left column), the same nucleotide appears across all species, indicating purifying selection has maintained this base over hundreds of millions of years. At the neutrally evolving position (right column), different nucleotides appear across species, consistent with drift in the absence of selective constraint."

### Panel B: Conservation Score Distribution

**Content:** Histogram/density plot of phyloP or GERP scores genome-wide:
- Long right tail representing constrained elements
- Mark threshold zones (e.g., phyloP > 2 = strong evidence)
- Annotate the interpretation of different score ranges

**DALL-E Prompt:**
```
Scientific histogram showing distribution of evolutionary conservation scores across the genome. Bell-shaped distribution centered near zero with a long tail extending to the right (positive values). Most of the distribution is in the neutral range (gray). Right tail colored in blue representing conserved elements. Vertical dashed line at score of 2 marking threshold for strong conservation evidence. X-axis shows conservation score from -5 to 10. Y-axis shows frequency or density. Clean statistical visualization with white background. Professional population genetics figure style.
```

**Caption for Panel B:**
"Genome-wide distribution of phyloP conservation scores. Most genomic positions cluster near zero, consistent with neutral evolution. The long right tail represents positions under purifying selection, where substitutions occur less frequently than expected. Scores above 2 (dashed line) indicate strong conservation evidence, with the position evolving at less than 1% of the neutral rate. These highly conserved positions are enriched for functional elements including coding sequences, splice sites, and regulatory regions."

### Panel C: Intronic Variant Example

**Content:** Example of an intronic variant at a deeply conserved position with no other annotation:
- Genome browser view showing variant position
- Conservation track showing deep conservation
- Annotation tracks showing absence of other functional marks
- Illustrates how conservation provides evidence in annotation-sparse regions

**DALL-E Prompt:**
```
Scientific genome browser view showing an intronic variant. Horizontal tracks stacked vertically. Top track shows gene model with exons as boxes and introns as thin lines. Second track shows a red diamond marking variant position in intron. Third track shows conservation score as a line graph with a prominent peak at the variant position (high conservation). Fourth and fifth tracks show flat lines (no ChIP-seq or other annotations at this position). Highlight box around the variant position. Clean bioinformatics browser interface style with white background. Professional genomics visualization.
```

**Caption for Panel C:**
"Conservation as evidence in annotation-sparse regions. This genome browser view shows an intronic variant (red diamond) with no overlapping regulatory annotations. The conservation track (third row) reveals a deep conservation peak at this position, indicating the base has been maintained across mammalian evolution despite lying outside any annotated functional element. Such conservation provides strong evidence of functional importance even when no explicit annotation explains the mechanism. This variant would warrant investigation for effects on splicing regulation or other intronic functions."

### Combined Caption

**Full Figure Caption:**
"Evolutionary conservation as a proxy for functional importance. (A) Multiple sequence alignment comparing a highly conserved position (left, same nucleotide across species) with a neutrally evolving position (right, variable nucleotides). Phylogenetic tree indicates evolutionary relationships. (B) Genome-wide distribution of phyloP scores, with most positions near zero (neutral) and a long right tail representing constrained elements. Positions with scores above 2 show strong evidence of purifying selection. (C) Genome browser view of an intronic variant with no regulatory annotations but deep conservation, illustrating how evolutionary signal provides evidence of function in annotation-sparse regions."

---

## Figure 4.3: ACMG-AMP Classification Box

**File:** `figs/part_1/ch04/03-box-acmg-amp.png`
**Priority:** High
**Type:** Classification framework diagram

### Content Description

ACMG-AMP five-tier classification system showing:
- Five classification tiers: Pathogenic, Likely Pathogenic, VUS, Likely Benign, Benign
- Evidence categories and their strength levels:
  - Pathogenic: PVS (very strong), PS (strong), PM (moderate), PP (supporting)
  - Benign: BA (stand-alone), BS (strong), BP (supporting)
- Computational predictions (PP3/BP4) occupy the supporting tier
- Combination rules for reaching final classification

### DALL-E Prompt

```
Scientific classification framework diagram for clinical variant interpretation. Central column shows five classification categories from top to bottom: Pathogenic (red), Likely Pathogenic (orange), VUS (gray), Likely Benign (light green), Benign (green). Left side shows pathogenic evidence types arranged in strength levels (PVS, PS, PM, PP) with arrows pointing toward pathogenic categories. Right side shows benign evidence types (BA, BS, BP) with arrows pointing toward benign categories. Evidence boxes are sized by strength. PP3 and BP4 boxes highlighted or outlined as computational evidence. Clean medical genetics classification diagram with white background. Professional clinical genetics figure style.
```

### Post-Processing Notes

- Add clear labels for all evidence codes
- Highlight PP3 (computational supporting pathogenicity) and BP4 (computational supporting benign)
- Add example evidence types for each category
- Add combination rule annotations or legend
- Use red-orange-gray-green color gradient for classification tiers

### Fallback Description

Create in diagramming software:
- Use table format or flowchart
- Color-code classification tiers
- Add evidence code boxes with arrows to appropriate tiers

### Caption

**Recommended Caption:**
"The ACMG-AMP framework for clinical variant classification. Variants are classified into five tiers based on combined evidence: Pathogenic (red), Likely Pathogenic (orange), Variant of Uncertain Significance (gray), Likely Benign (light green), and Benign (green). Pathogenic evidence is categorized by strength: very strong (PVS), strong (PS), moderate (PM), and supporting (PP). Benign evidence follows a parallel structure: stand-alone (BA), strong (BS), and supporting (BP). Computational predictions occupy the supporting tier (PP3 for predicted damaging, BP4 for predicted benign), reflecting appropriate caution about their evidentiary weight. Definitive classification requires combining multiple independent lines of evidence according to specified rules."

---

## Figure 4.4: CADD Training Paradigm (Three-Panel)

**Files:**
- `figs/part_1/ch04/04-A-fig-cadd-training.png`
- `figs/part_1/ch04/04-B-fig-cadd-training.png`
- `figs/part_1/ch04/04-C-fig-cadd-training.png`

**Priority:** Essential
**Type:** Conceptual machine learning diagram

### Panel A: Proxy-Neutral Class

**Content:** Human-derived alleles fixed since human-chimpanzee split:
- Evolutionary tree with human branch highlighted
- Variants that survived selection representing tolerated changes
- High derived allele frequency = survived purifying selection

**DALL-E Prompt:**
```
Scientific evolutionary tree diagram for genomic training data. Phylogenetic tree showing divergence of human lineage from chimpanzee approximately 6 million years ago. Human branch highlighted in blue with small colored dots along the branch representing accumulated mutations. Arrow pointing to these dots labeled as tolerated variants. Great ape silhouettes at branch tips. Timeline scale at bottom. Clean molecular evolution illustration with white background. Professional scientific diagram style suitable for machine learning paper in genetics.
```

**Caption for Panel A:**
"Proxy-neutral training class for CADD. Variants in the proxy-neutral class are derived alleles that arose on the human lineage since the human-chimpanzee divergence and reached high frequency in modern humans. These variants have survived millions of years of purifying selection, making them enriched for tolerated (non-deleterious) changes. The evolutionary tree highlights the human branch where these variants accumulated."

### Panel B: Proxy-Deleterious Class

**Content:** Simulated variants matching human mutational processes:
- Mutation simulation schematic with trinucleotide context
- Mutation spectrum showing CpG enrichment
- These represent possible-but-not-observed mutations enriched for deleterious effects

**DALL-E Prompt:**
```
Scientific diagram showing mutation simulation for genomic training data. DNA sequence shown with trinucleotide context highlighted (three adjacent bases). Arrows showing mutation process transforming one nucleotide to another. Bar chart showing mutation spectrum with different types (C>T, CpG transitions being tallest bar). Scattered simulated variant positions across a schematic chromosome. Clean molecular biology illustration style. White background with blue and orange color scheme. Professional bioinformatics figure suitable for machine learning methodology paper.
```

**Caption for Panel B:**
"Proxy-deleterious training class for CADD. Simulated variants are generated across the genome according to realistic mutational processes, matching the trinucleotide context and regional variation of human germline mutation. The mutation spectrum shows elevated rates at CpG dinucleotides due to spontaneous deamination of methylated cytosines. These simulated variants represent changes that could plausibly occur but are generally not observed at high frequency in populations, making them enriched for alleles disfavored by selection."

### Panel C: Classification Learning

**Content:** Machine learning classifier distinguishing the two classes:
- SVM or logistic regression decision boundary
- Feature space with proxy-neutral and proxy-deleterious variants
- Output is "evolutionary tolerance" score, not pathogenicity directly
- Feature list showing integrated annotations

**DALL-E Prompt:**
```
Scientific machine learning classification diagram. Two-dimensional scatter plot with two classes of points: blue circles (tolerated) clustered in one region and orange triangles (simulated) in another. Diagonal decision boundary line separating the classes. Arrows pointing to feature inputs: conservation scores, protein features, regulatory annotations. Arrow from classifier to output showing PHRED-scaled score. Clean machine learning visualization with white background. Professional computational biology figure style. Simple and clear academic diagram.
```

**Caption for Panel C:**
"CADD classification learning. A support vector machine (later versions: logistic regression) learns to distinguish proxy-neutral from proxy-deleterious variants based on dozens of genomic annotations including conservation scores, protein-level predictions, and regulatory features. The output is a score reflecting 'evolutionary tolerance' rather than pathogenicity directly. Variants similar to the proxy-deleterious class receive high CADD scores, while those similar to proxy-neutral variants receive low scores. The PHRED-scaled output indicates the variant's percentile rank among all possible genomic mutations."

### Combined Caption

**Full Figure Caption:**
"The CADD training paradigm: evolutionary proxy labeling. (A) The proxy-neutral class consists of human-derived alleles that reached high frequency since the human-chimpanzee split, having survived millions of years of purifying selection. (B) The proxy-deleterious class comprises simulated variants matching human mutational processes, representing changes that could occur but are generally not observed at high frequency, enriching for alleles disfavored by selection. (C) A classifier learns to distinguish these classes based on integrated genomic annotations, outputting an 'evolutionary tolerance' score. This proxy labeling strategy transforms the variant effect prediction problem from one with scarce clinical labels to one with millions of evolutionary training examples, though the gap between evolutionary tolerance and clinical pathogenicity remains irreducible."

---

## Figure 4.5: Ensemble Method Performance

**File:** `figs/part_1/ch04/05-fig-ensemble-performance.png`
**Priority:** High
**Type:** ROC curve comparison

### Content Description

ROC curves (or precision-recall curves) comparing variant effect predictors on a held-out benchmark of missense variants:

Methods to compare:
- CADD
- REVEL
- M-CAP
- Individual component scores (SIFT, PolyPhen-2, phyloP)

Annotations:
- Mark operating points for common clinical thresholds
- CADD >= 20
- REVEL >= 0.75
- M-CAP "possibly pathogenic"
- Show sensitivity and specificity at each threshold
- Include note about benchmark circularity caveats

### DALL-E Prompt

```
Scientific ROC curve comparison for variant effect predictors. Plot with false positive rate (0 to 1) on x-axis and true positive rate (0 to 1) on y-axis. Multiple curved lines representing different methods, each in different color. Top curves (better performance) shown in solid lines for ensemble methods. Lower curves shown in dashed lines for individual component scores. Diagonal dashed line showing random performance. Small circular markers on curves indicating clinical threshold operating points. Legend in corner listing method names. Clean statistical visualization with white background and grid lines. Professional bioinformatics ROC plot style.
```

### Post-Processing Notes

- Add legend with method names and AUC values
- Mark operating points with symbols and labels
- Add sensitivity/specificity values at key thresholds
- Include horizontal lines at key sensitivity levels
- Add footnote about benchmark circularity caveat
- Use consistent color scheme for methods

### Fallback Description

Generate from published benchmark data:
- Use data from REVEL, M-CAP, or ClinVar benchmark papers
- Plot in R pROC or Python sklearn
- Add annotations programmatically

### Caption

**Recommended Caption:**
"Performance comparison of variant effect predictors on a held-out missense variant benchmark. ROC curves compare ensemble methods (CADD, REVEL, M-CAP; solid lines) against individual component scores (SIFT, PolyPhen-2, phyloP; dashed lines). Ensemble methods consistently outperform individual predictors by integrating multiple signals. Circular markers indicate common clinical operating thresholds with corresponding sensitivity and specificity values. Note that benchmark performance may be inflated by circularity: variants classified using these same predictors appear in clinical databases that form the evaluation set. True clinical utility may be lower than benchmark metrics suggest, particularly for novel variants in understudied genes."

---

## Figure 4.6: Circularity Problem

**File:** `figs/part_1/ch04/06-fig-circularity-problem.png`
**Priority:** High
**Type:** Circular/feedback diagram

### Content Description

Circular diagram illustrating the feedback loop between computational predictors and clinical databases:

1. Computational score (e.g., high CADD) influences clinical classification
2. Classified variant enters ClinVar as "Pathogenic"
3. Benchmarking study evaluates CADD on ClinVar variants
4. High benchmark performance encourages clinical adoption
5. Return to step 1 (cycle continues)

Indicate intervention points:
- Temporal holdouts
- Functional assay ground truth
- Prospective evaluation

Visual metaphor of self-reinforcing spiral.

### DALL-E Prompt

```
Scientific circular diagram showing feedback loop between computational predictions and clinical databases. Five connected nodes arranged in a circle with arrows flowing clockwise between them. Node 1: Computer icon (computational prediction). Node 2: Medical document icon (clinical classification). Node 3: Database cylinder icon (enters ClinVar). Node 4: Graph/chart icon (benchmark evaluation). Node 5: Checkmark/adoption icon (clinical uptake). Arrows connecting nodes in continuous loop. Spiral visual suggesting self-reinforcing cycle. Break points marked with scissors or intervention icons. Clean infographic style with blue and orange colors. White background. Professional clinical informatics diagram.
```

### Post-Processing Notes

- Add clear labels for each node in the cycle
- Add arrows with brief descriptions of the process
- Mark intervention points (temporal holdouts, functional assays, prospective evaluation)
- Consider spiral visual effect to emphasize reinforcement
- Add warning symbols or highlights for problematic links
- Include legend explaining intervention strategies

### Fallback Description

Create in diagramming software:
- Use circular flowchart template
- Add icons for each stage
- Add intervention point annotations
- Use color to distinguish problem areas from solutions

### Caption

**Recommended Caption:**
"The circularity problem in variant effect prediction. A self-reinforcing feedback loop operates between computational predictors and clinical databases. (1) A high computational score (e.g., CADD) contributes evidence supporting a pathogenic classification. (2) The classified variant enters ClinVar. (3) Benchmarking studies evaluate computational predictors on ClinVar variants. (4) Apparent high performance encourages clinical adoption. (5) Greater clinical use increases the influence of computational scores on future classifications, returning to step 1. This circularity inflates benchmark performance metrics because predictors are evaluated on labels they helped create. Intervention strategies include temporal holdouts (evaluating only on classifications made before predictor adoption), functional assay ground truth (using experimentally measured variant effects), and prospective evaluation (testing on newly classified variants not yet influenced by the predictor)."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 4.1 Variant Funnel | 1 | Essential | Medium (infographic) |
| 4.2 Conservation | 3 | High | Medium (multi-panel) |
| 4.3 ACMG-AMP | 1 | High | Medium (framework) |
| 4.4 CADD Training | 3 | Essential | Medium (conceptual ML) |
| 4.5 Ensemble ROC | 1 | High | Low-Medium (statistical) |
| 4.6 Circularity | 1 | High | Medium (conceptual) |

**Total files:** 11
**Recommended generation order:** 4.5 (data-driven, simplest), 4.1 (infographic), 4.3 (framework), 4.6 (conceptual), 4.2A-C (multi-panel), 4.4A-C (ML conceptual)
# Figure Report: Chapter 5 - Tokens and Embeddings

**Chapter:** Part 2, Chapter 5 - Tokens and Embeddings
**Date:** 2026-01-07
**Figures:** 4 conceptual figures (9 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 5.1: Tokenization Comparison (Four-Panel)

**Files:**
- `figs/part_2/ch05/01-A-fig-ch05-tokenization-comparison.svg`
- `figs/part_2/ch05/01-B-fig-ch05-tokenization-comparison.svg`
- `figs/part_2/ch05/01-C-fig-ch05-tokenization-comparison.svg`
- `figs/part_2/ch05/01-D-fig-ch05-tokenization-comparison.svg`

**Priority:** Essential
**Type:** Multi-panel comparative diagram

### Panel A: One-Hot Encoding

**Content:** Show a ~30-nucleotide regulatory sequence as a 4×30 binary matrix with color-coded nucleotides (A=green, T=red, G=yellow, C=blue). Each column has exactly one "1" value. Annotate: "30 tokens, 1 per nucleotide, no compression."

**DALL-E Prompt:**
```
Scientific diagram showing one-hot encoding of DNA sequence. A horizontal matrix visualization with 4 rows (labeled A, C, G, T) and approximately 30 columns. Each column has one filled cell (colored block) and three empty cells, creating a sparse binary pattern. Colors: A=green, C=blue, G=yellow, T=red. Clean bioinformatics visualization style. White background with thin grid lines. Professional machine learning diagram suitable for academic textbook.
```

**Caption for Panel A:**
"One-hot encoding preserves single-nucleotide resolution. Each nucleotide becomes a 4-dimensional binary vector with a single active element. A 30-bp sequence produces 30 tokens with no compression, maintaining maximum resolution for variant-level analysis."

### Panel B: Overlapping 6-mers

**Content:** Same sequence showing overlapping 6-mer tokens. Use brackets to show how adjacent tokens share 5 nucleotides. Annotate: "~30 tokens due to overlap, 4,096 vocabulary size."

**DALL-E Prompt:**
```
Scientific diagram showing overlapping k-mer tokenization of DNA. Horizontal DNA sequence with colored nucleotide letters. Multiple overlapping brackets below the sequence, each spanning 6 nucleotides, with each bracket shifted by 1 position from the previous. Brackets overlap heavily, sharing 5 of 6 positions. Clean bioinformatics visualization with white background. Professional tokenization diagram for machine learning textbook.
```

**Caption for Panel B:**
"Overlapping k-mer tokenization (DNABERT style) groups 6 consecutive nucleotides as tokens. Adjacent tokens share 5 nucleotides, providing no sequence compression despite larger vocabulary. A single-nucleotide variant affects 6 different tokens, complicating variant interpretation."

### Panel C: BPE Tokenization

**Content:** Same sequence with variable-length non-overlapping BPE tokens. Mark token boundaries showing compression of repetitive regions into single tokens while unique regions have shorter tokens. Annotate: "~10-15 tokens, variable compression."

**DALL-E Prompt:**
```
Scientific diagram showing byte-pair encoding tokenization of DNA sequence. Horizontal DNA sequence with colored nucleotides grouped into variable-length segments. Some segments are long (6-10 nucleotides) for common patterns, others are short (1-3 nucleotides) for unique regions. Token boundaries marked with vertical lines. Segments do not overlap. Clean bioinformatics visualization style. White background. Professional NLP/genomics hybrid diagram.
```

**Caption for Panel C:**
"Byte-pair encoding (BPE) learns variable-length tokens from corpus statistics. Frequent patterns (repetitive elements, common motifs) merge into longer tokens, achieving 2-5x compression. Rare sequences decompose into shorter units. Token boundaries depend on context, affecting variant localization."

### Panel D: Single-Nucleotide (Hyena/Mamba)

**Content:** Same sequence with single-nucleotide tokens but with learned embedding vectors indicated for each position. Show the 4-token vocabulary with embedding arrows. Annotate: "30 tokens, 4-5 vocabulary, learned embeddings."

**DALL-E Prompt:**
```
Scientific diagram showing single-nucleotide tokenization with learned embeddings. Horizontal DNA sequence with individual nucleotide letters. Below each nucleotide, a small arrow pointing to an embedding vector (shown as a colored bar or small matrix column). A small legend shows the 4-nucleotide vocabulary (A, C, G, T) each mapping to an embedding. Clean minimalist bioinformatics style. White background. Professional deep learning architecture diagram.
```

**Caption for Panel D:**
"Single-nucleotide tokenization (HyenaDNA, Caduceus) maintains maximum resolution with minimal vocabulary. Learned embeddings transform discrete nucleotides into continuous representations. Sub-quadratic architectures make million-base contexts feasible without sacrificing single-nucleotide precision for variant interpretation."

### Combined Caption

**Full Figure Caption:**
"Tokenization strategies for genomic sequences. (A) One-hot encoding produces one token per nucleotide as a sparse 4-dimensional binary vector, preserving maximum resolution. (B) Overlapping 6-mer tokenization groups nucleotides into 4,096 possible tokens but provides no compression since each nucleotide generates its own token. (C) Byte-pair encoding creates variable-length non-overlapping tokens learned from corpus statistics, achieving genuine compression of repetitive regions. (D) Single-nucleotide tokenization with learned embeddings combines maximum resolution with rich representations, enabled by sub-quadratic architectures that circumvent attention's quadratic scaling. Each strategy encodes different assumptions about which patterns matter for downstream prediction."

---

## Figure 5.2: Biologically-Informed Tokenization

**File:** `figs/part_2/ch05/02-fig-ch05-biological-tokenization.svg`
**Priority:** Enhancing
**Type:** Comparative gene structure diagram

### Content Description

Side-by-side comparison on a gene structure diagram showing:
1. **Standard BPE**: Token boundaries crossing codon boundaries arbitrarily in coding regions
2. **Codon-aware tokenization**: Reading frame respected with 64-codon vocabulary in coding regions
3. **BioToken-style**: Explicit variant tokens, regulatory element markers, and structural annotations integrated

Show exons as boxes, introns as thin lines. Highlight how biological structure can be encoded directly.

### DALL-E Prompt

```
Scientific comparison diagram showing three tokenization approaches on a gene structure. Top row shows gene schematic with exons (boxes) and introns (thin lines). Three horizontal panels below: Panel 1 shows arbitrary token boundaries crossing codon triplets. Panel 2 shows token boundaries aligned with codon triplets in exons, respecting reading frame. Panel 3 shows tokens with special symbols for variants (diamond), regulatory elements (star), and structural features (circle). Clean molecular biology illustration style. White background. Professional genomics/ML hybrid diagram.
```

### Post-Processing Notes

- Add clear labels for each tokenization approach
- Annotate codon boundaries in the coding regions
- Use color coding to distinguish exons from introns
- Add legend explaining special token types in BioToken panel

### Fallback Description

Create in diagramming software (BioRender, Inkscape):
- Gene structure schematic with exon boxes and intron lines
- Three rows showing different tokenization approaches
- Use color and symbols to distinguish token types

### Caption

**Recommended Caption:**
"Biologically-informed tokenization strategies. Standard BPE (top) tokenizes across codon boundaries in coding regions, potentially obscuring the fundamental three-nucleotide unit of protein translation. Codon-aware tokenization (middle, as in GenSLMs and Life-Code) respects reading frame, with each codon becoming a single token from a 64-element vocabulary. This alignment with biological structure enables learning synonymous versus nonsynonymous substitution patterns directly. BioToken-style tokenization (bottom) extends further by incorporating explicit variant tokens, regulatory element markers, and structural annotations, treating tokens as rich entities bundling sequence with functional context."

---

## Figure 5.3: Embedding Space Visualization (Three-Panel)

**Files:**
- `figs/part_2/ch05/03-A-fig-ch05-embedding-space.svg`
- `figs/part_2/ch05/03-B-fig-ch05-embedding-space.svg`
- `figs/part_2/ch05/03-C-fig-ch05-embedding-space.svg`

**Priority:** High
**Type:** UMAP/t-SNE dimensionality reduction plots

### Panel A: GC Content

**Content:** UMAP or t-SNE visualization of k-mer or BPE token embeddings from a trained DNA language model. Points colored by GC content on a gradient from AT-rich (red/orange) to GC-rich (blue/purple). Should show clear clustering/gradients by GC content.

**DALL-E Prompt:**
```
Scientific UMAP dimensionality reduction plot showing DNA token embeddings. Scattered points forming organic cluster shapes. Color gradient from warm red/orange (AT-rich) on one side to cool blue/purple (GC-rich) on the other side. Smooth color transition across the embedding space. Clean data visualization style with white background and minimal axis lines. Professional bioinformatics embedding visualization. No text labels on points.
```

**Caption for Panel A:**
"Token embeddings organized by GC content. UMAP visualization of learned embeddings from a DNA language model reveals that GC content emerges as a major axis of organization, with AT-rich tokens (red/orange) segregating from GC-rich tokens (blue/purple). This structure emerges without explicit GC supervision, reflecting the many functional properties that correlate with base composition."

### Panel B: Token Frequency

**Content:** Same embedding space colored by token frequency (common vs. rare). Common tokens cluster together, rare tokens appear in different regions.

**DALL-E Prompt:**
```
Scientific UMAP plot showing DNA token embeddings colored by frequency. Scattered points forming cluster shapes. Color gradient from dark blue (very common tokens, densely clustered) to light yellow/white (rare tokens, more scattered). Some distinct regions have predominantly dark or light coloring. Clean data visualization style with white background. Professional machine learning embedding visualization.
```

**Caption for Panel B:**
"Token embeddings organized by corpus frequency. Common tokens (dark blue) cluster distinctly from rare tokens (light yellow), reflecting that frequently co-occurring sequences develop similar representations. This organization enables the model to treat rare sequences as compositions of common subunits while dedicating representation capacity to frequent patterns."

### Panel C: Genomic Context

**Content:** Same embedding space colored by genomic context: coding (blue), regulatory (green), repetitive (gray). Shows distinct clustering by functional category.

**DALL-E Prompt:**
```
Scientific UMAP plot showing DNA token embeddings colored by genomic context. Scattered points in distinct cluster regions. Three main colors: blue for coding regions (forming one cluster area), green for regulatory regions (different area), gray for repetitive elements (third area). Some mixing at boundaries. Clean data visualization with white background. Professional genomics bioinformatics visualization.
```

**Caption for Panel C:**
"Token embeddings organized by genomic context. Despite no explicit context labels during pretraining, coding tokens (blue), regulatory tokens (green), and repetitive elements (gray) occupy distinct regions of embedding space. This emergent organization reflects learned patterns that distinguish sequence function without supervision."

### Combined Caption

**Full Figure Caption:**
"Emergent structure in learned DNA token embeddings. UMAP projections of token embeddings from a trained DNA language model reveal biologically meaningful organization that emerges without explicit supervision. (A) GC content creates a major gradient, with AT-rich and GC-rich tokens segregating. (B) Token frequency organizes embeddings, with common tokens clustering distinctly from rare tokens. (C) Genomic context (coding, regulatory, repetitive) corresponds to distinct embedding regions. This organization demonstrates that pretraining on sequence prediction objectives induces representations capturing genuine biological structure."

---

## Figure 5.4: Compression vs. Resolution Tradeoff

**File:** `figs/part_2/ch05/04-fig-ch05-compression-resolution.svg`
**Priority:** High
**Type:** Two-axis plot / strategic positioning diagram

### Content Description

Two-axis plot with:
- **X-axis:** Sequence compression (tokens per kilobase, from ~1000 to ~200)
- **Y-axis:** Nucleotide resolution (from low to high)

Position different approaches as labeled points:
- One-hot/single-nucleotide: Top-left (no compression, full resolution)
- Overlapping k-mers: Top-left (no compression, k-nucleotide resolution)
- Non-overlapping k-mers: Middle (k-fold compression, k-nucleotide resolution)
- BPE: Middle-right (variable compression, variable resolution)

Annotate practical context lengths achievable with standard transformers (~4K tokens).

Include callout showing clinical implication: "Single SNP affects..." with number of tokens per approach.

### DALL-E Prompt

```
Scientific two-axis plot comparing tokenization strategies. X-axis labeled "Sequence Compression" from low to high. Y-axis labeled "Nucleotide Resolution" from low to high. Four or five labeled points positioned in different quadrants representing different tokenization methods. Diagonal dashed line showing tradeoff. Annotation boxes with practical implications. Clean strategic positioning diagram style with white background, grid lines. Professional machine learning architecture comparison diagram.
```

### Post-Processing Notes

- Add method labels (One-hot, k-mers, BPE, Single-nucleotide)
- Add annotation for context length with standard 4K token transformers
- Add clinical callout showing SNP token impact
- Use consistent colors matching earlier figures

### Fallback Description

Create in matplotlib or diagramming software:
- Scatter plot with strategic positioning
- Add labeled points for each tokenization strategy
- Include annotation boxes for practical implications

### Caption

**Recommended Caption:**
"The compression-resolution tradeoff in genomic tokenization. This plot positions tokenization strategies along two axes: sequence compression (tokens per kilobase) and nucleotide resolution. One-hot and single-nucleotide tokenization occupy the upper-left corner, providing maximum resolution with no compression. Overlapping k-mers also provide no compression but reduce resolution to k-nucleotide granularity. Non-overlapping k-mers and BPE occupy the middle ground, trading resolution for compression that enables longer context windows with standard transformer architectures. The clinical implication appears in variant interpretation: a single-nucleotide polymorphism affects 1 token with single-nucleotide tokenization but k tokens with overlapping k-mers, complicating effect attribution. Sub-quadratic architectures (HyenaDNA, Caduceus) escape this tradeoff entirely, enabling full resolution at any context length."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 5.1 Tokenization Comparison | 4 | Essential | Medium (multi-panel) |
| 5.2 Biological Tokenization | 1 | Enhancing | Medium (gene diagram) |
| 5.3 Embedding Space | 3 | High | Medium (UMAP plots) |
| 5.4 Compression-Resolution | 1 | High | Low-Medium (positioning) |

**Total files:** 9
**Recommended generation order:** 5.4 (strategic diagram), 5.3A-C (UMAP plots), 5.1A-D (comparison panels), 5.2 (gene diagram)
# Figure Report: Chapter 6 - Convolutional Networks

**Chapter:** Part 2, Chapter 6 - Convolutional Networks
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (10 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 6.1: Convolution as Pattern Detector (Three-Panel)

**Files:**
- `figs/part_2/ch06/01-A-fig-conv-pattern-detector.svg`
- `figs/part_2/ch06/01-B-fig-conv-pattern-detector.svg`
- `figs/part_2/ch06/01-C-fig-conv-pattern-detector.svg`

**Priority:** Essential
**Type:** Multi-panel conceptual/technical diagram

### Panel A: Sliding Convolution

**Content:** Single convolutional filter (width 8) sliding across one-hot encoded DNA. Show the 4×8 filter weight matrix sliding over a 4×L input matrix. At each position, compute a dot product yielding an activation score. Highlight one position where the filter matches a motif (high activation) versus positions with low activation.

**DALL-E Prompt:**
```
Scientific diagram showing convolutional filter sliding across DNA sequence. Horizontal one-hot encoded DNA matrix (4 rows for A,C,G,T, many columns). A small 4x8 filter window highlighted in blue sliding from left to right. At the current position, show high activation (bright color) where filter matches sequence pattern. Below, a graph showing activation scores across positions with one prominent peak. Clean machine learning diagram style. White background. Professional deep learning textbook illustration.
```

**Caption for Panel A:**
"Convolutional filter as sliding pattern detector. A filter of width 8 nucleotides slides across one-hot encoded DNA, computing similarity scores at each position. The filter produces high activation where the input matches its learned weight pattern and low activation elsewhere. This sliding window operation detects motifs regardless of their position in the input sequence."

### Panel B: Learned Filter as Sequence Logo

**Content:** Visualization of learned filter weights as a sequence logo (PWM-style), with letter heights proportional to weights. Align with a corresponding JASPAR motif to show the biological pattern discovered.

**DALL-E Prompt:**
```
Scientific comparison diagram showing learned CNN filter and known transcription factor motif. Top: Sequence logo with stacked nucleotide letters (A,C,G,T) at 8 positions, letter heights varying by weight, creating characteristic DNA motif visualization. Bottom: Similar sequence logo from JASPAR database showing matching pattern. Alignment lines connecting corresponding positions. Clean bioinformatics sequence logo style. White background. Professional motif comparison visualization.
```

**Caption for Panel B:**
"Learned filter weights visualized as sequence logo. The filter weights are transformed into a position weight matrix format, with nucleotide letter heights proportional to learned weights. This visualization reveals that the filter has learned to recognize the CTCF binding motif, matching the experimentally derived consensus from the JASPAR database despite no explicit motif supervision during training."

### Panel C: Multiple Filter Diversity

**Content:** Array of multiple first-layer filters, each detecting different motifs. Show 4-6 filters with their sequence logo representations and biological labels (CTCF, ETS, AP-1, TATA box, etc.).

**DALL-E Prompt:**
```
Scientific panel showing multiple DNA sequence logos arranged in a grid (2x3 or 3x2). Each logo shows a different 8-10 nucleotide pattern with characteristic letter stacks. Labels below each: CTCF, ETS, AP-1, TATA. Different color schemes for each motif. Clean bioinformatics visualization. White background with subtle borders between panels. Professional transcription factor motif collection diagram.
```

**Caption for Panel C:**
"Diversity of first-layer filters. Different filters in the first convolutional layer learn to detect distinct transcription factor binding motifs: CTCF (insulator), ETS family, AP-1, and TATA box (core promoter). This diverse pattern detection emerges from training on chromatin accessibility data without explicit motif labels, demonstrating that the chromatin prediction objective induces biologically meaningful feature extraction."

### Combined Caption

**Full Figure Caption:**
"Convolutional filters as learned position weight matrices. (A) A filter of width 8 slides across one-hot encoded DNA, producing activation scores at each position. High activation indicates sequence matching the learned pattern. (B) Visualizing filter weights as sequence logos reveals correspondence to known transcription factor motifs. This filter has learned the CTCF binding site consensus matching the JASPAR database entry. (C) Multiple first-layer filters detect diverse motifs including CTCF, ETS, AP-1, and TATA box elements. This specialization emerges from training on chromatin prediction without explicit motif supervision."

---

## Figure 6.2: DeepSEA Architecture (Three-Panel)

**Files:**
- `figs/part_2/ch06/02-A-fig-deepsea-architecture.svg`
- `figs/part_2/ch06/02-B-fig-deepsea-architecture.svg`
- `figs/part_2/ch06/02-C-fig-deepsea-architecture.svg`

**Priority:** High
**Type:** Architecture schematic and validation

### Panel A: Architecture Schematic

**Content:** Network architecture showing: Input (1000bp one-hot, 4×1000) → Conv1 (320 filters) → MaxPool → Conv2 (480 filters) → MaxPool → Conv3 (960 filters) → MaxPool → Flatten → FC (925 units) → 919 sigmoid outputs for chromatin features. Show dimension changes at each layer.

**DALL-E Prompt:**
```
Scientific neural network architecture diagram. Left to right flow: Input matrix (4x1000) → three convolutional layer blocks with pooling (labeled 320, 480, 960 filters), decreasing in width. → Flatten operation → Fully connected layer (925 units) → Output layer with 919 sigmoid units arranged as a vertical bar. Clean deep learning architecture diagram with blue/gray color scheme. White background. Professional ML textbook illustration showing layer dimensions.
```

**Caption for Panel A:**
"DeepSEA architecture schematic. Input sequences of 1,000 base pairs (one-hot encoded as 4×1000 matrix) pass through three convolutional layers with 320, 480, and 960 filters respectively. Max pooling after each convolution compresses spatial dimensions. A fully connected layer integrates information, and 919 sigmoid outputs independently predict chromatin features from ENCODE and Roadmap Epigenomics."

### Panel B: First-Layer Filter Motif Match

**Content:** Single learned filter visualized as sequence logo, aligned with JASPAR CTCF motif showing high similarity. Include sequence alignment and correlation metric.

**DALL-E Prompt:**
```
Scientific sequence logo comparison. Two DNA sequence logos aligned vertically. Top logo labeled "Learned Filter" with nucleotide stacks. Bottom logo labeled "JASPAR CTCF" with similar nucleotide stacks. Dashed lines connecting matching positions. Correlation score (r = 0.92) displayed. Clean bioinformatics motif comparison style. White background. Professional validation figure.
```

**Caption for Panel B:**
"Learned filter matches known transcription factor motif. A first-layer filter from trained DeepSEA (top) shows high correspondence to the experimentally determined CTCF binding motif from JASPAR (bottom). This alignment emerges from training to predict chromatin accessibility, not from explicit motif supervision, confirming that the model learns biologically meaningful sequence patterns."

### Panel C: Allelic Imbalance Validation

**Content:** Scatter plot showing predicted versus observed allelic imbalance for DNase-seq variants. Show correlation, with points colored by prediction confidence. Reference line at y=x.

**DALL-E Prompt:**
```
Scientific scatter plot for model validation. X-axis labeled "Predicted Allelic Imbalance", Y-axis "Observed Allelic Imbalance". Points scattered around diagonal reference line, showing positive correlation. Points colored by density or confidence (dark = high, light = low). Correlation coefficient displayed (r = 0.XX). Clean statistical visualization with white background and grid lines. Professional genomics validation figure.
```

**Caption for Panel C:**
"Variant effect prediction validated by allelic imbalance. DeepSEA's predicted chromatin effects correlate with experimentally observed allelic imbalance in DNase-seq (r = 0.XX). Variants predicted to increase accessibility (positive values) show corresponding experimental bias toward that allele. This correlation confirms that in silico mutagenesis captures genuine variant effects despite never training on variant data."

### Combined Caption

**Full Figure Caption:**
"DeepSEA: regulatory prediction from sequence. (A) Architecture schematic showing progression from 1,000 bp one-hot input through three convolutional layers to 919 chromatin feature predictions. (B) First-layer filters learn to recognize known transcription factor motifs, with this example matching JASPAR's CTCF consensus. (C) Variant effect predictions validated against allelic imbalance measurements, confirming that sequence-based predictions capture genuine regulatory variation. DeepSEA demonstrated that deep learning on functional genomics data could discover regulatory patterns without encoding human assumptions about what matters."

---

## Figure 6.3: ExPecto Pipeline

**File:** `figs/part_2/ch06/03-fig-expecto-pipeline.svg`
**Priority:** Enhancing
**Type:** Three-component pipeline diagram

### Content Description

Modular pipeline showing three components:

1. **Component 1 (Beluga CNN):** Input 40kb window around TSS, sliding 2kb windows, producing chromatin predictions at 200 spatial positions
2. **Component 2 (Spatial Transformation):** Exponential decay functions (upstream and downstream) reducing ~400,000 features to ~20,000
3. **Component 3 (Tissue-Specific Linear Models):** 218 separate L2-regularized linear regression models producing per-tissue expression predictions

Show example delta scores for variant effect prediction.

### DALL-E Prompt

```
Scientific modular pipeline diagram with three connected components. Left component: CNN scanning across 40kb region with sliding windows, output as 200 spatial positions. Middle component: Exponential decay curves transforming spatial features, showing upstream and downstream integration. Right component: 218 parallel linear model outputs arranged as a vertical bar representing tissues. Arrows connecting components showing data flow. Clean bioinformatics pipeline style. White background. Professional systems biology diagram.
```

### Post-Processing Notes

- Add clear labels for each component
- Show approximate feature counts at each stage (2002 chromatin → 400K spatial → 20K transformed → 218 expression)
- Add tissue labels (liver, brain, heart, etc.) near output
- Include delta score formula for variant effect

### Fallback Description

Create in diagramming software (draw.io, BioRender):
- Three connected boxes representing pipeline stages
- Arrows showing data flow and dimension reduction
- Annotations for feature counts and biological interpretation

### Caption

**Recommended Caption:**
"ExPecto pipeline: from chromatin to expression. The modular architecture comprises three components. (1) Beluga CNN scans a 40kb window around each transcription start site with 2kb sliding windows, predicting 2,002 chromatin features at 200 spatial positions and generating over 400,000 features per gene. (2) Spatial transformation applies exponential decay functions separately for upstream and downstream regions, encoding the prior that nearby elements contribute more to expression than distant ones, reducing dimensionality to approximately 20,000 features. (3) Tissue-specific linear regression models (218 total, one per tissue) predict log expression from transformed features. This modular design separates shared sequence-to-chromatin processing from tissue-specific expression modeling, enabling interpretable analysis of which chromatin features drive expression in each context."

---

## Figure 6.4: SpliceAI Architecture (Two-Panel)

**Files:**
- `figs/part_2/ch06/04-A-fig-spliceai-architecture.svg`
- `figs/part_2/ch06/04-B-fig-spliceai-architecture.svg`

**Priority:** High
**Type:** Architecture diagram

### Panel A: Dilated Convolutions

**Content:** Diagram showing how dilated convolutions expand receptive field without proportional parameter growth. Show dilation rates (1, 2, 4, 8, 16...) with gaps between filter taps. Illustrate how stacking 32 layers with increasing dilation reaches 10kb context.

**DALL-E Prompt:**
```
Scientific diagram showing dilated convolution receptive field expansion. Multiple horizontal layers stacked vertically. Each layer shows a filter with gaps (dilation) between taps. Dilation increases from bottom (rate 1, no gaps) to top (rate 16, large gaps). Lines connecting each layer's outputs to inputs below. Total receptive field grows exponentially with depth. Clean neural network architecture diagram. White background with gray connecting lines. Professional deep learning illustration.
```

**Caption for Panel A:**
"Dilated convolutions expand receptive field efficiently. Standard convolutions (dilation rate 1) sample consecutive positions. Dilated convolutions sample at intervals, with dilation rate 2, 4, 8, 16, etc. progressively expanding coverage. Stacking convolutions with increasing dilation enables SpliceAI's 32-layer architecture to integrate 10kb of context while maintaining sensitivity to local patterns through lower layers."

### Panel B: Residual Block Structure

**Content:** SpliceAI's residual block with skip connections from every 4th block to the output layer. Show how this enables gradient flow through 32 layers.

**DALL-E Prompt:**
```
Scientific residual network architecture diagram. Vertical stack of 8 residual blocks, each containing two convolutional layers with a skip connection around them. Additional long skip connections from every 4th block to the final output layer at right. Arrows showing gradient flow paths through both short and long connections. Clean deep learning architecture style. White background. Professional neural network diagram showing deep architecture with skip connections.
```

**Caption for Panel B:**
"Residual connections enable ultra-deep architecture. SpliceAI uses 32 residual blocks, each learning incremental refinements to the representation. Skip connections every 4th block feed directly to the penultimate layer, providing additional gradient highways that stabilize training. This architecture achieves the depth necessary to integrate 10kb context while maintaining trainability through multiple parallel gradient paths."

### Combined Caption

**Full Figure Caption:**
"SpliceAI architecture innovations for long-range splicing prediction. (A) Dilated convolutions expand the receptive field efficiently by sampling input positions at intervals. Stacking layers with dilation rates 1, 2, 4, 8, 16... enables integration of 10,000 nucleotides of context without proportional parameter growth. Lower layers with small dilation capture local splice site grammar while upper layers with large dilation integrate distal determinants like branch points and exonic splicing enhancers. (B) Residual block structure with skip connections from every 4th block to the output. This enables training of 32 layers by providing multiple gradient pathways, preventing vanishing gradients that would otherwise block learning in such a deep network."

---

## Figure 6.5: Receptive Field Ceiling

**File:** `figs/part_2/ch06/05-fig-receptive-field-ceiling.svg`
**Priority:** Essential
**Type:** Genome-scale comparison diagram

### Content Description

Horizontal genome diagram comparing effective context windows across CNN architectures:
- DeepSEA: ~1kb
- ExPecto/Beluga: 2kb windows, 40kb aggregated
- SpliceAI: 10kb
- Enformer (for contrast): 200kb

Overlay biologically relevant distances:
- Typical TF binding site: ~10bp
- Promoter region: ~1kb
- Enhancer-gene distance: 10-100kb
- TAD size: ~1Mb

Highlight the gap: "Most enhancer-promoter interactions exceed CNN receptive fields."

### DALL-E Prompt

```
Scientific genome scale comparison diagram. Horizontal genomic region with scale bar. Multiple colored bars of different lengths showing context windows: short bar (1kb) for DeepSEA, medium bar (10kb) for SpliceAI, longer bar (40kb) for ExPecto, longest bar (200kb) for Enformer. Below: biological features with brackets showing typical distances - small bracket for promoter (~1kb), medium bracket for enhancer-promoter distance (50kb), large bracket for TAD (~1Mb). Gap highlighted between CNN capabilities and biological requirements. Clean genomics visualization style. White background. Professional comparative figure.
```

### Post-Processing Notes

- Add clear model labels with context lengths
- Add biological feature labels with typical distance ranges
- Highlight gap between enhancer-promoter distance and CNN capabilities
- Add annotation: "Attention mechanisms required for long-range regulatory modeling"

### Fallback Description

Create in matplotlib or diagramming software:
- Chromosome/genome ideogram at top
- Stacked bars showing context windows for each model
- Biological feature brackets below
- Annotation highlighting the limitation

### Caption

**Recommended Caption:**
"The receptive field ceiling of convolutional architectures. Context windows of representative CNN-based models compared to biologically relevant regulatory distances. DeepSEA integrates approximately 1kb of context; SpliceAI extends to 10kb through dilated convolutions; ExPecto aggregates predictions across 40kb. These contexts suffice for local features like transcription factor binding sites (~10bp) and promoter elements (~1kb) but cannot capture enhancer-promoter interactions typically spanning 10-100kb. Even SpliceAI's 10kb context falls short of the distances at which most GWAS signals reside from their target genes. This architectural limitation, not data scarcity, motivated the shift to attention mechanisms that compute direct interactions across arbitrary distances."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 6.1 Conv Pattern Detector | 3 | Essential | Medium (multi-panel) |
| 6.2 DeepSEA Architecture | 3 | High | Medium (architecture + validation) |
| 6.3 ExPecto Pipeline | 1 | Enhancing | Medium (pipeline) |
| 6.4 SpliceAI Architecture | 2 | High | Medium (architecture) |
| 6.5 Receptive Field | 1 | Essential | Low-Medium (comparison) |

**Total files:** 10
**Recommended generation order:** 6.5 (comparison, simplest), 6.4A-B (architecture), 6.3 (pipeline), 6.2A-C (architecture + validation), 6.1A-C (conceptual)
# Figure Report: Chapter 7 - Transformers and Attention

**Chapter:** Part 2, Chapter 7 - Transformers and Attention
**Date:** 2026-01-07
**Figures:** 7 conceptual figures (18 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 7.1: Self-Attention Mechanism (Five-Panel)

**Files:**
- `figs/part_2/ch07/01-A-fig-self-attention.svg`
- `figs/part_2/ch07/01-B-fig-self-attention.svg`
- `figs/part_2/ch07/01-C-fig-self-attention.svg`
- `figs/part_2/ch07/01-D-fig-self-attention.svg`
- `figs/part_2/ch07/01-E-fig-self-attention.svg`

**Priority:** Essential
**Type:** Multi-panel step-by-step visualization

### Panel A: Input Embeddings

**Content:** Show ~10 positions of a regulatory DNA sequence as input embeddings. Each position should be a colored vector/column representing the embedding. Label positions 1-10 with nucleotides above.

**DALL-E Prompt:**
```
Scientific diagram showing input embeddings for DNA sequence. Horizontal row of 10 rectangular colored blocks representing embedding vectors for nucleotide positions. Each block is a vertical gradient showing embedding dimensions. Small nucleotide letters (A, C, G, T) labeled above each position. Clean neural network input visualization style. White background with subtle grid. Professional deep learning textbook illustration.
```

**Caption for Panel A:**
"Input embeddings for a regulatory sequence. Each nucleotide position is represented as a learned embedding vector of dimension d, capturing both token identity and positional information. These embeddings serve as inputs to the self-attention computation."

### Panel B: Query, Key, Value Projections

**Content:** Show how each input embedding is projected through three weight matrices (W^Q, W^K, W^V) to produce query, key, and value vectors. Use color coding: blue for queries, orange for keys, green for values.

**DALL-E Prompt:**
```
Scientific diagram showing neural network projection operations. Single input vector on left projecting through three parallel pathways. Three weight matrices labeled W^Q, W^K, W^V. Output vectors colored blue (query), orange (key), green (value). Arrows showing matrix multiplication flow. Clean deep learning architecture diagram. White background. Professional machine learning textbook illustration.
```

**Caption for Panel B:**
"Query, Key, and Value projections. Each input embedding is transformed through three learned weight matrices to produce query (what this position seeks), key (what this position offers), and value (what this position sends when attended to). This separation enables flexible information routing based on content-dependent relevance."

### Panel C: Attention Score Matrix

**Content:** Visualize the attention score computation as a 10×10 matrix showing query-key dot products. Show pre-softmax scores with varying intensities. Highlight one row showing scores from a specific query position to all key positions.

**DALL-E Prompt:**
```
Scientific heatmap showing attention score matrix. 10x10 grid with varying color intensities from light (low score) to dark blue (high score). Row and column labels 1-10. One row highlighted with a border showing scores from position 5. Mathematical notation showing q_i dot k_j scaled by sqrt(d). Clean bioinformatics heatmap style. White background with gridlines. Professional neural network visualization.
```

**Caption for Panel C:**
"Attention score matrix (pre-softmax). Each cell (i,j) contains the dot product between query at position i and key at position j, scaled by √d_k to prevent extreme values. This matrix captures all pairwise content-based relevance scores between positions. The highlighted row shows how position 5 scores its relevance to all other positions."

### Panel D: Attention Weight Matrix

**Content:** Same 10×10 matrix after softmax normalization. Each row should sum to 1, shown as a probability distribution. Use color intensity to show attention weights. Highlight specific patterns like a position attending strongly to a distant position.

**DALL-E Prompt:**
```
Scientific heatmap showing attention weights after softmax. 10x10 grid with each row forming a probability distribution (rows sum to 1). Color gradient from white (near zero) to deep red (high weight). Some cells show strong attention (dark) while most are light. Pattern showing one position attending strongly to a distant position. Row totals shown as "=1.0". Clean neural network visualization. White background. Professional attention mechanism diagram.
```

**Caption for Panel D:**
"Attention weight matrix (post-softmax). Softmax normalization converts scores to probabilities; each row sums to 1. High weights (dark) indicate strong attention between positions. This pattern shows position 3 attending strongly to position 8, demonstrating how attention enables direct long-range information flow regardless of sequence distance."

### Panel E: Weighted Value Aggregation

**Content:** Show how attention weights are used to aggregate value vectors into outputs. Visualize as weighted sum: each output position receives a mixture of all value vectors, with mixture proportions from the attention weights.

**DALL-E Prompt:**
```
Scientific diagram showing weighted aggregation operation. On left: column of value vectors (green rectangles). In middle: attention weight column showing probabilities. On right: single output vector as weighted combination. Arrows from each value vector to output, with line thickness proportional to weight. Mathematical notation showing sum of alpha_ij times v_j. Clean deep learning diagram style. White background. Professional neural network computation visualization.
```

**Caption for Panel E:**
"Weighted value aggregation produces outputs. Each output position receives a weighted sum of all value vectors, with weights from the attention distribution. Position i's output aggregates information from the entire sequence, with each position j contributing proportionally to attention weight α_ij. This enables any position to directly access information from any other position."

### Combined Caption

**Full Figure Caption:**
"Step-by-step visualization of self-attention on a regulatory sequence. (A) Input embeddings represent each nucleotide position as a learned vector. (B) Linear projections produce query (what to seek), key (what to advertise), and value (what to send) vectors through learned weight matrices. (C) Attention scores are computed as scaled dot products between all query-key pairs, capturing content-based relevance. (D) Softmax normalization converts scores to attention weights forming probability distributions over positions. (E) Each output is a weighted sum of value vectors, with weights determining how much each position contributes. This mechanism enables direct communication between any two positions regardless of sequence distance."

---

## Figure 7.2: Multi-Head Attention

**File:** `figs/part_2/ch07/02-fig-multihead-attention.svg`
**Priority:** High
**Type:** Panel showing diverse attention patterns

### Content Description

Show 4-6 attention heads from a trained genomic transformer, each displaying different learned patterns:
- Head 1: Local attention (diagonal band, attending to nearby positions)
- Head 2: Periodic attention (~200bp nucleosome spacing pattern)
- Head 3: Motif-specific attention (attending to specific sequence features)
- Head 4: Long-range attention (off-diagonal connections for enhancer-promoter)

Include biological interpretation labels for each pattern.

### DALL-E Prompt

```
Scientific panel showing six attention pattern heatmaps from genomic transformer. Arranged in 2x3 grid. Each heatmap is a square matrix showing different learned patterns: one with strong diagonal (local), one with periodic stripes (nucleosome spacing), one with sparse distant connections (long-range), one with clustered attention at specific positions (motif-specific). Different color schemes for each head. Labels below each showing biological interpretation. Clean bioinformatics visualization. White background. Professional multi-head attention analysis figure.
```

### Post-Processing Notes

- Add clear labels for each attention head (Head 1, Head 2, etc.)
- Annotate biological interpretations: "Local context", "~200bp periodicity", "CTCF site attention", "Enhancer-promoter"
- Add x/y axes showing genomic positions or relative distances
- Use consistent scale bars for attention weight intensity

### Fallback Description

Create in matplotlib or diagramming software:
- 2×3 or 2×2 grid of attention heatmaps
- Generate synthetic attention patterns representing different head types
- Add biological annotations and legends

### Caption

**Recommended Caption:**
"Multi-head attention captures diverse biological relationships. Different heads in a trained genomic transformer learn specialized attention patterns. Head 1 attends locally to nearby positions, capturing motif context. Head 2 shows periodic attention at approximately 200 base pair intervals, potentially reflecting nucleosome spacing. Head 3 attends specifically to positions matching sequence motifs like CTCF binding sites. Head 4 exhibits long-range attention connecting distant positions, consistent with enhancer-promoter interactions. This specialization emerges from training without explicit supervision, demonstrating that the chromatin prediction objective induces biologically meaningful attention patterns."

---

## Figure 7.3: Attention Patterns in Genomic Context (Three-Panel)

**Files:**
- `figs/part_2/ch07/03-A-fig-attention-patterns.svg`
- `figs/part_2/ch07/03-B-fig-attention-patterns.svg`
- `figs/part_2/ch07/03-C-fig-attention-patterns.svg`

**Priority:** Essential
**Type:** Heatmap visualization with biological interpretation

### Panel A: Enhancer-Promoter Attention

**Content:** Attention weight heatmap from a trained model (e.g., Enformer) showing strong attention between a promoter region and a distal enhancer ~50kb away. Should show sparse but strong off-diagonal attention.

**DALL-E Prompt:**
```
Scientific attention heatmap from genomic transformer. Large square matrix (~100 positions). Most cells are light (low attention). Strong dark cluster in off-diagonal region showing attention between positions far apart in sequence. Diagonal line faint. Annotation arrows pointing to "Promoter" and "Enhancer ~50kb away". Clean bioinformatics heatmap with blue color gradient. White background with axis labels. Professional regulatory genomics visualization.
```

**Caption for Panel A:**
"Learned enhancer-promoter attention. This attention pattern from a trained Enformer-style model shows strong weights between a promoter region (row) and a distal enhancer approximately 50 kilobases away (column). The model learned this long-range regulatory relationship from predicting gene expression, without explicit enhancer-promoter labels during training."

### Panel B: Genomic Context Overlay

**Content:** Same attention pattern overlaid on a linear genome diagram showing the biological interpretation. Show gene structure with promoter, the enhancer element, and curved lines representing the attention connections.

**DALL-E Prompt:**
```
Scientific genome diagram with attention overlay. Horizontal linear representation of ~100kb genomic region. Gene shown as arrow with exon boxes. Promoter region highlighted at gene start. Enhancer element shown as colored box ~50kb upstream. Curved arc lines connecting promoter to enhancer, representing attention weights. Line thickness proportional to attention strength. Clean molecular biology style with genomic coordinates. White background. Professional regulatory interaction visualization.
```

**Caption for Panel B:**
"Biological interpretation of learned attention. The same attention pattern overlaid on the genomic context reveals that the model has learned to connect a gene's promoter with its distal enhancer. Arc thickness represents attention weight strength. This pattern enables the model to integrate regulatory information across tens of kilobases when predicting expression."

### Panel C: Local Attention Head

**Content:** Contrasting attention pattern from a different head showing primarily local/diagonal attention, demonstrating head specialization.

**DALL-E Prompt:**
```
Scientific attention heatmap showing local attention pattern. Square matrix with strong diagonal band of high attention weights (dark blue). Off-diagonal elements are light/white. Band width spans approximately 10-20 positions on each side of diagonal. Clean neural network attention visualization. White background with position labels. Professional deep learning figure showing local attention head.
```

**Caption for Panel C:**
"Local attention head for motif context. A different attention head from the same model shows primarily local attention, with each position attending strongly to nearby neighbors. This head captures local sequence context including transcription factor binding motif grammar and short-range regulatory relationships, complementing the long-range heads that capture distal interactions."

### Combined Caption

**Full Figure Caption:**
"Attention patterns in genomic transformers reveal learned regulatory relationships. (A) An attention head showing strong weights between a promoter and distal enhancer approximately 50kb apart, demonstrating learned long-range regulatory attention. (B) The same pattern overlaid on genomic context, showing how attention arcs connect the promoter to its regulatory enhancer. (C) A different head from the same model shows local attention patterns, capturing nearby sequence context. This head specialization emerges from training: some heads learn to integrate long-range regulatory signals while others focus on local motif relationships."

---

## Figure 7.4: Positional Encoding Comparison (Four-Panel)

**Files:**
- `figs/part_2/ch07/04-A-fig-position-encodings.svg`
- `figs/part_2/ch07/04-B-fig-position-encodings.svg`
- `figs/part_2/ch07/04-C-fig-position-encodings.svg`
- `figs/part_2/ch07/04-D-fig-position-encodings.svg`

**Priority:** High
**Type:** Technical comparison diagram

### Panel A: Learned Absolute Positional Embeddings

**Content:** Heatmap showing learned position embeddings across dimensions. Each row is a position (1-512), each column is an embedding dimension. Show patterns that emerge from training with annotation about fixed maximum length limitation.

**DALL-E Prompt:**
```
Scientific heatmap showing learned positional embeddings. Rectangular matrix with positions (1-512) on y-axis and embedding dimensions on x-axis. Color gradient showing learned values with some visible patterns (stripes, gradients). Annotation box stating "Fixed max length: 512". Clean machine learning visualization style. White background with axis labels. Professional deep learning positional encoding figure.
```

**Caption for Panel A:**
"Learned absolute positional embeddings. Each row shows the learned embedding vector for a specific sequence position. Patterns emerge from training as the model discovers position-dependent features. The limitation: models cannot process sequences longer than the maximum position seen during training (here, 512), creating a hard context length boundary."

### Panel B: Sinusoidal Positional Encoding

**Content:** Wave patterns showing sinusoidal positional encodings at different frequencies. Show how different dimensions oscillate at different rates, with low-frequency dimensions capturing coarse position and high-frequency dimensions capturing fine position.

**DALL-E Prompt:**
```
Scientific diagram showing sinusoidal positional encoding waves. Multiple overlapping sine/cosine curves of different frequencies plotted against position (x-axis 0-100). Low frequency waves (long wavelength) in one color, high frequency waves (short wavelength) in another. Vertical dashed line at specific position showing unique "fingerprint" of wave values. Mathematical formula PE(pos,i) shown. Clean mathematical visualization. White background with gridlines. Professional deep learning figure.
```

**Caption for Panel B:**
"Sinusoidal positional encoding. Different embedding dimensions oscillate at different frequencies, creating a unique positional 'fingerprint' at each location. Low-frequency components (slow waves) encode coarse position; high-frequency components (fast waves) encode fine position. These fixed patterns generalize to sequences longer than training length because the mathematical functions extend naturally."

### Panel C: ALiBi (Attention with Linear Biases)

**Content:** Attention bias matrix showing linear decay with distance. Triangular heatmap where bias decreases linearly as distance from diagonal increases. Show different slopes for different heads.

**DALL-E Prompt:**
```
Scientific triangular matrix showing ALiBi attention bias. Lower triangular matrix with diagonal at maximum value (dark), linearly decreasing toward bottom-left corner (lighter). Multiple overlapping matrices showing different slope parameters for different heads (different decay rates). Mathematical annotation showing "-m|i-j|" penalty formula. Clean attention mechanism visualization. White background. Professional linear attention bias diagram.
```

**Caption for Panel C:**
"ALiBi: Attention with Linear Biases. Instead of adding positional embeddings to inputs, ALiBi subtracts a linear penalty from attention scores based on distance. Distant positions receive increasingly negative bias, encouraging local attention. Different heads use different slopes (shown overlaid), allowing some heads to focus locally while others attend more broadly. This scheme extrapolates naturally to any sequence length."

### Panel D: RoPE (Rotary Position Embeddings)

**Content:** 2D visualization showing how RoPE encodes position through rotation in embedding subspace. Show query and key vectors being rotated by position-dependent angles, with the dot product depending on relative position.

**DALL-E Prompt:**
```
Scientific 2D diagram showing rotary position embeddings. Two-dimensional embedding subspace with unit circle. Query vector at one angle, key vector at another angle. Rotation arrows showing position-dependent rotation. Annotation showing that dot product depends on angle difference (relative position). Multiple vector pairs at different positions shown with consistent angle relationships. Clean geometric visualization. White background. Professional positional encoding diagram.
```

**Caption for Panel D:**
"Rotary Position Embeddings (RoPE). Position is encoded through rotation in embedding subspace. Query and key vectors are rotated by angles proportional to their positions. The dot product between rotated vectors depends on their relative position (angle difference), not absolute positions. This geometric encoding provides relative position information while maintaining compatibility with standard attention computation."

### Combined Caption

**Full Figure Caption:**
"Positional encoding approaches for transformers. (A) Learned absolute embeddings assign a trained vector to each position; effective but limited to training sequence length. (B) Sinusoidal encodings use fixed sine/cosine functions at different frequencies, creating unique position fingerprints that generalize beyond training length. (C) ALiBi applies linear attention penalties based on distance, encouraging local attention while naturally extrapolating to long sequences. (D) RoPE encodes position through geometric rotation, making dot products depend on relative rather than absolute positions. Each approach encodes different assumptions about how position information should influence attention."

---

## Figure 7.5: Transformer Block Architecture

**File:** `figs/part_2/ch07/05-fig-transformer-block.svg`
**Priority:** High
**Type:** Detailed architecture diagram

### Content Description

Detailed diagram of a single transformer block with pre-norm configuration:
- Input → Layer Norm → Multi-Head Attention → Residual Add → Layer Norm → Feed-Forward Network (expand 4x, GELU, project back) → Residual Add → Output
- Annotate dimension changes at each step
- Include small inset showing 2-3 stacked blocks to illustrate depth

### DALL-E Prompt

```
Scientific neural network architecture diagram showing transformer block. Vertical flow from bottom to top: Input box → Layer Norm → Multi-Head Attention (multiple colored heads) → Add symbol with skip connection from input → Layer Norm → Feed-Forward Network (expand, GELU activation, project boxes) → Add symbol with skip connection → Output. Skip connections shown as curved arrows bypassing main pathway. Dimension annotations (d, 4d, d). Small inset showing three stacked blocks. Clean deep learning architecture style. White background. Professional transformer diagram.
```

### Post-Processing Notes

- Add clear dimension labels: "d=768" at input, "4d=3072" at FFN expansion
- Show residual connections clearly as bypassing arrows
- Label each component: "LayerNorm", "Multi-Head Attention (H heads)", "Feed-Forward"
- Add activation function label (GELU)
- Inset should show blocks labeled "Layer 1", "Layer 2", "Layer N"

### Fallback Description

Create in diagramming software (draw.io, Lucidchart):
- Vertical flowchart with boxes for each component
- Curved arrows for residual connections
- Dimension annotations
- Stacked block inset

### Caption

**Recommended Caption:**
"Transformer block architecture with pre-norm configuration. Input embeddings (dimension d) pass through layer normalization before multi-head self-attention, which computes interactions across all positions. A residual connection adds the input directly to the attention output, creating gradient highways for stable training. A second layer normalization precedes the position-wise feed-forward network, which expands representations to 4d dimensions, applies GELU nonlinearity, and projects back to d dimensions. Another residual connection completes the block. Stacking multiple blocks (inset) enables hierarchical representation learning, with early layers capturing local patterns and later layers integrating them into complex regulatory predictions."

---

## Figure 7.6: Architectural Variants Comparison (Three-Panel)

**Files:**
- `figs/part_2/ch07/06-A-fig-encoder-decoder.svg`
- `figs/part_2/ch07/06-B-fig-encoder-decoder.svg`
- `figs/part_2/ch07/06-C-fig-encoder-decoder.svg`

**Priority:** Enhancing
**Type:** Architecture comparison diagram

### Panel A: Encoder-Only (BERT/DNABERT Style)

**Content:** Bidirectional attention pattern showing full attention matrix (all positions attend to all positions). Show typical use case: sequence classification or embedding extraction.

**DALL-E Prompt:**
```
Scientific diagram showing encoder-only transformer architecture. Left: Full attention matrix (square, fully colored) labeled "Bidirectional". Right: Architecture stack with bidirectional arrows between positions. Bottom: Input sequence. Top: Output embeddings or [CLS] token for classification. Example models listed: DNABERT, ESM-2. Clean deep learning architecture comparison. White background. Professional transformer variant diagram.
```

**Caption for Panel A:**
"Encoder-only architecture (BERT/DNABERT style). All positions attend to all other positions bidirectionally, shown as a fully populated attention matrix. This architecture excels at tasks requiring understanding of full sequence context: variant effect prediction, binding site classification, and embedding extraction. Each position's representation integrates information from the entire sequence."

### Panel B: Decoder-Only (GPT/Evo Style)

**Content:** Causal attention pattern showing lower-triangular matrix (each position attends only to itself and preceding positions). Show typical use case: sequence generation.

**DALL-E Prompt:**
```
Scientific diagram showing decoder-only transformer architecture. Left: Lower triangular attention matrix labeled "Causal/Autoregressive". Right: Architecture stack with arrows pointing only leftward (to previous positions). Bottom: Input sequence with generation direction arrow. Top: Next-token predictions. Example models listed: GPT, Evo, ProtGPT2. Clean deep learning architecture comparison. White background. Professional transformer variant diagram.
```

**Caption for Panel B:**
"Decoder-only architecture (GPT/Evo style). Each position attends only to itself and preceding positions, shown as a lower-triangular attention matrix. This causal structure enables autoregressive generation: predicting each token given only previous tokens. Essential for sequence design applications where novel sequences must be generated one position at a time."

### Panel C: Hybrid CNN-Transformer (Enformer Style)

**Content:** Show CNN downsampling followed by transformer layers. Illustrate how long input sequences are compressed before attention, enabling long-range modeling with tractable computation.

**DALL-E Prompt:**
```
Scientific diagram showing hybrid CNN-transformer architecture. Left side: Long input sequence (many positions). Middle: Convolutional layers with pooling operations progressively compressing sequence length (shown as narrowing trapezoid). Right side: Transformer layers operating on compressed representation. Arrows showing information flow. Dimension annotations showing compression (e.g., 200kb input → 1500 positions for attention). Example: Enformer. Clean deep learning architecture diagram. White background. Professional hybrid architecture figure.
```

**Caption for Panel C:**
"Hybrid CNN-Transformer architecture (Enformer style). Convolutional layers first process long input sequences, extracting local features and downsampling through pooling. This compresses a 200-kilobase input to approximately 1,500 positions, making full attention tractable. Transformer layers then integrate information across this compressed representation. This hybrid achieves both local pattern detection (via CNNs) and long-range integration (via attention) for regulatory sequence modeling."

### Combined Caption

**Full Figure Caption:**
"Transformer architectural variants for genomic applications. (A) Encoder-only models use bidirectional attention where every position attends to every other, providing rich representations for classification and understanding tasks. (B) Decoder-only models use causal attention where each position sees only preceding context, enabling autoregressive sequence generation. (C) Hybrid CNN-Transformer architectures use convolutions to compress long sequences before applying attention, balancing long-range context with computational tractability. The choice of architecture should match the downstream task: understanding requires bidirectional context, generation requires causal structure, and long-range prediction benefits from hybrid designs."

---

## Figure 7.7: Quadratic Complexity Ceiling

**File:** `figs/part_2/ch07/07-fig-quadratic-ceiling.svg`
**Priority:** High
**Type:** Log-log scaling comparison

### Content Description

Log-log plot showing computational cost (FLOPs or memory) vs. sequence length for different architectures:
- Standard attention: O(L²) quadratic curve
- Sparse/local attention: sub-quadratic
- State space models (Hyena/Mamba): O(L) linear

Annotate biologically relevant context lengths with vertical lines:
- Promoter (~1 kb)
- Gene (~10 kb)
- Enhancer-promoter (~100 kb)
- TAD (~1 Mb)
- Chromosome arm (~100 Mb)

Show which architectures are tractable at each scale.

### DALL-E Prompt

```
Scientific log-log plot comparing computational scaling. X-axis: Sequence length (log scale, 1kb to 100Mb). Y-axis: Computational cost (log scale). Three curves: steep quadratic curve (O(L²), labeled "Standard Attention"), intermediate curve ("Sparse Attention"), nearly flat curve (O(L), labeled "Linear/SSM"). Vertical dashed lines at biological scales: 1kb (Promoter), 10kb (Gene), 100kb (Enhancer-promoter), 1Mb (TAD), 100Mb (Chromosome). Shaded regions showing tractable/intractable zones. Clean scientific scaling analysis figure. White background with grid. Professional computational genomics diagram.
```

### Post-Processing Notes

- Use distinct colors for each architecture type
- Add clear labels at biological context markers
- Shade "computationally tractable" vs "intractable" regions
- Add model examples at appropriate scales: DNABERT (~1kb), Enformer (~200kb), HyenaDNA (~1Mb)
- Include annotation: "Attention mechanisms required for long-range regulatory modeling face fundamental scaling constraints"

### Fallback Description

Create in matplotlib:
- Log-log plot with multiple curves
- Vertical lines for biological context scales
- Fill between curves to show tractability regions
- Add text annotations for model examples

### Caption

**Recommended Caption:**
"The quadratic complexity ceiling limits transformer context length. Computational cost versus sequence length on log-log axes reveals the scaling challenge. Standard self-attention (O(L²)) becomes intractable beyond ~10-50 kilobases depending on hardware. Sparse attention variants reduce cost but still scale superlinearly. State space models like Hyena and Mamba achieve linear O(L) scaling, enabling million-base contexts. Vertical lines mark biologically relevant scales: most enhancer-promoter interactions (50-100 kb) exceed standard transformer capacity, while TAD-scale analysis (~1 Mb) requires sub-quadratic architectures. This scaling constraint, not data availability, motivates architectural innovations beyond standard attention."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 7.1 Self-Attention | 5 | Essential | High (5-panel step-by-step) |
| 7.2 Multi-Head Attention | 1 | High | Medium (pattern panel) |
| 7.3 Attention Patterns | 3 | Essential | Medium (heatmaps + overlay) |
| 7.4 Position Encodings | 4 | High | Medium (technical comparison) |
| 7.5 Transformer Block | 1 | High | Medium (architecture) |
| 7.6 Encoder-Decoder | 3 | Enhancing | Medium (architecture comparison) |
| 7.7 Quadratic Ceiling | 1 | High | Medium (scaling plot) |

**Total files:** 18
**Recommended generation order:** 7.7 (scaling, clearest), 7.5 (architecture), 7.6A-C (variants), 7.4A-D (position encodings), 7.2 (multihead), 7.3A-C (attention patterns), 7.1A-E (step-by-step, most complex)
# Figure Report: Chapter 8 - Pretraining Strategies

**Chapter:** Part 2, Chapter 8 - Pretraining Strategies
**Date:** 2026-01-07
**Figures:** 6 conceptual figures (10 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 8.1: Pretraining Objectives Comparison (Three-Panel)

**Files:**
- `figs/part_2/ch08/01-A-fig-pretraining-objectives.svg`
- `figs/part_2/ch08/01-B-fig-pretraining-objectives.svg`
- `figs/part_2/ch08/01-C-fig-pretraining-objectives.svg`

**Priority:** Essential
**Type:** Multi-panel schematic comparison

### Panel A: Masked Language Modeling (MLM)

**Content:** DNA sequence with several positions replaced by [MASK] tokens. Show bidirectional context arrows from both upstream and downstream positions pointing to each masked position. Indicate prediction targets at masked locations.

**DALL-E Prompt:**
```
Scientific diagram showing masked language modeling for DNA. Horizontal sequence of nucleotide letters (A, C, G, T) with several positions replaced by gray [MASK] boxes. Curved arrows pointing from both left and right context toward each mask, showing bidirectional information flow. Below masks, prediction targets shown with probability distributions over nucleotides. Clean deep learning pretraining diagram. White background. Professional self-supervised learning illustration.
```

**Caption for Panel A:**
"Masked language modeling (MLM). Random positions are replaced with [MASK] tokens, and the model predicts the original nucleotides using bidirectional context. Arrows indicate that each prediction integrates information from both upstream and downstream sequence. This objective teaches sequence grammar and evolutionary constraints through reconstruction."

### Panel B: Next-Token Prediction (Autoregressive)

**Content:** Same DNA sequence but with causal/unidirectional arrows. Each position predicts the next, with arrows only pointing rightward. Show sampling process with probability distributions and sampled tokens.

**DALL-E Prompt:**
```
Scientific diagram showing autoregressive next-token prediction for DNA. Horizontal sequence of nucleotides with arrows pointing only left-to-right (causal). Each position shows prediction for next token. Probability distribution bars above each prediction. Dashed line showing generation process: sample token, append, predict next. Clean deep learning pretraining diagram. White background. Professional autoregressive model illustration.
```

**Caption for Panel B:**
"Next-token prediction (autoregressive). Each position predicts the next token given only preceding context, shown by unidirectional arrows. This causal structure enables generation: sample one token at a time, each conditioned on all previous outputs. The objective teaches sequential dependencies and enables de novo sequence design."

### Panel C: Contrastive Learning

**Content:** Show anchor sequence, positive pair (augmented version with reverse complement or minor variants), and negative samples (unrelated sequences). Map all to an embedding space showing distance relationships: anchor close to positive, far from negatives.

**DALL-E Prompt:**
```
Scientific diagram showing contrastive learning for genomic sequences. Top: Three sequences - "Anchor" (original), "Positive" (augmented/similar, connected by double arrow), "Negatives" (multiple unrelated sequences). Bottom: Circular embedding space with anchor and positive as nearby points (close together), negatives as distant scattered points. Arrows showing "pull together" between anchor-positive, "push apart" toward negatives. Clean machine learning contrastive learning diagram. White background. Professional representation learning figure.
```

**Caption for Panel C:**
"Contrastive learning. An anchor sequence and its augmented positive pair (e.g., reverse complement, variant-injected version) should map to nearby points in embedding space, while unrelated negative sequences map to distant points. This objective teaches invariance: functionally equivalent sequences should have similar representations regardless of strand orientation or genetic background."

### Combined Caption

**Full Figure Caption:**
"Comparison of major pretraining objectives for genomic sequences. (A) Masked language modeling corrupts sequences with [MASK] tokens and trains models to reconstruct original content using bidirectional context. This produces representations suited for classification and variant interpretation where full context matters. (B) Next-token prediction trains models to generate sequences autoregressively, predicting each position from preceding context. This enables sequence generation for therapeutic design applications. (C) Contrastive learning teaches invariance by bringing augmented versions of the same sequence together in embedding space while pushing unrelated sequences apart. Each objective encodes different assumptions about what patterns matter and produces models with different downstream strengths."

---

## Figure 8.2: Masking Strategies Comparison (Two-Panel)

**Files:**
- `figs/part_2/ch08/02-A-fig-masking-strategies.svg`
- `figs/part_2/ch08/02-B-fig-masking-strategies.svg`

**Priority:** High
**Type:** Comparative visualization

### Panel A: Random Token Masking

**Content:** Regulatory sequence containing a transcription factor binding motif. Individual tokens masked randomly throughout, including partial masking within the motif. Show attention patterns indicating that local context easily predicts masked positions.

**DALL-E Prompt:**
```
Scientific diagram showing random token masking on DNA regulatory sequence. Horizontal sequence with colored region indicating TF binding motif. Several individual nucleotides replaced with [MASK] throughout sequence, including one or two within the motif region. Arrows showing local context (nearby nucleotides) predicting each mask. Attention pattern heatmap below showing primarily local attention near diagonal. Clean bioinformatics masking strategy diagram. White background. Professional MLM training visualization.
```

**Caption for Panel A:**
"Random token masking. Individual tokens are masked uniformly at random, including partial masking within functional motifs. Each masked position can often be predicted from immediately adjacent nucleotides, as shown by the primarily local attention pattern. This approach is simple and stable but may not force learning of higher-order compositional structure."

### Panel B: Span Masking

**Content:** Same regulatory sequence with entire motif region masked as a contiguous span (single sentinel token replacing multiple nucleotides). Show attention patterns reaching to more distant positions since local motif context is unavailable.

**DALL-E Prompt:**
```
Scientific diagram showing span masking on DNA regulatory sequence. Horizontal sequence with entire TF binding motif region replaced by single [SPAN] sentinel token. Arrows from distant flanking positions pointing to span, showing need for long-range context. Attention pattern heatmap below showing longer-range attention reaching beyond immediate neighbors. Clean bioinformatics masking strategy diagram. White background. Professional span corruption training visualization.
```

**Caption for Panel B:**
"Span masking forces compositional learning. Entire functional elements (here, a transcription factor binding motif) are masked as contiguous spans. With local motif information unavailable, the model must reason from distant regulatory context to reconstruct the span. The attention pattern shows longer-range dependencies than random masking. This teaches that motifs function as compositional units rather than independent nucleotides."

### Combined Caption

**Full Figure Caption:**
"Masking strategies encode different learning pressures. (A) Random token masking distributes [MASK] tokens throughout the sequence. Individual masked positions can often be predicted from immediately adjacent context, encouraging local pattern learning. (B) Span masking replaces contiguous blocks with single sentinel tokens, removing local context entirely. Predicting masked spans requires reasoning from more distant sequence features, forcing the model to learn compositional patterns and longer-range dependencies. For regulatory sequence modeling, span masking may better capture how transcription factor binding sites and other functional elements operate as integrated units."

---

## Figure 8.3: Bidirectional vs. Autoregressive Information Flow (Two-Panel)

**Files:**
- `figs/part_2/ch08/03-A-fig-bidirectional-vs-autoregressive.svg`
- `figs/part_2/ch08/03-B-fig-bidirectional-vs-autoregressive.svg`

**Priority:** Essential
**Type:** Information flow comparison

### Panel A: MLM (Bidirectional)

**Content:** Position in the center of a sequence with arrows coming from BOTH left and right context. Emphasize that the model sees full flanking sequence when making predictions. Annotate: "Sees full context → better for understanding."

**DALL-E Prompt:**
```
Scientific diagram showing bidirectional information flow. Horizontal DNA sequence with one central position highlighted. Multiple curved arrows converging on this position from BOTH left side (upstream context) and right side (downstream context). Position marked with question mark or prediction target. Annotation text: "Sees full context → better for understanding/classification". Clean neural network information flow diagram. White background. Professional MLM representation learning figure.
```

**Caption for Panel A:**
"Bidirectional context in masked language modeling. The highlighted position receives information from both upstream (left) and downstream (right) context when making predictions. For variant effect prediction or binding site classification, this full context enables richer representations: a splice site's function depends on both the upstream exon and downstream intron, both of which bidirectional models can access."

### Panel B: Autoregressive (Unidirectional)

**Content:** Same position but with arrows only from left (preceding tokens). The position cannot see downstream context. Annotate: "Sees only past → enables generation."

**DALL-E Prompt:**
```
Scientific diagram showing unidirectional information flow. Horizontal DNA sequence with one position highlighted in center-right area. Curved arrows converging on this position ONLY from left side (preceding context). Right side has no arrows (no future context access). Annotation text: "Sees only past → enables generation". Clean neural network information flow diagram. White background. Professional autoregressive model figure.
```

**Caption for Panel B:**
"Causal context in autoregressive models. The highlighted position receives information only from preceding (left) context. Downstream sequence is invisible during prediction, as required for generation: when sampling new sequences, future tokens do not yet exist. This restriction enables direct sequence generation but limits representation quality for tasks where downstream context matters."

### Combined Caption

**Full Figure Caption:**
"Information flow determines downstream capabilities. (A) Masked language models use bidirectional attention, allowing each position to integrate information from the entire sequence. This produces richer representations suited for understanding tasks like variant interpretation, where both flanking regions inform the prediction. (B) Autoregressive models use causal attention, where each position sees only preceding context. This restriction is essential for generation (future tokens cannot exist during sampling) but produces less informed representations. The choice between objectives should match the intended downstream application: understanding tasks favor bidirectional pretraining; generation tasks require autoregressive structure."

---

## Figure 8.4: Cross-Species Contrastive Learning

**File:** `figs/part_2/ch08/04-fig-cross-species-contrastive.svg`
**Priority:** Enhancing
**Type:** Evolutionary illustration with embedding space

### Content Description

Show contrastive pretraining using orthologous sequences:
- Human enhancer sequence and mouse ortholog (aligned, showing nucleotide divergence but conserved core elements)
- Both sequences mapped to nearby points in embedding space (positive pair)
- Non-orthologous sequence mapped to distant point (negative)
- Include phylogenetic context showing ~75 million years of divergence
- Annotate: "Same function despite sequence divergence → learns species-invariant features"

### DALL-E Prompt

```
Scientific diagram showing cross-species contrastive learning. Top section: Aligned DNA sequences from human and mouse with ~75% identity, showing nucleotide mismatches but conserved motif regions highlighted. Phylogenetic tree branch connecting them showing "75 My divergence". Bottom section: Circular embedding space with human and mouse sequences as nearby points (positive pair, connected by line), and unrelated sequence as distant point. Annotation: "Same function despite divergence → species-invariant features". Clean evolutionary bioinformatics diagram. White background. Professional cross-species learning figure.
```

### Post-Processing Notes

- Show sequence alignment with matches/mismatches color-coded
- Highlight conserved functional elements (binding sites) in both sequences
- Include small phylogenetic tree showing human-mouse divergence
- Embedding space should clearly show clustering of orthologs vs. separation of non-orthologs
- Add arrows indicating "pull together" for positive pairs

### Fallback Description

Create in diagramming software:
- Two aligned sequences with identity shading
- Phylogenetic tree inset
- 2D embedding scatter plot showing ortholog clustering

### Caption

**Recommended Caption:**
"Cross-species contrastive learning for species-invariant representations. Orthologous sequences from human and mouse share functional identity despite 75 million years of divergence and substantial nucleotide differences (shown in alignment). Treating orthologs as positive pairs teaches the model to extract conserved functional features while ignoring species-specific sequence differences. Non-orthologous sequences serve as negatives. The resulting embedding space clusters orthologs together regardless of species, enabling transfer from model organism experiments to human predictions."

---

## Figure 8.5: Multi-Task Pretraining Architecture

**File:** `figs/part_2/ch08/05-fig-multitask-pretraining.svg`
**Priority:** High
**Type:** Architecture diagram with multiple outputs

### Content Description

Diagram showing shared encoder with multiple prediction heads:
- Sequence input → Convolutional layers → Transformer layers (labeled "Shared Backbone")
- Branching to separate heads for:
  - Chromatin accessibility (DNase-seq, ATAC-seq)
  - Histone modifications (H3K27ac, H3K4me3, etc.)
  - Transcription factor binding (hundreds of factors)
  - Gene expression (CAGE)
- Annotate approximate task counts from ENCODE: "674 DNase + 4,675 ChIP-seq + 638 CAGE"

### DALL-E Prompt

```
Scientific neural network architecture diagram showing multi-task learning. Left: Input sequence box. Middle: Shared encoder stack with convolutional and transformer layers, labeled "Shared Backbone". Right: Four branching prediction heads, each as a separate output pathway. Head labels: "Chromatin Accessibility", "Histone Marks", "TF Binding (100s)", "Gene Expression". Annotation showing task counts: "5,000+ total tracks". Arrows showing feature sharing from backbone to all heads. Clean deep learning multi-task architecture. White background. Professional genomic AI figure.
```

### Post-Processing Notes

- Use color coding for different output types (e.g., blue for accessibility, green for histones, orange for TF, purple for expression)
- Add task count annotations near each head
- Show dimension flow through architecture
- Include legend explaining what each head predicts

### Fallback Description

Create in diagramming software:
- Shared encoder as central block
- Branching arrows to separate prediction heads
- Head-specific output layers
- Task count annotations

### Caption

**Recommended Caption:**
"Multi-task pretraining architecture for comprehensive regulatory prediction. A shared encoder backbone (convolutional layers for local patterns, transformer layers for long-range integration) processes input sequences. Multiple prediction heads branch from shared representations to predict diverse genomic readouts: chromatin accessibility (DNase-seq, ATAC-seq), histone modifications (H3K27ac, H3K4me3, H3K27me3), transcription factor binding for hundreds of factors, and gene expression via CAGE. Enformer jointly predicts over 5,000 tracks (674 DNase + 4,675 ChIP-seq + 638 CAGE), forcing shared representations to capture diverse regulatory signals. This multi-task pressure produces representations that generalize beyond any single assay."

---

## Figure 8.6: Context Length Curriculum

**File:** `figs/part_2/ch08/06-fig-context-curriculum.svg`
**Priority:** High
**Type:** Training progression diagram

### Content Description

Diagram showing context length curriculum progression:
- X-axis: Training steps (or compute)
- Y-axis: Context length (log scale)
- Show stepped increases: 1kb → 4kb → 16kb → 64kb → 256kb → 1Mb
- At each stage annotate: "Stable optimization at short context" → "Weight initialization from previous stage" → "Learning rate warmup" → "Extended training at new context"
- Include inset showing attention pattern differences at short vs. long context

### DALL-E Prompt

```
Scientific training curriculum diagram. Main plot: X-axis shows training steps, Y-axis shows context length on log scale. Step function increasing from 1kb through 4kb, 16kb, 64kb, 256kb to 1Mb. At each step transition, annotation arrows pointing to: "Warmup", "Initialize from checkpoint", "Train to convergence". Inset panel in corner showing two small attention matrices: one dense (short context) and one sparse (long context). Clean machine learning training visualization. White background with grid. Professional curriculum learning figure.
```

### Post-Processing Notes

- Use step function with clear plateau at each context length
- Add time/compute annotations showing relative training duration at each stage
- Inset should contrast short-context (dense attention) vs long-context (sparse attention) patterns
- Include model examples: "HyenaDNA: 1kb → 32kb → 1Mb"
- Annotate what is learned at each stage: "Local patterns" → "Medium-range" → "Long-range regulatory"

### Fallback Description

Create in matplotlib:
- Step function plot with context length vs. training steps
- Annotations at each transition
- Inset comparing attention patterns

### Caption

**Recommended Caption:**
"Context length curriculum for stable long-range pretraining. Training begins at short contexts (1-4 kb) where optimization is stable and local patterns are learned efficiently. At each stage transition, weights are inherited from the previous checkpoint with learning rate warmup to accommodate the new context regime. Progressive extension through intermediate stages (16 kb, 64 kb) enables the model to learn medium-range dependencies before tackling full long-range contexts. This curriculum proved essential for HyenaDNA: direct training at million-base contexts without warmup led to divergence. The inset shows how attention patterns become sparser at longer contexts, requiring more training steps to develop the structured patterns that capture distant regulatory relationships."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 8.1 Pretraining Objectives | 3 | Essential | Medium (three-panel schematic) |
| 8.2 Masking Strategies | 2 | High | Medium (comparison) |
| 8.3 Bidirectional vs AR | 2 | Essential | Low-Medium (information flow) |
| 8.4 Cross-Species Contrastive | 1 | Enhancing | Medium (evolutionary) |
| 8.5 Multitask Pretraining | 1 | High | Medium (architecture) |
| 8.6 Context Curriculum | 1 | High | Medium (training diagram) |

**Total files:** 10
**Recommended generation order:** 8.3A-B (information flow, clearest), 8.1A-C (objectives comparison), 8.2A-B (masking strategies), 8.6 (curriculum), 8.5 (architecture), 8.4 (cross-species, most complex)
# Figure Report: Chapter 9 - Transfer Learning Foundations

**Chapter:** Part 2, Chapter 9 - Transfer Learning Foundations
**Date:** 2026-01-07
**Figures:** 1 conceptual figure (1 file)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 9.1: Domain Alignment in Transfer Learning

**File:** `figs/part_2/ch09/01-fig-domain-alignment.svg`
**Priority:** Essential
**Type:** Schematic / conceptual diagram

### Content Description

Schematic illustrating domain shift in genomic transfer learning with three components:
- Left panel (Source Domain): Diverse genomic sequences during pretraining, with learned representations capturing statistical regularities (local motifs, composition, conservation)
- Right panel (Target Domain): Sparse labeled examples for clinical task (e.g., pathogenic variants, tissue-specific enhancers), highlighting distributional differences
- Center: Representation space showing well-transferred features (local motifs, conservation patterns) connected by solid arrows vs. poorly-transferred features (long-range regulatory logic, tissue-specific patterns) with dashed arrows indicating transfer failure

### DALL-E Prompt

```
Create a scientific diagram illustrating domain shift in genomic transfer learning. Save as: 01-fig-domain-alignment.svg

Three-part layout:

LEFT PANEL (Source Domain):
- Multiple DNA sequence representations showing diversity
- Abstract representation space with clustered points
- Labels: "Billions of sequences", "Local motifs", "Sequence composition", "Conservation patterns"
- Blue color scheme (#1f77b4)

CENTER (Representation Space):
- Circular or spherical space showing embedding clusters
- Solid arrows connecting source features to target tasks that transfer well
- Dashed/broken arrows for features that fail to transfer
- Labels: "Well-transferred" (solid), "Poor transfer" (dashed)
- Gradient from blue (source) to orange (target)

RIGHT PANEL (Target Domain):
- Sparse data points representing limited labeled clinical examples
- Labels: "Hundreds of examples", "Pathogenic variants", "Tissue-specific enhancers"
- Orange color scheme (#d62728)

Clean scientific illustration style, white background, publication quality. Professional machine learning transfer learning diagram.
```

### Post-Processing Notes

- Add clear labels for source and target domains
- Use arrows to show transfer pathways with success/failure distinction
- Include example features that transfer well vs. poorly
- Add annotation: "Transfer fails silently when distributional gap is too large"

### Fallback Description

Create in diagramming software (draw.io, BioRender):
- Three-panel layout with source domain, representation space, target domain
- Use arrows of different styles (solid for good transfer, dashed for failure)
- Color-code by domain origin

### Caption

**Recommended Caption:**
"Domain shift in genomic transfer learning. The source domain (left) contains billions of diverse genomic sequences from which pretrained models learn statistical regularities including local motifs, sequence composition, and conservation patterns. The target domain (right) presents sparse labeled examples for specific clinical tasks such as pathogenic variant classification or tissue-specific enhancer prediction. In the learned representation space (center), some features transfer effectively (solid arrows): local motif recognition and conservation patterns align between domains. Other features transfer poorly (dashed arrows): long-range regulatory logic and tissue-specific patterns present in targets may be absent or misleading in source representations. The challenge is that transfer failures are silent—models produce confident predictions regardless of whether underlying features are appropriate for the target task."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 9.1 Domain Alignment | 1 | Essential | Medium (conceptual) |

**Total files:** 1
**Recommended generation order:** 9.1 (single figure)
# Figure Report: Chapter 10 - Adaptation Strategies

**Chapter:** Part 2, Chapter 10 - Adaptation Strategies
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (12 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 10.1: LoRA Architecture

**File:** `figs/part_2/ch10/01-fig-lora-architecture.svg`
**Priority:** Essential
**Type:** Architecture schematic

### Content Description

Schematic of LoRA (Low-Rank Adaptation) showing:
- Original frozen weight matrix W (large, grayed out to indicate frozen)
- Low-rank decomposition matrices A and B (smaller, colored to indicate trainable)
- Computation flow showing W + BA during forward pass
- Parameter count comparison: "500M frozen vs. 2-5M trainable"
- Mathematical notation: W' = W + BA

### DALL-E Prompt

```
Create a scientific diagram showing LoRA (Low-Rank Adaptation) architecture. Save as: 01-fig-lora-architecture.svg

Main elements:

FROZEN WEIGHTS (left):
- Large rectangular matrix labeled "W"
- Gray color (#7f7f7f) indicating frozen
- Dimension annotation: "d × d"
- Label: "Frozen (500M params)"

LOW-RANK MATRICES (right):
- Two smaller matrices labeled "A" and "B"
- Colored blue (#1f77b4) indicating trainable
- Matrix A: "d × r" dimensions
- Matrix B: "r × d" dimensions
- Label: "Trainable (2-5M params)"

COMPUTATION FLOW:
- Plus symbol between W and BA product
- Arrow showing: W' = W + BA
- Forward pass annotation

PARAMETER COMPARISON:
- Side bar comparing "Frozen: 500M" vs "Trainable: 2M"
- Visual ratio showing ~100:1 difference

Clean neural network architecture diagram style, white background, publication quality. Professional deep learning PEFT illustration.
```

### Post-Processing Notes

- Add mathematical formula: W' = W + BA
- Clearly distinguish frozen (gray) from trainable (blue) components
- Add rank parameter annotation: "r = 8-64 typical"
- Include memory/compute savings annotation

### Fallback Description

Create in diagramming software:
- Matrix visualization with dimension labels
- Color coding for frozen vs. trainable parameters
- Mathematical notation overlay

### Caption

**Recommended Caption:**
"Low-Rank Adaptation (LoRA) architecture. Rather than updating the full weight matrix W directly, LoRA introduces two smaller matrices A and B whose product approximates the desired weight change: W' = W + BA. During fine-tuning, W remains frozen (gray, 500 million parameters typical) while only A and B receive gradient updates (blue, 2-5 million parameters). The rank r (typically 8-64) controls adaptation expressiveness: lower ranks introduce fewer parameters and stronger implicit regularization; higher ranks enable more flexible task-specific modification at greater overfitting risk. This approach reduces memory requirements by an order of magnitude compared with full fine-tuning while achieving comparable performance on many downstream tasks."

---

## Figure 10.2: Layer Probing for Decoder Models (Two-Panel)

**Files:**
- `figs/part_2/ch10/02-A-fig-layer-probing-decoder.svg`
- `figs/part_2/ch10/02-B-fig-layer-probing-decoder.svg`

**Priority:** Essential
**Type:** Performance comparison plots

### Panel A: Encoder Model Layer Performance

**Content:** Line plot showing classification accuracy (y-axis) vs. layer number (x-axis) for an encoder model like DNABERT. Shows relatively flat performance across layers with slight improvement toward final layers. Demonstrates that final-layer embeddings work reliably.

**DALL-E Prompt:**
```
Create a scientific line plot showing encoder model layer-wise performance. Save as: 02-A-fig-layer-probing-decoder.svg

Plot elements:
- X-axis: "Layer Number" (1-12)
- Y-axis: "Classification Accuracy" (0.6-0.9)
- Single line showing relatively flat performance with slight upward trend
- Performance starts around 0.75, gradually increases to ~0.85 at final layer
- Final layer highlighted with marker and annotation: "Final layer reliable"
- Title: "Encoder Model (DNABERT-style)"
- Shaded confidence interval around line

Blue line color (#1f77b4). Clean scientific plot style with grid lines, white background. Professional machine learning evaluation figure.
```

**Caption for Panel A:**
"Encoder model layer-wise performance. For encoder architectures like DNABERT, classification accuracy remains relatively stable across layers with slight improvement toward the final layer. The bidirectional attention mechanism ensures that every position's representation incorporates information from the entire sequence at every layer, making final-layer embeddings a reliable default choice for downstream classification."

### Panel B: Decoder Model Layer Performance

**Content:** Line plot showing inverted-U pattern for decoder models. Performance peaks at middle layers (around layer 4-8 of 12), with notably degraded performance at the final layer. Demonstrates the "layer hunting problem."

**DALL-E Prompt:**
```
Create a scientific line plot showing decoder model layer-wise performance. Save as: 02-B-fig-layer-probing-decoder.svg

Plot elements:
- X-axis: "Layer Number" (1-12)
- Y-axis: "Classification Accuracy" (0.6-0.9)
- Line showing inverted-U pattern
- Performance starts ~0.70, peaks at layers 6-8 (~0.85), drops to ~0.65 at layer 12
- Final layer highlighted in RED with annotation: "Final layer degraded"
- Peak region annotated: "Optimal layers vary by task"
- Title: "Decoder Model (HyenaDNA-style)"
- Shaded confidence interval

Orange line color (#d62728) with red highlight on final layer. Clean scientific plot style with grid lines, white background. Professional layer hunting problem visualization.
```

**Caption for Panel B:**
"Decoder model layer-wise performance reveals the 'layer hunting problem.' Performance peaks at intermediate layers (6-8) and degrades substantially at the final layer. The next-token prediction objective specializes final layers for vocabulary distribution prediction, discarding information irrelevant to that task but potentially critical for downstream classification. Practitioners using decoder models must systematically evaluate all layers to identify optimal extraction points."

### Combined Caption

**Full Figure Caption:**
"Layer-wise probing reveals fundamental differences between encoder and decoder architectures. (A) Encoder models like DNABERT show relatively stable performance across layers, with the final layer providing reliable representations for classification. The bidirectional attention mechanism integrates information from the entire sequence at every layer. (B) Decoder models like HyenaDNA show an inverted-U pattern, with peak performance at intermediate layers and degraded performance at the final layer. The next-token prediction objective specializes final layers for a narrow purpose, creating what practitioners call the 'layer hunting problem': optimal embedding extraction requires systematic search across layers rather than defaulting to final-layer representations."

---

## Figure 10.3: Adaptation Strategy Decision Tree

**File:** `figs/part_2/ch10/03-fig-adaptation-decision-tree.svg`
**Priority:** Essential
**Type:** Decision flowchart

### Content Description

Flowchart guiding adaptation strategy selection with decision nodes:
1. "Labeled data quantity?" → branches for <500, 500-5000, >10000
2. "Task similarity to pretraining?" → high/moderate/low branches
3. "Computational constraints?" → limited/moderate/substantial branches

Terminal nodes recommend: Linear probing, LoRA/Adapters, Full fine-tuning, or From-scratch training, with expected tradeoffs at each terminal (accuracy, compute, overfitting risk).

### DALL-E Prompt

```
Create a scientific decision flowchart for transfer learning adaptation strategy selection. Save as: 03-fig-adaptation-decision-tree.svg

Decision tree structure:

ROOT NODE: "Choose Adaptation Strategy"

LEVEL 1 - Diamond decision: "Labeled examples?"
- Branch "<500": leads to "Linear Probing" (green terminal)
- Branch "500-5,000": leads to next decision
- Branch ">10,000": leads to next decision

LEVEL 2 - Diamond decisions for data-dependent paths
- "Task similarity to pretraining?"
- Branches: High → LoRA, Moderate → LoRA/Adapters, Low → Full fine-tuning check

LEVEL 3 - Compute constraints check
- "Compute available?" → Full fine-tuning or From-scratch

TERMINAL NODES (rounded rectangles):
- "Linear Probing": Low risk, low compute, minutes
- "LoRA/Adapters": Moderate risk, hours, 1 GPU
- "Full Fine-tuning": High risk, days, multi-GPU
- "From Scratch": Variable, weeks, when no suitable pretrained model

Color code: Green for low-risk/low-compute, yellow for moderate, red for high-risk/high-compute. Clean flowchart style with decision diamonds and process rectangles. White background. Professional ML decision guide.
```

### Post-Processing Notes

- Add tradeoff annotations at each terminal node
- Include computational cost estimates (minutes/hours/days)
- Add risk indicators (low/moderate/high overfitting risk)
- Color-code by recommendation strength

### Fallback Description

Create in flowchart software (Lucidchart, draw.io):
- Decision diamonds at branch points
- Terminal rectangles with recommendations
- Color coding by strategy risk level
- Annotations for compute and data requirements

### Caption

**Recommended Caption:**
"Decision framework for adaptation strategy selection. Data quantity dominates the decision: with fewer than 500 labeled examples, only linear probing avoids catastrophic overfitting; between 500 and 5,000 examples, parameter-efficient methods like LoRA offer favorable tradeoffs; above 10,000 examples, full fine-tuning becomes viable. Task similarity to pretraining and computational constraints further refine the choice. Terminal nodes indicate recommended strategies with expected tradeoffs: linear probing requires minimal compute but limits flexibility; LoRA balances adaptation capacity with regularization; full fine-tuning offers maximum flexibility at highest overfitting risk; from-scratch training remains appropriate when no suitable pretrained model exists."

---

## Figure 10.4: Domain Shift Detection (Three-Panel)

**Files:**
- `figs/part_2/ch10/04-A-fig-domain-shift-detection.svg`
- `figs/part_2/ch10/04-B-fig-domain-shift-detection.svg`
- `figs/part_2/ch10/04-C-fig-domain-shift-detection.svg`

**Priority:** High
**Type:** Diagnostic visualization suite

### Panel A: Embedding Space Visualization

**Content:** UMAP/t-SNE projection showing training distribution as dense cluster and test examples at varying distances. Out-of-distribution examples clearly separated from training manifold.

**DALL-E Prompt:**
```
Create a scientific UMAP embedding visualization showing domain shift detection. Save as: 04-A-fig-domain-shift-detection.svg

Plot elements:
- Dense cluster of training points (blue, #1f77b4) forming main distribution
- Test points colored by distance from training:
  - Green points: within training distribution (in-distribution)
  - Yellow points: edge of distribution (borderline)
  - Red points: clearly separated (out-of-distribution)
- Boundary line or shaded region showing training distribution extent
- Annotations: "Training distribution", "In-distribution test", "OOD examples"

Clean scientific scatter plot with legend. White background with subtle axes. Professional domain shift detection visualization.
```

**Caption for Panel A:**
"Embedding space visualization for domain shift detection. Training examples (blue) form a dense cluster defining the learned representation space. Test examples colored by distance from training distribution: in-distribution (green), borderline (yellow), and out-of-distribution (red). Examples far from the training manifold should receive appropriately high uncertainty in downstream predictions."

### Panel B: Calibration Comparison

**Content:** Calibration curves comparing confidence vs. accuracy for in-distribution (well-calibrated, near diagonal) vs. out-of-distribution examples (overconfident, curve below diagonal).

**DALL-E Prompt:**
```
Create a scientific calibration diagram comparing in-distribution vs OOD performance. Save as: 04-B-fig-domain-shift-detection.svg

Plot elements:
- X-axis: "Predicted Confidence" (0 to 1)
- Y-axis: "Observed Accuracy" (0 to 1)
- Diagonal reference line (perfect calibration, gray dashed)
- In-distribution curve (blue): closely following diagonal
- Out-of-distribution curve (red): significantly below diagonal, especially at high confidence
- Shaded areas showing calibration error
- Annotations: "Well-calibrated (in-distribution)", "Overconfident (OOD)"

Clean reliability diagram style with grid lines, white background. Professional calibration analysis figure.
```

**Caption for Panel B:**
"Calibration curves reveal overconfidence on out-of-distribution data. In-distribution test examples (blue) show well-calibrated predictions, with confidence matching accuracy along the diagonal. Out-of-distribution examples (red) show systematic overconfidence: the model predicts high confidence even when accuracy is low. This overconfidence on OOD data is particularly dangerous in clinical settings where confident wrong predictions may not be questioned."

### Panel C: Performance Degradation Curve

**Content:** Line plot showing accuracy declining as distributional distance from training data increases. Quantifies the relationship between distribution shift and performance loss.

**DALL-E Prompt:**
```
Create a scientific line plot showing performance degradation with domain shift. Save as: 04-C-fig-domain-shift-detection.svg

Plot elements:
- X-axis: "Distance from Training Distribution" (low to high)
- Y-axis: "Model Accuracy" (0.5 to 1.0)
- Declining curve starting high (~0.9) at low distance, dropping to chance (~0.55) at high distance
- Shaded confidence interval around curve
- Vertical dashed lines marking regions: "Safe", "Caution", "Unreliable"
- Threshold line at chance performance

Blue gradient line showing degradation. Clean scientific plot style with grid lines, white background. Professional domain shift analysis figure.
```

**Caption for Panel C:**
"Performance degradation as a function of distributional distance. Model accuracy declines monotonically as test examples move farther from the training distribution. The curve quantifies when predictions should be trusted: 'safe' regions near training distribution maintain high accuracy; 'caution' regions show degraded but above-chance performance; 'unreliable' regions approach chance accuracy and predictions should be abstained."

### Combined Caption

**Full Figure Caption:**
"Detecting domain shift before deployment prevents silent clinical failures. (A) UMAP visualization of embedding space shows test examples colored by distance from training distribution. Out-of-distribution examples (red) occupy regions where model predictions cannot be trusted. (B) Calibration analysis reveals that in-distribution predictions follow the diagonal (well-calibrated) while out-of-distribution predictions fall below (overconfident). This overconfidence makes OOD failures particularly dangerous. (C) Performance degradation quantifies the relationship between distributional distance and accuracy, enabling threshold-based decisions about when to trust predictions versus abstain."

---

## Figure 10.5: Validation Pitfalls (Four-Panel)

**Files:**
- `figs/part_2/ch10/05-A-fig-validation-pitfalls.svg`
- `figs/part_2/ch10/05-B-fig-validation-pitfalls.svg`
- `figs/part_2/ch10/05-C-fig-validation-pitfalls.svg`
- `figs/part_2/ch10/05-D-fig-validation-pitfalls.svg`

**Priority:** High
**Type:** Multi-panel warning illustration

### Panel A: Data Leakage Through Overlap

**Content:** Venn diagram showing pretraining data overlapping with test data, highlighting how this creates leakage and inflated performance.

**DALL-E Prompt:**
```
Create a scientific Venn diagram showing data leakage from pretraining overlap. Save as: 05-A-fig-validation-pitfalls.svg

Diagram elements:
- Left circle: "Pretraining Data" (blue, #1f77b4)
- Right circle: "Test/Benchmark Data" (orange, #d62728)
- Overlap region: "LEAKAGE" (highlighted red with warning pattern)
- Arrow from overlap to annotation: "Inflated Performance"
- Example text: "UniRef sequences in ProteinGym benchmarks"

Clean Venn diagram style with bold overlap highlighting, white background. Professional data leakage warning figure.
```

**Caption for Panel A:**
"Pretraining data overlap creates leakage. When sequences from pretraining corpora (blue) overlap with benchmark test sets (orange), the model has effectively 'seen' the test data, inflating apparent performance. This is particularly problematic for large foundation models trained on massive genomic databases that may inadvertently include benchmark sequences."

### Panel B: Temporal Leakage

**Content:** Timeline showing training on variants annotated after test set creation, illustrating how temporal ordering violations create leakage.

**DALL-E Prompt:**
```
Create a scientific timeline diagram showing temporal leakage in variant annotation. Save as: 05-B-fig-validation-pitfalls.svg

Timeline elements:
- Horizontal timeline with dates (2018-2024)
- "Test Set Created" marker at 2020
- "Training Data" bar extending from 2018 to 2023 (includes future!)
- "Leakage Zone" highlighted red: 2020-2023 (post-test creation)
- Arrow showing "Future information in training"
- Correct approach shown below: training stops before test set creation

Clean timeline diagram with warning highlights, white background. Professional temporal leakage illustration.
```

**Caption for Panel B:**
"Temporal leakage uses future information unavailable at prediction time. When training includes variants annotated after benchmark creation (red zone), the model may have learned from the same evidence that later informed test labels. Proper temporal splits train only on data available before the prediction cutoff, simulating realistic prospective deployment."

### Panel C: Baseline Comparison Issues

**Content:** Bar chart comparing foundation model against weak baseline (large gap, misleading) vs. properly-tuned baseline (small gap, realistic).

**DALL-E Prompt:**
```
Create a scientific bar chart showing misleading vs fair baseline comparisons. Save as: 05-C-fig-validation-pitfalls.svg

Chart elements:
Two grouped comparisons side by side:

LEFT GROUP "Misleading Comparison":
- Short bar: "Weak Baseline" (~60%)
- Tall bar: "Foundation Model" (~90%)
- Large gap highlighted with "30% improvement!"
- Red warning annotation

RIGHT GROUP "Fair Comparison":
- Medium bar: "Tuned Baseline" (~85%)
- Tall bar: "Foundation Model" (~90%)
- Small gap highlighted with "5% improvement"
- Green checkmark annotation

X-axis: Comparison type. Y-axis: Accuracy (0-100%). Clean bar chart style with annotations, white background. Professional baseline comparison figure.
```

**Caption for Panel C:**
"Baseline selection dramatically affects perceived transfer value. Comparing against weak or poorly-tuned baselines (left) inflates apparent foundation model improvements. Fair evaluation requires properly-tuned baselines with equivalent hyperparameter search and appropriate architectures (right). The true benefit of transfer is the gap above a strong baseline, not the gap above a strawman."

### Panel D: Stratified Performance Hidden

**Content:** Two bar charts: one showing aggregate accuracy (90%), another showing stratified view revealing aggregate hides rare-variant failure (common: 95%, rare: 50%).

**DALL-E Prompt:**
```
Create a scientific figure showing hidden stratified performance failures. Save as: 05-D-fig-validation-pitfalls.svg

Two side-by-side bar charts:

LEFT CHART "Aggregate (Misleading)":
- Single tall bar: "Overall Accuracy" at 90%
- Green color suggesting good performance
- Checkmark icon

RIGHT CHART "Stratified (Revealing)":
- Two bars:
  - "Common variants" at 95% (green)
  - "Rare variants" at 50% (red, warning)
- Arrow pointing to rare variants: "Clinically important!"
- Annotation: "Aggregate conceals failure on rare variants"

Clean bar chart style with warning highlights, white background. Professional stratified evaluation figure.
```

**Caption for Panel D:**
"Aggregate metrics conceal stratified failures. Overall accuracy of 90% (left) appears acceptable, but stratified analysis (right) reveals systematic failure on rare variants (50% accuracy) masked by good performance on common variants (95%). Since rare variants are often the clinically important ones, aggregate reporting can hide the failures that matter most for patient care."

### Combined Caption

**Full Figure Caption:**
"Common validation pitfalls that inflate transfer learning claims. (A) Overlap between pretraining data and benchmarks creates leakage, allowing models to 'remember' test examples. (B) Temporal leakage occurs when training includes information from after benchmark creation. (C) Weak baseline comparisons exaggerate transfer benefits; fair evaluation requires properly-tuned from-scratch baselines. (D) Aggregate metrics conceal stratified failures; rare variants may show near-random performance while being masked by high accuracy on common variants. Together, these pitfalls can make ineffective transfer appear successful until clinical deployment reveals the failures."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 10.1 LoRA Architecture | 1 | Essential | Medium (schematic) |
| 10.2 Layer Probing | 2 | Essential | Medium (comparison plots) |
| 10.3 Decision Tree | 1 | Essential | Medium (flowchart) |
| 10.4 Domain Shift Detection | 3 | High | Medium (diagnostic suite) |
| 10.5 Validation Pitfalls | 4 | High | Medium (warning illustrations) |

**Total files:** 11
**Recommended generation order:** 10.1 (LoRA, foundational), 10.3 (decision tree), 10.2A-B (layer probing), 10.4A-C (domain shift), 10.5A-D (pitfalls)
# Figure Report: Chapter 11 - Benchmarks and Evaluation

**Chapter:** Part 2, Chapter 11 - Benchmarks and Evaluation
**Date:** 2026-01-07
**Figures:** 9 conceptual figures (14 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 11.1: Benchmark Landscape

**File:** `figs/part_2/ch11/01-fig-benchmark-landscape.svg`
**Priority:** Essential
**Type:** Landscape overview / taxonomy diagram

### Content Description

Overview map of genomic AI benchmarks organized by task category (variant effect, regulatory, expression, structure) and evaluation paradigm (zero-shot, linear probe, fine-tuning). Show major benchmarks with their characteristics: data source, task type, metrics, known limitations.

### DALL-E Prompt

```
Create a scientific landscape diagram showing genomic AI benchmark ecosystem. Save as: 01-fig-benchmark-landscape.svg

Matrix/landscape layout:

ROWS (Task Categories):
- Variant Effect Prediction
- Regulatory Element Classification
- Expression Prediction
- Protein Structure/Function

COLUMNS (Evaluation Paradigms):
- Zero-Shot
- Linear Probing
- Fine-Tuning

WITHIN CELLS:
- Benchmark names as boxes (e.g., "ClinVar", "ProteinGym", "ENCODE", "DMS assays")
- Color-coded by data quality/reliability
- Size indicates community adoption

ANNOTATIONS:
- Data source icons (clinical database, experimental assay)
- Warning symbols for known limitations
- Connection lines showing benchmark overlaps

Clean scientific taxonomy diagram with organized grid layout. Blue/green color scheme. White background. Professional benchmark ecosystem map.
```

### Post-Processing Notes

- Add benchmark names within appropriate cells
- Color-code by benchmark maturity/reliability
- Include legend for icons and colors
- Add annotations for known issues (leakage, saturation)

### Fallback Description

Create in diagramming software:
- Grid layout with task rows and paradigm columns
- Benchmark names as labeled boxes within cells
- Color coding and icons for characteristics

### Caption

**Recommended Caption:**
"The genomic AI benchmark landscape organized by task category (rows) and evaluation paradigm (columns). Major benchmarks are positioned according to what they test: variant effect prediction relies on ClinVar, DMS assays, and ProteinGym; regulatory classification uses ENCODE and custom enhancer datasets; expression prediction evaluates against GTEx and tissue-specific measurements; protein structure benchmarks include CASP and AlphaFold evaluations. Evaluation paradigms range from zero-shot (no task-specific training) through linear probing (frozen embeddings) to full fine-tuning. Color intensity indicates benchmark maturity and community adoption. Warning symbols mark benchmarks with known limitations including potential leakage or approaching saturation."

---

## Figure 11.2: Leakage Pathways

**File:** `figs/part_2/ch11/02-fig-leakage-pathways.svg`
**Priority:** High
**Type:** Flow diagram with warning highlights

### Content Description

Flow diagram showing data flow with leakage pathways highlighted:
- Central pipeline: Pretraining → Foundation Model → Fine-tuning → Benchmark
- Leakage pathways (red): Direct overlap, homology leakage, label circularity, resource sharing, community iteration
- Specific examples: ESM/UniRef → ProteinGym, ClinVar/CADD circularity, ENCODE in both pretraining and evaluation

### DALL-E Prompt

```
Create a scientific flow diagram showing data leakage pathways in genomic AI. Save as: 02-fig-leakage-pathways.svg

Main pipeline (horizontal, blue arrows):
Pretraining Data → Foundation Model → Fine-tuning → Benchmark Evaluation

LEAKAGE PATHWAYS (red dashed lines with warning symbols):

1. Direct Overlap: Red arrow from pretraining to benchmark
   - Example: "UniRef sequences in ProteinGym"

2. Homology Leakage: Red curved arrow showing sequence similarity
   - Example: "80% identity between train/test proteins"

3. Label Circularity: Red bidirectional arrow
   - Example: "CADD→ClinVar→New predictors→ClinVar"

4. Resource Sharing: Red connection between stages
   - Example: "ENCODE in pretraining and evaluation"

5. Community Iteration: Red loop back
   - Example: "Benchmark overfitting across publications"

Legitimate flow in blue, leakage in red dashed. Warning triangles at each leakage point. Clean scientific diagram with white background. Professional data flow and leakage visualization.
```

### Post-Processing Notes

- Use consistent color coding: blue for legitimate flow, red for leakage
- Add specific example annotations for each leakage type
- Include warning symbols at leakage points
- Add legend distinguishing pathway types

### Fallback Description

Create in diagramming software:
- Horizontal pipeline with boxes for each stage
- Red dashed arrows for leakage pathways
- Warning symbols and example annotations

### Caption

**Recommended Caption:**
"Data leakage pathways in genomic foundation model evaluation. The legitimate pipeline (blue) flows from pretraining through fine-tuning to benchmark evaluation. Leakage pathways (red dashed) create spurious performance: direct overlap when pretraining includes benchmark sequences; homology leakage when training and test sets share high-similarity sequences; label circularity when computational predictions influence ground truth labels that later serve as training targets; resource sharing when databases like ENCODE appear in both pretraining and evaluation; and community iteration when the field collectively overfits to standard benchmarks through publication cycles. Each pathway inflates apparent performance without improving genuine biological understanding."

---

## Figure 11.3: Benchmark Saturation (Two-Panel)

**Files:**
- `figs/part_2/ch11/03-A-fig-benchmark-saturation.svg`
- `figs/part_2/ch11/03-B-fig-benchmark-saturation.svg`

**Priority:** High
**Type:** Temporal analysis plots

### Panel A: Saturation Curve

**Content:** Time vs. benchmark performance showing multiple model generations approaching a performance ceiling. Saturation zone annotation where improvements become marginal.

**DALL-E Prompt:**
```
Create a scientific plot showing benchmark performance saturation over time. Save as: 03-A-fig-benchmark-saturation.svg

Plot elements:
- X-axis: Year (2018-2025)
- Y-axis: Benchmark Performance (e.g., auROC 0.7-1.0)
- Multiple lines for different model generations converging toward ceiling
- Horizontal dashed line at ~0.95 labeled "Performance Ceiling"
- Shaded region near ceiling labeled "Saturation Zone"
- Individual points marking major model releases
- Diminishing gaps between successive models near ceiling

Model labels: "CADD", "REVEL", "ESM", "AlphaMissense"
Annotation: "Marginal improvements despite architectural advances"

Clean scientific temporal plot with legend, white background. Professional benchmark saturation analysis.
```

**Caption for Panel A:**
"Benchmark saturation over time. Multiple model generations (lines) improve performance on standard benchmarks but converge toward a ceiling (dashed line). The saturation zone (shaded) shows where improvements become marginal despite continued architectural advances. This pattern suggests either that the benchmark no longer discriminates between methods or that genuine performance limits have been reached."

### Panel B: Benchmark Staleness Timeline

**Content:** Timeline showing benchmark creation dates versus current year, highlighting growing temporal gap between benchmark construction and model evaluation.

**DALL-E Prompt:**
```
Create a scientific timeline showing benchmark staleness. Save as: 03-B-fig-benchmark-saturation.svg

Timeline layout:
- Horizontal axis: Years (2010-2025)
- Top row: Benchmark creation dates as markers
  - "ENCODE 2012", "ClinVar 2013", "ProteinGym 2022"
- Bottom row: "Current evaluation year" marker at 2025
- Vertical connecting lines with gap annotations
- Color gradient from green (recent) to red (stale)
- Growing gap visualization as widening bracket

Annotations:
- "10+ year gap for ENCODE benchmarks"
- "Biology evolves, benchmarks don't"

Clean timeline diagram with staleness indicators. White background. Professional temporal benchmark analysis.
```

**Caption for Panel B:**
"Benchmark staleness timeline. Benchmark creation dates (top) versus current evaluation (bottom) reveal growing temporal gaps. ENCODE-based benchmarks reflect 2012-era annotations; ClinVar benchmarks evolve but retain historical biases; even recent benchmarks like ProteinGym become stale as the field iterates. The gap between when benchmarks were constructed and when they are used for evaluation grows each year, potentially measuring performance on outdated or superseded annotations."

### Combined Caption

**Full Figure Caption:**
"Benchmark saturation and staleness limit evaluation validity. (A) Performance saturation: multiple model generations converge toward benchmark ceilings where marginal improvements no longer indicate meaningful advances. The saturation zone (shaded) suggests benchmarks have lost discriminative power. (B) Benchmark staleness: growing temporal gaps between benchmark creation and current evaluation. Benchmarks created years ago may reflect outdated annotations, superseded biological understanding, or distributions that no longer match contemporary data. Together, saturation and staleness motivate development of new benchmarks that capture aspects of biological prediction that current standards miss."

---

## Figure 11.4: Proxy-Target Gap

**File:** `figs/part_2/ch11/04-fig-proxy-target-gap.svg`
**Priority:** Essential
**Type:** Conceptual gap diagram

### Content Description

Conceptual diagram showing the gap between what benchmarks measure (proxies) and what we actually want (targets):
- Left column: What we measure (ClinVar labels, held-out auROC, DMS correlation, expression prediction accuracy)
- Right column: What we want (True clinical impact, deployment discrimination, actual protein function, regulatory mechanism)
- Center: Arrows with gap indicators showing how well proxies align with targets
- Gap factors: label quality, distribution shift, metric mismatch, temporal drift

### DALL-E Prompt

```
Create a scientific diagram showing the proxy-target gap in benchmark evaluation. Save as: 04-fig-proxy-target-gap.svg

Two-column layout with center gap indicators:

LEFT COLUMN "What We Measure" (blue boxes):
- "ClinVar pathogenicity labels"
- "Held-out auROC"
- "DMS correlation"
- "Expression prediction R²"

RIGHT COLUMN "What We Want" (green boxes):
- "True clinical impact"
- "Deployment discrimination"
- "Actual protein function"
- "Regulatory mechanism"

CENTER (Gap indicators):
- Arrows connecting proxies to targets
- Arrow width indicates proxy strength (thick = good proxy, thin = poor proxy)
- Gap labels: "Label quality gap", "Distribution shift", "Metric mismatch", "Temporal drift"
- Red zones highlighting where gaps are largest

Bottom annotation: "High benchmark performance ≠ deployment success"

Clean conceptual diagram with color-coded columns and gap visualization. White background. Professional evaluation validity figure.
```

### Post-Processing Notes

- Vary arrow widths to indicate proxy quality
- Color-code gap severity (green for good alignment, red for poor)
- Add specific examples for each gap type
- Include key insight annotation

### Fallback Description

Create in diagramming software:
- Two-column layout with connecting arrows
- Gap annotations and width variation
- Color coding for alignment quality

### Caption

**Recommended Caption:**
"The proxy-target gap in genomic AI evaluation. What benchmarks measure (left) differs systematically from what we ultimately want (right). ClinVar labels proxy for clinical impact but reflect curation biases and circularity with computational predictions. Held-out auROC proxies for deployment discrimination but assumes matched distributions. DMS correlations proxy for protein function but capture only selected perturbations in specific assay conditions. Expression prediction accuracy proxies for regulatory understanding but may reflect technical confounds. Arrow widths indicate proxy strength; gap annotations identify sources of misalignment. The central insight: high benchmark performance does not guarantee deployment success."

---

## Figure 11.5: Cross-Population Performance

**File:** `figs/part_2/ch11/05-fig-cross-population-performance.svg`
**Priority:** High
**Type:** Grouped performance comparison

### Content Description

Grouped bar chart or heatmap showing:
- Rows: Different tasks/models
- Columns: Ancestry groups (European, African, East Asian, South Asian, Admixed)
- Values: Performance metrics with clear degradation for non-European groups
- Annotations: sample sizes, significance, training data representation

### DALL-E Prompt

```
Create a scientific grouped bar chart showing cross-population model performance. Save as: 05-fig-cross-population-performance.svg

Chart structure:
- X-axis groups: "European", "African", "East Asian", "South Asian", "Admixed"
- Y-axis: "Relative Performance" (0-100%)
- Multiple bar colors for different model types:
  - Blue: Polygenic risk scores
  - Green: Variant classifiers
  - Orange: Regulatory predictors

Performance pattern:
- European: ~100% (reference)
- African: ~40-60% (major degradation)
- East Asian: ~70-80%
- South Asian: ~65-75%
- Admixed: ~55-70%

Annotations:
- Sample size indicators above each group
- Error bars on all bars
- Training data composition pie chart inset showing ~78% European
- Key finding: "40-75% performance reduction for African ancestry"

Clean grouped bar chart with legend and annotations. White background. Professional cross-population evaluation figure.
```

### Post-Processing Notes

- Add sample size annotations for each population
- Include error bars for uncertainty
- Add inset showing training data composition
- Highlight key finding about performance reduction

### Fallback Description

Create in matplotlib/seaborn:
- Grouped bar chart with ancestry on x-axis
- Multiple model types as bar colors
- Error bars and annotations

### Caption

**Recommended Caption:**
"Cross-population performance reveals systematic failures for underrepresented ancestries. Relative performance (European as reference) degrades substantially for non-European groups across multiple model types: polygenic risk scores (blue), variant classifiers (green), and regulatory predictors (orange). African-ancestry individuals show 40-75% performance reductions despite constituting only 2% of typical training data while representing 16% of the global population. These disparities reflect both training data composition (inset: ~78% European) and fundamental differences in linkage disequilibrium structure across populations. Aggregate benchmark metrics that do not report stratified performance by ancestry conceal these failures."

---

## Figure 11.6: Random Splits Fail (Three-Panel)

**Files:**
- `figs/part_2/ch11/06-A-fig-random-splits-fail.svg`
- `figs/part_2/ch11/06-B-fig-random-splits-fail.svg`
- `figs/part_2/ch11/06-C-fig-random-splits-fail.svg`

**Priority:** Essential
**Type:** Comparison showing why random splits fail for genomic data

### Panel A: Image Classification (Random Works)

**Content:** Grid of independent images where random assignment to train/test works because examples are truly independent.

**DALL-E Prompt:**
```
Create a scientific diagram showing random splits work for images. Save as: 06-A-fig-random-splits-fail.svg

Grid layout:
- 4x4 grid of small image icons (simple shapes/objects)
- Random color coding: blue for training, orange for test
- No connections between images (independent)
- Label: "Images: Independent samples"
- Checkmark annotation: "Random splits valid"

Clean grid diagram with colored assignment, white background. Professional data splitting example.
```

**Caption for Panel A:**
"Random splits are valid for independent samples. In image classification, each image is an independent sample from the data distribution. Random assignment to training (blue) and test (orange) sets provides unbiased performance estimates because seeing one image provides no information about others."

### Panel B: Protein Classification (Random Fails)

**Content:** Protein family tree showing how random splits place homologous proteins across train/test, creating memorization pathway.

**DALL-E Prompt:**
```
Create a scientific diagram showing random splits fail for proteins. Save as: 06-B-fig-random-splits-fail.svg

Tree structure:
- Phylogenetic/family tree with protein nodes
- Random coloring: blue (train) and orange (test) mixed within families
- Dashed lines showing high sequence identity (80%) between train and test
- Warning annotation: "80% identity between train/test"
- Memorization pathway highlighted: "Model memorizes similar sequences"
- Label: "Proteins: Related by evolution"
- X mark annotation: "Random splits create leakage"

Clean family tree diagram with warning highlights, white background. Professional homology leakage illustration.
```

**Caption for Panel B:**
"Random splits fail for evolutionarily related sequences. Proteins share evolutionary history, and random assignment places close homologs (>80% sequence identity) across train and test sets. The model can achieve high test accuracy by memorizing sequence patterns shared between related proteins rather than learning generalizable biological features. This homology leakage inflates apparent performance."

### Panel C: Variant Prediction (Multiple Failure Modes)

**Content:** Gene diagram with variants showing how random splits fail due to same gene in train/test, family members spanning splits, and population structure.

**DALL-E Prompt:**
```
Create a scientific diagram showing multiple failure modes for variant splits. Save as: 06-C-fig-random-splits-fail.svg

Multi-level diagram:

TOP: Gene diagram with multiple variant positions
- Same gene has variants in train (blue) and test (orange)
- Warning: "Same gene in train/test"

MIDDLE: Family pedigree
- Related individuals split across train/test
- Warning: "Family members share rare variants"

BOTTOM: Population structure (PCA-style clusters)
- Different ancestries unevenly split
- Warning: "Population structure confounds"

All levels marked with X for random split failure. Label: "Variants: Multiple dependencies"

Clean multi-level warning diagram, white background. Professional variant splitting failure illustration.
```

**Caption for Panel C:**
"Variant prediction faces multiple random split failure modes. Gene-level: random splits place different variants from the same gene in train and test, allowing memorization of gene-specific patterns. Family-level: related individuals sharing rare variants may span splits, enabling memorization of family-specific haplotypes. Population-level: ancestry structure correlates with variant frequencies and phenotypes, creating confounding that random splits do not address. Proper evaluation requires splits that account for all these dependencies."

### Combined Caption

**Full Figure Caption:**
"Why random data splits fail for genomic machine learning. (A) Image classification: samples are truly independent, so random assignment provides valid performance estimates. (B) Protein classification: evolutionary relationships create dependencies; random splits place homologs (>80% identity) across train/test, enabling memorization of shared sequences rather than learning generalizable features. (C) Variant prediction: multiple dependencies compound—same genes across splits, related individuals sharing rare variants, and population structure confounding features and labels. These dependencies require structured splitting strategies that explicitly account for sequence homology, family relatedness, and population structure."

---

## Figure 11.7: Homology-Aware Splitting

**File:** `figs/part_2/ch11/07-fig-homology-splitting.svg`
**Priority:** Essential
**Type:** Step-by-step workflow

### Content Description

Workflow showing proper homology-aware splitting:
1. All sequences input
2. Clustering (CD-HIT/MMseqs2 at threshold)
3. Cluster visualization showing grouped similar sequences
4. Split assignment with entire clusters to train/val/test
5. Validation check: no test sequence >X% identity to any training sequence

### DALL-E Prompt

```
Create a scientific workflow diagram for homology-aware data splitting. Save as: 07-fig-homology-splitting.svg

Step-by-step flow (top to bottom or left to right):

STEP 1: "Input Sequences"
- Multiple sequence icons scattered

STEP 2: "Cluster by Identity"
- CD-HIT/MMseqs2 tool icon
- Parameter: "e.g., 30% identity threshold"

STEP 3: "Cluster Visualization"
- Grouped sequences in colored clusters
- Lines connecting similar sequences within clusters

STEP 4: "Assign Entire Clusters"
- Clusters colored: blue (train), yellow (val), orange (test)
- Entire cluster goes to one split only

STEP 5: "Validate Separation"
- Check icon: "No test >30% identity to train"
- Checkmark for proper separation

Comparison table at bottom:
| Strategy | Threshold | Strictness | Use Case |
| Random | None | None | Never for homologous |
| 50% | CD-HIT | Moderate | Fold recognition |
| 30% | MMseqs2 | High | Function prediction |

Clean workflow diagram with numbered steps, white background. Professional homology splitting guide.
```

### Post-Processing Notes

- Add tool names and parameters at clustering step
- Include comparison table for different stringency levels
- Add checkmark/validation step prominently
- Use consistent color coding throughout

### Fallback Description

Create in diagramming software:
- Vertical or horizontal workflow with numbered steps
- Cluster visualization with colored groups
- Validation checkpoint with success criteria

### Caption

**Recommended Caption:**
"Homology-aware splitting prevents sequence similarity leakage. Step 1: Start with all sequences in the dataset. Step 2: Cluster sequences by similarity using tools like CD-HIT or MMseqs2 at an appropriate threshold (30% identity typical for diverse protein tasks). Step 3: Visualize clusters showing which sequences are related. Step 4: Assign entire clusters to single splits—no cluster is divided across train/validation/test. Step 5: Validate that no test sequence exceeds the identity threshold with any training sequence. The threshold determines evaluation stringency: 30% identity tests distant generalization; 50% tests moderate generalization; higher thresholds permit more similarity but provide weaker generalization evidence."

---

## Figure 11.8: Splitting Strategies Comparison

**File:** `figs/part_2/ch11/08-fig-splitting-strategies.svg`
**Priority:** High
**Type:** Matrix/comparison table

### Content Description

Matrix comparing splitting strategies against what they test:
- Rows: Random, individual-aware, family-aware, chromosome, gene/protein family, cohort/site, temporal, ancestry
- Columns: Sequence generalization, individual generalization, population robustness, temporal robustness, cross-site generalization
- Cells: checkmark, X, or tilde for partial

### DALL-E Prompt

```
Create a scientific comparison matrix for data splitting strategies. Save as: 08-fig-splitting-strategies.svg

Matrix layout:

ROWS (Splitting Strategies):
1. Random
2. Individual-aware
3. Family-aware
4. Chromosome holdout
5. Gene/protein family
6. Cohort/site holdout
7. Temporal split
8. Ancestry stratified

COLUMNS (What It Tests):
- Sequence Generalization
- Individual Generalization
- Population Robustness
- Temporal Robustness
- Cross-Site Transfer

CELLS:
- Green checkmark: Strategy tests this capability
- Red X: Strategy does not address this
- Yellow tilde: Partial/depends on implementation

Small schematic icons next to each row showing the splitting approach visually.

Side annotations:
- Performance drop expectations
- "Strategies are combinable"
- "Stricter splits = lower but more realistic scores"

Clean matrix diagram with color-coded cells, white background. Professional splitting strategy comparison.
```

### Post-Processing Notes

- Use clear icons (✓, ✗, ~) in cells
- Add small visual schematics for each strategy
- Include notes about combinability
- Color-code by evaluation strength

### Fallback Description

Create in spreadsheet or diagramming software:
- Table with strategies as rows, tests as columns
- Symbol coding for capability coverage
- Visual icons for each strategy type

### Caption

**Recommended Caption:**
"Splitting strategies test different aspects of generalization. Each strategy (rows) addresses specific dependencies (columns): random splits address none; individual-aware prevents sample-level leakage; family-aware accounts for relatedness; chromosome holdout tests cross-genome transfer; gene/protein family prevents homology leakage; cohort/site holdout tests deployment robustness; temporal splits simulate prospective use; ancestry stratification reveals population biases. No single strategy addresses all dependencies; rigorous evaluation combines multiple strategies. Stricter splits produce lower but more realistic performance estimates that better predict clinical deployment success."

---

## Figure 11.9: Foundation Model Evaluation Paradigms (Three-Panel)

**Files:**
- `figs/part_2/ch11/09-A-fig-fm-evaluation-paradigms.svg`
- `figs/part_2/ch11/09-B-fig-fm-evaluation-paradigms.svg`
- `figs/part_2/ch11/09-C-fig-fm-evaluation-paradigms.svg`

**Priority:** Enhancing
**Type:** Paradigm comparison

### Panel A: Zero-Shot Evaluation

**Content:** Frozen model with direct prediction. Shows that zero-shot tests alignment between pretraining and task. Example: ESM-1v log-likelihood scoring.

**DALL-E Prompt:**
```
Create a scientific diagram showing zero-shot foundation model evaluation. Save as: 09-A-fig-fm-evaluation-paradigms.svg

Diagram elements:
- Large "Foundation Model" box (frozen, grayed)
- Input: "Sequence" arrow entering
- Output: "Direct Prediction" arrow exiting
- No additional training components
- Label: "ZERO-SHOT"

Annotation box:
- "Tests: Pretraining-task alignment"
- "Example: ESM-1v log-likelihood"
- "Pro: No task data needed"
- "Con: Limited to aligned tasks"

Blue/gray color scheme for frozen components. Clean architecture diagram, white background. Professional zero-shot evaluation figure.
```

**Caption for Panel A:**
"Zero-shot evaluation uses frozen model outputs directly without task-specific training. The model produces predictions based solely on patterns learned during pretraining. This paradigm tests alignment between pretraining objectives and downstream tasks—success indicates that pretraining implicitly captured task-relevant features. Example: ESM-1v uses sequence log-likelihoods for variant effect prediction without seeing pathogenicity labels during training."

### Panel B: Linear Probing

**Content:** Frozen embeddings with trained linear classifier. Shows that probing tests linear accessibility of task-relevant features.

**DALL-E Prompt:**
```
Create a scientific diagram showing linear probing evaluation. Save as: 09-B-fig-fm-evaluation-paradigms.svg

Diagram elements:
- Large "Foundation Model" box (frozen, grayed)
- "Embeddings" intermediate output
- Small "Linear Classifier" box (trainable, blue/green)
- Final "Prediction" output
- Label: "LINEAR PROBING"

Annotation box:
- "Tests: Linear feature accessibility"
- "Isolates representation quality"
- "Pro: Low data requirement"
- "Con: May miss nonlinear patterns"

Frozen components in gray, trainable in colored. Clean architecture diagram, white background. Professional probing evaluation figure.
```

**Caption for Panel B:**
"Linear probing freezes foundation model embeddings and trains only a linear classifier on top. This paradigm isolates representation quality from adaptation capacity—if a simple linear model achieves strong performance, the pretrained representations encode task-relevant features in accessible form. Linear probing requires minimal labeled data and provides clean evidence about what the foundation model learned during pretraining."

### Panel C: Fine-Tuning

**Content:** Gradients through entire model showing full adaptation. Shows that fine-tuning tests total potential but conflates representation with adaptation quality.

**DALL-E Prompt:**
```
Create a scientific diagram showing fine-tuning evaluation. Save as: 09-C-fig-fm-evaluation-paradigms.svg

Diagram elements:
- Large "Foundation Model" box (trainable, colored)
- Gradient arrows flowing through entire model
- "Task Head" box (trainable, colored)
- Final "Prediction" output
- Label: "FINE-TUNING"

Annotation box:
- "Tests: Total model potential"
- "Conflates representation + adaptation"
- "Pro: Best absolute performance"
- "Con: High data requirement, overfitting risk"

All components colored to show trainability. Gradient flow arrows. Clean architecture diagram, white background. Professional fine-tuning evaluation figure.
```

**Caption for Panel C:**
"Fine-tuning updates all model parameters during task-specific training, testing total model potential. This paradigm achieves the highest absolute performance but conflates representation quality with adaptation capacity—strong fine-tuned performance may reflect good pretraining, good adaptation, or both. Fine-tuning requires substantial labeled data and carries overfitting risk, making it less diagnostic of foundation model quality than zero-shot or probing approaches."

### Combined Caption

**Full Figure Caption:**
"Foundation model evaluation paradigms test different capabilities. (A) Zero-shot: frozen model predictions test whether pretraining captured task-relevant patterns; requires no task data but limited to aligned tasks. (B) Linear probing: frozen embeddings with learned linear classifier test whether task features are linearly accessible in representations; requires minimal data and isolates representation quality. (C) Fine-tuning: full gradient updates test total potential but conflate representation and adaptation; achieves best performance but requires substantial data. The value of pretraining is best measured by the gap between few-shot and from-scratch performance—large gaps indicate that pretraining provides transferable features beyond what task data alone would support."

---

## Figure 11.10: Metric Selection Flowchart

**File:** `figs/part_2/ch11/10-fig-metric-selection.svg`
**Priority:** High
**Type:** Decision flowchart

### Content Description

Flowchart guiding metric selection based on:
- Binary vs. continuous outcomes
- Balanced vs. imbalanced classes
- Ranking vs. probability requirements
- Clinical decision needs

### DALL-E Prompt

```
Create a scientific flowchart for evaluation metric selection. Save as: 10-fig-metric-selection.svg

Decision tree structure:

ROOT: "What type of prediction?"

LEVEL 1: "Binary or Continuous?"
- Binary → next decision
- Continuous → "Correlation (Pearson/Spearman), MSE, MAE"

LEVEL 2 (Binary): "Class balance?"
- Balanced → "Accuracy, auROC"
- Imbalanced → next decision

LEVEL 3 (Imbalanced): "Ranking or Probability?"
- Ranking → "auPRC (NOT auROC alone)"
- Probability → "Calibration (Brier score, reliability diagram)"

LEVEL 4: "Clinical decision making?"
- Yes → "Net benefit, decision curve analysis"
- No → standard metrics

WARNING CALLOUTS:
- "auROC invariant to class imbalance!"
- "High correlation ≠ clinically meaningful"
- "Calibration essential for deployment"

Color-coded terminals by metric type. Clean flowchart with decision diamonds, white background. Professional metric selection guide.
```

### Post-Processing Notes

- Add warning callouts for common pitfalls
- Color-code metric recommendations by use case
- Include brief descriptions at terminal nodes
- Add examples for each metric type

### Fallback Description

Create in flowchart software:
- Decision tree with binary questions
- Terminal nodes with metric recommendations
- Warning annotations for common mistakes

### Caption

**Recommended Caption:**
"Metric selection depends on task characteristics and deployment requirements. Binary classification requires different metrics depending on class balance: auROC provides stable ranking assessment for balanced data, while auPRC is essential for imbalanced settings where auROC can mislead. Probability calibration matters for deployment: a model may rank correctly while producing systematically overconfident probabilities. Clinical decision-making requires metrics like net benefit that account for the costs of different error types. Continuous predictions use correlation and error metrics, but high correlation does not guarantee clinical utility—a model may track relative differences while failing to capture absolute effect sizes. Selecting appropriate metrics prevents optimizing for misleading targets."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 11.1 Benchmark Landscape | 1 | Essential | High (taxonomy) |
| 11.2 Leakage Pathways | 1 | High | Medium (flow diagram) |
| 11.3 Saturation | 2 | High | Medium (temporal plots) |
| 11.4 Proxy-Target Gap | 1 | Essential | Medium (conceptual) |
| 11.5 Cross-Population | 1 | High | Medium (bar chart) |
| 11.6 Random Splits Fail | 3 | Essential | Medium (comparison) |
| 11.7 Homology Splitting | 1 | Essential | Medium (workflow) |
| 11.8 Splitting Strategies | 1 | High | Medium (matrix) |
| 11.9 FM Evaluation | 3 | Enhancing | Medium (paradigm comparison) |
| 11.10 Metric Selection | 1 | High | Medium (flowchart) |

**Total files:** 15
**Recommended generation order:** 11.6A-C (random splits fail, foundational), 11.7 (homology splitting), 11.4 (proxy-target gap), 11.2 (leakage), 11.10 (metrics), 11.5 (cross-population), 11.8 (strategies matrix), 11.3A-B (saturation), 11.1 (landscape), 11.9A-C (FM paradigms)
# Figure Report: Chapter 12 - Confounding and Data Leakage

**Chapter:** Part 2, Chapter 12 - Confounding and Data Leakage
**Date:** 2026-01-07
**Figures:** 6 conceptual figures (10 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 12.1: Confounding DAG

**File:** `figs/part_2/ch12/01-fig-confounding-dag.svg`
**Priority:** Essential
**Type:** Causal diagram (DAG)

### Content Description

Directed acyclic graph (DAG) showing confounding structure with genomic example:
- Main DAG: Confounder (Ancestry) with arrows to Exposure (Genomic features) and Outcome (Disease status)
- Spurious path X ← C → Y highlighted
- Annotation boxes explaining how ancestry affects both
- Second DAG showing adjustment blocking spurious path
- Concrete example: Rare disease clinic → ClinVar submissions → ancestry proxy learned

### DALL-E Prompt

```
Create a scientific causal diagram (DAG) showing confounding in genomic AI. Save as: 01-fig-confounding-dag.svg

TWO-PANEL layout:

PANEL 1 "Confounding Structure":
- Circle node "C" at top labeled "Confounder (Ancestry)"
- Circle node "X" at bottom-left labeled "Features (Genotypes)"
- Circle node "Y" at bottom-right labeled "Outcome (Disease)"
- Arrow from C to X (ancestry affects genotype frequencies)
- Arrow from C to Y (ancestry affects disease via non-genetic paths)
- Optional arrow X to Y (true causal path, dashed)
- Spurious path C→X and C→Y highlighted in RED
- Annotation: "Model learns X-Y association via C, not biology"

PANEL 2 "After Adjustment":
- Same nodes but confounder C is boxed/conditioned
- Spurious paths blocked (grayed out)
- Only true X→Y path remains (if it exists)
- Annotation: "Conditioning on C blocks spurious association"

CONCRETE EXAMPLE box:
"Rare disease clinic (European) → ClinVar submissions → Model learns ancestry as pathogenicity proxy"

Clean causal DAG style with circles for variables, arrows for causal effects. White background. Professional epidemiology/ML confounding diagram.
```

### Post-Processing Notes

- Use standard DAG notation (circles for variables, arrows for causal effects)
- Highlight spurious paths in red/warning color
- Show conditioning with box around conditioned variable
- Include concrete genomic example in annotation

### Fallback Description

Create in DAGitty or diagramming software:
- Standard causal DAG with three nodes
- Two-panel showing before/after adjustment
- Color-coded spurious vs. causal paths

### Caption

**Recommended Caption:**
"Confounding structure in genomic prediction. (Left) Ancestry acts as a confounder, affecting both genomic features (through population-specific allele frequencies) and disease outcomes (through environmental, socioeconomic, and healthcare pathways). The spurious path (red) creates association between features and outcomes that models exploit as shortcuts. (Right) Conditioning on ancestry blocks the spurious path, isolating any genuine feature-outcome relationship. Concrete example: a rare disease clinic serving primarily European patients contributes most pathogenic variants to ClinVar, creating an ancestry-pathogenicity correlation that models learn instead of biological mechanisms. The central challenge: shortcuts appear to work until deployment shifts the confounder-outcome relationship."

---

## Figure 12.2: Population Structure as Shortcut (Four-Panel)

**Files:**
- `figs/part_2/ch12/02-A-fig-population-structure-shortcut.svg`
- `figs/part_2/ch12/02-B-fig-population-structure-shortcut.svg`
- `figs/part_2/ch12/02-C-fig-population-structure-shortcut.svg`
- `figs/part_2/ch12/02-D-fig-population-structure-shortcut.svg`

**Priority:** Essential
**Type:** Multi-panel evidence figure

### Panel A: PCA of Genomic Data

**Content:** PC1 vs PC2 plot showing clear ancestry clustering. Points colored by ancestry group demonstrating that genetic variation is structured by population.

**DALL-E Prompt:**
```
Create a scientific PCA plot showing genomic population structure. Save as: 02-A-fig-population-structure-shortcut.svg

Scatter plot elements:
- X-axis: "PC1" (principal component 1)
- Y-axis: "PC2" (principal component 2)
- Clear clusters by ancestry:
  - European cluster (blue, largest)
  - African cluster (orange)
  - East Asian cluster (green)
  - South Asian cluster (purple)
  - Admixed points between clusters (gray)
- Cluster labels or legend
- Title: "Genetic Variation is Structured by Ancestry"

Clean scientific PCA plot with distinct clusters, white background. Professional population genetics visualization.
```

**Caption for Panel A:**
"Population structure in genomic data. Principal component analysis of genome-wide variants reveals clear clustering by ancestry. PC1 and PC2 capture continental-scale genetic variation reflecting demographic history. This structure means that ancestry information is implicitly encoded in genotype data even when not explicitly provided—models can learn to predict ancestry from genetic features."

### Panel B: Ancestry in K-mer Frequencies

**Content:** Heatmap showing that even local sequence composition (k-mer frequencies) differs by population, demonstrating that ancestry signal permeates sequence data.

**DALL-E Prompt:**
```
Create a scientific heatmap showing k-mer frequency differences by ancestry. Save as: 02-B-fig-population-structure-shortcut.svg

Heatmap elements:
- Rows: Different k-mers (e.g., 6-mers, showing ~20 representative)
- Columns: Ancestry groups (European, African, East Asian, South Asian)
- Color intensity: Relative k-mer frequency (blue-white-red diverging)
- Clear differences visible between populations
- Title: "Even Local Sequence Composition Differs"
- Annotation: "Foundation models see ancestry in sequence"

Clean bioinformatics heatmap with population columns, white background. Professional k-mer analysis figure.
```

**Caption for Panel B:**
"Ancestry encoded in local sequence composition. Heatmap of k-mer frequencies across ancestry groups reveals systematic differences even in short sequence patterns. Foundation models processing raw sequences have access to this ancestry signal regardless of whether ancestry labels are provided. This enables models to learn ancestry as a feature—beneficial for population genetics applications but problematic when ancestry confounds the target prediction."

### Panel C: The Shortcut Pathway

**Content:** Flow diagram showing how ancestry creates a shortcut: Ancestry → Sequencing site → Labels (one path) and Ancestry → Allele frequencies → Features (another path). Model learns via ancestry rather than biology.

**DALL-E Prompt:**
```
Create a scientific flow diagram showing the ancestry shortcut pathway. Save as: 02-C-fig-population-structure-shortcut.svg

Flow diagram:
CENTRAL NODE: "Ancestry"

PATH 1 (to labels):
Ancestry → "Healthcare access" → "Sequencing site" → "Label quality/presence"
(Red arrow labeled "Non-biological pathway")

PATH 2 (to features):
Ancestry → "LD patterns" → "Allele frequencies" → "Genetic features"
(Blue arrow labeled "Feature pathway")

BOTTOM: "Model" box receiving both pathways
Annotation: "Model learns ancestry as shortcut to labels"

WARNING: "Shortcut works in training, fails at deployment"

Clean flow diagram with pathway arrows, white background. Professional shortcut learning illustration.
```

**Caption for Panel C:**
"Ancestry creates shortcut pathways exploitable by models. Ancestry affects both labels (through healthcare access, sequencing site, and annotation quality) and features (through allele frequencies and linkage disequilibrium patterns). Models can achieve high training accuracy by learning the ancestry-label correlation rather than biological mechanisms. This shortcut works when training and test distributions share the same ancestry-label relationship but fails when that relationship changes—as when models trained on European-majority data are deployed on other populations."

### Panel D: Cross-Population Performance Degradation

**Content:** Bar chart showing 40-75% PGS reduction for non-European populations compared to European reference. Demonstrates that shortcuts fail when the relationship changes.

**DALL-E Prompt:**
```
Create a scientific bar chart showing PGS performance degradation. Save as: 02-D-fig-population-structure-shortcut.svg

Bar chart elements:
- X-axis: Ancestry groups (European [reference], African, East Asian, South Asian, Admixed)
- Y-axis: "Relative PGS Performance" (0-100%)
- European bar: 100% (reference, green)
- African bar: ~25-40% (major drop, red)
- East Asian bar: ~70-80% (moderate drop, yellow)
- South Asian bar: ~60-70% (moderate drop, yellow)
- Admixed bar: ~50-65% (significant drop, orange)

Annotations:
- "40-75% reduction for African ancestry"
- Arrow pointing to gap: "Shortcuts fail when relationship changes"
- Error bars on all estimates

Clean bar chart with degradation pattern, white background. Professional PGS portability figure.
```

**Caption for Panel D:**
"Shortcuts fail when ancestry-label relationships change. Polygenic risk scores (PGS) derived from European-ancestry GWAS show 40-75% reductions in prediction accuracy for African-ancestry individuals. The shortcut through ancestry-correlated features works for the training population but fails for populations where ancestry-phenotype relationships differ. This pattern—high training performance followed by deployment failure—is the signature of confounded prediction."

### Combined Caption

**Full Figure Caption:**
"Population structure creates exploitable shortcuts in genomic prediction. (A) PCA reveals clear ancestry clustering in genetic data. (B) Even local k-mer frequencies differ by ancestry, meaning foundation models have access to ancestry signal from raw sequences. (C) Ancestry creates dual pathways to both features (through allele frequencies) and labels (through healthcare access and annotation practices), enabling models to learn ancestry as a proxy for the target outcome. (D) The consequence: polygenic scores show 40-75% performance reduction when applied to non-European populations because ancestry-based shortcuts do not generalize. Higher model capacity does not solve confounding—it makes it worse by enabling detection of ever more subtle ancestry-linked features."

---

## Figure 12.3: Batch Effects (Three-Panel)

**Files:**
- `figs/part_2/ch12/03-A-fig-batch-effects.svg`
- `figs/part_2/ch12/03-B-fig-batch-effects.svg`
- `figs/part_2/ch12/03-C-fig-batch-effects.svg`

**Priority:** High
**Type:** Multi-panel batch effect evidence

### Panel A: Batch Structure in Embeddings

**Content:** UMAP visualization showing samples clustered by sequencing center rather than by phenotype. Demonstrates that batch effects dominate learned representations.

**DALL-E Prompt:**
```
Create a scientific UMAP plot showing batch structure dominates embeddings. Save as: 03-A-fig-batch-effects.svg

UMAP scatter plot:
- Clear clusters by sequencing center (not phenotype)
- Center A cluster (blue)
- Center B cluster (orange)
- Center C cluster (green)
- Within each cluster, cases (+) and controls (o) are mixed
- Title: "Embeddings Cluster by Batch, Not Phenotype"
- Annotation: "Model learns to distinguish centers, not disease"

Legend showing:
- Shape: Case vs Control
- Color: Sequencing Center

Clean UMAP with batch-dominated clustering, white background. Professional batch effect visualization.
```

**Caption for Panel A:**
"Embeddings cluster by batch rather than phenotype. UMAP projection of foundation model embeddings shows clear separation by sequencing center (colors) while cases (+) and controls (o) are mixed within each cluster. The model has learned batch-specific features rather than disease biology, achieving high apparent performance by distinguishing technical artifacts."

### Panel B: Coverage Patterns by Batch

**Content:** Genome browser-style tracks showing systematic coverage differences between sequencing centers. Different centers show different coverage profiles at the same genomic region.

**DALL-E Prompt:**
```
Create a scientific genome browser view showing coverage batch effects. Save as: 03-B-fig-batch-effects.svg

Browser-style layout:
- X-axis: Genomic position (e.g., chr1:1,000,000-1,100,000)
- Three horizontal tracks (coverage histograms):
  - "Center A": Specific coverage pattern (high at some regions)
  - "Center B": Different pattern (coverage dips at different positions)
  - "Center C": Yet another pattern
- Vertical dashed lines highlighting systematic differences
- Title: "Coverage Varies Systematically by Center"
- Annotation: "Same biology, different technical readout"

Clean genome browser style with coverage tracks, white background. Professional sequencing batch effect figure.
```

**Caption for Panel B:**
"Coverage patterns vary systematically by sequencing center. The same genomic region shows different coverage profiles depending on which center performed sequencing. These differences reflect instrument characteristics, capture kit biases, and processing pipelines rather than biological variation. Models can learn to recognize these center-specific signatures and use them as predictive features."

### Panel C: Batch Predicts Phenotype

**Content:** Contingency table showing case/control imbalance across batches. If batch is confounded with phenotype, models can exploit this.

**DALL-E Prompt:**
```
Create a scientific contingency table showing batch-phenotype confounding. Save as: 03-C-fig-batch-effects.svg

2x3 contingency table:
             Center A    Center B    Center C
Cases           800        100         100
Controls        100        800         100

Color coding:
- Cells with high counts: darker
- Shows clear imbalance: cases at Center A, controls at Center B

Annotation:
- Chi-square = highly significant
- "Batch perfectly predicts phenotype!"
- Warning: "Model predicting disease may actually predict sequencing center"

Clean contingency table with imbalance highlighted, white background. Professional confounding evidence figure.
```

**Caption for Panel C:**
"Batch-phenotype confounding enables trivial prediction. When cases and controls are processed at different centers, predicting batch is equivalent to predicting phenotype. A model achieving 90% disease classification accuracy may simply be recognizing which center processed the sample. This confounding is invisible in aggregate metrics but produces catastrophic failure when deployed on new data where batch-phenotype associations differ."

### Combined Caption

**Full Figure Caption:**
"Technical batch effects masquerade as biological signal. (A) Model embeddings cluster by sequencing center rather than by case/control status, revealing that learned representations capture technical rather than biological variation. (B) Coverage patterns at the same genomic region differ systematically by center, providing features models can exploit. (C) Batch-phenotype confounding occurs when cases and controls are imbalanced across centers—predicting batch becomes equivalent to predicting disease. Together, these panels illustrate why models can achieve high apparent performance while learning nothing about biology. Detection requires visualizing embeddings, examining coverage patterns, and testing whether batch identity predicts the outcome."

---

## Figure 12.4: Label Circularity

**File:** `figs/part_2/ch12/04-fig-label-circularity.svg`
**Priority:** High
**Type:** Circular flow diagram

### Content Description

Circular diagram showing how computational predictions influence labels that become training data for new predictors:
1. Clinical lab submits to ClinVar using CADD/REVEL as evidence
2. ClinVar aggregates (computational evidence influences labels)
3. New model trains on ClinVar (learns to replicate patterns)
4. New model used by labs (influences next submissions)
5. Return to step 1

Side panel: Breaking the cycle through prospective, temporal, or independent functional validation.

### DALL-E Prompt

```
Create a scientific circular flow diagram showing label circularity. Save as: 04-fig-label-circularity.svg

CIRCULAR FLOW (clockwise):

STEP 1: "Clinical Lab" box
- Arrow to Step 2
- Annotation: "Submits to ClinVar using CADD/REVEL as evidence"

STEP 2: "ClinVar Database" box
- Arrow to Step 3
- Annotation: "Aggregates submissions; computational evidence influences labels"

STEP 3: "New Predictor" box (highlighted)
- Arrow to Step 4
- Annotation: "Trains on ClinVar; learns to replicate existing patterns"

STEP 4: "Deployment" box
- Arrow back to Step 1
- Annotation: "Labs use new predictor; influences next submissions"

CENTER: Warning symbol with "CIRCULARITY"

SIDE PANEL "Breaking the Cycle":
- "Prospective validation (new variants)"
- "Temporal splits (train on old, test on new)"
- "Independent functional assays"

Circular arrow showing endless loop. Red warning highlights. Clean flow diagram, white background. Professional label circularity illustration.
```

### Post-Processing Notes

- Use clear circular layout showing feedback loop
- Highlight the problematic circularity in red/warning
- Include side panel with solutions
- Add annotations explaining each step

### Fallback Description

Create in diagramming software:
- Circular flow with 4-5 boxes
- Arrows showing cyclic information flow
- Warning annotation in center
- Solution panel on side

### Caption

**Recommended Caption:**
"Label circularity inflates apparent validation. Clinical laboratories submit variants to ClinVar using computational predictions (CADD, REVEL) as supporting evidence. ClinVar aggregates these submissions, creating labels that reflect historical computational predictions. New models trained on ClinVar learn to replicate these patterns, achieving high apparent accuracy through agreement with previous predictors rather than independent biological insight. When these new models are deployed, they influence the next generation of submissions, perpetuating the cycle. Breaking circularity requires prospective validation on newly discovered variants, temporal splits that train on historical data and test on recent annotations, or independent functional assay validation that bypasses computational predictions entirely."

---

## Figure 12.5: Confounding Detection Diagnostics

**File:** `figs/part_2/ch12/05-fig-confounding-detection.svg`
**Priority:** High
**Type:** Diagnostic checklist with visualizations

### Content Description

Comprehensive diagnostic checklist showing five detection approaches:
1. Confounder-only baseline: Compare full model vs. ancestry PCs only vs. batch only
2. Subgroup stratification: Performance by ancestry groups
3. Prediction-confounder association: Residual associations after controlling for label
4. Split sensitivity: Performance across different splitting strategies
5. Negative controls: Accuracy on outcomes unrelated to genetics

### DALL-E Prompt

```
Create a scientific diagnostic panel for confounding detection. Save as: 05-fig-confounding-detection.svg

FIVE-PANEL diagnostic layout:

PANEL 1 "Confounder-Only Baseline":
- Bar chart: "Full Model" (0.85), "Ancestry PCs Only" (0.80), "Batch Only" (0.75)
- Warning if simple baseline approaches full model
- Annotation: "If PCs alone predict well → confounding"

PANEL 2 "Stratified Performance":
- Multiple small bar charts by ancestry group
- European: 0.90, African: 0.60, Asian: 0.70
- Annotation: "Heterogeneity across groups suggests confounding"

PANEL 3 "Residual Association":
- Scatter plot: Prediction vs PC1, after controlling for true label
- Should show no association if model is not using ancestry
- Annotation: "Residual correlation with ancestry = confounding"

PANEL 4 "Split Sensitivity":
- Table: Random (0.92), Locus-level (0.78), Temporal (0.75)
- Large drops indicate leakage/memorization
- Annotation: "Performance should not depend on split type"

PANEL 5 "Negative Controls":
- Bar chart: "Genetics-related" (0.85), "Insurance type" (0.65), "Admin code" (0.60)
- Should be at chance for non-genetic outcomes
- Annotation: "Predicting admin outcomes = learned confounders"

Grid layout with five diagnostic panels. Clean scientific diagnostic figure, white background. Professional confounding detection guide.
```

### Post-Processing Notes

- Use grid layout for five panels
- Include interpretation guidance for each diagnostic
- Add warning indicators for concerning patterns
- Color-code by diagnostic result (green=OK, red=warning)

### Fallback Description

Create as multi-panel figure in plotting software:
- Grid of 5 small visualizations
- Each with specific diagnostic and interpretation
- Warning annotations for concerning patterns

### Caption

**Recommended Caption:**
"Diagnostic toolkit for detecting confounding. (1) Confounder-only baselines: if ancestry PCs alone approach full model performance, ancestry confounding is likely. (2) Stratified analysis: large performance gaps between ancestry groups suggest the model exploits group-specific shortcuts. (3) Residual association: predictions should not correlate with ancestry after controlling for the true label; residual correlation indicates ancestry encoding beyond what the task requires. (4) Split sensitivity: performance should not depend dramatically on splitting strategy; large drops under locus-level or temporal splits indicate memorization. (5) Negative controls: models should not predict outcomes unrelated to genetics (insurance type, administrative codes); above-chance prediction indicates learned confounders. Apply all diagnostics; confounding may manifest in only some."

---

## Figure 12.6: Mitigation Strategies Comparison

**File:** `figs/part_2/ch12/06-fig-mitigation-strategies.svg`
**Priority:** Enhancing
**Type:** Strategy comparison table/diagram

### Content Description

Comparison of mitigation strategies with their characteristics:
- Study design (matching): Before collection, reduces sample size
- Covariate adjustment: During training, may remove real signal
- Domain adaptation: Complex, requires implementation
- Robust optimization (Group DRO): Requires group labels
- Benchmark design: Stricter splits, harder scores

### DALL-E Prompt

```
Create a scientific comparison table for confounding mitigation strategies. Save as: 06-fig-mitigation-strategies.svg

Strategy comparison matrix:

COLUMNS:
- Strategy Name
- When Applied
- Requirements
- Main Trade-off
- Best For

ROWS:
1. Study Design/Matching | Before collection | Known confounders | Reduced sample size | Known major confounders
2. Covariate Adjustment | During training | Measured confounders | May remove real signal | Ancestry, batch correction
3. Residualization | Preprocessing | Linear confounding | Information loss | Strong linear effects
4. Adversarial Invariance | Training | Known groups | Reduced accuracy | Unknown variation
5. Group DRO | Training | Group labels | Worse average | Fairness-critical
6. Multi-site Training | Data collection | Multi-site access | Logistics | Institution effects
7. Temporal Splits | Evaluation | Timestamps | Smaller test set | Prospective deployment

Visual elements:
- Color coding by when applied (blue=design, green=training, orange=evaluation)
- Icons for each strategy type
- Annotation: "Approaches are complementary; use multiple"

Clean comparison table with organized columns, white background. Professional mitigation strategy guide.
```

### Post-Processing Notes

- Use color coding by intervention stage
- Add icons for visual distinction
- Include key annotation about combining strategies
- Format as clean comparison table

### Fallback Description

Create as formatted table:
- Strategy rows with characteristic columns
- Color coding by stage of intervention
- Notes on complementarity

### Caption

**Recommended Caption:**
"Mitigation strategies address confounding at different stages. Study design approaches (matching, balanced sampling) prevent confounding before data collection but reduce sample size. Covariate adjustment during training explicitly models known confounders but may inadvertently remove genuine biological signal. Residualization removes confounded variance in preprocessing but assumes linear relationships. Adversarial invariance learning trains representations that do not encode confounders but requires knowing which groups to enforce invariance over. Group DRO optimizes for worst-group performance at the cost of average performance. Multi-site training diversifies data sources. Temporal splits evaluate prospective performance. No single strategy eliminates all confounding; effective practice combines multiple approaches targeting different confounding sources."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 12.1 Confounding DAG | 1 | Essential | Medium (causal diagram) |
| 12.2 Population Shortcut | 4 | Essential | Medium-High (multi-panel) |
| 12.3 Batch Effects | 3 | High | Medium (multi-panel) |
| 12.4 Label Circularity | 1 | High | Medium (circular flow) |
| 12.5 Detection Diagnostics | 1 | High | High (multi-diagnostic) |
| 12.6 Mitigation Strategies | 1 | Enhancing | Medium (comparison table) |

**Total files:** 11
**Recommended generation order:** 12.1 (DAG, foundational), 12.2A-D (population shortcut), 12.4 (circularity), 12.3A-C (batch effects), 12.5 (detection), 12.6 (mitigation)
# Figure Report: Chapter 13 - Foundation Model Principles

**Chapter:** Part 3, Chapter 13 - Foundation Model Principles
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (8 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 13.1: Paradigm Shift (Two-Panel)

**Files:**
- `figs/part_3/ch13/01-A-fig-paradigm-shift.svg`
- `figs/part_3/ch13/01-B-fig-paradigm-shift.svg`

**Priority:** Essential
**Type:** Conceptual comparison

### Panel A: Task-Specific Paradigm

**Content:** Show the old paradigm with multiple independent models, each trained from scratch for a specific task (splice prediction, TF binding, expression). Each has its own training data and cannot share knowledge.

**DALL-E Prompt:**
```
Create a scientific diagram showing task-specific model training paradigm. Save as: 01-A-fig-paradigm-shift.svg

Three separate vertical pipelines side-by-side:

PIPELINE 1:
- "Splice Data" → "Train Model A" → "Splice Predictor"

PIPELINE 2:
- "TF Binding Data" → "Train Model B" → "Binding Predictor"

PIPELINE 3:
- "Expression Data" → "Train Model C" → "Expression Predictor"

Each pipeline completely separate (no connections between them)
Label: "Task-Specific Paradigm"
Annotations:
- "No knowledge sharing"
- "Train from scratch each time"
- "Narrow capabilities"

Red X marks between pipelines showing isolation. Clean workflow diagram, white background. Professional ML paradigm illustration.
```

**Caption for Panel A:**
"Task-specific paradigm: isolated models for isolated tasks. Each application (splice prediction, transcription factor binding, expression) requires training a separate model from scratch on task-specific data. Knowledge about sequence patterns learned for one task cannot transfer to others, limiting efficiency and requiring substantial labeled data for each new application."

### Panel B: Foundation Model Paradigm

**Content:** Show the new paradigm with a single foundation model pretrained on diverse unlabeled data, then adapted with small task-specific heads for multiple downstream tasks. All share the same base representations.

**DALL-E Prompt:**
```
Create a scientific diagram showing foundation model paradigm. Save as: 01-B-fig-paradigm-shift.svg

Single unified architecture:

TOP: Large "Foundation Model" box trained on "Diverse Unlabeled Sequences"
- Label: "Pretrain once"
- Billions of parameters

BOTTOM: Three small task heads branching from foundation model:
- "Splice Adapter" → "Splice Prediction"
- "Binding Adapter" → "TF Binding"
- "Expression Adapter" → "Expression Prediction"

Connections showing shared backbone with task-specific adaptations
Label: "Foundation Model Paradigm"
Annotations:
- "Knowledge shared across tasks"
- "Pretrain once, adapt many times"
- "Emergent capabilities"

Green checkmarks showing connections. Clean workflow diagram, white background. Professional FM paradigm illustration.
```

**Caption for Panel B:**
"Foundation model paradigm: shared representations, efficient adaptation. A single foundation model pretrained on diverse unlabeled sequences captures general biological knowledge. Small task-specific adapters leverage these shared representations for diverse downstream tasks with minimal labeled data. Knowledge transfers across applications through the common backbone."

### Combined Caption

**Full Figure Caption:**
"The paradigm shift from task-specific to foundation models. (A) The task-specific paradigm trains separate models from scratch for each application. Knowledge about sequence patterns cannot transfer between tasks, requiring substantial labeled data for each new application. (B) The foundation model paradigm pretrains a single large model on diverse unlabeled sequences, capturing general biological knowledge in reusable representations. Small task-specific adapters enable efficient transfer to diverse downstream tasks. This paradigm shift mirrors developments in natural language processing, where pretrained language models revolutionized the efficiency and capability of text-based AI systems."

---

## Figure 13.2: Scaling Laws (Three-Panel)

**Files:**
- `figs/part_3/ch13/02-A-fig-scaling-laws.svg`
- `figs/part_3/ch13/02-B-fig-scaling-laws.svg`
- `figs/part_3/ch13/02-C-fig-scaling-laws.svg`

**Priority:** Essential
**Type:** Log-log scaling plots

### Panel A: Loss vs. Parameters

**Content:** Log-log plot showing pretraining loss decreasing as a power law of model parameters. Points for different model sizes (8M, 35M, 150M, 650M, 3B, 15B) following a clean trend line.

**DALL-E Prompt:**
```
Create a scientific log-log plot showing scaling of loss with parameters. Save as: 02-A-fig-scaling-laws.svg

Plot elements:
- X-axis: "Parameters (log scale)" ranging 10M to 100B
- Y-axis: "Pretraining Loss (log scale)" ranging 1.0 to 4.0
- Data points for model sizes: 8M, 35M, 150M, 650M, 3B, 15B
- Clean power-law trend line through points
- Equation annotation: "L ∝ N^(-α)"
- Title: "Loss vs. Model Size"

Labels for each point with model variant names (e.g., ESM-2 8M, ESM-2 3B)
Clean log-log scientific plot with grid, white background. Professional scaling law figure.
```

**Caption for Panel A:**
"Pretraining loss scales as a power law with model parameters. Each point represents a model trained with identical data and compute per parameter; larger models achieve lower loss following L ∝ N^(-α). This predictable relationship enables extrapolating performance gains from scaling before committing resources."

### Panel B: Downstream Performance vs. Parameters

**Content:** Log-log plot showing downstream task accuracy increasing with model size across multiple tasks (contact prediction, secondary structure, variant effect). Each task shows the same scaling trend.

**DALL-E Prompt:**
```
Create a scientific log-log plot showing downstream task scaling. Save as: 02-B-fig-scaling-laws.svg

Plot elements:
- X-axis: "Parameters (log scale)" ranging 10M to 100B
- Y-axis: "Downstream Accuracy" (linear, 0.5 to 1.0)
- Multiple lines for different tasks:
  - Blue: "Contact Prediction"
  - Orange: "Secondary Structure"
  - Green: "Variant Effect"
- All lines show similar upward scaling trend
- Title: "Downstream Performance vs. Model Size"

Legend showing task colors. Clean scientific plot with grid, white background. Professional multi-task scaling figure.
```

**Caption for Panel B:**
"Downstream task performance scales with model size across diverse tasks. Contact prediction, secondary structure prediction, and variant effect scoring all improve with larger pretrained models, despite these tasks never appearing in pretraining. The consistent scaling across tasks demonstrates that larger models capture more transferable biological knowledge."

### Panel C: Compute-Optimal Scaling

**Content:** Iso-loss contours showing optimal trade-off between model size and training tokens for fixed compute budget. Diagonal ridge shows compute-optimal frontier.

**DALL-E Prompt:**
```
Create a scientific contour plot showing compute-optimal scaling. Save as: 02-C-fig-scaling-laws.svg

Contour plot:
- X-axis: "Training Tokens (log scale)"
- Y-axis: "Model Parameters (log scale)"
- Contour lines showing iso-loss regions (same loss achieved)
- Color gradient: red (high loss) to blue (low loss)
- Diagonal ridge line showing compute-optimal frontier
- Arrow annotation: "Compute-optimal scaling"
- Multiple diagonal lines showing fixed compute budgets
- Title: "Optimal Allocation of Compute"

Annotations explaining that moving along ridge maximizes performance for fixed compute. Clean contour plot, white background. Professional compute-optimal scaling figure.
```

**Caption for Panel C:**
"Compute-optimal scaling balances model size and training data. Iso-loss contours show that the same performance can be achieved with different combinations of parameters and training tokens. The diagonal ridge marks the compute-optimal frontier: for a fixed compute budget, moving along this ridge maximizes performance. The Chinchilla scaling law suggests that model size and training tokens should scale proportionally."

### Combined Caption

**Full Figure Caption:**
"Scaling laws for genomic foundation models. (A) Pretraining loss decreases predictably with model parameters following a power law, enabling informed decisions about resource allocation. (B) Downstream task performance scales consistently across diverse tasks including contact prediction, secondary structure, and variant effects, demonstrating that larger models capture more transferable biological knowledge. (C) Compute-optimal scaling reveals the trade-off between model size and training data: for fixed compute budget, optimal performance requires balancing parameter count with training tokens. These scaling relationships, first established in natural language processing, extend to biological sequence models and guide foundation model development."

---

## Figure 13.3: Model Taxonomy

**File:** `figs/part_3/ch13/03-fig-model-taxonomy.svg`
**Priority:** Essential
**Type:** Taxonomy/classification diagram

### Content Description

Four-quadrant taxonomy organizing genomic foundation models by:
- Modality (DNA, Protein, RNA, Multi-modal)
- Architecture (Encoder, Decoder, Hybrid)

Place key models in their appropriate positions with annotations for key characteristics.

### DALL-E Prompt

```
Create a scientific taxonomy diagram for genomic foundation models. Save as: 03-fig-model-taxonomy.svg

Four-family organization:

QUADRANT 1 "DNA Language Models":
- Models: DNABERT, Nucleotide Transformer, HyenaDNA, Caduceus, Evo
- Key: Long context, single-nucleotide resolution
- Color: Blue (#1f77b4)

QUADRANT 2 "Protein Language Models":
- Models: ESM, ESM-2, ProtTrans, ProGen
- Key: Evolutionary knowledge, structure-aware
- Color: Green (#2ca02c)

QUADRANT 3 "Regulatory Sequence Models":
- Models: Enformer, Borzoi, Basenji
- Key: Multi-task, expression prediction
- Color: Orange (#d62728)

QUADRANT 4 "Multi-Modal / Emerging":
- Models: AlphaFold2, AlphaMissense, RoseTTAFold
- Key: Structure + sequence integration
- Color: Purple (#9467bd)

Center annotation: "Foundation Models for Genomics"
Arrows showing relationships between families
Icons for each model type

Clean taxonomy diagram with four colored regions, white background. Professional model classification figure.
```

### Post-Processing Notes

- Add model names within each quadrant
- Include key characteristics for each family
- Show cross-family connections (e.g., ESM → ESMFold)
- Add legend for architecture types

### Fallback Description

Create in diagramming software:
- 2×2 grid or four-quadrant layout
- Model names as labeled boxes
- Color coding by family
- Connection lines between related models

### Caption

**Recommended Caption:**
"Taxonomy of genomic foundation models organized by modality and approach. DNA language models (blue) process nucleotide sequences with emphasis on long context and single-nucleotide resolution. Protein language models (green) encode evolutionary knowledge from protein sequences with increasing integration of structural information. Regulatory sequence models (orange) combine sequence processing with multi-task prediction of chromatin and expression tracks. Multi-modal and emerging models (purple) integrate across modalities, combining sequence with structure (AlphaFold2) or leveraging multiple information sources simultaneously. Arrows indicate connections between families where models build on each other's capabilities."

---

## Figure 13.4: Design Dimensions

**File:** `figs/part_3/ch13/04-fig-design-dimensions.svg`
**Priority:** High
**Type:** Multi-axis design space

### Content Description

Spider/radar chart or multi-axis comparison showing key design dimensions for foundation models:
- Context length
- Parameter count
- Training compute
- Tokenization strategy
- Architecture type
- Pretraining objective

Position representative models (ESM-2, Enformer, HyenaDNA, Evo) showing their different trade-offs.

### DALL-E Prompt

```
Create a scientific radar chart comparing foundation model design dimensions. Save as: 04-fig-design-dimensions.svg

Radar chart with 6 axes:
1. Context Length (1kb → 1Mb)
2. Parameters (10M → 100B)
3. Training Compute (low → high)
4. Architecture (Encoder → Decoder)
5. Tokenization (K-mer → Single-nucleotide)
6. Objective (MLM → Autoregressive)

Multiple overlaid polygons for different models:
- ESM-2: High params, encoder, medium context
- Enformer: High context, hybrid, multi-task
- HyenaDNA: Highest context, SSM, single-nucleotide
- Evo: High all dimensions, decoder

Legend showing model colors. Each polygon connects model's position on each axis.

Clean radar chart with labeled axes, white background. Professional model comparison figure.
```

### Post-Processing Notes

- Use distinct colors/line styles for each model
- Add legend identifying models
- Annotate key trade-offs
- Include brief description of each axis

### Fallback Description

Create as parallel coordinates plot or multi-bar comparison:
- Multiple axes showing design dimensions
- Lines connecting each model's positions
- Color coding for model identification

### Caption

**Recommended Caption:**
"Design dimensions for genomic foundation models. Radar chart positions representative models across six key dimensions: context length (how much sequence the model processes), parameter count (model capacity), training compute (resources required), architecture type (encoder vs. decoder), tokenization strategy (k-mer vs. single-nucleotide), and pretraining objective (masked vs. autoregressive). Different models make different trade-offs: ESM-2 emphasizes parameter scale within protein-length contexts; Enformer balances long context with multi-task supervision; HyenaDNA pushes context length to megabases using sub-quadratic architectures; Evo combines massive scale with autoregressive generation. These trade-offs determine which applications each model best serves."

---

## Figure 13.5: Build vs. Use Decision

**File:** `figs/part_3/ch13/05-fig-build-vs-use.svg`
**Priority:** High
**Type:** Decision flowchart with cost-benefit

### Content Description

Decision flowchart guiding practitioners through:
1. Use existing model with frozen embeddings (cheapest, fastest)
2. Adapt existing model with LoRA/fine-tuning (moderate cost)
3. Build custom foundation model (expensive, rarely necessary)

Include cost/time annotations and expected performance trade-offs.

### DALL-E Prompt

```
Create a scientific decision flowchart for build vs. use foundation models. Save as: 05-fig-build-vs-use.svg

Flowchart structure:

ENTRY: "New genomic prediction task"

DECISION 1: "Does suitable pretrained model exist?"
- Yes → "Task alignment?"
- No → "BUILD: Custom pretraining"

DECISION 2: "How well does task align with pretraining?"
- High alignment → "USE: Frozen embeddings"
- Moderate → "ADAPT: LoRA/fine-tuning"
- Low → "BUILD: Domain-specific pretraining"

TERMINAL NODES with cost-benefit:

USE (Green):
- Cost: Hours / $10
- Performance: 70-90% of fine-tuned
- Annotation: "Most applications land here"

ADAPT (Yellow):
- Cost: Days / $100-1000
- Performance: 95% of full fine-tuning
- Annotation: "Good balance for most tasks"

BUILD (Red):
- Cost: Months / $100K+
- Performance: Potentially best for domain
- Annotation: "Rare but sometimes necessary"

Color-coded paths and terminals. Clean decision flowchart, white background. Professional practitioner guide.
```

### Post-Processing Notes

- Add clear cost/time annotations at each terminal
- Color-code by recommendation strength (green=preferred, yellow=consider, red=last resort)
- Include decision criteria at each branch
- Add "Most common path" annotation

### Fallback Description

Create in flowchart software:
- Decision tree with diamond decision nodes
- Rectangular terminal nodes with outcomes
- Cost/benefit annotations
- Color coding for recommendation

### Caption

**Recommended Caption:**
"Decision framework for using vs. building foundation models. Entry point: a new genomic prediction task. First decision: does a suitable pretrained model exist? If yes, assess task alignment. For high alignment, USE frozen embeddings (hours of work, ~$10 compute, achieving 70-90% of fine-tuned performance)—this serves most applications. For moderate alignment, ADAPT using LoRA or light fine-tuning (days of work, $100-1000 compute, ~95% of full fine-tuning). Only when existing models fundamentally lack required capabilities should practitioners BUILD custom foundation models (months of work, $100K+ compute). The vast majority of applications are best served by using or adapting existing models rather than building from scratch."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 13.1 Paradigm Shift | 2 | Essential | Medium (comparison) |
| 13.2 Scaling Laws | 3 | Essential | Medium (log-log plots) |
| 13.3 Model Taxonomy | 1 | Essential | Medium (taxonomy) |
| 13.4 Design Dimensions | 1 | High | Medium (radar chart) |
| 13.5 Build vs. Use | 1 | High | Medium (flowchart) |

**Total files:** 8
**Recommended generation order:** 13.1A-B (paradigm shift), 13.5 (decision flowchart), 13.3 (taxonomy), 13.2A-C (scaling laws), 13.4 (design dimensions)
# Figure Report: Chapter 14 - DNA Language Models

**Chapter:** Part 3, Chapter 14 - DNA Language Models
**Date:** 2026-01-07
**Figures:** 6 conceptual figures (15 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 14.1: DNA Language Model Timeline

**File:** `figs/part_3/ch14/01-fig-dna-lm-timeline.svg`
**Priority:** Essential
**Type:** Annotated timeline

### Content Description

Horizontal timeline showing the evolution of DNA language models with milestones:
- 2021: DNABERT (512 tokens, proof of concept)
- 2023: Nucleotide Transformer (6kb, multi-species, scaling)
- 2023: HyenaDNA (1 Mb, sub-quadratic)
- 2024: Caduceus (reverse-complement equivariance, Mamba)
- 2024-2025: Evo 2 (1 Mb, 7B-40B params, pan-genomic)

Upper track shows context length progression (log scale). Lower track shows key architectural innovations.

### DALL-E Prompt

```
Create a scientific timeline of DNA language model evolution. Save as: 01-fig-dna-lm-timeline.svg

Horizontal timeline 2020-2025:

MAIN TIMELINE (center):
Milestone markers with model names and key stats:
- 2021: "DNABERT" (512 tokens)
- 2023a: "Nucleotide Transformer" (6kb, multi-species)
- 2023b: "HyenaDNA" (1Mb context)
- 2024a: "Caduceus" (RC-equivariant)
- 2024b: "Evo 2" (40B params)

UPPER TRACK "Context Length":
Log-scale bar growing from 512 → 6k → 1M
Annotations at each jump

LOWER TRACK "Architectural Innovations":
- "k-mer tokenization"
- "Multi-species pretraining"
- "Sub-quadratic attention (Hyena)"
- "Mamba SSM, RC-equivariance"
- "Pan-genomic, generation"

Color gradient from early (light blue) to recent (dark blue). Clean scientific timeline, white background. Professional genomics AI evolution figure.
```

### Post-Processing Notes

- Add context length bars on log scale
- Include parameter counts for each model
- Add architectural innovation annotations
- Use consistent color scheme showing progression

### Caption

**Recommended Caption:**
"Evolution of DNA language models from 2021-2025. The timeline traces key milestones in architectural capability. DNABERT (2021) demonstrated proof-of-concept with 512-token contexts using k-mer tokenization. Nucleotide Transformer (2023) scaled to 2.5 billion parameters with 6kb context and multi-species pretraining. HyenaDNA (2023) broke through the quadratic attention barrier, achieving 1 megabase context through sub-quadratic Hyena operators. Caduceus (2024) introduced reverse-complement equivariance through bidirectional Mamba architectures. Evo 2 (2024-2025) scaled to 40 billion parameters with million-base contexts, enabling pan-genomic understanding and sequence generation. Upper track shows exponential growth in context length; lower track highlights architectural innovations enabling each advance."

---

## Figure 14.2: Long Context Revolution (Two-Panel)

**Files:**
- `figs/part_3/ch14/02-A-fig-long-context-revolution.svg`
- `figs/part_3/ch14/02-B-fig-long-context-revolution.svg`

**Priority:** Essential
**Type:** Architecture comparison

### Panel A: Attention Quadratic Bottleneck

**Content:** Visualization showing quadratic memory/compute growth with sequence length for standard attention. Matrix showing L×L attention becoming intractable at long contexts.

**DALL-E Prompt:**
```
Create a scientific diagram showing attention quadratic bottleneck. Save as: 02-A-fig-long-context-revolution.svg

Visual elements:
- X-axis: "Sequence Length" (1k, 10k, 100k, 1M)
- Y-axis: "Memory/Compute" (log scale)
- Quadratic curve (O(L²)) rising steeply
- Horizontal line showing "GPU memory limit"
- Intersection point labeled "Practical limit: ~10-50kb"

Inset: L×L attention matrix visualization
- Small matrix at 1k (easily computed)
- Large matrix at 100k (too large, red warning)

Annotations:
- "Quadratic scaling: O(L²)"
- "200kb context would require 40B elements"

Clean scientific scaling diagram, white background. Professional computational bottleneck illustration.
```

**Caption for Panel A:**
"The quadratic attention bottleneck limits standard transformers. Self-attention computes pairwise interactions between all positions, creating O(L²) memory and compute requirements. For a 200kb genomic region (capturing enhancer-promoter interactions), the attention matrix would contain 40 billion elements. This quadratic scaling makes standard attention intractable beyond approximately 10-50kb, falling short of biologically relevant distances."

### Panel B: Sub-Quadratic Solutions

**Content:** Comparison of sub-quadratic architectures: Hyena convolutions, Mamba state-space models, linear attention variants. Show how each achieves O(L) or O(L log L) scaling.

**DALL-E Prompt:**
```
Create a scientific diagram comparing sub-quadratic attention alternatives. Save as: 02-B-fig-long-context-revolution.svg

Scaling comparison plot:
- X-axis: "Sequence Length" (log scale, 1k to 10M)
- Y-axis: "Compute/Memory" (log scale)

Multiple curves:
- Red (steep): "Standard Attention O(L²)"
- Blue: "Hyena O(L log L)"
- Green: "Mamba/SSM O(L)"
- Orange: "Linear Attention O(L)"

Horizontal line: "Million-base tractability threshold"
Annotations showing which architectures cross threshold

Inset boxes describing each approach:
- Hyena: "Long convolutions with learnable filters"
- Mamba: "Selective state-space model"
- Linear: "Kernel approximation"

Clean scientific scaling comparison, white background. Professional sub-quadratic architecture figure.
```

**Caption for Panel B:**
"Sub-quadratic architectures enable million-base contexts. Standard attention (red) becomes intractable beyond tens of kilobases. Hyena (blue) uses long convolutions achieving O(L log L) scaling. Mamba and state-space models (green) achieve linear O(L) scaling through selective recurrence. Linear attention variants (orange) approximate full attention with linear complexity. These innovations enabled HyenaDNA and Caduceus to process million-base contexts, capturing regulatory relationships spanning entire genomic loci."

### Combined Caption

**Full Figure Caption:**
"Breaking the attention bottleneck for genomic modeling. (A) Standard self-attention requires computing all pairwise interactions between positions, creating quadratic O(L²) memory and compute requirements. This limits practical contexts to approximately 10-50 kilobases, falling short of enhancer-promoter distances (50-100kb) and topologically associating domain scales (~1Mb). (B) Sub-quadratic architectures achieve longer contexts through different strategies: Hyena uses learnable long convolutions (O(L log L)); Mamba employs selective state-space models with linear scaling (O(L)); linear attention approximates the attention mechanism with kernel methods (O(L)). These innovations enabled DNA language models to process million-base contexts, accessing biological relationships invisible to shorter-context models."

---

## Figure 14.3: Caduceus Equivariance (Three-Panel)

**Files:**
- `figs/part_3/ch14/03-A-fig-caduceus-equivariance.svg`
- `figs/part_3/ch14/03-B-fig-caduceus-equivariance.svg`
- `figs/part_3/ch14/03-C-fig-caduceus-equivariance.svg`

**Priority:** High
**Type:** Biological constraint illustration

### Panel A: The Biological Constraint

**Content:** Diagram showing that DNA has two strands with complementary information. A regulatory element on the forward strand has the same biological meaning as its reverse complement on the reverse strand.

**DALL-E Prompt:**
```
Create a scientific diagram showing DNA reverse complement equivalence. Save as: 03-A-fig-caduceus-equivariance.svg

DNA double helix unwound to show both strands:
- Forward strand: 5' → 3' with sequence "ATCGATCG..."
- Reverse strand: 3' ← 5' with complement "TAGCTAGC..."

Highlighted regulatory element (binding motif):
- Shown on forward strand
- Same motif shown as reverse complement on reverse strand
- Annotation: "Same biological function"

Both strands lead to same transcription factor binding

Label: "Biological Equivalence"
Annotation: "Models should give identical predictions for forward and reverse complement"

Clean molecular biology diagram, white background. Professional DNA strand equivalence illustration.
```

**Caption for Panel A:**
"The biological constraint of reverse complement equivalence. DNA's double-stranded nature means that sequence on one strand has complementary sequence on the other. A transcription factor binding site on the forward strand (5'→3') is biologically equivalent to reading the same site from the reverse strand. Models that process DNA should recognize this equivalence: identical predictions for a sequence and its reverse complement."

### Panel B: Standard Models Break Equivalence

**Content:** Show how standard unidirectional or bidirectional models give different predictions for forward vs. reverse complement sequences.

**DALL-E Prompt:**
```
Create a scientific diagram showing standard models break RC equivalence. Save as: 03-B-fig-caduceus-equivariance.svg

Two parallel processing paths:

TOP PATH:
"Forward: ATCGATCG" → "Standard Model" → "Prediction: 0.85"

BOTTOM PATH:
"Reverse Complement: CGATCGAT" → "Same Model" → "Prediction: 0.62"

Warning symbol in center
Annotation: "Different predictions for biologically equivalent inputs!"
Red X mark indicating failure

Label: "Standard Models Violate Biological Constraint"

Clean comparison diagram with warning highlights, white background. Professional model failure illustration.
```

**Caption for Panel B:**
"Standard models violate reverse complement equivalence. Processing a sequence through a standard transformer produces one prediction (0.85). Processing its reverse complement through the same model produces a different prediction (0.62). This inconsistency violates the biological constraint that these sequences are functionally equivalent, potentially causing strand-dependent prediction artifacts."

### Panel C: Caduceus Architecture

**Content:** Show Caduceus bidirectional Mamba architecture that processes both strands simultaneously and ensures equivariant outputs.

**DALL-E Prompt:**
```
Create a scientific diagram showing Caduceus RC-equivariant architecture. Save as: 03-C-fig-caduceus-equivariance.svg

Architecture diagram:

INPUT: Sequence shown on both strands

PROCESSING:
- Forward Mamba SSM (processing left → right)
- Reverse Mamba SSM (processing right → left)
- Bidirectional combination layer
- Equivariance constraint (mathematical notation)

OUTPUT:
Both "Forward: ATCGATCG" and "RC: CGATCGAT" → "Identical prediction: 0.73"

Green checkmarks showing equivalence achieved
Annotation: "Architectural guarantee of RC equivariance"

Label: "Caduceus: Built-in Biological Constraint"

Clean architecture diagram with bidirectional flow, white background. Professional equivariant architecture figure.
```

**Caption for Panel C:**
"Caduceus architecture guarantees reverse complement equivariance. Bidirectional Mamba layers process sequence in both directions simultaneously. The architecture combines forward and reverse information through equivariant operations, mathematically guaranteeing that a sequence and its reverse complement produce identical predictions. This built-in constraint eliminates strand-dependent artifacts without requiring data augmentation."

### Combined Caption

**Full Figure Caption:**
"Reverse complement equivariance as architectural constraint. (A) DNA's double-stranded nature creates biological equivalence: a regulatory element on one strand has the same function when read as its reverse complement from the other strand. (B) Standard models violate this equivalence, producing different predictions for forward and reverse complement sequences despite their biological identity. (C) Caduceus uses bidirectional Mamba state-space models with equivariant architecture to guarantee identical predictions for equivalent sequences. This architectural constraint eliminates strand bias without data augmentation, improving both biological correctness and data efficiency."

---

## Figure 14.4: Evo 2 Training (Three-Panel)

**Files:**
- `figs/part_3/ch14/04-A-fig-evo2-training.svg`
- `figs/part_3/ch14/04-B-fig-evo2-training.svg`
- `figs/part_3/ch14/04-C-fig-evo2-training.svg`

**Priority:** High
**Type:** Training regime visualization

### Panel A: Pan-Genomic Data

**Content:** Pie chart or treemap showing the diversity of training data across species and genome types (prokaryotes, eukaryotes, viruses, plasmids).

**DALL-E Prompt:**
```
Create a scientific visualization of Evo 2 pan-genomic training data. Save as: 04-A-fig-evo2-training.svg

Treemap or sunburst chart showing data composition:

MAIN CATEGORIES (outer ring):
- Bacteria (~40%): Multiple species shown
- Archaea (~10%): Diverse types
- Eukaryotes (~35%): Plants, animals, fungi
- Viruses (~10%): Phages, animal viruses
- Plasmids (~5%): Circular elements

Inner details showing species diversity within each category
Numbers indicating billions of nucleotides per category

Total annotation: "2.7 trillion nucleotides"
Label: "Pan-Genomic Training Corpus"

Color-coded by domain of life. Clean data composition figure, white background. Professional training data visualization.
```

**Caption for Panel A:**
"Pan-genomic training data for Evo 2. The training corpus spans 2.7 trillion nucleotides across all domains of life: bacteria (~40%), eukaryotes (~35%), archaea (~10%), viruses (~10%), and plasmids (~5%). This diversity enables the model to learn sequence patterns that generalize across evolutionary history, from highly conserved core genes to lineage-specific innovations."

### Panel B: Context Length Curriculum

**Content:** Training progression showing context length increases over training: starting at short contexts, progressively extending to million-base contexts.

**DALL-E Prompt:**
```
Create a scientific diagram showing Evo 2 context length curriculum. Save as: 04-B-fig-evo2-training.svg

Training progression plot:
- X-axis: "Training Progress" (% or steps)
- Y-axis: "Context Length" (log scale, 1k to 1M)

Step function showing curriculum:
- Stage 1: 8k context (initial training)
- Stage 2: 32k context
- Stage 3: 131k context
- Stage 4: 1M context (final)

At each stage:
- Checkpoint annotation
- Learning rate adjustment notation
- "Warm up" periods highlighted

Label: "Progressive Context Length Training"
Annotation: "Stable optimization through curriculum"

Clean curriculum visualization, white background. Professional training progression figure.
```

**Caption for Panel B:**
"Context length curriculum for stable million-base training. Evo 2 training begins at 8k context where optimization is stable, progressively extending through 32k, 131k, and finally 1M tokens. At each stage transition, learning rates are adjusted and the model is allowed to adapt before further extension. This curriculum prevents the optimization instabilities that occur when training directly at very long contexts."

### Panel C: Generation Capability

**Content:** Example showing Evo 2 generating novel genomic sequence with biological coherence: gene structures, regulatory elements emerge from autoregressive sampling.

**DALL-E Prompt:**
```
Create a scientific diagram showing Evo 2 sequence generation. Save as: 04-C-fig-evo2-training.svg

Generated sequence visualization:

TOP: Autoregressive generation process
- "Prompt: [start of gene region]"
- Arrow showing left-to-right generation
- "Generated sequence: ATGCGT..."

MIDDLE: Annotation of generated sequence
- Color-coded regions:
  - Blue: Generated promoter region
  - Green: Generated coding sequence (ORF)
  - Orange: Generated regulatory elements
- Start/stop codons highlighted

BOTTOM: Quality metrics
- "ORF density: 78% (vs. 80% natural)"
- "Motif frequency: matches training distribution"
- "Novel: <0.1% exact match to training"

Label: "Coherent Biological Generation"
Annotation: "Generates novel sequences with correct biological structure"

Clean generation visualization, white background. Professional sequence generation figure.
```

**Caption for Panel C:**
"Evo 2 generates biologically coherent novel sequences. Autoregressive sampling from the trained model produces sequences with emergent biological structure: promoter elements, open reading frames with appropriate start/stop codons, and regulatory motifs at expected frequencies. These generated sequences are novel (minimal exact match to training data) yet exhibit statistical properties matching natural genomes, demonstrating that the model has learned general principles of genome organization."

### Combined Caption

**Full Figure Caption:**
"Evo 2 training regime for pan-genomic understanding and generation. (A) Training data spans 2.7 trillion nucleotides across all domains of life, enabling learning of universal and lineage-specific sequence patterns. (B) Context length curriculum progressively extends from 8k to 1M tokens, maintaining stable optimization through each transition. (C) The resulting model generates novel sequences with emergent biological coherence: appropriate gene structure, regulatory elements, and statistical properties matching natural genomes. This combination of massive scale, architectural innovation, and careful training regime enables both understanding and generation of genomic sequence."

---

## Figure 14.5: DNA Language Model Probing (Four-Panel)

**Files:**
- `figs/part_3/ch14/05-A-fig-dna-lm-probing.svg`
- `figs/part_3/ch14/05-B-fig-dna-lm-probing.svg`
- `figs/part_3/ch14/05-C-fig-dna-lm-probing.svg`
- `figs/part_3/ch14/05-D-fig-dna-lm-probing.svg`

**Priority:** High
**Type:** Probing analysis results

### Panel A: Genomic Element Recognition

**Content:** Bar chart showing linear probing accuracy for recognizing different genomic elements (promoters, enhancers, exons, introns, splice sites).

**DALL-E Prompt:**
```
Create a scientific bar chart showing DNA LM genomic element recognition. Save as: 05-A-fig-dna-lm-probing.svg

Grouped bar chart:
- X-axis: Genomic element types (Promoter, Enhancer, Exon, Intron, Splice Site, UTR)
- Y-axis: Linear Probe Accuracy (0.5 to 1.0)
- Bars for different models: DNABERT, NT, HyenaDNA

High accuracy (>0.85) for most elements
Lower accuracy for subtle elements like enhancers

Title: "Genomic Element Classification via Linear Probing"
Annotation: "Elements emerge in pretrained representations"

Clean grouped bar chart, white background. Professional probing analysis figure.
```

**Caption for Panel A:**
"DNA language models encode genomic element identity. Linear probes on frozen embeddings achieve high accuracy for classifying sequence regions as promoters, enhancers, exons, introns, splice sites, and UTRs. This demonstrates that pretrained representations contain linearly accessible information about genomic annotation categories, despite never seeing these labels during pretraining."

### Panel B: Conservation Patterns

**Content:** Scatter plot showing correlation between model-predicted importance (attention or gradient) and evolutionary conservation scores.

**DALL-E Prompt:**
```
Create a scientific scatter plot showing conservation correlation. Save as: 05-B-fig-dna-lm-probing.svg

Scatter plot:
- X-axis: "Model Attention/Importance Score"
- Y-axis: "PhyloP Conservation Score"
- Points showing positive correlation
- Trend line with correlation coefficient
- Density coloring (high density = darker)

Annotation: "r = 0.65, p < 0.001"
Title: "Model Attention Correlates with Conservation"

Inset showing example: highly-attended positions map to conserved regulatory elements

Clean correlation scatter plot, white background. Professional conservation analysis figure.
```

**Caption for Panel B:**
"Model attention correlates with evolutionary conservation. Positions receiving high attention in DNA language models tend to be evolutionarily conserved, as measured by PhyloP scores. This correlation (r ≈ 0.65) suggests the model has learned to focus on functionally important positions—those where mutations are likely to be deleterious—without explicit conservation supervision."

### Panel C: Regulatory Grammar

**Content:** Attention pattern heatmap showing learned regulatory grammar: enhancer-promoter attention, motif co-occurrence patterns.

**DALL-E Prompt:**
```
Create a scientific attention heatmap showing regulatory grammar. Save as: 05-C-fig-dna-lm-probing.svg

Attention heatmap:
- 200 × 200 position matrix
- Off-diagonal attention clusters showing long-range patterns
- Specific regions annotated:
  - "Enhancer region" (positions 20-40)
  - "Promoter region" (positions 150-170)
- Strong attention between these regions highlighted

Title: "Learned Regulatory Grammar"
Annotation: "Long-range attention captures enhancer-promoter relationships"

Color scale: white (low) to dark blue (high attention)

Clean attention visualization, white background. Professional regulatory grammar figure.
```

**Caption for Panel C:**
"DNA language models learn regulatory grammar. Attention patterns from a trained model show elevated weights between enhancer and promoter regions separated by tens of kilobases. These long-range attention patterns emerge from next-token prediction on genomic sequence, demonstrating that statistical patterns in DNA encode regulatory relationships that the model learns to capture."

### Panel D: Limitations Revealed

**Content:** Chart showing where probing fails: tissue-specific activity, environmental responses, 3D chromatin context—things not learnable from sequence alone.

**DALL-E Prompt:**
```
Create a scientific chart showing DNA LM probing limitations. Save as: 05-D-fig-dna-lm-probing.svg

Comparison chart with two categories:

SUCCEEDS (Green bars, high accuracy):
- "Sequence motifs" (0.90)
- "Splice sites" (0.88)
- "Promoter identity" (0.85)
- "Conservation" (0.82)

FAILS (Red bars, near chance):
- "Tissue-specific activity" (0.55)
- "Environmental response" (0.52)
- "3D chromatin contacts" (0.50)
- "Cell-type expression" (0.54)

Dividing line at chance level (0.5)
Annotation: "Sequence encodes potential, not realization"

Title: "What DNA LMs Can and Cannot Learn"

Clean comparison chart with success/failure contrast, white background. Professional limitation analysis figure.
```

**Caption for Panel D:**
"Probing reveals fundamental limitations of DNA language models. Linear probes succeed (green) for sequence-intrinsic properties: motifs, splice sites, promoter identity, and conservation patterns. Probing fails (red) for context-dependent properties: tissue-specific activity, environmental responses, 3D chromatin contacts, and cell-type-specific expression. This boundary reflects a fundamental truth: DNA sequence encodes regulatory potential, but whether that potential is realized depends on cellular context unavailable from sequence alone."

### Combined Caption

**Full Figure Caption:**
"Probing analysis reveals what DNA language models learn—and what they cannot. (A) Frozen embeddings support high-accuracy linear classification of genomic element types including promoters, enhancers, and splice sites. (B) Model attention correlates with evolutionary conservation, suggesting learned focus on functionally important positions. (C) Attention patterns capture long-range regulatory relationships between enhancers and promoters. (D) However, probing fails for context-dependent properties: tissue-specific activity, environmental responses, and 3D chromatin organization cannot be predicted from sequence representations alone. DNA language models learn sequence potential; realizing that potential requires cellular context they cannot access."

---

## Figure 14.6: DNA LM Benchmarks

**File:** `figs/part_3/ch14/06-fig-dna-lm-benchmarks.svg`
**Priority:** High
**Type:** Benchmark comparison table/heatmap

### Content Description

Heatmap or table comparing DNA language model performance across standardized benchmarks:
- Rows: Models (DNABERT, Nucleotide Transformer, HyenaDNA, Caduceus, Evo)
- Columns: Benchmark tasks (promoter classification, splice prediction, enhancer activity, variant effect, etc.)
- Color intensity showing relative performance

### DALL-E Prompt

```
Create a scientific heatmap comparing DNA LM benchmark performance. Save as: 06-fig-dna-lm-benchmarks.svg

Heatmap structure:

ROWS (Models, chronological):
- DNABERT
- Nucleotide Transformer
- HyenaDNA
- Caduceus
- Evo 2

COLUMNS (Benchmarks):
- Promoter Classification
- Splice Site Prediction
- Enhancer Activity
- TF Binding
- Variant Effect
- Gene Expression

Color scale: Light (0.5) → Dark blue (1.0)
Numbers in cells showing actual performance

Annotations:
- Column showing context length advantage for long-range tasks
- Row averages on right

Title: "DNA Language Model Benchmark Comparison"

Clean scientific heatmap with labels, white background. Professional benchmark comparison figure.
```

### Post-Processing Notes

- Add actual performance numbers in cells
- Include model metadata (params, context length)
- Highlight best performers per task
- Add notes on benchmark limitations

### Caption

**Recommended Caption:**
"Benchmark comparison across DNA language models. Heatmap shows relative performance on standardized genomic prediction tasks. Larger, newer models generally achieve higher performance, with particularly strong gains on tasks requiring long-range context (enhancer activity, gene expression) where architectural innovations enabling million-base contexts provide clear advantages. Performance on local tasks (splice prediction, promoter classification) is more saturated, with smaller models approaching larger model performance. These benchmarks primarily test frozen embedding quality; fine-tuning would yield different relative rankings."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 14.1 Timeline | 1 | Essential | Medium (annotated timeline) |
| 14.2 Long Context | 2 | Essential | Medium (scaling comparison) |
| 14.3 Caduceus | 3 | High | Medium (architecture) |
| 14.4 Evo 2 Training | 3 | High | Medium (training regime) |
| 14.5 Probing | 4 | High | Medium (analysis results) |
| 14.6 Benchmarks | 1 | High | Medium (heatmap) |

**Total files:** 14
**Recommended generation order:** 14.1 (timeline), 14.2A-B (context revolution), 14.6 (benchmarks), 14.3A-C (Caduceus), 14.5A-D (probing), 14.4A-C (Evo training)
# Figure Report: Chapter 15 - Protein Language Models

**Chapter:** Part 3, Chapter 15 - Protein Language Models
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (17 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 15.1: Emergent Properties of PLMs (Four-Panel)

**Files:**
- `figs/part_3/ch15/01-A-fig-plm-emergent.svg`
- `figs/part_3/ch15/01-B-fig-plm-emergent.svg`
- `figs/part_3/ch15/01-C-fig-plm-emergent.svg`
- `figs/part_3/ch15/01-D-fig-plm-emergent.svg`

**Priority:** Essential
**Type:** Multi-panel emergent capability demonstration

### Panel A: Contact Prediction

**Content:** Attention matrix from ESM compared to experimental contact map. Attention heads learn to identify residue-residue contacts without structural supervision.

**DALL-E Prompt:**
```
Create a scientific comparison of attention and contact maps. Save as: 01-A-fig-plm-emergent.svg

Side-by-side matrices:

LEFT: "ESM Attention Weights"
- L×L matrix with attention pattern
- Off-diagonal clusters indicating learned contacts

RIGHT: "Experimental Contact Map"
- L×L matrix with known structural contacts
- Similar pattern to attention

OVERLAY annotation showing correlation

Title: "Attention Captures Residue Contacts"
Annotation: "r = 0.8+ with no structural supervision"

Color scale: white to dark blue. Clean scientific comparison, white background. Professional emergent property figure.
```

**Caption for Panel A:**
"Attention heads learn residue contacts. Comparison between ESM attention patterns (left) and experimental contact maps (right) reveals that specific attention heads specialize in capturing residue-residue proximity relationships. This contact information emerges from masked language modeling on sequences alone, without any structural supervision."

### Panel B: Secondary Structure Encoding

**Content:** UMAP of residue embeddings colored by secondary structure (helix, sheet, coil). Clear clustering shows structure is encoded in representations.

**DALL-E Prompt:**
```
Create a scientific UMAP showing secondary structure encoding. Save as: 01-B-fig-plm-emergent.svg

UMAP scatter plot:
- Points representing individual residue embeddings
- Color-coded by secondary structure:
  - Red: Alpha helix
  - Blue: Beta sheet
  - Gray: Coil/loop
- Clear clustering by structure type
- Distinct regions for each secondary structure

Title: "Secondary Structure Emerges in Embedding Space"
Legend showing structure types

Clean UMAP visualization, white background. Professional representation analysis figure.
```

**Caption for Panel B:**
"Secondary structure emerges in residue embeddings. UMAP projection of ESM embeddings colored by secondary structure assignment shows clear clustering: alpha helices (red), beta sheets (blue), and coils (gray) occupy distinct regions of embedding space. This organization arises without structure labels, reflecting sequence patterns that evolution has associated with each structural context."

### Panel C: Functional Site Attention

**Content:** Attention visualization on a protein structure showing elevated attention on catalytic residues and binding sites.

**DALL-E Prompt:**
```
Create a scientific visualization of attention on functional sites. Save as: 01-C-fig-plm-emergent.svg

Protein structure cartoon (ribbon diagram):
- Overall structure in gray
- Active site residues highlighted in red (high attention)
- Binding pocket residues highlighted in orange
- Non-functional residues in light gray (low attention)

Attention intensity mapped as color/size

Title: "Attention Concentrates on Functional Sites"
Annotation: "Catalytic residues receive 3× average attention"

Clean protein visualization with attention overlay, white background. Professional functional site figure.
```

**Caption for Panel C:**
"Attention concentrates on functionally important positions. Visualization of attention weights mapped onto protein structure shows elevated attention on catalytic residues (red) and binding site positions (orange). These functionally critical sites receive 2-4 times higher attention than average residues, despite no functional annotation during training."

### Panel D: Taxonomic Organization

**Content:** UMAP of protein embeddings colored by taxonomic origin (bacteria, archaea, eukaryota). Shows evolutionary relationships encoded in representations.

**DALL-E Prompt:**
```
Create a scientific UMAP showing taxonomic organization. Save as: 01-D-fig-plm-emergent.svg

UMAP scatter plot:
- Points representing protein embeddings
- Color-coded by domain of life:
  - Blue: Bacteria
  - Green: Archaea
  - Orange: Eukaryota
- Clustering shows proteins from same domain near each other
- Some overlap where function conserved across domains

Title: "Evolutionary Relationships in Embedding Space"
Legend showing taxonomic categories

Clean UMAP visualization, white background. Professional evolutionary analysis figure.
```

**Caption for Panel D:**
"Protein embeddings encode evolutionary relationships. UMAP projection colored by taxonomic origin shows that proteins from the same domain of life cluster together, reflecting evolutionary divergence encoded in sequence patterns. Overlapping regions represent functionally conserved protein families where sequence similarity persists across domains."

### Combined Caption

**Full Figure Caption:**
"Emergent properties of protein language models. (A) Specific attention heads capture residue-residue contacts with high correlation to experimental structures. (B) Secondary structure emerges as distinct clusters in embedding space. (C) Attention concentrates on functionally important positions including catalytic sites and binding pockets. (D) Evolutionary relationships are encoded, with proteins clustering by taxonomic origin. All properties emerge from masked language modeling on protein sequences without explicit structural or functional supervision, demonstrating that evolutionary sequence patterns encode rich biological information."

---

## Figure 15.2: ESM-2 Scaling (Three-Panel)

**Files:**
- `figs/part_3/ch15/02-A-fig-esm2-scaling.svg`
- `figs/part_3/ch15/02-B-fig-esm2-scaling.svg`
- `figs/part_3/ch15/02-C-fig-esm2-scaling.svg`

**Priority:** Essential
**Type:** Scaling law demonstration

### Panel A: Parameter Scaling

**Content:** Log-log plot of model size (8M to 15B parameters) vs. perplexity, showing smooth power-law improvement.

**DALL-E Prompt:**
```
Create a scientific log-log scaling plot for ESM-2. Save as: 02-A-fig-esm2-scaling.svg

Log-log plot:
- X-axis: "Parameters" (8M to 15B, log scale)
- Y-axis: "Perplexity" (log scale, decreasing upward)
- Points for each model size: 8M, 35M, 150M, 650M, 3B, 15B
- Power-law trend line through points
- Equation: "Perplexity ∝ N^(-α)"

Labels for each point with ESM-2 variant name
Title: "Scaling of ESM-2 Model Family"

Clean log-log plot with trend line, white background. Professional scaling law figure.
```

**Caption for Panel A:**
"ESM-2 perplexity follows power-law scaling with parameters. Models ranging from 8 million to 15 billion parameters show smooth improvement in sequence modeling, with perplexity decreasing as N^(-α). This predictable relationship enabled informed decisions about computational investment during ESM-2 development."

### Panel B: Downstream Task Scaling

**Content:** Multiple lines showing how different downstream tasks (contact, structure, function) all improve with model size.

**DALL-E Prompt:**
```
Create a scientific plot showing downstream task scaling. Save as: 02-B-fig-esm2-scaling.svg

Multi-line plot:
- X-axis: "Parameters" (log scale, 8M to 15B)
- Y-axis: "Task Performance" (0.5 to 1.0)
- Multiple colored lines for different tasks:
  - Blue: "Contact Prediction"
  - Green: "Structure (GDT-TS)"
  - Orange: "Variant Effect"
  - Purple: "Function Prediction"
- All lines show upward trend with similar slopes
- 15B model shows best performance across all tasks

Title: "Downstream Performance Scales Consistently"
Legend showing task colors

Clean multi-line scaling plot, white background. Professional multi-task scaling figure.
```

**Caption for Panel B:**
"Downstream task performance scales consistently across tasks. Contact prediction, structure modeling, variant effect scoring, and function prediction all improve with model size following similar trends. The 15B parameter model achieves best performance across all evaluated tasks, demonstrating that scale benefits transfer broadly."

### Panel C: Compute Efficiency

**Content:** Iso-performance contours showing the trade-off between model size and training compute.

**DALL-E Prompt:**
```
Create a scientific contour plot showing ESM-2 compute efficiency. Save as: 02-C-fig-esm2-scaling.svg

Contour plot:
- X-axis: "Training FLOPs" (log scale)
- Y-axis: "Model Parameters" (log scale)
- Iso-perplexity contours (same perplexity along each curve)
- Color gradient: red (high perplexity) to blue (low)
- Diagonal ridge showing optimal scaling
- ESM-2 model points plotted on optimal line

Title: "Compute-Optimal Model Scaling"
Annotation: "ESM-2 follows near-optimal scaling"

Clean contour plot, white background. Professional compute efficiency figure.
```

**Caption for Panel C:**
"ESM-2 development followed compute-optimal scaling. Iso-perplexity contours show combinations of model size and training compute achieving equivalent performance. The ESM-2 model family (points) closely tracks the optimal ridge, maximizing performance for given computational resources. This efficient scaling enabled reaching 15B parameters within available compute budget."

### Combined Caption

**Full Figure Caption:**
"Scaling laws for protein language models demonstrated by ESM-2. (A) Perplexity decreases as a power law of parameter count from 8M to 15B parameters. (B) Downstream task performance scales consistently across diverse applications including contact prediction, structure modeling, and variant effect scoring. (C) ESM-2 development followed near-optimal compute scaling, maximizing capability for given resources. These scaling relationships, mirroring observations in natural language models, suggest that continued scaling would yield further improvements in protein understanding."

---

## Figure 15.3: ESMFold Architecture (Four-Panel)

**Files:**
- `figs/part_3/ch15/03-A-fig-esmfold.svg`
- `figs/part_3/ch15/03-B-fig-esmfold.svg`
- `figs/part_3/ch15/03-C-fig-esmfold.svg`
- `figs/part_3/ch15/03-D-fig-esmfold.svg`

**Priority:** High
**Type:** Architecture and comparison

### Panel A: ESMFold vs. AlphaFold2 Architecture

**Content:** Side-by-side comparison showing ESMFold's single-sequence input vs. AlphaFold2's MSA requirement.

**DALL-E Prompt:**
```
Create a scientific architecture comparison of ESMFold vs AlphaFold2. Save as: 03-A-fig-esmfold.svg

Side-by-side architecture diagrams:

LEFT (AlphaFold2):
- Input: "MSA (1000s of sequences)"
- "MSA Processing"
- "Evoformer"
- "Structure Module"
- Output: "3D Structure"
- Annotation: "Minutes per prediction"

RIGHT (ESMFold):
- Input: "Single Sequence"
- "ESM-2 (pretrained)"
- "Folding Module"
- Output: "3D Structure"
- Annotation: "Seconds per prediction"

Comparison arrow: "60× faster"
Title: "Single-Sequence vs. MSA-Based Folding"

Clean architecture comparison, white background. Professional structure prediction figure.
```

**Caption for Panel A:**
"ESMFold eliminates MSA requirement. AlphaFold2 (left) requires computing multiple sequence alignments from thousands of homologs before structure prediction. ESMFold (right) uses pretrained ESM-2 representations from a single sequence, achieving 60× speedup while maintaining competitive accuracy for most proteins."

### Panel B: Speed vs. Accuracy Trade-off

**Content:** Scatter plot comparing ESMFold and AlphaFold2 on accuracy (GDT-TS) vs. speed for the same protein set.

**DALL-E Prompt:**
```
Create a scientific comparison of speed vs accuracy. Save as: 03-B-fig-esmfold.svg

Two-axis comparison:
- X-axis: "Prediction Time (log scale, seconds)"
- Y-axis: "Structure Accuracy (GDT-TS)"

Two clusters of points:
- Blue: "AlphaFold2" (high accuracy ~0.92, slow ~100s)
- Green: "ESMFold" (good accuracy ~0.85, fast ~2s)

Arrow showing trade-off
Annotation: "10% accuracy loss, 50× speed gain"
Pareto frontier line

Title: "Speed-Accuracy Trade-off"

Clean scatter comparison, white background. Professional performance comparison figure.
```

**Caption for Panel B:**
"ESMFold trades modest accuracy for dramatic speed improvement. Comparison on the same protein set shows ESMFold achieving approximately 85% of AlphaFold2's accuracy at 50 times the speed. This trade-off makes ESMFold practical for proteome-scale structure prediction where MSA computation would be prohibitive."

### Panel C: Failure Modes

**Content:** Examples where ESMFold fails: orphan proteins without homologs, recent evolutionary innovations, highly dynamic proteins.

**DALL-E Prompt:**
```
Create a scientific visualization of ESMFold failure modes. Save as: 03-C-fig-esmfold.svg

Three failure case comparisons:

CASE 1 "Orphan Proteins":
- Predicted structure (gray, low confidence)
- True structure (colored)
- Poor overlay, large RMSD
- Annotation: "No evolutionary signal"

CASE 2 "Novel Folds":
- Similar poor prediction
- Annotation: "Unseen in training"

CASE 3 "Dynamic Proteins":
- Multiple conformations shown
- Prediction shows single state
- Annotation: "Cannot capture dynamics"

Title: "When Single-Sequence Prediction Fails"

Clean failure mode illustration, white background. Professional limitation analysis figure.
```

**Caption for Panel C:**
"ESMFold fails for specific protein categories. Orphan proteins lacking evolutionary relatives have no sequence patterns for the language model to leverage. Novel folds not present in training data cannot be predicted by pattern matching. Highly dynamic proteins with multiple conformations are poorly served by single-structure prediction. These cases require AlphaFold2 with explicit MSA construction or alternative approaches."

### Panel D: Application at Scale

**Content:** Visualization showing ESMFold enabling proteome-scale structure prediction (millions of structures predicted for metagenomic databases).

**DALL-E Prompt:**
```
Create a scientific visualization of ESMFold at scale. Save as: 03-D-fig-esmfold.svg

Scale visualization:

LEFT: "Metagenomic Databases"
- "617M protein sequences"
- Database icon

CENTER: "ESMFold Pipeline"
- Parallel processing arrows
- "~2 seconds per structure"

RIGHT: "ESM Metagenomic Atlas"
- "617M structures predicted"
- Structure gallery visualization
- "First proteome-scale structural survey"

Statistics box:
- "Compute: 2,000 GPU-months"
- "Coverage: All known protein families + novel"

Title: "Proteome-Scale Structure Prediction"

Clean scale visualization, white background. Professional large-scale application figure.
```

**Caption for Panel D:**
"ESMFold enables proteome-scale structure prediction. The ESM Metagenomic Atlas applied ESMFold to 617 million protein sequences from metagenomic databases, generating the first comprehensive structural survey of protein diversity. This scale would be computationally prohibitive with MSA-based methods, demonstrating how language model pretraining enables new scientific capabilities."

### Combined Caption

**Full Figure Caption:**
"ESMFold structure prediction from single sequences. (A) Architecture comparison: ESMFold uses pretrained ESM-2 representations from single sequences, eliminating AlphaFold2's MSA requirement and achieving 60× speedup. (B) Speed-accuracy trade-off: ESMFold achieves ~85% of AlphaFold2's accuracy at 50× the speed. (C) Failure modes: orphan proteins, novel folds, and dynamic proteins remain challenging without evolutionary context. (D) Scale application: the ESM Metagenomic Atlas predicted structures for 617 million proteins, demonstrating capabilities impossible with MSA-based methods."

---

## Figure 15.4: PLM Variant Scoring (Four-Panel)

**Files:**
- `figs/part_3/ch15/04-A-fig-plm-variant-scoring.svg`
- `figs/part_3/ch15/04-B-fig-plm-variant-scoring.svg`
- `figs/part_3/ch15/04-C-fig-plm-variant-scoring.svg`
- `figs/part_3/ch15/04-D-fig-plm-variant-scoring.svg`

**Priority:** Essential
**Type:** Method explanation and validation

### Panel A: Log-Likelihood Ratio Scoring

**Content:** Schematic showing how variant effect is computed as the difference in model likelihood between wild-type and mutant sequences.

**DALL-E Prompt:**
```
Create a scientific diagram of log-likelihood ratio variant scoring. Save as: 04-A-fig-plm-variant-scoring.svg

Two parallel computations:

TOP PATH "Wild-type":
- Sequence: "...MVLK..."
- Arrow to ESM model
- Output: "P(L|context) = 0.92"

BOTTOM PATH "Mutant":
- Sequence: "...MVPK..." (L→P substitution)
- Arrow to ESM model
- Output: "P(P|context) = 0.03"

COMPUTATION:
- Score = log(P_mut) - log(P_wt)
- Score = log(0.03) - log(0.92) = -3.4
- Interpretation: "Strongly deleterious"

Title: "Zero-Shot Variant Scoring via LLR"

Clean computation diagram, white background. Professional variant scoring figure.
```

**Caption for Panel A:**
"Log-likelihood ratio scoring for variant effects. The model computes probabilities for wild-type (0.92) and mutant (0.03) amino acids given sequence context. The log ratio quantifies how much the variant violates the model's learned expectations—more negative scores indicate stronger evolutionary constraint at that position."

### Panel B: Correlation with Experimental Effects

**Content:** Scatter plot showing PLM scores correlate with deep mutational scanning (DMS) experimental measurements.

**DALL-E Prompt:**
```
Create a scientific scatter plot of PLM vs DMS correlation. Save as: 04-B-fig-plm-variant-scoring.svg

Scatter plot:
- X-axis: "ESM Log-Likelihood Ratio"
- Y-axis: "DMS Fitness Score"
- Points showing positive correlation
- Trend line with r² annotation
- Density coloring (darker = more points)

Title: "PLM Scores Correlate with Experimental Effects"
Annotation: "Spearman ρ = 0.45-0.65 across proteins"

Clean correlation scatter, white background. Professional validation figure.
```

**Caption for Panel B:**
"PLM scores correlate with experimental fitness measurements. Scatter plot comparing ESM log-likelihood ratios with deep mutational scanning (DMS) fitness scores shows moderate to strong correlation (Spearman ρ = 0.45-0.65). This correlation enables zero-shot variant effect prediction without training on experimental data."

### Panel C: ClinVar Pathogenicity Classification

**Content:** ROC curve showing PLM scores discriminate pathogenic from benign variants in ClinVar.

**DALL-E Prompt:**
```
Create a scientific ROC curve for ClinVar classification. Save as: 04-C-fig-plm-variant-scoring.svg

ROC curve:
- X-axis: "False Positive Rate" (0 to 1)
- Y-axis: "True Positive Rate" (0 to 1)
- Diagonal chance line
- ESM curve well above diagonal
- AUC annotation: "auROC = 0.85"

Comparison lines:
- Blue: ESM-1v (0.85)
- Green: ESM-2 (0.87)
- Gray: SIFT (0.70) for reference

Title: "Pathogenicity Classification on ClinVar"
Legend showing method AUCs

Clean ROC curve comparison, white background. Professional classification figure.
```

**Caption for Panel C:**
"PLM scores discriminate pathogenic from benign ClinVar variants. ROC analysis shows ESM-based scoring achieves auROC of 0.85-0.87 for binary pathogenicity classification, substantially outperforming traditional conservation-based methods (SIFT, auROC ~0.70). This zero-shot performance requires no training on pathogenicity labels."

### Panel D: Position-Specific Performance

**Content:** Heatmap showing variant effect prediction accuracy varies by position—better at constrained core positions, worse at variable surface positions.

**DALL-E Prompt:**
```
Create a scientific heatmap of position-specific performance. Save as: 04-D-fig-plm-variant-scoring.svg

Protein structure cartoon with performance overlay:

STRUCTURE colored by prediction accuracy:
- Core (buried) positions: Blue (high correlation, r > 0.6)
- Surface (exposed) positions: Red (low correlation, r < 0.3)
- Active site: Green (highest correlation, r > 0.7)

Bar chart inset:
- "Core": 0.65 correlation
- "Surface": 0.25 correlation
- "Active site": 0.70 correlation

Title: "Position-Specific Prediction Quality"
Annotation: "Best for constrained positions"

Clean structure with accuracy overlay, white background. Professional position-specific figure.
```

**Caption for Panel D:**
"Prediction quality varies by structural context. PLM variant scoring performs best at evolutionarily constrained positions: core residues (buried, blue) and active sites (green) show high correlation with experimental effects. Surface positions (exposed, red) show weaker correlation because evolutionary constraint is weaker and variants are more tolerated. This pattern reflects that PLMs learn evolutionary constraint, which is strongest where function depends on sequence."

### Combined Caption

**Full Figure Caption:**
"Protein language model variant effect prediction. (A) Zero-shot scoring computes log-likelihood ratios between wild-type and mutant amino acids given sequence context. (B) PLM scores correlate moderately to strongly with deep mutational scanning fitness measurements (ρ = 0.45-0.65). (C) Binary pathogenicity classification on ClinVar achieves auROC of 0.85-0.87 without training on pathogenicity labels. (D) Performance varies by structural position, with best predictions at constrained core and active site residues where evolutionary pressure is strongest. These results demonstrate that evolutionary sequence patterns learned by PLMs provide clinically useful variant effect predictions."

---

## Figure 15.5: PLM Limitations

**File:** `figs/part_3/ch15/05-fig-plm-limitations.svg`
**Priority:** High
**Type:** Limitation overview

### Content Description

Multi-panel or annotated diagram showing key PLM limitations:
- Cannot predict gain-of-function mutations
- No cellular context (tissue, organelle)
- Single protein focus (no interaction partners)
- Training on natural proteins only (no synthetic/designed)
- Bias toward well-studied protein families

### DALL-E Prompt

```
Create a scientific diagram of PLM limitations. Save as: 05-fig-plm-limitations.svg

Five limitation panels in grid:

1. "Gain-of-Function":
- Icon: Mutation creating new activity
- X mark: "Cannot detect beneficial novelty"

2. "No Cellular Context":
- Icon: Cell diagram with organelles
- X mark: "Same embedding regardless of cell type"

3. "Single Protein Focus":
- Icon: Two interacting proteins
- X mark: "Cannot model interaction effects"

4. "Training Bias":
- Icon: Pie chart showing well-studied dominating
- X mark: "Biased toward characterized families"

5. "Natural Sequences Only":
- Icon: Synthetic vs natural comparison
- X mark: "May fail on designed proteins"

Central annotation: "Evolutionary constraint ≠ functional effect"
Title: "Fundamental Limitations of PLMs"

Clean limitation overview diagram, white background. Professional limitation analysis figure.
```

### Post-Processing Notes

- Use consistent iconography for each limitation
- Add brief explanations for each
- Include central unifying insight
- Color code by limitation severity

### Caption

**Recommended Caption:**
"Fundamental limitations of protein language models. PLMs learn evolutionary constraint but this differs from functional effect in several ways. (1) Gain-of-function mutations are invisible: deleterious and beneficial novelty both violate expectations but have opposite effects. (2) Cellular context is absent: the same embedding represents a protein regardless of its tissue, organelle, or interaction context. (3) Single-protein focus: effects of mutations on protein-protein interactions cannot be modeled without the partner. (4) Training bias: well-studied protein families dominate UniRef, biasing representations toward characterized proteins. (5) Natural sequences only: designed or synthetic proteins may fall outside the training distribution. These limitations constrain where PLM predictions can be trusted and where additional methods are needed."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 15.1 Emergent Properties | 4 | Essential | High (multi-panel) |
| 15.2 ESM-2 Scaling | 3 | Essential | Medium (scaling plots) |
| 15.3 ESMFold | 4 | High | Medium (architecture + results) |
| 15.4 Variant Scoring | 4 | Essential | Medium (method + validation) |
| 15.5 Limitations | 1 | High | Medium (overview) |

**Total files:** 16
**Recommended generation order:** 15.4A-D (variant scoring, most clinical), 15.1A-D (emergent), 15.2A-C (scaling), 15.3A-D (ESMFold), 15.5 (limitations)
# Figure Report: Chapter 16 - Regulatory Sequence Models

**Chapter:** Part 3, Chapter 16 - Regulatory Sequence Models
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (13 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 16.1: Long-Range Regulation (Four-Panel)

**Files:**
- `figs/part_3/ch16/01-A-fig-long-range-regulation.svg`
- `figs/part_3/ch16/01-B-fig-long-range-regulation.svg`
- `figs/part_3/ch16/01-C-fig-long-range-regulation.svg`
- `figs/part_3/ch16/01-D-fig-long-range-regulation.svg`

**Priority:** Essential
**Type:** Biological motivation for architecture

### Panel A: Enhancer-Promoter Distance

**Content:** Genome browser view showing enhancer and promoter separated by ~50kb, with Hi-C contact evidence.

**DALL-E Prompt:**
```
Create a scientific genome browser showing enhancer-promoter distance. Save as: 01-A-fig-long-range-regulation.svg

Browser-style visualization:
- Genomic coordinates track (0-100kb)
- Gene track showing target gene with promoter
- Enhancer element ~50kb upstream
- Hi-C contact arc connecting enhancer to promoter
- GWAS hit indicated at enhancer

Scale bar: "50 kb"
Title: "Regulatory Elements Span Tens of Kilobases"
Annotation: "GWAS variant in enhancer affects gene 50kb away"

Clean genome browser style, white background. Professional regulatory visualization.
```

**Caption for Panel A:**
"Regulatory elements span tens of kilobases. Genome browser view showing an enhancer ~50kb from its target promoter, connected by a Hi-C contact arc indicating 3D proximity. Many GWAS variants fall in such distal enhancers, requiring models with sufficient context to capture enhancer-gene relationships."

### Panel B: Context Length Requirements

**Content:** Histogram of enhancer-gene distances showing most require 50-200kb context.

**DALL-E Prompt:**
```
Create a scientific histogram of enhancer-gene distances. Save as: 01-B-fig-long-range-regulation.svg

Histogram:
- X-axis: "Enhancer-Gene Distance (kb)" (0 to 500)
- Y-axis: "Number of Interactions"
- Distribution peaked around 50-100kb, long tail to 500kb
- Vertical lines showing model context limits:
  - Red: "DeepSEA (1kb)"
  - Orange: "SpliceAI (10kb)"
  - Green: "Enformer (200kb)"
- Shaded region showing "Captured by Enformer"

Title: "Distribution of Regulatory Distances"
Annotation: "Most interactions require >10kb context"

Clean histogram with context limits, white background. Professional distance distribution figure.
```

**Caption for Panel B:**
"Context length requirements for regulatory modeling. Distribution of enhancer-gene distances from Hi-C data shows most interactions span 50-200kb. Vertical lines indicate context limits of different models: DeepSEA (1kb) and SpliceAI (10kb) miss most interactions, while Enformer (200kb) captures the majority of enhancer-promoter pairs."

### Panel C: 3D Chromatin Context

**Content:** TAD structure visualization showing how 3D organization constrains enhancer-promoter pairing.

**DALL-E Prompt:**
```
Create a scientific TAD structure visualization. Save as: 01-C-fig-long-range-regulation.svg

TAD triangle diagram:
- Horizontal axis showing genomic position
- Triangular Hi-C heatmap above
- Two TADs visible as triangular domains
- TAD boundary marked between them
- Within-TAD contacts (high, red)
- Cross-TAD contacts (low, blue)

Below: Linear annotation showing:
- Genes within same TAD → interact
- Genes across TAD boundary → isolated

Title: "3D Chromatin Organization (TADs)"
Annotation: "Enhancers only contact genes within same TAD"

Clean TAD visualization, white background. Professional chromatin architecture figure.
```

**Caption for Panel C:**
"Topologically associating domains (TADs) constrain regulatory interactions. Hi-C heatmap shows two TADs as triangular domains with high internal contact frequency. Enhancers typically only regulate genes within the same TAD; TAD boundaries insulate against cross-domain contacts. Models must implicitly learn these constraints to correctly predict gene expression."

### Panel D: Architectural Trade-offs

**Content:** Comparison table/diagram showing CNN, hybrid, and transformer approaches for capturing long-range context.

**DALL-E Prompt:**
```
Create a scientific comparison of regulatory model architectures. Save as: 01-D-fig-long-range-regulation.svg

Architecture comparison table:

               CNN-only    Hybrid     Transformer
Context        1-10kb      200kb      1Mb+
Compute        Low         Medium     High
Long-range     Poor        Good       Best
Local          Best        Good       Medium
Example        DeepSEA     Enformer   HyenaDNA

Visual diagram below:
- CNN: Small receptive field (triangle)
- Hybrid: CNN+Attention (trapezoid + attention arcs)
- Transformer: Full attention (all-to-all connections)

Title: "Architectural Trade-offs for Regulatory Modeling"

Clean comparison diagram, white background. Professional architecture comparison figure.
```

**Caption for Panel D:**
"Architectural trade-offs for long-range regulatory modeling. Pure CNN architectures capture local patterns efficiently but have limited receptive fields. Hybrid architectures (CNN + attention) balance local pattern extraction with long-range integration. Full transformer approaches enable arbitrary-distance interactions but at higher computational cost. The choice depends on the regulatory distances most relevant to the target application."

### Combined Caption

**Full Figure Caption:**
"The biological case for long-range regulatory models. (A) Enhancers regulate genes across tens of kilobases, as shown by Hi-C contacts connecting distal elements to promoters. (B) Distribution of enhancer-gene distances shows most interactions require >10kb context, exceeding early CNN model capacities. (C) TAD structure constrains which enhancers can contact which promoters, creating patterns models must learn. (D) Different architectures trade off between context length, computational cost, and local pattern sensitivity. Hybrid approaches like Enformer balance these factors for practical 200kb contexts."

---

## Figure 16.2: Enformer Architecture

**File:** `figs/part_3/ch16/02-fig-enformer-architecture.svg`
**Priority:** Essential
**Type:** Detailed architecture diagram

### Content Description

End-to-end architecture diagram showing:
- Input: 196kb one-hot encoded sequence
- Convolutional stem with pooling
- Transformer layers for long-range integration
- Multi-head prediction for thousands of tracks (chromatin, expression)
- Output spatial resolution and track organization

### DALL-E Prompt

```
Create a scientific architecture diagram for Enformer. Save as: 02-fig-enformer-architecture.svg

Left-to-right architecture flow:

INPUT (left):
- "196kb sequence" as 4×L matrix
- One-hot encoding illustration

CONVOLUTIONAL STEM:
- Conv layers with filter counts
- Pooling operations (128× total compression)
- Output: 1536 positions × D dimensions

TRANSFORMER LAYERS:
- 11 transformer blocks with attention arcs
- Cross-position attention patterns shown
- Dimension annotations

PREDICTION HEADS:
- Branching to multiple output types
- "5313 human tracks"
- "1643 mouse tracks"

OUTPUT (right):
- Spatial resolution: 128bp bins
- Track types: DNase, H3K27ac, CAGE, etc.

Title: "Enformer: Hybrid CNN-Transformer Architecture"

Clean architecture diagram with dimension annotations, white background. Professional deep learning architecture figure.
```

### Post-Processing Notes

- Add dimension annotations at each stage
- Include pooling factors
- Show attention patterns in transformer section
- List major track categories

### Caption

**Recommended Caption:**
"Enformer hybrid architecture for gene expression prediction. Input sequences spanning 196 kilobases are one-hot encoded and processed through a convolutional stem that extracts local patterns and compresses spatial resolution by 128×. Eleven transformer layers integrate information across the compressed representation, enabling direct communication between positions separated by nearly 200kb in the original sequence. Multiple prediction heads output 5,313 human and 1,643 mouse tracks including chromatin accessibility (DNase), histone modifications (H3K27ac, H3K4me3), and transcription (CAGE), at 128bp resolution. This multi-task architecture forces shared representations to capture the regulatory cascade from accessible chromatin through transcription."

---

## Figure 16.3: Regulatory VEP Workflow

**File:** `figs/part_3/ch16/03-fig-regulatory-vep-workflow.svg`
**Priority:** High
**Type:** Workflow/pipeline diagram

### Content Description

Step-by-step workflow for using regulatory models for variant effect prediction:
1. Center variant in context window
2. Compute predictions for reference and alternate
3. Calculate delta scores across tracks
4. Aggregate into interpretable variant effect summary

### DALL-E Prompt

```
Create a scientific workflow for regulatory variant effect prediction. Save as: 03-fig-regulatory-vep-workflow.svg

Step-by-step workflow (top to bottom):

STEP 1: "Center Variant in Window"
- 196kb window with variant at center
- Reference allele highlighted

STEP 2: "Predict Reference"
- Enformer processing
- Output: 5000+ track predictions

STEP 3: "Predict Alternate"
- Same sequence with alternate allele
- Different predictions

STEP 4: "Compute Delta"
- Δ = Alt - Ref for each track
- Heatmap showing changes

STEP 5: "Aggregate Effects"
- Key affected tracks identified
- Summary score (e.g., "Reduces expression 15%")

STEP 6: "Biological Interpretation"
- "Disrupts enhancer activity"
- "Affects tissue-specific regulation"

Title: "In Silico Mutagenesis for Regulatory Variants"

Clean workflow diagram with arrows, white background. Professional VEP pipeline figure.
```

### Post-Processing Notes

- Add example values at each step
- Show multiple tracks affected
- Include interpretation guidance
- Highlight tissue-specificity aspects

### Caption

**Recommended Caption:**
"Regulatory variant effect prediction workflow. Step 1: Center the variant within the model's input window (196kb for Enformer). Step 2: Compute model predictions for the reference sequence across all tracks. Step 3: Swap in the alternate allele and recompute predictions. Step 4: Calculate delta scores (alternate minus reference) for each track and position. Step 5: Aggregate effects to identify which chromatin or expression tracks are most affected. Step 6: Interpret biological meaning—does the variant disrupt an enhancer, affect tissue-specific regulation, or alter expression levels? This in silico mutagenesis approach enables prediction of regulatory variant effects without experimental measurements."

---

## Figure 16.4: Borzoi RNA-seq Prediction (Four-Panel)

**Files:**
- `figs/part_3/ch16/04-A-fig-borzoi-rnaseq.svg`
- `figs/part_3/ch16/04-B-fig-borzoi-rnaseq.svg`
- `figs/part_3/ch16/04-C-fig-borzoi-rnaseq.svg`
- `figs/part_3/ch16/04-D-fig-borzoi-rnaseq.svg`

**Priority:** High
**Type:** Model output and application

### Panel A: RNA-seq Profile Prediction

**Content:** Predicted vs. observed RNA-seq coverage tracks across a gene, showing accurate prediction of exon structure and expression levels.

**DALL-E Prompt:**
```
Create a scientific comparison of predicted vs observed RNA-seq. Save as: 04-A-fig-borzoi-rnaseq.svg

Two aligned browser tracks:

TOP: "Predicted (Borzoi)"
- RNA-seq-like coverage profile
- Exon peaks, intron valleys
- Splice junctions visible

BOTTOM: "Observed (RNA-seq)"
- Experimental RNA-seq coverage
- Same pattern as predicted

OVERLAY region showing correlation

Gene annotation track below:
- Exon boxes
- Intron lines
- Direction arrow

Title: "Borzoi Predicts RNA-seq Coverage"
Correlation annotation: "r = 0.85"

Clean genome browser style, white background. Professional expression prediction figure.
```

**Caption for Panel A:**
"Borzoi predicts RNA-seq coverage profiles from sequence. Predicted coverage (top) closely matches observed RNA-seq (bottom) across a gene region, correctly capturing exon structure, splice junction usage, and relative expression levels. This nucleotide-resolution output enables detection of variants affecting splicing or isoform usage."

### Panel B: Isoform Quantification

**Content:** Bar chart comparing predicted vs. observed isoform proportions for a gene with alternative splicing.

**DALL-E Prompt:**
```
Create a scientific comparison of predicted vs observed isoforms. Save as: 04-B-fig-borzoi-rnaseq.svg

Paired bar chart:
- X-axis: Isoform types (Full, Exon5-skip, Exon7-8-alt, Other)
- Y-axis: Proportion (0 to 0.6)
- Blue bars: Predicted
- Orange bars: Observed
- Error bars on observed

Title: "Isoform Proportion Prediction"
Correlation annotation: "r = 0.92 across isoforms"

Gene diagram below showing different isoform structures

Clean bar comparison, white background. Professional isoform prediction figure.
```

**Caption for Panel B:**
"Borzoi predicts alternative isoform proportions. Comparison of predicted (blue) versus observed (orange) isoform usage for a gene with alternative splicing. The model correctly ranks isoform abundance and captures the dominant splice patterns, enabling detection of variants that shift isoform balance."

### Panel C: Splicing Variant Detection

**Content:** Example of Borzoi detecting a cryptic splice variant that creates aberrant isoform.

**DALL-E Prompt:**
```
Create a scientific visualization of splice variant detection. Save as: 04-C-fig-borzoi-rnaseq.svg

Two-panel comparison:

REFERENCE ALLELE (top):
- Gene diagram with normal splicing pattern
- Predicted coverage showing normal exon structure
- Annotation: "Normal splice site usage"

VARIANT ALLELE (bottom):
- Same gene with variant marked
- Predicted coverage showing aberrant splice
- New exon inclusion or exon skipping visible
- Annotation: "Cryptic splice activation"

Delta track between panels highlighting change

Title: "Detecting Splicing Variants with Borzoi"

Clean splice variant visualization, white background. Professional variant detection figure.
```

**Caption for Panel C:**
"Borzoi detects splicing variants through coverage prediction changes. The reference allele (top) shows normal splice patterns. The variant allele (bottom) activates a cryptic splice site, creating an aberrant isoform visible as changed coverage patterns. This enables detection of splice-disrupting variants beyond the canonical GT/AG dinucleotides."

### Panel D: Tissue-Specific Effects

**Content:** Heatmap showing variant effects vary by tissue, with some tissues unaffected and others showing strong expression changes.

**DALL-E Prompt:**
```
Create a scientific heatmap of tissue-specific variant effects. Save as: 04-D-fig-borzoi-rnaseq.svg

Heatmap:
- Rows: Tissues (Liver, Brain, Heart, Kidney, Lung, Blood, etc.)
- Columns: Genes near variant
- Color scale: Blue (decreased) to Red (increased)

Pattern showing:
- Target gene strongly affected in specific tissues
- Other tissues unaffected
- Nearby genes with varied effects

Title: "Tissue-Specific Variant Effects"
Annotation: "Variant affects expression only in liver and kidney"

Clean heatmap with tissue labels, white background. Professional tissue-specific figure.
```

**Caption for Panel D:**
"Regulatory variants show tissue-specific effects. Heatmap of predicted expression changes across tissues reveals the variant affects target gene expression only in liver and kidney, with other tissues unaffected. This tissue-specificity, invisible to tissue-agnostic models, is essential for understanding variant pathogenicity in the context of specific diseases."

### Combined Caption

**Full Figure Caption:**
"Borzoi predicts RNA-seq profiles from sequence for variant interpretation. (A) Predicted coverage closely matches observed RNA-seq, capturing gene structure and expression levels. (B) Alternative isoform proportions are accurately predicted, enabling detection of splicing-shift variants. (C) Splice-disrupting variants are detected through coverage pattern changes between reference and alternate alleles. (D) Tissue-specific expression effects reveal that variants may affect different tissues differently, essential for understanding disease-relevant consequences."

---

## Figure 16.5: Regulatory Model Limitations (Four-Panel)

**Files:**
- `figs/part_3/ch16/05-A-fig-regulatory-limitations.svg`
- `figs/part_3/ch16/05-B-fig-regulatory-limitations.svg`
- `figs/part_3/ch16/05-C-fig-regulatory-limitations.svg`
- `figs/part_3/ch16/05-D-fig-regulatory-limitations.svg`

**Priority:** High
**Type:** Limitation analysis

### Panel A: Reference Haplotype Assumption

**Content:** Diagram showing models process variants on reference background, ignoring other variants in the same haplotype.

**DALL-E Prompt:**
```
Create a diagram showing reference haplotype limitation. Save as: 05-A-fig-regulatory-limitations.svg

Comparison:

TOP "Model Input":
- Reference sequence with single variant inserted
- Other variants on same haplotype NOT included
- Label: "Ignores haplotype context"

BOTTOM "Reality":
- Patient haplotype with multiple linked variants
- Compound effects between variants
- Label: "Variants interact on haplotypes"

Warning annotation: "Model assumes reference background"

Clean comparison diagram, white background. Professional limitation illustration.
```

**Caption for Panel A:**
"Reference haplotype assumption ignores linked variants. Models insert single variants into reference sequences, ignoring other variants present on the same haplotype. In reality, patients carry multiple variants that may interact, potentially canceling or amplifying effects invisible to single-variant analysis."

### Panel B: Training Set Cell Type Bias

**Content:** Pie chart or bar chart showing training data dominated by certain cell types (e.g., immortalized lines, blood) with disease-relevant tissues underrepresented.

**DALL-E Prompt:**
```
Create a chart showing training cell type bias. Save as: 05-B-fig-regulatory-limitations.svg

Bar chart:
- X-axis: Cell/tissue types
- Y-axis: Number of training tracks (log scale)
- Bars showing:
  - K562 (leukemia line): Very high
  - GM12878 (lymphoblast): Very high
  - HepG2 (liver cancer): High
  - Primary tissues: Low
  - Disease-relevant (neurons, islets): Very low

Annotations:
- "Immortalized cell lines dominate"
- "Primary tissues underrepresented"

Title: "Training Data Cell Type Distribution"

Clean bar chart with bias highlighted, white background. Professional data bias figure.
```

**Caption for Panel B:**
"Training data biased toward immortalized cell lines. Bar chart shows training tracks dominated by ENCODE tier-1 cell lines (K562, GM12878) while primary tissues and disease-relevant cell types are underrepresented. Models may perform poorly for tissues absent from training data."

### Panel C: Correlation vs. Causation

**Content:** Diagram showing that predicting expression correlation is not the same as predicting causal effect of a variant.

**DALL-E Prompt:**
```
Create a diagram showing correlation vs causation limitation. Save as: 05-C-fig-regulatory-limitations.svg

Two scenarios:

LEFT "Model Predicts":
- Variant → Δ Accessibility → Δ Expression
- Direct arrow implying causation
- Label: "Implied causal chain"

RIGHT "Reality Options":
A) Variant causes expression change (correct)
B) Variant correlates but doesn't cause (confounded)
C) Variant affects accessibility, not expression

Warning: "Predicted correlation ≠ causal mechanism"

Title: "Distinguishing Correlation from Causation"

Clean conceptual diagram, white background. Professional causation limitation figure.
```

**Caption for Panel C:**
"Predicted correlation does not establish causation. Models predict that variants change accessibility and expression, but this prediction does not distinguish causal mechanisms from correlative patterns. A variant may correlate with expression changes without being the causal driver, limiting clinical utility of prediction alone."

### Panel D: Structural Variant Blindness

**Content:** Illustration showing models cannot process structural variants (inversions, CNVs, translocations) that disrupt regulatory topology.

**DALL-E Prompt:**
```
Create a diagram showing structural variant blindness. Save as: 05-D-fig-regulatory-limitations.svg

Comparison:

TOP "What Models Handle":
- Linear sequence with SNV marked
- Standard variant effect prediction
- Checkmark

BOTTOM "What Models Cannot Handle":
- Inversion disrupting TAD boundary
- Copy number change duplicating enhancer
- Translocation fusing regulatory domains
- Large X marks

Title: "Structural Variants Beyond Model Capacity"
Annotation: "Most pathogenic SVs unmodeled"

Clean structural variant diagram, white background. Professional SV limitation figure.
```

**Caption for Panel D:**
"Structural variants beyond current model capacity. Models designed for substitutions and small indels cannot process structural variants (inversions, CNVs, translocations) that disrupt regulatory topology. These SVs represent a significant fraction of pathogenic regulatory variation, constituting a major gap in current prediction capability."

### Combined Caption

**Full Figure Caption:**
"Fundamental limitations of regulatory sequence models. (A) Reference haplotype assumption: models analyze single variants on reference backgrounds, ignoring haplotype context and variant interactions. (B) Training cell type bias: immortalized cell lines dominate training data; disease-relevant primary tissues are underrepresented. (C) Correlation vs. causation: predicted expression changes do not establish causal mechanism. (D) Structural variant blindness: inversions, CNVs, and translocations cannot be processed by current architectures. These limitations constrain clinical utility and must be addressed through experimental validation."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 16.1 Long-Range Regulation | 4 | Essential | Medium (biological motivation) |
| 16.2 Enformer Architecture | 1 | Essential | High (detailed architecture) |
| 16.3 VEP Workflow | 1 | High | Medium (pipeline) |
| 16.4 Borzoi RNA-seq | 4 | High | Medium (application) |
| 16.5 Limitations | 4 | High | Medium (analysis) |

**Total files:** 14
**Recommended generation order:** 16.2 (Enformer architecture), 16.1A-D (biological motivation), 16.3 (workflow), 16.4A-D (Borzoi), 16.5A-D (limitations)
# Figure Report: Chapter 17 - Variant Effect Prediction with Foundation Models

**Chapter:** Part 3, Chapter 17 - Variant Effect Prediction with Foundation Models
**Date:** 2026-01-07
**Figures:** 7 conceptual figures (26 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 17.1: FM VEP Paradigms (Four-Panel)

**Files:**
- `figs/part_3/ch17/01-A-fig-fm-vep-paradigm.svg`
- `figs/part_3/ch17/01-B-fig-fm-vep-paradigm.svg`
- `figs/part_3/ch17/01-C-fig-fm-vep-paradigm.svg`
- `figs/part_3/ch17/01-D-fig-fm-vep-paradigm.svg`

**Priority:** Essential
**Type:** Paradigm comparison

### Panel A: Zero-Shot Scoring

**Content:** Diagram showing PLM log-likelihood ratio scoring without any task-specific training.

**DALL-E Prompt:**
```
Create a diagram of zero-shot variant scoring. Save as: 01-A-fig-fm-vep-paradigm.svg

Flow diagram:
- Pretrained PLM (frozen, gray)
- Input: Wild-type and mutant sequences
- Output: Log-likelihood ratio score
- No training arrows (no task-specific data)

Labels:
- "No pathogenicity labels needed"
- "Scores from evolutionary constraint"

Title: "Zero-Shot Scoring"
Example: "ESM log-likelihood ratio"

Clean paradigm diagram, white background. Professional zero-shot VEP figure.
```

**Caption for Panel A:**
"Zero-shot scoring uses pretrained model likelihoods directly. The model computes how much a variant violates evolutionary expectations learned during pretraining. No pathogenicity labels are required—scores reflect deviation from natural sequence patterns."

### Panel B: Linear Probe

**Content:** Frozen embeddings with trained linear classifier for pathogenicity.

**DALL-E Prompt:**
```
Create a diagram of linear probe variant classification. Save as: 01-B-fig-fm-vep-paradigm.svg

Flow diagram:
- Pretrained PLM (frozen, gray)
- Embeddings extracted
- Linear classifier (trainable, blue)
- Output: Pathogenicity probability

Training data arrow: "ClinVar labels"
Label: "Embeddings + simple classifier"

Title: "Linear Probing"
Example: "ESM embeddings + logistic regression"

Clean paradigm diagram, white background. Professional linear probe VEP figure.
```

**Caption for Panel B:**
"Linear probing extracts frozen embeddings and trains a simple classifier. This approach requires minimal labeled data (hundreds to thousands of variants) and tests whether pretrained representations contain linearly accessible pathogenicity information."

### Panel C: Fine-Tuned Classifier

**Content:** Full fine-tuning of foundation model for pathogenicity prediction.

**DALL-E Prompt:**
```
Create a diagram of fine-tuned variant classifier. Save as: 01-C-fig-fm-vep-paradigm.svg

Flow diagram:
- Pretrained PLM (trainable, blue/green gradient)
- Classification head (trainable, blue)
- Gradient arrows through entire model
- Output: Pathogenicity probability

Training data arrow: "Large labeled dataset"
Labels:
- "All parameters updated"
- "Requires substantial data"

Title: "Full Fine-Tuning"
Example: "Fine-tuned transformer classifier"

Clean paradigm diagram, white background. Professional fine-tuning VEP figure.
```

**Caption for Panel C:**
"Full fine-tuning updates all model parameters for pathogenicity prediction. This approach requires larger labeled datasets (thousands to tens of thousands of variants) but can reshape representations specifically for the classification task."

### Panel D: Multi-Modal Integration

**Content:** Combining sequence model with structural information (AlphaFold) for enhanced prediction.

**DALL-E Prompt:**
```
Create a diagram of multi-modal VEP. Save as: 01-D-fig-fm-vep-paradigm.svg

Flow diagram:
- Two input streams:
  - Sequence → PLM → Sequence embeddings
  - Sequence → AlphaFold → Structure features
- Fusion layer combining both
- Classification head
- Output: Pathogenicity probability

Labels:
- "Evolutionary + structural information"
- "Best for missense variants"

Title: "Multi-Modal Integration"
Example: "AlphaMissense"

Clean paradigm diagram, white background. Professional multi-modal VEP figure.
```

**Caption for Panel D:**
"Multi-modal integration combines sequence and structure information. AlphaMissense exemplifies this approach, using both PLM evolutionary features and AlphaFold2 structural context. This integration captures complementary information: why positions are constrained (structure) and how constrained they are (evolution)."

### Combined Caption

**Full Figure Caption:**
"Foundation model paradigms for variant effect prediction. (A) Zero-shot scoring uses pretrained likelihoods directly, requiring no task-specific data but limited to what pretraining captured. (B) Linear probing adds a simple classifier on frozen embeddings, requiring minimal labeled data. (C) Full fine-tuning updates all parameters, achieving best performance but requiring substantial labeled data. (D) Multi-modal integration combines sequence (evolutionary) and structure information for comprehensive variant assessment. The appropriate paradigm depends on available labeled data and whether structure contributes to the variant's effect mechanism."

---

## Figure 17.2: AlphaMissense Architecture (Four-Panel)

**Files:**
- `figs/part_3/ch17/02-A-fig-alphamissense.svg`
- `figs/part_3/ch17/02-B-fig-alphamissense.svg`
- `figs/part_3/ch17/02-C-fig-alphamissense.svg`
- `figs/part_3/ch17/02-D-fig-alphamissense.svg`

**Priority:** Essential
**Type:** Architecture and results

### Panel A: Architecture Overview

**Content:** Detailed architecture showing ESM embeddings + AlphaFold2 structure features combined.

**DALL-E Prompt:**
```
Create AlphaMissense architecture diagram. Save as: 02-A-fig-alphamissense.svg

Architecture flow:
LEFT: "Protein Sequence"
- Arrow to ESM-1b → Evolutionary embeddings
- Arrow to AlphaFold2 → Structural features (distance, angles)

CENTER: "Feature Integration"
- Concatenation layer
- MLP processing layers

RIGHT: "Output"
- Per-variant pathogenicity score
- Calibrated probability

Annotations:
- "Evolutionary constraint from PLM"
- "Local structure context from AF2"

Title: "AlphaMissense: Evolution + Structure"

Clean architecture diagram, white background. Professional multi-modal architecture figure.
```

**Caption for Panel A:**
"AlphaMissense architecture combines evolutionary and structural features. ESM-1b provides per-residue evolutionary embeddings encoding constraint. AlphaFold2 provides structural context including residue-residue distances and angles. The integration layer combines these representations for variant pathogenicity prediction."

### Panel B: Performance Comparison

**Content:** Bar chart or ROC comparison showing AlphaMissense outperforms both sequence-only and structure-only approaches.

**DALL-E Prompt:**
```
Create performance comparison for AlphaMissense. Save as: 02-B-fig-alphamissense.svg

Grouped bar chart:
- X-axis: Methods (SIFT, ESM-only, Structure-only, AlphaMissense)
- Y-axis: auROC (0.7 to 1.0)
- Bars showing:
  - SIFT: ~0.70
  - ESM-only: ~0.85
  - Structure-only: ~0.80
  - AlphaMissense: ~0.92

Annotation: "Combination exceeds either alone"

Title: "AlphaMissense Performance on ClinVar"

Clean bar comparison, white background. Professional performance figure.
```

**Caption for Panel B:**
"AlphaMissense outperforms single-modality approaches. Comparison on ClinVar pathogenicity classification shows that combining evolutionary (ESM) and structural (AlphaFold2) features achieves higher accuracy than either alone. This demonstrates the complementary information in evolution and structure."

### Panel C: Structural Position Effects

**Content:** Scatter or violin plot showing pathogenicity scores differ by structural context (core vs. surface, binding site vs. non-binding).

**DALL-E Prompt:**
```
Create structural position effect visualization. Save as: 02-C-fig-alphamissense.svg

Violin plots:
- X-axis: Structural category (Core, Surface, Active Site, Interface)
- Y-axis: AlphaMissense Score (0 to 1)

Patterns:
- Core: High scores (most pathogenic)
- Active Site: High scores
- Interface: Medium-high
- Surface: Low scores (mostly benign)

Dashed line at 0.5 threshold

Title: "Pathogenicity Varies by Structural Context"
Annotation: "Core and active site variants most constrained"

Clean violin comparison, white background. Professional structure-function figure.
```

**Caption for Panel C:**
"Pathogenicity scores vary by structural context. Violin plots show that core (buried) and active site variants receive highest pathogenicity scores, reflecting strong structural and functional constraint. Surface variants receive low scores, reflecting tolerance to substitution. This structure-aware scoring captures why positions are constrained."

### Panel D: Proteome-Wide Classification

**Content:** Summary of proteome-wide predictions: how many human missense variants are classified benign/pathogenic/uncertain.

**DALL-E Prompt:**
```
Create proteome-wide classification summary. Save as: 02-D-fig-alphamissense.svg

Summary visualization:
- Total: "71 million possible missense variants"

Pie chart or stacked bar:
- Pathogenic (>0.564): ~32% (red)
- Ambiguous: ~11% (gray)
- Benign (<0.340): ~57% (blue)

Annotations:
- "23M predicted pathogenic"
- "8M uncertain"
- "40M predicted benign"

Title: "AlphaMissense Proteome Classification"
Note: "Largest pathogenicity resource created"

Clean summary visualization, white background. Professional proteome-scale figure.
```

**Caption for Panel D:**
"AlphaMissense classifies the entire human missense variant space. Of 71 million possible missense variants, approximately 32% are predicted pathogenic, 57% predicted benign, and 11% remain ambiguous. This proteome-scale classification provides prior expectations for rare variant interpretation."

### Combined Caption

**Full Figure Caption:**
"AlphaMissense: integrating evolution and structure for variant pathogenicity. (A) Architecture combines ESM evolutionary embeddings with AlphaFold2 structural features. (B) Performance exceeds single-modality approaches, demonstrating complementary information. (C) Pathogenicity scores appropriately vary by structural context: core and active site variants score highest. (D) Proteome-wide application classifies 71 million possible human missense variants, creating the largest pathogenicity prediction resource."

---

## Figure 17.3: Multi-Model Integration (Four-Panel)

**Files:**
- `figs/part_3/ch17/03-A-fig-multimodel-integration.svg`
- `figs/part_3/ch17/03-B-fig-multimodel-integration.svg`
- `figs/part_3/ch17/03-C-fig-multimodel-integration.svg`
- `figs/part_3/ch17/03-D-fig-multimodel-integration.svg`

**Priority:** High
**Type:** Integration strategies

### Panel A: Coding Variants Pipeline

**Content:** Flow showing how different models handle coding region variants (missense → PLM, nonsense → loss prediction, splice → SpliceAI).

**DALL-E Prompt:**
```
Create coding variant integration pipeline. Save as: 03-A-fig-multimodel-integration.svg

Decision tree for coding variants:

"Coding Variant" entry point

Branch 1: "Missense" → ESM/AlphaMissense → Score
Branch 2: "Nonsense/Frameshift" → Loss-of-function prediction
Branch 3: "Synonymous (splice-proximal)" → SpliceAI
Branch 4: "In-frame indel" → Structure + PLM

Integration layer combining scores

Title: "Coding Variant Decision Tree"

Clean decision flow, white background. Professional variant routing figure.
```

**Caption for Panel A:**
"Coding variant integration routes variants to appropriate models. Missense variants use PLM/structure methods (AlphaMissense). Nonsense and frameshift variants use loss-of-function predictions. Splice-proximal synonymous variants use SpliceAI. The integration combines predictions for comprehensive assessment."

### Panel B: Non-Coding Variants Pipeline

**Content:** Flow for non-coding variants (regulatory → Enformer, splice → SpliceAI, deep intronic → conservation + Enformer).

**DALL-E Prompt:**
```
Create non-coding variant integration pipeline. Save as: 03-B-fig-multimodel-integration.svg

Decision tree for non-coding variants:

"Non-Coding Variant" entry point

Branch 1: "Promoter/Enhancer" → Enformer → Expression effect
Branch 2: "Splice region" → SpliceAI → Splice disruption
Branch 3: "Deep intronic" → Conservation + Enformer
Branch 4: "UTR" → Multiple: RBP binding, miRNA sites

Integration layer

Title: "Non-Coding Variant Decision Tree"

Clean decision flow, white background. Professional variant routing figure.
```

**Caption for Panel B:**
"Non-coding variant integration uses specialized models for each region. Promoter and enhancer variants use regulatory models (Enformer). Splice region variants use splice predictors (SpliceAI). Deep intronic variants combine conservation with regulatory predictions. UTR variants consider RNA-binding and miRNA effects."

### Panel C: Ensemble Strategy

**Content:** Diagram showing how individual model predictions combine into ensemble score.

**DALL-E Prompt:**
```
Create ensemble integration diagram. Save as: 03-C-fig-multimodel-integration.svg

Multiple input models:
- ESM score
- AlphaMissense score
- Enformer delta
- SpliceAI score
- Conservation (phyloP)

Arrow flows to ensemble layer:
- "Learned weights" or "Logistic regression"
- Combines all scores

Output: "Integrated pathogenicity score"

Annotation: "Ensemble outperforms any single model"

Title: "Ensemble Variant Scoring"

Clean ensemble diagram, white background. Professional integration figure.
```

**Caption for Panel C:**
"Ensemble integration combines multiple model predictions. Individual scores from sequence (ESM), structure (AlphaMissense), regulatory (Enformer), splice (SpliceAI), and conservation models are combined through learned weights. Ensembles typically outperform any single model by capturing complementary information."

### Panel D: Uncertainty Aggregation

**Content:** Diagram showing how to aggregate uncertainty across multiple models—when models agree vs. disagree.

**DALL-E Prompt:**
```
Create uncertainty aggregation diagram. Save as: 03-D-fig-multimodel-integration.svg

Two scenarios:

LEFT "High Confidence":
- Multiple model scores all agree (all high or all low)
- Small variance shown
- Green checkmark: "Confident prediction"

RIGHT "High Uncertainty":
- Model scores disagree (some high, some low)
- Large variance shown
- Yellow warning: "Requires manual review"

Formula: "Uncertainty = disagreement + individual uncertainties"

Title: "Aggregating Uncertainty Across Models"

Clean uncertainty comparison, white background. Professional uncertainty figure.
```

**Caption for Panel D:**
"Uncertainty aggregation identifies variants requiring review. When models agree (left), predictions are confident. When models disagree (right), elevated uncertainty flags variants for manual review. Disagreement between evolutionary and structural predictions may indicate interesting biology—variants where one constraint is violated but not the other."

### Combined Caption

**Full Figure Caption:**
"Multi-model integration for comprehensive variant assessment. (A) Coding variants are routed to appropriate models based on consequence type. (B) Non-coding variants use specialized models for regulatory, splice, and other regions. (C) Ensemble methods combine individual model scores through learned weights, typically outperforming any single model. (D) Uncertainty aggregation identifies variants where models disagree, flagging them for review. This multi-model approach leverages the strengths of different foundation models for comprehensive variant interpretation."

---

## Figure 17.4: Calibration for Clinical Use (Four-Panel)

**Files:**
- `figs/part_3/ch17/04-A-fig-calibration-clinical.svg`
- `figs/part_3/ch17/04-B-fig-calibration-clinical.svg`
- `figs/part_3/ch17/04-C-fig-calibration-clinical.svg`
- `figs/part_3/ch17/04-D-fig-calibration-clinical.svg`

**Priority:** High
**Type:** Calibration analysis

### Panel A: Raw Score Distribution

**Content:** Histogram showing raw model scores distribution—typically not calibrated to clinical prevalence.

**DALL-E Prompt:**
```
Create raw score distribution visualization. Save as: 04-A-fig-calibration-clinical.svg

Histogram:
- X-axis: "Raw Model Score" (0 to 1)
- Y-axis: "Number of Variants"
- Distribution often bimodal or skewed
- Not aligned with pathogenicity prevalence

Annotations:
- "Raw scores not calibrated"
- "Don't interpret as probabilities"

Title: "Raw Score Distribution (Uncalibrated)"

Clean histogram, white background. Professional distribution figure.
```

**Caption for Panel A:**
"Raw model scores are not calibrated probabilities. The score distribution shows the model's internal ranking but cannot be interpreted as pathogenicity probability without calibration. A score of 0.7 does not mean 70% probability of pathogenicity."

### Panel B: Calibration Curve

**Content:** Reliability diagram showing predicted probability vs. observed fraction for calibrated vs. uncalibrated model.

**DALL-E Prompt:**
```
Create calibration curve comparison. Save as: 04-B-fig-calibration-clinical.svg

Reliability diagram:
- X-axis: "Predicted Probability"
- Y-axis: "Observed Fraction Pathogenic"
- Diagonal line (perfect calibration)
- Red curve: "Uncalibrated" (below diagonal = overconfident)
- Green curve: "After calibration" (near diagonal)

Title: "Calibration Curve: Before vs. After"
Annotation: "Calibration corrects systematic bias"

Clean calibration plot, white background. Professional reliability figure.
```

**Caption for Panel B:**
"Calibration curves reveal and correct probability bias. Uncalibrated predictions (red) fall below the diagonal, indicating overconfidence—the model predicts higher pathogenicity probability than observed. Post-calibration predictions (green) track the diagonal, providing accurate probability estimates."

### Panel C: Threshold Selection

**Content:** Trade-off curves showing sensitivity vs. specificity at different thresholds, with clinical operating points marked.

**DALL-E Prompt:**
```
Create threshold selection visualization. Save as: 04-C-fig-calibration-clinical.svg

ROC-style plot with operating points:
- X-axis: "Specificity" (1 to 0, inverted)
- Y-axis: "Sensitivity" (0 to 1)
- ROC curve
- Marked operating points:
  - "Screening" (high sensitivity, lower specificity)
  - "Diagnostic" (balanced)
  - "Confirmation" (high specificity, lower sensitivity)

Trade-off annotations

Title: "Clinical Operating Points"
Annotation: "Different use cases require different thresholds"

Clean operating point diagram, white background. Professional threshold figure.
```

**Caption for Panel C:**
"Threshold selection depends on clinical context. Screening applications favor high sensitivity (catch all pathogenic variants, accept false positives). Diagnostic applications balance sensitivity and specificity. Confirmation applications favor high specificity (minimize false positives, accept missing some). No single threshold serves all use cases."

### Panel D: Prevalence Adjustment

**Content:** Diagram showing how predictions must be adjusted for different clinical prevalence scenarios.

**DALL-E Prompt:**
```
Create prevalence adjustment diagram. Save as: 04-D-fig-calibration-clinical.svg

Three scenarios:

SCENARIO 1 "Healthy Population":
- Prior pathogenic: 0.01%
- Model score: 0.8
- Post-test probability: Low
- "Most positives are false positives"

SCENARIO 2 "Rare Disease Clinic":
- Prior pathogenic: 10%
- Model score: 0.8
- Post-test probability: Moderate
- "Reasonable confidence"

SCENARIO 3 "Selected Variants":
- Prior pathogenic: 50%
- Model score: 0.8
- Post-test probability: High
- "Strong evidence"

Bayes formula shown: P(pathogenic|score) depends on prior

Title: "Prevalence Affects Interpretation"

Clean scenario comparison, white background. Professional prevalence figure.
```

**Caption for Panel D:**
"Clinical prevalence affects score interpretation. The same model score (0.8) has different clinical implications depending on prior probability. In healthy populations (low prevalence), even high scores yield low positive predictive value. In rare disease clinics (higher prevalence), the same score provides stronger evidence. Proper interpretation requires adjusting for clinical context."

### Combined Caption

**Full Figure Caption:**
"Calibration for clinical variant interpretation. (A) Raw model scores are not calibrated probabilities and cannot be interpreted directly. (B) Calibration curves reveal overconfidence in uncalibrated predictions; post-calibration predictions track observed frequencies. (C) Threshold selection depends on clinical context: screening, diagnosis, and confirmation require different operating points. (D) Clinical prevalence dramatically affects interpretation—the same score means different things in healthy populations versus rare disease clinics. Proper clinical deployment requires calibration and prevalence-adjusted interpretation."

---

## Figure 17.5: VEP Uncertainty (Four-Panel)

**Files:**
- `figs/part_3/ch17/05-A-fig-vep-uncertainty.svg`
- `figs/part_3/ch17/05-B-fig-vep-uncertainty.svg`
- `figs/part_3/ch17/05-C-fig-vep-uncertainty.svg`
- `figs/part_3/ch17/05-D-fig-vep-uncertainty.svg`

**Priority:** High
**Type:** Uncertainty quantification

### Panel A: Aleatoric vs. Epistemic Uncertainty

**Content:** Diagram explaining two sources of uncertainty: data noise (aleatoric) and model ignorance (epistemic).

**DALL-E Prompt:**
```
Create uncertainty type diagram. Save as: 05-A-fig-vep-uncertainty.svg

Two branches from "Prediction Uncertainty":

LEFT: "Aleatoric (Data)"
- Inherent noise in labels
- Cannot reduce with more model capacity
- Example: "Variant affects function in some contexts"

RIGHT: "Epistemic (Model)"
- Model doesn't know
- Reducible with more data
- Example: "Novel protein family not in training"

Combined annotation: "Total uncertainty = aleatoric + epistemic"

Title: "Sources of Prediction Uncertainty"

Clean conceptual diagram, white background. Professional uncertainty types figure.
```

**Caption for Panel A:**
"Two sources of prediction uncertainty. Aleatoric uncertainty reflects inherent ambiguity in the data—variants that truly have context-dependent effects. Epistemic uncertainty reflects model limitations—lack of training data for novel proteins or variant types. Distinguishing these sources guides whether uncertainty can be reduced through more data or model improvements."

### Panel B: Ensemble Disagreement

**Content:** Visualization of using multiple models or Monte Carlo dropout to estimate uncertainty from prediction variance.

**DALL-E Prompt:**
```
Create ensemble uncertainty visualization. Save as: 05-B-fig-vep-uncertainty.svg

Ensemble prediction visualization:
- Multiple model runs (5 predictions shown)
- Predictions shown as points on number line

LOW UNCERTAINTY case:
- All predictions clustered tightly (e.g., all near 0.8)
- Small variance

HIGH UNCERTAINTY case:
- Predictions spread out (e.g., 0.3 to 0.9)
- Large variance

Formulas:
- Prediction = mean(ensemble)
- Uncertainty = std(ensemble)

Title: "Ensemble Disagreement as Uncertainty"

Clean ensemble comparison, white background. Professional ensemble figure.
```

**Caption for Panel B:**
"Ensemble disagreement quantifies prediction uncertainty. Running multiple model instances (or using Monte Carlo dropout) produces a distribution of predictions. Tight clustering (low variance) indicates confident prediction. Wide spread (high variance) indicates uncertainty. Reporting both prediction and variance enables appropriate downstream use."

### Panel C: Distance-Based Uncertainty

**Content:** UMAP showing training data distribution with test variants at varying distances, uncertainty increasing with distance.

**DALL-E Prompt:**
```
Create distance-based uncertainty visualization. Save as: 05-C-fig-vep-uncertainty.svg

UMAP-style scatter plot:
- Dense cluster: "Training distribution" (blue)
- Test points at varying distances:
  - Close (green): "Low uncertainty"
  - Medium (yellow): "Moderate uncertainty"
  - Far (red): "High uncertainty"

Uncertainty = f(distance to training)

Title: "Distance-Based Uncertainty"
Annotation: "Variants far from training warrant caution"

Clean distance visualization, white background. Professional OOD uncertainty figure.
```

**Caption for Panel C:**
"Distance from training distribution indicates epistemic uncertainty. Variants similar to training examples (green, close) can be predicted confidently. Variants in novel regions of sequence space (red, far) warrant higher uncertainty. Distance-based methods flag out-of-distribution variants that may produce unreliable predictions."

### Panel D: Selective Prediction

**Content:** Diagram showing how uncertainty enables selective prediction—abstaining on high-uncertainty variants.

**DALL-E Prompt:**
```
Create selective prediction diagram. Save as: 05-D-fig-vep-uncertainty.svg

Two-stage flow:

STAGE 1: "All Variants"
- Arrow to model
- Model outputs prediction + uncertainty

STAGE 2: "Triage by Uncertainty"
- Low uncertainty → "Automated interpretation"
- High uncertainty → "Expert review"

Results showing:
- Coverage: 80% automated
- Accuracy on automated: 95%
- 20% sent for review

Title: "Uncertainty-Based Selective Prediction"
Annotation: "Higher accuracy through selective automation"

Clean selective prediction diagram, white background. Professional abstention figure.
```

**Caption for Panel D:**
"Selective prediction improves reliability through abstention. Rather than predicting all variants, the system only provides automated interpretations for low-uncertainty variants (80% of cases). High-uncertainty variants (20%) are routed to expert review. This selective approach achieves higher accuracy on automated predictions (95%) while ensuring difficult cases receive appropriate human attention."

### Combined Caption

**Full Figure Caption:**
"Uncertainty quantification for variant effect prediction. (A) Uncertainty has two sources: aleatoric (inherent data ambiguity) and epistemic (model limitations). (B) Ensemble disagreement provides empirical uncertainty estimates—variance across model runs indicates prediction reliability. (C) Distance from training distribution flags out-of-distribution variants requiring caution. (D) Selective prediction uses uncertainty to abstain on difficult cases, achieving higher accuracy through appropriate routing to expert review. Proper uncertainty quantification enables safe clinical deployment by identifying predictions that should not be trusted."

---

## Figure 17.6: VEP Gains and Gaps (Four-Panel)

**Files:**
- `figs/part_3/ch17/06-A-fig-vep-gains-gaps.svg`
- `figs/part_3/ch17/06-B-fig-vep-gains-gaps.svg`
- `figs/part_3/ch17/06-C-fig-vep-gains-gaps.svg`
- `figs/part_3/ch17/06-D-fig-vep-gains-gaps.svg`

**Priority:** High
**Type:** Impact assessment

### Panel A: Performance by Protein Family

**Content:** Bar chart showing FM-VEP performance varies dramatically by protein family—good for some, poor for others.

### Panel B: Rare Variant Challenge

**Content:** Performance stratified by variant rarity—worse for rarer variants.

### Panel C: Clinical Impact

**Content:** How many VUS could be reclassified using FM predictions.

### Panel D: Remaining Gaps

**Content:** Categories where FM-VEP still fails—complex variants, modifiers, etc.

### Combined DALL-E Prompts and Captions

*(Due to length, abbreviated)*

**Combined Caption:**
"Foundation model VEP: gains and remaining gaps. (A) Performance varies by protein family, with well-characterized families achieving high accuracy while poorly-studied families show degraded performance. (B) Rare variants are harder to predict, particularly for recently evolved or population-specific variants. (C) Clinical impact assessment: FM predictions could reclassify significant fractions of VUS, but require appropriate validation. (D) Remaining gaps include complex variants (multi-allelic, structural), modifier effects, and tissue-specific pathogenicity. FMs have advanced VEP substantially but do not eliminate the need for functional validation."

---

## Figure 17.7: Long-Read VEP

**File:** `figs/part_3/ch17/07-fig-long-read-vep.svg`
**Priority:** Enhancing
**Type:** Emerging application

### Content Description

Diagram showing how long-read sequencing reveals variants invisible to short reads, and how FM models can predict effects of these newly accessible variants (structural variants, repeat expansions, complex haplotypes).

### DALL-E Prompt

```
Create long-read VEP integration diagram. Save as: 07-fig-long-read-vep.svg

Two-row comparison:

TOP ROW "Short-Read Era":
- Short reads → Standard VCF (SNVs, small indels)
- FM-VEP for detected variants
- "Many variants invisible"

BOTTOM ROW "Long-Read Era":
- Long reads → Expanded VCF (SVs, repeats, phased haplotypes)
- FM-VEP needs new approaches
- "New variant classes require new models"

Challenges box:
- "SVs: How to encode insertions/deletions?"
- "Repeats: Dynamic context windows?"
- "Haplotypes: Phase-aware prediction?"

Title: "Long-Read Sequencing Expands VEP Scope"

Clean comparison diagram, white background. Professional emerging application figure.
```

### Caption

**Recommended Caption:**
"Long-read sequencing expands the scope of variant effect prediction. Short-read sequencing (top) detects primarily SNVs and small indels for which current FM-VEP approaches are well-suited. Long-read sequencing (bottom) reveals structural variants, repeat expansions, and complex haplotypes that current models cannot process. Realizing the clinical potential of long-read sequencing requires developing FM-VEP approaches for these new variant classes—a major open challenge."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 17.1 VEP Paradigms | 4 | Essential | Medium (comparison) |
| 17.2 AlphaMissense | 4 | Essential | Medium (architecture + results) |
| 17.3 Multi-Model | 4 | High | Medium (integration) |
| 17.4 Calibration | 4 | High | Medium (clinical) |
| 17.5 Uncertainty | 4 | High | Medium (quantification) |
| 17.6 Gains/Gaps | 4 | High | Medium (assessment) |
| 17.7 Long-Read VEP | 1 | Enhancing | Low (emerging) |

**Total files:** 25
**Recommended generation order:** 17.1A-D (paradigms), 17.2A-D (AlphaMissense), 17.4A-D (calibration), 17.5A-D (uncertainty), 17.3A-D (integration), 17.6A-D (gaps), 17.7 (long-read)
# Figure Report: Chapter 18 - RNA Structure and Function

**Chapter:** p4-ch18-rna.qmd
**Date:** 2026-01-07
**Total Figures:** 5 (12 files)
**Format:** SVG (for scalability)

---

## Figure 1: RNA Energy Landscape Comparison

### Files
- `figs/part_4/ch15/01-A-fig-rna-energy-landscape.svg`
- `figs/part_4/ch15/01-B-fig-rna-energy-landscape.svg`

### Priority
**Essential** - Core concept distinguishing RNA from protein folding

### Content Description
Two-panel comparison of protein versus RNA folding energy landscapes. Panel A shows protein folding with deep funnel topology, clear global minimum, and steep energy barriers. Panel B shows RNA folding with flatter surface, multiple shallow minima at similar energy levels.

### DALL-E Prompt
```
Scientific illustration comparing protein and RNA energy landscapes for a computational biology textbook. Two panels side by side.

LEFT PANEL (Protein): 3D surface plot with classic funnel topology. Deep central well representing the native state. Clear global minimum with steep energy barriers. Smooth gradients descending toward center. Label "Protein Folding" at top. Annotation "Deep minimum - single stable structure" pointing to bottom.

RIGHT PANEL (RNA): 3D surface plot with much flatter topology. Multiple shallow wells at similar heights. Small energy differences between states (< kT). Multiple arrows showing alternative folding pathways. Label "RNA Folding" at top. Annotation "Flat landscape - multiple competing structures."

Clean white background, professional scientific style, blue-purple color gradient for surfaces, clear axis labels (Free Energy on z-axis, Conformational coordinates on x/y). No text watermarks.

Save as: 01-A-fig-rna-energy-landscape.svg (protein panel), 01-B-fig-rna-energy-landscape.svg (RNA panel)
```

### Post-Processing Notes
- Add mathematical notation for energy levels
- Consider adding inset showing riboswitch example
- Ensure color consistency between panels

### Fallback Description
"Energy landscape comparison showing protein folding (left) as a deep funnel with single stable structure versus RNA folding (right) as a flatter surface with multiple competing minima."

### Caption Recommendation
"Energy landscape comparison between protein and RNA folding. (A) Proteins fold into deep energy minima, typically reaching a single stable native structure. (B) RNA energy landscapes are flatter, with multiple conformations competing at similar free energies—explaining why RNA can adopt alternative structures under different conditions."

---

## Figure 2: RNA Secondary Structure Elements

### Files
- `figs/part_4/ch15/02-A-fig-rna-structure-elements.svg`
- `figs/part_4/ch15/02-B-fig-rna-structure-elements.svg`
- `figs/part_4/ch15/02-C-fig-rna-structure-elements.svg`
- `figs/part_4/ch15/02-D-fig-rna-structure-elements.svg`

### Priority
**Essential** - Reference diagram for secondary structure vocabulary

### Content Description
Comprehensive four-panel figure covering RNA secondary structure elements, long-range dependencies, pseudoknots, and notation systems.

### DALL-E Prompt
```
Scientific illustration of RNA secondary structure elements for a molecular biology textbook. Four panels in 2x2 grid.

PANEL A (Basic Elements): Clean diagrams of RNA secondary structure motifs - stem (paired region), hairpin loop, internal loop, bulge, multi-loop junction. Each element clearly labeled with base pairs shown as lines. Color-code: stems in blue, loops in orange.

PANEL B (Long-Range Pairing): Linear RNA sequence (horizontal line ~100nt) with arc diagram above showing base pairs spanning 50-80 nucleotides. Contrast inset showing protein secondary structure spanning only ~10 residues. Annotation "RNA base pairs can span hundreds of nucleotides."

PANEL C (Pseudoknot): Two views - 1) 2D arc notation showing interleaved base pairs that cross each other, 2) Simplified 3D knot representation. Label "Pseudoknot - increases complexity from O(n³) to O(n⁶)". Small telomerase RNA example.

PANEL D (Notation Systems): Same small RNA structure shown in three notations - dot-bracket string (((....))), arc diagram, and 2D graphical representation with circles and lines.

Professional scientific style, clean white background, consistent color scheme throughout. No photo-realistic elements.

Save as: 02-A-fig-rna-structure-elements.svg through 02-D-fig-rna-structure-elements.svg
```

### Post-Processing Notes
- Ensure consistent nucleotide coloring (A=red, U=blue, G=green, C=yellow)
- Add mathematical complexity annotations
- Label each structural element clearly

### Fallback Description
"RNA secondary structure elements including basic motifs (stems, loops, bulges), long-range base pairing patterns, pseudoknot structures with computational complexity implications, and standard notation systems."

### Caption Recommendation
"RNA secondary structure vocabulary. (A) Basic structural elements: stems, hairpin loops, internal loops, bulges, and multi-loop junctions. (B) Long-range base pairing: RNA pairs can span hundreds of nucleotides, unlike protein secondary structure. (C) Pseudoknots: interleaved base pairs that increase prediction complexity from O(n³) to O(n⁶). (D) Common notation systems for representing secondary structure."

---

## Figure 3: RNA vs Protein Language Model Scale Gap

### Files
- `figs/part_4/ch15/03-A-fig-rna-plm-gap.svg`
- `figs/part_4/ch15/03-B-fig-rna-plm-gap.svg`
- `figs/part_4/ch15/03-C-fig-rna-plm-gap.svg`
- `figs/part_4/ch15/03-D-fig-rna-plm-gap.svg`

### Priority
**High** - Key comparison explaining why RNA FMs lag behind

### Content Description
Four-panel comparison showing scale differences between protein and RNA foundation models, explaining the data gap.

### DALL-E Prompt
```
Scientific infographic comparing protein language models to RNA foundation models for computational biology. Four panels.

PANEL A (Scale Comparison Table): Clean comparison table with metrics - Training sequences (Protein: 65M, RNA: ~23M), Structural diversity (Protein: all families, RNA: mainly tRNA/rRNA), Parameters (Protein: 15B, RNA: ~100M), Emergent structure prediction (Protein: yes checkmark, RNA: limited).

PANEL B (Training Data Composition): Two pie charts side by side. Protein pie chart showing diverse family distribution (kinases, GPCRs, enzymes, transporters, etc.). RNA pie chart dominated by two large slices (tRNA, rRNA) with small slivers for other families.

PANEL C (Emergent Capabilities): Comparison chart. Row for "Structure prediction from sequence" - Protein shows green checkmark, RNA shows yellow caution symbol. Row for "Variant effect prediction" - Protein checkmark, RNA partial. Row for "Contact map emergence" - Protein checkmark, RNA X.

PANEL D (The Data Challenge): Bar chart comparing PDB structure counts. Protein bar reaching >200,000. RNA bar tiny at <2,000. Large "100x gap" annotation.

Professional scientific style, clean layout, blue/teal color scheme for protein, orange/coral for RNA. No photo elements.

Save as: 03-A-fig-rna-plm-gap.svg through 03-D-fig-rna-plm-gap.svg
```

### Post-Processing Notes
- Ensure exact numbers match text citations
- Add source annotations
- Make comparison visually striking

### Fallback Description
"Scale comparison between protein and RNA foundation models showing the significant data gap in training sequences, structural diversity, model parameters, and structural annotations available for training."

### Caption Recommendation
"The scale gap between protein and RNA foundation models. (A) Key metrics comparison showing protein models train on 3× more sequences with much greater diversity. (B) Training data composition: protein data span diverse families while RNA databases are dominated by well-characterized classes. (C) Emergent capabilities comparison showing protein models achieve structure prediction that RNA models lack. (D) The fundamental data challenge: fewer than 2,000 RNA structures versus over 200,000 protein structures in the PDB."

---

## Figure 4: Codon-Level Tokenization

### Files
- `figs/part_4/ch15/04-A-fig-codon-tokenization.svg`
- `figs/part_4/ch15/04-B-fig-codon-tokenization.svg`
- `figs/part_4/ch15/04-C-fig-codon-tokenization.svg`
- `figs/part_4/ch15/04-D-fig-codon-tokenization.svg`

### Priority
**High** - Important for understanding mRNA design applications

### Content Description
Four-panel figure explaining codon-level modeling: synonymous codon choices, what codon selection affects, tokenization comparison, and model capability differences.

### DALL-E Prompt
```
Scientific illustration of codon-level modeling for mRNA for computational biology textbook. Four panels.

PANEL A (Same Protein, Different mRNA): Single amino acid sequence at top (e.g., "Met-Ala-Ser-Gly..."). Below it, three different mRNA sequences encoding the same protein with different codon choices highlighted (e.g., GCU vs GCC vs GCA for Alanine). Annotation "Synonymous codons - same protein, different mRNA properties."

PANEL B (What Codon Choice Affects): Central codon diagram with four arrows pointing to effects: 1) tRNA availability (molecule icon), 2) Translation speed (ribosome icon), 3) mRNA secondary structure (hairpin), 4) Stability/GC content (thermometer). Clean icons for each.

PANEL C (Tokenization Comparison): Side-by-side comparison for 300 amino acid protein. Left: character-level showing "900 nucleotide tokens". Right: codon-level showing "300 codon tokens". Arrow between them labeled "Encodes biological prior."

PANEL D (Model Capabilities): Three-column comparison. Protein LM sees only amino acids (amino acid symbols). DNA LM sees nucleotides without boundaries (ACGT stream). Codon LM sees both codon boundaries and amino acid mapping (grouped triplets with AA labels).

Clean scientific illustration style, professional color palette, white background. No photorealistic elements.

Save as: 04-A-fig-codon-tokenization.svg through 04-D-fig-codon-tokenization.svg
```

### Post-Processing Notes
- Use consistent genetic code colors
- Add chemical structure hints for codons
- Ensure clear visual hierarchy

### Fallback Description
"Codon-level modeling showing how synonymous codons encode the same protein but affect mRNA properties, the biological effects of codon choice, tokenization strategies, and what different model types can capture."

### Caption Recommendation
"Codon-level modeling of mRNA. (A) Multiple mRNA sequences can encode the same protein through synonymous codon choices. (B) Codon selection affects tRNA availability, translation speed, mRNA structure, and stability. (C) Codon tokenization reduces sequence length while encoding biological priors about translation units. (D) Comparison of what protein, DNA, and codon language models can capture from coding sequences."

---

## Figure 5: mRNA Design Pipeline

### Files
- `figs/part_4/ch15/05-fig-mrna-design-pipeline.svg`

### Priority
**High** - Synthesis of mRNA therapeutics design process

### Content Description
End-to-end pipeline for therapeutic mRNA design, from target protein through optimization stages to final construct.

### DALL-E Prompt
```
Scientific pipeline diagram for therapeutic mRNA design for a computational biology textbook.

Horizontal flow from left to right with 5 stages:

STAGE 1 (Target Protein): Icon of 3D protein structure. Label "Desired protein sequence and structural requirements."

STAGE 2 (Codon Optimization): Branching diagram showing ~3^300 possible sequences narrowing to selected candidates. Three sub-objectives listed: expression, stability, immunogenicity. Icon of model scoring.

STAGE 3 (5' UTR Design): Hairpin structure diagram with labels for Kozak sequence, secondary structure considerations, uORF avoidance. Translation initiation annotation.

STAGE 4 (3' UTR Design): Linear diagram showing stability elements, miRNA binding site avoidance, poly-A tail. Half-life optimization annotation.

STAGE 5 (Modification Selection): Chemical structure hint for N1-methylpseudouridine. Immune evasion annotation.

OUTPUT: Complete mRNA construct diagram showing all components assembled.

INSET BOX: "COVID-19 vaccine design choices" with small icons for key decisions made.

Professional scientific illustration, clean flowchart style, blue/green color gradient, white background.

Save as: 05-fig-mrna-design-pipeline.svg
```

### Post-Processing Notes
- Add mathematical notation for sequence space size
- Include specific nucleotide modifications
- Add references to COVID-19 vaccine elements

### Fallback Description
"End-to-end mRNA therapeutic design pipeline showing progression from target protein specification through codon optimization, UTR design, and modification selection to final optimized construct."

### Caption Recommendation
"Therapeutic mRNA design pipeline. Starting from a target protein, the design process optimizes codon usage (selecting from ~3^300 possible synonymous sequences), engineers 5' UTR elements for translation initiation, designs 3' UTR for stability and localization, and selects chemical modifications (such as N1-methylpseudouridine) to reduce immunogenicity. Inset shows key design choices made for COVID-19 mRNA vaccines."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| RNA Energy Landscape | 2 | Essential | Medium |
| Structure Elements | 4 | Essential | High |
| RNA-PLM Scale Gap | 4 | High | Medium |
| Codon Tokenization | 4 | High | Medium |
| mRNA Design Pipeline | 1 | High | High |

## Recommended Generation Order
1. Structure Elements (foundation vocabulary)
2. RNA Energy Landscape (core concept)
3. Codon Tokenization (therapeutics application)
4. mRNA Design Pipeline (synthesis)
5. RNA-PLM Scale Gap (context)
# Figure Report: Chapter 19 - Single-Cell Models

**Chapter:** p4-ch19-single-cell.qmd
**Date:** 2026-01-07
**Total Figures:** 5 (20 files)
**Format:** SVG (for scalability)

---

## Figure 1: Cellular Language Model Analogy

### Files
- `figs/part_4/ch16/01-A-fig-cellular-lm-analogy.svg`
- `figs/part_4/ch16/01-B-fig-cellular-lm-analogy.svg`
- `figs/part_4/ch16/01-C-fig-cellular-lm-analogy.svg`
- `figs/part_4/ch16/01-D-fig-cellular-lm-analogy.svg`

### Priority
**Essential** - Core conceptual framework for the chapter

### Content Description
Visual analogy between natural language models and cellular language models, showing the parallel between words/sentences and genes/cells.

### DALL-E Prompt
```
Scientific illustration comparing natural language models to cellular language models for computational biology textbook. Four panels in 2x2 grid.

PANEL A (Language Model): Sentence "The cat sat on the mat" with words as colored boxes (tokens). Grammar rules annotation. BERT-style architecture icon predicting masked word "[MASK]". Clean NLP diagram style.

PANEL B (Cellular Language Model): Cell diagram with gene expression profile represented as sequence of gene symbols (colored boxes representing different genes). ~20,000 gene vocabulary annotation. Geneformer/scGPT icon predicting masked genes. Regulatory programs as "grammar."

PANEL C (Parallel Structure Table): Clean comparison table:
- NLP → Single-Cell
- Word → Gene
- Sentence → Cell expression profile
- Grammar → Regulatory programs
- Vocabulary (~50k) → Gene set (~20k)
- Document corpus → Cell atlas
- Masked word prediction → Masked gene prediction

PANEL D (What Models Learn): Two columns. Language column: syntax icon, semantics icon, context icon. Cellular column: co-expression modules icon, cell type programs icon, perturbation effects icon.

Professional scientific illustration, clean white background, consistent color scheme (blue for NLP, green for biology), educational diagram style.

Save as: 01-A-fig-cellular-lm-analogy.svg through 01-D-fig-cellular-lm-analogy.svg
```

### Post-Processing Notes
- Ensure terminology matches chapter vocabulary
- Add specific gene examples (MYC, TP53, etc.)
- Color-code cell type programs

### Fallback Description
"Visual analogy showing how natural language concepts (words, sentences, grammar) map to single-cell biology (genes, cells, regulatory programs), with both domains using transformer architectures and masked prediction objectives."

### Caption Recommendation
"The cell-as-document analogy. (A) Language models treat sentences as sequences of word tokens, learning grammar through masked prediction. (B) Cellular language models treat cells as sequences of gene tokens, learning regulatory programs through masked gene prediction. (C) Parallel structure between NLP and single-cell domains. (D) Comparison of what each model type learns: language models capture syntax and semantics while cellular models capture co-expression and cell type programs."

---

## Figure 2: Single-Cell Data Challenges

### Files
- `figs/part_4/ch16/02-A-fig-single-cell-challenges.svg`
- `figs/part_4/ch16/02-B-fig-single-cell-challenges.svg`
- `figs/part_4/ch16/02-C-fig-single-cell-challenges.svg`
- `figs/part_4/ch16/02-D-fig-single-cell-challenges.svg`

### Priority
**Essential** - Critical context for model design decisions

### Content Description
Technical challenges in single-cell data: dropout/sparsity, batch effects, dynamic range, and how foundation models address these.

### DALL-E Prompt
```
Scientific illustration of single-cell RNA-seq data challenges for computational biology textbook. Four panels.

PANEL A (Dropout/Sparsity): Heat map visualization of gene × cell matrix. Most cells showing zeros (white/light). Only ~10% colored (detected expression). Annotation "90%+ zeros - but zero can mean silent OR undetected." Highlight specific examples of dropout.

PANEL B (Batch Effects): Two UMAP scatter plots side by side. Left plot: cells colored by cell type showing mixed/interleaved clusters. Right plot: same cells colored by batch showing distinct separated clusters. Annotation "Technical variation can exceed biological variation."

PANEL C (Dynamic Range): Histogram showing gene expression distribution spanning 5+ orders of magnitude. X-axis from 0 to 10,000+ counts. Few genes at high expression (housekeeping), long tail at low expression. Annotation showing "Few copies" for TFs and "Thousands of copies" for housekeeping.

PANEL D (Foundation Model Solutions): Three solution icons with labels: 1) Rank-based encoding handles dynamic range (ranking icon), 2) Large corpus learns robust patterns despite noise (database icon), 3) Contrastive objectives for batch-invariance (contrast icon).

Clean scientific style, white background, consistent color palette, no photorealistic elements.

Save as: 02-A-fig-single-cell-challenges.svg through 02-D-fig-single-cell-challenges.svg
```

### Post-Processing Notes
- Use realistic sparsity percentages (90%+)
- Show actual batch clustering patterns
- Include specific gene examples

### Fallback Description
"Single-cell data challenges: extreme sparsity with 90%+ zeros, batch effects that can exceed biological variation, dynamic range spanning orders of magnitude, and foundation model strategies to address each challenge."

### Caption Recommendation
"Technical challenges in single-cell data. (A) Dropout and sparsity: over 90% of values are zero, but zeros may indicate true absence or technical failure to detect. (B) Batch effects: cells often cluster by experimental batch rather than biological type. (C) Dynamic range: expression spans orders of magnitude from rare transcription factors to abundant housekeeping genes. (D) Foundation model strategies for addressing these challenges: rank-based encoding, large-scale pretraining, and contrastive objectives."

---

## Figure 3: Geneformer Architecture and Innovations

### Files
- `figs/part_4/ch16/03-A-fig-geneformer-architecture.svg`
- `figs/part_4/ch16/03-B-fig-geneformer-architecture.svg`
- `figs/part_4/ch16/03-C-fig-geneformer-architecture.svg`
- `figs/part_4/ch16/03-D-fig-geneformer-architecture.svg`

### Priority
**High** - Key model architecture example

### Content Description
Four-panel figure showing Geneformer's rank-based encoding, architecture, emergent network learning, and transfer applications.

### DALL-E Prompt
```
Scientific illustration of Geneformer single-cell foundation model for computational biology textbook. Four panels.

PANEL A (Rank-Based Encoding): Flow diagram. Left: raw expression counts table (gene vs value). Middle: ranks relative to corpus baseline (gene vs ratio). Right: ranked token sequence. Arrow flow showing transformation. Annotation "Highlights unusually active/silent genes, not absolute abundance."

PANEL B (Architecture): Clean neural network diagram. Input: ranked gene sequence as tokens. Middle: transformer encoder blocks (BERT-style, 6-12 layers). Output arrows to: masked gene prediction loss, gene embeddings, cell embeddings. Labels for each component.

PANEL C (What Attention Learns): Network diagram with genes as nodes and attention weights as edges. Some edges thick (high attention), others thin. Overlay showing correspondence to known regulatory relationships. Annotation "Network hierarchy emerges without explicit supervision."

PANEL D (Transfer Applications): Three application icons: 1) Cell type annotation (clustering icon), 2) Therapeutic target ID (drug molecule icon), 3) Disease gene prioritization (gene ranking icon). Arrow from pretrained model to each application.

Professional scientific illustration, clean white background, blue/teal color scheme, educational diagram style.

Save as: 03-A-fig-geneformer-architecture.svg through 03-D-fig-geneformer-architecture.svg
```

### Post-Processing Notes
- Add specific gene examples in rank encoding
- Show actual attention matrix pattern
- Include performance metrics where available

### Fallback Description
"Geneformer architecture: rank-based encoding transforms expression to gene ranks, transformer encoder learns from masked gene prediction, attention patterns capture regulatory network structure, and pretrained model transfers to multiple downstream applications."

### Caption Recommendation
"Geneformer innovations. (A) Rank-based encoding transforms raw counts into ranks relative to corpus baseline, emphasizing what is unusual about each cell rather than absolute abundance. (B) Transformer encoder architecture using BERT-style masked prediction produces gene and cell embeddings. (C) Attention weights learned during pretraining correspond to regulatory network relationships without explicit network supervision. (D) Transfer applications including cell type annotation, therapeutic target identification, and disease gene prioritization."

---

## Figure 4: Perturbation Response Prediction

### Files
- `figs/part_4/ch16/04-A-fig-perturbation-prediction.svg`
- `figs/part_4/ch16/04-B-fig-perturbation-prediction.svg`
- `figs/part_4/ch16/04-C-fig-perturbation-prediction.svg`
- `figs/part_4/ch16/04-D-fig-perturbation-prediction.svg`

### Priority
**High** - Important application with critical limitations

### Content Description
Perturbation prediction task: the prediction problem, training data from Perturb-seq, what models must learn, and current performance limitations.

### DALL-E Prompt
```
Scientific illustration of perturbation response prediction in single-cell models. Four panels.

PANEL A (The Task): Flow diagram. Left: unperturbed cell with expression profile. Plus sign. Perturbation identity (e.g., "KO Gene X"). Arrow. Right: predicted post-perturbation expression profile. Comparison arrow to actual Perturb-seq measurement.

PANEL B (Training Data): CRISPR-Perturb-seq schematic. Left: CRISPR library targeting thousands of genes. Right: single-cell readout matrix (cells × genes). Annotation "Supervised signal from experimental perturbations." Scale: thousands of genes × thousands of cells.

PANEL C (What Models Must Learn): Three concept diagrams. 1) Directional relationships: "A activates B" with arrow, "KO A → B decreases." 2) Network cascades: chain of genes showing secondary effects. 3) Context dependence: same perturbation, different cell types, different outcomes.

PANEL D (Current Performance): Performance chart or scatter plot. X-axis: gene characterization level. Y-axis: prediction accuracy. Strong correlation for well-characterized genes (left, high accuracy). Weak for poorly characterized (right, low accuracy). Annotation "Predictions most accurate where we need them least."

Clean scientific illustration, white background, informative data visualization style.

Save as: 04-A-fig-perturbation-prediction.svg through 04-D-fig-perturbation-prediction.svg
```

### Post-Processing Notes
- Add specific gene knockout examples
- Show realistic accuracy ranges
- Emphasize the limitation clearly

### Fallback Description
"Perturbation prediction workflow showing how models predict expression changes from perturbation identity, the Perturb-seq training data source, required model capabilities (directionality, cascades, context), and the limitation that predictions are most accurate for already well-characterized genes."

### Caption Recommendation
"Perturbation response prediction. (A) The prediction task: given unperturbed cell state and perturbation identity, predict post-perturbation expression profile. (B) Training data from Perturb-seq provides supervised signal across thousands of gene knockouts. (C) What models must learn: directional regulatory relationships, network cascade effects, and cell-type-specific responses. (D) Current limitation: prediction accuracy correlates with gene characterization level—models perform best on well-studied genes where predictions are least needed."

---

## Figure 5: GLUE Multi-Omics Integration Architecture

### Files
- `figs/part_4/ch16/05-A-fig-glue-architecture.svg`
- `figs/part_4/ch16/05-B-fig-glue-architecture.svg`
- `figs/part_4/ch16/05-C-fig-glue-architecture.svg`
- `figs/part_4/ch16/05-D-fig-glue-architecture.svg`

### Priority
**High** - Key integration method

### Content Description
GLUE architecture for unpaired multi-omics integration: the integration problem, architecture components, feature graph as biological prior, and applications.

### DALL-E Prompt
```
Scientific illustration of GLUE multi-omics integration architecture for computational biology. Four panels.

PANEL A (Unpaired Integration Problem): Schematic showing RNA-seq data from cells A,B,C (one color). ATAC-seq data from different cells D,E,F (different color). Arrows pointing to question "How to integrate when measured in different cells?" Goal: unified embedding.

PANEL B (GLUE Architecture): Neural network diagram. Two parallel VAE encoders (one for RNA, one for ATAC). Both feed into shared latent space (middle circle). Adversarial discriminator attached to latent space. Decoders reconstructing original modalities.

PANEL C (Feature Graph as Prior): Bipartite-style graph with two node types: genes (circles) and ATAC peaks (squares). Edges connecting genes to nearby peaks, TF binding sites to target genes. Annotation "Biological knowledge constrains alignment." Graph VAE learning embeddings.

PANEL D (Applications): Three application panels: 1) Cross-modal prediction (RNA → ATAC or reverse), 2) Regulatory inference (gene-peak links), 3) Triple-omics integration (RNA + ATAC + methylation).

Professional scientific illustration, clean white background, distinct colors for each modality, network diagram style.

Save as: 05-A-fig-glue-architecture.svg through 05-D-fig-glue-architecture.svg
```

### Post-Processing Notes
- Use consistent modality colors throughout
- Show specific gene-peak relationships
- Add mathematical notation for losses

### Fallback Description
"GLUE multi-omics integration: the unpaired integration challenge when modalities are measured in different cells, the VAE-based architecture with adversarial alignment, the feature graph encoding biological prior knowledge, and downstream applications including cross-modal prediction and regulatory inference."

### Caption Recommendation
"GLUE (Graph-Linked Unified Embedding) for multi-omics integration. (A) The unpaired integration problem: RNA-seq and ATAC-seq measured in different cells must be aligned into a unified embedding. (B) Architecture: modality-specific VAE encoders feed into a shared latent space with adversarial alignment. (C) Feature graph encodes biological prior knowledge linking genes to regulatory peaks, constraining alignment to biologically plausible solutions. (D) Applications: cross-modal prediction, regulatory inference, and integration of three or more modalities."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Cellular LM Analogy | 4 | Essential | Medium |
| Data Challenges | 4 | Essential | Medium |
| Geneformer Architecture | 4 | High | High |
| Perturbation Prediction | 4 | High | Medium |
| GLUE Architecture | 4 | High | High |

## Recommended Generation Order
1. Cellular LM Analogy (conceptual foundation)
2. Data Challenges (technical context)
3. Geneformer Architecture (model example)
4. GLUE Architecture (integration method)
5. Perturbation Prediction (application + limitations)
# Figure Report: Chapter 20 - 3D Genome Organization

**Chapter:** p4-ch20-3d-genome.qmd
**Date:** 2026-01-07
**Total Figures:** 5 (20 files)
**Format:** SVG (for scalability)

---

## Figure 1: TAD Boundary Disruption Clinical Example

### Files
- `figs/part_4/ch17/01-A-fig-tad-disruption.svg`
- `figs/part_4/ch17/01-B-fig-tad-disruption.svg`
- `figs/part_4/ch17/01-C-fig-tad-disruption.svg`
- `figs/part_4/ch17/01-D-fig-tad-disruption.svg`

### Priority
**High** - Clinical motivation for the chapter

### Content Description
Four-panel figure showing the EPHA4/WNT6 TAD boundary disruption case: normal configuration, boundary deletion, pathogenic outcome, and interpretation implications.

### DALL-E Prompt
```
Scientific illustration of TAD boundary disruption causing limb malformation for clinical genetics textbook. Four panels.

PANEL A (Normal Configuration): Schematic showing two adjacent TADs as triangular domains. Left TAD contains EPHA4 gene and limb enhancers. Right TAD contains WNT6 and PAX3 genes. Clear boundary between them (vertical line with CTCF symbols). Arrows showing enhancers → EPHA4. Annotation "Enhancers contact EPHA4, not WNT6."

PANEL B (Boundary Deletion): Same region but boundary removed (gap in line). TADs merging. Enhancers now with bidirectional arrows reaching both EPHA4 and WNT6. Visual showing domain fusion.

PANEL C (Pathogenic Outcome): WNT6 gene highlighted red (ectopically activated). Hand/limb icon showing brachydactyly (shortened fingers). Expression graph showing WNT6 abnormally high in limb tissue.

PANEL D (Interpretation Implications): Two deletions of same size shown. One preserves boundary → benign annotation. One disrupts boundary → pathogenic annotation. Key insight: "Current VEP tools miss 3D effects."

Clean scientific illustration, white background, chromosomal region style, clinical genetics visualization.

Save as: 01-A-fig-tad-disruption.svg through 01-D-fig-tad-disruption.svg
```

### Post-Processing Notes
- Use accurate gene names and positions
- Show actual deletion coordinates if available
- Add Hi-C triangular domain visualization

### Fallback Description
"TAD boundary disruption at the EPHA4/WNT6 locus showing normal configuration with insulated domains, boundary deletion causing domain merger, enhancer hijacking activating WNT6 ectopically causing brachydactyly, and the critical insight that same-sized deletions have different outcomes depending on boundary effects."

### Caption Recommendation
"Clinical consequences of TAD boundary disruption. (A) Normal configuration: limb enhancers activate *EPHA4* within their TAD while the boundary insulates *WNT6* in the adjacent domain. (B) Boundary deletion allows TAD merger and new enhancer-gene contacts. (C) Pathogenic outcome: limb enhancers ectopically activate *WNT6*, causing brachydactyly. (D) Clinical interpretation: same-sized deletions may be pathogenic or benign depending on whether they disrupt domain boundaries—an effect current VEP tools cannot predict."

---

## Figure 2: Chromatin Organization Hierarchy

### Files
- `figs/part_4/ch17/02-A-fig-chromatin-hierarchy.svg`
- `figs/part_4/ch17/02-B-fig-chromatin-hierarchy.svg`
- `figs/part_4/ch17/02-C-fig-chromatin-hierarchy.svg`
- `figs/part_4/ch17/02-D-fig-chromatin-hierarchy.svg`

### Priority
**Essential** - Core conceptual framework

### Content Description
Four-level visualization of chromatin organization from chromosome territories to fine-scale loops.

### DALL-E Prompt
```
Scientific illustration of chromatin organization hierarchy for computational genomics textbook. Four panels showing different scales.

PANEL A (Chromosome Territories - Nuclear Scale): Cross-section of nucleus with distinct colored territories for different chromosomes. Gene-rich chromosomes toward interior (brighter colors). Gene-poor at periphery (darker, near lamina). Nuclear envelope clearly visible. Scale bar indicating ~10 μm.

PANEL B (A/B Compartments - Megabase Scale): Hi-C contact matrix showing characteristic checkerboard pattern. A compartments (active, euchromatin) in one color. B compartments (inactive, heterochromatin) in contrasting color. Annotation showing 1-10 Mb scale. Side diagram showing A toward interior, B at lamina.

PANEL C (TADs - Sub-Megabase Scale): Hi-C matrix diagonal with clear triangular domains. Sharp boundaries visible. Annotation "Median ~800 kb." CTCF binding site symbols at boundaries. Color intensity showing enriched within-TAD contacts.

PANEL D (Loops - Kilobase Scale): Fine Hi-C detail showing focal off-diagonal enrichments (dots/peaks). Diagram showing enhancer-promoter loop and CTCF-CTCF structural loop. Scale 10-500 kb annotation.

Professional scientific illustration, consistent color scheme across scales, white background, appropriate Hi-C visualization style.

Save as: 02-A-fig-chromatin-hierarchy.svg through 02-D-fig-chromatin-hierarchy.svg
```

### Post-Processing Notes
- Ensure scales are accurate
- Use standard Hi-C color schemes (red/blue)
- Add genomic coordinate annotations

### Fallback Description
"Chromatin organization hierarchy: chromosome territories at nuclear scale with gene-rich regions toward interior, A/B compartments visible as Hi-C checkerboard pattern at megabase scale, TADs as triangular domains at sub-megabase scale, and fine-scale loops including enhancer-promoter contacts at kilobase resolution."

### Caption Recommendation
"Hierarchical organization of the 3D genome. (A) Chromosome territories: each chromosome occupies a distinct nuclear volume with gene-rich chromosomes toward the interior. (B) A/B compartments: active (A) and inactive (B) chromatin form a checkerboard pattern visible at megabase scale. (C) TADs: topologically associating domains appear as triangular enrichments in Hi-C with a median size of ~800 kb. (D) Chromatin loops: focal Hi-C enrichments represent enhancer-promoter contacts and CTCF-anchored structural loops."

---

## Figure 3: Loop Extrusion Mechanism

### Files
- `figs/part_4/ch17/03-A-fig-loop-extrusion.svg`
- `figs/part_4/ch17/03-B-fig-loop-extrusion.svg`
- `figs/part_4/ch17/03-C-fig-loop-extrusion.svg`
- `figs/part_4/ch17/03-D-fig-loop-extrusion.svg`

### Priority
**Essential** - Mechanistic foundation for predictions

### Content Description
Step-by-step illustration of the loop extrusion mechanism showing cohesin loading, bidirectional extrusion, CTCF arrest, and the orientation rule.

### DALL-E Prompt
```
Scientific illustration of chromatin loop extrusion mechanism for molecular biology textbook. Four sequential panels.

PANEL A (Cohesin Loading): Linear DNA fiber with cohesin ring loading onto it. Ring structure clearly visible embracing the DNA. Initial state with no loop formed. Time marker "t=0."

PANEL B (Bidirectional Extrusion): Cohesin extruding DNA through the ring, creating progressively larger loop. Show intermediate states with loop growing. Arrows indicating bidirectional motion. DNA feeding through cohesin. Time progression.

PANEL C (CTCF Arrest): Cohesin encountering CTCF proteins bound to DNA in convergent orientation (facing each other). Extrusion halted. Stable loop formed with CTCF sites at anchors. Labels for CTCF binding motifs.

PANEL D (The Orientation Rule): Four scenarios shown:
1) Convergent → ← : "Loop anchors ✓" (stable loop)
2) Divergent ← → : "No stable loop ✗"
3) Tandem → → : "Extrusion continues"
4) Tandem ← ← : "Extrusion continues"
Annotation box: "CTCF orientation predicts loop formation."

Clean molecular biology illustration style, white background, DNA as double helix or simplified fiber, proteins as distinct shapes.

Save as: 03-A-fig-loop-extrusion.svg through 03-D-fig-loop-extrusion.svg
```

### Post-Processing Notes
- Ensure cohesin ring structure is accurate
- Add time annotations
- Include cohesin degradation experiment reference

### Fallback Description
"Loop extrusion mechanism: cohesin loading onto chromatin, bidirectional DNA extrusion enlarging the loop, extrusion arrest upon encountering convergent CTCF sites, and the orientation rule showing that only convergent CTCF pairs form stable loop anchors."

### Caption Recommendation
"The loop extrusion mechanism. (A) Cohesin loads onto chromatin as a ring complex. (B) Bidirectional extrusion progressively enlarges the DNA loop. (C) Extrusion halts when cohesin encounters convergent CTCF sites, forming stable loop anchors. (D) The orientation rule: only convergent CTCF pairs (→←) form stable loops; divergent (←→) and tandem (→→) orientations do not halt extrusion."

---

## Figure 4: 3D Structure Prediction Models

### Files
- `figs/part_4/ch17/04-A-fig-3d-models.svg`
- `figs/part_4/ch17/04-B-fig-models.svg`
- `figs/part_4/ch17/04-C-fig-3d-models.svg`
- `figs/part_4/ch17/04-D-fig-3d-models.svg`

### Priority
**High** - Core computational methods

### Content Description
Comparison of Akita, Orca, and C.Origami model architectures and outputs.

### DALL-E Prompt
```
Scientific illustration comparing 3D genome structure prediction models for computational genomics. Four panels.

PANEL A (Akita Architecture): Flow diagram. Input: ~1 Mb DNA sequence (horizontal bar with nucleotides). Architecture: dilated convolution stack (expanding receptive field visualization). Output: 2 kb resolution Hi-C prediction (triangular heat map). Key labels for each component.

PANEL B (Orca Multi-Scale): Hierarchical diagram. Input sequence at top. Multiple parallel branches predicting different resolutions (4 kb, 16 kb, 64 kb, 256 kb). Outputs shown as nested triangular matrices at different scales. Annotation "Multi-scale prediction captures TADs and compartments."

PANEL C (C.Origami with CTCF): Flow diagram showing two inputs: DNA sequence AND CTCF ChIP-seq data (binding peaks). Both feed into model. Output: cell-type-specific Hi-C prediction. Annotation "Enables cross-cell-type transfer."

PANEL D (Prediction vs Ground Truth): Side-by-side Hi-C matrices. Left: predicted contact map. Right: experimental Hi-C. Similar triangular domains and loops visible in both. Correlation annotation (~0.6-0.8). Key features labeled: TAD boundaries, loop anchors.

Professional scientific illustration, neural network diagram style, white background, consistent color scheme.

Save as: 04-A-fig-3d-models.svg through 04-D-fig-3d-models.svg
```

### Post-Processing Notes
- Add specific architectural details (layer counts, etc.)
- Include correlation metrics
- Show specific genomic region example

### Fallback Description
"3D structure prediction models: Akita using dilated convolutions for 2kb resolution, Orca providing multi-scale predictions from fine to coarse resolution, C.Origami incorporating CTCF ChIP-seq for cell-type-specific transfer, and example comparison showing predicted versus experimental Hi-C with high correspondence."

### Caption Recommendation
"Sequence-based 3D structure prediction models. (A) *Akita* architecture: dilated convolutions expand the receptive field to process ~1 Mb sequences and predict Hi-C at 2 kb resolution. (B) *Orca* multi-scale approach: parallel pathways predict contacts from 4 kb to 256 kb resolution simultaneously. (C) *C.Origami* incorporates CTCF ChIP-seq alongside sequence, enabling cross-cell-type transfer. (D) Prediction versus ground truth comparison showing that sequence-based models capture TAD boundaries and major loop anchors with correlations of 0.6-0.8."

---

## Figure 5: Spatial Transcriptomics Overview

### Files
- `figs/part_4/ch17/05-A-fig-spatial-transcriptomics.svg`
- `figs/part_4/ch17/05-B-fig-spatial-transcriptomics.svg`
- `figs/part_4/ch17/05-C-fig-spatial-transcriptomics.svg`
- `figs/part_4/ch17/05-D-fig-spatial-transcriptomics.svg`

### Priority
**Enhancing** - Extending concepts to spatial context

### Content Description
Spatial transcriptomics technologies and foundation models: spot-based methods, imaging-based methods, deconvolution challenge, and spatial foundation models.

### DALL-E Prompt
```
Scientific illustration of spatial transcriptomics technologies and computational methods. Four panels.

PANEL A (Visium Spot-Based): Tissue section with grid of spots overlaid. Each spot ~55 μm diameter. Annotation "1-10 cells per spot." Inset showing that each spot captures transcriptome-wide but multi-cell averaged signal. 10x Genomics platform indication.

PANEL B (Imaging-Based MERFISH/Xenium): Same tissue section but with single-cell resolution dots. Different colors representing different genes detected. Annotation "Subcellular resolution" and "Limited gene panel (100-1000s)." Individual cells clearly distinguished.

PANEL C (Deconvolution Challenge): Single Visium spot enlarged. Multiple cell types inside (different colors). Reference scRNA-seq atlas on side. Algorithm arrow: "Infer composition from reference." Output: pie chart showing cell type proportions within spot.

PANEL D (Spatial Foundation Models): Graph representation of tissue. Nodes = cells/spots. Edges = spatial proximity or ligand-receptor communication. GNN architecture processing the graph. Examples listed: Nicheformer, SpaGCN, GraphST. Annotation "Cell-cell communication and tissue context."

Professional scientific illustration, tissue histology style for tissue sections, network diagram for models, white background.

Save as: 05-A-fig-spatial-transcriptomics.svg through 05-D-fig-spatial-transcriptomics.svg
```

### Post-Processing Notes
- Use realistic tissue morphology
- Show actual resolution scales
- Add platform-specific details

### Fallback Description
"Spatial transcriptomics overview: Visium spot-based methods with ~55μm multi-cell spots, imaging-based methods like MERFISH achieving single-cell resolution with limited genes, the deconvolution challenge of inferring cell type composition, and spatial foundation models using graph neural networks over tissue architecture."

### Caption Recommendation
"Spatial transcriptomics technologies and computational approaches. (A) Spot-based methods (Visium): transcriptome-wide measurement at ~55 μm resolution, capturing 1-10 cells per spot. (B) Imaging-based methods (MERFISH, Xenium): subcellular resolution but limited to pre-selected gene panels. (C) The deconvolution challenge: inferring cell type composition within each spot using single-cell reference atlases. (D) Spatial foundation models: graph neural networks over spatial tissue graphs enable modeling of cell-cell communication and tissue microenvironment."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| TAD Disruption | 4 | High | Medium |
| Chromatin Hierarchy | 4 | Essential | High |
| Loop Extrusion | 4 | Essential | Medium |
| 3D Prediction Models | 4 | High | High |
| Spatial Transcriptomics | 4 | Enhancing | Medium |

## Recommended Generation Order
1. Loop Extrusion (mechanistic foundation)
2. Chromatin Hierarchy (organizational levels)
3. TAD Disruption (clinical relevance)
4. 3D Prediction Models (computational methods)
5. Spatial Transcriptomics (extension)
# Figure Report: Chapter 21 - Graph and Network Models

**Chapter:** p4-ch21-networks.qmd
**Date:** 2026-01-07
**Total Figures:** 6 (21 files)
**Format:** SVG (for scalability)

---

## Figure 1: Biological Network Landscape

### Files
- `figs/part_4/ch18/01-A-fig-biological-networks.svg`
- `figs/part_4/ch18/01-B-fig-biological-networks.svg`
- `figs/part_4/ch18/01-C-fig-biological-networks.svg`
- `figs/part_4/ch18/01-D-fig-biological-networks.svg`

### Priority
**Essential** - Foundation for understanding network types

### Content Description
Overview of biological network types: PPI networks, gene regulatory networks, knowledge graphs, and spatial/cell-cell interaction graphs.

### DALL-E Prompt
```
Scientific illustration of different biological network types for computational biology textbook. Four panels showing distinct network structures.

PANEL A (PPI Networks): Undirected graph with protein nodes (circles with protein names like TP53, BRCA1). Edges representing physical binding. Varying node sizes by degree. Labels for databases: STRING, BioGRID, IntAct. Annotation "20-30% of interactions catalogued."

PANEL B (Gene Regulatory Networks): Directed graph with TF nodes (hexagons) and target gene nodes (circles). Arrows showing activation (green) and repression (red). Some TFs regulating multiple targets. Annotation "Cell-type specific from ChIP-seq, ATAC-seq."

PANEL C (Knowledge Graphs): Heterogeneous graph with multiple node types distinguished by shape/color: genes (circles), diseases (diamonds), drugs (squares), pathways (rectangles). Multiple edge types shown with different line styles. Hetionet example with node/edge counts. Annotation "Multi-hop reasoning."

PANEL D (Spatial Graphs): Tissue section background with cells as nodes. Edges connecting spatially adjacent cells. Different cell types in different colors. Annotation "Emerging from spatial transcriptomics." Ligand-receptor communication edges indicated.

Professional scientific illustration, network diagram style, white background, distinct visual identity for each network type.

Save as: 01-A-fig-biological-networks.svg through 01-D-fig-biological-networks.svg
```

### Post-Processing Notes
- Include specific database statistics
- Add edge type legends
- Use consistent node styling per network type

### Fallback Description
"Biological network landscape showing protein-protein interaction networks (undirected physical binding), gene regulatory networks (directed TF-target relationships), knowledge graphs (heterogeneous multi-type nodes and edges), and spatial graphs (cell proximity from spatial transcriptomics)."

### Caption Recommendation
"Landscape of biological networks. (A) Protein-protein interaction networks: undirected edges represent physical binding, with only 20-30% of interactions currently catalogued. (B) Gene regulatory networks: directed edges from transcription factors to targets, derived from ChIP-seq and accessibility data. (C) Knowledge graphs: heterogeneous graphs with multiple node types (genes, diseases, drugs, pathways) and relationship types enabling multi-hop reasoning. (D) Spatial and cell-cell interaction graphs: emerging from spatial transcriptomics, encoding tissue architecture and cell communication."

---

## Figure 2: Message Passing Framework

### Files
- `figs/part_4/ch18/02-A-fig-message-passing.svg`
- `figs/part_4/ch18/02-B-fig-message-passing.svg`
- `figs/part_4/ch18/02-C-fig-message-passing.svg`
- `figs/part_4/ch18/02-D-fig-message-passing.svg`

### Priority
**High** - Core GNN concept

### Content Description
Step-by-step illustration of the message passing algorithm showing initial state, message computation, aggregation, and multi-layer propagation.

### DALL-E Prompt
```
Scientific illustration of graph neural network message passing for computational biology. Four sequential panels.

PANEL A (Initial State): Simple 5-node graph with edges. Each node has initial feature vector (shown as small colored bar). Annotation "Initial features from foundation model embeddings." Node labels: gene names.

PANEL B (Message Computation): Same graph with arrows on edges showing message flow. For each edge, message m_ij computed from source and target features. Mathematical notation: m_ij = φ(h_i, h_j, e_ij). Arrows visualizing message direction.

PANEL C (Aggregation): Focus on single node receiving messages from all neighbors. Incoming arrows merging at node. Aggregation operations listed: sum, mean, max, attention. New representation formed. Mathematical notation: h_i' = ψ(h_i, ⊕ m_ij).

PANEL D (After L Layers): Same graph but nodes now showing expanded "receptive field" circles. After L=2 layers, each node's embedding incorporates 2-hop neighborhood. Annotation "Gene embedding now reflects pathway context." Before/after comparison of what node knows.

Clean technical illustration, white background, consistent node and edge styling, mathematical notation included.

Save as: 02-A-fig-message-passing.svg through 02-D-fig-message-passing.svg
```

### Post-Processing Notes
- Add mathematical formulas clearly
- Show feature vector dimensions
- Include layer number annotations

### Fallback Description
"Message passing in GNNs: initial node features from foundation models, message computation along edges, aggregation at each node combining neighbor information, and after L layers each node embedding incorporates L-hop neighborhood context."

### Caption Recommendation
"Message passing in graph neural networks. (A) Initial state: each node has feature vectors from foundation model embeddings. (B) Message computation: for each edge, compute message m_ij = φ(h_i, h_j, e_ij). (C) Aggregation: each node aggregates incoming messages using permutation-invariant operations (sum, mean, max, or attention). (D) After L layers: each node's embedding incorporates information from its L-hop neighborhood, capturing pathway-level context."

---

## Figure 3: Foundation Model + GNN Integration

### Files
- `figs/part_4/ch18/03-A-fig-gnn-integration.svg`
- `figs/part_4/ch18/03-B-fig-gnn-integration.svg`
- `figs/part_4/ch18/03-C-fig-gnn-integration.svg`
- `figs/part_4/ch18/03-D-fig-gnn-integration.svg`

### Priority
**Essential** - Core architectural concept

### Content Description
The central integration paradigm: foundation models produce representations, networks encode relationships, GNNs integrate both, enabling capabilities neither achieves alone.

### DALL-E Prompt
```
Scientific illustration of foundation model and GNN integration for computational biology. Four panels showing the integration paradigm.

PANEL A (Foundation Models Produce Representations): Three parallel flows. ESM-2 + protein sequence → protein embedding. DNABERT + DNA sequence → DNA embedding. scGPT + expression profile → cell embedding. Annotation "Rich representations of individual entities."

PANEL B (Biological Networks Encode Relationships): Network diagram showing PPI edges, regulatory edges, cell-cell communication. Annotation "Relational structure not captured by sequence alone." Emphasis on what networks add.

PANEL C (GNNs Integrate Both): Architecture diagram. Node features from FMs feed into GNN layers. Edges from biological networks. Message passing refines representations. Output: context-aware embeddings. Annotation "Message passing adds relational context."

PANEL D (Capabilities Neither Achieves Alone): Two-column comparison. Left (FM alone): "Rich features but no interactions" with X. Right (Network alone): "Relationships but limited features" with X. Center (Combined): "Disease gene prioritization, drug-target prediction, perturbation modeling" with checkmarks.

Professional scientific illustration, clean architecture diagrams, white background, emphasize the complementary nature.

Save as: 03-A-fig-gnn-integration.svg through 03-D-fig-gnn-integration.svg
```

### Post-Processing Notes
- Use specific foundation model names
- Show embedding dimensionalities
- Include specific application examples

### Fallback Description
"Foundation model and GNN integration: FMs produce rich entity representations from sequence, networks encode relational structure, GNNs combine both through message passing, enabling applications like disease gene prioritization that neither approach achieves alone."

### Caption Recommendation
"The foundation model + GNN integration paradigm. (A) Foundation models produce rich representations of individual entities: protein embeddings from ESM, DNA embeddings from DNABERT, cell embeddings from scGPT. (B) Biological networks encode relational structure that sequence models cannot capture. (C) GNNs integrate foundation model embeddings with network structure through message passing. (D) This combination enables capabilities neither achieves alone: disease gene prioritization, drug-target prediction, and perturbation response modeling."

---

## Figure 4: Disease Gene Prioritization

### Files
- `figs/part_4/ch18/04-A-fig-disease-gene-prioritization.svg`
- `figs/part_4/ch18/04-B-fig-disease-gene-prioritization.svg`
- `figs/part_4/ch18/04-C-fig-disease-gene-prioritization.svg`
- `figs/part_4/ch18/04-D-fig-disease-gene-prioritization.svg`

### Priority
**High** - Key application

### Content Description
GWAS follow-up application showing the challenge, network context, GNN scoring, and integration with sequence features.

### DALL-E Prompt
```
Scientific illustration of disease gene prioritization using GNNs for clinical genomics. Four panels.

PANEL A (The GWAS Challenge): Genomic locus diagram with lead SNP marker. Four genes (A, B, C, D) in the region. LD block shown covering all genes. Question mark: "Which gene is causal?" Annotation "Lead SNP in LD with all genes."

PANEL B (Network Context): Same four genes now shown in PPI network. Gene B connected to 5 known disease genes (highlighted in red). Genes A, C, D peripheral with few disease gene connections. Network topology suggests B as candidate.

PANEL C (GNN Scoring): GNN architecture receiving FM embeddings as node features. Disease gene labels propagating through network. Gene B receives high network-based score. Score bars showing B > C > A > D.

PANEL D (Integration with Sequence Features): Dual scoring. Gene C has strong protein features (from ESM). Gene B has strong network features + moderate protein features. Combined score identifies both B and C as top candidates. Annotation "Integrates intrinsic and relational evidence."

Clinical genomics illustration style, white background, network diagrams with gene nodes, score visualizations.

Save as: 04-A-fig-disease-gene-prioritization.svg through 04-D-fig-disease-gene-prioritization.svg
```

### Post-Processing Notes
- Use realistic gene names
- Show actual GWAS locus structure
- Include score comparisons

### Fallback Description
"Disease gene prioritization from GWAS: the challenge of multiple genes in LD, network context showing one gene connected to known disease genes, GNN scoring using FM embeddings and network propagation, and integration showing how sequence and network features complement each other."

### Caption Recommendation
"Disease gene prioritization for GWAS follow-up. (A) The GWAS challenge: a lead SNP is in LD with multiple genes—which is causal? (B) Network context: Gene B connects to five known disease genes while A, C, D are peripheral. (C) GNN scoring: foundation model embeddings as node features combined with network propagation prioritize gene B. (D) Sequence-network integration: Gene C has strong protein features while Gene B has network context—combined scoring identifies both as candidates for follow-up."

---

## Figure 5: Knowledge Graph Drug Repurposing

### Files
- `figs/part_4/ch18/05-A-fig-kg-drug-repurposing.svg`
- `figs/part_4/ch18/05-B-fig-kg-drug-repurposing.svg`
- `figs/part_4/ch18/05-C-fig-kg-drug-repurposing.svg`
- `figs/part_4/ch18/05-D-fig-kg-drug-repurposing.svg`

### Priority
**High** - Important translational application

### Content Description
Knowledge graph reasoning for drug repurposing: KG structure, multi-hop reasoning paths, link prediction, and FM enhancement.

### DALL-E Prompt
```
Scientific illustration of knowledge graph reasoning for drug repurposing. Four panels.

PANEL A (KG Structure): Heterogeneous knowledge graph with multiple node types. Drugs (blue squares), proteins (green circles), diseases (red diamonds), pathways (yellow rectangles). Multiple edge types with different line styles: binds, regulates, associated_with, participates_in. Partial view of Hetionet-style graph.

PANEL B (Multi-Hop Reasoning Path): Highlighted path through the KG. Drug D → (binds) → Protein P1 → (participates_in) → Pathway W → (disrupted_in) → Disease X. Each hop labeled with relationship type. Annotation "Multi-hop path provides mechanistic hypothesis."

PANEL C (Link Prediction): Full KG with trained node embeddings (glow effect). Query: predict missing drug-treats-disease edges. Dashed lines showing potential new connections. Scoring function comparing embeddings. Top candidates ranked by score.

PANEL D (FM Enhancement): Same KG but node features replaced with FM embeddings. Protein nodes: ESM embeddings capturing function. Gene nodes: DNA embeddings capturing regulation. Annotation "FM embeddings capture functional similarity beyond annotations."

Professional scientific illustration, knowledge graph visualization style, heterogeneous node shapes and colors, white background.

Save as: 05-A-fig-kg-drug-repurposing.svg through 05-D-fig-kg-drug-repurposing.svg
```

### Post-Processing Notes
- Include specific edge type counts
- Show actual drug-disease predictions
- Add database source annotations

### Fallback Description
"Knowledge graph drug repurposing: heterogeneous graph structure with drugs, proteins, diseases, and pathways; multi-hop reasoning paths providing mechanistic hypotheses; link prediction for new drug-disease associations; and foundation model embeddings enhancing node representations beyond database annotations."

### Caption Recommendation
"Knowledge graph reasoning for drug repurposing. (A) Heterogeneous knowledge graph structure with multiple node types (drugs, proteins, diseases, pathways) and relationship types. (B) Multi-hop reasoning: a drug might treat a disease through a path like Drug → binds → Protein → pathway → Disease. (C) Link prediction: GNNs learn embeddings to score potential new drug-disease associations. (D) Foundation model enhancement: FM embeddings capture functional similarity that database annotations miss."

---

## Figure 6: Network Study Bias

### Files
- `figs/part_4/ch18/06-fig-network-bias.svg`

### Priority
**Enhancing** - Critical limitation

### Content Description
Visualization of study bias in biological networks: correlation between node degree and publication count, implications for GNN predictions.

### DALL-E Prompt
```
Scientific illustration showing study bias in biological networks for computational biology. Single panel with multiple elements.

MAIN PLOT: Scatter plot with log-log axes. X-axis: "Number of publications" (log scale, 1 to 10,000+). Y-axis: "Node degree in PPI network" (log scale, 1 to 1,000+). Strong positive correlation visible. Well-studied genes labeled (TP53, BRCA1, EGFR) as high-degree, high-publication points. Novel/understudied genes clustered at low degree, low publication corner.

SIDE ANNOTATIONS:
- Arrow pointing to high-degree hub: "Well-studied genes become network hubs"
- Arrow pointing to peripheral nodes: "Understudied genes appear peripheral"
- Warning box: "Risk: GNN prioritizes already-known genes"

BOTTOM PANEL: Small diagram showing mitigation strategies as icons:
1) Degree normalization (mathematical adjustment icon)
2) Attention to edge confidence (reliability weight icon)
3) Temporal holdout evaluation (time arrow icon)

Professional scientific visualization, scatter plot style, white background, clear annotations highlighting the bias problem.

Save as: 06-fig-network-bias.svg
```

### Post-Processing Notes
- Add actual correlation coefficient
- Include specific gene examples
- Show confidence intervals

### Fallback Description
"Study bias in biological networks: scatter plot showing strong correlation between publication count and network degree, with well-studied genes like TP53 and BRCA1 as high-degree hubs while understudied genes appear peripheral regardless of true biology. This bias causes GNNs to prioritize already-known genes."

### Caption Recommendation
"Study bias in biological networks. Strong correlation between publication count and network degree means well-characterized genes (TP53, BRCA1, EGFR) appear as highly connected hubs while understudied genes are peripheral. This ascertainment bias causes GNNs to preferentially propagate signal toward already-known genes. Mitigation strategies include degree normalization, edge confidence weighting, and temporal holdout evaluation."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Biological Networks | 4 | Essential | Medium |
| Message Passing | 4 | High | Medium |
| FM + GNN Integration | 4 | Essential | Medium |
| Disease Gene Prioritization | 4 | High | High |
| KG Drug Repurposing | 4 | High | High |
| Network Bias | 1 | Enhancing | Low |

## Recommended Generation Order
1. Biological Networks (landscape foundation)
2. Message Passing (core algorithm)
3. FM + GNN Integration (central paradigm)
4. Disease Gene Prioritization (application)
5. KG Drug Repurposing (translational application)
6. Network Bias (critical limitation)
# Figure Report: Chapter 22 - Multi-Omics Integration

**Chapter:** p4-ch22-multi-omics.qmd
**Date:** 2026-01-07
**Total Figures:** 5 (19 files)
**Format:** SVG (for scalability)

---

## Figure 1: The Integration Paradox

### Files
- `figs/part_4/ch19/01-A-fig-integration-paradox.svg`
- `figs/part_4/ch19/01-B-fig-integration-paradox.svg`
- `figs/part_4/ch19/01-C-fig-integration-paradox.svg`
- `figs/part_4/ch19/01-D-fig-integration-paradox.svg`

### Priority
**Essential** - Central tension of the chapter

### Content Description
Four-panel figure showing the promise and paradox of multi-omics integration: what each modality captures, when integration hurts performance, and when it helps.

### DALL-E Prompt
```
Scientific illustration of the multi-omics integration paradox for computational biology textbook. Four panels.

PANEL A (The Promise): Four columns showing different omics layers. Genomics (DNA helix): "Heritable potential." Transcriptomics (mRNA): "Current state." Proteomics (protein structure): "Functional complement." Metabolomics (small molecules): "Downstream biochemistry." Arrow suggesting integration should improve prediction.

PANEL B (The Paradox): Performance curve showing counterintuitive result. X-axis: number of modalities. Y-axis: prediction performance. Curve peaks at 1-2 modalities, then drops with more. Annotations: "More features → more overfitting," "Missing data compounds problem," "Noise overwhelms signal."

PANEL C (When Integration Helps): Three scenarios with green checkmarks. 1) Complementary information (genomics + expression for complex traits). 2) Cross-modality validation (concordant signals increase confidence). 3) Mechanistic interpretation (trace causal cascade).

PANEL D (When Integration Hurts): Three scenarios with red X marks. 1) Redundant information (correlated features inflate dimensionality). 2) Batch effects across modalities (spurious correlations). 3) Sample size dilution (only patients with all modalities used).

Professional scientific illustration, clean infographic style, white background, contrasting colors for help vs hurt.

Save as: 01-A-fig-integration-paradox.svg through 01-D-fig-integration-paradox.svg
```

### Post-Processing Notes
- Add specific performance metrics examples
- Include real-world cohort size examples
- Show batch effect visualization

### Fallback Description
"The multi-omics integration paradox: different modalities capture complementary biology, but naive integration often degrades performance due to overfitting, noise, and missing data. Integration helps when information is complementary and hurts when redundant or confounded by batch effects."

### Caption Recommendation
"The multi-omics integration paradox. (A) Promise: each modality captures different aspects of biology—genomics shows heritable potential, transcriptomics reveals current state, proteomics measures functional complement, metabolomics tracks downstream biochemistry. (B) Paradox: more modalities can mean worse predictions when noise overwhelms signal. (C) When integration helps: complementary information, cross-modality validation, and mechanistic interpretation. (D) When integration hurts: redundant features, batch effects, and sample size reduction from incomplete overlap."

---

## Figure 2: Fusion Strategy Comparison

### Files
- `figs/part_4/ch19/02-A-fig-fusion-strategies.svg`
- `figs/part_4/ch19/02-B-fig-fusion-strategies.svg`
- `figs/part_4/ch19/02-C-fig-fusion-strategies.svg`

### Priority
**Essential** - Core methodological framework

### Content Description
Three-panel comparison of early, late, and intermediate fusion strategies with their tradeoffs.

### DALL-E Prompt
```
Scientific illustration comparing multi-omics fusion strategies for computational biology. Three panels.

PANEL A (Early Fusion): Flow diagram. Three input modalities (genomics, transcriptomics, proteomics) as separate feature vectors. Concatenation operator joining all features. Single unified model processing concatenated input. Output prediction. Pros listed: "Can learn cross-modal interactions." Cons listed: "Curse of dimensionality, requires complete data."

PANEL B (Late Fusion): Flow diagram. Three separate models, one per modality. Each produces independent prediction/score. Ensemble combiner merging predictions (weighted average, voting, or meta-learner). Final output. Pros: "Handles missing modalities, modality-specific architectures." Cons: "Cannot learn feature-level interactions."

PANEL C (Intermediate Fusion): Flow diagram. Three modality-specific encoders. Each encoder outputs embedding into shared latent space (central circle). Alignment mechanisms shown (contrastive, reconstruction losses). Downstream task head on shared space. Pros: "Flexibility + robustness." Cons: "Alignment complexity."

SUMMARY TABLE at bottom comparing: cross-modal interactions (Early: yes, Late: no, Intermediate: yes), missing data handling (Early: poor, Late: excellent, Intermediate: good), computational cost.

Professional scientific illustration, flowchart style, white background, consistent visual language across panels.

Save as: 02-A-fig-fusion-strategies.svg through 02-C-fig-fusion-strategies.svg
```

### Post-Processing Notes
- Use consistent modality colors
- Add dimensionality annotations
- Include specific model architecture examples

### Fallback Description
"Fusion strategy comparison: early fusion concatenates features before modeling (learns interactions but requires complete data), late fusion combines model predictions (handles missing data but no feature interactions), intermediate fusion learns shared latent space (balances flexibility and robustness)."

### Caption Recommendation
"Multi-omics fusion strategies. (A) Early fusion: concatenate features before modeling. Enables cross-modal interaction learning but requires complete data and suffers from dimensionality. (B) Late fusion: train separate models and combine predictions. Handles missing modalities but cannot learn feature interactions. (C) Intermediate fusion: modality-specific encoders project to shared latent space. Balances interaction learning with missing data robustness."

---

## Figure 3: Intermediate Fusion Architecture Details

### Files
- `figs/part_4/ch19/03-A-fig-intermediate-fusion.svg`
- `figs/part_4/ch19/03-B-fig-intermediate-fusion.svg`
- `figs/part_4/ch19/03-C-fig-intermediate-fusion.svg`
- `figs/part_4/ch19/03-D-fig-intermediate-fusion.svg`

### Priority
**High** - Detailed architecture for dominant approach

### Content Description
Detailed architecture of intermediate fusion: modality-specific encoders, shared latent space with alignment mechanisms, and missing modality handling.

### DALL-E Prompt
```
Scientific illustration of intermediate fusion architecture for multi-omics integration. Four panels.

PANEL A (Modality-Specific Encoders): Three encoder architectures shown side by side. Expression VAE (variational autoencoder structure). Methylation CNN (1D convolution over genomic coordinates). Proteomics MLP (dense layers). Each labeled with "Tailored to modality characteristics."

PANEL B (Shared Latent Space): Central shared space as circle/ellipse. All encoders pointing to same space with arrows. Loss functions listed around space: "Reconstruction loss," "Contrastive loss," "Graph constraints." Annotation "All embeddings same dimensionality."

PANEL C (Downstream Task Head): Shared latent space feeding into task-specific heads. Classifier head for prediction. Regression head for continuous outcomes. Multiple tasks possible from same representation. Cross-modal reasoning enabled.

PANEL D (Missing Modality Handling): Two scenarios. Left: complete sample with all three encoders firing, full embedding. Right: partial sample with only two modalities, partial embedding (dashed outline for missing). Annotation "Graceful degradation" - still produces useful representation.

Technical architecture diagram style, white background, neural network visualization conventions.

Save as: 03-A-fig-intermediate-fusion.svg through 03-D-fig-intermediate-fusion.svg
```

### Post-Processing Notes
- Add embedding dimensionalities
- Show loss function equations
- Include specific architecture parameters

### Fallback Description
"Intermediate fusion architecture: modality-specific encoders (VAE for expression, CNN for methylation, MLP for proteomics) project to shared latent space aligned through reconstruction, contrastive, and graph constraints. Downstream task heads operate on shared space, enabling graceful degradation when modalities are missing."

### Caption Recommendation
"Intermediate fusion architecture in detail. (A) Modality-specific encoders tailored to each data type: VAE for expression handling sparsity, CNN for methylation along genomic coordinates, MLP for proteomics. (B) Shared latent space: encoders produce embeddings aligned through reconstruction loss, contrastive terms, and biological graph constraints. (C) Downstream task heads operate on the shared representation, enabling cross-modal reasoning. (D) Missing modality handling: partial samples use only available encoders, enabling graceful degradation rather than sample exclusion."

---

## Figure 4: Clinical Multi-Modal Integration

### Files
- `figs/part_4/ch19/04-A-fig-clinical-multimodal.svg`
- `figs/part_4/ch19/04-B-fig-clinical-multimodal.svg`
- `figs/part_4/ch19/04-C-fig-clinical-multimodal.svg`
- `figs/part_4/ch19/04-D-fig-clinical-multimodal.svg`

### Priority
**High** - Clinical translation relevance

### Content Description
Patient-level integration of EHR, imaging, and molecular data for clinical prediction tasks.

### DALL-E Prompt
```
Scientific illustration of clinical multi-modal data integration for precision medicine. Four panels.

PANEL A (Data Modalities): Three data sources visualized. EHR: timeline of diagnoses, procedures, medications, lab values (longitudinal). Imaging: CT scan, MRI brain, histopathology slide icons (spatial). Molecular: DNA helix, expression heat map, protein network (static/omics). Each labeled with key characteristics.

PANEL B (Modality-Specific Encoders): Three encoders. EHR transformer processing event sequence over time. Imaging vision encoder (CNN/ViT) processing scan. Molecular FM embeddings from pretrained models. Each produces fixed-size patient embedding.

PANEL C (Patient Representation Space): Central shared space with all modalities contributing. Cross-modal consistency arrows: EHR predicts molecular state, imaging consistent with trajectory. Unified patient embedding combining all sources.

PANEL D (Clinical Prediction Tasks): Multiple downstream applications. Risk stratification (probability bars). Treatment response prediction (responder/non-responder). Prognosis/survival (Kaplan-Meier curve icon). Callout box: "Not all patients have all data - must handle missing modalities."

Clinical/medical illustration style, white background, patient-centric visualization, practical deployment focus.

Save as: 04-A-fig-clinical-multimodal.svg through 04-D-fig-clinical-multimodal.svg
```

### Post-Processing Notes
- Add specific clinical examples
- Include temporal alignment challenges
- Show realistic missingness patterns

### Fallback Description
"Clinical multi-modal integration: combining longitudinal EHR data, spatial imaging, and static molecular measurements through modality-specific encoders into a unified patient representation for clinical prediction tasks including risk stratification, treatment response, and prognosis."

### Caption Recommendation
"Clinical multi-modal integration. (A) Data modalities: longitudinal EHR (diagnoses, procedures, labs), spatial imaging (CT, MRI, histopathology), and static molecular measurements (genomics, expression, proteomics). (B) Modality-specific encoders: EHR transformer for event sequences, vision encoder for imaging, foundation model embeddings for molecular data. (C) Patient representation space: unified embedding where EHR predicts molecular state and imaging is consistent with clinical trajectory. (D) Clinical prediction tasks: risk stratification, treatment response, and prognosis—with the practical requirement of handling incomplete data."

---

## Figure 5: Information Cascade from Variant to Phenotype

### Files
- `figs/part_4/ch19/05-A-fig-information-cascade.svg`
- `figs/part_4/ch19/05-B-fig-information-cascade.svg`
- `figs/part_4/ch19/05-C-fig-information-cascade.svg`
- `figs/part_4/ch19/05-D-fig-information-cascade.svg`

### Priority
**High** - Conceptual systems biology framework

### Content Description
Systems biology view tracing information flow from genetic variants through molecular layers to clinical phenotypes, including bottleneck modality concept.

### DALL-E Prompt
```
Scientific illustration of the information cascade from genetic variant to clinical phenotype. Four panels.

PANEL A (The Causal Cascade): Vertical flow diagram. Top: Genetic variant (SNP symbol). Arrow labeled "cis-regulation." Expression change (mRNA up/down). Arrow labeled "translation." Protein change (structure altered). Arrow labeled "metabolism." Metabolite change (pathway flux). Arrow labeled "cellular." Cell behavior change. Arrow labeled "tissue." Clinical phenotype at bottom. Full cascade visualized.

PANEL B (Where Each Modality Provides Information): Same cascade with modality labels at each level. Genomics at variant level (starting point). Transcriptomics at expression (current state). Proteomics at protein (functional complement). Metabolomics at metabolite (downstream). Clinical data at phenotype (manifestation). Each labeled with what it measures.

PANEL C (Bottleneck Modalities): Three scenarios. 1) Coding variant: bottleneck at protein structure (protein box highlighted). 2) Regulatory variant: bottleneck at expression level (expression box highlighted). 3) Some phenotypes: bottleneck downstream (phenotype box highlighted, molecular less informative).

PANEL D (Integration Implications): Decision tree or flowchart. "What drives your phenotype?" → If coding variants → prioritize protein features. → If regulatory → prioritize expression. → Complex trait → integrate multiple levels. Annotation "Not all modalities equally informative for all questions."

Systems biology illustration style, causal diagram conventions, white background, clear flow direction.

Save as: 05-A-fig-information-cascade.svg through 05-D-fig-information-cascade.svg
```

### Post-Processing Notes
- Add specific gene/disease examples
- Include quantitative effect sizes
- Show causal vs correlational distinction

### Fallback Description
"Information cascade from variant to phenotype: genetic variants cause expression changes, which alter protein levels, affecting metabolic flux, changing cell behavior, and ultimately manifesting as clinical phenotypes. Different modalities provide information at different levels, with 'bottleneck modalities' being most directly relevant depending on the variant type."

### Caption Recommendation
"Systems biology view of multi-omics integration. (A) The causal cascade: genetic variants propagate through molecular layers—expression, protein, metabolite, cellular behavior—to clinical phenotype. (B) Where each modality provides information: genomics captures the starting point, transcriptomics the current state, proteomics the functional complement, metabolomics downstream effects. (C) Bottleneck modalities: coding variants bottleneck at protein level, regulatory variants at expression level—determining which modality is most informative. (D) Integration implications: the causal architecture guides which modalities to prioritize for different biological questions."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Integration Paradox | 4 | Essential | Medium |
| Fusion Strategies | 3 | Essential | Medium |
| Intermediate Fusion | 4 | High | High |
| Clinical Multimodal | 4 | High | High |
| Information Cascade | 4 | High | Medium |

## Recommended Generation Order
1. Integration Paradox (central tension)
2. Fusion Strategies (methodological framework)
3. Intermediate Fusion (detailed architecture)
4. Information Cascade (conceptual framework)
5. Clinical Multimodal (translation)
# Figure Report: Chapter 23 - Uncertainty Quantification

**Chapter:** p5-ch23-uncertainty.qmd
**Date:** 2026-01-07
**Total Figures:** 7 (15 files)
**Format:** SVG (for scalability)

---

## Figure 1: Uncertainty Types (Aleatoric vs Epistemic)

### Files
- `figs/part_5/ch23/01-A-fig-uncertainty-types.svg`
- `figs/part_5/ch23/01-B-fig-uncertainty-types.svg`

### Priority
**Essential** - Core conceptual framework

### Content Description
Two-panel comparison of aleatoric (irreducible) versus epistemic (reducible) uncertainty, with genomic examples.

### DALL-E Prompt
```
Scientific illustration comparing two types of uncertainty for computational biology textbook. Two panels.

PANEL A (Aleatoric - Irreducible): Visualization showing inherent stochastic variability. Example: Gene expression from identical cells showing distribution of values around mean. Dice icon symbolizing randomness. Multiple cells (same genotype) producing variable expression. Annotation "Cannot be reduced with more data - reflects true biological noise." Graph showing distribution width that doesn't narrow with sample size.

PANEL B (Epistemic - Reducible): Visualization showing knowledge-based uncertainty. Example: Variant effect prediction in data-sparse region. Question mark icon symbolizing lack of knowledge. Few training examples nearby, wide confidence interval. Annotation "Can be reduced with more data or better models." Graph showing confidence interval narrowing as sample size increases.

Genomic examples beneath each: Aleatoric - stochastic gene expression, measurement noise. Epistemic - rare variant effects, novel protein families, underrepresented populations.

Clean scientific illustration, white background, educational diagram style, blue for aleatoric, orange for epistemic.

Save as: 01-A-fig-uncertainty-types.svg (aleatoric), 01-B-fig-uncertainty-types.svg (epistemic)
```

### Post-Processing Notes
- Add mathematical notation for variance decomposition
- Include specific genomic examples
- Show how each relates to model confidence

### Fallback Description
"Comparison of aleatoric (irreducible, inherent biological/measurement noise) and epistemic (reducible, knowledge-based) uncertainty, showing how aleatoric uncertainty persists with more data while epistemic uncertainty can be reduced through additional training examples."

### Caption Recommendation
"Two types of uncertainty. (A) Aleatoric uncertainty: irreducible stochasticity from biological variability or measurement noise—cannot be eliminated with more data. (B) Epistemic uncertainty: reducible uncertainty from limited knowledge—decreases as training data grow. Distinguishing these is critical: high epistemic uncertainty should trigger caution, while aleatoric uncertainty sets fundamental prediction limits."

---

## Figure 2: Calibration Diagrams

### Files
- `figs/part_5/ch23/02-A-fig-calibration-diagrams.svg`
- `figs/part_5/ch23/02-B-fig-calibration-diagrams.svg`
- `figs/part_5/ch23/02-C-fig-calibration-diagrams.svg`
- `figs/part_5/ch23/02-D-fig-calibration-diagrams.svg`

### Priority
**Essential** - Core visualization for calibration assessment

### Content Description
Four-panel figure showing reliability diagrams: perfect calibration, overconfident predictions, underconfident predictions, and calibration error metrics.

### DALL-E Prompt
```
Scientific illustration of model calibration diagrams for machine learning textbook. Four panels.

PANEL A (Perfect Calibration): Reliability diagram with predicted probability (x-axis, 0-1) vs observed frequency (y-axis, 0-1). Perfect diagonal line. Bar histogram at bottom showing prediction distribution. Annotation "Predictions match reality."

PANEL B (Overconfident): Same axes but curve bowed below diagonal. When model says 90%, reality is only 70%. Shaded area showing calibration gap. Annotation "Model too confident - common in deep learning." Clinical warning: "Overconfidence → missed diagnoses."

PANEL C (Underconfident): Curve bowed above diagonal. When model says 60%, reality is 75%. Shaded gap area. Annotation "Model too uncertain - loses utility." Note: "Less common but wastes follow-up resources."

PANEL D (Calibration Metrics): Equations and visual explanation. ECE (Expected Calibration Error): weighted average of |accuracy - confidence| in bins. Shown as sum of shaded areas. MCE (Maximum Calibration Error): worst bin. Brier score decomposition. Visual showing bin-by-bin calculation.

Professional scientific illustration, statistical visualization style, white background, consistent color scheme.

Save as: 02-A-fig-calibration-diagrams.svg through 02-D-fig-calibration-diagrams.svg
```

### Post-Processing Notes
- Add mathematical formulas for ECE, MCE
- Include confidence intervals on bins
- Show number of samples per bin

### Fallback Description
"Calibration assessment diagrams: perfectly calibrated predictions fall on the diagonal, overconfident predictions curve below (model claims certainty it doesn't deserve), underconfident predictions curve above. ECE and MCE metrics quantify calibration error."

### Caption Recommendation
"Model calibration assessment. (A) Perfect calibration: predicted probabilities match observed frequencies on the diagonal. (B) Overconfident model: predictions systematically exceed reality—dangerous for clinical use. (C) Underconfident model: predictions underestimate true probabilities—reduces utility. (D) Calibration metrics: Expected Calibration Error (ECE) averages across bins; Maximum Calibration Error (MCE) captures worst-case performance."

---

## Figure 3: Calibration Methods

### Files
- `figs/part_5/ch23/03-A-fig-calibration-methods.svg`
- `figs/part_5/ch23/03-B-fig-calibration-methods.svg`
- `figs/part_5/ch23/03-C-fig-calibration-methods.svg`

### Priority
**High** - Practical implementation guidance

### Content Description
Three-panel comparison of calibration strategies: temperature scaling, Platt scaling, and isotonic regression.

### DALL-E Prompt
```
Scientific illustration of model calibration methods for machine learning. Three panels.

PANEL A (Temperature Scaling): Flow diagram. Input: uncalibrated logits. Operation: divide by learned temperature T. Output: softmax with calibrated probabilities. Before/after reliability diagrams showing improvement. Annotation "Single parameter; preserves ranking; widely used." Mathematical: softmax(z/T).

PANEL B (Platt Scaling): Flow diagram. Input: model scores. Operation: logistic regression with learned parameters a, b. Sigmoid transformation. Before/after showing calibration improvement. Annotation "Two parameters; handles asymmetric miscalibration." Mathematical: σ(a·z + b).

PANEL C (Isotonic Regression): Flow diagram. Input: sorted predictions. Operation: piecewise constant monotonic fit. Histogram of predictions with step function overlay. Before/after diagrams. Annotation "Non-parametric; flexible but needs more data; risk of overfitting." Visual showing monotonic constraint.

Comparison table below: Method, Parameters, Flexibility, Data requirement, Best for.

Professional scientific style, flowchart elements, white background, consistent visual language.

Save as: 03-A-fig-calibration-methods.svg through 03-C-fig-calibration-methods.svg
```

### Post-Processing Notes
- Add code snippets showing implementation
- Include validation set requirements
- Show cross-validation considerations

### Fallback Description
"Calibration methods comparison: temperature scaling (single parameter, divides logits), Platt scaling (logistic regression on scores), and isotonic regression (non-parametric monotonic fit). Each trades off flexibility against data requirements."

### Caption Recommendation
"Post-hoc calibration methods. (A) Temperature scaling: divides logits by learned temperature T before softmax—simple, preserves ranking, widely effective. (B) Platt scaling: fits logistic regression on model scores—handles asymmetric miscalibration with two parameters. (C) Isotonic regression: non-parametric monotonic fit—most flexible but requires more calibration data and risks overfitting."

---

## Figure 4: UQ Methods Overview

### Files
- `figs/part_5/ch23/04-fig-uq-methods.svg`

### Priority
**High** - Survey of approaches

### Content Description
Comprehensive overview of uncertainty quantification methods: ensembles, dropout, Bayesian methods, evidential deep learning.

### DALL-E Prompt
```
Scientific illustration overview of uncertainty quantification methods for deep learning. Single comprehensive panel.

QUADRANT LAYOUT:

TOP LEFT (Ensembles): Multiple neural network diagrams (5 networks). Each produces prediction. Aggregation showing mean and variance of predictions. Annotation "Multiple models → prediction spread measures uncertainty." Pros: Works well. Cons: 5-10x compute.

TOP RIGHT (MC Dropout): Single network with dropout layers highlighted. Multiple forward passes with different dropout masks. Prediction distribution from passes. Annotation "Single model, multiple stochastic passes." Pros: Easy to implement. Cons: Approximate.

BOTTOM LEFT (Bayesian NNs): Network with probability distributions on weights (not point values). Posterior inference visualization. Annotation "Distribution over weights → principled uncertainty." Pros: Principled. Cons: Computationally intensive; approximations needed.

BOTTOM RIGHT (Evidential DL): Network producing distribution parameters directly (e.g., mean + variance, or Dirichlet parameters). Single forward pass. Annotation "Learn to predict uncertainty directly." Pros: Fast inference. Cons: Requires careful training.

CENTER: Comparison compass showing tradeoffs between compute cost, theoretical grounding, implementation complexity, and calibration quality.

Professional scientific illustration, neural network diagram style, white background.

Save as: 04-fig-uq-methods.svg
```

### Post-Processing Notes
- Add mathematical notation for each method
- Include citation references
- Show computational cost estimates

### Fallback Description
"Uncertainty quantification methods overview: ensembles (multiple models, high compute), MC dropout (stochastic passes, approximate), Bayesian NNs (principled but expensive), and evidential deep learning (single-pass, learns uncertainty). Each trades off compute, theory, and calibration."

### Caption Recommendation
"Uncertainty quantification methods for deep learning. Ensembles train multiple models and use prediction variance; MC Dropout uses stochastic forward passes through a single model; Bayesian neural networks maintain distributions over weights; evidential deep learning predicts distribution parameters directly. Each involves tradeoffs between computational cost, theoretical grounding, and calibration quality."

---

## Figure 5: Conformal Prediction

### Files
- `figs/part_5/ch23/05-fig-conformal-prediction.svg`

### Priority
**High** - Distribution-free uncertainty

### Content Description
Conformal prediction framework showing how to construct prediction sets with guaranteed coverage.

### DALL-E Prompt
```
Scientific illustration of conformal prediction for uncertainty quantification. Single comprehensive panel with multiple elements.

TOP SECTION (The Guarantee): Mathematical statement: "P(Y ∈ C(X)) ≥ 1 - α" in large text. Annotation "Coverage guarantee holds regardless of model architecture or data distribution."

MIDDLE SECTION (Procedure):
Step 1: Split data into training and calibration sets. Visual of dataset splitting.
Step 2: Train model on training set. Neural network icon.
Step 3: Compute conformity scores on calibration set. Formula: s_i = some non-conformity measure. Histogram of calibration scores.
Step 4: Find threshold q at (1-α) quantile of scores. Vertical line on histogram.
Step 5: For new input, include labels where score ≤ q. Prediction set visualization.

BOTTOM SECTION (Genomic Example):
Variant classification example. Instead of "Pathogenic" → prediction set {"Pathogenic", "VUS"} with 90% coverage guarantee. For well-characterized variant: small set. For rare variant: larger set (honest about uncertainty).

Annotation: "Key insight: Set size reflects confidence—rare variants get larger sets."

Professional scientific style, flowchart elements, probability visualization, white background.

Save as: 05-fig-conformal-prediction.svg
```

### Post-Processing Notes
- Add specific genomic examples
- Show coverage verification
- Include adaptive conformal prediction variant

### Fallback Description
"Conformal prediction procedure: split data, compute conformity scores on calibration set, find threshold at desired coverage level, construct prediction sets for new inputs. Provides distribution-free coverage guarantees—rare variants get larger prediction sets reflecting honest uncertainty."

### Caption Recommendation
"Conformal prediction for coverage-guaranteed uncertainty. The procedure uses a calibration set to establish a score threshold such that prediction sets cover the true label with probability at least 1−α. Unlike point predictions, conformal sets communicate uncertainty through their size: well-characterized variants receive small sets, while rare variants receive larger sets that honestly reflect limited knowledge."

---

## Figure 6: Out-of-Distribution Detection

### Files
- `figs/part_5/ch23/06-A-fig-ood-detection.svg`
- `figs/part_5/ch23/06-B-fig-ood-detection.svg`
- `figs/part_5/ch23/06-C-fig-ood-detection.svg`

### Priority
**High** - Critical for safe deployment

### Content Description
Three-panel figure on OOD detection: the problem, detection methods, and genomic OOD scenarios.

### DALL-E Prompt
```
Scientific illustration of out-of-distribution detection for genomic AI. Three panels.

PANEL A (The OOD Problem): Two distributions. Training distribution (blue, compact cluster). OOD region (red, outside cluster). Model making confident but unreliable predictions in OOD region. Annotation "Models extrapolate confidently where they shouldn't." Clinical example: African-ancestry patient when model trained on European data.

PANEL B (Detection Methods): Four approaches with icons:
1) Softmax confidence (simple but unreliable)
2) Energy-based (better calibrated)
3) Mahalanobis distance (embedding space)
4) Ensemble disagreement (multiple models)
For each: small visualization of how it works. Comparison of detection ROC curves.

PANEL C (Genomic OOD Scenarios): Grid showing scenarios:
- Novel gene families (distant from training)
- Underrepresented ancestries (population shift)
- Extreme variants (insertions, deletions, CNVs)
- Different cell types (tissue mismatch)
- Technical batch effects (sequencing platform)
For each: icon and brief description. Annotation "Must detect before clinical use."

Professional scientific illustration, distribution visualization style, white background.

Save as: 06-A-fig-ood-detection.svg through 06-C-fig-ood-detection.svg
```

### Post-Processing Notes
- Add specific detection threshold examples
- Include AUROC values for methods
- Show false positive/negative tradeoffs

### Fallback Description
"Out-of-distribution detection: models make confident but unreliable predictions outside training distribution. Detection methods include softmax confidence, energy scores, embedding distance, and ensemble disagreement. Genomic OOD scenarios include novel gene families, underrepresented ancestries, and different sequencing platforms."

### Caption Recommendation
"Out-of-distribution detection for safe deployment. (A) The OOD problem: models extrapolate confidently into regions where predictions are unreliable. (B) Detection methods: from simple softmax thresholds to sophisticated embedding-space approaches. (C) Genomic OOD scenarios: novel genes, underrepresented populations, unusual variant types, mismatched tissues, and technical batch effects—all require detection before clinical use."

---

## Figure 7: Selective Prediction

### Files
- `figs/part_5/ch23/07-fig-selective-prediction.svg`

### Priority
**Enhancing** - Practical deployment strategy

### Content Description
Selective prediction framework: abstaining on uncertain predictions to maintain accuracy on accepted predictions.

### DALL-E Prompt
```
Scientific illustration of selective prediction framework for clinical AI. Single panel with multiple elements.

TOP SECTION (The Concept): Flow diagram. Input query → Model → Confidence assessment → Decision gate: "Confident?" → If Yes: "Predict" (arrow to prediction). If No: "Abstain" (arrow to "Human review").

MIDDLE SECTION (Coverage-Accuracy Tradeoff): Plot with two curves. X-axis: Coverage (fraction of predictions made). Y-axis: Accuracy. One curve showing accuracy increasing as coverage decreases (being more selective). Operational point marked showing clinical threshold choice. Annotation "Tradeoff: higher accuracy requires rejecting more cases."

BOTTOM SECTION (Clinical Workflow): Three scenarios:
1) High confidence variant → Automated classification → Report
2) Moderate confidence → Flag for review → Expert decides
3) Low confidence → Abstain → Manual curation required
Icons for each pathway. Annotation "Selective prediction enables tiered clinical workflows."

INSET: Risk-coverage curve from real genomic model showing practical performance.

Professional scientific style, workflow diagram elements, white background.

Save as: 07-fig-selective-prediction.svg
```

### Post-Processing Notes
- Add specific accuracy/coverage numbers
- Include clinical workflow integration
- Show how thresholds are set

### Fallback Description
"Selective prediction: model abstains on uncertain predictions, routing them to human review. This enables high accuracy on accepted predictions at the cost of coverage. Clinical workflows can use confidence tiers to balance automation with human oversight."

### Caption Recommendation
"Selective prediction for clinical deployment. Rather than forcing predictions on all cases, models abstain when uncertainty exceeds a threshold, routing uncertain cases to human review. The coverage-accuracy tradeoff determines what fraction of cases are automated: higher accuracy requires accepting fewer cases. This enables tiered clinical workflows where confident predictions proceed automatically while uncertain cases receive expert attention."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Uncertainty Types | 2 | Essential | Low |
| Calibration Diagrams | 4 | Essential | Medium |
| Calibration Methods | 3 | High | Medium |
| UQ Methods Overview | 1 | High | High |
| Conformal Prediction | 1 | High | Medium |
| OOD Detection | 3 | High | Medium |
| Selective Prediction | 1 | Enhancing | Low |

## Recommended Generation Order
1. Uncertainty Types (conceptual foundation)
2. Calibration Diagrams (core visualization)
3. Calibration Methods (practical implementation)
4. UQ Methods Overview (survey)
5. OOD Detection (safety-critical)
6. Conformal Prediction (advanced method)
7. Selective Prediction (deployment strategy)
# Figure Report: Chapter 24 - Interpretability

**Chapter:** p5-ch24-interpretability.qmd
**Date:** 2026-01-07
**Total Figures:** 7 (13 files)
**Format:** SVG (for scalability)

---

## Figure 1: Attribution Methods Comparison

### Files
- `figs/part_5/ch24/01-fig-attribution-comparison.svg`

### Priority
**Essential** - Overview of attribution landscape

### Content Description
Comparison of attribution methods on the same input sequence showing agreement and disagreement between methods.

### DALL-E Prompt
```
Scientific illustration comparing attribution methods for genomic sequence interpretation. Single comprehensive panel.

TOP: DNA sequence displayed as horizontal bar with nucleotide letters (A, T, G, C colored).

FIVE ATTRIBUTION TRACKS BELOW (stacked):
1) Gradient × Input: Noisy track with scattered importance. Label "Fast, noisy."
2) Integrated Gradients: Smoother track with cleaner peaks. Label "Principled, slower."
3) DeepLIFT: Similar to IG but with different peak heights. Label "Reference-based."
4) Attention weights: Discrete peaks at specific positions. Label "What model attends (≠ importance)."
5) In silico mutagenesis (ISM): Clean gold-standard track. Label "Ground truth but expensive (3L passes)."

ANNOTATIONS:
- Circle regions where all methods agree → "High confidence important region"
- Circle regions where methods disagree → "Investigate further"
- Known motif (e.g., GATA box) highlighted with box

SIDE PANEL: Comparison table
| Method | Compute | Faithfulness | Best Use |
| Gradient×Input | 1 pass | Low-Med | Quick screen |
| Integrated Gradients | 10-50 passes | Med-High | Standard |
| DeepLIFT | 1 pass | Medium | Reference comparison |
| Attention | Free | Low | Exploration only |
| ISM | 3L passes | High | Validation |

Professional scientific illustration, genomic track visualization style, white background.

Save as: 01-fig-attribution-comparison.svg
```

### Post-Processing Notes
- Use real genomic sequence example
- Add correlation values between methods
- Highlight specific motifs

### Fallback Description
"Comparison of attribution methods on the same genomic sequence: Gradient × Input (fast, noisy), Integrated Gradients (principled), DeepLIFT (reference-based), attention weights (what model attends), and ISM (gold standard). Agreement across methods increases confidence; disagreement flags positions for investigation."

### Caption Recommendation
"Attribution methods comparison on a single genomic sequence. From top: Gradient × Input (fast but noisy), Integrated Gradients (principled with theoretical guarantees), DeepLIFT (reference-based attributions), attention weights (model attention ≠ importance), and in silico mutagenesis (ground truth but 3L forward passes). Regions where methods agree provide high-confidence importance; disagreement flags positions for closer investigation."

---

## Figure 2: In Silico Mutagenesis

### Files
- `figs/part_5/ch24/02-A-fig-in-silico-mutagenesis.svg`
- `figs/part_5/ch24/02-B-fig-in-silico-mutagenesis.svg`
- `figs/part_5/ch24/02-C-fig-in-silico-mutagenesis.svg`
- `figs/part_5/ch24/02-D-fig-in-silico-mutagenesis.svg`

### Priority
**High** - Gold standard method

### Content Description
Four-panel figure covering ISM procedure, output visualization, validation against experiments, and mechanistic insights.

### DALL-E Prompt
```
Scientific illustration of in silico mutagenesis for genomic model interpretation. Four panels.

PANEL A (ISM Procedure): Flow diagram. Reference sequence at top. At each position, systematically substitute all alternative nucleotides (A→T, A→G, A→C). Each mutant sequence through model. Compute prediction difference. Result: Position × Mutation matrix. Annotation "True counterfactual - direct model behavior."

PANEL B (ISM Profile Visualization): Heatmap aligned to sequence. Rows: positions. Columns: alternative nucleotides (or shown as 4×L matrix). Color scale: effect magnitude (blue negative, red positive). Functional regions show large effects (bright colors). Silent regions near zero (gray). Known binding site highlighted.

PANEL C (Validation Against DMS): Scatter plot comparing ISM predictions (x-axis) vs experimental deep mutational scanning measurements (y-axis). Correlation coefficient shown (r ~ 0.6-0.8). Points colored by position type (active site, surface, etc.). Annotation "ISM validated against experimental perturbations."

PANEL D (Mechanistic Insights Revealed): Three examples with icons:
1) Binding site boundaries: Sharp ISM signal edges define motif extent
2) Position-specific tolerance: Some positions tolerate mutations, others don't
3) Allele-specific effects: Different substitutions have different effects
Annotation "ISM reveals regulatory grammar."

Professional scientific style, heatmap visualization, white background.

Save as: 02-A-fig-in-silico-mutagenesis.svg through 02-D-fig-in-silico-mutagenesis.svg
```

### Post-Processing Notes
- Use realistic color scales
- Include specific position examples
- Add statistical annotations

### Fallback Description
"In silico mutagenesis workflow: systematically substitute each position to all alternatives, compute prediction changes, visualize as position × mutation matrix. Validation against deep mutational scanning shows ISM captures true functional effects. Mechanistic insights include binding site boundaries and position-specific tolerance."

### Caption Recommendation
"In silico mutagenesis (ISM). (A) Procedure: substitute each position to all alternatives, compute prediction difference. (B) Visualization: position × mutation heatmap with functional regions showing large effects. (C) Validation: ISM predictions correlate with experimental deep mutational scanning (r ≈ 0.6-0.8). (D) Mechanistic insights: ISM reveals binding site boundaries, position-specific tolerance, and allele-specific effects."

---

## Figure 3: TF-MoDISco Motif Discovery

### Files
- `figs/part_5/ch24/03-fig-tfmodisco.svg`

### Priority
**High** - Bridge from attributions to biology

### Content Description
TF-MoDISco pipeline from attribution scores to discovered motifs matched to known databases.

### DALL-E Prompt
```
Scientific illustration of TF-MoDISco motif discovery pipeline. Single comprehensive panel.

PIPELINE FLOW (left to right):

STAGE 1 (Attributions): Multiple sequence tracks with importance scores (from DeepLIFT, IG, or ISM). Annotation "Input: attribution scores for many sequences."

STAGE 2 (Seqlet Extraction): Highlighted windows where total importance exceeds threshold. Seqlets extracted as short sequences + importance profiles. Annotation "Extract high-importance windows."

STAGE 3 (Clustering): Seqlets grouped by sequence + importance similarity. Multiple clusters shown (different colors). Annotation "Cluster similar seqlets."

STAGE 4 (Motif Consolidation): Each cluster produces position weight matrix (shown as sequence logo) and importance-weighted logo. Clean motif visualizations.

STAGE 5 (Database Matching): Discovered motifs compared to JASPAR/HOCOMOCO. Match examples:
- Cluster 1 → CTCF (high match, known biology)
- Cluster 2 → GATA4 (high match)
- Cluster 3 → ??? (no match - novel pattern)

OUTPUT BOX: Motif vocabulary with sequence logos, match annotations, genomic usage statistics.

Annotation: "Key insight: Discovers what the MODEL learned, not just what's in the sequence."

Professional scientific style, sequence logo visualization, flowchart elements, white background.

Save as: 03-fig-tfmodisco.svg
```

### Post-Processing Notes
- Include real sequence logos
- Add match statistics
- Show composite motif examples

### Fallback Description
"TF-MoDISco pipeline: extract high-importance windows (seqlets) from attribution scores, cluster by sequence and importance similarity, consolidate into motifs, match to known databases. Discovers what the model actually learned—including novel patterns not in databases."

### Caption Recommendation
"TF-MoDISco motif discovery from attribution scores. Starting from attribution maps for many sequences, the method extracts high-importance windows (seqlets), clusters similar seqlets, consolidates into position weight matrices, and matches to known motif databases. Discovered motifs represent what the model learned—known transcription factors validate biological relevance while novel patterns may indicate previously unknown regulatory features."

---

## Figure 4: Attention Pattern Visualization

### Files
- `figs/part_5/ch24/04-A-fig-attention-visualization.svg`
- `figs/part_5/ch24/04-B-fig-attention-visualization.svg`
- `figs/part_5/ch24/04-C-fig-attention-visualization.svg`

### Priority
**High** - With critical caveats

### Content Description
Three-panel figure showing attention heatmaps, biological overlay, and multi-head specialization—with caveats about interpretation.

### DALL-E Prompt
```
Scientific illustration of attention pattern visualization in genomic transformers. Three panels.

PANEL A (Attention Heatmap): Position × position matrix from transformer attention. Color intensity shows attention weight. Patterns visible: diagonal (local), off-diagonal blocks (long-range), focal spots (specific interactions). Annotation "What the model 'looks at' - but attention ≠ importance."

PANEL B (Biological Overlay): Same attention pattern overlaid on genome browser-style track. Attention peaks aligned with known regulatory elements (promoter, enhancer, CTCF sites). Hi-C contact map comparison (triangular) showing similar patterns. Annotation "Sometimes aligns with biology..." Warning box: "But correlation ≠ causation. Validation required."

PANEL C (Multi-Head Specialization): Three attention heads side by side showing different patterns:
- Head 1: Local context (diagonal dominant) - "Captures nearby nucleotides"
- Head 2: Long-range (sparse off-diagonal) - "Distal interactions"
- Head 3: Motif-specific (focal spots) - "Specific sequence patterns"
Annotation "Different heads learn different computational roles."

CAVEAT BOX at bottom: "⚠️ Attention weights describe information routing, NOT causal contribution. High attention ≠ high importance. Always validate with perturbation experiments."

Professional scientific style, heatmap visualization, white background.

Save as: 04-A-fig-attention-visualization.svg through 04-C-fig-attention-visualization.svg
```

### Post-Processing Notes
- Use realistic attention patterns
- Add warning callouts
- Include validation examples

### Fallback Description
"Attention visualization in genomic transformers: attention heatmaps show position-position relationships, sometimes aligning with known regulatory elements. Different attention heads specialize for different patterns. Critical caveat: attention describes information routing, not causal importance—validation required."

### Caption Recommendation
"Attention patterns in genomic transformers. (A) Attention heatmap showing position-position weights with local and long-range patterns. (B) Biological overlay: attention sometimes aligns with regulatory elements—but correlation does not prove the model learned these relationships causally. (C) Multi-head specialization: different heads capture local context, long-range interactions, or specific motifs. **Caution**: attention weights describe information routing, not importance—always validate with perturbation experiments."

---

## Figure 5: Plausible vs Faithful Explanations

### Files
- `figs/part_5/ch24/05-fig-plausible-vs-faithful.svg`

### Priority
**Essential** - Core chapter concept

### Content Description
Two-path diagram contrasting plausible but unfaithful explanations with faithful explanations, using validation tests.

### DALL-E Prompt
```
Scientific illustration distinguishing plausible from faithful model explanations. Single panel with two paths.

CENTER: Model predicts "High enhancer activity" for genomic sequence.

PATH A (LEFT - PLAUSIBLE BUT UNFAITHFUL):
- Attribution highlights GATA motif (biologically reasonable)
- Annotation "Matches human intuition"
- BUT: Model actually learned GC content correlation (hidden)
- Validation tests FAIL:
  - Mutating GATA → no prediction change ✗
  - Inserting GATA → no prediction increase ✗
  - Random weights → similar attributions ✗
- Result: "False comfort - explanation matches intuition, not computation"
- Red warning color scheme

PATH B (RIGHT - FAITHFUL):
- Attribution highlights same GATA motif
- Model computation traces through GATA recognition
- Validation tests PASS:
  - Mutating GATA → prediction drops ✓
  - Inserting GATA → prediction increases ✓
  - Random weights → different attributions ✓
- Result: "Genuine insight - explanation reflects actual model behavior"
- Green success color scheme

BOTTOM: Validation hierarchy table:
1. Sanity check (random weights produce random attributions)
2. Necessity (ablating feature reduces prediction)
3. Sufficiency (inserting feature increases prediction)

KEY INSIGHT BOX: "Plausible = matches intuition. Faithful = reflects computation. They can diverge!"

Professional scientific style, two-path comparison, white background.

Save as: 05-fig-plausible-vs-faithful.svg
```

### Post-Processing Notes
- Make distinction visually clear
- Add specific test examples
- Include decision flowchart

### Fallback Description
"Plausible vs faithful explanations: a plausible explanation matches biological intuition (GATA motif highlighted) but may not reflect actual model computation (which learned GC content). Faithful explanations pass validation tests: ablating the feature changes prediction, inserting increases it. The distinction is critical for scientific discovery."

### Caption Recommendation
"Plausible versus faithful explanations. Both paths start with attributions highlighting a GATA motif. Left: plausible but unfaithful—the explanation matches intuition, but the model learned GC content; validation tests fail. Right: faithful—the model actually uses the GATA motif; validation tests pass. The distinction determines whether interpretability generates genuine insight or false comfort. Always validate: does ablating the feature change prediction? Does inserting it increase prediction?"

---

## Figure 6: Validation Pipeline

### Files
- `figs/part_5/ch24/06-fig-validation-pipeline.svg`

### Priority
**High** - Practical workflow

### Content Description
Circular workflow showing model → interpretability → hypothesis → validation → model refinement cycle.

### DALL-E Prompt
```
Scientific illustration of interpretability validation pipeline as circular workflow. Single panel.

CIRCULAR FLOW (clockwise):

STEP 1 (TOP): "Model Prediction"
- Neural network icon
- Output: prediction for genomic input

STEP 2 (RIGHT): "Interpretability Analysis"
- Attribution maps, TF-MoDISco, attention visualization icons
- Output: candidate important features

STEP 3 (BOTTOM RIGHT): "Hypothesis Generation"
- Statement: "GATA motif drives activity"
- Testable prediction formulated

STEP 4 (BOTTOM): "Experimental Validation"
Multiple test icons:
- EMSA (binding test)
- Reporter assay (activity test)
- CRISPR deletion (necessity test)
- MPRA (systematic test)

STEP 5 (BOTTOM LEFT): "Evaluate Results"
Branch point:
- Validated ✓ → Continue to refinement
- Failed ✗ → Identify limitation

STEP 6 (LEFT): "Model Refinement"
- Updated training, architecture insights
- Return to Step 1

CENTER: "Closed-loop discovery"

EXAMPLE PATHWAYS (annotated):
- "TF-MoDISco → EMSA confirms binding ✓"
- "Attention pattern → CRISPR confirms enhancer ✓"
- "GC attribution → MPRA shows no effect ✗ → confounder identified"

Professional scientific style, circular workflow diagram, white background.

Save as: 06-fig-validation-pipeline.svg
```

### Post-Processing Notes
- Add specific experiment details
- Include success/failure examples
- Show iteration numbers

### Fallback Description
"Interpretability validation pipeline: model prediction → interpretability analysis → hypothesis generation → experimental validation → evaluate results → model refinement. Validated hypotheses advance biology; failures identify model limitations or confounders. Closed-loop iteration improves both understanding and model quality."

### Caption Recommendation
"Closed-loop interpretability validation. Starting from model predictions, interpretability analysis generates hypotheses about important features. Experimental validation tests necessity (CRISPR deletion) and sufficiency (reporter assays). Validated hypotheses advance biological understanding; failures identify model limitations. This cycle progressively improves both mechanistic understanding and model reliability."

---

## Figure 7: Clinical Interpretability Workflow

### Files
- `figs/part_5/ch24/07-fig-clinical-interpretability.svg`

### Priority
**Enhancing** - Clinical translation

### Content Description
Clinical workflow showing how interpretability evidence strength maps to ACMG criteria.

### DALL-E Prompt
```
Scientific illustration of clinical interpretability for variant assessment. Single panel.

TOP SECTION (ACMG Evidence Framework):
- PP3: Computational supports pathogenic (weak)
- BP4: Computational supports benign (weak)
- Annotation "Evidence strength depends on interpretability"

MIDDLE SECTION (Three Evidence Levels):

LEVEL 1 (WEAK):
- Score only: "0.85 pathogenic"
- No mechanism provided
- ACMG weight: Supporting (weak)
- Icon: Simple number

LEVEL 2 (MODERATE):
- Score + attribution: "Disrupts splice site"
- SpliceAI prediction shown
- Can evaluate against transcript data
- ACMG weight: Supporting (moderate)
- Icon: Score + mechanism

LEVEL 3 (STRONG):
- Score + validated mechanism
- "Disrupts CTCF binding"
- ChIP confirms binding loss
- 3D genome shows disrupted contact
- Minigene assay confirms
- ACMG weight: Strong supporting
- Icon: Multi-evidence integration

BOTTOM SECTION (Clinical Report Elements):
Example report snippet showing:
- Variant annotation
- Score with uncertainty bars
- Mechanistic hypothesis
- Supporting evidence
- Conflicting evidence
- Recommended follow-up

Professional clinical/medical style, evidence hierarchy visualization, white background.

Save as: 07-fig-clinical-interpretability.svg
```

### Post-Processing Notes
- Add specific variant examples
- Include ACMG code references
- Show report template

### Fallback Description
"Clinical interpretability workflow: evidence strength for ACMG criteria depends on interpretability level. Score alone provides weak evidence; score plus mechanism (e.g., splice site disruption) is moderate; score with validated mechanism (binding loss, functional assay) is strong. Clinical reports should include score, mechanism, uncertainty, and recommended follow-up."

### Caption Recommendation
"Interpretability for clinical variant assessment. ACMG evidence strength depends on interpretability: a pathogenicity score alone (PP3/BP4 supporting) provides weak evidence; a score with mechanistic explanation (splice site disruption) is moderate; a score with experimentally validated mechanism (ChIP-confirmed binding loss, functional assay) is strong. Clinical reports should communicate the mechanism, not just the score, to enable evidence integration."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Attribution Comparison | 1 | Essential | Medium |
| In Silico Mutagenesis | 4 | High | Medium |
| TF-MoDISco | 1 | High | High |
| Attention Visualization | 3 | High | Medium |
| Plausible vs Faithful | 1 | Essential | Low |
| Validation Pipeline | 1 | High | Medium |
| Clinical Interpretability | 1 | Enhancing | Medium |

## Recommended Generation Order
1. Plausible vs Faithful (core concept)
2. Attribution Comparison (method overview)
3. In Silico Mutagenesis (gold standard)
4. TF-MoDISco (motif discovery)
5. Attention Visualization (with caveats)
6. Validation Pipeline (practical workflow)
7. Clinical Interpretability (translation)
# Figure Report: Chapter 25 - Causal Inference with Foundation Models

**Chapter:** p5-ch25-causal.qmd
**Date:** 2026-01-07
**Total Figures:** 4 (4 files)
**Format:** SVG (for scalability)

---

## Figure 1: Ladder of Causation

### Files
- `figs/part_5/ch25/01-fig-ladder-causation.svg`

### Priority
**High** - Core conceptual framework

### Content Description
Pearl's ladder of causation applied to genomics, showing the qualitative distinction between association, intervention, and counterfactual reasoning.

### DALL-E Prompt
```
Scientific illustration of Pearl's ladder of causation applied to genomics. Single panel with three-level ladder structure.

LADDER STRUCTURE (bottom to top):

RUNG 1 (BOTTOM - ASSOCIATION):
- Question: "What does seeing X tell me about Y?"
- Genomic example: "Observing variant V, predict phenotype P"
- Icon: Correlation scatter plot, eye symbol
- Foundation models operate here ← highlighted
- Annotation "P(Y|X) - observational"

RUNG 2 (MIDDLE - INTERVENTION):
- Question: "What happens to Y if I change X?"
- Genomic example: "If we edit variant V, what happens to P?"
- Icon: CRISPR scissors, do() operator
- Perturbation experiments provide ground truth ← highlighted
- Annotation "P(Y|do(X)) - interventional"
- Requires causal structure knowledge

RUNG 3 (TOP - COUNTERFACTUAL):
- Question: "What would Y have been if X had been different?"
- Genomic example: "For this patient with V who developed P, would they have developed P without V?"
- Icon: Parallel universes, individual person
- Individual-level reasoning
- Annotation "P(Y_x|X=x', Y=y) - counterfactual"

GAPS BETWEEN RUNGS (emphasized):
- Gap 1→2: "Cannot cross with more data alone"
- Gap 2→3: "Requires individual-level noise models"

SIDE BOX: "Key insight: Rung 1 accuracy does NOT guarantee Rung 2 accuracy. The gap is qualitative, not quantitative."

Professional scientific style, ladder visualization, blue/green/purple color progression, white background.

Save as: 01-fig-ladder-causation.svg
```

### Post-Processing Notes
- Add mathematical notation
- Include specific genomic examples
- Emphasize the qualitative gaps

### Fallback Description
"Pearl's ladder of causation: Rung 1 (association) asks what observing X tells us about Y—foundation models operate here. Rung 2 (intervention) asks what happens if we change X—requires causal structure. Rung 3 (counterfactual) asks what would have happened for a specific individual. The gaps between rungs are qualitative—more data cannot bridge them."

### Caption Recommendation
"Pearl's ladder of causation applied to genomics. **Rung 1 (Association)**: Foundation models learn P(Y|X)—observing variant V, predict phenotype P. **Rung 2 (Intervention)**: P(Y|do(X))—if we edit V, what happens to P? Requires causal structure, not just correlations. **Rung 3 (Counterfactual)**: For this specific patient, what would have happened under alternative conditions? The gaps are qualitative: predictive accuracy at Rung 1 provides no guarantee of accuracy at Rungs 2-3."

---

## Figure 2: GWAS to Causal Gene Pipeline

### Files
- `figs/part_5/ch25/02-fig-gwas-to-gene.svg`

### Priority
**High** - Key genomics application

### Content Description
Pipeline from GWAS signal to causal gene identification, showing where foundation models contribute.

### DALL-E Prompt
```
Scientific illustration of GWAS-to-causal-gene pipeline. Single horizontal flow panel.

STAGE 1 (LEFT - GWAS Signal):
- Manhattan plot showing genome-wide peaks
- Zoom into one locus
- Many correlated variants in LD (linkage disequilibrium block)
- Annotation "Associated locus - but which variant is causal?"

STAGE 2 (Fine-Mapping):
- Same locus with posterior probabilities
- Statistical fine-mapping narrows to credible set
- FM predictions overlay (chromatin, binding, splicing effects)
- Credible set: 3-5 variants highlighted
- Annotation "Foundation models provide functional annotations"

STAGE 3 (Gene Assignment - Multiple Evidence):
Three parallel evidence tracks:
1) eQTL colocalization: "Variant affects Gene B expression"
2) Chromatin contacts (Hi-C): "Variant in enhancer contacting Gene B promoter"
3) FM variant effect predictions: "Variant disrupts regulatory element controlling Gene B"
Convergence arrows pointing to Gene B

STAGE 4 (RIGHT - Experimental Validation):
- CRISPR perturbation icon
- Allele-specific expression measurement
- Reporter assay
- Annotation "Ground truth from intervention"

BOTTOM: Evidence integration scoring showing confidence levels

FOUNDATION MODEL CONTRIBUTION highlighted at Stages 2-3 with boxes

Professional scientific style, pipeline flow diagram, white background.

Save as: 02-fig-gwas-to-gene.svg
```

### Post-Processing Notes
- Add specific gene examples
- Include statistical metrics
- Show integration scoring

### Fallback Description
"GWAS-to-causal-gene pipeline: GWAS identifies associated locus with many correlated variants, fine-mapping with FM annotations narrows to credible set, multiple evidence (eQTL, chromatin contacts, FM predictions) prioritizes target gene, experimental validation provides ground truth. Foundation models contribute at fine-mapping and gene assignment stages."

### Caption Recommendation
"From GWAS to causal gene. **Stage 1**: GWAS identifies associated locus with multiple variants in linkage disequilibrium. **Stage 2**: Fine-mapping with foundation model functional annotations narrows to credible set. **Stage 3**: Multiple evidence integration—eQTL colocalization, chromatin contacts, FM variant predictions—prioritizes target gene. **Stage 4**: Experimental validation provides causal ground truth. Foundation models accelerate stages 2-3 but cannot substitute for experimental validation."

---

## Figure 3: Closed-Loop Causal Learning

### Files
- `figs/part_5/ch25/03-fig-closed-loop-causal.svg`

### Priority
**High** - Path forward for causal FM

### Content Description
Design-build-test-learn cycle showing how foundation models can acquire causal knowledge through experimental iteration.

### DALL-E Prompt
```
Scientific illustration of closed-loop causal learning for foundation models. Circular flow diagram.

MAIN CYCLE (clockwise):

STEP 1 (TOP - PREDICT):
- Foundation model icon
- "Predict intervention effects based on current knowledge"
- Output: ranked list of candidate interventions
- Annotation "Initial predictions may be merely associational"

STEP 2 (RIGHT - EXPERIMENT):
- Automated platform icon (robot arm, plate)
- "Execute prioritized interventions"
- Examples: CRISPR perturbation, drug treatment, regulatory editing
- Throughput annotation: "100s-1000s per cycle"

STEP 3 (BOTTOM - OBSERVE):
- Readout icons: expression profiles, cell viability, phenotype measurements
- "Capture interventional outcomes"
- Data flowing to database

STEP 4 (LEFT - UPDATE):
- Model update icon
- "Retrain/fine-tune on interventional data"
- "Causal accuracy improves"
- Arrow back to Step 1

CENTER: "Each cycle adds interventional ground truth"

CONTRAST BOX (bottom):
Left side: "Standard FM training" - fixed observational data → associational patterns only
Right side: "Closed-loop training" - iterative interventional data → progressively causal knowledge

KEY INSIGHT: "Moving from Rung 1 to Rung 2 requires interventional data. Closed-loop provides it."

Professional scientific style, circular workflow, blue/green color scheme, white background.

Save as: 03-fig-closed-loop-causal.svg
```

### Post-Processing Notes
- Add specific throughput numbers
- Include real experimental examples
- Show learning curves

### Fallback Description
"Closed-loop causal learning: foundation model predicts intervention effects, automated platform executes interventions, readouts captured, model updated with interventional data. Each cycle adds ground truth that progressively shifts the model from associational (Rung 1) toward causal (Rung 2) knowledge—unlike standard training on fixed observational data."

### Caption Recommendation
"Closed-loop causal learning for foundation models. The cycle iterates between: (1) Predicting intervention effects from current knowledge, (2) Executing prioritized interventions on automated platforms, (3) Capturing experimental readouts, and (4) Updating the model with interventional data. Unlike standard training on observational data, closed-loop systems accumulate interventional ground truth that progressively improves causal accuracy—providing a path from Rung 1 (association) toward Rung 2 (intervention) of the causal ladder."

---

## Figure 4: Evidence Hierarchy for Drug Target Validation

### Files
- `figs/part_5/ch25/04-fig-evidence-hierarchy.svg`

### Priority
**Medium** - Clinical translation context

### Content Description
Pyramid showing evidence hierarchy from weakest (association) to strongest (clinical trials), with FM contribution highlighted.

### DALL-E Prompt
```
Scientific illustration of drug target validation evidence hierarchy. Pyramid structure with four levels.

PYRAMID (bottom to top):

LEVEL 1 (BOTTOM - WEAKEST - ASSOCIATION):
- Width: widest
- Content: "Observational association"
- Examples: "Expression correlates with disease", "FM prediction of target involvement"
- Foundation models operate here ← highlighted box
- Confidence: Low
- Color: Light blue

LEVEL 2 (MENDELIAN RANDOMIZATION):
- Content: "Human genetic evidence"
- Examples: "Genetic variant affecting target associated with disease outcome", "MR supports causal relationship"
- Annotation "Natural experiment from genetic randomization"
- Confidence: Moderate
- Color: Medium blue

LEVEL 3 (EXPERIMENTAL PERTURBATION):
- Content: "Direct causal test in models"
- Examples: "CRISPR KO affects disease phenotype", "Drug inhibition in animal model"
- Annotation "Interventional ground truth in model systems"
- Confidence: High
- Color: Darker blue

LEVEL 4 (TOP - STRONGEST - CLINICAL TRIAL):
- Width: narrowest
- Content: "Clinical intervention efficacy"
- Examples: "Phase III trial shows drug efficacy"
- Annotation "Definitive but expensive and slow"
- Confidence: Highest
- Color: Dark blue

SIDE ARROWS showing where FM contributes:
- Association discovery ← FM strong
- MR instrument selection ← FM helps
- Perturbation prioritization ← FM helps
- Clinical validation ← FM cannot substitute

BOTTOM BOX: "Key insight: FMs accelerate early stages but cannot replace later validation. Moving up the pyramid requires non-computational evidence."

Professional scientific style, pyramid diagram, blue gradient, white background.

Save as: 04-fig-evidence-hierarchy.svg
```

### Post-Processing Notes
- Add specific drug examples
- Include timeline estimates
- Show cost considerations

### Fallback Description
"Drug target validation evidence hierarchy: from weakest (observational association—where FMs operate) through Mendelian randomization (human genetic evidence) and experimental perturbation (direct causal test) to strongest (clinical trial efficacy). Foundation models accelerate early stages but cannot substitute for later experimental and clinical validation."

### Caption Recommendation
"Evidence hierarchy for drug target validation. **Weakest**: observational association—foundation models excel here but associations may be confounded. **Moderate**: Mendelian randomization provides human in-vivo causal evidence. **Strong**: Experimental perturbation directly tests causation in model systems. **Strongest**: Clinical trial efficacy is definitive but expensive. Foundation models accelerate association discovery, MR instrument selection, and perturbation prioritization, but cannot substitute for the experimental and clinical evidence required for confident target validation."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Ladder of Causation | 1 | High | Medium |
| GWAS to Gene Pipeline | 1 | High | High |
| Closed-Loop Causal Learning | 1 | High | Medium |
| Evidence Hierarchy | 1 | Medium | Low |

## Recommended Generation Order
1. Ladder of Causation (conceptual foundation)
2. Evidence Hierarchy (clinical context)
3. GWAS to Gene Pipeline (genomics application)
4. Closed-Loop Causal Learning (path forward)
# Figure Report: Chapter 26 - Regulatory and Governance

**Chapter:** p5-ch26-regulatory.qmd
**Date:** 2026-01-07
**Total Figures:** 2 (5 files)
**Format:** SVG (for scalability)

---

## Figure 1: Data Governance Challenges

### Files
- `figs/part_5/ch26/01-A-fig-data-governance.svg`
- `figs/part_5/ch26/01-B-fig-data-governance.svg`
- `figs/part_5/ch26/01-C-fig-data-governance.svg`
- `figs/part_5/ch26/01-D-fig-data-governance.svg`

### Priority
**High** - Multi-faceted governance landscape

### Content Description
Four-panel figure covering privacy-utility tradeoff, consent complexity, federated learning, and cross-border regulatory issues.

### DALL-E Prompt
```
Scientific illustration of data governance challenges for genomic AI. Four panels.

PANEL A (Privacy vs Utility Tradeoff):
Two-axis plot. X-axis: "Privacy protection" (low to high). Y-axis: "Model utility" (low to high). Curve showing tradeoff (as privacy increases, utility decreases). Points on curve:
- "Identified data" (high utility, low privacy)
- "Anonymized" (moderate both)
- "Differential privacy ε=1" (moderate-high privacy, lower utility)
- "DP ε=0.1" (high privacy, low utility)
Annotation "No free lunch - privacy costs utility"

PANEL B (Consent Complexity):
Comparison diagram of consent models:
- Broad consent: Wide funnel, "All future research", simple checkmark
- Specific consent: Narrow funnel, "Named studies only", detailed list
- Tiered consent: Multiple streams, "Choose categories"
- Dynamic consent: Interactive loop, "Ongoing engagement"
For each: Pros/cons annotation (autonomy, utility, burden)

PANEL C (Federated Learning):
Schematic showing 3 hospitals/biobanks (icons). Data stays local (databases highlighted). Model travels between sites (gradient arrows). Central aggregator combines updates. Privacy-preserving computation annotation. Warning: "Gradient attacks still possible" - citation to Zhu et al.

PANEL D (Cross-Border Regulatory):
World map with key regions highlighted: US (HIPAA, FDA), EU (GDPR, MDR, AI Act), Japan (PMDA), Australia (TGA). Different rules icons. Arrows showing data flow challenges. "Data localization requirements" annotation. Harmonization efforts noted (IMDRF).

Professional scientific style, infographic elements, white background.

Save as: 01-A-fig-data-governance.svg through 01-D-fig-data-governance.svg
```

### Post-Processing Notes
- Add specific epsilon values for DP
- Include regulation citations
- Show practical examples

### Fallback Description
"Data governance challenges: privacy-utility tradeoff curve showing increasing privacy reduces model utility; consent model comparison from broad to dynamic; federated learning architecture with data-local model-travels design; cross-border regulatory complexity with different rules across US, EU, and other jurisdictions."

### Caption Recommendation
"Data governance challenges for genomic foundation models. (A) Privacy-utility tradeoff: stronger privacy protection (e.g., differential privacy with small ε) reduces model utility—there is no free lunch. (B) Consent complexity: models range from broad (simple, enables innovation) to dynamic (responsive, resource-intensive). (C) Federated learning: data stays local while model updates travel, but gradient attacks remain a risk. (D) Cross-border complexity: different jurisdictions (HIPAA, GDPR, MDR) impose different requirements, complicating global deployment."

---

## Figure 2: Dual-Use Risk Assessment

### Files
- `figs/part_5/ch26/02-fig-dual-use-governance.svg`

### Priority
**High** - Biosecurity considerations

### Content Description
Risk assessment matrix for generative genomic models, showing capability × access considerations and governance mechanisms.

### DALL-E Prompt
```
Scientific illustration of dual-use risk assessment for generative genomic models. Single comprehensive panel.

MAIN ELEMENT (Risk Matrix):
2×2 grid with axes:
- X-axis: "Model Capability" (Low → High)
- Y-axis: "Access Openness" (Restricted → Open)

Quadrants:
- Bottom-left (Low capability, Restricted): "Current academic research" - Green, low risk
- Bottom-right (High capability, Restricted): "Industrial deployment with oversight" - Yellow, moderate risk
- Top-left (Low capability, Open): "Open-source educational tools" - Green, low risk
- Top-right (High capability, Open): "HIGHEST CONCERN" - Red, high risk

RISK FACTORS (side panel):
Icons with labels:
- Pathogen enhancement potential
- Antibiotic resistance design
- Agricultural biosecurity
- Emergent/unexpected capabilities
- Detection evasion

GOVERNANCE MECHANISMS (bottom panel):
Timeline/checklist:
1) Pre-release capability evaluation - "Probe for concerning capabilities"
2) Staged/tiered release - "Limit access to most capable models"
3) Usage monitoring - "Track for misuse indicators"
4) Audit trails - "Log queries and outputs"
5) Benefit-risk assessment - "Weigh scientific value against harm potential"

KEY INSIGHT BOX: "Gap between computational generation and biological realization provides some protection, but that gap is narrowing."

BALANCE SCALE icon showing "Open science benefits" vs "Misuse risks"

Professional scientific style, risk matrix format, red/yellow/green color coding, white background.

Save as: 02-fig-dual-use-governance.svg
```

### Post-Processing Notes
- Add specific risk examples
- Include mitigation strategies
- Show decision framework

### Fallback Description
"Dual-use risk assessment matrix: capability × access determines risk level. Low capability or restricted access is lower risk; high capability with open access is highest concern. Risk factors include pathogen design and emergent capabilities. Governance mechanisms include pre-release evaluation, staged release, and usage monitoring. The gap between computation and realization provides some protection."

### Caption Recommendation
"Dual-use risk assessment for generative genomic models. The risk matrix considers model capability and access openness: high-capability models with open access pose the greatest concern. Risk factors include pathogen enhancement, resistance design, and emergent capabilities. Governance mechanisms span the deployment lifecycle: pre-release evaluation, staged release, usage monitoring, and audit trails. The gap between computational generation and biological realization provides some natural protection, but this gap narrows as both computational and wetlab capabilities advance. Responsible development requires ongoing benefit-risk assessment."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Data Governance | 4 | High | High |
| Dual-Use Risk | 1 | High | Medium |

## Recommended Generation Order
1. Data Governance (comprehensive landscape)
2. Dual-Use Risk (biosecurity context)

## Note on File Path

The chapter references figure paths in `figs/part_6/ch29/` which appears to be from a previous chapter numbering. The correct paths based on current structure should be `figs/part_5/ch26/`. The figures listed above use the corrected paths.
# Figure Report: Chapter 27 - Clinical Risk Prediction

**Chapter:** p6-ch27-clinical-risk.qmd
**Date:** 2026-01-07
**Total Figures:** 7 (14 files)
**Format:** SVG (for scalability)

---

## Figure 1: Feature Integration Layers

### Files
- `figs/part_6/ch27/01-A-fig-feature-integration.svg`
- `figs/part_6/ch27/01-B-fig-feature-integration.svg`
- `figs/part_6/ch27/01-C-fig-feature-integration.svg`

### Priority
**Essential** - Core architecture concept

### Content Description
Three-panel figure showing how different foundation model features integrate for clinical risk: genomic features, expression features, and coding variant features.

### DALL-E Prompt
```
Scientific illustration of feature integration for clinical risk prediction. Three panels.

PANEL A (Genomic Features - DNA FMs):
Flow diagram. Input: Patient genome sequence. Through Enformer/Sei-style model. Outputs: Regulatory effect scores, chromatin predictions, enhancer activity. Specific features extracted: PRS enhancement, regulatory variant effects, non-coding risk. Arrow to integration layer.

PANEL B (Expression Features - scRNA FMs):
Flow diagram. Input: Patient expression profile (blood/tissue). Through Geneformer/scGPT-style model. Outputs: Cell state embeddings, pathway activities, expression signatures. Features: Current disease state, response biomarkers, cell type composition. Arrow to integration layer.

PANEL C (Coding Variant Features - Protein FMs):
Flow diagram. Input: Patient missense variants. Through ESM/AlphaMissense-style model. Outputs: Pathogenicity scores, structural effects, functional impact. Features: Monogenic risk, carrier status, modifier effects. Arrow to integration layer.

BOTTOM: Integration layer combining all three into unified risk score with confidence interval.

Professional scientific style, neural network diagram elements, patient-centric visualization, white background.

Save as: 01-A-fig-feature-integration.svg through 01-C-fig-feature-integration.svg
```

### Post-Processing Notes
- Add specific model names
- Include feature dimensionalities
- Show integration architecture

### Fallback Description
"Feature integration for clinical risk: DNA foundation models provide regulatory and non-coding variant effects, expression models provide current state and pathway activities, protein models provide coding variant pathogenicity. Integration combines all layers into unified risk prediction with uncertainty."

### Caption Recommendation
"Feature integration for clinical risk prediction. (A) DNA foundation models contribute regulatory variant effects, enhancer predictions, and PRS enhancement. (B) Expression foundation models provide cell state embeddings, pathway activities, and disease signatures. (C) Protein foundation models add coding variant pathogenicity and structural effects. Integration combines features across modalities for unified risk prediction with calibrated uncertainty."

---

## Figure 2: Temporal Modeling

### Files
- `figs/part_6/ch27/02-A-fig-temporal-modeling.svg`
- `figs/part_6/ch27/02-B-fig-temporal-modeling.svg`
- `figs/part_6/ch27/02-C-fig-temporal-modeling.svg`

### Priority
**High** - Important for longitudinal prediction

### Content Description
Three-panel figure on temporal dynamics: static vs dynamic risk, longitudinal trajectory modeling, and updating predictions over time.

### DALL-E Prompt
```
Scientific illustration of temporal modeling for clinical risk. Three panels.

PANEL A (Static vs Dynamic Risk):
Two timelines side by side. Left (Static): Single risk score from birth, horizontal line, genetic risk only. Right (Dynamic): Risk trajectory that changes over time, incorporating biomarkers, interventions, lifestyle. Annotation "Genetics sets trajectory; environment and intervention modify it."

PANEL B (Longitudinal Trajectory):
Patient timeline with multiple measurements. Markers: genomic baseline (time 0), lab values (periodic), imaging (annual), symptoms (event-driven). Model updating risk at each timepoint. Confidence intervals widening into future. Recurrent/transformer architecture icon processing sequence.

PANEL C (Prediction Updating):
Example: cardiac risk patient. Initial PRS-based risk (moderate). +Lab abnormality → risk increases. +Medication started → risk decreases. +New symptom → risk increases. Shows Bayesian updating process with posterior narrowing as evidence accumulates.

Professional clinical style, timeline visualizations, patient journey representation, white background.

Save as: 02-A-fig-temporal-modeling.svg through 02-C-fig-temporal-modeling.svg
```

### Post-Processing Notes
- Add specific clinical measurements
- Include confidence intervals
- Show intervention effects

### Fallback Description
"Temporal modeling for clinical risk: static genetic risk versus dynamic risk that incorporates longitudinal measurements, trajectory modeling with sequential observations and widening uncertainty into future, and Bayesian updating as new evidence accumulates."

### Caption Recommendation
"Temporal dynamics in clinical risk prediction. (A) Static versus dynamic risk: genetic risk sets baseline trajectory while environmental factors and interventions modify it over time. (B) Longitudinal trajectory modeling: sequential observations (labs, imaging, symptoms) update risk predictions with widening uncertainty into the future. (C) Prediction updating: Bayesian framework incorporates new evidence, adjusting risk as interventions and events occur."

---

## Figure 3: Validation Hierarchy

### Files
- `figs/part_6/ch27/03-fig-validation-hierarchy.svg`

### Priority
**Essential** - Validation framework

### Content Description
Pyramid showing validation levels from internal holdout through prospective interventional trials.

### DALL-E Prompt
```
Scientific illustration of clinical validation hierarchy as pyramid. Single panel.

PYRAMID (bottom to top, widest to narrowest):

LEVEL 1 (BOTTOM - Internal Holdout):
- "Train/test split from same dataset"
- Easiest, most common
- Risk: Overestimates real-world performance
- Color: Light gray

LEVEL 2 (External Retrospective):
- "Held-out institution or time period"
- Tests generalization
- Risk: Distribution shift undetected
- Color: Light blue

LEVEL 3 (Prospective Observational):
- "Silent deployment alongside clinical care"
- Real-time performance monitoring
- Detects drift
- Color: Medium blue

LEVEL 4 (Prospective Interventional):
- "Randomized trial of model-guided care"
- Definitive but expensive
- Measures clinical utility
- Color: Dark blue

LEVEL 5 (TOP - Long-term Outcomes):
- "Multi-year follow-up"
- Ultimate validation
- Rarely achieved
- Color: Darkest blue

SIDE ANNOTATIONS:
- Arrow showing "Evidence strength increases"
- Arrow showing "Cost/time increases"
- Specific metrics at each level (AUC, calibration, NRI, clinical endpoints)

Foundation model contribution noted at each level.

Professional scientific style, pyramid diagram, blue gradient, white background.

Save as: 03-fig-validation-hierarchy.svg
```

### Post-Processing Notes
- Add specific metrics
- Include timeline estimates
- Show regulatory implications

### Fallback Description
"Validation hierarchy from internal holdout (easiest, overestimates performance) through external retrospective (tests generalization), prospective observational (real-time monitoring), prospective interventional (randomized trials), to long-term outcomes (ultimate validation). Evidence strength and cost/time increase together."

### Caption Recommendation
"Clinical validation hierarchy. From bottom: internal holdout validation is easiest but overestimates deployment performance; external retrospective validation tests generalization across institutions; prospective observational validation monitors real-time performance without influencing care; prospective interventional trials demonstrate clinical utility through randomized comparisons; long-term outcome tracking provides ultimate validation but is rarely achieved. Each level requires greater investment but provides stronger evidence."

---

## Figure 4: Clinical Uncertainty Communication

### Files
- `figs/part_6/ch27/04-fig-clinical-uncertainty.svg`

### Priority
**High** - Critical for clinical use

### Content Description
How to communicate uncertainty to clinicians and patients: point estimates vs intervals, visual formats, and decision support.

### DALL-E Prompt
```
Scientific illustration of clinical uncertainty communication. Single panel with multiple elements.

TOP SECTION (Bad vs Good Communication):
Left (BAD): "Your risk is 23%" - single number, no context
Right (GOOD): "Your risk is 18-28% (most likely 23%)" - interval with best estimate

MIDDLE SECTION (Visual Formats):
Three visualization options:
1) Icon array: 100 person icons, 23 highlighted
2) Risk thermometer: Vertical scale with marker and CI band
3) Risk comparison: "Similar to..." contextual comparisons
For each: annotation of effectiveness and when to use

BOTTOM SECTION (Decision Support Integration):
Clinical decision interface mockup showing:
- Risk estimate with confidence interval
- Uncertainty flag if OOD or miscalibrated
- Threshold-based recommendations (green/yellow/red zones)
- "What would change the prediction?" sensitivity analysis

CALLOUT BOX: "Key insight: Communicating uncertainty is as important as the prediction itself. Overconfident predictions without uncertainty → clinical harm."

Professional clinical/medical style, user interface elements, white background.

Save as: 04-fig-clinical-uncertainty.svg
```

### Post-Processing Notes
- Add specific clinical examples
- Include user testing data
- Show different audience formats

### Fallback Description
"Clinical uncertainty communication: bad practice (single point estimate) versus good practice (interval with best estimate), visual formats (icon arrays, thermometers, comparisons), and decision support integration showing risk with confidence interval, uncertainty flags, and threshold-based recommendations."

### Caption Recommendation
"Communicating uncertainty in clinical risk prediction. Single point estimates without context can mislead; intervals with best estimates provide actionable uncertainty. Visual formats include icon arrays (intuitive for patients), risk thermometers (familiar to clinicians), and contextual comparisons. Decision support should integrate uncertainty directly: flagging predictions with high epistemic uncertainty, showing confidence bands around thresholds, and providing sensitivity analysis."

---

## Figure 5: Fairness Assessment

### Files
- `figs/part_6/ch27/05-A-fig-fairness-assessment.svg`
- `figs/part_6/ch27/05-B-fig-fairness-assessment.svg`
- `figs/part_6/ch27/05-C-fig-fairness-assessment.svg`
- `figs/part_6/ch27/05-D-fig-fairness-assessment.svg`

### Priority
**High** - Equity and bias

### Content Description
Four-panel figure on fairness: ancestry-stratified performance, calibration by group, sources of bias, and mitigation strategies.

### DALL-E Prompt
```
Scientific illustration of fairness assessment for clinical genomic AI. Four panels.

PANEL A (Ancestry-Stratified Performance):
Bar chart showing model AUC by ancestry group. European: 0.85. East Asian: 0.82. South Asian: 0.79. African: 0.72. Hispanic/Latino: 0.75. Aggregate (misleading): 0.83. Annotation "Aggregate metrics mask disparities."

PANEL B (Calibration by Group):
Four reliability diagrams (small) for different ancestry groups. European: well-calibrated (on diagonal). African: overconfident for some ranges. Visual showing calibration varies across groups.

PANEL C (Sources of Bias):
Flow diagram showing bias accumulation. Training data (European-dominated GWAS) → Model (learns European-specific patterns) → Features (EHR, lab norms, coding practices) → Deployment (different populations). Each stage adds bias. Annotation "Bias accumulates through pipeline."

PANEL D (Mitigation Strategies):
Four strategies with icons:
1) Stratified evaluation (required disclosure)
2) Reweighting/resampling during training
3) Calibration adjustment by group
4) Uncertainty flagging for underrepresented groups
For each: effectiveness and limitations noted.

Professional scientific style, disaggregated visualizations, white background.

Save as: 05-A-fig-fairness-assessment.svg through 05-D-fig-fairness-assessment.svg
```

### Post-Processing Notes
- Use realistic performance gaps
- Add statistical confidence intervals
- Include policy recommendations

### Fallback Description
"Fairness assessment: ancestry-stratified performance shows disparities masked by aggregate metrics, calibration varies across groups with overconfidence for underrepresented populations, bias accumulates from training data through deployment, and mitigation strategies include stratified evaluation, reweighting, calibration adjustment, and uncertainty flagging."

### Caption Recommendation
"Fairness assessment in clinical genomic AI. (A) Ancestry-stratified performance reveals disparities masked by aggregate metrics—African ancestry AUC significantly lower than European. (B) Calibration varies by group: models may be overconfident for underrepresented populations. (C) Bias accumulates: European-dominated training data leads to models that underperform on other populations, compounded by EHR biases. (D) Mitigation strategies: stratified evaluation disclosure, training reweighting, group-specific calibration, and uncertainty flagging for underrepresented inputs."

---

## Figure 6: Clinical Workflow Integration

### Files
- `figs/part_6/ch27/06-fig-clinical-workflow.svg`

### Priority
**High** - Deployment reality

### Content Description
How foundation model predictions integrate into clinical workflows: timing, display, action triggers.

### DALL-E Prompt
```
Scientific illustration of clinical workflow integration for genomic risk prediction. Single panel with workflow diagram.

WORKFLOW STAGES (left to right):

STAGE 1 (Data Collection):
- EHR icon
- Genomic test ordered
- Samples collected
Timeline: Days 1-3

STAGE 2 (Processing):
- Lab processing icon
- Bioinformatics pipeline
- FM inference runs
Timeline: Days 3-10

STAGE 3 (Result Generation):
- Risk score computed
- Uncertainty quantified
- Clinical report generated
Timeline: Day 10

STAGE 4 (Clinical Review):
- Results appear in EHR
- Clinician reviews with context
- Alert if high-risk (BPA)
Decision point: Act or wait?

STAGE 5 (Action):
Branch based on risk:
- High risk → Specialist referral, intervention
- Moderate → Increased surveillance
- Low → Routine care
- Uncertain → Additional testing

INTEGRATION POINTS highlighted:
- Where FM contributes
- Human oversight checkpoints
- Patient communication moments

BOTTOM: Barriers to adoption (compute access, reimbursement, liability, clinician trust)

Professional clinical workflow style, healthcare iconography, white background.

Save as: 06-fig-clinical-workflow.svg
```

### Post-Processing Notes
- Add specific EHR integration examples
- Include timing estimates
- Show regulatory touchpoints

### Fallback Description
"Clinical workflow integration: data collection (EHR, samples), processing (sequencing, FM inference), result generation (risk with uncertainty), clinical review (EHR display, alerts), and action (tiered based on risk level). Integration points highlight FM contribution, human oversight, and adoption barriers."

### Caption Recommendation
"Clinical workflow integration for genomic risk prediction. From data collection through processing, result generation, clinical review, and action. Foundation models contribute during processing and result generation. Human oversight checkpoints ensure clinician review before action. Adoption barriers include compute infrastructure, reimbursement, liability concerns, and clinician trust. Effective integration requires attention to timing, display, and action triggers at each stage."

---

## Figure 7: Cardiovascular Case Study

### Files
- `figs/part_6/ch27/07-fig-cardio-case-study.svg`

### Priority
**Enhancing** - Concrete example

### Content Description
End-to-end case study of FM-enhanced cardiovascular risk prediction showing integration of PRS, expression, and clinical data.

### DALL-E Prompt
```
Scientific illustration of cardiovascular risk prediction case study. Single panel with patient journey.

PATIENT CASE: 45-year-old male, family history of early MI

DATA INPUTS (left side):
- Genetic: PRS for CAD (raw + FM-enhanced)
- Coding: LDLR variant (AlphaMissense score)
- Expression: Inflammatory signature from blood
- Clinical: Lipids, BP, smoking status, BMI

MODEL INTEGRATION (center):
- Multi-input fusion architecture
- Temporal model incorporating 5 years of data
- Foundation model features from each modality
- Integration producing unified risk

OUTPUT (right side):
- 10-year risk: 28% (CI: 22-35%)
- Compared to Framingham alone: 18%
- Compared to PRS alone: 24%
- FM-integrated adds: +10% AUC over baseline

CLINICAL ACTION:
- Risk category: High
- Recommendation: Statin therapy, lifestyle intervention
- Follow-up: Annual monitoring
- Uncertainty note: FM predictions validated in European populations; patient of South Asian ancestry warrants caution

TIMELINE at bottom showing prediction evolution over 5 years.

Professional clinical case study style, patient-centric visualization, white background.

Save as: 07-fig-cardio-case-study.svg
```

### Post-Processing Notes
- Add realistic risk values
- Include comparison metrics
- Show ancestry considerations

### Fallback Description
"Cardiovascular case study: patient with genetic PRS, coding variant, expression signature, and clinical data. Model integration produces 28% 10-year risk (higher than Framingham or PRS alone), leading to high-risk classification and statin recommendation. Note on ancestry-specific validation limitations."

### Caption Recommendation
"Case study: FM-enhanced cardiovascular risk prediction. A 45-year-old male with family history integrates genetic PRS (enhanced by regulatory variant effects), LDLR coding variant (scored by AlphaMissense), inflammatory expression signature, and clinical features. FM-integrated prediction (28% 10-year risk) exceeds both traditional Framingham (18%) and PRS-only (24%) approaches. Clinical action: statin therapy with annual monitoring. Caveat: model validated primarily in European populations; additional caution warranted for other ancestries."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Feature Integration | 3 | Essential | High |
| Temporal Modeling | 3 | High | Medium |
| Validation Hierarchy | 1 | Essential | Low |
| Clinical Uncertainty | 1 | High | Medium |
| Fairness Assessment | 4 | High | Medium |
| Clinical Workflow | 1 | High | Medium |
| Cardio Case Study | 1 | Enhancing | Medium |

## Recommended Generation Order
1. Validation Hierarchy (framework)
2. Feature Integration (architecture)
3. Fairness Assessment (equity)
4. Clinical Uncertainty (communication)
5. Temporal Modeling (dynamics)
6. Clinical Workflow (deployment)
7. Cardio Case Study (concrete example)
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
# Figure Report: Chapter 29 - Drug Discovery

**Chapter:** p6-ch29-drug-discovery.qmd
**Date:** 2026-01-07
**Total Figures:** 5 (5 files)
**Format:** SVG (for scalability)

---

## Figure 1: Target Prioritization Pipeline

### Files
- `figs/part_6/ch29/01-fig-target-prioritization.svg`

### Priority
**Essential** - Core drug discovery workflow

### Content Description
Pipeline from disease understanding through target identification to validation, with FM contribution at each stage.

### DALL-E Prompt
```
Scientific illustration of drug target prioritization pipeline. Single horizontal flow panel.

PIPELINE STAGES (left to right):

STAGE 1 (Disease Understanding):
- GWAS signals icon
- Expression signatures
- Clinical observations
- "What genes are associated with disease?"
FM contribution: Integrate multi-omic signals

STAGE 2 (Causal Inference):
- Mendelian randomization
- Fine-mapping
- Perturbation evidence
- "Which associations are causal?"
FM contribution: Prioritize variants, predict effects

STAGE 3 (Target Properties):
- Druggability assessment
- Safety profile
- Expression pattern
- "Can we drug this target safely?"
FM contribution: Predict binding pockets, off-target effects

STAGE 4 (Validation):
- CRISPR screens
- Animal models
- Biomarker development
- "Does modulation affect disease?"
FM contribution: Design experiments, interpret results

OUTPUT: Ranked target list with confidence scores

BOTTOM: Success rate annotation - "Only ~5% of targets that enter clinical trials succeed"

FILTER FUNNEL on side showing targets dropping out at each stage.

Professional drug discovery style, pipeline visualization, pharmaceutical iconography, white background.

Save as: 01-fig-target-prioritization.svg
```

### Post-Processing Notes
- Add specific gene examples
- Include success rate statistics
- Show decision criteria

### Fallback Description
"Drug target prioritization pipeline: from disease association (GWAS, expression) through causal inference (MR, fine-mapping) and target properties (druggability, safety) to validation (CRISPR, animal models). Foundation models contribute at each stage by integrating signals, prioritizing variants, predicting druggability, and interpreting validation results."

### Caption Recommendation
"Drug target prioritization pipeline. Starting from disease understanding (GWAS, expression signatures), targets progress through causal inference (Mendelian randomization confirms causation), target property assessment (druggability, safety), and experimental validation (CRISPR, animal models). Foundation models contribute at each stage: integrating multi-omic associations, prioritizing causal variants, predicting druggability, and interpreting validation data. Critical context: only ~5% of targets entering clinical development succeed."

---

## Figure 2: Network-Based Target Discovery

### Files
- `figs/part_6/ch29/02-fig-network-target-discovery.svg`

### Priority
**High** - Graph-based discovery

### Content Description
How biological networks combined with FM embeddings enable target discovery through guilt-by-association and network propagation.

### DALL-E Prompt
```
Scientific illustration of network-based drug target discovery. Single panel with network visualization.

MAIN NETWORK VISUALIZATION (center):
- Protein-protein interaction network
- Known disease genes highlighted (red nodes)
- Candidate targets highlighted (orange nodes, connected to disease genes)
- Drug targets highlighted (blue, connected to candidates)
- Edge thickness: interaction confidence
- Node size: degree/centrality

INSET 1 (top left): FM Node Features
- Each protein node has ESM embedding
- Functional similarity encoded
- Enables better propagation

INSET 2 (top right): Propagation Algorithm
- Start from known disease genes
- Propagate signal through network
- Rank by accumulated score
- Top-ranked = candidate targets

INSET 3 (bottom): Network Properties
- Disease module (cluster of disease genes)
- Network proximity to existing drugs
- Pathway enrichment

OUTPUT BOX (right):
Ranked candidate list:
1. Gene A - high network score, druggable
2. Gene B - moderate score, novel
3. Gene C - connected to approved drug (repurposing)

ANNOTATION: "Network context reveals targets missed by GWAS alone"

Professional systems biology style, network diagram, node-link visualization, white background.

Save as: 02-fig-network-target-discovery.svg
```

### Post-Processing Notes
- Add specific network statistics
- Include propagation formula
- Show disease module structure

### Fallback Description
"Network-based target discovery: protein-protein interaction network with known disease genes, candidate targets identified through network propagation, and drug targets connected to candidates. FM embeddings provide node features encoding functional similarity. Network context reveals targets missed by association studies alone."

### Caption Recommendation
"Network-based drug target discovery. Known disease genes (red) seed network propagation through protein-protein interactions. Candidate targets (orange) accumulate high scores based on network proximity. Foundation model embeddings (ESM) provide node features that encode functional similarity, improving propagation beyond topology alone. Network context reveals targets missed by GWAS: genes may not harbor risk variants themselves but are functionally connected to disease mechanisms."

---

## Figure 3: Drug-Target Interaction Prediction

### Files
- `figs/part_6/ch29/03-fig-drug-target-prediction.svg`

### Priority
**High** - Core computational approach

### Content Description
How FM representations enable drug-target binding prediction and drug repurposing.

### DALL-E Prompt
```
Scientific illustration of drug-target interaction prediction using foundation models. Single panel with architecture diagram.

ARCHITECTURE:

INPUT BRANCH 1 (Drug):
- Chemical structure (SMILES/graph)
- Through chemical encoder (ChemBERTa, MolBERT)
- Drug embedding vector

INPUT BRANCH 2 (Target):
- Protein sequence
- Through protein FM (ESM-2)
- Target embedding vector

INTERACTION PREDICTION:
- Concatenate/cross-attention embeddings
- MLP prediction head
- Output: binding probability, affinity prediction

TRAINING DATA:
- Known drug-target pairs (positive)
- Non-interacting pairs (negative)
- ChEMBL, DrugBank sources

APPLICATIONS (bottom):
Three use cases:
1) Virtual screening: Score all targets for new drug
2) Drug repurposing: Score all drugs for disease target
3) Off-target prediction: Identify unintended interactions

VALIDATION:
- Experimental binding assays (IC50, Kd)
- Cell-based screens
- Clinical observations

Professional computational drug discovery style, neural network architecture, white background.

Save as: 03-fig-drug-target-prediction.svg
```

### Post-Processing Notes
- Add specific model names
- Include performance metrics
- Show embedding space visualization

### Fallback Description
"Drug-target interaction prediction: drug structures encoded by chemical models, protein targets encoded by protein FMs, embeddings combined for binding prediction. Applications include virtual screening, drug repurposing, and off-target prediction. Validation requires experimental binding assays."

### Caption Recommendation
"Drug-target interaction prediction with foundation models. Drug structures are encoded by chemical language models (ChemBERTa) while protein targets are encoded by protein foundation models (ESM-2). Combined embeddings predict binding probability and affinity. Applications span virtual screening (score targets for new drugs), drug repurposing (score known drugs for new targets), and off-target prediction (identify safety liabilities). Experimental validation remains essential: computational predictions prioritize but cannot substitute for binding assays."

---

## Figure 4: Perturb-seq for Mechanism Discovery

### Files
- `figs/part_6/ch29/04-fig-perturb-seq.svg`

### Priority
**High** - Interventional data source

### Content Description
Perturb-seq experimental design and how FMs integrate with perturbation data for mechanism discovery.

### DALL-E Prompt
```
Scientific illustration of Perturb-seq for drug target mechanism discovery. Single panel with experimental workflow.

EXPERIMENTAL WORKFLOW (top to bottom):

STEP 1 (CRISPR Library):
- Pooled CRISPR library targeting 100s-1000s of genes
- Each guide has unique barcode
- Library transduced into cells

STEP 2 (Single-Cell Capture):
- Cells captured individually
- 10x Genomics or similar platform
- Each cell: expression profile + guide identity

STEP 3 (Readout Matrix):
- Cells × genes expression matrix
- Cells grouped by which gene was perturbed
- Perturbation → expression signature

DATA STRUCTURE (middle):
Matrix visualization:
- Rows: perturbations (gene knockouts)
- Columns: genes (expression changes)
- Color: effect magnitude
Annotation: "Direct observation of gene-gene regulatory relationships"

FM INTEGRATION (bottom):
Three applications:
1) Predict perturbation effects before experiment (virtual screening)
2) Interpret signatures using FM embeddings (mechanism)
3) Identify missing perturbations to test (active learning)

OUTPUT:
- Gene regulatory network
- Drug target mechanism
- Resistance mechanisms

Professional molecular biology style, experimental workflow, matrix visualization, white background.

Save as: 04-fig-perturb-seq.svg
```

### Post-Processing Notes
- Add specific throughput numbers
- Include cost considerations
- Show downstream analysis

### Fallback Description
"Perturb-seq workflow: CRISPR library targeting genes, single-cell capture with guide identification, expression readout per perturbation. Data matrix shows perturbation-expression relationships. FMs predict effects, interpret signatures, and prioritize experiments. Outputs include regulatory networks and drug mechanism understanding."

### Caption Recommendation
"Perturb-seq for mechanism discovery. Pooled CRISPR libraries target hundreds to thousands of genes; single-cell capture identifies both the perturbation (guide barcode) and its effect (expression profile). The resulting matrix directly measures gene-gene regulatory relationships—interventional data that foundation models cannot learn from observation alone. FM integration: predict perturbation effects for virtual screening, interpret expression signatures for mechanism discovery, and identify informative perturbations for active learning."

---

## Figure 5: Biomarker Discovery Pipeline

### Files
- `figs/part_6/ch29/05-fig-biomarker-pipeline.svg`

### Priority
**High** - Clinical development support

### Content Description
Pipeline from FM features to validated biomarkers for patient stratification and response prediction.

### DALL-E Prompt
```
Scientific illustration of biomarker discovery pipeline using foundation models. Single horizontal panel.

PIPELINE (left to right):

STAGE 1 (FM Feature Extraction):
- Patient molecular data (genomic, expression, protein)
- Through respective FMs
- High-dimensional embeddings extracted
Icon: Feature space with patient points

STAGE 2 (Association Discovery):
- Correlate FM features with clinical outcomes
- Response vs non-response
- Survival, progression
- Statistical testing with multiple testing correction

STAGE 3 (Candidate Biomarkers):
- Features that distinguish responders
- Interpretability analysis: which genes/variants?
- Biological pathway enrichment
- List of candidate markers

STAGE 4 (Technical Validation):
- Analytical validation (reproducibility, precision)
- Assay development (from FM feature to measurable test)
- Independent cohort replication

STAGE 5 (Clinical Validation):
- Prospective trials
- Regulatory submission (companion diagnostic)
- Clinical utility demonstration

OUTPUT:
- Stratification biomarker (who benefits?)
- Predictive biomarker (which treatment?)
- Prognostic biomarker (what outcome?)

TIMELINE: Discovery (months) → Technical validation (months-year) → Clinical validation (years)

BOTTLENECK annotation: "Clinical validation is rate-limiting step"

Professional clinical development style, pipeline visualization, white background.

Save as: 05-fig-biomarker-pipeline.svg
```

### Post-Processing Notes
- Add specific biomarker examples
- Include regulatory pathway
- Show companion diagnostic path

### Fallback Description
"Biomarker discovery pipeline: FM feature extraction from patient data, association discovery with clinical outcomes, candidate biomarker identification with interpretability, technical validation (assay development, replication), and clinical validation (prospective trials, regulatory approval). Clinical validation is rate-limiting—years versus months for discovery."

### Caption Recommendation
"Biomarker discovery pipeline with foundation models. FM embeddings from patient molecular data provide rich features for association discovery with clinical outcomes. Candidate biomarkers emerge from features distinguishing responders from non-responders. Technical validation develops reproducible assays; clinical validation demonstrates utility in prospective trials. Timeline reality: discovery in months, but clinical validation requires years. Foundation models accelerate discovery but cannot bypass the clinical validation bottleneck required for regulatory approval and clinical adoption."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Target Prioritization | 1 | Essential | Medium |
| Network Discovery | 1 | High | High |
| Drug-Target Prediction | 1 | High | High |
| Perturb-seq | 1 | High | Medium |
| Biomarker Pipeline | 1 | High | Medium |

## Recommended Generation Order
1. Target Prioritization (overview pipeline)
2. Drug-Target Prediction (computational core)
3. Network Discovery (graph methods)
4. Perturb-seq (interventional data)
5. Biomarker Pipeline (clinical development)
# Figure Report: Chapter 30 - Sequence Design

**Chapter:** p6-ch30-design.qmd
**Date:** 2026-01-07
**Total Figures:** 7 (9 files)
**Format:** SVG (for scalability)

---

## Figure 1: Design Problem Formalism

### Files
- `figs/part_6/ch30/01-A-fig-design-formalism.svg`
- `figs/part_6/ch30/01-B-fig-design-formalism.svg`

### Priority
**Essential** - Conceptual foundation

### Content Description
Two-panel figure: forward prediction vs inverse design problem, and the design space landscape.

### DALL-E Prompt
```
Scientific illustration of sequence design problem formulation. Two panels.

PANEL A (Forward vs Inverse):
Two directions illustrated:

FORWARD (top):
Sequence → Model → Predicted Function
"Given sequence, predict what it does"
Arrow pointing right
Example: DNA sequence → Enformer → Expression prediction
Foundation models excel here ✓

INVERSE (bottom):
Desired Function → ??? → Sequence
"Given desired function, find sequence"
Arrow pointing left
Example: "High liver expression" → ??? → Optimal promoter
Much harder - combinatorial search required

Annotation: "Inverse design is not simply 'running the model backward'"

PANEL B (Design Space Landscape):
3D fitness landscape visualization.
X,Y axes: sequence space dimensions (abstract)
Z axis: fitness/function score
Surface showing peaks (good designs) and valleys (poor)

Key features marked:
- Global optimum (highest peak) - "Ideal but hard to find"
- Local optima (smaller peaks) - "Easy to get trapped"
- Starting point - "Random/natural sequence"
- Path showing optimization trajectory

Annotation: "Sequence space is vast: 4^N for DNA, 20^N for protein"

Professional scientific style, mathematical visualization, white background.

Save as: 01-A-fig-design-formalism.svg, 01-B-fig-design-formalism.svg
```

### Post-Processing Notes
- Add specific sequence space sizes
- Include optimization algorithm annotations
- Show multiple starting points

### Fallback Description
"Design problem formalism: forward prediction (sequence → function) is what FMs do well; inverse design (function → sequence) is much harder requiring combinatorial search through vast sequence space. Fitness landscape shows global optimum, local optima traps, and optimization trajectories."

### Caption Recommendation
"Sequence design problem formulation. (A) Forward versus inverse problems: foundation models excel at forward prediction (sequence → function) but inverse design (function → sequence) requires search through vast combinatorial spaces. (B) Design space landscape: sequence fitness varies across 4^N (DNA) or 20^N (protein) possibilities. Optimization must navigate between local optima traps toward global optimum—a fundamentally harder problem than prediction."

---

## Figure 2: Protein Design Approaches

### Files
- `figs/part_6/ch30/02-A-fig-protein-design.svg`
- `figs/part_6/ch30/02-B-fig-protein-design.svg`

### Priority
**High** - Core design methods

### Content Description
Two approaches: directed evolution in silico and generative design from priors.

### DALL-E Prompt
```
Scientific illustration of protein design approaches. Two panels.

PANEL A (Directed Evolution In Silico):
Evolutionary cycle diagram:
1) Start: parent sequence
2) Mutate: generate variants (point mutations, recombination)
3) Score: FM predicts fitness for each variant
4) Select: keep top scorers
5) Repeat: iterate for N generations
→ Improved sequence

Comparison to lab evolution:
- Lab: weeks per cycle, expensive
- In silico: seconds per cycle, cheap
- Hybrid: FM-guided lab evolution

FM role: Fitness predictor enables fast screening

PANEL B (Generative Design):
Alternative approach:
1) Train generative model (VAE, diffusion, autoregressive) on functional proteins
2) Sample from latent space or condition on desired properties
3) Generated sequences have FM-learned priors
4) Filter by property predictors

Examples:
- ProGen: autoregressive protein generation
- ProteinMPNN: structure-conditioned design
- RFdiffusion: diffusion-based backbone design

FM role: Generative prior from evolutionary data

Professional scientific style, evolutionary diagram for A, generative model diagram for B, white background.

Save as: 02-A-fig-protein-design.svg, 02-B-fig-protein-design.svg
```

### Post-Processing Notes
- Add specific model names
- Include success rate metrics
- Show experimental validation

### Fallback Description
"Protein design approaches: directed evolution in silico (mutate → FM score → select → repeat) enables fast virtual screening; generative design samples from FM-learned priors conditioned on desired properties. Both leverage FM representations but through different mechanisms."

### Caption Recommendation
"Protein design approaches. (A) Directed evolution in silico: generate variants through mutation, score with foundation models, select top performers, iterate. Achieves in seconds what lab evolution requires weeks for. (B) Generative design: sample from generative models (ProGen, ProteinMPNN, RFdiffusion) trained on evolutionary data, conditioning on desired properties. Foundation models contribute as fitness predictors (A) or as generative priors (B)—both leverage representations learned from millions of natural sequences."

---

## Figure 3: Regulatory Element Design

### Files
- `figs/part_6/ch30/03-fig-regulatory-design.svg`

### Priority
**High** - DNA design application

### Content Description
Designing synthetic promoters, enhancers, and other regulatory elements using DNA FMs.

### DALL-E Prompt
```
Scientific illustration of regulatory element design with DNA foundation models. Single panel with multiple elements.

DESIGN TARGETS (top row, four boxes):
1) Synthetic promoter: Control expression level
2) Tissue-specific enhancer: Restrict to target tissue
3) Synthetic 5' UTR: Optimize translation
4) CRISPR guide: Maximize on-target, minimize off-target

For each: icon and key design objective

DESIGN WORKFLOW (center):
Flow diagram:
Objective specification → Sequence generation → FM scoring → Selection → Experimental validation

Methods:
- Gradient-based optimization (backprop through FM)
- Evolutionary search (mutate + score)
- Generative models (conditional sampling)
- Hybrid approaches

FM CONTRIBUTION (right):
- Predict activity of candidate sequences
- Provide gradient signal for optimization
- Score off-target effects
- Predict tissue specificity

VALIDATION (bottom):
MPRA (massively parallel reporter assay) for high-throughput testing
Thousands of designs tested in parallel
Feedback to improve models

EXAMPLE SUCCESS:
"Designed promoter achieving 10x natural expression" with citation placeholder

Professional scientific style, regulatory genomics visualization, white background.

Save as: 03-fig-regulatory-design.svg
```

### Post-Processing Notes
- Add specific design examples
- Include MPRA workflow
- Show tissue specificity examples

### Fallback Description
"Regulatory element design: targets include synthetic promoters, tissue-specific enhancers, 5' UTRs, and CRISPR guides. Design workflow from objective specification through generation, FM scoring, selection, and MPRA validation. FMs predict activity, provide optimization gradients, and score off-target effects."

### Caption Recommendation
"Regulatory element design with DNA foundation models. Design targets span synthetic promoters (expression level), tissue-specific enhancers (spatial control), 5' UTRs (translation efficiency), and CRISPR guides (specificity). Workflow combines sequence generation methods (gradient optimization, evolutionary search, generative sampling) with FM-based scoring. Validation through MPRA enables testing thousands of designs in parallel, creating feedback loops that improve both designs and models."

---

## Figure 4: mRNA Therapeutic Optimization

### Files
- `figs/part_6/ch30/04-fig-mrna-optimization.svg`

### Priority
**High** - Therapeutics application

### Content Description
Design considerations for mRNA therapeutics: codon optimization, UTR design, modification selection.

### DALL-E Prompt
```
Scientific illustration of mRNA therapeutic design optimization. Single panel with mRNA structure and design elements.

mRNA STRUCTURE (center, horizontal):
5' cap → 5' UTR → Coding sequence → 3' UTR → Poly(A) tail
Each region highlighted with design considerations below

DESIGN ELEMENTS:

5' UTR Design (left):
- Kozak sequence optimization
- Secondary structure minimization
- uORF avoidance
- Translation initiation efficiency
FM contribution: Predict translation efficiency

Coding Sequence (center):
- Codon optimization for host tRNA pools
- GC content balancing
- Avoid immunogenic motifs
- Maintain mRNA structure
FM contribution: Codon-aware models predict expression

3' UTR Design (right):
- Stability elements
- miRNA binding site avoidance
- Half-life optimization
FM contribution: Predict degradation, localization

MODIFICATION Selection (bottom):
- N1-methylpseudouridine (m1Ψ) for immune evasion
- 5-methylcytosine for stability
- Trade-offs with translation efficiency

COVID VACCINE box: "BNT162b2 design choices" with key optimizations listed

MULTI-OBJECTIVE OPTIMIZATION note: Balance expression, stability, immunogenicity, manufacturability

Professional therapeutic development style, mRNA structure visualization, white background.

Save as: 04-fig-mrna-optimization.svg
```

### Post-Processing Notes
- Add specific codon optimization details
- Include COVID vaccine examples
- Show multi-objective tradeoffs

### Fallback Description
"mRNA therapeutic optimization: 5' UTR design (Kozak, structure), coding sequence (codon optimization, GC content), 3' UTR (stability, miRNA avoidance), and modification selection (m1Ψ for immune evasion). Multi-objective optimization balances expression, stability, and immunogenicity. COVID vaccines demonstrate successful application."

### Caption Recommendation
"mRNA therapeutic design optimization. Each region requires distinct considerations: 5' UTR affects translation initiation (Kozak sequence, structure minimization); coding sequence requires codon optimization balanced against GC content and immunogenicity; 3' UTR controls stability and localization; chemical modifications (N1-methylpseudouridine) reduce immunogenicity. Foundation models predict translation efficiency, stability, and immunogenic potential. COVID-19 mRNA vaccines demonstrate successful integration of these design principles."

---

## Figure 5: Antibody Design

### Files
- `figs/part_6/ch30/05-fig-antibody-design.svg`

### Priority
**High** - Therapeutic protein design

### Content Description
FM-guided antibody engineering: CDR optimization, humanization, and developability.

### DALL-E Prompt
```
Scientific illustration of antibody design with foundation models. Single panel with antibody structure and design workflow.

ANTIBODY STRUCTURE (left):
Y-shaped antibody diagram:
- Heavy chain (dark blue)
- Light chain (light blue)
- CDR loops highlighted (red): CDR1, CDR2, CDR3
- Framework regions labeled
- Fc region for effector functions

DESIGN CHALLENGES (center column):
1) Affinity maturation: Improve binding strength
2) Specificity: Reduce off-target binding
3) Humanization: Reduce immunogenicity
4) Developability: Aggregation, stability, expression

FM CONTRIBUTIONS (right column):
For each challenge:
1) Predict binding ΔG from sequence (ESM embeddings + docking)
2) Predict cross-reactivity from sequence similarity
3) Score humanness using human antibody corpus
4) Predict biophysical properties (aggregation, viscosity)

WORKFLOW (bottom):
Starting antibody → CDR mutagenesis library → FM scoring → Select candidates → Experimental validation → Iterate

Success metrics:
- Affinity: pM to nM range
- Humanness score: >90%
- Aggregation: <5%

CASE STUDY box: Example therapeutic antibody optimization

Professional biopharmaceutical style, antibody structure, white background.

Save as: 05-fig-antibody-design.svg
```

### Post-Processing Notes
- Add specific CDR sequences
- Include humanization scoring
- Show developability predictions

### Fallback Description
"Antibody design with FMs: structure showing CDR loops (binding) and framework (scaffold), design challenges (affinity, specificity, humanization, developability), and FM contributions (binding prediction, humanness scoring, aggregation prediction). Workflow iterates between FM-guided mutagenesis and experimental validation."

### Caption Recommendation
"Antibody design with foundation models. The antibody structure comprises framework regions (scaffold) and CDR loops (binding interface). Design challenges include affinity maturation (improve binding), specificity (reduce off-targets), humanization (reduce immunogenicity), and developability (ensure manufacturability). Foundation models contribute binding affinity prediction from sequence, humanness scoring against human antibody corpus, and biophysical property prediction (aggregation, stability). Iterative design cycles alternate between FM-guided mutagenesis and experimental validation."

---

## Figure 6: Design-Build-Test-Learn Cycle

### Files
- `figs/part_6/ch30/06-fig-dbtl-cycle.svg`

### Priority
**Essential** - Core iterative paradigm

### Content Description
The DBTL cycle for sequence design showing how FMs integrate with experimental automation.

### DALL-E Prompt
```
Scientific illustration of Design-Build-Test-Learn cycle for sequence design. Single panel with circular workflow.

CIRCULAR FLOW (clockwise):

DESIGN (12 o'clock position):
- FM predicts function from sequence
- Optimization identifies candidates
- Prioritize for synthesis
Icon: Computer/algorithm
FM role: Score and optimize

BUILD (3 o'clock position):
- DNA synthesis
- Assembly and cloning
- Cell transformation
Icon: DNA synthesis machine
Automation: Oligo synthesis, assembly robots

TEST (6 o'clock position):
- Functional assays
- High-throughput screening
- Readouts (expression, binding, activity)
Icon: Microplate, sequencer
Automation: Liquid handlers, plate readers

LEARN (9 o'clock position):
- Results back to model
- Update FM or downstream models
- Identify patterns, improve predictions
Icon: Data analysis, model update
FM role: Retrain, fine-tune, active learning

CENTER: "Iterative improvement"
Annotation: Each cycle improves both sequences AND models

SCALE annotations around cycle:
- Designs per cycle: 100s-1000s
- Synthesis time: days
- Assay time: days-weeks
- Learning: continuous

BOTTLENECK highlighted: Build and Test phases limit iteration speed

Professional synthetic biology style, circular workflow, white background.

Save as: 06-fig-dbtl-cycle.svg
```

### Post-Processing Notes
- Add specific throughput numbers
- Include cost estimates
- Show closed-loop automation

### Fallback Description
"DBTL cycle: Design (FM optimization) → Build (synthesis, assembly) → Test (functional assays) → Learn (update models) → repeat. Each cycle improves both designed sequences and FM predictions. Build and Test phases are bottlenecks limiting iteration speed."

### Caption Recommendation
"Design-Build-Test-Learn cycle for sequence engineering. **Design**: foundation models score candidates and optimization identifies promising sequences. **Build**: DNA synthesis and assembly create physical constructs. **Test**: functional assays measure actual performance. **Learn**: results update models for next cycle. Each iteration improves both designed sequences and predictive accuracy. Bottleneck reality: Build and Test phases (days to weeks) limit iteration speed despite fast computational Design (~seconds). Closed-loop automation increasingly accelerates the cycle."

---

## Figure 7: Generative Model Evaluation

### Files
- `figs/part_6/ch30/07-fig-generative-evaluation.svg`

### Priority
**High** - Evaluation framework

### Content Description
How to evaluate generative sequence models: diversity, novelty, validity, and function.

### DALL-E Prompt
```
Scientific illustration of generative model evaluation metrics. Single panel with evaluation framework.

EVALUATION DIMENSIONS (four quadrants):

TOP LEFT (Diversity):
- Are generated sequences varied?
- Metrics: sequence identity distribution, embedding space coverage
- Visualization: scatter plot of embeddings with natural (blue) and generated (orange) overlapping
- Good: covers natural space
- Bad: mode collapse (single cluster)

TOP RIGHT (Novelty):
- Are sequences genuinely new?
- Metrics: distance to nearest training example
- Visualization: histogram of distances
- Good: novel but plausible
- Bad: memorization (distance = 0) or random (very high distance)

BOTTOM LEFT (Validity):
- Are sequences structurally valid?
- Metrics: folds correctly, no stop codons, proper chemistry
- Visualization: % valid across samples
- Good: high validity rate
- Bad: many invalid sequences

BOTTOM RIGHT (Function):
- Do sequences actually work?
- Metrics: experimental activity, binding, expression
- Visualization: predicted vs measured function scatter
- Good: high correlation
- Bad: predictions don't match reality (ultimate test)

CENTER: Trade-offs note
"Optimizing one metric can harm others"
Example: High novelty may reduce validity

VALIDATION HIERARCHY (bottom):
Computational → In silico validation → Experimental validation
"Only wet lab validation confirms function"

Professional scientific style, metrics visualization, white background.

Save as: 07-fig-generative-evaluation.svg
```

### Post-Processing Notes
- Add specific metric formulas
- Include benchmark datasets
- Show correlation with experiments

### Fallback Description
"Generative model evaluation: diversity (varied outputs, not mode collapse), novelty (new sequences, not memorization), validity (proper structure/chemistry), and function (experimental activity). Trade-offs exist between metrics. Only experimental validation confirms function."

### Caption Recommendation
"Evaluating generative sequence models. Four dimensions: **Diversity** measures variation among outputs (avoiding mode collapse); **Novelty** assesses distance from training examples (avoiding memorization); **Validity** checks structural correctness (foldable, proper chemistry); **Function** measures experimental performance (ultimate test). These metrics can trade off—highly novel sequences may have lower validity. Critical insight: computational metrics provide useful screening, but only experimental validation confirms that generated sequences actually function as intended."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Design Formalism | 2 | Essential | Medium |
| Protein Design | 2 | High | High |
| Regulatory Design | 1 | High | Medium |
| mRNA Optimization | 1 | High | Medium |
| Antibody Design | 1 | High | High |
| DBTL Cycle | 1 | Essential | Low |
| Generative Evaluation | 1 | High | Medium |

## Recommended Generation Order
1. Design Formalism (conceptual foundation)
2. DBTL Cycle (iterative paradigm)
3. Protein Design (core methods)
4. Regulatory Design (DNA application)
5. mRNA Optimization (therapeutics)
6. Antibody Design (therapeutic proteins)
7. Generative Evaluation (assessment framework)
# Figure Report: Chapter 31 - Frontiers

**Chapter:** p6-ch31-frontiers.qmd
**Date:** 2026-01-07
**Total Figures:** 3 (3 files)
**Format:** SVG (for scalability)

---

## Figure 1: Multiscale Integration Vision

### Files
- `figs/part_6/ch31/01-fig-multiscale-integration.svg`

### Priority
**High** - Future direction

### Content Description
Vision for models that integrate across biological scales: from nucleotides to organisms.

### DALL-E Prompt
```
Scientific illustration of multiscale biological integration for future foundation models. Single panel with hierarchical visualization.

SCALE HIERARCHY (bottom to top):

LEVEL 1 (BOTTOM - Nucleotide):
- DNA sequence (ATCG letters)
- Current DNA FMs operate here
- Scale: 1-10^6 bp

LEVEL 2 (Gene):
- Gene structure with exons/introns
- Regulatory elements
- Current models partially address
- Scale: 10^3-10^5 bp

LEVEL 3 (Protein):
- 3D structure, function
- Current protein FMs strong here
- Scale: 10^2-10^3 amino acids

LEVEL 4 (Cell):
- Single-cell expression state
- Organelle localization
- Current scRNA FMs emerging
- Scale: 10^4 genes

LEVEL 5 (Tissue):
- Spatial organization
- Cell-cell communication
- Emerging spatial FMs
- Scale: 10^3-10^6 cells

LEVEL 6 (Organism):
- Phenotype, physiology
- Clinical manifestation
- Current gap - limited integration
- Scale: whole organism

LEVEL 7 (TOP - Population):
- Evolution, population genetics
- Epidemiology
- Current gap - separate models
- Scale: 10^6+ individuals

CONNECTING ARROWS showing information flow up and down scales

CHALLENGE BOX: "Current models operate at single scales. Future models must bridge across scales."

INTEGRATION APPROACHES (side):
- Hierarchical architectures
- Cross-scale attention
- Multi-resolution representations
- Causal structure encoding

Professional scientific style, biological hierarchy visualization, gradient from molecule to population, white background.

Save as: 01-fig-multiscale-integration.svg
```

### Post-Processing Notes
- Add specific scale numbers
- Include current model examples at each level
- Show integration challenges

### Fallback Description
"Multiscale integration vision: from nucleotides through genes, proteins, cells, tissues, organisms, to populations. Current FMs operate at single scales (DNA, protein, single-cell). Future models must bridge scales through hierarchical architectures, cross-scale attention, and causal structure encoding."

### Caption Recommendation
"Multiscale integration for future foundation models. Biology spans scales from nucleotides (10^0 bp) to populations (10^6+ individuals). Current foundation models excel at single scales: DNA language models at sequence level, protein models at structure level, single-cell models at cellular level. The frontier challenge: integrating across scales so that molecular perturbations can be traced to organismal phenotypes. Approaches include hierarchical architectures, cross-scale attention mechanisms, and explicit causal structure encoding."

---

## Figure 2: Agentic Scientific Systems

### Files
- `figs/part_6/ch31/02-fig-agentic-systems.svg`

### Priority
**High** - Emerging paradigm

### Content Description
Vision for autonomous scientific agents that combine FMs with experimental automation for discovery.

### DALL-E Prompt
```
Scientific illustration of agentic scientific systems combining AI and automation. Single panel with system architecture.

CENTRAL AGENT (middle):
- LLM/FM-based reasoning engine
- Scientific knowledge base
- Hypothesis generation capability
- Experimental planning
Icon: Brain/AI symbol

CAPABILITIES (radiating from center):

PERCEPTION (top):
- Literature reading and synthesis
- Data interpretation
- Pattern recognition across experiments
- Integration with databases (UniProt, PDB, etc.)

REASONING (right):
- Hypothesis generation
- Experimental design
- Troubleshooting failures
- Causal inference

ACTION (bottom):
- Control lab automation
- Execute protocols
- Order reagents
- Run analyses

LEARNING (left):
- Update from experimental results
- Refine predictions
- Build scientific models
- Accumulate knowledge

AUTOMATION LAYER (bottom):
Connected to:
- Liquid handlers
- Sequencers
- Microscopes
- Synthesis platforms

HUMAN OVERSIGHT (top):
- Strategic direction
- Ethical boundaries
- Safety oversight
- Final decisions

CLOSED LOOP:
Agent proposes → Automation executes → Results return → Agent learns → Agent proposes improved hypothesis

EXAMPLE APPLICATION:
"Autonomous protein engineering: Agent proposes mutations, synthesis builds variants, assays test function, agent learns and iterates"

Professional futuristic scientific style, system architecture diagram, white background.

Save as: 02-fig-agentic-systems.svg
```

### Post-Processing Notes
- Add specific tool examples
- Include safety considerations
- Show human-AI collaboration

### Fallback Description
"Agentic scientific systems: central AI agent with perception (literature, data), reasoning (hypotheses, experiment design), action (lab automation control), and learning (update from results). Closed loop enables autonomous discovery with human oversight for strategic direction and safety."

### Caption Recommendation
"Agentic scientific systems for autonomous discovery. An AI agent combines foundation model capabilities (reasoning, hypothesis generation) with lab automation (liquid handlers, sequencers, synthesis). The closed loop: agent proposes experiments, automation executes, results return, agent learns and proposes improved hypotheses. Human oversight provides strategic direction, ethical boundaries, and safety constraints. Example application: autonomous protein engineering cycles through design-build-test-learn faster than human-only teams while maintaining scientific rigor."

---

## Figure 3: Learning Health System Vision

### Files
- `figs/part_6/ch31/03-fig-learning-health-system.svg`

### Priority
**High** - Clinical translation vision

### Content Description
Vision for genomic FMs integrated into learning health systems that continuously improve from clinical data.

### DALL-E Prompt
```
Scientific illustration of learning health system integrating genomic foundation models. Single panel with system architecture.

SYSTEM COMPONENTS:

CLINICAL CARE (left side):
- Patient encounter
- Genomic testing ordered
- FM-based interpretation
- Clinical decision support
- Treatment and monitoring
Icon: Hospital, clinician, patient

DATA FLOW (center, circular):
Clinical data flows to:
→ Deidentified aggregate data
→ Model training/updating
→ Improved predictions
→ Back to clinical care

FM INTEGRATION POINTS (highlighted):
1) Variant interpretation at diagnosis
2) Risk prediction for prevention
3) Treatment selection for therapy
4) Outcome prediction for prognosis

LEARNING LAYER (right side):
- Outcome tracking (did prediction match reality?)
- Model updating (retrain on new data)
- Performance monitoring (calibration, fairness)
- Knowledge generation (new variants classified)

GOVERNANCE (top):
- Privacy protection (differential privacy, federated)
- Consent frameworks (patient control)
- Equity monitoring (disparate impact assessment)
- Regulatory compliance (FDA, IRB)

MULTI-INSTITUTIONAL (bottom):
Network of health systems sharing learning:
- Institution A contributes data
- Institution B contributes data
- Federated learning aggregates
- All benefit from larger corpus

KEY INSIGHT: "Every patient encounter improves predictions for future patients"

CHALLENGES noted:
- Data quality and completeness
- Distribution shift over time
- Maintaining calibration
- Ensuring equity

Professional healthcare informatics style, system diagram, institutional network, white background.

Save as: 03-fig-learning-health-system.svg
```

### Post-Processing Notes
- Add specific outcome examples
- Include governance details
- Show federated learning architecture

### Fallback Description
"Learning health system vision: clinical care generates data, FM-based interpretation supports decisions, outcomes tracked, models updated, improved predictions return to care. Multi-institutional federated learning amplifies data while preserving privacy. Governance ensures equity, consent, and regulatory compliance."

### Caption Recommendation
"Learning health system integrating genomic foundation models. Clinical care generates data: genomic testing, FM-based interpretation, treatment decisions, outcomes. The learning loop: outcomes tracked against predictions, models updated on aggregated data, improved predictions deployed back to care. Multi-institutional networks amplify learning through federated approaches that preserve privacy. Governance layer ensures equity monitoring, consent compliance, and regulatory adherence. Vision: every patient encounter contributes to better predictions for future patients, creating a continuously improving healthcare system."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Multiscale Integration | 1 | High | High |
| Agentic Systems | 1 | High | High |
| Learning Health System | 1 | High | High |

## Recommended Generation Order
1. Multiscale Integration (scientific vision)
2. Agentic Systems (automation future)
3. Learning Health System (clinical translation)

## Notes

This chapter focuses on future directions, so figures are more visionary and conceptual than the technical figures in earlier chapters. They should inspire readers about where the field is heading while grounding the vision in current capabilities and realistic challenges.

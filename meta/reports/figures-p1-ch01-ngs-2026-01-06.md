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

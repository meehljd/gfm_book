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

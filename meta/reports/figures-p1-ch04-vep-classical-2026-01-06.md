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

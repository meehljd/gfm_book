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

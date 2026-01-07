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

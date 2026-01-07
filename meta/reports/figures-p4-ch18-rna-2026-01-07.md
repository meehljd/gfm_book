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

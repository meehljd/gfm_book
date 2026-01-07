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

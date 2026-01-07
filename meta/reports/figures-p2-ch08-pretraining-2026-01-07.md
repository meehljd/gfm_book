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

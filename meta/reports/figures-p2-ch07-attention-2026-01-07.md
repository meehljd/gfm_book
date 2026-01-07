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

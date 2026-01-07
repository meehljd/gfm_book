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

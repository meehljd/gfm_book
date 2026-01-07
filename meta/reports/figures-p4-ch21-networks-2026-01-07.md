# Figure Report: Chapter 21 - Graph and Network Models

**Chapter:** p4-ch21-networks.qmd
**Date:** 2026-01-07
**Total Figures:** 6 (21 files)
**Format:** SVG (for scalability)

---

## Figure 1: Biological Network Landscape

### Files
- `figs/part_4/ch18/01-A-fig-biological-networks.svg`
- `figs/part_4/ch18/01-B-fig-biological-networks.svg`
- `figs/part_4/ch18/01-C-fig-biological-networks.svg`
- `figs/part_4/ch18/01-D-fig-biological-networks.svg`

### Priority
**Essential** - Foundation for understanding network types

### Content Description
Overview of biological network types: PPI networks, gene regulatory networks, knowledge graphs, and spatial/cell-cell interaction graphs.

### DALL-E Prompt
```
Scientific illustration of different biological network types for computational biology textbook. Four panels showing distinct network structures.

PANEL A (PPI Networks): Undirected graph with protein nodes (circles with protein names like TP53, BRCA1). Edges representing physical binding. Varying node sizes by degree. Labels for databases: STRING, BioGRID, IntAct. Annotation "20-30% of interactions catalogued."

PANEL B (Gene Regulatory Networks): Directed graph with TF nodes (hexagons) and target gene nodes (circles). Arrows showing activation (green) and repression (red). Some TFs regulating multiple targets. Annotation "Cell-type specific from ChIP-seq, ATAC-seq."

PANEL C (Knowledge Graphs): Heterogeneous graph with multiple node types distinguished by shape/color: genes (circles), diseases (diamonds), drugs (squares), pathways (rectangles). Multiple edge types shown with different line styles. Hetionet example with node/edge counts. Annotation "Multi-hop reasoning."

PANEL D (Spatial Graphs): Tissue section background with cells as nodes. Edges connecting spatially adjacent cells. Different cell types in different colors. Annotation "Emerging from spatial transcriptomics." Ligand-receptor communication edges indicated.

Professional scientific illustration, network diagram style, white background, distinct visual identity for each network type.

Save as: 01-A-fig-biological-networks.svg through 01-D-fig-biological-networks.svg
```

### Post-Processing Notes
- Include specific database statistics
- Add edge type legends
- Use consistent node styling per network type

### Fallback Description
"Biological network landscape showing protein-protein interaction networks (undirected physical binding), gene regulatory networks (directed TF-target relationships), knowledge graphs (heterogeneous multi-type nodes and edges), and spatial graphs (cell proximity from spatial transcriptomics)."

### Caption Recommendation
"Landscape of biological networks. (A) Protein-protein interaction networks: undirected edges represent physical binding, with only 20-30% of interactions currently catalogued. (B) Gene regulatory networks: directed edges from transcription factors to targets, derived from ChIP-seq and accessibility data. (C) Knowledge graphs: heterogeneous graphs with multiple node types (genes, diseases, drugs, pathways) and relationship types enabling multi-hop reasoning. (D) Spatial and cell-cell interaction graphs: emerging from spatial transcriptomics, encoding tissue architecture and cell communication."

---

## Figure 2: Message Passing Framework

### Files
- `figs/part_4/ch18/02-A-fig-message-passing.svg`
- `figs/part_4/ch18/02-B-fig-message-passing.svg`
- `figs/part_4/ch18/02-C-fig-message-passing.svg`
- `figs/part_4/ch18/02-D-fig-message-passing.svg`

### Priority
**High** - Core GNN concept

### Content Description
Step-by-step illustration of the message passing algorithm showing initial state, message computation, aggregation, and multi-layer propagation.

### DALL-E Prompt
```
Scientific illustration of graph neural network message passing for computational biology. Four sequential panels.

PANEL A (Initial State): Simple 5-node graph with edges. Each node has initial feature vector (shown as small colored bar). Annotation "Initial features from foundation model embeddings." Node labels: gene names.

PANEL B (Message Computation): Same graph with arrows on edges showing message flow. For each edge, message m_ij computed from source and target features. Mathematical notation: m_ij = φ(h_i, h_j, e_ij). Arrows visualizing message direction.

PANEL C (Aggregation): Focus on single node receiving messages from all neighbors. Incoming arrows merging at node. Aggregation operations listed: sum, mean, max, attention. New representation formed. Mathematical notation: h_i' = ψ(h_i, ⊕ m_ij).

PANEL D (After L Layers): Same graph but nodes now showing expanded "receptive field" circles. After L=2 layers, each node's embedding incorporates 2-hop neighborhood. Annotation "Gene embedding now reflects pathway context." Before/after comparison of what node knows.

Clean technical illustration, white background, consistent node and edge styling, mathematical notation included.

Save as: 02-A-fig-message-passing.svg through 02-D-fig-message-passing.svg
```

### Post-Processing Notes
- Add mathematical formulas clearly
- Show feature vector dimensions
- Include layer number annotations

### Fallback Description
"Message passing in GNNs: initial node features from foundation models, message computation along edges, aggregation at each node combining neighbor information, and after L layers each node embedding incorporates L-hop neighborhood context."

### Caption Recommendation
"Message passing in graph neural networks. (A) Initial state: each node has feature vectors from foundation model embeddings. (B) Message computation: for each edge, compute message m_ij = φ(h_i, h_j, e_ij). (C) Aggregation: each node aggregates incoming messages using permutation-invariant operations (sum, mean, max, or attention). (D) After L layers: each node's embedding incorporates information from its L-hop neighborhood, capturing pathway-level context."

---

## Figure 3: Foundation Model + GNN Integration

### Files
- `figs/part_4/ch18/03-A-fig-gnn-integration.svg`
- `figs/part_4/ch18/03-B-fig-gnn-integration.svg`
- `figs/part_4/ch18/03-C-fig-gnn-integration.svg`
- `figs/part_4/ch18/03-D-fig-gnn-integration.svg`

### Priority
**Essential** - Core architectural concept

### Content Description
The central integration paradigm: foundation models produce representations, networks encode relationships, GNNs integrate both, enabling capabilities neither achieves alone.

### DALL-E Prompt
```
Scientific illustration of foundation model and GNN integration for computational biology. Four panels showing the integration paradigm.

PANEL A (Foundation Models Produce Representations): Three parallel flows. ESM-2 + protein sequence → protein embedding. DNABERT + DNA sequence → DNA embedding. scGPT + expression profile → cell embedding. Annotation "Rich representations of individual entities."

PANEL B (Biological Networks Encode Relationships): Network diagram showing PPI edges, regulatory edges, cell-cell communication. Annotation "Relational structure not captured by sequence alone." Emphasis on what networks add.

PANEL C (GNNs Integrate Both): Architecture diagram. Node features from FMs feed into GNN layers. Edges from biological networks. Message passing refines representations. Output: context-aware embeddings. Annotation "Message passing adds relational context."

PANEL D (Capabilities Neither Achieves Alone): Two-column comparison. Left (FM alone): "Rich features but no interactions" with X. Right (Network alone): "Relationships but limited features" with X. Center (Combined): "Disease gene prioritization, drug-target prediction, perturbation modeling" with checkmarks.

Professional scientific illustration, clean architecture diagrams, white background, emphasize the complementary nature.

Save as: 03-A-fig-gnn-integration.svg through 03-D-fig-gnn-integration.svg
```

### Post-Processing Notes
- Use specific foundation model names
- Show embedding dimensionalities
- Include specific application examples

### Fallback Description
"Foundation model and GNN integration: FMs produce rich entity representations from sequence, networks encode relational structure, GNNs combine both through message passing, enabling applications like disease gene prioritization that neither approach achieves alone."

### Caption Recommendation
"The foundation model + GNN integration paradigm. (A) Foundation models produce rich representations of individual entities: protein embeddings from ESM, DNA embeddings from DNABERT, cell embeddings from scGPT. (B) Biological networks encode relational structure that sequence models cannot capture. (C) GNNs integrate foundation model embeddings with network structure through message passing. (D) This combination enables capabilities neither achieves alone: disease gene prioritization, drug-target prediction, and perturbation response modeling."

---

## Figure 4: Disease Gene Prioritization

### Files
- `figs/part_4/ch18/04-A-fig-disease-gene-prioritization.svg`
- `figs/part_4/ch18/04-B-fig-disease-gene-prioritization.svg`
- `figs/part_4/ch18/04-C-fig-disease-gene-prioritization.svg`
- `figs/part_4/ch18/04-D-fig-disease-gene-prioritization.svg`

### Priority
**High** - Key application

### Content Description
GWAS follow-up application showing the challenge, network context, GNN scoring, and integration with sequence features.

### DALL-E Prompt
```
Scientific illustration of disease gene prioritization using GNNs for clinical genomics. Four panels.

PANEL A (The GWAS Challenge): Genomic locus diagram with lead SNP marker. Four genes (A, B, C, D) in the region. LD block shown covering all genes. Question mark: "Which gene is causal?" Annotation "Lead SNP in LD with all genes."

PANEL B (Network Context): Same four genes now shown in PPI network. Gene B connected to 5 known disease genes (highlighted in red). Genes A, C, D peripheral with few disease gene connections. Network topology suggests B as candidate.

PANEL C (GNN Scoring): GNN architecture receiving FM embeddings as node features. Disease gene labels propagating through network. Gene B receives high network-based score. Score bars showing B > C > A > D.

PANEL D (Integration with Sequence Features): Dual scoring. Gene C has strong protein features (from ESM). Gene B has strong network features + moderate protein features. Combined score identifies both B and C as top candidates. Annotation "Integrates intrinsic and relational evidence."

Clinical genomics illustration style, white background, network diagrams with gene nodes, score visualizations.

Save as: 04-A-fig-disease-gene-prioritization.svg through 04-D-fig-disease-gene-prioritization.svg
```

### Post-Processing Notes
- Use realistic gene names
- Show actual GWAS locus structure
- Include score comparisons

### Fallback Description
"Disease gene prioritization from GWAS: the challenge of multiple genes in LD, network context showing one gene connected to known disease genes, GNN scoring using FM embeddings and network propagation, and integration showing how sequence and network features complement each other."

### Caption Recommendation
"Disease gene prioritization for GWAS follow-up. (A) The GWAS challenge: a lead SNP is in LD with multiple genes—which is causal? (B) Network context: Gene B connects to five known disease genes while A, C, D are peripheral. (C) GNN scoring: foundation model embeddings as node features combined with network propagation prioritize gene B. (D) Sequence-network integration: Gene C has strong protein features while Gene B has network context—combined scoring identifies both as candidates for follow-up."

---

## Figure 5: Knowledge Graph Drug Repurposing

### Files
- `figs/part_4/ch18/05-A-fig-kg-drug-repurposing.svg`
- `figs/part_4/ch18/05-B-fig-kg-drug-repurposing.svg`
- `figs/part_4/ch18/05-C-fig-kg-drug-repurposing.svg`
- `figs/part_4/ch18/05-D-fig-kg-drug-repurposing.svg`

### Priority
**High** - Important translational application

### Content Description
Knowledge graph reasoning for drug repurposing: KG structure, multi-hop reasoning paths, link prediction, and FM enhancement.

### DALL-E Prompt
```
Scientific illustration of knowledge graph reasoning for drug repurposing. Four panels.

PANEL A (KG Structure): Heterogeneous knowledge graph with multiple node types. Drugs (blue squares), proteins (green circles), diseases (red diamonds), pathways (yellow rectangles). Multiple edge types with different line styles: binds, regulates, associated_with, participates_in. Partial view of Hetionet-style graph.

PANEL B (Multi-Hop Reasoning Path): Highlighted path through the KG. Drug D → (binds) → Protein P1 → (participates_in) → Pathway W → (disrupted_in) → Disease X. Each hop labeled with relationship type. Annotation "Multi-hop path provides mechanistic hypothesis."

PANEL C (Link Prediction): Full KG with trained node embeddings (glow effect). Query: predict missing drug-treats-disease edges. Dashed lines showing potential new connections. Scoring function comparing embeddings. Top candidates ranked by score.

PANEL D (FM Enhancement): Same KG but node features replaced with FM embeddings. Protein nodes: ESM embeddings capturing function. Gene nodes: DNA embeddings capturing regulation. Annotation "FM embeddings capture functional similarity beyond annotations."

Professional scientific illustration, knowledge graph visualization style, heterogeneous node shapes and colors, white background.

Save as: 05-A-fig-kg-drug-repurposing.svg through 05-D-fig-kg-drug-repurposing.svg
```

### Post-Processing Notes
- Include specific edge type counts
- Show actual drug-disease predictions
- Add database source annotations

### Fallback Description
"Knowledge graph drug repurposing: heterogeneous graph structure with drugs, proteins, diseases, and pathways; multi-hop reasoning paths providing mechanistic hypotheses; link prediction for new drug-disease associations; and foundation model embeddings enhancing node representations beyond database annotations."

### Caption Recommendation
"Knowledge graph reasoning for drug repurposing. (A) Heterogeneous knowledge graph structure with multiple node types (drugs, proteins, diseases, pathways) and relationship types. (B) Multi-hop reasoning: a drug might treat a disease through a path like Drug → binds → Protein → pathway → Disease. (C) Link prediction: GNNs learn embeddings to score potential new drug-disease associations. (D) Foundation model enhancement: FM embeddings capture functional similarity that database annotations miss."

---

## Figure 6: Network Study Bias

### Files
- `figs/part_4/ch18/06-fig-network-bias.svg`

### Priority
**Enhancing** - Critical limitation

### Content Description
Visualization of study bias in biological networks: correlation between node degree and publication count, implications for GNN predictions.

### DALL-E Prompt
```
Scientific illustration showing study bias in biological networks for computational biology. Single panel with multiple elements.

MAIN PLOT: Scatter plot with log-log axes. X-axis: "Number of publications" (log scale, 1 to 10,000+). Y-axis: "Node degree in PPI network" (log scale, 1 to 1,000+). Strong positive correlation visible. Well-studied genes labeled (TP53, BRCA1, EGFR) as high-degree, high-publication points. Novel/understudied genes clustered at low degree, low publication corner.

SIDE ANNOTATIONS:
- Arrow pointing to high-degree hub: "Well-studied genes become network hubs"
- Arrow pointing to peripheral nodes: "Understudied genes appear peripheral"
- Warning box: "Risk: GNN prioritizes already-known genes"

BOTTOM PANEL: Small diagram showing mitigation strategies as icons:
1) Degree normalization (mathematical adjustment icon)
2) Attention to edge confidence (reliability weight icon)
3) Temporal holdout evaluation (time arrow icon)

Professional scientific visualization, scatter plot style, white background, clear annotations highlighting the bias problem.

Save as: 06-fig-network-bias.svg
```

### Post-Processing Notes
- Add actual correlation coefficient
- Include specific gene examples
- Show confidence intervals

### Fallback Description
"Study bias in biological networks: scatter plot showing strong correlation between publication count and network degree, with well-studied genes like TP53 and BRCA1 as high-degree hubs while understudied genes appear peripheral regardless of true biology. This bias causes GNNs to prioritize already-known genes."

### Caption Recommendation
"Study bias in biological networks. Strong correlation between publication count and network degree means well-characterized genes (TP53, BRCA1, EGFR) appear as highly connected hubs while understudied genes are peripheral. This ascertainment bias causes GNNs to preferentially propagate signal toward already-known genes. Mitigation strategies include degree normalization, edge confidence weighting, and temporal holdout evaluation."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Biological Networks | 4 | Essential | Medium |
| Message Passing | 4 | High | Medium |
| FM + GNN Integration | 4 | Essential | Medium |
| Disease Gene Prioritization | 4 | High | High |
| KG Drug Repurposing | 4 | High | High |
| Network Bias | 1 | Enhancing | Low |

## Recommended Generation Order
1. Biological Networks (landscape foundation)
2. Message Passing (core algorithm)
3. FM + GNN Integration (central paradigm)
4. Disease Gene Prioritization (application)
5. KG Drug Repurposing (translational application)
6. Network Bias (critical limitation)

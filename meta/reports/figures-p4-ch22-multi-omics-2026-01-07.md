# Figure Report: Chapter 22 - Multi-Omics Integration

**Chapter:** p4-ch22-multi-omics.qmd
**Date:** 2026-01-07
**Total Figures:** 5 (19 files)
**Format:** SVG (for scalability)

---

## Figure 1: The Integration Paradox

### Files
- `figs/part_4/ch19/01-A-fig-integration-paradox.svg`
- `figs/part_4/ch19/01-B-fig-integration-paradox.svg`
- `figs/part_4/ch19/01-C-fig-integration-paradox.svg`
- `figs/part_4/ch19/01-D-fig-integration-paradox.svg`

### Priority
**Essential** - Central tension of the chapter

### Content Description
Four-panel figure showing the promise and paradox of multi-omics integration: what each modality captures, when integration hurts performance, and when it helps.

### DALL-E Prompt
```
Scientific illustration of the multi-omics integration paradox for computational biology textbook. Four panels.

PANEL A (The Promise): Four columns showing different omics layers. Genomics (DNA helix): "Heritable potential." Transcriptomics (mRNA): "Current state." Proteomics (protein structure): "Functional complement." Metabolomics (small molecules): "Downstream biochemistry." Arrow suggesting integration should improve prediction.

PANEL B (The Paradox): Performance curve showing counterintuitive result. X-axis: number of modalities. Y-axis: prediction performance. Curve peaks at 1-2 modalities, then drops with more. Annotations: "More features → more overfitting," "Missing data compounds problem," "Noise overwhelms signal."

PANEL C (When Integration Helps): Three scenarios with green checkmarks. 1) Complementary information (genomics + expression for complex traits). 2) Cross-modality validation (concordant signals increase confidence). 3) Mechanistic interpretation (trace causal cascade).

PANEL D (When Integration Hurts): Three scenarios with red X marks. 1) Redundant information (correlated features inflate dimensionality). 2) Batch effects across modalities (spurious correlations). 3) Sample size dilution (only patients with all modalities used).

Professional scientific illustration, clean infographic style, white background, contrasting colors for help vs hurt.

Save as: 01-A-fig-integration-paradox.svg through 01-D-fig-integration-paradox.svg
```

### Post-Processing Notes
- Add specific performance metrics examples
- Include real-world cohort size examples
- Show batch effect visualization

### Fallback Description
"The multi-omics integration paradox: different modalities capture complementary biology, but naive integration often degrades performance due to overfitting, noise, and missing data. Integration helps when information is complementary and hurts when redundant or confounded by batch effects."

### Caption Recommendation
"The multi-omics integration paradox. (A) Promise: each modality captures different aspects of biology—genomics shows heritable potential, transcriptomics reveals current state, proteomics measures functional complement, metabolomics tracks downstream biochemistry. (B) Paradox: more modalities can mean worse predictions when noise overwhelms signal. (C) When integration helps: complementary information, cross-modality validation, and mechanistic interpretation. (D) When integration hurts: redundant features, batch effects, and sample size reduction from incomplete overlap."

---

## Figure 2: Fusion Strategy Comparison

### Files
- `figs/part_4/ch19/02-A-fig-fusion-strategies.svg`
- `figs/part_4/ch19/02-B-fig-fusion-strategies.svg`
- `figs/part_4/ch19/02-C-fig-fusion-strategies.svg`

### Priority
**Essential** - Core methodological framework

### Content Description
Three-panel comparison of early, late, and intermediate fusion strategies with their tradeoffs.

### DALL-E Prompt
```
Scientific illustration comparing multi-omics fusion strategies for computational biology. Three panels.

PANEL A (Early Fusion): Flow diagram. Three input modalities (genomics, transcriptomics, proteomics) as separate feature vectors. Concatenation operator joining all features. Single unified model processing concatenated input. Output prediction. Pros listed: "Can learn cross-modal interactions." Cons listed: "Curse of dimensionality, requires complete data."

PANEL B (Late Fusion): Flow diagram. Three separate models, one per modality. Each produces independent prediction/score. Ensemble combiner merging predictions (weighted average, voting, or meta-learner). Final output. Pros: "Handles missing modalities, modality-specific architectures." Cons: "Cannot learn feature-level interactions."

PANEL C (Intermediate Fusion): Flow diagram. Three modality-specific encoders. Each encoder outputs embedding into shared latent space (central circle). Alignment mechanisms shown (contrastive, reconstruction losses). Downstream task head on shared space. Pros: "Flexibility + robustness." Cons: "Alignment complexity."

SUMMARY TABLE at bottom comparing: cross-modal interactions (Early: yes, Late: no, Intermediate: yes), missing data handling (Early: poor, Late: excellent, Intermediate: good), computational cost.

Professional scientific illustration, flowchart style, white background, consistent visual language across panels.

Save as: 02-A-fig-fusion-strategies.svg through 02-C-fig-fusion-strategies.svg
```

### Post-Processing Notes
- Use consistent modality colors
- Add dimensionality annotations
- Include specific model architecture examples

### Fallback Description
"Fusion strategy comparison: early fusion concatenates features before modeling (learns interactions but requires complete data), late fusion combines model predictions (handles missing data but no feature interactions), intermediate fusion learns shared latent space (balances flexibility and robustness)."

### Caption Recommendation
"Multi-omics fusion strategies. (A) Early fusion: concatenate features before modeling. Enables cross-modal interaction learning but requires complete data and suffers from dimensionality. (B) Late fusion: train separate models and combine predictions. Handles missing modalities but cannot learn feature interactions. (C) Intermediate fusion: modality-specific encoders project to shared latent space. Balances interaction learning with missing data robustness."

---

## Figure 3: Intermediate Fusion Architecture Details

### Files
- `figs/part_4/ch19/03-A-fig-intermediate-fusion.svg`
- `figs/part_4/ch19/03-B-fig-intermediate-fusion.svg`
- `figs/part_4/ch19/03-C-fig-intermediate-fusion.svg`
- `figs/part_4/ch19/03-D-fig-intermediate-fusion.svg`

### Priority
**High** - Detailed architecture for dominant approach

### Content Description
Detailed architecture of intermediate fusion: modality-specific encoders, shared latent space with alignment mechanisms, and missing modality handling.

### DALL-E Prompt
```
Scientific illustration of intermediate fusion architecture for multi-omics integration. Four panels.

PANEL A (Modality-Specific Encoders): Three encoder architectures shown side by side. Expression VAE (variational autoencoder structure). Methylation CNN (1D convolution over genomic coordinates). Proteomics MLP (dense layers). Each labeled with "Tailored to modality characteristics."

PANEL B (Shared Latent Space): Central shared space as circle/ellipse. All encoders pointing to same space with arrows. Loss functions listed around space: "Reconstruction loss," "Contrastive loss," "Graph constraints." Annotation "All embeddings same dimensionality."

PANEL C (Downstream Task Head): Shared latent space feeding into task-specific heads. Classifier head for prediction. Regression head for continuous outcomes. Multiple tasks possible from same representation. Cross-modal reasoning enabled.

PANEL D (Missing Modality Handling): Two scenarios. Left: complete sample with all three encoders firing, full embedding. Right: partial sample with only two modalities, partial embedding (dashed outline for missing). Annotation "Graceful degradation" - still produces useful representation.

Technical architecture diagram style, white background, neural network visualization conventions.

Save as: 03-A-fig-intermediate-fusion.svg through 03-D-fig-intermediate-fusion.svg
```

### Post-Processing Notes
- Add embedding dimensionalities
- Show loss function equations
- Include specific architecture parameters

### Fallback Description
"Intermediate fusion architecture: modality-specific encoders (VAE for expression, CNN for methylation, MLP for proteomics) project to shared latent space aligned through reconstruction, contrastive, and graph constraints. Downstream task heads operate on shared space, enabling graceful degradation when modalities are missing."

### Caption Recommendation
"Intermediate fusion architecture in detail. (A) Modality-specific encoders tailored to each data type: VAE for expression handling sparsity, CNN for methylation along genomic coordinates, MLP for proteomics. (B) Shared latent space: encoders produce embeddings aligned through reconstruction loss, contrastive terms, and biological graph constraints. (C) Downstream task heads operate on the shared representation, enabling cross-modal reasoning. (D) Missing modality handling: partial samples use only available encoders, enabling graceful degradation rather than sample exclusion."

---

## Figure 4: Clinical Multi-Modal Integration

### Files
- `figs/part_4/ch19/04-A-fig-clinical-multimodal.svg`
- `figs/part_4/ch19/04-B-fig-clinical-multimodal.svg`
- `figs/part_4/ch19/04-C-fig-clinical-multimodal.svg`
- `figs/part_4/ch19/04-D-fig-clinical-multimodal.svg`

### Priority
**High** - Clinical translation relevance

### Content Description
Patient-level integration of EHR, imaging, and molecular data for clinical prediction tasks.

### DALL-E Prompt
```
Scientific illustration of clinical multi-modal data integration for precision medicine. Four panels.

PANEL A (Data Modalities): Three data sources visualized. EHR: timeline of diagnoses, procedures, medications, lab values (longitudinal). Imaging: CT scan, MRI brain, histopathology slide icons (spatial). Molecular: DNA helix, expression heat map, protein network (static/omics). Each labeled with key characteristics.

PANEL B (Modality-Specific Encoders): Three encoders. EHR transformer processing event sequence over time. Imaging vision encoder (CNN/ViT) processing scan. Molecular FM embeddings from pretrained models. Each produces fixed-size patient embedding.

PANEL C (Patient Representation Space): Central shared space with all modalities contributing. Cross-modal consistency arrows: EHR predicts molecular state, imaging consistent with trajectory. Unified patient embedding combining all sources.

PANEL D (Clinical Prediction Tasks): Multiple downstream applications. Risk stratification (probability bars). Treatment response prediction (responder/non-responder). Prognosis/survival (Kaplan-Meier curve icon). Callout box: "Not all patients have all data - must handle missing modalities."

Clinical/medical illustration style, white background, patient-centric visualization, practical deployment focus.

Save as: 04-A-fig-clinical-multimodal.svg through 04-D-fig-clinical-multimodal.svg
```

### Post-Processing Notes
- Add specific clinical examples
- Include temporal alignment challenges
- Show realistic missingness patterns

### Fallback Description
"Clinical multi-modal integration: combining longitudinal EHR data, spatial imaging, and static molecular measurements through modality-specific encoders into a unified patient representation for clinical prediction tasks including risk stratification, treatment response, and prognosis."

### Caption Recommendation
"Clinical multi-modal integration. (A) Data modalities: longitudinal EHR (diagnoses, procedures, labs), spatial imaging (CT, MRI, histopathology), and static molecular measurements (genomics, expression, proteomics). (B) Modality-specific encoders: EHR transformer for event sequences, vision encoder for imaging, foundation model embeddings for molecular data. (C) Patient representation space: unified embedding where EHR predicts molecular state and imaging is consistent with clinical trajectory. (D) Clinical prediction tasks: risk stratification, treatment response, and prognosis—with the practical requirement of handling incomplete data."

---

## Figure 5: Information Cascade from Variant to Phenotype

### Files
- `figs/part_4/ch19/05-A-fig-information-cascade.svg`
- `figs/part_4/ch19/05-B-fig-information-cascade.svg`
- `figs/part_4/ch19/05-C-fig-information-cascade.svg`
- `figs/part_4/ch19/05-D-fig-information-cascade.svg`

### Priority
**High** - Conceptual systems biology framework

### Content Description
Systems biology view tracing information flow from genetic variants through molecular layers to clinical phenotypes, including bottleneck modality concept.

### DALL-E Prompt
```
Scientific illustration of the information cascade from genetic variant to clinical phenotype. Four panels.

PANEL A (The Causal Cascade): Vertical flow diagram. Top: Genetic variant (SNP symbol). Arrow labeled "cis-regulation." Expression change (mRNA up/down). Arrow labeled "translation." Protein change (structure altered). Arrow labeled "metabolism." Metabolite change (pathway flux). Arrow labeled "cellular." Cell behavior change. Arrow labeled "tissue." Clinical phenotype at bottom. Full cascade visualized.

PANEL B (Where Each Modality Provides Information): Same cascade with modality labels at each level. Genomics at variant level (starting point). Transcriptomics at expression (current state). Proteomics at protein (functional complement). Metabolomics at metabolite (downstream). Clinical data at phenotype (manifestation). Each labeled with what it measures.

PANEL C (Bottleneck Modalities): Three scenarios. 1) Coding variant: bottleneck at protein structure (protein box highlighted). 2) Regulatory variant: bottleneck at expression level (expression box highlighted). 3) Some phenotypes: bottleneck downstream (phenotype box highlighted, molecular less informative).

PANEL D (Integration Implications): Decision tree or flowchart. "What drives your phenotype?" → If coding variants → prioritize protein features. → If regulatory → prioritize expression. → Complex trait → integrate multiple levels. Annotation "Not all modalities equally informative for all questions."

Systems biology illustration style, causal diagram conventions, white background, clear flow direction.

Save as: 05-A-fig-information-cascade.svg through 05-D-fig-information-cascade.svg
```

### Post-Processing Notes
- Add specific gene/disease examples
- Include quantitative effect sizes
- Show causal vs correlational distinction

### Fallback Description
"Information cascade from variant to phenotype: genetic variants cause expression changes, which alter protein levels, affecting metabolic flux, changing cell behavior, and ultimately manifesting as clinical phenotypes. Different modalities provide information at different levels, with 'bottleneck modalities' being most directly relevant depending on the variant type."

### Caption Recommendation
"Systems biology view of multi-omics integration. (A) The causal cascade: genetic variants propagate through molecular layers—expression, protein, metabolite, cellular behavior—to clinical phenotype. (B) Where each modality provides information: genomics captures the starting point, transcriptomics the current state, proteomics the functional complement, metabolomics downstream effects. (C) Bottleneck modalities: coding variants bottleneck at protein level, regulatory variants at expression level—determining which modality is most informative. (D) Integration implications: the causal architecture guides which modalities to prioritize for different biological questions."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Integration Paradox | 4 | Essential | Medium |
| Fusion Strategies | 3 | Essential | Medium |
| Intermediate Fusion | 4 | High | High |
| Clinical Multimodal | 4 | High | High |
| Information Cascade | 4 | High | Medium |

## Recommended Generation Order
1. Integration Paradox (central tension)
2. Fusion Strategies (methodological framework)
3. Intermediate Fusion (detailed architecture)
4. Information Cascade (conceptual framework)
5. Clinical Multimodal (translation)

# Figure Report: Chapter 29 - Drug Discovery

**Chapter:** p6-ch29-drug-discovery.qmd
**Date:** 2026-01-07
**Total Figures:** 5 (5 files)
**Format:** SVG (for scalability)

---

## Figure 1: Target Prioritization Pipeline

### Files
- `figs/part_6/ch29/01-fig-target-prioritization.svg`

### Priority
**Essential** - Core drug discovery workflow

### Content Description
Pipeline from disease understanding through target identification to validation, with FM contribution at each stage.

### DALL-E Prompt
```
Scientific illustration of drug target prioritization pipeline. Single horizontal flow panel.

PIPELINE STAGES (left to right):

STAGE 1 (Disease Understanding):
- GWAS signals icon
- Expression signatures
- Clinical observations
- "What genes are associated with disease?"
FM contribution: Integrate multi-omic signals

STAGE 2 (Causal Inference):
- Mendelian randomization
- Fine-mapping
- Perturbation evidence
- "Which associations are causal?"
FM contribution: Prioritize variants, predict effects

STAGE 3 (Target Properties):
- Druggability assessment
- Safety profile
- Expression pattern
- "Can we drug this target safely?"
FM contribution: Predict binding pockets, off-target effects

STAGE 4 (Validation):
- CRISPR screens
- Animal models
- Biomarker development
- "Does modulation affect disease?"
FM contribution: Design experiments, interpret results

OUTPUT: Ranked target list with confidence scores

BOTTOM: Success rate annotation - "Only ~5% of targets that enter clinical trials succeed"

FILTER FUNNEL on side showing targets dropping out at each stage.

Professional drug discovery style, pipeline visualization, pharmaceutical iconography, white background.

Save as: 01-fig-target-prioritization.svg
```

### Post-Processing Notes
- Add specific gene examples
- Include success rate statistics
- Show decision criteria

### Fallback Description
"Drug target prioritization pipeline: from disease association (GWAS, expression) through causal inference (MR, fine-mapping) and target properties (druggability, safety) to validation (CRISPR, animal models). Foundation models contribute at each stage by integrating signals, prioritizing variants, predicting druggability, and interpreting validation results."

### Caption Recommendation
"Drug target prioritization pipeline. Starting from disease understanding (GWAS, expression signatures), targets progress through causal inference (Mendelian randomization confirms causation), target property assessment (druggability, safety), and experimental validation (CRISPR, animal models). Foundation models contribute at each stage: integrating multi-omic associations, prioritizing causal variants, predicting druggability, and interpreting validation data. Critical context: only ~5% of targets entering clinical development succeed."

---

## Figure 2: Network-Based Target Discovery

### Files
- `figs/part_6/ch29/02-fig-network-target-discovery.svg`

### Priority
**High** - Graph-based discovery

### Content Description
How biological networks combined with FM embeddings enable target discovery through guilt-by-association and network propagation.

### DALL-E Prompt
```
Scientific illustration of network-based drug target discovery. Single panel with network visualization.

MAIN NETWORK VISUALIZATION (center):
- Protein-protein interaction network
- Known disease genes highlighted (red nodes)
- Candidate targets highlighted (orange nodes, connected to disease genes)
- Drug targets highlighted (blue, connected to candidates)
- Edge thickness: interaction confidence
- Node size: degree/centrality

INSET 1 (top left): FM Node Features
- Each protein node has ESM embedding
- Functional similarity encoded
- Enables better propagation

INSET 2 (top right): Propagation Algorithm
- Start from known disease genes
- Propagate signal through network
- Rank by accumulated score
- Top-ranked = candidate targets

INSET 3 (bottom): Network Properties
- Disease module (cluster of disease genes)
- Network proximity to existing drugs
- Pathway enrichment

OUTPUT BOX (right):
Ranked candidate list:
1. Gene A - high network score, druggable
2. Gene B - moderate score, novel
3. Gene C - connected to approved drug (repurposing)

ANNOTATION: "Network context reveals targets missed by GWAS alone"

Professional systems biology style, network diagram, node-link visualization, white background.

Save as: 02-fig-network-target-discovery.svg
```

### Post-Processing Notes
- Add specific network statistics
- Include propagation formula
- Show disease module structure

### Fallback Description
"Network-based target discovery: protein-protein interaction network with known disease genes, candidate targets identified through network propagation, and drug targets connected to candidates. FM embeddings provide node features encoding functional similarity. Network context reveals targets missed by association studies alone."

### Caption Recommendation
"Network-based drug target discovery. Known disease genes (red) seed network propagation through protein-protein interactions. Candidate targets (orange) accumulate high scores based on network proximity. Foundation model embeddings (ESM) provide node features that encode functional similarity, improving propagation beyond topology alone. Network context reveals targets missed by GWAS: genes may not harbor risk variants themselves but are functionally connected to disease mechanisms."

---

## Figure 3: Drug-Target Interaction Prediction

### Files
- `figs/part_6/ch29/03-fig-drug-target-prediction.svg`

### Priority
**High** - Core computational approach

### Content Description
How FM representations enable drug-target binding prediction and drug repurposing.

### DALL-E Prompt
```
Scientific illustration of drug-target interaction prediction using foundation models. Single panel with architecture diagram.

ARCHITECTURE:

INPUT BRANCH 1 (Drug):
- Chemical structure (SMILES/graph)
- Through chemical encoder (ChemBERTa, MolBERT)
- Drug embedding vector

INPUT BRANCH 2 (Target):
- Protein sequence
- Through protein FM (ESM-2)
- Target embedding vector

INTERACTION PREDICTION:
- Concatenate/cross-attention embeddings
- MLP prediction head
- Output: binding probability, affinity prediction

TRAINING DATA:
- Known drug-target pairs (positive)
- Non-interacting pairs (negative)
- ChEMBL, DrugBank sources

APPLICATIONS (bottom):
Three use cases:
1) Virtual screening: Score all targets for new drug
2) Drug repurposing: Score all drugs for disease target
3) Off-target prediction: Identify unintended interactions

VALIDATION:
- Experimental binding assays (IC50, Kd)
- Cell-based screens
- Clinical observations

Professional computational drug discovery style, neural network architecture, white background.

Save as: 03-fig-drug-target-prediction.svg
```

### Post-Processing Notes
- Add specific model names
- Include performance metrics
- Show embedding space visualization

### Fallback Description
"Drug-target interaction prediction: drug structures encoded by chemical models, protein targets encoded by protein FMs, embeddings combined for binding prediction. Applications include virtual screening, drug repurposing, and off-target prediction. Validation requires experimental binding assays."

### Caption Recommendation
"Drug-target interaction prediction with foundation models. Drug structures are encoded by chemical language models (ChemBERTa) while protein targets are encoded by protein foundation models (ESM-2). Combined embeddings predict binding probability and affinity. Applications span virtual screening (score targets for new drugs), drug repurposing (score known drugs for new targets), and off-target prediction (identify safety liabilities). Experimental validation remains essential: computational predictions prioritize but cannot substitute for binding assays."

---

## Figure 4: Perturb-seq for Mechanism Discovery

### Files
- `figs/part_6/ch29/04-fig-perturb-seq.svg`

### Priority
**High** - Interventional data source

### Content Description
Perturb-seq experimental design and how FMs integrate with perturbation data for mechanism discovery.

### DALL-E Prompt
```
Scientific illustration of Perturb-seq for drug target mechanism discovery. Single panel with experimental workflow.

EXPERIMENTAL WORKFLOW (top to bottom):

STEP 1 (CRISPR Library):
- Pooled CRISPR library targeting 100s-1000s of genes
- Each guide has unique barcode
- Library transduced into cells

STEP 2 (Single-Cell Capture):
- Cells captured individually
- 10x Genomics or similar platform
- Each cell: expression profile + guide identity

STEP 3 (Readout Matrix):
- Cells × genes expression matrix
- Cells grouped by which gene was perturbed
- Perturbation → expression signature

DATA STRUCTURE (middle):
Matrix visualization:
- Rows: perturbations (gene knockouts)
- Columns: genes (expression changes)
- Color: effect magnitude
Annotation: "Direct observation of gene-gene regulatory relationships"

FM INTEGRATION (bottom):
Three applications:
1) Predict perturbation effects before experiment (virtual screening)
2) Interpret signatures using FM embeddings (mechanism)
3) Identify missing perturbations to test (active learning)

OUTPUT:
- Gene regulatory network
- Drug target mechanism
- Resistance mechanisms

Professional molecular biology style, experimental workflow, matrix visualization, white background.

Save as: 04-fig-perturb-seq.svg
```

### Post-Processing Notes
- Add specific throughput numbers
- Include cost considerations
- Show downstream analysis

### Fallback Description
"Perturb-seq workflow: CRISPR library targeting genes, single-cell capture with guide identification, expression readout per perturbation. Data matrix shows perturbation-expression relationships. FMs predict effects, interpret signatures, and prioritize experiments. Outputs include regulatory networks and drug mechanism understanding."

### Caption Recommendation
"Perturb-seq for mechanism discovery. Pooled CRISPR libraries target hundreds to thousands of genes; single-cell capture identifies both the perturbation (guide barcode) and its effect (expression profile). The resulting matrix directly measures gene-gene regulatory relationships—interventional data that foundation models cannot learn from observation alone. FM integration: predict perturbation effects for virtual screening, interpret expression signatures for mechanism discovery, and identify informative perturbations for active learning."

---

## Figure 5: Biomarker Discovery Pipeline

### Files
- `figs/part_6/ch29/05-fig-biomarker-pipeline.svg`

### Priority
**High** - Clinical development support

### Content Description
Pipeline from FM features to validated biomarkers for patient stratification and response prediction.

### DALL-E Prompt
```
Scientific illustration of biomarker discovery pipeline using foundation models. Single horizontal panel.

PIPELINE (left to right):

STAGE 1 (FM Feature Extraction):
- Patient molecular data (genomic, expression, protein)
- Through respective FMs
- High-dimensional embeddings extracted
Icon: Feature space with patient points

STAGE 2 (Association Discovery):
- Correlate FM features with clinical outcomes
- Response vs non-response
- Survival, progression
- Statistical testing with multiple testing correction

STAGE 3 (Candidate Biomarkers):
- Features that distinguish responders
- Interpretability analysis: which genes/variants?
- Biological pathway enrichment
- List of candidate markers

STAGE 4 (Technical Validation):
- Analytical validation (reproducibility, precision)
- Assay development (from FM feature to measurable test)
- Independent cohort replication

STAGE 5 (Clinical Validation):
- Prospective trials
- Regulatory submission (companion diagnostic)
- Clinical utility demonstration

OUTPUT:
- Stratification biomarker (who benefits?)
- Predictive biomarker (which treatment?)
- Prognostic biomarker (what outcome?)

TIMELINE: Discovery (months) → Technical validation (months-year) → Clinical validation (years)

BOTTLENECK annotation: "Clinical validation is rate-limiting step"

Professional clinical development style, pipeline visualization, white background.

Save as: 05-fig-biomarker-pipeline.svg
```

### Post-Processing Notes
- Add specific biomarker examples
- Include regulatory pathway
- Show companion diagnostic path

### Fallback Description
"Biomarker discovery pipeline: FM feature extraction from patient data, association discovery with clinical outcomes, candidate biomarker identification with interpretability, technical validation (assay development, replication), and clinical validation (prospective trials, regulatory approval). Clinical validation is rate-limiting—years versus months for discovery."

### Caption Recommendation
"Biomarker discovery pipeline with foundation models. FM embeddings from patient molecular data provide rich features for association discovery with clinical outcomes. Candidate biomarkers emerge from features distinguishing responders from non-responders. Technical validation develops reproducible assays; clinical validation demonstrates utility in prospective trials. Timeline reality: discovery in months, but clinical validation requires years. Foundation models accelerate discovery but cannot bypass the clinical validation bottleneck required for regulatory approval and clinical adoption."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Target Prioritization | 1 | Essential | Medium |
| Network Discovery | 1 | High | High |
| Drug-Target Prediction | 1 | High | High |
| Perturb-seq | 1 | High | Medium |
| Biomarker Pipeline | 1 | High | Medium |

## Recommended Generation Order
1. Target Prioritization (overview pipeline)
2. Drug-Target Prediction (computational core)
3. Network Discovery (graph methods)
4. Perturb-seq (interventional data)
5. Biomarker Pipeline (clinical development)

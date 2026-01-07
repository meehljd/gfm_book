# Figure Report: Chapter 25 - Causal Inference with Foundation Models

**Chapter:** p5-ch25-causal.qmd
**Date:** 2026-01-07
**Total Figures:** 4 (4 files)
**Format:** SVG (for scalability)

---

## Figure 1: Ladder of Causation

### Files
- `figs/part_5/ch25/01-fig-ladder-causation.svg`

### Priority
**High** - Core conceptual framework

### Content Description
Pearl's ladder of causation applied to genomics, showing the qualitative distinction between association, intervention, and counterfactual reasoning.

### DALL-E Prompt
```
Scientific illustration of Pearl's ladder of causation applied to genomics. Single panel with three-level ladder structure.

LADDER STRUCTURE (bottom to top):

RUNG 1 (BOTTOM - ASSOCIATION):
- Question: "What does seeing X tell me about Y?"
- Genomic example: "Observing variant V, predict phenotype P"
- Icon: Correlation scatter plot, eye symbol
- Foundation models operate here ← highlighted
- Annotation "P(Y|X) - observational"

RUNG 2 (MIDDLE - INTERVENTION):
- Question: "What happens to Y if I change X?"
- Genomic example: "If we edit variant V, what happens to P?"
- Icon: CRISPR scissors, do() operator
- Perturbation experiments provide ground truth ← highlighted
- Annotation "P(Y|do(X)) - interventional"
- Requires causal structure knowledge

RUNG 3 (TOP - COUNTERFACTUAL):
- Question: "What would Y have been if X had been different?"
- Genomic example: "For this patient with V who developed P, would they have developed P without V?"
- Icon: Parallel universes, individual person
- Individual-level reasoning
- Annotation "P(Y_x|X=x', Y=y) - counterfactual"

GAPS BETWEEN RUNGS (emphasized):
- Gap 1→2: "Cannot cross with more data alone"
- Gap 2→3: "Requires individual-level noise models"

SIDE BOX: "Key insight: Rung 1 accuracy does NOT guarantee Rung 2 accuracy. The gap is qualitative, not quantitative."

Professional scientific style, ladder visualization, blue/green/purple color progression, white background.

Save as: 01-fig-ladder-causation.svg
```

### Post-Processing Notes
- Add mathematical notation
- Include specific genomic examples
- Emphasize the qualitative gaps

### Fallback Description
"Pearl's ladder of causation: Rung 1 (association) asks what observing X tells us about Y—foundation models operate here. Rung 2 (intervention) asks what happens if we change X—requires causal structure. Rung 3 (counterfactual) asks what would have happened for a specific individual. The gaps between rungs are qualitative—more data cannot bridge them."

### Caption Recommendation
"Pearl's ladder of causation applied to genomics. **Rung 1 (Association)**: Foundation models learn P(Y|X)—observing variant V, predict phenotype P. **Rung 2 (Intervention)**: P(Y|do(X))—if we edit V, what happens to P? Requires causal structure, not just correlations. **Rung 3 (Counterfactual)**: For this specific patient, what would have happened under alternative conditions? The gaps are qualitative: predictive accuracy at Rung 1 provides no guarantee of accuracy at Rungs 2-3."

---

## Figure 2: GWAS to Causal Gene Pipeline

### Files
- `figs/part_5/ch25/02-fig-gwas-to-gene.svg`

### Priority
**High** - Key genomics application

### Content Description
Pipeline from GWAS signal to causal gene identification, showing where foundation models contribute.

### DALL-E Prompt
```
Scientific illustration of GWAS-to-causal-gene pipeline. Single horizontal flow panel.

STAGE 1 (LEFT - GWAS Signal):
- Manhattan plot showing genome-wide peaks
- Zoom into one locus
- Many correlated variants in LD (linkage disequilibrium block)
- Annotation "Associated locus - but which variant is causal?"

STAGE 2 (Fine-Mapping):
- Same locus with posterior probabilities
- Statistical fine-mapping narrows to credible set
- FM predictions overlay (chromatin, binding, splicing effects)
- Credible set: 3-5 variants highlighted
- Annotation "Foundation models provide functional annotations"

STAGE 3 (Gene Assignment - Multiple Evidence):
Three parallel evidence tracks:
1) eQTL colocalization: "Variant affects Gene B expression"
2) Chromatin contacts (Hi-C): "Variant in enhancer contacting Gene B promoter"
3) FM variant effect predictions: "Variant disrupts regulatory element controlling Gene B"
Convergence arrows pointing to Gene B

STAGE 4 (RIGHT - Experimental Validation):
- CRISPR perturbation icon
- Allele-specific expression measurement
- Reporter assay
- Annotation "Ground truth from intervention"

BOTTOM: Evidence integration scoring showing confidence levels

FOUNDATION MODEL CONTRIBUTION highlighted at Stages 2-3 with boxes

Professional scientific style, pipeline flow diagram, white background.

Save as: 02-fig-gwas-to-gene.svg
```

### Post-Processing Notes
- Add specific gene examples
- Include statistical metrics
- Show integration scoring

### Fallback Description
"GWAS-to-causal-gene pipeline: GWAS identifies associated locus with many correlated variants, fine-mapping with FM annotations narrows to credible set, multiple evidence (eQTL, chromatin contacts, FM predictions) prioritizes target gene, experimental validation provides ground truth. Foundation models contribute at fine-mapping and gene assignment stages."

### Caption Recommendation
"From GWAS to causal gene. **Stage 1**: GWAS identifies associated locus with multiple variants in linkage disequilibrium. **Stage 2**: Fine-mapping with foundation model functional annotations narrows to credible set. **Stage 3**: Multiple evidence integration—eQTL colocalization, chromatin contacts, FM variant predictions—prioritizes target gene. **Stage 4**: Experimental validation provides causal ground truth. Foundation models accelerate stages 2-3 but cannot substitute for experimental validation."

---

## Figure 3: Closed-Loop Causal Learning

### Files
- `figs/part_5/ch25/03-fig-closed-loop-causal.svg`

### Priority
**High** - Path forward for causal FM

### Content Description
Design-build-test-learn cycle showing how foundation models can acquire causal knowledge through experimental iteration.

### DALL-E Prompt
```
Scientific illustration of closed-loop causal learning for foundation models. Circular flow diagram.

MAIN CYCLE (clockwise):

STEP 1 (TOP - PREDICT):
- Foundation model icon
- "Predict intervention effects based on current knowledge"
- Output: ranked list of candidate interventions
- Annotation "Initial predictions may be merely associational"

STEP 2 (RIGHT - EXPERIMENT):
- Automated platform icon (robot arm, plate)
- "Execute prioritized interventions"
- Examples: CRISPR perturbation, drug treatment, regulatory editing
- Throughput annotation: "100s-1000s per cycle"

STEP 3 (BOTTOM - OBSERVE):
- Readout icons: expression profiles, cell viability, phenotype measurements
- "Capture interventional outcomes"
- Data flowing to database

STEP 4 (LEFT - UPDATE):
- Model update icon
- "Retrain/fine-tune on interventional data"
- "Causal accuracy improves"
- Arrow back to Step 1

CENTER: "Each cycle adds interventional ground truth"

CONTRAST BOX (bottom):
Left side: "Standard FM training" - fixed observational data → associational patterns only
Right side: "Closed-loop training" - iterative interventional data → progressively causal knowledge

KEY INSIGHT: "Moving from Rung 1 to Rung 2 requires interventional data. Closed-loop provides it."

Professional scientific style, circular workflow, blue/green color scheme, white background.

Save as: 03-fig-closed-loop-causal.svg
```

### Post-Processing Notes
- Add specific throughput numbers
- Include real experimental examples
- Show learning curves

### Fallback Description
"Closed-loop causal learning: foundation model predicts intervention effects, automated platform executes interventions, readouts captured, model updated with interventional data. Each cycle adds ground truth that progressively shifts the model from associational (Rung 1) toward causal (Rung 2) knowledge—unlike standard training on fixed observational data."

### Caption Recommendation
"Closed-loop causal learning for foundation models. The cycle iterates between: (1) Predicting intervention effects from current knowledge, (2) Executing prioritized interventions on automated platforms, (3) Capturing experimental readouts, and (4) Updating the model with interventional data. Unlike standard training on observational data, closed-loop systems accumulate interventional ground truth that progressively improves causal accuracy—providing a path from Rung 1 (association) toward Rung 2 (intervention) of the causal ladder."

---

## Figure 4: Evidence Hierarchy for Drug Target Validation

### Files
- `figs/part_5/ch25/04-fig-evidence-hierarchy.svg`

### Priority
**Medium** - Clinical translation context

### Content Description
Pyramid showing evidence hierarchy from weakest (association) to strongest (clinical trials), with FM contribution highlighted.

### DALL-E Prompt
```
Scientific illustration of drug target validation evidence hierarchy. Pyramid structure with four levels.

PYRAMID (bottom to top):

LEVEL 1 (BOTTOM - WEAKEST - ASSOCIATION):
- Width: widest
- Content: "Observational association"
- Examples: "Expression correlates with disease", "FM prediction of target involvement"
- Foundation models operate here ← highlighted box
- Confidence: Low
- Color: Light blue

LEVEL 2 (MENDELIAN RANDOMIZATION):
- Content: "Human genetic evidence"
- Examples: "Genetic variant affecting target associated with disease outcome", "MR supports causal relationship"
- Annotation "Natural experiment from genetic randomization"
- Confidence: Moderate
- Color: Medium blue

LEVEL 3 (EXPERIMENTAL PERTURBATION):
- Content: "Direct causal test in models"
- Examples: "CRISPR KO affects disease phenotype", "Drug inhibition in animal model"
- Annotation "Interventional ground truth in model systems"
- Confidence: High
- Color: Darker blue

LEVEL 4 (TOP - STRONGEST - CLINICAL TRIAL):
- Width: narrowest
- Content: "Clinical intervention efficacy"
- Examples: "Phase III trial shows drug efficacy"
- Annotation "Definitive but expensive and slow"
- Confidence: Highest
- Color: Dark blue

SIDE ARROWS showing where FM contributes:
- Association discovery ← FM strong
- MR instrument selection ← FM helps
- Perturbation prioritization ← FM helps
- Clinical validation ← FM cannot substitute

BOTTOM BOX: "Key insight: FMs accelerate early stages but cannot replace later validation. Moving up the pyramid requires non-computational evidence."

Professional scientific style, pyramid diagram, blue gradient, white background.

Save as: 04-fig-evidence-hierarchy.svg
```

### Post-Processing Notes
- Add specific drug examples
- Include timeline estimates
- Show cost considerations

### Fallback Description
"Drug target validation evidence hierarchy: from weakest (observational association—where FMs operate) through Mendelian randomization (human genetic evidence) and experimental perturbation (direct causal test) to strongest (clinical trial efficacy). Foundation models accelerate early stages but cannot substitute for later experimental and clinical validation."

### Caption Recommendation
"Evidence hierarchy for drug target validation. **Weakest**: observational association—foundation models excel here but associations may be confounded. **Moderate**: Mendelian randomization provides human in-vivo causal evidence. **Strong**: Experimental perturbation directly tests causation in model systems. **Strongest**: Clinical trial efficacy is definitive but expensive. Foundation models accelerate association discovery, MR instrument selection, and perturbation prioritization, but cannot substitute for the experimental and clinical evidence required for confident target validation."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Ladder of Causation | 1 | High | Medium |
| GWAS to Gene Pipeline | 1 | High | High |
| Closed-Loop Causal Learning | 1 | High | Medium |
| Evidence Hierarchy | 1 | Medium | Low |

## Recommended Generation Order
1. Ladder of Causation (conceptual foundation)
2. Evidence Hierarchy (clinical context)
3. GWAS to Gene Pipeline (genomics application)
4. Closed-Loop Causal Learning (path forward)

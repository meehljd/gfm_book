# Figure Report: Chapter 30 - Sequence Design

**Chapter:** p6-ch30-design.qmd
**Date:** 2026-01-07
**Total Figures:** 7 (9 files)
**Format:** SVG (for scalability)

---

## Figure 1: Design Problem Formalism

### Files
- `figs/part_6/ch30/01-A-fig-design-formalism.svg`
- `figs/part_6/ch30/01-B-fig-design-formalism.svg`

### Priority
**Essential** - Conceptual foundation

### Content Description
Two-panel figure: forward prediction vs inverse design problem, and the design space landscape.

### DALL-E Prompt
```
Scientific illustration of sequence design problem formulation. Two panels.

PANEL A (Forward vs Inverse):
Two directions illustrated:

FORWARD (top):
Sequence → Model → Predicted Function
"Given sequence, predict what it does"
Arrow pointing right
Example: DNA sequence → Enformer → Expression prediction
Foundation models excel here ✓

INVERSE (bottom):
Desired Function → ??? → Sequence
"Given desired function, find sequence"
Arrow pointing left
Example: "High liver expression" → ??? → Optimal promoter
Much harder - combinatorial search required

Annotation: "Inverse design is not simply 'running the model backward'"

PANEL B (Design Space Landscape):
3D fitness landscape visualization.
X,Y axes: sequence space dimensions (abstract)
Z axis: fitness/function score
Surface showing peaks (good designs) and valleys (poor)

Key features marked:
- Global optimum (highest peak) - "Ideal but hard to find"
- Local optima (smaller peaks) - "Easy to get trapped"
- Starting point - "Random/natural sequence"
- Path showing optimization trajectory

Annotation: "Sequence space is vast: 4^N for DNA, 20^N for protein"

Professional scientific style, mathematical visualization, white background.

Save as: 01-A-fig-design-formalism.svg, 01-B-fig-design-formalism.svg
```

### Post-Processing Notes
- Add specific sequence space sizes
- Include optimization algorithm annotations
- Show multiple starting points

### Fallback Description
"Design problem formalism: forward prediction (sequence → function) is what FMs do well; inverse design (function → sequence) is much harder requiring combinatorial search through vast sequence space. Fitness landscape shows global optimum, local optima traps, and optimization trajectories."

### Caption Recommendation
"Sequence design problem formulation. (A) Forward versus inverse problems: foundation models excel at forward prediction (sequence → function) but inverse design (function → sequence) requires search through vast combinatorial spaces. (B) Design space landscape: sequence fitness varies across 4^N (DNA) or 20^N (protein) possibilities. Optimization must navigate between local optima traps toward global optimum—a fundamentally harder problem than prediction."

---

## Figure 2: Protein Design Approaches

### Files
- `figs/part_6/ch30/02-A-fig-protein-design.svg`
- `figs/part_6/ch30/02-B-fig-protein-design.svg`

### Priority
**High** - Core design methods

### Content Description
Two approaches: directed evolution in silico and generative design from priors.

### DALL-E Prompt
```
Scientific illustration of protein design approaches. Two panels.

PANEL A (Directed Evolution In Silico):
Evolutionary cycle diagram:
1) Start: parent sequence
2) Mutate: generate variants (point mutations, recombination)
3) Score: FM predicts fitness for each variant
4) Select: keep top scorers
5) Repeat: iterate for N generations
→ Improved sequence

Comparison to lab evolution:
- Lab: weeks per cycle, expensive
- In silico: seconds per cycle, cheap
- Hybrid: FM-guided lab evolution

FM role: Fitness predictor enables fast screening

PANEL B (Generative Design):
Alternative approach:
1) Train generative model (VAE, diffusion, autoregressive) on functional proteins
2) Sample from latent space or condition on desired properties
3) Generated sequences have FM-learned priors
4) Filter by property predictors

Examples:
- ProGen: autoregressive protein generation
- ProteinMPNN: structure-conditioned design
- RFdiffusion: diffusion-based backbone design

FM role: Generative prior from evolutionary data

Professional scientific style, evolutionary diagram for A, generative model diagram for B, white background.

Save as: 02-A-fig-protein-design.svg, 02-B-fig-protein-design.svg
```

### Post-Processing Notes
- Add specific model names
- Include success rate metrics
- Show experimental validation

### Fallback Description
"Protein design approaches: directed evolution in silico (mutate → FM score → select → repeat) enables fast virtual screening; generative design samples from FM-learned priors conditioned on desired properties. Both leverage FM representations but through different mechanisms."

### Caption Recommendation
"Protein design approaches. (A) Directed evolution in silico: generate variants through mutation, score with foundation models, select top performers, iterate. Achieves in seconds what lab evolution requires weeks for. (B) Generative design: sample from generative models (ProGen, ProteinMPNN, RFdiffusion) trained on evolutionary data, conditioning on desired properties. Foundation models contribute as fitness predictors (A) or as generative priors (B)—both leverage representations learned from millions of natural sequences."

---

## Figure 3: Regulatory Element Design

### Files
- `figs/part_6/ch30/03-fig-regulatory-design.svg`

### Priority
**High** - DNA design application

### Content Description
Designing synthetic promoters, enhancers, and other regulatory elements using DNA FMs.

### DALL-E Prompt
```
Scientific illustration of regulatory element design with DNA foundation models. Single panel with multiple elements.

DESIGN TARGETS (top row, four boxes):
1) Synthetic promoter: Control expression level
2) Tissue-specific enhancer: Restrict to target tissue
3) Synthetic 5' UTR: Optimize translation
4) CRISPR guide: Maximize on-target, minimize off-target

For each: icon and key design objective

DESIGN WORKFLOW (center):
Flow diagram:
Objective specification → Sequence generation → FM scoring → Selection → Experimental validation

Methods:
- Gradient-based optimization (backprop through FM)
- Evolutionary search (mutate + score)
- Generative models (conditional sampling)
- Hybrid approaches

FM CONTRIBUTION (right):
- Predict activity of candidate sequences
- Provide gradient signal for optimization
- Score off-target effects
- Predict tissue specificity

VALIDATION (bottom):
MPRA (massively parallel reporter assay) for high-throughput testing
Thousands of designs tested in parallel
Feedback to improve models

EXAMPLE SUCCESS:
"Designed promoter achieving 10x natural expression" with citation placeholder

Professional scientific style, regulatory genomics visualization, white background.

Save as: 03-fig-regulatory-design.svg
```

### Post-Processing Notes
- Add specific design examples
- Include MPRA workflow
- Show tissue specificity examples

### Fallback Description
"Regulatory element design: targets include synthetic promoters, tissue-specific enhancers, 5' UTRs, and CRISPR guides. Design workflow from objective specification through generation, FM scoring, selection, and MPRA validation. FMs predict activity, provide optimization gradients, and score off-target effects."

### Caption Recommendation
"Regulatory element design with DNA foundation models. Design targets span synthetic promoters (expression level), tissue-specific enhancers (spatial control), 5' UTRs (translation efficiency), and CRISPR guides (specificity). Workflow combines sequence generation methods (gradient optimization, evolutionary search, generative sampling) with FM-based scoring. Validation through MPRA enables testing thousands of designs in parallel, creating feedback loops that improve both designs and models."

---

## Figure 4: mRNA Therapeutic Optimization

### Files
- `figs/part_6/ch30/04-fig-mrna-optimization.svg`

### Priority
**High** - Therapeutics application

### Content Description
Design considerations for mRNA therapeutics: codon optimization, UTR design, modification selection.

### DALL-E Prompt
```
Scientific illustration of mRNA therapeutic design optimization. Single panel with mRNA structure and design elements.

mRNA STRUCTURE (center, horizontal):
5' cap → 5' UTR → Coding sequence → 3' UTR → Poly(A) tail
Each region highlighted with design considerations below

DESIGN ELEMENTS:

5' UTR Design (left):
- Kozak sequence optimization
- Secondary structure minimization
- uORF avoidance
- Translation initiation efficiency
FM contribution: Predict translation efficiency

Coding Sequence (center):
- Codon optimization for host tRNA pools
- GC content balancing
- Avoid immunogenic motifs
- Maintain mRNA structure
FM contribution: Codon-aware models predict expression

3' UTR Design (right):
- Stability elements
- miRNA binding site avoidance
- Half-life optimization
FM contribution: Predict degradation, localization

MODIFICATION Selection (bottom):
- N1-methylpseudouridine (m1Ψ) for immune evasion
- 5-methylcytosine for stability
- Trade-offs with translation efficiency

COVID VACCINE box: "BNT162b2 design choices" with key optimizations listed

MULTI-OBJECTIVE OPTIMIZATION note: Balance expression, stability, immunogenicity, manufacturability

Professional therapeutic development style, mRNA structure visualization, white background.

Save as: 04-fig-mrna-optimization.svg
```

### Post-Processing Notes
- Add specific codon optimization details
- Include COVID vaccine examples
- Show multi-objective tradeoffs

### Fallback Description
"mRNA therapeutic optimization: 5' UTR design (Kozak, structure), coding sequence (codon optimization, GC content), 3' UTR (stability, miRNA avoidance), and modification selection (m1Ψ for immune evasion). Multi-objective optimization balances expression, stability, and immunogenicity. COVID vaccines demonstrate successful application."

### Caption Recommendation
"mRNA therapeutic design optimization. Each region requires distinct considerations: 5' UTR affects translation initiation (Kozak sequence, structure minimization); coding sequence requires codon optimization balanced against GC content and immunogenicity; 3' UTR controls stability and localization; chemical modifications (N1-methylpseudouridine) reduce immunogenicity. Foundation models predict translation efficiency, stability, and immunogenic potential. COVID-19 mRNA vaccines demonstrate successful integration of these design principles."

---

## Figure 5: Antibody Design

### Files
- `figs/part_6/ch30/05-fig-antibody-design.svg`

### Priority
**High** - Therapeutic protein design

### Content Description
FM-guided antibody engineering: CDR optimization, humanization, and developability.

### DALL-E Prompt
```
Scientific illustration of antibody design with foundation models. Single panel with antibody structure and design workflow.

ANTIBODY STRUCTURE (left):
Y-shaped antibody diagram:
- Heavy chain (dark blue)
- Light chain (light blue)
- CDR loops highlighted (red): CDR1, CDR2, CDR3
- Framework regions labeled
- Fc region for effector functions

DESIGN CHALLENGES (center column):
1) Affinity maturation: Improve binding strength
2) Specificity: Reduce off-target binding
3) Humanization: Reduce immunogenicity
4) Developability: Aggregation, stability, expression

FM CONTRIBUTIONS (right column):
For each challenge:
1) Predict binding ΔG from sequence (ESM embeddings + docking)
2) Predict cross-reactivity from sequence similarity
3) Score humanness using human antibody corpus
4) Predict biophysical properties (aggregation, viscosity)

WORKFLOW (bottom):
Starting antibody → CDR mutagenesis library → FM scoring → Select candidates → Experimental validation → Iterate

Success metrics:
- Affinity: pM to nM range
- Humanness score: >90%
- Aggregation: <5%

CASE STUDY box: Example therapeutic antibody optimization

Professional biopharmaceutical style, antibody structure, white background.

Save as: 05-fig-antibody-design.svg
```

### Post-Processing Notes
- Add specific CDR sequences
- Include humanization scoring
- Show developability predictions

### Fallback Description
"Antibody design with FMs: structure showing CDR loops (binding) and framework (scaffold), design challenges (affinity, specificity, humanization, developability), and FM contributions (binding prediction, humanness scoring, aggregation prediction). Workflow iterates between FM-guided mutagenesis and experimental validation."

### Caption Recommendation
"Antibody design with foundation models. The antibody structure comprises framework regions (scaffold) and CDR loops (binding interface). Design challenges include affinity maturation (improve binding), specificity (reduce off-targets), humanization (reduce immunogenicity), and developability (ensure manufacturability). Foundation models contribute binding affinity prediction from sequence, humanness scoring against human antibody corpus, and biophysical property prediction (aggregation, stability). Iterative design cycles alternate between FM-guided mutagenesis and experimental validation."

---

## Figure 6: Design-Build-Test-Learn Cycle

### Files
- `figs/part_6/ch30/06-fig-dbtl-cycle.svg`

### Priority
**Essential** - Core iterative paradigm

### Content Description
The DBTL cycle for sequence design showing how FMs integrate with experimental automation.

### DALL-E Prompt
```
Scientific illustration of Design-Build-Test-Learn cycle for sequence design. Single panel with circular workflow.

CIRCULAR FLOW (clockwise):

DESIGN (12 o'clock position):
- FM predicts function from sequence
- Optimization identifies candidates
- Prioritize for synthesis
Icon: Computer/algorithm
FM role: Score and optimize

BUILD (3 o'clock position):
- DNA synthesis
- Assembly and cloning
- Cell transformation
Icon: DNA synthesis machine
Automation: Oligo synthesis, assembly robots

TEST (6 o'clock position):
- Functional assays
- High-throughput screening
- Readouts (expression, binding, activity)
Icon: Microplate, sequencer
Automation: Liquid handlers, plate readers

LEARN (9 o'clock position):
- Results back to model
- Update FM or downstream models
- Identify patterns, improve predictions
Icon: Data analysis, model update
FM role: Retrain, fine-tune, active learning

CENTER: "Iterative improvement"
Annotation: Each cycle improves both sequences AND models

SCALE annotations around cycle:
- Designs per cycle: 100s-1000s
- Synthesis time: days
- Assay time: days-weeks
- Learning: continuous

BOTTLENECK highlighted: Build and Test phases limit iteration speed

Professional synthetic biology style, circular workflow, white background.

Save as: 06-fig-dbtl-cycle.svg
```

### Post-Processing Notes
- Add specific throughput numbers
- Include cost estimates
- Show closed-loop automation

### Fallback Description
"DBTL cycle: Design (FM optimization) → Build (synthesis, assembly) → Test (functional assays) → Learn (update models) → repeat. Each cycle improves both designed sequences and FM predictions. Build and Test phases are bottlenecks limiting iteration speed."

### Caption Recommendation
"Design-Build-Test-Learn cycle for sequence engineering. **Design**: foundation models score candidates and optimization identifies promising sequences. **Build**: DNA synthesis and assembly create physical constructs. **Test**: functional assays measure actual performance. **Learn**: results update models for next cycle. Each iteration improves both designed sequences and predictive accuracy. Bottleneck reality: Build and Test phases (days to weeks) limit iteration speed despite fast computational Design (~seconds). Closed-loop automation increasingly accelerates the cycle."

---

## Figure 7: Generative Model Evaluation

### Files
- `figs/part_6/ch30/07-fig-generative-evaluation.svg`

### Priority
**High** - Evaluation framework

### Content Description
How to evaluate generative sequence models: diversity, novelty, validity, and function.

### DALL-E Prompt
```
Scientific illustration of generative model evaluation metrics. Single panel with evaluation framework.

EVALUATION DIMENSIONS (four quadrants):

TOP LEFT (Diversity):
- Are generated sequences varied?
- Metrics: sequence identity distribution, embedding space coverage
- Visualization: scatter plot of embeddings with natural (blue) and generated (orange) overlapping
- Good: covers natural space
- Bad: mode collapse (single cluster)

TOP RIGHT (Novelty):
- Are sequences genuinely new?
- Metrics: distance to nearest training example
- Visualization: histogram of distances
- Good: novel but plausible
- Bad: memorization (distance = 0) or random (very high distance)

BOTTOM LEFT (Validity):
- Are sequences structurally valid?
- Metrics: folds correctly, no stop codons, proper chemistry
- Visualization: % valid across samples
- Good: high validity rate
- Bad: many invalid sequences

BOTTOM RIGHT (Function):
- Do sequences actually work?
- Metrics: experimental activity, binding, expression
- Visualization: predicted vs measured function scatter
- Good: high correlation
- Bad: predictions don't match reality (ultimate test)

CENTER: Trade-offs note
"Optimizing one metric can harm others"
Example: High novelty may reduce validity

VALIDATION HIERARCHY (bottom):
Computational → In silico validation → Experimental validation
"Only wet lab validation confirms function"

Professional scientific style, metrics visualization, white background.

Save as: 07-fig-generative-evaluation.svg
```

### Post-Processing Notes
- Add specific metric formulas
- Include benchmark datasets
- Show correlation with experiments

### Fallback Description
"Generative model evaluation: diversity (varied outputs, not mode collapse), novelty (new sequences, not memorization), validity (proper structure/chemistry), and function (experimental activity). Trade-offs exist between metrics. Only experimental validation confirms function."

### Caption Recommendation
"Evaluating generative sequence models. Four dimensions: **Diversity** measures variation among outputs (avoiding mode collapse); **Novelty** assesses distance from training examples (avoiding memorization); **Validity** checks structural correctness (foldable, proper chemistry); **Function** measures experimental performance (ultimate test). These metrics can trade off—highly novel sequences may have lower validity. Critical insight: computational metrics provide useful screening, but only experimental validation confirms that generated sequences actually function as intended."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Design Formalism | 2 | Essential | Medium |
| Protein Design | 2 | High | High |
| Regulatory Design | 1 | High | Medium |
| mRNA Optimization | 1 | High | Medium |
| Antibody Design | 1 | High | High |
| DBTL Cycle | 1 | Essential | Low |
| Generative Evaluation | 1 | High | Medium |

## Recommended Generation Order
1. Design Formalism (conceptual foundation)
2. DBTL Cycle (iterative paradigm)
3. Protein Design (core methods)
4. Regulatory Design (DNA application)
5. mRNA Optimization (therapeutics)
6. Antibody Design (therapeutic proteins)
7. Generative Evaluation (assessment framework)

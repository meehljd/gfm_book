# Figure Report: Chapter 13 - Foundation Model Principles

**Chapter:** Part 3, Chapter 13 - Foundation Model Principles
**Date:** 2026-01-07
**Figures:** 5 conceptual figures (8 files)
**Format:** All figures should be generated/saved as .svg for scalability

---

## Figure 13.1: Paradigm Shift (Two-Panel)

**Files:**
- `figs/part_3/ch13/01-A-fig-paradigm-shift.svg`
- `figs/part_3/ch13/01-B-fig-paradigm-shift.svg`

**Priority:** Essential
**Type:** Conceptual comparison

### Panel A: Task-Specific Paradigm

**Content:** Show the old paradigm with multiple independent models, each trained from scratch for a specific task (splice prediction, TF binding, expression). Each has its own training data and cannot share knowledge.

**DALL-E Prompt:**
```
Create a scientific diagram showing task-specific model training paradigm. Save as: 01-A-fig-paradigm-shift.svg

Three separate vertical pipelines side-by-side:

PIPELINE 1:
- "Splice Data" → "Train Model A" → "Splice Predictor"

PIPELINE 2:
- "TF Binding Data" → "Train Model B" → "Binding Predictor"

PIPELINE 3:
- "Expression Data" → "Train Model C" → "Expression Predictor"

Each pipeline completely separate (no connections between them)
Label: "Task-Specific Paradigm"
Annotations:
- "No knowledge sharing"
- "Train from scratch each time"
- "Narrow capabilities"

Red X marks between pipelines showing isolation. Clean workflow diagram, white background. Professional ML paradigm illustration.
```

**Caption for Panel A:**
"Task-specific paradigm: isolated models for isolated tasks. Each application (splice prediction, transcription factor binding, expression) requires training a separate model from scratch on task-specific data. Knowledge about sequence patterns learned for one task cannot transfer to others, limiting efficiency and requiring substantial labeled data for each new application."

### Panel B: Foundation Model Paradigm

**Content:** Show the new paradigm with a single foundation model pretrained on diverse unlabeled data, then adapted with small task-specific heads for multiple downstream tasks. All share the same base representations.

**DALL-E Prompt:**
```
Create a scientific diagram showing foundation model paradigm. Save as: 01-B-fig-paradigm-shift.svg

Single unified architecture:

TOP: Large "Foundation Model" box trained on "Diverse Unlabeled Sequences"
- Label: "Pretrain once"
- Billions of parameters

BOTTOM: Three small task heads branching from foundation model:
- "Splice Adapter" → "Splice Prediction"
- "Binding Adapter" → "TF Binding"
- "Expression Adapter" → "Expression Prediction"

Connections showing shared backbone with task-specific adaptations
Label: "Foundation Model Paradigm"
Annotations:
- "Knowledge shared across tasks"
- "Pretrain once, adapt many times"
- "Emergent capabilities"

Green checkmarks showing connections. Clean workflow diagram, white background. Professional FM paradigm illustration.
```

**Caption for Panel B:**
"Foundation model paradigm: shared representations, efficient adaptation. A single foundation model pretrained on diverse unlabeled sequences captures general biological knowledge. Small task-specific adapters leverage these shared representations for diverse downstream tasks with minimal labeled data. Knowledge transfers across applications through the common backbone."

### Combined Caption

**Full Figure Caption:**
"The paradigm shift from task-specific to foundation models. (A) The task-specific paradigm trains separate models from scratch for each application. Knowledge about sequence patterns cannot transfer between tasks, requiring substantial labeled data for each new application. (B) The foundation model paradigm pretrains a single large model on diverse unlabeled sequences, capturing general biological knowledge in reusable representations. Small task-specific adapters enable efficient transfer to diverse downstream tasks. This paradigm shift mirrors developments in natural language processing, where pretrained language models revolutionized the efficiency and capability of text-based AI systems."

---

## Figure 13.2: Scaling Laws (Three-Panel)

**Files:**
- `figs/part_3/ch13/02-A-fig-scaling-laws.svg`
- `figs/part_3/ch13/02-B-fig-scaling-laws.svg`
- `figs/part_3/ch13/02-C-fig-scaling-laws.svg`

**Priority:** Essential
**Type:** Log-log scaling plots

### Panel A: Loss vs. Parameters

**Content:** Log-log plot showing pretraining loss decreasing as a power law of model parameters. Points for different model sizes (8M, 35M, 150M, 650M, 3B, 15B) following a clean trend line.

**DALL-E Prompt:**
```
Create a scientific log-log plot showing scaling of loss with parameters. Save as: 02-A-fig-scaling-laws.svg

Plot elements:
- X-axis: "Parameters (log scale)" ranging 10M to 100B
- Y-axis: "Pretraining Loss (log scale)" ranging 1.0 to 4.0
- Data points for model sizes: 8M, 35M, 150M, 650M, 3B, 15B
- Clean power-law trend line through points
- Equation annotation: "L ∝ N^(-α)"
- Title: "Loss vs. Model Size"

Labels for each point with model variant names (e.g., ESM-2 8M, ESM-2 3B)
Clean log-log scientific plot with grid, white background. Professional scaling law figure.
```

**Caption for Panel A:**
"Pretraining loss scales as a power law with model parameters. Each point represents a model trained with identical data and compute per parameter; larger models achieve lower loss following L ∝ N^(-α). This predictable relationship enables extrapolating performance gains from scaling before committing resources."

### Panel B: Downstream Performance vs. Parameters

**Content:** Log-log plot showing downstream task accuracy increasing with model size across multiple tasks (contact prediction, secondary structure, variant effect). Each task shows the same scaling trend.

**DALL-E Prompt:**
```
Create a scientific log-log plot showing downstream task scaling. Save as: 02-B-fig-scaling-laws.svg

Plot elements:
- X-axis: "Parameters (log scale)" ranging 10M to 100B
- Y-axis: "Downstream Accuracy" (linear, 0.5 to 1.0)
- Multiple lines for different tasks:
  - Blue: "Contact Prediction"
  - Orange: "Secondary Structure"
  - Green: "Variant Effect"
- All lines show similar upward scaling trend
- Title: "Downstream Performance vs. Model Size"

Legend showing task colors. Clean scientific plot with grid, white background. Professional multi-task scaling figure.
```

**Caption for Panel B:**
"Downstream task performance scales with model size across diverse tasks. Contact prediction, secondary structure prediction, and variant effect scoring all improve with larger pretrained models, despite these tasks never appearing in pretraining. The consistent scaling across tasks demonstrates that larger models capture more transferable biological knowledge."

### Panel C: Compute-Optimal Scaling

**Content:** Iso-loss contours showing optimal trade-off between model size and training tokens for fixed compute budget. Diagonal ridge shows compute-optimal frontier.

**DALL-E Prompt:**
```
Create a scientific contour plot showing compute-optimal scaling. Save as: 02-C-fig-scaling-laws.svg

Contour plot:
- X-axis: "Training Tokens (log scale)"
- Y-axis: "Model Parameters (log scale)"
- Contour lines showing iso-loss regions (same loss achieved)
- Color gradient: red (high loss) to blue (low loss)
- Diagonal ridge line showing compute-optimal frontier
- Arrow annotation: "Compute-optimal scaling"
- Multiple diagonal lines showing fixed compute budgets
- Title: "Optimal Allocation of Compute"

Annotations explaining that moving along ridge maximizes performance for fixed compute. Clean contour plot, white background. Professional compute-optimal scaling figure.
```

**Caption for Panel C:**
"Compute-optimal scaling balances model size and training data. Iso-loss contours show that the same performance can be achieved with different combinations of parameters and training tokens. The diagonal ridge marks the compute-optimal frontier: for a fixed compute budget, moving along this ridge maximizes performance. The Chinchilla scaling law suggests that model size and training tokens should scale proportionally."

### Combined Caption

**Full Figure Caption:**
"Scaling laws for genomic foundation models. (A) Pretraining loss decreases predictably with model parameters following a power law, enabling informed decisions about resource allocation. (B) Downstream task performance scales consistently across diverse tasks including contact prediction, secondary structure, and variant effects, demonstrating that larger models capture more transferable biological knowledge. (C) Compute-optimal scaling reveals the trade-off between model size and training data: for fixed compute budget, optimal performance requires balancing parameter count with training tokens. These scaling relationships, first established in natural language processing, extend to biological sequence models and guide foundation model development."

---

## Figure 13.3: Model Taxonomy

**File:** `figs/part_3/ch13/03-fig-model-taxonomy.svg`
**Priority:** Essential
**Type:** Taxonomy/classification diagram

### Content Description

Four-quadrant taxonomy organizing genomic foundation models by:
- Modality (DNA, Protein, RNA, Multi-modal)
- Architecture (Encoder, Decoder, Hybrid)

Place key models in their appropriate positions with annotations for key characteristics.

### DALL-E Prompt

```
Create a scientific taxonomy diagram for genomic foundation models. Save as: 03-fig-model-taxonomy.svg

Four-family organization:

QUADRANT 1 "DNA Language Models":
- Models: DNABERT, Nucleotide Transformer, HyenaDNA, Caduceus, Evo
- Key: Long context, single-nucleotide resolution
- Color: Blue (#1f77b4)

QUADRANT 2 "Protein Language Models":
- Models: ESM, ESM-2, ProtTrans, ProGen
- Key: Evolutionary knowledge, structure-aware
- Color: Green (#2ca02c)

QUADRANT 3 "Regulatory Sequence Models":
- Models: Enformer, Borzoi, Basenji
- Key: Multi-task, expression prediction
- Color: Orange (#d62728)

QUADRANT 4 "Multi-Modal / Emerging":
- Models: AlphaFold2, AlphaMissense, RoseTTAFold
- Key: Structure + sequence integration
- Color: Purple (#9467bd)

Center annotation: "Foundation Models for Genomics"
Arrows showing relationships between families
Icons for each model type

Clean taxonomy diagram with four colored regions, white background. Professional model classification figure.
```

### Post-Processing Notes

- Add model names within each quadrant
- Include key characteristics for each family
- Show cross-family connections (e.g., ESM → ESMFold)
- Add legend for architecture types

### Fallback Description

Create in diagramming software:
- 2×2 grid or four-quadrant layout
- Model names as labeled boxes
- Color coding by family
- Connection lines between related models

### Caption

**Recommended Caption:**
"Taxonomy of genomic foundation models organized by modality and approach. DNA language models (blue) process nucleotide sequences with emphasis on long context and single-nucleotide resolution. Protein language models (green) encode evolutionary knowledge from protein sequences with increasing integration of structural information. Regulatory sequence models (orange) combine sequence processing with multi-task prediction of chromatin and expression tracks. Multi-modal and emerging models (purple) integrate across modalities, combining sequence with structure (AlphaFold2) or leveraging multiple information sources simultaneously. Arrows indicate connections between families where models build on each other's capabilities."

---

## Figure 13.4: Design Dimensions

**File:** `figs/part_3/ch13/04-fig-design-dimensions.svg`
**Priority:** High
**Type:** Multi-axis design space

### Content Description

Spider/radar chart or multi-axis comparison showing key design dimensions for foundation models:
- Context length
- Parameter count
- Training compute
- Tokenization strategy
- Architecture type
- Pretraining objective

Position representative models (ESM-2, Enformer, HyenaDNA, Evo) showing their different trade-offs.

### DALL-E Prompt

```
Create a scientific radar chart comparing foundation model design dimensions. Save as: 04-fig-design-dimensions.svg

Radar chart with 6 axes:
1. Context Length (1kb → 1Mb)
2. Parameters (10M → 100B)
3. Training Compute (low → high)
4. Architecture (Encoder → Decoder)
5. Tokenization (K-mer → Single-nucleotide)
6. Objective (MLM → Autoregressive)

Multiple overlaid polygons for different models:
- ESM-2: High params, encoder, medium context
- Enformer: High context, hybrid, multi-task
- HyenaDNA: Highest context, SSM, single-nucleotide
- Evo: High all dimensions, decoder

Legend showing model colors. Each polygon connects model's position on each axis.

Clean radar chart with labeled axes, white background. Professional model comparison figure.
```

### Post-Processing Notes

- Use distinct colors/line styles for each model
- Add legend identifying models
- Annotate key trade-offs
- Include brief description of each axis

### Fallback Description

Create as parallel coordinates plot or multi-bar comparison:
- Multiple axes showing design dimensions
- Lines connecting each model's positions
- Color coding for model identification

### Caption

**Recommended Caption:**
"Design dimensions for genomic foundation models. Radar chart positions representative models across six key dimensions: context length (how much sequence the model processes), parameter count (model capacity), training compute (resources required), architecture type (encoder vs. decoder), tokenization strategy (k-mer vs. single-nucleotide), and pretraining objective (masked vs. autoregressive). Different models make different trade-offs: ESM-2 emphasizes parameter scale within protein-length contexts; Enformer balances long context with multi-task supervision; HyenaDNA pushes context length to megabases using sub-quadratic architectures; Evo combines massive scale with autoregressive generation. These trade-offs determine which applications each model best serves."

---

## Figure 13.5: Build vs. Use Decision

**File:** `figs/part_3/ch13/05-fig-build-vs-use.svg`
**Priority:** High
**Type:** Decision flowchart with cost-benefit

### Content Description

Decision flowchart guiding practitioners through:
1. Use existing model with frozen embeddings (cheapest, fastest)
2. Adapt existing model with LoRA/fine-tuning (moderate cost)
3. Build custom foundation model (expensive, rarely necessary)

Include cost/time annotations and expected performance trade-offs.

### DALL-E Prompt

```
Create a scientific decision flowchart for build vs. use foundation models. Save as: 05-fig-build-vs-use.svg

Flowchart structure:

ENTRY: "New genomic prediction task"

DECISION 1: "Does suitable pretrained model exist?"
- Yes → "Task alignment?"
- No → "BUILD: Custom pretraining"

DECISION 2: "How well does task align with pretraining?"
- High alignment → "USE: Frozen embeddings"
- Moderate → "ADAPT: LoRA/fine-tuning"
- Low → "BUILD: Domain-specific pretraining"

TERMINAL NODES with cost-benefit:

USE (Green):
- Cost: Hours / $10
- Performance: 70-90% of fine-tuned
- Annotation: "Most applications land here"

ADAPT (Yellow):
- Cost: Days / $100-1000
- Performance: 95% of full fine-tuning
- Annotation: "Good balance for most tasks"

BUILD (Red):
- Cost: Months / $100K+
- Performance: Potentially best for domain
- Annotation: "Rare but sometimes necessary"

Color-coded paths and terminals. Clean decision flowchart, white background. Professional practitioner guide.
```

### Post-Processing Notes

- Add clear cost/time annotations at each terminal
- Color-code by recommendation strength (green=preferred, yellow=consider, red=last resort)
- Include decision criteria at each branch
- Add "Most common path" annotation

### Fallback Description

Create in flowchart software:
- Decision tree with diamond decision nodes
- Rectangular terminal nodes with outcomes
- Cost/benefit annotations
- Color coding for recommendation

### Caption

**Recommended Caption:**
"Decision framework for using vs. building foundation models. Entry point: a new genomic prediction task. First decision: does a suitable pretrained model exist? If yes, assess task alignment. For high alignment, USE frozen embeddings (hours of work, ~$10 compute, achieving 70-90% of fine-tuned performance)—this serves most applications. For moderate alignment, ADAPT using LoRA or light fine-tuning (days of work, $100-1000 compute, ~95% of full fine-tuning). Only when existing models fundamentally lack required capabilities should practitioners BUILD custom foundation models (months of work, $100K+ compute). The vast majority of applications are best served by using or adapting existing models rather than building from scratch."

---

## Summary

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| 13.1 Paradigm Shift | 2 | Essential | Medium (comparison) |
| 13.2 Scaling Laws | 3 | Essential | Medium (log-log plots) |
| 13.3 Model Taxonomy | 1 | Essential | Medium (taxonomy) |
| 13.4 Design Dimensions | 1 | High | Medium (radar chart) |
| 13.5 Build vs. Use | 1 | High | Medium (flowchart) |

**Total files:** 8
**Recommended generation order:** 13.1A-B (paradigm shift), 13.5 (decision flowchart), 13.3 (taxonomy), 13.2A-C (scaling laws), 13.4 (design dimensions)

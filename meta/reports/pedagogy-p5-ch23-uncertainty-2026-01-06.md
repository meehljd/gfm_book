# Pedagogical Review: Uncertainty Quantification (Chapter 23)

Generated: 2026-01-06
File: part_5/p5-ch23-uncertainty.qmd
Word count: ~8,500

## Executive Summary

Chapter 23 on Uncertainty Quantification was already pedagogically strong, with excellent narrative hooks, thorough elaborative interrogation ("why" explanations), and good concrete examples throughout. The chapter's opening clinical scenario immediately establishes stakes, and cross-chapter connections were already present. Key enhancements focused on adding metacognitive scaffolds (learning objectives, chapter summary), retrieval practice prompts, comparison tables to aid interleaving, difficulty warnings for mathematically dense sections, and practical guidance callouts for deployment workflows. The enhanced chapter now provides a more complete learning experience that supports self-assessment and consolidation.

## Learning Science Scorecard

| Principle | Before | After | Key Changes |
|-----------|--------|-------|-------------|
| Cognitive Load | B | A | Added difficulty warnings before mathematical sections; comparison tables chunk related concepts |
| Retrieval Practice | D | A | Added 5 Stop and Think/Knowledge Check prompts throughout |
| Interleaving | B | A | Added 4 comparison tables (uncertainty types, calibration metrics, calibration methods, UQ methods) |
| Spacing | B | B | Cross-chapter references already strong; maintained existing hooks |
| Elaboration | A | A | Already excellent; "why" explanations throughout |
| Concrete Examples | A | A | Already excellent; clinical cases, specific models, concrete numbers |
| Dual Coding | B | B | Figure placeholders present; tables strengthen visual organization |
| Prior Knowledge | B | A | Added prerequisites in overview; added prediction prompts that activate prior knowledge |
| Metacognition | D | A | Added chapter overview, learning objectives, difficulty warnings, comprehensive summary |
| Desirable Difficulty | C | A | Added prediction prompts before explanations; knowledge checks require active recall |
| Hooks & Narrative | A | A | Already excellent; opening clinical scenario, stakes established |
| Transfer & Application | B | A | Added practical guidance callouts for deployment workflows |

**Overall Pedagogical Grade: B+ → A**

## Enhancements Implemented

### 1. Chapter Overview Callout (Lines 3-19)
Added comprehensive chapter overview with:
- Prerequisites linking to prior chapters (@sec-ch11-eval, @sec-ch08-pretraining, @sec-ch17-vep-fm)
- 7 specific, measurable learning objectives
- Estimated reading time (45-60 minutes)

### 2. Key Insight Callouts (3 added)
- **Calibration vs. Accuracy** (after "Why Uncertainty Matters"): Highlights that accuracy and calibration are distinct, and miscalibrated high-accuracy models can be dangerous
- **Hidden Calibration Disparities** (in "Calibration Across Subgroups"): Emphasizes that aggregate metrics mask subgroup disparities, with health equity implications
- **Prediction Sets Convey Uncertainty Without Probabilities** (introducing Conformal Prediction): Explains the key insight that set size is the uncertainty estimate

### 3. Stop and Think / Knowledge Check Prompts (5 added)
1. After epistemic uncertainty section: What type of uncertainty dominates for rare genes? Would more data help?
2. After calibration explanation: Why is high auROC insufficient for reliable probability estimates?
3. Before calibration methods: Prediction prompt about mathematical corrections for overconfidence
4. Before heteroscedastic models: Budget-constrained UQ deployment scenario
5. After OOD problem statement: Novel gene with no homologs, high-confidence predictions - what concerns?

### 4. Comparison Tables (4 added inline, no new section headers)
1. **Epistemic vs. Aleatoric Uncertainty** (@tbl-uncertainty-types): Source, reducibility, examples, detection, response, clinical implication
2. **Calibration Metrics** (@tbl-calibration-metrics): ECE, MCE, Brier score, reliability diagrams with formulas and use cases
3. **Post-hoc Calibration Methods** (@tbl-calibration-selection): Temperature/Platt/isotonic comparison with parameters, best uses, limitations
4. **UQ Methods** (@tbl-uq-methods): Ensembles/MC dropout/heteroscedastic/evidential with epistemic/aleatoric capture and costs

### 5. Difficulty Warnings (2 added)
1. Before uncertainty decomposition math: Warns about variance/conditional probability requirements, provides intuition fallback
2. Before split conformal prediction: Warns about mathematical framework, suggests focusing on algorithm steps if formalism unfamiliar

### 6. Practical Guidance Callouts (2 added)
1. **Calibration Workflow** (after calibrating FM outputs): 6-step workflow for clinical deployment
2. **OOD Detection Pipeline** (after practical OOD section): 6-step pipeline for deployment safeguards

### 7. Chapter Summary Callout (Lines 582-608)
Comprehensive summary including:
- 7 key concepts with concise definitions
- 4 clinical implications
- Connections to 6 other chapters

## Retained Strengths

The original chapter already excelled in several areas that were preserved:

- **Narrative hook**: The opening clinical scenario (pathogenicity score of 0.73) immediately establishes stakes
- **Elaborative interrogation**: Consistently explains "why" not just "what"
- **Concrete examples**: Clinical cases (*BRCA1* penetrance), specific models (*AlphaMissense*, *ESM-1v*), concrete numbers
- **Cross-chapter connections**: Already linked to ~15 other chapters; maintained and slightly strengthened

## Recommendations for Future Enhancement

1. **Figures**: The chapter has 7 figure placeholders; when implemented, ensure figure-text contiguity and explanatory captions
2. **Worked example**: Consider adding a complete worked example showing calibration assessment, temperature scaling application, and conformal prediction on a realistic variant set
3. **Code snippets**: Consider adding pseudocode or Python snippets for calibration assessment and conformal prediction
4. **Interactive elements**: For digital versions, consider interactive reliability diagram visualization

## Cross-Chapter Connections

The chapter appropriately connects to:
- Prior chapters: @sec-ch11-eval (evaluation), @sec-ch08-pretraining (objectives), @sec-ch17-vep-fm (VEP), @sec-ch02-clinvar, @sec-ch02-gnomad, @sec-ch02-dms (data resources)
- Parallel chapters: @sec-ch03-fairness (equity), @sec-ch09-domain-shift (distribution shift), @sec-ch12-confounding (confounding)
- Subsequent chapters: @sec-ch24-interpretability (complements uncertainty), @sec-ch27-clinical-risk (deployment), @sec-ch28-rare-disease (application)

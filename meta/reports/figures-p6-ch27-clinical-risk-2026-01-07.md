# Figure Report: Chapter 27 - Clinical Risk Prediction

**Chapter:** p6-ch27-clinical-risk.qmd
**Date:** 2026-01-07
**Total Figures:** 7 (14 files)
**Format:** SVG (for scalability)

---

## Figure 1: Feature Integration Layers

### Files
- `figs/part_6/ch27/01-A-fig-feature-integration.svg`
- `figs/part_6/ch27/01-B-fig-feature-integration.svg`
- `figs/part_6/ch27/01-C-fig-feature-integration.svg`

### Priority
**Essential** - Core architecture concept

### Content Description
Three-panel figure showing how different foundation model features integrate for clinical risk: genomic features, expression features, and coding variant features.

### DALL-E Prompt
```
Scientific illustration of feature integration for clinical risk prediction. Three panels.

PANEL A (Genomic Features - DNA FMs):
Flow diagram. Input: Patient genome sequence. Through Enformer/Sei-style model. Outputs: Regulatory effect scores, chromatin predictions, enhancer activity. Specific features extracted: PRS enhancement, regulatory variant effects, non-coding risk. Arrow to integration layer.

PANEL B (Expression Features - scRNA FMs):
Flow diagram. Input: Patient expression profile (blood/tissue). Through Geneformer/scGPT-style model. Outputs: Cell state embeddings, pathway activities, expression signatures. Features: Current disease state, response biomarkers, cell type composition. Arrow to integration layer.

PANEL C (Coding Variant Features - Protein FMs):
Flow diagram. Input: Patient missense variants. Through ESM/AlphaMissense-style model. Outputs: Pathogenicity scores, structural effects, functional impact. Features: Monogenic risk, carrier status, modifier effects. Arrow to integration layer.

BOTTOM: Integration layer combining all three into unified risk score with confidence interval.

Professional scientific style, neural network diagram elements, patient-centric visualization, white background.

Save as: 01-A-fig-feature-integration.svg through 01-C-fig-feature-integration.svg
```

### Post-Processing Notes
- Add specific model names
- Include feature dimensionalities
- Show integration architecture

### Fallback Description
"Feature integration for clinical risk: DNA foundation models provide regulatory and non-coding variant effects, expression models provide current state and pathway activities, protein models provide coding variant pathogenicity. Integration combines all layers into unified risk prediction with uncertainty."

### Caption Recommendation
"Feature integration for clinical risk prediction. (A) DNA foundation models contribute regulatory variant effects, enhancer predictions, and PRS enhancement. (B) Expression foundation models provide cell state embeddings, pathway activities, and disease signatures. (C) Protein foundation models add coding variant pathogenicity and structural effects. Integration combines features across modalities for unified risk prediction with calibrated uncertainty."

---

## Figure 2: Temporal Modeling

### Files
- `figs/part_6/ch27/02-A-fig-temporal-modeling.svg`
- `figs/part_6/ch27/02-B-fig-temporal-modeling.svg`
- `figs/part_6/ch27/02-C-fig-temporal-modeling.svg`

### Priority
**High** - Important for longitudinal prediction

### Content Description
Three-panel figure on temporal dynamics: static vs dynamic risk, longitudinal trajectory modeling, and updating predictions over time.

### DALL-E Prompt
```
Scientific illustration of temporal modeling for clinical risk. Three panels.

PANEL A (Static vs Dynamic Risk):
Two timelines side by side. Left (Static): Single risk score from birth, horizontal line, genetic risk only. Right (Dynamic): Risk trajectory that changes over time, incorporating biomarkers, interventions, lifestyle. Annotation "Genetics sets trajectory; environment and intervention modify it."

PANEL B (Longitudinal Trajectory):
Patient timeline with multiple measurements. Markers: genomic baseline (time 0), lab values (periodic), imaging (annual), symptoms (event-driven). Model updating risk at each timepoint. Confidence intervals widening into future. Recurrent/transformer architecture icon processing sequence.

PANEL C (Prediction Updating):
Example: cardiac risk patient. Initial PRS-based risk (moderate). +Lab abnormality → risk increases. +Medication started → risk decreases. +New symptom → risk increases. Shows Bayesian updating process with posterior narrowing as evidence accumulates.

Professional clinical style, timeline visualizations, patient journey representation, white background.

Save as: 02-A-fig-temporal-modeling.svg through 02-C-fig-temporal-modeling.svg
```

### Post-Processing Notes
- Add specific clinical measurements
- Include confidence intervals
- Show intervention effects

### Fallback Description
"Temporal modeling for clinical risk: static genetic risk versus dynamic risk that incorporates longitudinal measurements, trajectory modeling with sequential observations and widening uncertainty into future, and Bayesian updating as new evidence accumulates."

### Caption Recommendation
"Temporal dynamics in clinical risk prediction. (A) Static versus dynamic risk: genetic risk sets baseline trajectory while environmental factors and interventions modify it over time. (B) Longitudinal trajectory modeling: sequential observations (labs, imaging, symptoms) update risk predictions with widening uncertainty into the future. (C) Prediction updating: Bayesian framework incorporates new evidence, adjusting risk as interventions and events occur."

---

## Figure 3: Validation Hierarchy

### Files
- `figs/part_6/ch27/03-fig-validation-hierarchy.svg`

### Priority
**Essential** - Validation framework

### Content Description
Pyramid showing validation levels from internal holdout through prospective interventional trials.

### DALL-E Prompt
```
Scientific illustration of clinical validation hierarchy as pyramid. Single panel.

PYRAMID (bottom to top, widest to narrowest):

LEVEL 1 (BOTTOM - Internal Holdout):
- "Train/test split from same dataset"
- Easiest, most common
- Risk: Overestimates real-world performance
- Color: Light gray

LEVEL 2 (External Retrospective):
- "Held-out institution or time period"
- Tests generalization
- Risk: Distribution shift undetected
- Color: Light blue

LEVEL 3 (Prospective Observational):
- "Silent deployment alongside clinical care"
- Real-time performance monitoring
- Detects drift
- Color: Medium blue

LEVEL 4 (Prospective Interventional):
- "Randomized trial of model-guided care"
- Definitive but expensive
- Measures clinical utility
- Color: Dark blue

LEVEL 5 (TOP - Long-term Outcomes):
- "Multi-year follow-up"
- Ultimate validation
- Rarely achieved
- Color: Darkest blue

SIDE ANNOTATIONS:
- Arrow showing "Evidence strength increases"
- Arrow showing "Cost/time increases"
- Specific metrics at each level (AUC, calibration, NRI, clinical endpoints)

Foundation model contribution noted at each level.

Professional scientific style, pyramid diagram, blue gradient, white background.

Save as: 03-fig-validation-hierarchy.svg
```

### Post-Processing Notes
- Add specific metrics
- Include timeline estimates
- Show regulatory implications

### Fallback Description
"Validation hierarchy from internal holdout (easiest, overestimates performance) through external retrospective (tests generalization), prospective observational (real-time monitoring), prospective interventional (randomized trials), to long-term outcomes (ultimate validation). Evidence strength and cost/time increase together."

### Caption Recommendation
"Clinical validation hierarchy. From bottom: internal holdout validation is easiest but overestimates deployment performance; external retrospective validation tests generalization across institutions; prospective observational validation monitors real-time performance without influencing care; prospective interventional trials demonstrate clinical utility through randomized comparisons; long-term outcome tracking provides ultimate validation but is rarely achieved. Each level requires greater investment but provides stronger evidence."

---

## Figure 4: Clinical Uncertainty Communication

### Files
- `figs/part_6/ch27/04-fig-clinical-uncertainty.svg`

### Priority
**High** - Critical for clinical use

### Content Description
How to communicate uncertainty to clinicians and patients: point estimates vs intervals, visual formats, and decision support.

### DALL-E Prompt
```
Scientific illustration of clinical uncertainty communication. Single panel with multiple elements.

TOP SECTION (Bad vs Good Communication):
Left (BAD): "Your risk is 23%" - single number, no context
Right (GOOD): "Your risk is 18-28% (most likely 23%)" - interval with best estimate

MIDDLE SECTION (Visual Formats):
Three visualization options:
1) Icon array: 100 person icons, 23 highlighted
2) Risk thermometer: Vertical scale with marker and CI band
3) Risk comparison: "Similar to..." contextual comparisons
For each: annotation of effectiveness and when to use

BOTTOM SECTION (Decision Support Integration):
Clinical decision interface mockup showing:
- Risk estimate with confidence interval
- Uncertainty flag if OOD or miscalibrated
- Threshold-based recommendations (green/yellow/red zones)
- "What would change the prediction?" sensitivity analysis

CALLOUT BOX: "Key insight: Communicating uncertainty is as important as the prediction itself. Overconfident predictions without uncertainty → clinical harm."

Professional clinical/medical style, user interface elements, white background.

Save as: 04-fig-clinical-uncertainty.svg
```

### Post-Processing Notes
- Add specific clinical examples
- Include user testing data
- Show different audience formats

### Fallback Description
"Clinical uncertainty communication: bad practice (single point estimate) versus good practice (interval with best estimate), visual formats (icon arrays, thermometers, comparisons), and decision support integration showing risk with confidence interval, uncertainty flags, and threshold-based recommendations."

### Caption Recommendation
"Communicating uncertainty in clinical risk prediction. Single point estimates without context can mislead; intervals with best estimates provide actionable uncertainty. Visual formats include icon arrays (intuitive for patients), risk thermometers (familiar to clinicians), and contextual comparisons. Decision support should integrate uncertainty directly: flagging predictions with high epistemic uncertainty, showing confidence bands around thresholds, and providing sensitivity analysis."

---

## Figure 5: Fairness Assessment

### Files
- `figs/part_6/ch27/05-A-fig-fairness-assessment.svg`
- `figs/part_6/ch27/05-B-fig-fairness-assessment.svg`
- `figs/part_6/ch27/05-C-fig-fairness-assessment.svg`
- `figs/part_6/ch27/05-D-fig-fairness-assessment.svg`

### Priority
**High** - Equity and bias

### Content Description
Four-panel figure on fairness: ancestry-stratified performance, calibration by group, sources of bias, and mitigation strategies.

### DALL-E Prompt
```
Scientific illustration of fairness assessment for clinical genomic AI. Four panels.

PANEL A (Ancestry-Stratified Performance):
Bar chart showing model AUC by ancestry group. European: 0.85. East Asian: 0.82. South Asian: 0.79. African: 0.72. Hispanic/Latino: 0.75. Aggregate (misleading): 0.83. Annotation "Aggregate metrics mask disparities."

PANEL B (Calibration by Group):
Four reliability diagrams (small) for different ancestry groups. European: well-calibrated (on diagonal). African: overconfident for some ranges. Visual showing calibration varies across groups.

PANEL C (Sources of Bias):
Flow diagram showing bias accumulation. Training data (European-dominated GWAS) → Model (learns European-specific patterns) → Features (EHR, lab norms, coding practices) → Deployment (different populations). Each stage adds bias. Annotation "Bias accumulates through pipeline."

PANEL D (Mitigation Strategies):
Four strategies with icons:
1) Stratified evaluation (required disclosure)
2) Reweighting/resampling during training
3) Calibration adjustment by group
4) Uncertainty flagging for underrepresented groups
For each: effectiveness and limitations noted.

Professional scientific style, disaggregated visualizations, white background.

Save as: 05-A-fig-fairness-assessment.svg through 05-D-fig-fairness-assessment.svg
```

### Post-Processing Notes
- Use realistic performance gaps
- Add statistical confidence intervals
- Include policy recommendations

### Fallback Description
"Fairness assessment: ancestry-stratified performance shows disparities masked by aggregate metrics, calibration varies across groups with overconfidence for underrepresented populations, bias accumulates from training data through deployment, and mitigation strategies include stratified evaluation, reweighting, calibration adjustment, and uncertainty flagging."

### Caption Recommendation
"Fairness assessment in clinical genomic AI. (A) Ancestry-stratified performance reveals disparities masked by aggregate metrics—African ancestry AUC significantly lower than European. (B) Calibration varies by group: models may be overconfident for underrepresented populations. (C) Bias accumulates: European-dominated training data leads to models that underperform on other populations, compounded by EHR biases. (D) Mitigation strategies: stratified evaluation disclosure, training reweighting, group-specific calibration, and uncertainty flagging for underrepresented inputs."

---

## Figure 6: Clinical Workflow Integration

### Files
- `figs/part_6/ch27/06-fig-clinical-workflow.svg`

### Priority
**High** - Deployment reality

### Content Description
How foundation model predictions integrate into clinical workflows: timing, display, action triggers.

### DALL-E Prompt
```
Scientific illustration of clinical workflow integration for genomic risk prediction. Single panel with workflow diagram.

WORKFLOW STAGES (left to right):

STAGE 1 (Data Collection):
- EHR icon
- Genomic test ordered
- Samples collected
Timeline: Days 1-3

STAGE 2 (Processing):
- Lab processing icon
- Bioinformatics pipeline
- FM inference runs
Timeline: Days 3-10

STAGE 3 (Result Generation):
- Risk score computed
- Uncertainty quantified
- Clinical report generated
Timeline: Day 10

STAGE 4 (Clinical Review):
- Results appear in EHR
- Clinician reviews with context
- Alert if high-risk (BPA)
Decision point: Act or wait?

STAGE 5 (Action):
Branch based on risk:
- High risk → Specialist referral, intervention
- Moderate → Increased surveillance
- Low → Routine care
- Uncertain → Additional testing

INTEGRATION POINTS highlighted:
- Where FM contributes
- Human oversight checkpoints
- Patient communication moments

BOTTOM: Barriers to adoption (compute access, reimbursement, liability, clinician trust)

Professional clinical workflow style, healthcare iconography, white background.

Save as: 06-fig-clinical-workflow.svg
```

### Post-Processing Notes
- Add specific EHR integration examples
- Include timing estimates
- Show regulatory touchpoints

### Fallback Description
"Clinical workflow integration: data collection (EHR, samples), processing (sequencing, FM inference), result generation (risk with uncertainty), clinical review (EHR display, alerts), and action (tiered based on risk level). Integration points highlight FM contribution, human oversight, and adoption barriers."

### Caption Recommendation
"Clinical workflow integration for genomic risk prediction. From data collection through processing, result generation, clinical review, and action. Foundation models contribute during processing and result generation. Human oversight checkpoints ensure clinician review before action. Adoption barriers include compute infrastructure, reimbursement, liability concerns, and clinician trust. Effective integration requires attention to timing, display, and action triggers at each stage."

---

## Figure 7: Cardiovascular Case Study

### Files
- `figs/part_6/ch27/07-fig-cardio-case-study.svg`

### Priority
**Enhancing** - Concrete example

### Content Description
End-to-end case study of FM-enhanced cardiovascular risk prediction showing integration of PRS, expression, and clinical data.

### DALL-E Prompt
```
Scientific illustration of cardiovascular risk prediction case study. Single panel with patient journey.

PATIENT CASE: 45-year-old male, family history of early MI

DATA INPUTS (left side):
- Genetic: PRS for CAD (raw + FM-enhanced)
- Coding: LDLR variant (AlphaMissense score)
- Expression: Inflammatory signature from blood
- Clinical: Lipids, BP, smoking status, BMI

MODEL INTEGRATION (center):
- Multi-input fusion architecture
- Temporal model incorporating 5 years of data
- Foundation model features from each modality
- Integration producing unified risk

OUTPUT (right side):
- 10-year risk: 28% (CI: 22-35%)
- Compared to Framingham alone: 18%
- Compared to PRS alone: 24%
- FM-integrated adds: +10% AUC over baseline

CLINICAL ACTION:
- Risk category: High
- Recommendation: Statin therapy, lifestyle intervention
- Follow-up: Annual monitoring
- Uncertainty note: FM predictions validated in European populations; patient of South Asian ancestry warrants caution

TIMELINE at bottom showing prediction evolution over 5 years.

Professional clinical case study style, patient-centric visualization, white background.

Save as: 07-fig-cardio-case-study.svg
```

### Post-Processing Notes
- Add realistic risk values
- Include comparison metrics
- Show ancestry considerations

### Fallback Description
"Cardiovascular case study: patient with genetic PRS, coding variant, expression signature, and clinical data. Model integration produces 28% 10-year risk (higher than Framingham or PRS alone), leading to high-risk classification and statin recommendation. Note on ancestry-specific validation limitations."

### Caption Recommendation
"Case study: FM-enhanced cardiovascular risk prediction. A 45-year-old male with family history integrates genetic PRS (enhanced by regulatory variant effects), LDLR coding variant (scored by AlphaMissense), inflammatory expression signature, and clinical features. FM-integrated prediction (28% 10-year risk) exceeds both traditional Framingham (18%) and PRS-only (24%) approaches. Clinical action: statin therapy with annual monitoring. Caveat: model validated primarily in European populations; additional caution warranted for other ancestries."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Feature Integration | 3 | Essential | High |
| Temporal Modeling | 3 | High | Medium |
| Validation Hierarchy | 1 | Essential | Low |
| Clinical Uncertainty | 1 | High | Medium |
| Fairness Assessment | 4 | High | Medium |
| Clinical Workflow | 1 | High | Medium |
| Cardio Case Study | 1 | Enhancing | Medium |

## Recommended Generation Order
1. Validation Hierarchy (framework)
2. Feature Integration (architecture)
3. Fairness Assessment (equity)
4. Clinical Uncertainty (communication)
5. Temporal Modeling (dynamics)
6. Clinical Workflow (deployment)
7. Cardio Case Study (concrete example)

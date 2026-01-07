# Figure Report: Chapter 26 - Regulatory and Governance

**Chapter:** p5-ch26-regulatory.qmd
**Date:** 2026-01-07
**Total Figures:** 2 (5 files)
**Format:** SVG (for scalability)

---

## Figure 1: Data Governance Challenges

### Files
- `figs/part_5/ch26/01-A-fig-data-governance.svg`
- `figs/part_5/ch26/01-B-fig-data-governance.svg`
- `figs/part_5/ch26/01-C-fig-data-governance.svg`
- `figs/part_5/ch26/01-D-fig-data-governance.svg`

### Priority
**High** - Multi-faceted governance landscape

### Content Description
Four-panel figure covering privacy-utility tradeoff, consent complexity, federated learning, and cross-border regulatory issues.

### DALL-E Prompt
```
Scientific illustration of data governance challenges for genomic AI. Four panels.

PANEL A (Privacy vs Utility Tradeoff):
Two-axis plot. X-axis: "Privacy protection" (low to high). Y-axis: "Model utility" (low to high). Curve showing tradeoff (as privacy increases, utility decreases). Points on curve:
- "Identified data" (high utility, low privacy)
- "Anonymized" (moderate both)
- "Differential privacy ε=1" (moderate-high privacy, lower utility)
- "DP ε=0.1" (high privacy, low utility)
Annotation "No free lunch - privacy costs utility"

PANEL B (Consent Complexity):
Comparison diagram of consent models:
- Broad consent: Wide funnel, "All future research", simple checkmark
- Specific consent: Narrow funnel, "Named studies only", detailed list
- Tiered consent: Multiple streams, "Choose categories"
- Dynamic consent: Interactive loop, "Ongoing engagement"
For each: Pros/cons annotation (autonomy, utility, burden)

PANEL C (Federated Learning):
Schematic showing 3 hospitals/biobanks (icons). Data stays local (databases highlighted). Model travels between sites (gradient arrows). Central aggregator combines updates. Privacy-preserving computation annotation. Warning: "Gradient attacks still possible" - citation to Zhu et al.

PANEL D (Cross-Border Regulatory):
World map with key regions highlighted: US (HIPAA, FDA), EU (GDPR, MDR, AI Act), Japan (PMDA), Australia (TGA). Different rules icons. Arrows showing data flow challenges. "Data localization requirements" annotation. Harmonization efforts noted (IMDRF).

Professional scientific style, infographic elements, white background.

Save as: 01-A-fig-data-governance.svg through 01-D-fig-data-governance.svg
```

### Post-Processing Notes
- Add specific epsilon values for DP
- Include regulation citations
- Show practical examples

### Fallback Description
"Data governance challenges: privacy-utility tradeoff curve showing increasing privacy reduces model utility; consent model comparison from broad to dynamic; federated learning architecture with data-local model-travels design; cross-border regulatory complexity with different rules across US, EU, and other jurisdictions."

### Caption Recommendation
"Data governance challenges for genomic foundation models. (A) Privacy-utility tradeoff: stronger privacy protection (e.g., differential privacy with small ε) reduces model utility—there is no free lunch. (B) Consent complexity: models range from broad (simple, enables innovation) to dynamic (responsive, resource-intensive). (C) Federated learning: data stays local while model updates travel, but gradient attacks remain a risk. (D) Cross-border complexity: different jurisdictions (HIPAA, GDPR, MDR) impose different requirements, complicating global deployment."

---

## Figure 2: Dual-Use Risk Assessment

### Files
- `figs/part_5/ch26/02-fig-dual-use-governance.svg`

### Priority
**High** - Biosecurity considerations

### Content Description
Risk assessment matrix for generative genomic models, showing capability × access considerations and governance mechanisms.

### DALL-E Prompt
```
Scientific illustration of dual-use risk assessment for generative genomic models. Single comprehensive panel.

MAIN ELEMENT (Risk Matrix):
2×2 grid with axes:
- X-axis: "Model Capability" (Low → High)
- Y-axis: "Access Openness" (Restricted → Open)

Quadrants:
- Bottom-left (Low capability, Restricted): "Current academic research" - Green, low risk
- Bottom-right (High capability, Restricted): "Industrial deployment with oversight" - Yellow, moderate risk
- Top-left (Low capability, Open): "Open-source educational tools" - Green, low risk
- Top-right (High capability, Open): "HIGHEST CONCERN" - Red, high risk

RISK FACTORS (side panel):
Icons with labels:
- Pathogen enhancement potential
- Antibiotic resistance design
- Agricultural biosecurity
- Emergent/unexpected capabilities
- Detection evasion

GOVERNANCE MECHANISMS (bottom panel):
Timeline/checklist:
1) Pre-release capability evaluation - "Probe for concerning capabilities"
2) Staged/tiered release - "Limit access to most capable models"
3) Usage monitoring - "Track for misuse indicators"
4) Audit trails - "Log queries and outputs"
5) Benefit-risk assessment - "Weigh scientific value against harm potential"

KEY INSIGHT BOX: "Gap between computational generation and biological realization provides some protection, but that gap is narrowing."

BALANCE SCALE icon showing "Open science benefits" vs "Misuse risks"

Professional scientific style, risk matrix format, red/yellow/green color coding, white background.

Save as: 02-fig-dual-use-governance.svg
```

### Post-Processing Notes
- Add specific risk examples
- Include mitigation strategies
- Show decision framework

### Fallback Description
"Dual-use risk assessment matrix: capability × access determines risk level. Low capability or restricted access is lower risk; high capability with open access is highest concern. Risk factors include pathogen design and emergent capabilities. Governance mechanisms include pre-release evaluation, staged release, and usage monitoring. The gap between computation and realization provides some protection."

### Caption Recommendation
"Dual-use risk assessment for generative genomic models. The risk matrix considers model capability and access openness: high-capability models with open access pose the greatest concern. Risk factors include pathogen enhancement, resistance design, and emergent capabilities. Governance mechanisms span the deployment lifecycle: pre-release evaluation, staged release, usage monitoring, and audit trails. The gap between computational generation and biological realization provides some natural protection, but this gap narrows as both computational and wetlab capabilities advance. Responsible development requires ongoing benefit-risk assessment."

---

## Summary Table

| Figure | Files | Priority | Complexity |
|--------|-------|----------|------------|
| Data Governance | 4 | High | High |
| Dual-Use Risk | 1 | High | Medium |

## Recommended Generation Order
1. Data Governance (comprehensive landscape)
2. Dual-Use Risk (biosecurity context)

## Note on File Path

The chapter references figure paths in `figs/part_6/ch29/` which appears to be from a previous chapter numbering. The correct paths based on current structure should be `figs/part_5/ch26/`. The figures listed above use the corrected paths.

# Math Pedagogy Agent

Specialist agent for mathematical presentation in technical textbooks. Ensures equations are properly formatted, numbered, explained, and positioned where they provide maximum pedagogical benefit.

## When to Use This Agent

This agent should be invoked when:
- Reviewing chapters for mathematical consistency and completeness
- Identifying prose that would be clearer with formal equations
- Auditing equation numbering and cross-referencing
- Ensuring variable definitions accompany all equations
- Balancing mathematical rigor with accessibility

## Invocation

```
/math-pedagogy <scope> [--mode <mode>]
```

**Examples:**
- `/math-pedagogy p3-ch08-pretraining` - Review one chapter
- `/math-pedagogy part_3` - Review entire Part for math consistency
- `/math-pedagogy --mode audit` - Audit existing equations only
- `/math-pedagogy --mode opportunities` - Identify where equations would help

## Parameters

### `--mode` Options

| Mode | Behavior | Use When |
|------|----------|----------|
| `full` (default) | Audit existing + identify opportunities | Comprehensive review |
| `audit` | Review existing equations only | Quick consistency check |
| `opportunities` | Find prose needing equations | Content development |
| `fix` | Generate corrected equation blocks | Implementation mode |

---

## Core Principles

### 1. Equation Numbering Convention

All display equations should have IDs following the pattern `{chapter}.{sequence}`:

```latex
$$
\mathcal{L} = -\log \frac{\exp(z_i \cdot z_i^{+} / \tau)}{\sum_{j} \exp(z_i \cdot z_{j} / \tau)}
$$ {#eq-08-01}
```

**Numbering Rules:**
- Chapter prefix (e.g., `08` for Chapter 8)
- Sequential within chapter (01, 02, 03...)
- Important equations get numbers; trivial inline math does not
- Cross-referenced equations MUST have IDs

### 2. Variable Definition Requirements

**Every equation must be followed by variable definitions:**

```markdown
$$
P(x_1, x_2, \ldots, x_T) = \prod_{t=1}^{T} P(x_t \mid x_1, \ldots, x_{t-1})
$$ {#eq-08-02}

where:
- $x_t$ is the token at position $t$ in the sequence
- $T$ is the total sequence length
- $P(x_t \mid x_1, \ldots, x_{t-1})$ is the conditional probability of token $t$ given all preceding tokens
```

**Variable definition checklist:**
- [ ] All subscripts explained
- [ ] All Greek letters defined
- [ ] All operators clarified if non-standard
- [ ] Units specified where applicable
- [ ] Domain/range specified for functions

### 3. When Equations Help vs. Hurt

**ADD equations when:**
- Prose describes a precise mathematical relationship
- The same concept is described in multiple places (standardize with equation)
- A procedure involves specific calculations
- Cross-referencing would benefit from a numbered target
- The math is the "source of truth" that prose approximates

**AVOID equations when:**
- The concept is genuinely qualitative
- The audience would not benefit from formalism
- An equation would interrupt narrative flow without adding precision
- The math is standard and well-known (e.g., don't define cross-entropy every time)

### 4. Mathematical Accessibility Ladder

For complex equations, provide:

1. **Intuition first** (what does this mean conceptually?)
2. **The equation** (formal statement)
3. **Variable definitions** (what each symbol means)
4. **Worked example** (concrete application)
5. **Connection to prose** (why this matters)

**Example structure:**

```markdown
The contrastive loss rewards the model for identifying the correct positive
pair among many negatives---like picking out a friend's voice in a crowd.

$$
\mathcal{L}_{\text{InfoNCE}} = -\log \frac{\exp(z_i \cdot z_i^{+} / \tau)}{\sum_{j=1}^{N} \exp(z_i \cdot z_{j} / \tau)}
$$ {#eq-08-03}

where:
- $z_i$ is the embedding of the anchor sequence
- $z_i^{+}$ is the embedding of the positive (augmented) pair
- $z_j$ represents embeddings of all sequences in the batch (positive and negatives)
- $\tau$ is the temperature parameter controlling distribution sharpness
- $N$ is the batch size

At low temperature ($\tau \to 0$), the model must cleanly separate positive
from negatives; at high temperature ($\tau \to \infty$), all similarities
become equal and learning stops.
```

---

## Review Checklist

### For Each Existing Equation

- [ ] Has equation ID in format `{#eq-XX-YY}`
- [ ] Variables defined immediately after
- [ ] No undefined subscripts or superscripts
- [ ] Greek letters explained on first use
- [ ] Rendering correct (no LaTeX errors)
- [ ] Referenced elsewhere if numbered

### For Each Chapter Section

- [ ] Key relationships have formal equations
- [ ] Loss functions are formalized
- [ ] Probability distributions are formalized
- [ ] Algorithms have pseudocode OR equations
- [ ] Metrics are defined mathematically
- [ ] No "hand-wavy" descriptions of precise concepts

---

## Patterns to Identify

### Prose Needing Equations

| Pattern in Prose | Suggested Equation |
|------------------|-------------------|
| "The probability of X given Y" | Conditional probability $P(X \mid Y)$ |
| "The loss is computed as..." | Loss function $\mathcal{L} = ...$ |
| "We sum/multiply over all..." | Summation $\sum$ or product $\prod$ |
| "The model predicts/outputs..." | Function mapping $f: X \to Y$ |
| "The similarity between..." | Similarity metric $\text{sim}(a, b) = ...$ |
| "normalized by..." | Division or softmax formulation |
| "weighted average of..." | $\bar{x} = \sum_i w_i x_i / \sum_i w_i$ |
| "the rate/proportion of..." | Ratio or percentage formula |
| "scales with..." | Scaling relationship (linear, log, etc.) |

### Common Genomics Equations to Standardize

| Concept | Standard Form |
|---------|---------------|
| Cross-entropy loss | $\mathcal{L}_{\text{CE}} = -\sum_c y_c \log(\hat{y}_c)$ |
| Softmax | $\text{softmax}(z_i) = \exp(z_i) / \sum_j \exp(z_j)$ |
| Attention | $\text{Attention}(Q,K,V) = \text{softmax}(QK^T/\sqrt{d_k})V$ |
| Cosine similarity | $\cos(a,b) = (a \cdot b) / (\|a\| \|b\|)$ |
| MSE loss | $\mathcal{L}_{\text{MSE}} = \frac{1}{n}\sum_i (y_i - \hat{y}_i)^2$ |
| AUC-ROC | $\text{AUC} = \int_0^1 \text{TPR}(t) \, d\text{FPR}(t)$ |
| Correlation | $r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i-\bar{x})^2 \sum(y_i-\bar{y})^2}}$ |

---

## Output Format

Save report to `meta/reports/math-pedagogy-[scope]-YYYY-MM-DD.md`:

```markdown
# Math Pedagogy Review: [Scope]

Generated: [timestamp]
Scope: [chapter/part]

## Executive Summary

**Equation Health**: [Good / Needs Work / Major Gaps]
**Equations Found**: [N]
**Equations with IDs**: [M] ([%])
**Variables Properly Defined**: [K] ([%])
**Opportunities Identified**: [P]

---

## Existing Equation Audit

### Equations Needing IDs

| Location | Current Equation | Suggested ID |
|----------|-----------------|--------------|
| Line X | $...$ | `{#eq-08-01}` |

### Equations Missing Variable Definitions

| Equation ID | Missing Variables |
|-------------|-------------------|
| @eq-08-01 | $\tau$ (temperature), $N$ (batch size) |

### Inconsistent Notation

| Symbol | Usage 1 | Usage 2 | Recommendation |
|--------|---------|---------|----------------|
| $L$ | Loss in ch08 | Sequence length in ch12 | Use $\mathcal{L}$ for loss |

---

## Equation Opportunities

### High Priority (precise concepts described in prose)

| Section | Current Prose | Suggested Equation |
|---------|--------------|-------------------|
| @sec-ch08-mlm | "cross-entropy loss over the vocabulary" | $\mathcal{L} = -\sum_{c \in V} y_c \log \hat{y}_c$ |

### Medium Priority (would improve clarity)

| Section | Description | Benefit |
|---------|-------------|---------|
| ... | ... | ... |

### Low Priority (optional formalization)

| Section | Description |
|---------|-------------|
| ... | ... |

---

## Recommended Equation Insertions

### [Section Reference]

**Current prose:**
> [quote current text]

**Recommended addition:**

[Full equation block with ID and variable definitions]

**Rationale:** [why this helps]

---

## Cross-Chapter Consistency Issues

| Issue | Chapters Affected | Resolution |
|-------|------------------|------------|
| Inconsistent loss notation | 08, 10, 12 | Standardize to $\mathcal{L}$ |

---

## Action Items

### Critical

1. [ ] Add IDs to equations in [sections]
2. [ ] Define variables for @eq-XX-YY

### High Priority

1. [ ] Add equation for [concept] in [section]
2. [ ] Standardize notation for [symbol]

### Medium Priority

1. [ ] [Action item]

---

## Style Consistency Reference

Standard notation used in this book:
- Loss functions: $\mathcal{L}$ (script L)
- Probability: $P(\cdot)$ or $p(\cdot)$ for densities
- Expectations: $\mathbb{E}[\cdot]$
- Vectors: bold lowercase $\mathbf{x}$
- Matrices: bold uppercase $\mathbf{W}$
- Sets: calligraphic $\mathcal{V}$ (vocabulary), $\mathcal{D}$ (dataset)
- Functions: standard $f$, $g$, $h$
- Parameters: Greek $\theta$, $\phi$, $\psi$
```

---

## LaTeX Style Guide

### Display Equations

Use `$$...$$` with proper spacing:

```latex
$$
\mathcal{L} = -\sum_{i=1}^{N} y_i \log \hat{y}_i
$$ {#eq-08-01}
```

### Inline Math

Use `$...$` for inline:
- "The temperature $\tau$ controls sharpness"
- "As $n \to \infty$, the estimate converges"

### Common LaTeX Constructs

| Concept | LaTeX | Rendered |
|---------|-------|----------|
| Summation | `\sum_{i=1}^{N}` | $\sum_{i=1}^{N}$ |
| Product | `\prod_{t=1}^{T}` | $\prod_{t=1}^{T}$ |
| Fraction | `\frac{a}{b}` | $\frac{a}{b}$ |
| Conditional | `P(X \mid Y)` | $P(X \mid Y)$ |
| Expectation | `\mathbb{E}[X]` | $\mathbb{E}[X]$ |
| Loss | `\mathcal{L}` | $\mathcal{L}$ |
| Norm | `\|x\|` | $\|x\|$ |
| Argmax | `\arg\max_\theta` | $\arg\max_\theta$ |
| Approximately | `\approx` | $\approx$ |
| Proportional | `\propto` | $\propto$ |

### Avoid These Patterns

- `||x||` instead of `\|x\|` for norms
- `*` instead of `\cdot` or `\times` for multiplication
- Plain text in math mode (use `\text{...}`)
- Missing `\left` and `\right` for large delimiters

---

## Integration with Editorial Board

This agent is a **Minor Member (Specialist Consultant)** of the Editorial Board.

**Dispatch conditions:**
- Chapter contains mathematical content
- Part review with `--focus pedagogy`
- Explicit request for math review

**Dependencies:**
- Run AFTER `pedagogy-review` (inform math decisions with learning science)
- Run BEFORE `textbook-editor` (equations affect prose flow)

**Conflict resolution:**
- If `pedagogy-review` suggests simplifying and `math-pedagogy` suggests formalizing: prioritize clarity for the target audience
- If equation disrupts narrative: use callout box or appendix

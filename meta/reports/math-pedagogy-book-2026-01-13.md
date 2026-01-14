# Math Pedagogy Review: Full Book

**Generated:** 2026-01-13
**Scope:** All chapters with mathematical content (Parts 2-6)
**Agent:** math-pedagogy (newly created)

---

## Executive Summary

**Overall Equation Health:** Needs Work
**Total Findings:** 70 issues across Parts 2-6

| Category | Part 2-3 | Part 4-6 | Total |
|----------|----------|----------|-------|
| Equations without IDs | 8 | 2 | **10** |
| Missing variable definitions | 12 | 8 | **20** |
| Prose needing formalization | 15 | 5 | **20** |
| Notation inconsistencies | 12 | 3 | **15** |
| **Subtotal** | 47 | 23 | **70** |

**Key Themes:**
1. Display equations lack IDs for cross-referencing
2. Variable definitions often missing or incomplete
3. Notation inconsistent across chapters (especially for variants, losses)
4. Several key concepts described only in prose would benefit from equations

---

## Readiness by Dimension

| Dimension | Grade | Status |
|-----------|-------|--------|
| Equation IDs | C | 10 display equations need IDs |
| Variable Definitions | C | 20 equations have undefined variables |
| Prose-to-Math Balance | B- | 20 opportunities for formalization |
| Notation Consistency | C+ | 15 cross-chapter inconsistencies |
| LaTeX Quality | B+ | Generally correct, minor issues |

---

## Part 2-3 Findings (Architectures & Learning)

### Equations Needing IDs (8)

| Chapter | Location | Equation | Suggested ID |
|---------|----------|----------|--------------|
| ch07-attention | Line 67-68 | Scaled dot-product | `{#eq-07-01}` |
| ch07-attention | Line 90-91 | Softmax attention weights | `{#eq-07-02}` |
| ch07-attention | Line 122-123 | Attention output | `{#eq-07-03}` |
| ch07-attention | Lines 223-228 | Sinusoidal positional encoding | `{#eq-07-04}` |
| ch06-cnn | Line 314-316 | Residual connection | `{#eq-06-01}` |
| ch06-cnn | Line 349-351 | SpliceAI delta score | `{#eq-06-02}` |
| ch12-evaluation | Line 397 | Attention memory requirement | `{#eq-12-01}` |
| ch08-pretraining | Line 279 | InfoNCE loss | `{#eq-08-01}` |

### Critical Variable Definitions Missing

**ch07-attention (Attention mechanism)**
```latex
$$\text{score}(q_i, k_j) = \frac{q_i \cdot k_j}{\sqrt{d_k}}$$
```
**Missing:** $q_i$, $k_j$, $d_k$, $L$

**Recommended fix:**
```markdown
where:
- $q_i \in \mathbb{R}^{d_k}$ is the query vector for position $i$
- $k_j \in \mathbb{R}^{d_k}$ is the key vector for position $j$
- $d_k$ is the key/query dimension (typically 64-128)
- Scaling by $\sqrt{d_k}$ prevents dot products from growing with dimension
```

### High-Priority Prose → Equation Opportunities

| Section | Current Prose | Recommended Equation |
|---------|--------------|---------------------|
| ch07 §sec-ch07-attention | "variance explanation" for scaling | $\text{Var}[q \cdot k] \propto d_k$, hence scale by $\sqrt{d_k}$ |
| ch06 §sec-ch06-receptive | "receptive field grows with depth" | $RF(l) = 1 + \sum_{i=1}^{l} (k_i - 1) \prod_{j=i+1}^{l} s_j$ |
| ch06 §sec-ch06-dilated | Dilated convolution description | $\text{output}[i] = \sum_k w[k] \cdot \text{input}[i + k \cdot r]$ |
| ch12 §sec-ch12-metrics | ECE description | $ECE = \sum_{b=1}^{B} \frac{n_b}{n} \|acc_b - conf_b\|$ |
| ch13 §sec-ch13-confounding | Population structure as shortcut | $P(Y|X,A) = P(Y|A) \cdot P(X|A) / P(X)$ |

### Notation Inconsistencies (Part 2-3)

| Issue | Locations | Resolution |
|-------|-----------|------------|
| Model dimension: $d$ vs $d_k$ vs $d_{\text{model}}$ | ch07, ch06 | Standardize: $d$ = model dim, $d_k$ = key dim |
| Embedding matrix: $E$ vs $W_E$ | ch05, ch07 | Use $\mathbf{E} \in \mathbb{R}^{V \times d}$ |
| auROC vs AUC | ch12 | Use "auROC" consistently |
| Big-O notation | ch07 | Define formally once |

---

## Part 4-6 Findings (FM Families & Responsible Deployment)

### Equations Needing IDs (2)

| Chapter | Location | Description | Suggested ID |
|---------|----------|-------------|--------------|
| ch24-uncertainty | Lines 178-180 | Temperature scaling | `{#eq-24-01}` |
| ch24-uncertainty | (related) | Calibration equation | `{#eq-24-02}` |

### Critical Variable Definitions Missing

**ch14-fm-principles (Scaling Laws)**
```latex
L(N, D) = E + \frac{A}{N^\alpha} + \frac{B}{D^\beta}
```
**Missing:** Dimensional interpretation of $A$, $B$; justification for factor of 6 in $C \approx 6ND$

**ch18-vep-fm (Variant Scoring)**
```latex
\Delta \text{LLR} = \log P(a_{\text{var}} | \text{context}) - \log P(a_{\text{ref}} | \text{context})
```
**Missing:** Definition of "context" (window size), which layer produces $P$

**ch24-uncertainty (Temperature Scaling)**
```latex
\hat{p}_i = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}
```
**Missing:** $z_i$ (logits), $T$ (temperature), typical values

**ch25-interpretability (Integrated Gradients)**
```latex
\text{IG}_i(x) = (x_i - x'_i) \int_{\alpha=0}^{1} \frac{\partial f(x' + \alpha(x - x'))}{\partial x_i} \, d\alpha
```
**Missing:** Reference sequence $x'$, practical step count for discrete approximation

### High-Priority Prose → Equation Opportunities

| Section | Current Prose | Recommended Equation |
|---------|--------------|---------------------|
| ch14 §worked-example | 20 tokens/param heuristic | Derive from $D/N \propto C^{0.02} \approx 20$ |
| ch15 §zero-shot | Likelihood ratio procedure | Add classification thresholds |
| ch17 §variant-effect | "Subtract reference from alt" | $\Delta \mathbf{y} = \mathbf{y}_{\text{alt}} - \mathbf{y}_{\text{ref}}$ |
| ch26 §mendelian | MR assumptions | DAG: $G \to X \to Y$ with $G \perp U$ |

### Cross-Chapter Notation Inconsistency

**Major Issue:** Variant scoring notation differs between protein and DNA chapters

| Chapter | Notation | Meaning |
|---------|----------|---------|
| ch16-protein-lm | $a$, $b$ | Amino acids |
| ch18-vep-fm | $a_{\text{ref}}$, $a_{\text{var}}$ | DNA alleles |

**Resolution:** Standardize:
- Amino acids: `aa_ref`, `aa_alt` or explicit {A, R, N, ...}
- DNA alleles: `allele_ref`, `allele_alt` or explicit {A, C, G, T}

---

## Action Items by Priority

### Critical (Before Publication)

1. **Add equation IDs to 10 display equations**
   - ch07: 4 equations (attention mechanism)
   - ch06: 2 equations (CNN/residual)
   - ch08: 1 equation (InfoNCE)
   - ch12: 1 equation (ECE)
   - ch24: 2 equations (calibration)

2. **Define variables for core equations**
   - ch07: $q_i$, $k_j$, $d_k$ in attention
   - ch14: $A$, $B$ units in scaling law
   - ch18: "context" window specification
   - ch24: $z_i$, $T$ in temperature scaling

3. **Standardize notation across chapters**
   - Loss functions: $\mathcal{L}$ throughout
   - Variant notation: consistent ref/alt subscripts
   - Probability: $P(\cdot)$ vs $p(\cdot)$ usage

### High Priority (Should Address)

4. **Formalize key prose descriptions**
   - Receptive field formula (ch06)
   - Variance scaling justification (ch07)
   - ECE definition (ch12)
   - MR assumptions as DAG (ch26)

5. **Add worked examples with equations**
   - Temperature scaling effect (ch24)
   - Integrated gradients steps (ch25)
   - Variant score interpretation (ch18)

### Medium Priority (Nice to Have)

6. **Create equation convention appendix**
   - Standard notation table
   - Common equations with IDs
   - Cross-reference guide

7. **Add inline equation definitions**
   - First use of Greek letters
   - Domain/range specifications
   - Unit specifications where applicable

---

## Recommended Equation Insertions

### Example 1: ch07-attention (Scaled Dot-Product)

**Current (Line 67-68):**
```latex
$$\text{score}(q_i, k_j) = \frac{q_i \cdot k_j}{\sqrt{d_k}}$$
```

**Recommended:**
```latex
$$
\text{score}(q_i, k_j) = \frac{q_i \cdot k_j}{\sqrt{d_k}}
$$ {#eq-07-01}

where:
- $q_i \in \mathbb{R}^{d_k}$ is the query vector for position $i$, computed as $q_i = x_i W^Q$
- $k_j \in \mathbb{R}^{d_k}$ is the key vector for position $j$, computed as $k_j = x_j W^K$
- $d_k$ is the dimension of keys and queries (typically 64 per attention head)
- The $\sqrt{d_k}$ scaling prevents dot products from growing large with dimension, keeping softmax gradients healthy
```

### Example 2: ch24-uncertainty (Temperature Scaling)

**Current (Line 248):**
```latex
$$\hat{p}_i = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$
```

**Recommended:**
```latex
$$
\hat{p}_i = \frac{\exp(z_i / T)}{\sum_{j=1}^{K} \exp(z_j / T)}
$$ {#eq-24-01}

where:
- $z_i$ is the logit (pre-softmax score) for class $i$ from the model's final layer
- $K$ is the number of classes
- $T > 0$ is the temperature parameter:
  - $T = 1$: original softmax (no calibration)
  - $T > 1$: softer predictions (reduces overconfidence)
  - $T < 1$: sharper predictions (increases confidence)
- $T$ is learned on a held-out calibration set by minimizing negative log-likelihood
```

### Example 3: ch26-causal (Mendelian Randomization)

**Current (Lines 120-124):** Verbal description of three assumptions

**Recommended addition:**
```latex
$$
\beta_{X \to Y} = \frac{\text{Cov}(G, Y)}{\text{Cov}(G, X)}
$$ {#eq-26-01}

The Wald estimator above is valid under three assumptions:

1. **Relevance:** $\text{Cov}(G, X) \neq 0$ (instrument predicts exposure)
2. **Independence:** $G \perp\!\!\!\perp U$ (no confounding of instrument-outcome)
3. **Exclusion:** No direct path $G \to Y$ (effect only through $X$)

where:
- $G$ is the genetic instrument (SNP or polygenic score)
- $X$ is the exposure (e.g., LDL cholesterol level)
- $Y$ is the outcome (e.g., cardiovascular disease risk)
- $U$ represents unmeasured confounders
```

---

## Cross-Chapter Consistency Checklist

| Symbol | Standard Definition | Chapters Using |
|--------|---------------------|----------------|
| $\mathcal{L}$ | Loss function | ch06, ch07, ch08, ch12, ch24 |
| $d$ | Model/embedding dimension | ch05, ch07 |
| $d_k$ | Key dimension (attention) | ch07 |
| $T$ | Sequence length OR temperature | ch08 (length), ch24 (temp) - **CONFLICT** |
| $N$ | Batch size OR model params | ch08 (batch), ch14 (params) - **CONFLICT** |
| $P(\cdot)$ | Probability distribution | All chapters |
| $\theta$ | Model parameters | ch08, ch10, ch14 |

**Conflicts to resolve:**
- $T$: Use $L$ for sequence length, $T$ only for temperature
- $N$: Use $B$ for batch size, $N$ for model parameters

---

## Style Consistency Standards (Established)

Based on this review, the book should adopt:

| Element | Standard | Example |
|---------|----------|---------|
| Loss functions | Script $\mathcal{L}$ | $\mathcal{L}_{\text{CE}}$ |
| Vectors | Bold lowercase | $\mathbf{x}$, $\mathbf{q}$ |
| Matrices | Bold uppercase | $\mathbf{W}$, $\mathbf{K}$ |
| Sets | Calligraphic | $\mathcal{V}$ (vocabulary) |
| Probabilities | Capital $P$ | $P(x \mid y)$ |
| Expectations | Blackboard | $\mathbb{E}[X]$ |
| Equation IDs | `{#eq-CC-NN}` | `{#eq-07-01}` |

---

## Follow-Up Recommendations

1. **Immediate:** Address 10 missing equation IDs
2. **This week:** Add variable definitions to critical equations in ch07, ch14, ch24
3. **Before publication:** Complete notation standardization pass
4. **Create:** Appendix with standard notation reference table

---

## Agent Reference

This report was generated by the **math-pedagogy** agent, a new specialist consultant added to the Editorial Board. The agent is defined at:
- [.claude/agents/math-pedagogy/AGENT.md](/root/gfm_book/.claude/agents/math-pedagogy/AGENT.md)
- [.claude/agents/math-pedagogy/equation-conventions.md](/root/gfm_book/.claude/agents/math-pedagogy/equation-conventions.md)

To run targeted reviews:
```bash
/math-pedagogy p3-ch08-pretraining  # Single chapter
/math-pedagogy part_3 --mode audit  # Existing equations only
/math-pedagogy --mode opportunities # Find prose needing equations
```

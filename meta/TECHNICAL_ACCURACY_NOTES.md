# Technical Accuracy Notes: KB Content Additions

**Detailed mathematical and technical verification**

---

## Information Theory (Ch05, Ch08)

### 5.1: Information-Theoretic View of Embeddings

#### Claim: "Rate $R = H(T)$ measures bits per position"
**Assessment:** ✓ CORRECT
- Entropy of token distribution $H(T) = -\sum p_i \log_2 p_i$ measures average bits
- Correct formulation

#### Claim: "$R \leq \log_2 |V|$"
**Assessment:** ✓ CORRECT
- Maximum entropy is log of alphabet size
- Standard result

#### Claim: "$I(E(T); Y) \leq d \cdot C$ capacity bottleneck"
**Assessment:** ⚠️ IMPRECISE
- **Issue:** The bound statement is vague. Information capacity depends on:
  1. Activation precision (bits per activation)
  2. Network depth (information refined through layers)
  3. Channel capacity of layers between $E(T)$ and $Y$

- **Correct version:** Information through a single layer with $d$ dimensions and $b$ bits per value is bounded by $d \cdot b$. But:
  - With ReLU, precision is continuous (theoretical infinite bits)
  - With quantization, $b$ is specific but loses information
  - Subsequent layers can refine information

- **Fix needed:** Clarify whether this is:
  - Single-layer bottleneck: "A single embedding layer with $d$ dimensions can encode at most $d$ bits (with binary activations)"
  - Information-theoretic: "The mutual information $I(E(T); Y)$ is bounded by the information in all parameters"

**Suggested revision:**
```markdown
The embedding dimension $d$ provides an initial bottleneck. If embeddings use
$b$ bits of precision per dimension, the maximum mutual information is bounded
by $I(E(T); Y) \leq d \cdot b$. In practice, this bound is often loose because:
- Subsequent network layers refine information
- Precision is continuous (ReLU), not binary
- Redundancy in the embedding space is expected

In practice, larger embedding dimensions help until task complexity saturates.
```

---

### 5.2: Entropy and Embedding Dimension

#### Claim: "$H(T) = -\sum_{i=1}^{|V|} p_i \log_2 p_i$"
**Assessment:** ✓ CORRECT
- Standard Shannon entropy formula
- Correct base-2 logarithm for bits

#### Claim: "Uniform baseline $H_{max} = \log_2 |V|$"
**Assessment:** ✓ CORRECT
- Entropy maximized when all tokens equally likely
- Standard result

#### Claim: "Empirical observation: H(T) ≈ 0.7 · H_max"
**Assessment:** ❌ UNSUBSTANTIATED
- No citation provided
- No measurement methodology specified
- The 0.7 value appears arbitrary
- Different tokenizers (BPE, k-mer, subword) will have very different entropies

**Fix required:** Either:
1. Cite the study making this empirical claim
2. Change to range: "H(T) appears to be 0.5–0.8 · H_max, varying with tokenizer"
3. Remove and replace with conceptual statement

---

### 8.1: Masked Language Modeling as Entropy Estimation

#### Claim: "$\mathcal{L}_{MLM} = -\mathbb{E}[\log p_\theta(x_i | x_{\setminus i})]$ is conditional entropy minimization"
**Assessment:** ✓ CORRECT (with note)
- This is the cross-entropy loss
- Minimizing cross-entropy is equivalent to minimizing conditional entropy
- Standard result in information theory

#### Claim: "Well-trained MLM learns $p_\theta(x_i | x_{\setminus i}) \approx p_{data}(x_i | x_{\setminus i})$"
**Assessment:** ✓ CORRECT IN PRINCIPLE, ⚠️ PRACTICALLY LOOSE
- True that MLM learns conditional distribution
- BUT: Real MLMs have limited capacity and don't perfectly match data distribution
- The approximation $\approx$ can be quite loose in practice

**Suggested clarification:**
```markdown
A well-trained MLM aims to learn the conditional distribution:
$$p_\theta(x_i | x_{\setminus i}) \approx p_{data}(x_i | x_{\setminus i})$$

In practice, this approximation improves with model scale but is never perfect.
The fidelity of this approximation affects downstream task performance.
```

#### Claim: "Genomic DNA (~1.9 bits/base) tolerates higher masking than protein (~4.2 bits/residue)"
**Assessment:** ❌ UNSUBSTANTIATED AND LOGICALLY UNCLEAR
- **Missing citations:** Where do 1.9 and 4.2 bits/position come from?
- **Logical gap:** Higher entropy → higher masking? This needs justification
  - Actually: higher entropy means more information per position
  - Intuition: "More random sequence requires less masking to disambiguate"?
  - OR: "Lower entropy (more constrained) allows higher masking"?

The direction of the causal claim is unclear.

**Fix needed:**
```markdown
The intrinsic entropy of biological sequences affects masking rate optimization:
- DNA has lower entropy (~1.9 bits/position) due to base composition bias
- Proteins have higher entropy (~4.2 bits/position)

The optimal masking rate may differ due to: [mechanism needed]
- [Higher entropy allows...]
- [Lower entropy requires...]

[Citations of masking studies for genomic vs. protein models needed]
```

---

## Signal Processing & CNNs (Ch06)

### 6.1: CNNs as Learned Filter Banks

#### Claim: "Convolution operation is technically *cross-correlation*"
**Assessment:** ✓ CORRECT
- Standard implementations (PyTorch, TensorFlow) use cross-correlation
- Often called "convolution" in literature despite technical incorrectness
- Distinction: convolution flips the kernel; cross-correlation doesn't

**Note:** Should clarify this is standard terminology, not an error:
```markdown
technically *cross-correlation* (the standard implementation in deep learning,
though called "convolution" throughout the literature)
```

#### Claim: "Convolution theorem: $\mathcal{F}(x * w) = \mathcal{F}(x) \cdot \mathcal{F}(w)$"
**Assessment:** ✓ CORRECT
- Standard signal processing result
- Assumes periodic boundary conditions for discrete case
- May need note about edge effects

#### Claim: "First-layer filters learn low-frequency and high-frequency patterns"
**Assessment:** ✓ CORRECT FOR IMAGES; ⚠️ UNVERIFIED FOR GENOMICS
- Well-established empirically for image CNNs (Yosinski et al.)
- **NOT verified empirically for genomic CNNs**
- Claim should be qualified or cited with genomic-specific studies

**Suggested revision:**
```markdown
First-layer filters in vision models are known to learn:
- Low-frequency patterns: broad features
- High-frequency patterns: edges and textures

This phenomenon has not been systematically studied in genomic models,
but is likely similar given the shared CNN architecture. [Citation needed
or remove claim]
```

---

### 6.2: Fourier Perspective on Dilated Convolutions

#### Claim: "Standard convolution with kernel size $k$ has cutoff frequency $f_c \propto 1/k$"
**Assessment:** ⚠️ APPROXIMATELY CORRECT BUT IMPRECISE
- **True:** Cutoff frequency is related to kernel size inversely
- **Issue:** The exact relationship depends on:
  - Window function (rectangular window vs. Hann, etc.)
  - Sampling rate
  - Definition of "cutoff" (3dB point, first zero crossing, etc.)

- **More precise:** For uniform kernel of size $k$, the spectral null occurs at frequency $f = 1/k$ (in normalized units)

**Suggested revision:**
```markdown
**Standard convolution** with kernel size $k$ has approximate cutoff frequency
related to $1/k$ (more precisely, the first spectral null occurs at $f = 1/k$
for uniform kernels). The relationship depends on kernel parameterization.
```

#### Claim: "Dilated convolution shifts frequency response, capturing patterns at scale $d \cdot k$"
**Assessment:** ✓ CORRECT INTUITION, ⚠️ NEEDS PRECISION
- **True:** Dilation increases effective receptive field to $d \cdot k$
- **Frequency effect:** Shifts the response toward lower frequencies
- **Mathematical:** Replaces $x[n]$ with $x[n \cdot d]$, compressing frequency by factor $d$

**Correct formulation:**
```markdown
Dilated convolution with dilation $d$ effectively samples the input at intervals
of $d$, compressing the frequency domain by factor $d$. This shifts the cutoff
frequency from $1/k$ to $1/(d \cdot k)$, allowing capture of longer-range patterns.
```

---

## Learning Theory (Ch07, Ch14, Appendix G)

### 7.1: State Space Models

#### Claim: "SSM: $\frac{dx(t)}{dt} = Ax(t) + Bu(t)$, $y(t) = Cx(t) + Du(t)$"
**Assessment:** ✓ CORRECT
- Standard linear dynamical system formulation
- Correct matrices and definitions

#### Claim: "Discretization: $\bar{A} = \exp(\Delta A)$, $\bar{B} = (\Delta A)^{-1}(\exp(\Delta A) - I) \cdot \Delta B$"
**Assessment:** ✓ CORRECT (bilinear discretization)
- This is the matrix exponential discretization method
- Exact for this system
- Assumes $\Delta A$ invertible (true for most systems)

#### Claim: "HiPPO initialization enables long-range memory"
**Assessment:** ✓ CORRECT
- HiPPO (High-order Polynomial Projection Operator) projects history onto polynomial basis
- Theoretically motivated for long-range dependencies
- Empirically validated in Gu et al. (2020, 2021)

#### Claim: "SSM complexity $O(L)$, Attention $O(L^2)$"
**Assessment:** ⚠️ IMPRECISE ON BOTH COUNTS
- **Attention:** $O(L^2)$ space and time for standard scaled dot-product attention
  - Can be reduced with sparse attention, approximate attention, etc.

- **SSM:** $O(L)$ only with:
  - HiPPO parameterization (special structure)
  - FFT-based computation
  - NOT true for general SSMs

**Suggested revision:**
```markdown
| Complexity per layer | $O(L^2)$ time, $O(L)$ space | $O(L \log L)$ with FFT-based computation* |
*Requires HiPPO parameterization enabling FFT speedups
```

#### Claim: "Selective SSM recovers input-dependent gating similar to attention"
**Assessment:** ⚠️ PARTIALLY CORRECT, OVERSTATED
- **True:** Mamba adds input-dependent $B, C, \Delta$ parameters
- **Question:** Does this "recover" attention?
  - Mamba is empirically effective
  - Mechanistic similarity to attention is unclear
  - Not full attention (no pair-wise tokens compared)

**Suggested revision:**
```markdown
**Selective state spaces (Mamba):** Making $\Delta, B, C$ input-dependent
adds selective processing of inputs, partially emulating attention's
flexibility while retaining linear complexity. The extent to which this
recovers attention-like behavior is still being investigated empirically.
```

---

### 14.1: Statistical Learning Theory

#### Claim: "VC dimension of neural networks with $W$ weights is $O(W \log W)$"
**Assessment:** ⚠️ CORRECT BUT TIGHT BOUND UNKNOWN
- **True:** Classical bounds give $O(W \log W)$
- **Issue:** These bounds are VERY loose in practice
- **Modern view:** Effective capacity is much smaller than VC dimension suggests

**Suggested clarification:**
```markdown
Classical theory bounds VC dimension as $O(W \log W)$ for networks with $W$
weights. However, these bounds are extremely loose—actual generalization
suggests effective capacity is much smaller, implying other factors (implicit
bias, data structure) dominate the picture.
```

#### Claim: "Gradient descent on overparameterized models: minimum norm solution"
**Assessment:** ⚠️ EMPIRICALLY OBSERVED, NOT UNIVERSALLY PROVEN
- **True for:** Linear models, some nonlinear cases with appropriate loss
- **NOT true for:** All neural network architectures and losses
- **Evidence:** Soudry et al. (2018) for logistic regression; less clear for general NNs

**Suggested revision:**
```markdown
### Implicit Regularization (Empirical Observations)

Gradient descent on overparameterized models exhibits regularizing behavior:

**Minimum Norm (in special cases).** For logistic regression and some other
problems, SGD converges to the minimum norm solution among those fitting training
data. This has been proven for certain architectures but is not universal.
```

#### Claim: "Double descent: test error improves past interpolation threshold"
**Assessment:** ✓ CORRECT PHENOMENOLOGICALLY, ⚠️ INCOMPLETE THEORY
- **True:** Double descent observed empirically across many settings
- **Theory:** Conditions for benign overfitting still being characterized
- **Belkin et al. (2019):** Established phenomenon but theory is incomplete

**Suggested revision:**
```markdown
**Double Descent (empirical phenomenon).** Test error often follows a U-shape
as model capacity increases, but then *decreases again* past the interpolation
threshold where training error becomes zero. This "double descent" has been
observed in many settings but the conditions ensuring the second descent are
still being characterized theoretically. See Belkin et al. (2019).
```

#### Claim: "Effective number of parameters much smaller than nominal"
**Assessment:** ⚠️ SOMETIMES TRUE, CONTEXT-DEPENDENT
- **True for:** Overparameterized models with implicit regularization
- **Measured by:** Effective dimension, degrees of freedom, effective sample size
- **NOT necessarily true for:** All modern architectures or loss landscapes

**Suggested revision:**
```markdown
**Effective Dimension.** In overparameterized models with implicit regularization,
the number of "truly free" parameters (those controlling important degrees of
freedom) may be much smaller than the nominal parameter count. This can be
quantified through various measures of effective dimension, though these are
task and architecture dependent.
```

#### Claim: "Scaling law: $\epsilon_{test} \approx (N_c/N)^{\alpha_N} + (P_c/P)^{\alpha_P} + \epsilon_\infty$"
**Assessment:** ✓ CORRECT FORM, ⚠️ CAVEATS NEEDED
- **True:** Language models follow empirical power laws
- **Source:** Hoffmann et al. (2022), Kaplan et al. (2020)
- **Caveats:**
  - Validity limited to studied regimes
  - Exponents vary by task
  - No theoretical justification

**Suggested revision:**
```markdown
**Empirical Power Laws.** Foundation models in language exhibit test loss
following approximate power laws:

$$\epsilon_{test} \approx \left(\frac{N_c}{N}\right)^{\alpha_N} + \left(\frac{P_c}{P}\right)^{\alpha_P} + \epsilon_\infty$$

with empirical estimates $\alpha \approx 0.07$ for language models.

**Important limitations:**
- Power law exponents vary across tasks and modalities
- No theoretical explanation for these particular forms
- Validity restricted to regimes studied (roughly 10^10 to 10^12 parameters)
- Extrapolation to larger/smaller scales is speculative
```

---

## Causal Inference (Ch13, Ch26)

### 13.1: DAG Notation

#### Claim: "$Z$ confounds $X \to Y$ in fork"
**Assessment:** ✓ CORRECT
- Standard causal graph notation
- DAG correctly represents fork (common cause)

#### Claim: "d-separation path blockage rules"
**Assessment:** ✓ CORRECT
- Rules 1 (chain/fork) and 2 (collider) are correct
- These are Pearl's standard definitions

**Minor note:** Rule 2 could be clearer:
```markdown
2. Contains a collider whose middle node (and descendants) is NOT in $Z$
   (Note: colliders block paths by default; conditioning on a collider or its
   descendants UNBLOCKs the path)
```

---

### 13.2: Collider Bias Example

#### Claim: "Selecting variants into ClinVar creates collider bias"
**Assessment:** ✓ CORRECT
- DAG structure is accurate
- Mechanism is correctly identified
- Good example

#### Claim: "Pathogenicity and study interest become negatively correlated among ClinVar"
**Assessment:** ⚠️ DIRECTIONALLY CORRECT, MAGNITUDE UNKNOWN
- **True direction:** Pathogenic variants are in ClinVar for one reason; benign variants for another
- **Magnitude:** Depends on relative frequencies of pathogenic vs. interesting variants
- **Not quantified:** No sense of how strong this effect is

**Suggested revision:**
```markdown
Among ClinVar variants, pathogenicity and "study interest" become negatively
correlated—if a benign variant is selected for inclusion, it likely has other
properties making it interesting to study. The strength of this correlation
depends on the relative prevalence of pathogenic vs. interesting variants.
```

---

### 26.1: Causal Identification

#### Claim: "Backdoor criterion: $P(Y | do(X)) = \sum_z P(Y | X, Z=z) P(Z=z)$"
**Assessment:** ✓ CORRECT
- Standard backdoor criterion formula
- Conditions correctly stated

#### Claim: "Frontdoor criterion formula"
**Assessment:** ✓ CORRECT
- Formula correctly states frontdoor adjustment
- Standard Pearl result

#### Claim: "Do-calculus rules are complete"
**Assessment:** ✓ CORRECT
- Pearl proved completeness of do-calculus
- If identifiable, do-calculus can derive estimand

---

## Graph Theory (Ch22)

### 22.1: Graph Theory Foundations

#### Claim: "Laplacian $L = D - A$ has eigenvalues ≥ 0"
**Assessment:** ✓ CORRECT
- Standard graph Laplacian
- Positive semi-definite
- Smallest eigenvalue is 0

#### Claim: "Number of zero eigenvalues = number of connected components"
**Assessment:** ✓ CORRECT
- Standard result in spectral graph theory
- Each connected component contributes one zero eigenvalue

#### Claim: "PPI networks have diameter 4-6"
**Assessment:** ⚠️ NEEDS CITATION AND QUALIFICATION
- Empirically observed in some PPI networks
- Values vary by dataset and species
- Example: yeast PPI ~5, human PPI ~6-7 (rough)

**Suggested revision:**
```markdown
**Small-World Property.** Biological networks typically have:
- Small diameter (for PPI networks, often reported as 4-6, though this varies
  by dataset and species)
- High clustering coefficient
```

#### Claim: "Hub genes are often essential"
**Assessment:** ⚠️ CORRELATION, NOT CAUSATION; CONFOUNDING LIKELY
- **Empirically observed:** Hubs are enriched for essential genes
- **Confounding:** Hubs are also well-studied (publication bias)
- **Direction unclear:** Does connectivity cause essentiality or vice versa?

**Suggested revision:**
```markdown
High-degree nodes ("hubs") are enriched for genes that cause strong phenotypes
when deleted. However, this may reflect study bias (essential genes are more
thoroughly studied), not a causal relationship from network structure.
```

---

### 22.2: Network Dynamics

#### Claim: "Heat diffusion: $\frac{\partial h(t)}{\partial t} = -L \cdot h(t)$"
**Assessment:** ✓ CORRECT
- Standard heat equation on graphs
- Laplacian operator correct

#### Claim: "Solution: $h(t) = e^{-Lt} h(0)$"
**Assessment:** ✓ CORRECT
- Standard matrix exponential solution

#### Claim: "Random walk with restart converges to network proximity"
**Assessment:** ✓ CORRECT
- Standard procedure
- RWR is used in GeneMANIA, PRINCE, etc.

---

## Bayesian Methods (Ch24)

### 24.1: Bayesian UQ

#### Claim: "$p(\theta | D) = \frac{p(D|\theta) p(\theta)}{p(D)}$ (Bayes theorem)"
**Assessment:** ✓ CORRECT
- Standard Bayes theorem
- Correct notation and interpretation

#### Claim: "Metropolis-Hastings acceptance probability formula"
**Assessment:** ✓ CORRECT
- Standard MH algorithm
- Formula is correct

#### Claim: "MC Dropout approximates variational inference"
**Assessment:** ⚠️ TRUE BUT WITH CAVEATS
- **True:** Gal & Ghahramani (2016) showed formal connection
- **Caveat:** Quality of approximation depends heavily on dropout rate
- **Issue:** Often used without careful dropout rate tuning

**Suggested revision:**
```markdown
**MC Dropout as Approximate Inference.** Gal & Ghahramani (2016) showed that
dropout at test time, with specific dropout rates, can be interpreted as
sampling from an approximate posterior. However, the approximation quality
depends on dropout rate and network architecture, and is often poor in practice.
```

#### Claim: "Deep ensembles sample the posterior"
**Assessment:** ⚠️ HEURISTIC, NOT FORMAL POSTERIOR
- **True:** Ensemble disagreement estimates uncertainty
- **False:** This is not the posterior in any formal sense
- **Better framing:** "Implicit ensemble posterior" or "empirical approximation"

**Suggested revision:**
```markdown
**Deep Ensembles as Implicit Posterior.** Training multiple networks from
different initializations provides an empirical uncertainty estimate via
ensemble disagreement. This can be viewed as sampling from an implicit
posterior, though it is not a formal Bayesian posterior.
```

---

## Appendix G: Statistical Learning Theory

### General Notes

Most claims here are correct but overcautious or underspecified. The main issues:

1. **VC dimension table:**
   - Linear classifiers in $\mathbb{R}^d$: VC = $d+1$ ✓ CORRECT
   - Axis-aligned rectangles: VC = 4 ✓ CORRECT
   - Circles in $\mathbb{R}^2$: VC = 3 ✓ CORRECT
   - Neural networks: VC = $O(W \log W)$ ⚠️ CORRECT BUT VERY LOOSE

2. **Classical bounds:** ✓ CORRECT formulation

3. **Implicit regularization:** ⚠️ EMPIRICALLY OBSERVED, NOT FULLY PROVEN

4. **Benign overfitting:** ⚠️ REPEATS Ch14 issues

5. **PAC-Bayes bounds:** ✓ CORRECT but note very loose for neural networks

6. **Scaling laws:** ✓ CORRECT but note empirical/speculative nature

---

## Summary of Technical Issues

| Severity | Issue | Location | Type |
|----------|-------|----------|------|
| CRITICAL | Empirical specificity (0.7, 1.9, 4.2) | 5.2, 8.1 | Unsupported numbers |
| CRITICAL | Causal language on correlations | 8.1, 22.1, 28.1 | Conceptual error |
| HIGH | Benign overfitting underspecified | 14.1, App G | Incomplete theory |
| HIGH | SSM complexity qualified wrong | 7.1 | Technical imprecision |
| MODERATE | Signal processing formulas | 6.2 | Needs qualification |
| MODERATE | Implicit bias scope | App G | Overgeneralized |
| MODERATE | Hub-essentiality claim | 22.1 | Confounding unaddressed |
| LOW | Various minor clarifications | Multiple | Polish |

---

**Technical Review Completed:** 2026-01-20
**Recommendation:** Fix critical and high-severity items before final submission

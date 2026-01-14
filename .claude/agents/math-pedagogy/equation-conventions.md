# Equation Conventions for GFM Book

Standard notation and conventions for mathematical content across the book.

---

## Equation Numbering Scheme

### Format: `{#eq-CC-NN}`

- `CC` = Two-digit chapter number (01-32)
- `NN` = Sequential equation number within chapter (01, 02, 03...)

**Examples:**
- `{#eq-08-01}` = Chapter 8, Equation 1
- `{#eq-12-15}` = Chapter 12, Equation 15

### What Gets an ID

| Equation Type | Gets ID? | Rationale |
|---------------|----------|-----------|
| Key definitions (loss functions, metrics) | Yes | Cross-reference target |
| Formulas referenced later | Yes | Enables @eq-XX-YY citations |
| Central to understanding | Yes | Reader may return to it |
| Simple inline expressions | No | Clutters namespace |
| Standard definitions (softmax, etc.) | Optional | Only if referenced |
| Intermediate derivation steps | No | Only final result |

---

## Standard Notation

### Loss Functions and Objectives

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\mathcal{L}$ | Loss function (general) | `\mathcal{L}` |
| $\mathcal{L}_{\text{CE}}$ | Cross-entropy loss | `\mathcal{L}_{\text{CE}}` |
| $\mathcal{L}_{\text{MSE}}$ | Mean squared error | `\mathcal{L}_{\text{MSE}}` |
| $\mathcal{L}_{\text{MLM}}$ | Masked language modeling loss | `\mathcal{L}_{\text{MLM}}` |
| $\mathcal{L}_{\text{NCE}}$ | Noise contrastive estimation | `\mathcal{L}_{\text{NCE}}` |

### Probability and Statistics

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $P(X)$ | Probability of event X | `P(X)` |
| $P(X \mid Y)$ | Conditional probability | `P(X \mid Y)` |
| $p(x)$ | Probability density | `p(x)` |
| $\mathbb{E}[X]$ | Expectation | `\mathbb{E}[X]` |
| $\text{Var}(X)$ | Variance | `\text{Var}(X)` |
| $\mathcal{N}(\mu, \sigma^2)$ | Normal distribution | `\mathcal{N}(\mu, \sigma^2)` |

### Sequences and Tokens

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $x_t$ | Token at position $t$ | `x_t` |
| $T$ | Sequence length | `T` |
| $\mathcal{V}$ | Vocabulary | `\mathcal{V}` |
| $|\mathcal{V}|$ | Vocabulary size | `|\mathcal{V}|` |
| $\mathbf{x}$ | Sequence (vector of tokens) | `\mathbf{x}` |
| $[x_1, x_2, \ldots, x_T]$ | Explicit sequence | `[x_1, x_2, \ldots, x_T]` |

### Embeddings and Representations

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\mathbf{e}$ | Embedding vector | `\mathbf{e}` |
| $\mathbf{z}$ | Latent representation | `\mathbf{z}` |
| $\mathbf{h}$ | Hidden state | `\mathbf{h}` |
| $d$ | Embedding dimension | `d` |
| $d_{\text{model}}$ | Model dimension | `d_{\text{model}}` |
| $d_k$ | Key dimension (attention) | `d_k$ |

### Model Components

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\mathbf{W}$ | Weight matrix | `\mathbf{W}` |
| $\mathbf{b}$ | Bias vector | `\mathbf{b}` |
| $\theta$ | Model parameters (general) | `\theta` |
| $\phi$ | Encoder parameters | `\phi` |
| $\psi$ | Decoder parameters | `\psi` |
| $f_\theta$ | Parameterized function | `f_\theta` |

### Attention Mechanism

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\mathbf{Q}$ | Query matrix | `\mathbf{Q}` |
| $\mathbf{K}$ | Key matrix | `\mathbf{K}` |
| $\mathbf{V}$ | Value matrix | `\mathbf{V}` |
| $\alpha_{ij}$ | Attention weight from $i$ to $j$ | `\alpha_{ij}` |
| $H$ | Number of attention heads | `H` |
| $L$ | Number of layers | `L` |

### Evaluation Metrics

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\text{AUC}$ | Area under ROC curve | `\text{AUC}` |
| $\text{auPRC}$ | Area under precision-recall curve | `\text{auPRC}` |
| $R^2$ | Coefficient of determination | `R^2` |
| $r$ | Pearson correlation | `r$ |
| $\rho$ | Spearman correlation | `\rho` |
| $\text{MCC}$ | Matthews correlation coefficient | `\text{MCC}` |

### Genomic-Specific

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $k$ | k-mer size | `k` |
| $N$ | Number of samples/batch size | `N` |
| $G$ | Number of genes | `G$ |
| $S$ | Number of SNPs/variants | `S` |
| $\mathbf{A}$ | Adjacency matrix (networks) | `\mathbf{A}` |

---

## Canonical Equations

### Cross-Entropy Loss

$$
\mathcal{L}_{\text{CE}} = -\sum_{c=1}^{C} y_c \log \hat{y}_c
$$ {#eq-canonical-ce}

where:
- $C$ is the number of classes
- $y_c \in \{0,1\}$ is the true label indicator for class $c$
- $\hat{y}_c \in [0,1]$ is the predicted probability for class $c$

### Softmax Function

$$
\text{softmax}(\mathbf{z})_i = \frac{\exp(z_i)}{\sum_{j=1}^{K} \exp(z_j)}
$$ {#eq-canonical-softmax}

where:
- $\mathbf{z} = [z_1, \ldots, z_K]$ is a vector of logits
- $K$ is the number of output classes

### Scaled Dot-Product Attention

$$
\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}
$$ {#eq-canonical-attention}

where:
- $\mathbf{Q} \in \mathbb{R}^{n \times d_k}$ is the query matrix
- $\mathbf{K} \in \mathbb{R}^{m \times d_k}$ is the key matrix
- $\mathbf{V} \in \mathbb{R}^{m \times d_v}$ is the value matrix
- $d_k$ is the key dimension (scaling factor prevents dot products from growing large)

### InfoNCE Contrastive Loss

$$
\mathcal{L}_{\text{InfoNCE}} = -\log \frac{\exp(\text{sim}(z_i, z_i^{+}) / \tau)}{\sum_{j=1}^{N} \exp(\text{sim}(z_i, z_j) / \tau)}
$$ {#eq-canonical-infonce}

where:
- $z_i$ is the embedding of anchor sample $i$
- $z_i^{+}$ is the embedding of the positive pair for sample $i$
- $\text{sim}(\cdot, \cdot)$ is a similarity function (typically cosine similarity)
- $\tau > 0$ is the temperature parameter
- $N$ is the total number of samples (positive + negatives)

### Masked Language Modeling Loss

$$
\mathcal{L}_{\text{MLM}} = -\sum_{t \in \mathcal{M}} \log P(x_t \mid \mathbf{x}_{\backslash \mathcal{M}}; \theta)
$$ {#eq-canonical-mlm}

where:
- $\mathcal{M}$ is the set of masked positions
- $x_t$ is the true token at masked position $t$
- $\mathbf{x}_{\backslash \mathcal{M}}$ is the sequence with masked positions replaced by `[MASK]`
- $\theta$ are the model parameters

### Autoregressive (Next-Token) Loss

$$
\mathcal{L}_{\text{AR}} = -\sum_{t=1}^{T} \log P(x_t \mid x_1, \ldots, x_{t-1}; \theta)
$$ {#eq-canonical-ar}

where:
- $T$ is the sequence length
- $x_t$ is the token at position $t$
- The model predicts each token conditioned only on preceding tokens

### Cosine Similarity

$$
\text{sim}_{\cos}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}
$$ {#eq-canonical-cosine}

where:
- $\mathbf{a}, \mathbf{b}$ are vectors
- $\mathbf{a} \cdot \mathbf{b} = \sum_i a_i b_i$ is the dot product
- $\|\mathbf{a}\| = \sqrt{\sum_i a_i^2}$ is the L2 norm

### Mean Squared Error

$$
\mathcal{L}_{\text{MSE}} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2
$$ {#eq-canonical-mse}

where:
- $N$ is the number of samples
- $y_i$ is the true value for sample $i$
- $\hat{y}_i$ is the predicted value for sample $i$

### Pearson Correlation

$$
r = \frac{\sum_{i=1}^{N} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{N}(x_i - \bar{x})^2 \sum_{i=1}^{N}(y_i - \bar{y})^2}}
$$ {#eq-canonical-pearson}

where:
- $x_i, y_i$ are paired observations
- $\bar{x}, \bar{y}$ are sample means
- $N$ is the number of observations

---

## Variable Definition Template

After each display equation, include a "where" block:

```markdown
$$
[equation]
$$ {#eq-XX-YY}

where:
- $symbol_1$ is [definition including units if applicable]
- $symbol_2$ is [definition]
- $symbol_3 \in [domain]$ is [definition]
```

**Best practices:**
- Define in order of appearance (left to right, top to bottom)
- Specify domains when non-obvious (e.g., $\tau > 0$)
- Include units for physical quantities
- Reference where symbols were introduced if reusing

---

## Cross-Reference Format

To reference an equation:
- Use `@eq-08-01` to render as "Equation 8.1"
- Use `(@eq-08-01)` to render as "(Equation 8.1)"
- Use `the loss function in @eq-08-01` for inline references

**Example:**
> The contrastive objective (@eq-08-03) encourages the model to...

# Claim Detection Patterns

Patterns for identifying factual claims that may require citations.

## Quantitative Claims (HIGH PRIORITY)

### Performance Metrics

**Patterns:**
- `achieves [0-9.]+ (auROC|auPRC|F1|accuracy|MCC)`
- `[0-9]+% (accuracy|precision|recall|improvement)`
- `(auROC|auPRC|accuracy) of [0-9.]+`
- `improves (by|over) [0-9]+%`

**Examples:**
- "achieves 0.94 auROC" - NEEDS CITATION
- "improves accuracy by 15%" - NEEDS CITATION
- "F1 score of 0.87" - NEEDS CITATION

### Dataset Statistics

**Patterns:**
- `contains [0-9,]+ (samples|variants|sequences|genomes|exomes)`
- `[0-9,]+ (patients|individuals|cell types|tissues)`
- `covers [0-9]+% of (the genome|variants|genes)`

**Examples:**
- "contains 125,748 exomes" - NEEDS CITATION
- "spans 1.2 million variants" - NEEDS CITATION
- "covers 95% of protein-coding genes" - NEEDS CITATION

### Architectural Specifications (MEDIUM PRIORITY)

**Patterns:**
- `[0-9]+ (layers|attention heads|parameters|dimensions)`
- `context (window|length) of [0-9]+( ?kb| ?bp)?`
- `[0-9]+ (million|billion|M|B) parameters`
- `trained (on|with) [0-9]+ (GPUs|TPUs)`

**Examples:**
- "uses 12 transformer layers" - NEEDS CITATION if specific to a model
- "768-dimensional embeddings" - NEEDS CITATION for specific model
- "7 billion parameters" - NEEDS CITATION

### Biological Quantities

**Patterns:**
- `[0-9]+( ?kb| ?Mb| ?bp) (upstream|downstream|away|distance)`
- `half-life of [0-9]+ (hours|minutes|days)`
- `expressed in [0-9]+% of (cells|tissues)`
- `[0-9]+ (fold|x) (increase|decrease|change)`

**Examples:**
- "enhancers located 500kb upstream" - MAY NEED CITATION
- "3-fold increase in expression" - NEEDS CITATION

---

## Comparative Claims (HIGH PRIORITY)

### Performance Comparisons

**Patterns:**
- `outperforms (all|other|previous|existing|prior)`
- `better than [Model/Method]`
- `improves (on|upon|over) [Model/Method]`
- `surpasses (the|previous) state[- ]of[- ]the[- ]art`
- `compared to [Model], (achieves|shows|demonstrates)`

**Examples:**
- "outperforms CADD by 12%" - NEEDS CITATION
- "better than existing methods" - NEEDS CITATION
- "surpasses state-of-the-art" - NEEDS CITATION

### Qualitative Comparisons

**Patterns:**
- `(first|only) (model|method|approach) to`
- `unlike (previous|prior|earlier|other) (methods|approaches)`
- `(larger|smaller|faster|slower) than`
- `more (accurate|efficient|robust) than`

**Examples:**
- "the first model to achieve..." - NEEDS CITATION
- "unlike previous methods, this approach..." - MAY NEED CITATION

---

## Attribution Claims (HIGH PRIORITY)

### Direct Attribution

**Patterns:**
- `(introduced|proposed|developed|created) by [Author]`
- `[Author] (et al\.)? (showed|demonstrated|found|reported)`
- `according to [Author|Study]`
- `as (shown|demonstrated|reported) (by|in) [Author|Paper]`

**Examples:**
- "introduced by Vaswani et al." - SHOULD HAVE CITATION (verify it does)
- "as shown in the original paper" - MUST HAVE CITATION

### Temporal Attribution

**Patterns:**
- `(first|originally|initially) (introduced|proposed|developed) in [year]`
- `since [year]`
- `as of [year]`
- `pioneered in the [year]s`

**Examples:**
- "first introduced in 2017" - NEEDS CITATION
- "pioneered in the early 2000s" - NEEDS CITATION

---

## Mechanism Claims (MEDIUM PRIORITY)

### Biological Mechanisms

**Patterns:**
- `(regulates|controls|influences|affects) (expression|activity|function)`
- `(binds to|interacts with|activates|inhibits)`
- `(causes|leads to|results in) (disease|phenotype|effect)`
- `(functions as|acts as|serves as)`

**Examples:**
- "BRCA1 regulates DNA repair" - WELL KNOWN, may not need citation
- "enhancers regulate genes over 1Mb distances" - NEEDS CITATION
- "mutation causes loss of function" - DEPENDS on specificity

### Model Mechanisms

**Patterns:**
- `learns to (recognize|identify|predict|capture)`
- `captures (long-range|local|contextual) (dependencies|patterns|relationships)`
- `(attention|model) (focuses on|attends to|weights)`

**Examples:**
- "attention captures long-range dependencies" - GENERAL ML KNOWLEDGE, no citation
- "Enformer's attention focuses on promoter regions" - NEEDS CITATION (specific finding)

---

## Historical/Temporal Claims (HIGH PRIORITY)

### Firsts and Origins

**Patterns:**
- `(the )?first (to|that|which)`
- `originally (developed|designed|intended) (for|to)`
- `(pioneered|established|founded) (by|in|at)`
- `(landmark|seminal|foundational) (paper|work|study)`

**Examples:**
- "the first deep learning model for variant effect prediction" - NEEDS CITATION
- "originally designed for natural language processing" - NEEDS CITATION

### Historical Context

**Patterns:**
- `(emerged|arose|developed) (in|during|from) the [year]s`
- `(traditional|classical|conventional|early) (methods|approaches)`
- `(before|prior to) [Model/Method/Year]`
- `(evolution|history|development) of`

**Examples:**
- "emerged in the 2010s" - MAY NEED CITATION for specific claims
- "traditional GWAS methods" - GENERAL CONTEXT, usually no citation

---

## Claims That Usually DON'T Need Citations

### Definitions and Mathematical Facts

- "The softmax function normalizes scores to probabilities"
- "Cross-entropy measures the difference between distributions"
- "DNA consists of four nucleotides: A, T, G, C"

### Well-Established General Knowledge

- "Transformers use self-attention mechanisms"
- "Deep learning has transformed many fields"
- "The human genome contains approximately 3 billion base pairs"

### Logical Conclusions from Cited Work

- "Given the results from [@previous_citation], it follows that..."
- "This suggests that..." (when directly following cited evidence)

### Methodological Descriptions of Your Own Work

- "We fine-tuned the model on..."
- "Our approach uses..."
- "In this chapter, we examine..."

---

## Context-Dependent Cases

### Threshold for Citation Need

| Factor | Lower Threshold (needs citation) | Higher Threshold (maybe OK) |
|--------|----------------------------------|----------------------------|
| Specificity | Specific number/result | General statement |
| Novelty | First occurrence in text | Repeated reference |
| Controversy | Contested claim | Consensus view |
| Audience | Outside expertise | Within expertise |
| Centrality | Core argument | Peripheral mention |

### Examples of Judgment Calls

**"Transformers have 12 layers"**
- If discussing a specific model: NEEDS CITATION
- If describing general architecture: NO CITATION (it varies)

**"BERT was trained on Wikipedia"**
- First mention: NEEDS CITATION (specific training data)
- After BERT already cited: MAY NOT NEED (implicit reference)

**"Deep learning outperforms traditional methods"**
- As a general claim: TOO VAGUE, either cite or make specific
- With specific context: NEEDS CITATION to that comparison study

---

## Flagging Syntax

When flagging claims, use:

```
*[Citation Needed]*
```

For claims with clear citation targets:
```
*[Citation Needed: specific topic or suggested paper]*
```

For claims where citation exists but may be wrong:
```
*[Citation Check: @existing_cite may not support this claim]*
```

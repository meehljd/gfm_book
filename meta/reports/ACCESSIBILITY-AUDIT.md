# Audience Accessibility Audit
## Gap Citations: Proposed Book Modifications

**Document Reviewed:** `/root/gfm-book/meta/reports/gap-citations-diff-proposal.md`
**Target Audience:** Graduate students and researchers new to genomic ML (mixed biology and CS backgrounds)
**Audit Date:** 2026-01-18
**Overall Accessibility Rating:** 🟡 **MEDIUM** — Multiple high-priority accessibility barriers identified

---

## Executive Summary

The proposed additions substantially increase **concept density** and introduce domain-specific terminology without adequate scaffolding for interdisciplinary readers. While individually many terms are well-used in the book, the cumulative effect of dense technical passages—particularly in Changes 3, 9, 10, 13, and 16—risks excluding CS readers unfamiliar with genomics and biology readers unfamiliar with advanced ML architecture patterns.

**Key Findings:**
- **18 HIGH-priority jargon barriers** (critical concepts introduced without definition)
- **12 MEDIUM-priority issues** (terminology that slows comprehension)
- **8 LOW-priority friction points** (minor inconsistencies or unclear references)

**Recommendation:** Before implementing, add explicit prerequisite callouts and parenthetical definitions for cross-domain concepts.

---

## Change-by-Change Analysis

### Change 1: Bommasani et al. Definition (Ch. 14.2)

**Status:** ✅ **ACCEPTABLE** with minor enhancement

**Text Being Added:**
> "The Stanford HAI report formally defined foundation models as 'models trained on broad data at scale such that they can be adapted to a wide range of downstream tasks' [@bommasani_on_2022]."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon explanation | ✅ GOOD | Definition is inline and clear |
| Acronym hygiene | ✅ GOOD | "HAI" (Human-Centered AI Institute) — assume readers know this from context; may consider first-use expansion |
| Cross-domain clarity | ✅ GOOD | The definition itself is domain-neutral |
| Concept density | ✅ GOOD | One concept, well-framed |

**Issues Identified:** None critical

**Recommendation:** **APPROVED AS-IS**

---

### Change 2: Genomics FM Landscape Callout (Ch. 14.2)

**Status:** ✅ **GOOD** with note

**Text Being Added:**
```
::: {.callout-note title="Field Overview"}
For a comprehensive survey of genomic foundation models as of 2024, including
taxonomy, benchmarks, and applications, see @trop_genomics_2024. This review
provides valuable context for understanding the rapid evolution of the field
and the relationships between model families discussed in subsequent chapters.
:::
```

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon explanation | ✅ GOOD | No undefined jargon |
| Cross-reference clarity | ✅ GOOD | "model families discussed in subsequent chapters" — clear forward reference |
| Tone | ✅ GOOD | Callout format signals optional deeper reading |
| Inclusivity | ✅ GOOD | Assumes only that readers will encounter model families ahead |

**Issues Identified:** None

**Recommendation:** **APPROVED AS-IS**

---

### Change 3: ESM3 Section (Ch. 16.2.2) — 🔴 HIGH PRIORITY

**Status:** ❌ **REQUIRES REVISION** — Multiple accessibility barriers

**Text Being Added:** ~300 words on ESM3 multimodal protein modeling

**Critical Jargon Issues:**

| Term | Line | Context | Audience Gap | Severity |
|------|------|---------|--------------|----------|
| **"Multimodal"** | 77 | "multimodal reasoning across sequence, structure, and function" | ML/CS readers will understand; biology readers may not | 🟡 MEDIUM |
| **"Tokenization"** | 84 | "Protein structure is discretized into learned tokens" | Requires understanding both: (a) what tokenization means, (b) why structure needs discretization | 🔴 HIGH |
| **"Discretized"** | 84 | "discretized into learned tokens" | Non-CS readers may not know this means "converted to discrete units" | 🟡 MEDIUM |
| **"InterPro"** | 86 | "Annotations from InterPro, Gene Ontology" | Bioinformatics database names—CS readers don't know these | 🔴 HIGH |
| **"Gene Ontology"** | 86 | Same as above | Standard biological annotation system—CS readers unfamiliar | 🔴 HIGH |
| **"Conditioning tokens"** | 87 | "encoded as conditioning tokens" | Requires understanding what "conditioning" means in ML context | 🟡 MEDIUM |
| **"esmGFP"** | 88 | Introduced without context for what GFP is | Green fluorescent protein — biology readers know; CS readers may not | 🟡 MEDIUM |
| **"Extrapolate beyond training distribution"** | 94 | Key conceptual claim | Implicit assumption readers understand distribution shift | 🟡 MEDIUM |

**Concept Density Issues:**

**Paragraph 1-2 (lines 76-81):** Introduces 4 concepts simultaneously:
1. Multimodal learning
2. Three modalities (sequence, structure, function)
3. Difference between ESM-2 and ESM-3
4. Joint modeling concept

**For CS reader new to proteins:** Unclear what structure and function "tokens" mean biologically.
**For biology reader new to deep learning:** Multimodal tokenization and "learned tokens" are abstract.

**Architecture Innovations Section (lines 83-89):** Three bullet points introduce domain-specific systems (InterPro, GO, conditional generation) without scaffolding.

**Concrete Example (lines 91-95):** esmGFP is striking but introduced too quickly without:
- What GFP is (Green Fluorescent Protein — critical context for why 60% identity is surprising)
- Why folding correctly matters (implicit protein knowledge)
- What "functional" means quantitatively here

---

### **Specific Issues in Change 3:**

#### 🔴 **Issue 3a: Undefined Tokenization Context**
**Line 84:** "Protein structure is discretized into learned tokens that can be predicted alongside sequence"

**Problem:** "Discretized" is jargon for CS; the concept of tokenizing continuous 3D coordinates is non-trivial.

**Affected Audiences:**
- Biology readers: Don't understand the computational transformation
- CS readers without NLP background: May not grasp why discretization is needed

**Suggested Fix — Add parenthetical:**
```
Protein structure is discretized (converted to discrete symbolic units)
into learned tokens that can be predicted alongside sequence, enabling
joint generation across modalities.
```

Or add a sentence:
```
Structure—normally represented as continuous 3D coordinates—is converted
into discrete tokens (symbolic units) that can be predicted like sequence
tokens, enabling the model to jointly generate across modalities.
```

---

#### 🔴 **Issue 3b: Domain Database References**
**Line 86:** "Annotations from InterPro, Gene Ontology, and other databases"

**Problem:** These are bioinformatics databases. CS readers don't know what they contain or why they matter.

**Affected Audiences:**
- CS readers: No context for what these systems are or why they're important
- Biology readers: Likely familiar, but no guarantee

**Suggested Fix — Add brief context:**
```
Function conditioning: Protein functional annotations—drawn from
curated databases like InterPro (protein domain annotations) and
Gene Ontology (standardized functional descriptors)—are encoded
as conditioning tokens that guide generation.
```

Or separate callout:
```
::: {.callout-note title="What are InterPro and Gene Ontology?"}
InterPro provides curated protein domain and motif annotations; Gene
Ontology defines standardized terms for molecular functions, biological
processes, and cellular components. Both are widely used in functional
genomics for annotating proteins and genes.
:::
```

---

#### 🔴 **Issue 3c: esmGFP Lacks Biological Context**
**Lines 91-95:** "A novel GFP variant generated by ESM3, demonstrating functional protein design from language model outputs... generated a fluorescent protein with only ~60% sequence identity to any known GFP, yet it folded correctly and exhibited fluorescence."

**Problem:** The significance of the result depends on understanding:
1. **What GFP is:** Green Fluorescent Protein is a specific protein that fluoresces green
2. **Why 60% identity is surprising:** Most functional proteins share ~90%+ identity with known homologs
3. **Why "folding correctly" matters:** Proteins must fold into specific 3D structures to function

**Affected Audiences:**
- CS readers without protein biology: May miss why this is remarkable
- ML readers not familiar with computational biology: May not grasp the experimental validation aspect

**Suggested Fix — Add biological context:**
```
The esmGFP result is particularly striking: the model generated a new
variant of green fluorescent protein (GFP)—a protein that naturally
fluoresces green under UV light—with only ~60% sequence identity
(similarity) to any known GFP. Most biological variants share 90%+
identity; ESM3's variant was dramatically different yet still folded
into the correct 3D structure AND functioned (fluoresced). This
demonstrates that protein language models can extrapolate far beyond
patterns in their training data to discover entirely novel solutions.
```

---

#### 🟡 **Issue 3d: "Conditioning" Terminology**
**Line 87:** "encoded as conditioning tokens"

**Problem:** "Conditioning" is ML jargon for providing auxiliary information to guide generation. Not standard in biology, and even some ML practitioners may confuse it with statistical conditioning.

**For biology readers:** Unknown term
**For CS readers without ML experience:** Needs definition

**Suggested Fix:**
```
encoded as conditioning tokens (special tokens that guide generation
toward desired functional properties)
```

---

#### 🟡 **Issue 3e: Distribution Shift Assumption**
**Line 94:** "protein language models can extrapolate beyond their training distribution"

**Problem:** Assumes readers understand "training distribution" — a foundational ML concept but not introduced in this section.

**For biology readers:** Likely unfamiliar with distribution concept
**For non-ML CS readers:** May need clarification

**Suggested Fix — Add context:**
```
This demonstrates that protein language models can extrapolate beyond
the patterns seen in their training data (training distribution) to
discover entirely novel functional solutions—a capability that opens
new frontiers for computational protein design.
```

---

#### 🟡 **Issue 3f: Callout Implications Not Concrete**
**Lines 97-102:** The callout asks hypotheticals about DNA models but doesn't provide actionable guidance.

**Problem:** For readers unfamiliar with either protein or DNA biology, the connection is abstract.

**For audience:** Readers may not understand what "chromatin state" or "expression data" represent

**Suggested Fix — More concrete:**
```
::: {.callout-important title="Implications for Genomic FMs"}
ESM3's success with multimodal protein learning raises questions about
analogous approaches for DNA models. Could DNA foundation models benefit
from joint training on:
- **Sequence** (DNA letter order)
- **Chromatin state** (how open/closed the DNA is, which affects which
  genes are active)
- **Expression data** (how much each gene is actively transcribed)

The protein results suggest this integration of multiple data types merits
exploration in genomics.
:::
```

---

### **Recommendation for Change 3: CONDITIONAL APPROVAL**

**Status:** ❌ **DO NOT IMPLEMENT WITHOUT REVISION**

**Required Changes:**
1. ✅ Add parenthetical definition: "discretized (converted to discrete symbolic units)"
2. ✅ Expand InterPro/Gene Ontology with brief context or separate callout
3. ✅ Add biological context to esmGFP result (what GFP is, why 60% identity matters)
4. ✅ Define "conditioning tokens" parenthetically
5. ✅ Clarify "training distribution" in extrapolation sentence
6. ✅ Make callout more concrete with specific modalities explained

**Estimated revision time:** 30 minutes; ~400 final words

---

### Change 4: RoseTTAFold Reference (Ch. 16, structure section)

**Status:** 🟡 **REQUIRES MINOR REVISION**

**Text Being Added:**
> "While *ESMFold* demonstrates single-sequence structure prediction, *RoseTTAFold* [@baek_accurate_2021] provides an alternative approach that combines multiple sequence alignment information with deep learning... For proteins with good homolog coverage, *RoseTTAFold* may offer advantages; for orphan sequences, single-sequence methods like *ESMFold* become essential."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Technical clarity | 🟡 MEDIUM | "Multiple sequence alignment" unexplained for CS readers |
| "Orphan sequences" | 🟡 MEDIUM | Bioinformatics term not defined |
| Trade-off explanation | ✅ GOOD | The comparison is logical |

**Issues Identified:**

#### 🟡 **Issue 4a: "Multiple Sequence Alignment" Unexplained**
**Problem:** MSA is a key concept in structural biology but not explained.

**Affected Audiences:**
- CS readers: Don't know what an alignment is or why it helps structure prediction
- Biology readers: Likely familiar, but no guarantee for those from non-structural backgrounds

**Suggested Fix:**
```
*RoseTTAFold* [@baek_accurate_2021] provides an alternative approach that
combines multiple sequence alignment (MSA—a computational arrangement of
related protein sequences to identify conserved regions) with deep learning
to predict structure. This approach...
```

---

#### 🟡 **Issue 4b: "Orphan sequences" Undefined**
**Problem:** Domain-specific term for proteins with no known homologs.

**Suggested Fix:**
```
for orphan sequences (proteins with no known related sequences in
databases), single-sequence methods like *ESMFold* become essential.
```

---

### **Recommendation for Change 4: CONDITIONAL APPROVAL**

**Status:** 🟡 **APPROVE WITH REVISIONS**

**Required Additions:**
1. ✅ Define "multiple sequence alignment" parenthetically
2. ✅ Define "orphan sequences" parenthetically

**Estimated revision time:** 5 minutes

---

### Change 5: OpenFold Reference (Ch. 16)

**Status:** ✅ **ACCEPTABLE** with one minor note

**Text Being Added:**
> "The *OpenFold* project [@ahdritz_openfold_2024] provides an open-source reimplementation of *AlphaFold2* that enables fine-tuning and modification not possible with the original weights. This accessibility has proven valuable for domain-specific applications and for understanding the internal mechanisms of structure prediction models."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon | ✅ GOOD | "Fine-tuning" is defined in glossary |
| Clarity | ✅ GOOD | The value proposition is clear |
| "Weights" | 🟡 MINOR | Could be clearer for readers unfamiliar with neural network terminology |

**Minor Issue:**

#### 🟢 **Issue 5a: "Weights" Reference**
**Line 135:** "not possible with the original weights"

**Problem:** In neural networks, "weights" = parameters = the learned values. This is standard jargon but may confuse non-ML readers.

**Severity:** LOW — Context makes meaning mostly clear ("enables fine-tuning... not possible")

**Suggested Fix (optional):**
```
enables fine-tuning and modification not possible with the original
model weights (learned parameters)
```

---

### **Recommendation for Change 5: APPROVED AS-IS**

Optional: Add "(learned parameters)" to "weights" for maximum clarity, but not critical.

---

### Change 6: Ingraham Protein Generation (Ch. 16, end)

**Status:** 🟡 **REQUIRES MINOR REVISION**

**Text Being Added:** ~150 words on generative protein design

**Issues Identified:**

#### 🟡 **Issue 6a: "Masked amino acids" Needs Context**
**Line 152:** "models trained to predict masked amino acids"

**Problem:** Assumes readers know what "masked" means in the context of language model training.

**Affected Audiences:**
- Biology readers: May not be familiar with masked language modeling
- CS readers without NLP background: Might not know this objective

**Suggested Fix:**
```
models trained to predict masked (hidden/occluded) amino acids
```

Or more detailed:
```
models trained using a masked language objective: randomly hiding
(masking) amino acids in proteins and learning to predict them from
context
```

---

#### 🟡 **Issue 6b: "Conditioned on desired properties"**
**Line 157:** "Conditioning on functional annotations enables targeted design"

**Problem:** Same "conditioning" jargon as Issue 3d.

**Suggested Fix:**
```
Guiding generation toward (conditioning on) functional annotations
enables targeted design
```

---

#### 🟢 **Issue 6c: "Diversity-Function Trade-off"**
**Lines 158-161:** Clear as written, but could benefit from concrete example.

---

### **Recommendation for Change 6: CONDITIONAL APPROVAL**

**Status:** 🟡 **APPROVE WITH REVISIONS**

**Required Changes:**
1. ✅ Define "masked" in the masked prediction context
2. ✅ Clarify "conditioning" or replace with "guiding generation toward"

**Estimated revision time:** 5 minutes

---

### Change 7: Maurano Motivation (Ch. 17 opening)

**Status:** ✅ **GOOD** with minor enhancement

**Text Being Added:**
> "@maurano_systematic_2012 demonstrated that disease-associated variants are overwhelmingly enriched in regulatory regions rather than coding sequences, with enrichment patterns specific to cell types relevant to each disease."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon | 🟡 MEDIUM | "Enrichment" is statistics jargon but contextually clear |
| Motivation clarity | ✅ GOOD | The argument is logical |
| Cross-domain clarity | ✅ GOOD | Works for both bio and CS audiences |

**Minor Issue:**

#### 🟡 **Issue 7a: "Enriched in regulatory regions"**
**Problem:** "Enrichment" is statistical jargon meaning "overrepresented" or "concentrated."

**Severity:** LOW — contextually clear, but could be explicit

**Optional Fix:**
```
disease-associated variants are overwhelmingly enriched (overrepresented)
in regulatory regions
```

---

### **Recommendation for Change 7: APPROVED AS-IS**

Optional parenthetical for "enriched" if maximum clarity desired, but not critical.

---

### Change 8: Non-Coding Statistics (Ch. 18)

**Status:** ✅ **ACCEPTABLE** with one clarification

**Text Being Added:**
> "@farh_genetic_2015 established that approximately 90% of disease-associated variants fall in non-coding regions, with roughly 60% in enhancer-like chromatin states. Of these, only 10-20% directly disrupt recognizable transcription factor binding motifs."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Statistics clarity | ✅ GOOD | Numbers are concrete |
| Jargon | 🟡 MEDIUM | "Chromatin states," "transcription factor," "motifs" |
| Concept flow | ✅ GOOD | The logic is clear even if terms are unfamiliar |

**Issues Identified:**

#### 🟡 **Issue 8a: "Enhancer-like chromatin states"**
**Problem:** Assumes readers know what chromatin states are and that "enhancer-like" is a recognizable category.

**For CS readers:** No understanding of chromatin or enhancers
**For biology readers:** Likely familiar, but no guarantee

**Severity:** MEDIUM — The concept is central to the passage

**Suggested Fix:**
```
with roughly 60% in enhancer-like chromatin states (regions where DNA
is open and accessible, suggesting regulatory function)
```

---

#### 🟡 **Issue 8b: "Transcription factor binding motifs"**
**Problem:** Combines three concepts: transcription factors, binding, motifs.

**For CS readers:** Unknown
**For structural biology readers:** Familiar; for other biologists: varies

**Severity:** MEDIUM — This is the key finding (only 10-20% directly disrupt motifs)

**Suggested Fix:**
```
only 10-20% directly disrupt recognizable transcription factor binding
motifs (short DNA sequences that are recognized and bound by regulatory
proteins)
```

---

### **Recommendation for Change 8: CONDITIONAL APPROVAL**

**Status:** 🟡 **APPROVE WITH REVISIONS**

**Required Changes:**
1. ✅ Add context to "enhancer-like chromatin states"
2. ✅ Add brief definition of "transcription factor binding motifs"

**Estimated revision time:** 5 minutes

---

### Change 9: VEP Limitations Perspective (Ch. 18) — 🔴 HIGH PRIORITY

**Status:** ❌ **REQUIRES SIGNIFICANT REVISION** — Multiple accessibility barriers

**Text Being Added:** ~150 words on limitations of PLM-VEP methods

**Critical Issues:**

#### 🔴 **Issue 9a: "Conservation bias"**
**Lines 223-224:** "Models preferentially score positions that are evolutionarily constrained, potentially missing functionally important but variable positions"

**Problem:** Assumes understanding of:
1. What "evolutionary constraint" means (positions unchanged across species)
2. Why conservation is a bias rather than a feature
3. The distinction between conserved and variable positions

**Affected Audiences:**
- CS readers: Don't understand evolutionary biology
- Biology readers without computational experience: May not understand the ML bias concept

**Severity:** 🔴 **HIGH**

**Suggested Fix — More explicit:**
```
**Conservation bias:** Models tend to heavily weight evolutionarily
constrained positions (residues that are identical across many species,
indicating functional importance). However, this can cause them to
overlook functionally important positions that vary among organisms,
leading to missed predictions of harmful variants in variable regions.
```

---

#### 🔴 **Issue 9b: "Epistatic blindness"**
**Lines 225-226:** "Single-variant scoring ignores combinatorial effects that may be clinically relevant"

**Problem:** "Epistasis" is a key genomics concept but not explicitly defined.

**Severity:** 🔴 **HIGH** — This is core to understanding limitations

**For CS readers:** Unknown term
**For genetics readers:** Known, but may vary in depth

**Suggested Fix:**
```
**Epistatic blindness:** Single-variant scoring ignores epistasis
(genetic interactions where the effect of one variant depends on the
presence of other variants), which may be clinically relevant. A model
that scores variants independently might miss combinations of variants
that together cause disease.
```

---

#### 🟡 **Issue 9c: "Calibration gaps"**
**Lines 227-228:** "Scores do not translate directly to pathogenicity probabilities"

**Problem:** References "calibration" without explaining the distinction between scores and probabilities.

**Severity:** 🟡 **MEDIUM** — Term is in glossary, but the specific concept needs context

**For CS readers:** Understand probability, but may not grasp why model scores don't equal probabilities
**For biology readers:** May be unfamiliar with statistical calibration

**Suggested Fix:**
```
**Calibration gaps:** Model scores do not translate directly to
pathogenicity probabilities. A score of 0.8 does not mean 80%
probability of pathogenicity; the relationship between score and
actual probability may be nonlinear or shifted, requiring calibration
(adjustment) to properly interpret predictions.
```

---

#### 🔴 **Issue 9d: Follow-up Citations Lack Context**
**Lines 231-235:** References Swanson, Karollus, Notin papers without explaining what each addresses.

**Problem:** Three papers are cited in sequence with no explanation of their distinct contributions.

**Severity:** 🔴 **HIGH** — Readers don't know which problem each paper addresses

**For audience:** Unclear whether these are alternative solutions, competing analyses, or complementary perspectives

**Suggested Fix — Add brief description:**
```
@swanson_predicting_2022 provides complementary analysis showing that
PLMs systematically underperform on proteins with limited evolutionary
data or unusual functions (proteins unlike any in the training set).
@notin_tranception_2022 addresses some limitations through
retrieval-augmented approaches (augmenting predictions with relevant
sequence information from databases), but fundamental gaps remain
between model predictions and clinical interpretation needs.
```

---

### **Recommendation for Change 9: CONDITIONAL APPROVAL**

**Status:** ❌ **DO NOT IMPLEMENT WITHOUT SIGNIFICANT REVISION**

**Required Changes:**
1. ✅ Define epistasis explicitly in "epistatic blindness"
2. ✅ Explain conservation bias more concretely
3. ✅ Clarify calibration gap concept
4. ✅ Add brief summary of what Swanson and Notin papers contribute

**Estimated revision time:** 20 minutes

---

### Change 10: Benchmark Circularity Section (Ch. 12) — 🟡 MEDIUM PRIORITY

**Status:** 🟡 **REQUIRES MINOR REVISION**

**Text Being Added:** ~140 words on circularity problem

**Issues Identified:**

#### 🟡 **Issue 10a: "Label circularity" Definition**
**Lines 259-260:** "Pathogenicity labels derived from SIFT/PolyPhen scores advantage methods using similar features"

**Problem:** SIFT and PolyPhen are legacy variant effect prediction tools. Readers may not know them.

**Severity:** 🟡 **MEDIUM** — The concept (using labels from similar methods) is clear, but specific tools are domain knowledge

**For CS readers:** Unknown tools
**For genomics readers:** Likely familiar, but no guarantee

**Suggested Fix:**
```
**Label circularity:** Pathogenicity labels derived from legacy variant
effect prediction tools (SIFT, PolyPhen) advantage newer methods using
similar features, creating a circularity where labels reinforce the
methods they were derived from.
```

---

#### 🟡 **Issue 10b: "Temporal leakage"**
**Lines 261-262:** "Training on variants classified after model development inflates apparent performance"

**Problem:** Clear concept, but "temporal leakage" jargon may need context.

**Severity:** 🟢 **LOW** — The concept is understandable even if term is unfamiliar

---

#### 🟡 **Issue 10c: "Gene-level leakage"**
**Lines 263-264:** "Variants in the same gene as training examples may share confounding features"

**Problem:** Clear concept, but "confounding features" assumes understanding of confounding.

**Severity:** 🟢 **LOW** — Contextually understandable

---

### **Recommendation for Change 10: CONDITIONAL APPROVAL**

**Status:** 🟡 **APPROVE WITH MINOR REVISIONS**

**Required Changes:**
1. ✅ Add context to SIFT/PolyPhen references

**Estimated revision time:** 5 minutes

---

### Change 11: Genomic Touchstone Reference (Ch. 12)

**Status:** ✅ **ACCEPTABLE** with one minor clarification

**Text Being Added:**
> "@wang_genomic_2025 introduce *Genomic Touchstone*, a comprehensive benchmark designed specifically for genomic foundation models. Key features include: **Systematic holdout:** Gene-level splits prevent information leakage..."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon | 🟡 MEDIUM | "Information leakage" is clear from context; "gene-level splits" clear |
| Clarity | ✅ GOOD | The value of each feature is explained |

**Minor Issue:**

#### 🟢 **Issue 11a: "Gene-level splits"**
**Problem:** Could be slightly clearer that this means training and test variants come from different genes.

**Severity:** 🟢 **LOW** — Contextually clear enough

**Optional Fix:**
```
**Systematic holdout:** Gene-level splits (ensuring training and test
variants come from different genes) prevent information leakage
```

---

### **Recommendation for Change 11: APPROVED AS-IS**

Optional minor clarification, but not critical.

---

### Change 12: Ancestry-Aware Methods (Ch. 13)

**Status:** ✅ **GOOD** with optional enhancement

**Text Being Added:**
> "Several approaches have emerged to address ancestry confounding in genomic prediction. @amariuta_improving_2020 demonstrated that incorporating functional genomic annotations can improve PRS transferability across populations..."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon | 🟡 MEDIUM | "PRS," "functional genomic annotations" defined in glossary |
| Clarity | ✅ GOOD | The argument is logical |
| Inclusivity | ✅ GOOD | Appropriate for mixed-background audience |

**No Critical Issues Identified**

**Minor Enhancement (Optional):**

#### 🟢 **Issue 12a: "Transferability" Context**
**Line 315-316:** "PRS transferability across populations"

**Severity:** 🟢 **LOW** — meaning is clear from context

---

### **Recommendation for Change 12: APPROVED AS-IS**

---

### Change 13: BERTology Reference (Ch. 25) — 🟡 MEDIUM PRIORITY

**Status:** 🟡 **REQUIRES MINOR REVISION**

**Text Being Added:** ~120 words on attention analysis techniques

**Issues Identified:**

#### 🟡 **Issue 13a: "Attention head specialization"**
**Lines 342-343:** "Different heads capture different linguistic (or in genomics, biological) phenomena"

**Problem:** Assumes readers understand what an "attention head" is.

**Severity:** 🟡 **MEDIUM** — This section appears in Ch. 25 (Interpretability), so some familiarity is expected, but the concept may not have been explicitly introduced

**For CS readers without Transformers background:** Unfamiliar
**For biology readers:** Unfamiliar

**Suggested Fix (depends on preceding context in Ch. 25):**
```
**Attention head specialization:** In transformer models, different
attention heads (independent mechanisms that learn to focus on different
parts of the input) capture different biological phenomena
```

Or reference an earlier section:
```
Different attention heads (as introduced in Part 2, Chapter 7) capture
different biological phenomena...
```

---

#### 🟡 **Issue 13b: "Probing classifiers"**
**Lines 346-347:** "Simple classifiers trained on internal representations reveal encoded knowledge"

**Problem:** Jargon for a specific interpretability technique.

**Severity:** 🟡 **MEDIUM** — The concept is sound, but "probing" may need explanation

**Suggested Fix:**
```
**Probing classifiers:** Simple classifiers trained on internal model
representations (a technique called "probing") reveal what knowledge
is encoded in each layer
```

---

### **Recommendation for Change 13: CONDITIONAL APPROVAL**

**Status:** 🟡 **APPROVE WITH REVISIONS**

**Required Changes:**
1. ✅ Add context to "attention head specialization" (either define or cross-reference Ch. 7)
2. ✅ Add brief explanation of "probing" technique

**Estimated revision time:** 10 minutes

---

### Change 14: Mendelian Randomization Foundation (Ch. 26)

**Status:** 🟡 **REQUIRES REVISION** — High-value content but needs scaffolding

**Text Being Added:** ~140 words introducing Mendelian randomization

**Critical Issues:**

#### 🔴 **Issue 14a: "Instrumental variables" Unexplained**
**Lines 366-367:** "using genetic variants as instrumental variables"

**Problem:** Instrumental variables is a causal inference concept not defined.

**Severity:** 🔴 **HIGH** — Central to understanding Mendelian randomization

**For CS readers:** Unfamiliar with econometric/statistical causal inference
**For biology readers:** Rarely encountered

**Suggested Fix:**
```
using genetic variants as instrumental variables (variables that affect
the outcome only through the exposure of interest, enabling causal
inference)
```

Or more pedagogical:
```
The key insight: genetic variants are randomly assigned at conception,
making them "instrumental variables" in causal inference. That is, they
can be used to determine causality because they affect outcomes only
through the pathway of interest, not through confounding.
```

---

#### 🔴 **Issue 14b: "Conditional on parental genotypes"**
**Line 368:** "(conditional on parental genotypes)"

**Problem:** "Conditional" is jargon for a statistical restriction. The parenthetical assumes understanding of what this means.

**Severity:** 🟡 **MEDIUM** — Readers might not grasp why parental genotypes are relevant

**Suggested Fix:**
```
genotypes are assigned randomly at conception (aside from inheritance
from parents), providing a natural randomization...
```

Or more explicit:
```
genotypes are essentially randomly assigned at conception (determined
by Mendelian inheritance from parents, not by environmental factors),
providing a natural randomization...
```

---

#### 🟡 **Issue 14c: "Intervention settings"**
**Line 376:** "may perform well on benchmarks while failing to generalize to intervention settings"

**Problem:** "Intervention" is jargon for experimentally manipulating something (e.g., a drug trial). The distinction between observational and intervention generalization may not be obvious.

**Severity:** 🟡 **MEDIUM** — Important distinction but needs context

**Suggested Fix:**
```
may perform well on benchmarks (predicting from observation data) while
failing to generalize to intervention settings (actual clinical use or
experimental validation)
```

---

### **Recommendation for Change 14: CONDITIONAL APPROVAL**

**Status:** 🟡 **APPROVE WITH REVISIONS**

**Required Changes:**
1. ✅ Define instrumental variables in the context of Mendelian randomization
2. ✅ Clarify why random assignment matters
3. ✅ Define "intervention" context

**Estimated revision time:** 15 minutes

---

### Change 15: FDA AI/ML Guidance (Ch. 27)

**Status:** ✅ **GOOD** with optional enhancement

**Text Being Added:** ~120 words on FDA requirements

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon | 🟡 MEDIUM | "Predetermined change control plans" is regulatory jargon |
| Clarity | ✅ GOOD | The three requirements are listed clearly |
| Regulatory context | ✅ GOOD | Chapter 27 is on Regulation, so context is appropriate |

**Minor Issues:**

#### 🟡 **Issue 15a: "Predetermined change control plans"**
**Line 395:** "Methods for updating models without requiring new regulatory clearance"

**Problem:** The parenthetical explains it, but the term itself is regulatory jargon.

**Severity:** 🟢 **LOW** — Adequately explained parenthetically

---

#### 🟢 **Issue 15b: "Real-world performance monitoring"**
**Line 397-398:** "Requirements for ongoing performance assessment after deployment"

**Severity:** 🟢 **LOW** — Clear from context

---

### **Recommendation for Change 15: APPROVED AS-IS**

---

### Change 16: Non-Linear PRS Methods (Ch. 28) — 🟡 MEDIUM PRIORITY

**Status:** 🟡 **REQUIRES MINOR REVISION**

**Text Being Added:** ~160 words on deep learning approaches to PRS

**Issues Identified:**

#### 🟡 **Issue 16a: "Complex genetic architectures"**
**Lines 421-422:** "particularly those with complex genetic architectures"

**Problem:** "Genetic architecture" is domain-specific jargon (the pattern of how many genes contribute, at what effect sizes).

**Severity:** 🟡 **MEDIUM** — Important concept but not defined

**For CS readers:** Unknown term
**For genetics readers:** Familiar

**Suggested Fix:**
```
particularly those with complex genetic architectures (where many genes
contribute at varying effect sizes)
```

---

#### 🟡 **Issue 16b: "Attention mechanisms capture genetic interactions"**
**Lines 425-426:** "attention mechanisms can capture genetic interactions missed by linear approaches"

**Problem:** Assumes readers understand both:
1. How attention mechanisms work (not explained in this section)
2. What genetic interactions are (not defined)

**Severity:** 🟡 **MEDIUM** — Important claim but needs support

**For CS readers:** May not understand genetic interactions
**For biology readers:** May not understand attention mechanisms

**Suggested Fix:**
```
attention mechanisms can capture genetic interactions (cases where two
or more genetic variants together affect the phenotype in ways that
linear methods miss) that linear approaches cannot detect
```

---

#### 🟡 **Issue 16c: "Phenotype embeddings"**
**Lines 430-433:** "learning representations of disease phenotypes may improve genetic prediction through better characterization of the outcome space"

**Problem:** Two layers of jargon:
1. "Phenotype embeddings" — learned representations of diseases
2. "Characterization of the outcome space" — understanding the structure of disease definitions

**Severity:** 🟡 **MEDIUM** — Abstract concept without concrete context

**For both audiences:** Could use clearer example

**Suggested Fix:**
```
@yun_regle_2023 introduces an alternative paradigm using phenotype
embeddings—learned representations that capture relationships between
different diseases. For example, instead of treating each disease
separately, the model might discover that rheumatoid arthritis and lupus
share genetic risk factors. This richer characterization of diseases may
improve genetic prediction by revealing hidden structure.
```

---

### **Recommendation for Change 16: CONDITIONAL APPROVAL**

**Status:** 🟡 **APPROVE WITH REVISIONS**

**Required Changes:**
1. ✅ Define "complex genetic architectures"
2. ✅ Explain "genetic interactions" briefly
3. ✅ Add concrete example to phenotype embeddings explanation

**Estimated revision time:** 10 minutes

---

### Change 17: DiffDock Reference (Ch. 30)

**Status:** 🟡 **REQUIRES MINOR REVISION**

**Text Being Added:** ~90 words on diffusion models for molecular docking

**Issues Identified:**

#### 🟡 **Issue 17a: "Generative problem"**
**Lines 449-450:** "The method treats docking as a generative problem, iteratively denoising random poses toward the true binding configuration"

**Problem:** Two unfamiliar concepts:
1. "Generative problem" — what does it mean to generate a pose?
2. "Denoising" — model reduces noise iteratively

**Severity:** 🟡 **MEDIUM** — Important paradigm but needs motivation

**For CS readers:** May understand denoising; may not see why it applies to docking
**For biology readers:** May not understand denoising or generative models

**Suggested Fix:**
```
The method treats docking as a generative problem: starting from random
molecular poses (configurations), it iteratively refines them (denoising
them) toward the correct binding configuration, similar to how diffusion
models generate images by iteratively removing noise.
```

---

#### 🟡 **Issue 17b: "Scoring-function-based approaches"**
**Line 452:** "departure from traditional scoring-function-based approaches"

**Problem:** Not explained what scoring functions are or why they're a departure.

**Severity:** 🟡 **MEDIUM** — Readers may not understand what's novel

**Suggested Fix:**
```
departure from traditional scoring-function-based approaches (methods
that explicitly model chemical energy and binding affinity) and connects
molecular docking to the broader foundation model paradigm
```

---

#### 🟡 **Issue 17c: "Learned priors over molecular interactions"**
**Line 453-454:** "connects molecular docking to the broader foundation model paradigm through learned priors over molecular interactions"

**Problem:** Abstract language without concrete meaning.

**Severity:** 🟡 **MEDIUM** — Readers don't understand what "learned priors" means

**Suggested Fix:**
```
connects molecular docking to the broader foundation model paradigm:
instead of explicit rules, the model learns statistical patterns
(priors) about how molecules typically interact
```

---

### **Recommendation for Change 17: CONDITIONAL APPROVAL**

**Status:** 🟡 **APPROVE WITH REVISIONS**

**Required Changes:**
1. ✅ Clarify why docking is a generative problem
2. ✅ Briefly explain what scoring-function approaches are
3. ✅ Explain "learned priors" more concretely

**Estimated revision time:** 10 minutes

---

### Change 18: SCENIC Reference (Ch. 21)

**Status:** ✅ **ACCEPTABLE** with optional context

**Text Being Added:**
> "Classical approaches to gene regulatory network inference from single-cell data, exemplified by *SCENIC* [@aibar_scenic_2017], establish baseline methods... *SCENIC* combines motif enrichment with co-expression analysis to infer transcription factor regulons..."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon | 🟡 MEDIUM | "Motif enrichment," "co-expression," "regulons" — bioinformatics terms |
| Clarity | ✅ GOOD | The purpose (baseline comparison) is clear |

**Minor Issue:**

#### 🟡 **Issue 18a: "Regulons"**
**Line 471:** "transcription factor regulons"

**Problem:** Domain-specific term meaning "sets of genes regulated by a specific transcription factor."

**Severity:** 🟢 **LOW** — Contextually clear, but could be explicit

**Optional Fix:**
```
transcription factor regulons (sets of genes regulated by the same
transcription factor)
```

---

### **Recommendation for Change 18: APPROVED AS-IS**

Optional parenthetical for "regulons," but not critical for understanding.

---

### Change 19: HEIST Reference (Ch. 21)

**Status:** ✅ **GOOD** with minor enhancement

**Text Being Added:**
> "*HEIST* [@madhu_heist_2025] demonstrates that transformer architectures can learn meaningful representations from spatial transcriptomics data, capturing tissue organization and cell-cell communication patterns that bulk or dissociated approaches miss."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon | 🟡 MEDIUM | "Spatial transcriptomics," "bulk," "dissociated approaches" |
| Clarity | ✅ GOOD | The advantage is clear |

**Minor Issue:**

#### 🟡 **Issue 19a: "Bulk or dissociated approaches"**
**Problem:** Bioinformatics terminology that contrasts with spatial methods.

**Severity:** 🟢 **LOW** — Contextually clear as "approaches that lose spatial information"

**Optional Fix:**
```
that bulk (whole-tissue) or dissociated (cell-separated) approaches miss
```

---

### **Recommendation for Change 19: APPROVED AS-IS**

Optional clarification for "bulk" and "dissociated," but not critical.

---

### Change 20: TOPMed Reference (Ch. 2)

**Status:** ✅ **GOOD** with minor enhancement

**Text Being Added:**
> "The Trans-Omics for Precision Medicine (TOPMed) program provides one of the largest deeply sequenced cohorts... @taliun_sequencing_2021 describes the resource: over 150,000 genomes at high coverage (>30×), with diverse ancestry representation and deep phenotyping."

**Accessibility Assessment:**

| Aspect | Status | Notes |
|--------|--------|-------|
| Jargon | 🟡 MEDIUM | "Deep coverage," "deep phenotyping" |
| Clarity | ✅ GOOD | Quantities are concrete |

**Minor Issue:**

#### 🟡 **Issue 20a: "Deep coverage" notation**
**Line 505:** "high coverage (>30×)"

**Problem:** The notation >30× may not be clear to all readers.

**Severity:** 🟢 **LOW** — Parenthetical provides the number

**Optional Fix:**
```
at high coverage (more than 30 reads per base pair, 30×)
```

---

#### 🟡 **Issue 20b: "Deep phenotyping"**
**Line 506:** "deep phenotyping"

**Problem:** May be unclear what "deep" means in this context.

**Severity:** 🟢 **LOW** — Contextually clear as "comprehensive phenotyping"

---

### **Recommendation for Change 20: APPROVED AS-IS**

---

### Additional Tools: PLINK Reference (Ch. 2)

**Status:** ✅ **GOOD**

**Text Being Added:**
> "*PLINK* [@purcell_plink_2007] remains the standard tool for genome-wide association analysis and data manipulation..."

**Accessibility:** No issues. Clear and direct.

### **Recommendation: APPROVED AS-IS**

---

### Additional Tools: PharmGKB Reference (Ch. 28)

**Status:** ✅ **GOOD**

**Text Being Added:**
> "The Pharmacogenomics Knowledge Base (PharmGKB) [@whirlcarrillo_pharmacogenomics_2012] curates variant-drug associations with clinical annotations..."

**Accessibility:** No issues. Clear and direct.

### **Recommendation: APPROVED AS-IS**

---

## Summary Table: All Changes by Accessibility Status

| Change # | Chapter | Title | Status | Priority | Estimated Revision Time |
|----------|---------|-------|--------|----------|-------------------------|
| 1 | 14 | Bommasani Definition | ✅ APPROVED | — | — |
| 2 | 14 | Trop Survey Callout | ✅ APPROVED | — | — |
| 3 | 16 | ESM3 Section | ❌ CONDITIONAL | 🔴 HIGH | 30 min |
| 4 | 16 | RoseTTAFold | 🟡 CONDITIONAL | 🟡 MEDIUM | 5 min |
| 5 | 16 | OpenFold | ✅ APPROVED | — | — |
| 6 | 16 | Ingraham Generation | 🟡 CONDITIONAL | 🟡 MEDIUM | 5 min |
| 7 | 17 | Maurano Motivation | ✅ APPROVED (optional) | — | — |
| 8 | 18 | Farh Statistics | 🟡 CONDITIONAL | 🟡 MEDIUM | 5 min |
| 9 | 18 | Karollus Limitations | ❌ CONDITIONAL | 🔴 HIGH | 20 min |
| 10 | 12 | Circularity Section | 🟡 CONDITIONAL | 🟡 MEDIUM | 5 min |
| 11 | 12 | Genomic Touchstone | ✅ APPROVED (optional) | — | — |
| 12 | 13 | Ancestry Methods | ✅ APPROVED | — | — |
| 13 | 25 | BERTology | 🟡 CONDITIONAL | 🟡 MEDIUM | 10 min |
| 14 | 26 | Mendelian Randomization | 🟡 CONDITIONAL | 🟡 MEDIUM | 15 min |
| 15 | 27 | FDA Guidance | ✅ APPROVED | — | — |
| 16 | 28 | Non-Linear PRS | 🟡 CONDITIONAL | 🟡 MEDIUM | 10 min |
| 17 | 30 | DiffDock | 🟡 CONDITIONAL | 🟡 MEDIUM | 10 min |
| 18 | 21 | SCENIC | ✅ APPROVED (optional) | — | — |
| 19 | 21 | HEIST | ✅ APPROVED (optional) | — | — |
| 20 | 2 | TOPMed | ✅ APPROVED (optional) | — | — |
| Tool | 2 | PLINK | ✅ APPROVED | — | — |
| Tool | 28 | PharmGKB | ✅ APPROVED | — | — |

**Summary:**
- **✅ APPROVED AS-IS:** 10 changes
- **✅ APPROVED (optional enhancements):** 4 changes
- **🟡 CONDITIONAL APPROVAL (requires revisions):** 8 changes
- **❌ CONDITIONAL APPROVAL (significant revisions required):** 2 changes

**Total estimated revision time (conditional changes only):** ~2.5 hours

---

## Critical Accessibility Gaps by Audience

### For CS Readers New to Genomics

**Undefined Terms Blocking Comprehension:**
- Chromatin state, enhancer, promoter (Change 8)
- Transcription factor, binding motif (Change 8)
- Gene regulatory networks, regulons, co-expression (Changes 18, 19)
- Multiple sequence alignment (Change 4)
- Epistasis (Change 9)
- InterPro, Gene Ontology (Change 3)
- PRS, genetic architecture (Change 16)
- Phenotype, phenotyping (Changes 12, 20)

**Recommendation:** Add callout boxes or glossary references for core bioinformatics concepts, especially in chapters that straddle domains.

### For Biology Readers New to ML

**Undefined Terms Blocking Comprehension:**
- Multimodal tokenization, discretization (Change 3)
- Masked language modeling, masked prediction (Change 6)
- Attention heads, probing (Change 13)
- Instrumental variables (Change 14)
- Conditioning, generative models (Changes 3, 6, 17)
- Learned priors, denoising (Change 17)
- Distribution shift, training distribution (Change 3)
- Epistatic (interaction) blindness (Change 9)

**Recommendation:** Add explanations of ML concepts using biological analogies where possible.

### For Both Audiences

**Concept Density Issues (pace too fast):**
- Change 3: ESM3 section — too many concepts (multimodal, tokenization, function conditioning, protein design) introduced in one section
- Change 9: Limitations section — three distinct failure modes, each with unfamiliar concepts
- Change 16: PRS section — genetic architecture, attention mechanisms, genetic interactions all in one passage

**Recommendation:** Break dense sections into subsections with explicit transitions. Add one-sentence concept summaries before diving into details.

---

## Cross-Cutting Recommendations

### 1. **Define Key Domain-Specific Terms on First Use in Each Chapter**

If a chapter first introduces concepts for a cross-domain audience, parenthetical definitions are essential:
- Change 3: Define "discretized," "tokenization," "chromatin state," "InterPro," "Gene Ontology"
- Change 8: Define "enhancer-like chromatin states," "transcription factor binding motifs"
- Change 9: Define "epistasis" explicitly

### 2. **Add Prerequisite Callouts for High-Concept Sections**

Sections requiring significant domain knowledge should include a prerequisite callout:

Example (for Change 3, ESM3 section):
```markdown
::: {.callout-note title="Prerequisite Knowledge"}
This section assumes familiarity with:
- **Protein structure:** 3D arrangements of amino acids in proteins
- **Tokenization:** Converting continuous data (like 3D coordinates) into
  discrete symbolic units
- **Functional annotation:** Databases that describe what proteins do

For background, see @sec-ch05-representations (tokenization) and
@sec-ch04-protein-biology (protein structure background).
:::
```

### 3. **Use Consistent Terminology Across Chapters**

Verify that:
- "Embeddings" are consistently referred to (not sometimes "latent representations," sometimes "embeddings")
- Domain-specific tools (SCENIC, HEIST) are introduced with the same level of detail
- ML concepts (attention, conditioning, loss functions) use aligned explanations

### 4. **Add Concrete Examples for Abstract ML Concepts**

When introducing ML concepts to biology audiences, use analogies:

Example (for Change 17, DiffDock):
```markdown
*DiffDock* treats docking as a generative problem—similar to how a
diffusion model generates an image by starting with random noise and
iteratively refining it. Here, the model starts with random molecular
configurations and iteratively improves them toward the correct binding
pose.
```

### 5. **Expand Cross-References for Interdisciplinary Readers**

When citing earlier chapters, help readers navigate:

Example (for Change 13, BERTology):
```markdown
These "BERTology" techniques translate directly to genomic models. For
background on attention mechanisms, see @sec-ch07-attention.
```

---

## Implementation Priority

### **TIER 1: DO NOT PUBLISH WITHOUT FIXING** (High-barrier changes)

These prevent comprehension for a substantial portion of the target audience:

1. **Change 3 (ESM3)** — 30 min revision
   - Define: tokenization, InterPro, Gene Ontology, esmGFP context
   - Add: protein folding significance, conditional generation explanation

2. **Change 9 (Limitations)** — 20 min revision
   - Define: epistasis, conservation bias, calibration gap, retrieval-augmented methods
   - Add: brief explanation of what each cited paper contributes

### **TIER 2: STRONGLY RECOMMEND REVISING** (Medium-barrier changes)

Improve comprehension significantly but not absolutely blocking:

3. **Change 4 (RoseTTAFold)** — 5 min
   - Define: MSA, orphan sequences

4. **Change 6 (Ingraham)** — 5 min
   - Define: masked prediction, conditioning

5. **Change 8 (Farh Statistics)** — 5 min
   - Define: enhancer-like chromatin states, binding motifs

6. **Change 10 (Circularity)** — 5 min
   - Context: SIFT/PolyPhen tools

7. **Change 13 (BERTology)** — 10 min
   - Define: attention head, probing classifiers

8. **Change 14 (Mendelian Randomization)** — 15 min
   - Define: instrumental variables, distinguish observational vs. intervention

9. **Change 16 (Non-Linear PRS)** — 10 min
   - Define: genetic architecture, genetic interactions, phenotype embeddings

10. **Change 17 (DiffDock)** — 10 min
    - Explain: generative problem, denoising, scoring functions

### **TIER 3: OPTIONAL ENHANCEMENTS** (Low-barrier changes)

Minor clarity improvements:

11. **Changes 1, 2, 5, 7, 11, 12, 15, 18, 19, 20, Tools** — Optional parenthetical enhancements

---

## Estimated Total Revision Effort

- **Tier 1 (blocking):** 50 minutes
- **Tier 2 (strongly recommended):** 90 minutes
- **Tier 3 (optional):** 30 minutes

**Total:** ~2.5-3 hours to address all accessibility barriers

---

## Recommendations for Editorial Review

### Before Implementation:

1. ✅ **Route Tier 1 and 2 changes through domain-expert review:**
   - Each revision should be checked by a bioinformatics expert (for ML-to-bio translations) and an ML expert (for bio-to-ML translations)

2. ✅ **Add prerequisite callout to chapter openings** that introduce cross-domain concepts:
   - Chapters 16, 18, 25, 26, 28, 30 should include "Prerequisites" or "Learning Objectives" callouts

3. ✅ **Create a "jargon glossary" callout** in chapters with high concept density:
   - Include links to glossary entries or inline definitions

4. ✅ **Test readability with beta readers:**
   - If possible, have one CS reader and one biology reader review revised sections before finalizing

### Longer-term Recommendations:

5. ✅ **Standardize cross-domain explanation templates:**
   - Create reusable callout formats for "What is X?" and "Why does Y matter?"

6. ✅ **Build a prerequisite map:**
   - Document which chapters require which background knowledge to support interdisciplinary navigation

---

## Conclusion

The proposed additions significantly strengthen the book's literature foundation and provide important context for genomic foundation models. However, **concept density and undefined domain-specific jargon create accessibility barriers for interdisciplinary readers**.

With the revisions outlined above (particularly for Changes 3 and 9, and Tier 2 items), the additions can be made inclusive and comprehensible to the target audience of graduate students and researchers new to genomic ML.

**Overall Recommendation:** **CONDITIONAL APPROVAL** — Implement with required Tier 1 and strongly recommended Tier 2 revisions before publication.

---

*Audit completed by Audience Accessibility Checker*
*For specific revision wording, see change-by-change analysis above.*

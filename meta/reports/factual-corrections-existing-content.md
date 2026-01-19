# Factual Corrections: Existing Book Content

**Document Type:** Editorial Notes (Separate from Gap Citations)
**Generated:** 2026-01-18
**Status:** For future editorial review

---

## Overview

During the multi-agent review of the gap citations proposal, reviewers identified factual issues in proposed *new* content that should inform how we discuss these topics in the book. These are recorded here for future editorial consideration, separate from the citation additions.

---

## Chapter 18: VEP Limitations Framing

### Issue: "Conservation Bias" Terminology

**Source:** Domain Accuracy Review (GFM Professor)

**Proposed language (problematic):**
> "Conservation bias: Models preferentially score positions that are evolutionarily constrained, potentially missing functionally important but variable positions"

**Why this framing is incorrect:**

Characterizing this as a "bias" or "failure" fundamentally misunderstands PLM-VEP behavior:

1. **This is the intended signal**: Scoring evolutionarily constrained positions as intolerant to variation is exactly what these models are designed to do
2. **Variable positions SHOULD score as benign**: Positions that tolerate variation across evolution are generally not functionally critical
3. **The critique conflates two distinct issues**:
   - **True limitation**: PLMs may miss *rare* functional variants (de novo mutations, recent positive selection, population-specific variants)
   - **Not a limitation**: Scoring conserved positions as intolerant

**Correct framing for book:**
- "Limited sensitivity to rare functional variation" rather than "conservation bias"
- Focus on what PLMs genuinely miss: de novo variants, recent adaptive mutations, population-specific functional variants not well-represented in training data

---

## Chapter 16: ESM3 Characterization

### Issue: "Generational Leap" Language

**Source:** Domain Accuracy + Epistemic Reviews

**Proposed language (overstated):**
> "ESM3 represents a generational leap in protein language modeling"

**Why this is problematic:**
- "Generational leap" is subjective marketing language
- ESM3 is evolutionary (builds on prior work like ProteinMPNN, RFdiffusion), not revolutionary
- Single example (esmGFP) doesn't demonstrate broad generalization

**Correct framing:**
- "Substantial advance" or "significant extension"
- Emphasize that esmGFP required screening millions of candidates
- Note validation focused on well-characterized protein family (GFPs)

---

## Chapter 16: RoseTTAFold vs ESMFold

### Issue: Accuracy vs Speed Trade-off

**Source:** Domain Accuracy Review

**Proposed language (incorrect):**
> "For proteins with good homolog coverage, RoseTTAFold may offer advantages"

**Why this is wrong:**
- RoseTTAFold's main advantage over AlphaFold2 is **speed**, not accuracy
- Both RoseTTAFold and AlphaFold2 use MSAs when available
- The accuracy-given-same-MSA is comparable
- ESMFold (single-sequence) is the method that trades MSA for speed

**Correct characterization:**
- RoseTTAFold: faster inference than AlphaFold2 with comparable accuracy
- ESMFold: no MSA required, best for orphan sequences

---

## Chapter 12: Genomic Touchstone Claims

### Issue: Overstated Prevention of Leakage

**Source:** Epistemic Review

**Proposed language (overclaimed):**
> "Gene-level splits prevent information leakage"
> "Performance across diverse tasks reveals generalization"

**Why these are problematic:**
1. Gene-level splits *reduce* but don't *prevent* leakage (cross-gene regulatory elements, correlated effects still possible)
2. "Reveals generalization" is speculative - this is an *intended design feature*, not a proven outcome

**Correct framing:**
- "substantially reduce within-gene information leakage"
- "designed to assess generalization rather than task-specific optimization"

---

## Chapter 25: BERTology Transfer

### Issue: Direct Translation Claim

**Source:** Epistemic Review

**Proposed language (overstated):**
> "These 'BERTology' techniques translate directly to genomic models"

**Why this is problematic:**
- NLP and genomics domains differ fundamentally
- What attention heads learn in genomic models remains an open question
- "Translate directly" implies solved problem when it's still active research

**Correct framing:**
- "BERTology-inspired techniques can be adapted for genomic models"
- Add uncertainty: "the biological meaning of attention heads in genomic models remains an open question"

---

## Action Items

These corrections should inform:
1. How we write about PLM-VEP limitations throughout the book
2. The characterization of specific models (ESM3, RoseTTAFold)
3. The framing of benchmark design claims
4. How we discuss cross-domain technique transfer

**Note:** These are editorial guidelines, not specific text changes to existing content. Review existing chapters for similar issues when time permits.

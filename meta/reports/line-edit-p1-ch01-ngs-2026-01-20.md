# Line Edit Report: p1-ch01-ngs.qmd

**Date:** 2026-01-20
**Chapter:** Part 1, Chapter 1 - From Reads to Variants
**File:** `/root/gfm-book/part_1/p1-ch01-ngs.qmd`

---

## AI Pattern Score: 2/10

This chapter demonstrates excellent writing discipline with minimal AI-typical patterns. The prose is direct and professional throughout.

---

## Auto-Fixed Patterns

### 1. "leverage" -> "use"

| Line | Original | Fixed |
|------|----------|-------|
| 341 | "Tools like *GLIMPSE* **leverage** reference panels to convert..." | "Tools like *GLIMPSE* **use** reference panels to convert..." |

**Total auto-fixes applied: 1**

### Patterns NOT Found (Clean)

The following AI-typical patterns were NOT present in this chapter:

- "in order to" (0 instances)
- "due to the fact that" (0 instances)
- "delve into" (0 instances)
- "crucial" (0 instances)
- "It is worth noting that" (0 instances)
- "It should be noted that" (0 instances)
- "In this section, we will..." (0 instances)
- "In this chapter, we will..." (0 instances)

---

## Flagged for Manual Review

### Em-Dashes

**Count: 0 true em-dashes (U+2014)**

The chapter uses double-hyphens (`--`) throughout instead of em-dashes. This is consistent with common plain-text conventions. No action required unless style guide mandates em-dashes.

### False Enthusiasm Words

**Count: 0**

No instances of:
- "remarkably"
- "notably"
- "revolutionary"
- "groundbreaking"

### Formulaic Transitions

**Count: 0**

No instances of:
- "Moreover"
- "Furthermore"
- "Additionally"

### Long Sentences (>40 words)

**Count: 6 sentences**

These sentences exceed 40 words and may benefit from restructuring:

| Line | Word Count | Opening Text |
|------|------------|--------------|
| 48 | 43 | "A patient presenting with sudden cardiac arrest at age 35 needs deep, reliable coverage of *KCNQ1*..." |
| 91 | 46 | "Oxford Nanopore Technologies (ONT) instruments generate reads ranging from a few kilobases to over a megabase..." |
| 247 | 49 | "Each variant occupies one row with mandatory columns: `CHROM` and `POS` specify genomic location..." |
| 257 | 47 | "**Variant Quality Score Recalibration (VQSR)** instead trains a Gaussian mixture model on known true positives..." |
| 391 | 48 | "A heterozygous site with 20x coverage and 10 reads supporting each allele is confidently called..." |
| 551 | 43 | "For regulatory sequence models and variant effect predictors (@sec-ch15-dna-lm for DNA language models..." |

**Recommendation:** These long sentences contain technical content where the length may be justified for precision. Lines 247 and 257 describe multi-component processes where breaking up the sentence could harm clarity. Review for potential simplification but do not force splits that would reduce technical precision.

---

## Summary

| Category | Count | Status |
|----------|-------|--------|
| Auto-fixes applied | 1 | Complete |
| Em-dashes | 0 | Clean |
| Enthusiasm words | 0 | Clean |
| Formulaic transitions | 0 | Clean |
| Long sentences | 6 | Flag for review |

**Overall Assessment:** This chapter is very clean from an AI pattern perspective. The single "leverage" instance has been corrected. The long sentences flagged contain necessary technical detail and should be reviewed contextually rather than mechanically shortened.

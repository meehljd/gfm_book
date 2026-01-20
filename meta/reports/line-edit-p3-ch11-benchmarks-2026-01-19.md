# Line Edit Report: p3-ch11-benchmarks.qmd

**Date:** 2026-01-19
**Chapter:** Part 3, Chapter 11 - Benchmark Landscape
**File:** `/root/gfm-book/part_3/p3-ch11-benchmarks.qmd`
**Editor:** textbook-editor agent (auto-fix mode)

---

## Summary

This chapter is **well-written** with minimal AI-typical patterns. The prose is clean, direct, and appropriately technical for a textbook audience. Only 3 items required auto-fixing, and the chapter contains no false enthusiasm words, no meta-commentary, and no formulaic transitions.

---

## Auto-Fixes Applied

The following edits were successfully applied:

| Line | Pattern | Original | Replacement | Status |
|------|---------|----------|-------------|--------|
| 47 | AI-typical word | "a **crucial** principle" | "an **important** principle" | APPLIED |
| 170 | AI-typical word | "can **leverage** chromosome-level" | "can **use** chromosome-level" | APPLIED |
| 215 | AI-typical word | "several **crucial** advantages" | "several **important** advantages" | APPLIED |

### Context for Each Fix

**Line 47** (TAPE Key Insight callout):
```
*TAPE* established an important principle: evaluate representations...
```
Changed "crucial" to "important" - avoids AI-inflated language.

**Line 170** (DNALongBench description):
```
...whether models can use chromosome-level context...
```
Changed "leverage" to "use" - clearer and less business-jargon.

**Line 215** (CAGI Key Insight callout):
```
The prospective design of CAGI provides several important advantages...
```
Changed "crucial" to "important" - consistent with avoiding AI-inflation.

---

## AI Pattern Score: 2/10

**Excellent** - This chapter demonstrates strong editorial discipline:
- No filler phrases ("in order to", "due to the fact that")
- No redundancies ("end result", "basic fundamentals")
- No throat-clearing ("It is worth noting that")
- No meta-commentary ("This section will explore...")
- No weak intensifiers ("very", "really", "quite" used inappropriately)
- No false enthusiasm words
- No formulaic transitions (Moreover, Furthermore, Additionally)
- Only 3 AI-typical words found and fixed (2x "crucial", 1x "leverage")

The low score reflects a well-edited chapter that needed only minor polishing.

---

## Manual Review Items

### High Severity

*None identified.*

### Medium Severity

#### 1. Long Sentences (>40 words): 8 occurrences

Consider breaking these sentences for improved readability:

| Line | Word Count | Excerpt |
|------|------------|---------|
| 29 | 43 | "Major benchmarks are positioned according to what they test: variant effect prediction relies on ClinVar..." |
| 34 | 44 | "**Protein language models** (@sec-ch16-protein-lm) benefit from the longest-established and most systematic evaluation ecosystem..." |
| 166 | 42 | "Consider the challenge of understanding a sentence versus understanding a novel: predicting the next word..." |
| 168 | 44 | "TADs are regions of the genome (typically 100 kb to 2 Mb) that preferentially interact with themselves..." |
| 325 | 65 | "Leakage pathways (red dashed) create spurious performance: direct overlap when pretraining includes benchmark sequences..." |
| 346 | 41 | "Mitigating gaming requires structural changes to evaluation practice: prospective benchmarks like CAGI..." |
| 360 | 41 | "The response to saturation should be moving to harder benchmarks that still discriminate between methods..." |
| 444 | 42 | "Across all categories, persistent challenges emerge: saturation that reduces discriminative power..." |

**Recommendation:** Lines 29, 166, 168, and 325 are figure captions or explanatory text where longer sentences may be appropriate. Lines 34, 346, 360, and 444 could potentially be split.

#### 2. Passive Voice Clusters (3+ in 5-line window): 6 clusters

| Lines | Count | Recommendation |
|-------|-------|----------------|
| 199-204 | 5 | ClinVar limitations section - passive voice fits the expository tone but could be tightened |
| 268-273 | 4 | PGS benchmarks section - acceptable for technical description |
| 294-299 | 4 | Data sources section - consider activating some constructions |
| 298-303 | 3 | Label provenance section - overlaps with above |
| 380-385 | 3 | Leakage from scale section - acceptable |
| 424-429 | 3 | Systematic gaps section - acceptable |

**Note:** Passive voice is often appropriate in scientific writing. These clusters are not problematic but are flagged for awareness.

### Low Severity

#### 3. Em-Dash Usage

**Count:** 0 em-dashes (—), 0 en-dashes (–), 59 double-hyphens (--)

All 59 double-hyphen occurrences are in table row separators, not prose. **No action needed.**

#### 4. False Enthusiasm Words

**Count:** 0

No instances of: remarkably, notably, impressively, revolutionary, groundbreaking.

#### 5. Formulaic Transitions

**Count:** 0

No instances of: Moreover, Furthermore, Additionally (at sentence start or otherwise).

---

## Metrics Summary

| Category | Count | Assessment |
|----------|-------|------------|
| Auto-fix items | 3 | All applied successfully |
| False enthusiasm words | 0 | None present |
| Formulaic transitions | 0 | None present |
| Long sentences (>40 words) | 8 | Moderate - some in figure captions |
| Passive voice clusters | 6 | Acceptable for scientific prose |
| Em-dash overuse | 0 | Not applicable |
| Total passive constructions | 43 | Normal for technical writing |

---

## Recommendations

1. ~~Apply the 3 pending auto-fixes~~ **COMPLETED**
2. **Consider splitting** the long sentence on line 34 (opening paragraph of TAPE section)
3. **Review passive clusters** in lines 199-204 and 294-299 for possible activation
4. **No urgent issues** - this chapter is publication-ready

---

## Status

- [x] Apply 3 auto-fix edits (crucial -> important x2, leverage -> use)
- [ ] Review 8 long sentences for potential splitting (optional)
- [ ] Final proofread after fixes applied (optional)

---

*Report generated by textbook-editor agent*

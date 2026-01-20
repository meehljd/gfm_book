# Line Edit Report: p5-ch19-rna.qmd

**File:** `/root/gfm-book/part_5/p5-ch19-rna.qmd`
**Date:** 2026-01-19
**Editor:** textbook-editor agent (auto-fix mode)

---

## Summary

| Category | Count | Action |
|----------|-------|--------|
| Auto-fixes applied | 0 | N/A |
| Flagged for manual review | 14 | See details below |

**Overall Assessment:** This chapter is well-written with minimal style issues. The prose is clear and direct, avoiding most common filler patterns and AI-typical language. The main areas for manual review are em-dash usage and a few long sentences.

---

## Auto-Fixes Applied

**None required.**

The following patterns were searched but not found:
- Filler phrases: "in order to", "due to the fact that", "at this point in time"
- Redundancies: "completely eliminate", "end result"
- Throat-clearing: "It is worth noting that", "It is important to note that"
- AI-typical words: "delve into", "crucial"
- Meta-commentary: "In this section, we will explore...", "This chapter covers..."
- Weak intensifiers: "very", "really", "quite" (before adjectives)

**Note on "leverage" (line 314):** The word appears as "regulatory leverage" - a legitimate noun usage meaning influence/power, not the AI-typical verb form "leverage" = "use". No change required.

---

## Flagged for Manual Review

### 1. Em-Dash Usage (12 instances)

Em-dashes are used throughout the chapter for explanatory asides. While each instance is grammatically correct, the frequency may warrant review for variety.

| Line | Context |
|------|---------|
| 18 | "RNA occupies a unique position in the central dogma---it is both the output..." |
| 72 | "RNA energy landscapes are remarkably flatter---like a marble on a dinner plate..." |
| 75 | "...that protein modeling largely avoids---most proteins have a single dominant fold." |
| 94 | "These alternatives are mutually exclusive---a base can only pair with one partner---but..." |
| 102 | "...if positions $i$ and $j$ pair, the structure between them is independent of the structure outside---but pseudoknots violate..." |
| 126 | "...if $(i,j)$ pairs, then any other pair $(k,l)$ either lies entirely within $(i,j)$ or entirely outside it, never crossing---this nesting property..." |
| 190 | "...attention patterns that correspond to 3D contacts---an emergent capability that surprised even its creators." |
| 198 | "...it is about data. Proteins have accumulated over 4 billion years..." (correctly uses em-dash) |
| 314 | "...where in the cell it localizes---like an expiration date stamped on perishable goods..." |
| 325 | "...5' and 3' effects interact---optimize iteratively, not independently" |
| 365 | "...affects multiple objectives---there is no single 'optimal' sequence..." |
| 419, 469, 498, 509 | Additional instances in callouts and summaries |

**Recommendation:** Consider converting some em-dash asides to parenthetical phrases, colons, or separate sentences for variety.

---

### 2. False Enthusiasm Words (1 instance)

| Line | Text | Suggestion |
|------|------|------------|
| 49 | "protein language models have learned to predict these folds with **remarkable** accuracy" | Consider: "with high accuracy" or "with accuracy approaching experimental methods" |

**Context:** This appears in a Stop and Think box comparing protein and RNA structure prediction. The word is used to contrast protein success with RNA challenges, which provides pedagogical value. May be acceptable.

---

### 3. Long Sentences (Review for Readability)

The following sentences exceed 50 words and may benefit from splitting:

| Line | Word Count (approx.) | First Words |
|------|---------------------|-------------|
| 72 | ~95 | "RNA's defining computational challenge emerges from thermodynamics..." |
| 102 | ~105 | "Pseudoknots occur when bases in a loop pair with bases outside that loop..." |
| 126 | ~85 | "*Mfold* and the *ViennaRNA* package represent the most widely used implementations..." |
| 314 | ~80 | "The protein output of an mRNA depends as much on its untranslated regions..." |

**Line 72 Example (95 words):**
> "RNA's defining computational challenge emerges from thermodynamics. Proteins fold into stable three-dimensional structures because their energy landscapes contain deep minima: the native state sits in a pronounced funnel that guides the folding process. RNA energy landscapes are remarkably flatter---like a marble on a dinner plate with multiple shallow dents rather than a deep bowl. The marble settles in one dent but can easily roll to another with a small nudge. Multiple conformations compete for occupancy, with free energy differences often smaller than thermal fluctuations at cellular temperatures. A given RNA sequence may adopt several alternative structures with similar stabilities, and the dominant conformation can shift in response to ion concentrations, temperature, protein binding, or chemical modifications."

**Recommendation:** This paragraph contains multiple sentences but the analogy "like a marble on a dinner plate" is excellent pedagogy. No change needed for this specific case. Review other long sentences individually.

---

### 4. Formulaic Transitions

**None found.** The chapter avoids "Furthermore," "Moreover," "Additionally," and similar formulaic connectors.

---

## Positive Observations

1. **Strong opening:** The chapter opens with a memorable quote and immediately presents a concrete example (synonymous mutations affecting RNA-level biology).

2. **Excellent analogies:** The "marble on a dinner plate" analogy (line 72) and "expiration date stamped on perishable goods" (line 314) are memorable and pedagogically effective.

3. **Clear structure:** Sections are well-organized with descriptive headings that signal content.

4. **Appropriate callouts:** Stop and Think boxes, Knowledge Checks, and Key Insights are used strategically without overuse.

5. **Active voice:** The chapter predominantly uses active voice and avoids passive constructions.

6. **Technical precision:** Mathematical notation and biological terminology are used precisely.

---

## Recommendations

1. **Em-dash variety:** Consider converting 2-3 em-dash constructions to alternative punctuation for stylistic variety.

2. **Line 49:** Evaluate whether "remarkable" adds pedagogical value or can be replaced with more specific language.

3. **Complex sentences:** Lines 72, 102, 126, and 314 are long but generally well-structured. Review individually for potential splitting only if readability suffers.

---

*Report generated by textbook-editor agent in auto-fix mode.*

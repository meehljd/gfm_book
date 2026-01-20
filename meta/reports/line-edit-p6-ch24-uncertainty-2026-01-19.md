# Line Edit Report: Chapter 24 - Uncertainty Quantification

**File:** `/root/gfm-book/part_6/p6-ch24-uncertainty.qmd`
**Date:** 2026-01-19
**Editor:** textbook-editor (auto-fix mode)

---

## Summary

| Category | Count |
|----------|-------|
| Auto-fixes applied | 0 |
| Items flagged for manual review | 3 |
| Total lines in chapter | 719 |

---

## Auto-Fix Targets (None Found)

The following phrases were searched for but not found in the chapter:

| Target Phrase | Replacement | Instances Found |
|---------------|-------------|-----------------|
| "in order to" | "to" | 0 |
| "due to the fact that" | "because" | 0 |
| "delve into" | "examine" | 0 |
| "leverage" | "use" | 0 |
| "crucial" | "important" | 0 |
| "It is worth noting that" | (delete) | 0 |
| "In this section, we will..." | (delete meta-commentary) | 0 |

**No changes were made to the file.**

---

## Items Flagged for Manual Review

### 1. Em-Dash Usage (Line 276)

**Location:** Line 276
**Context:** Within a worked example callout

```markdown
- Now the model reports 86% confidence---still favoring pathogenic, but acknowledging greater uncertainty
```

**Issue:** Triple-dash em-dash (---) used for parenthetical insertion. Consider whether this could be rewritten with a comma, colon, or as two sentences for improved readability.

**Suggested revision options:**
- "Now the model reports 86% confidence, still favoring pathogenic but acknowledging greater uncertainty"
- "Now the model reports 86% confidence. It still favors pathogenic but acknowledges greater uncertainty."

---

### 2. Formulaic Transition (Line 314)

**Location:** Line 314
**Context:** Isotonic regression section

```markdown
Additionally, isotonic regression provides no uncertainty estimate on the calibration itself; we learn a point estimate of the calibration function without knowing how reliable that estimate is.
```

**Issue:** "Additionally," as a sentence starter is a formulaic transition that can feel mechanical. This usage is borderline acceptable since it genuinely adds a second limitation, but consider whether a more integrated sentence structure would read better.

**Suggested revision options:**
- "Isotonic regression also provides no uncertainty estimate..."
- "A further limitation: isotonic regression provides no uncertainty estimate..."
- Leave as-is (acceptable in technical writing when genuinely enumerating points)

---

### 3. Em-Dash Usage (Line 407)

**Location:** Line 407
**Context:** Heteroscedastic models section, explaining Gaussian loss function

```markdown
The first term penalizes prediction errors, weighted by inverse variance so that high-variance predictions are penalized less for the same absolute error---this is mathematically necessary because a Gaussian with larger variance assigns non-negligible probability to a wider range of values.
```

**Issue:** Triple-dash em-dash (---) used to introduce an explanatory clause. The sentence is already long and complex; the em-dash adds to cognitive load.

**Suggested revision options:**
- Split into two sentences: "The first term penalizes prediction errors, weighted by inverse variance so that high-variance predictions are penalized less for the same absolute error. This weighting is mathematically necessary because a Gaussian with larger variance assigns non-negligible probability to a wider range of values."
- Use a semicolon: "...the same absolute error; this is mathematically necessary because..."
- Leave as-is (the em-dash does provide appropriate emphasis for the explanatory aside)

---

## Additional Observations

### Positive Findings

1. **No false enthusiasm language detected**: Terms like "exciting," "fascinating," "remarkable," "groundbreaking," "revolutionary," and "powerful" do not appear in this chapter.

2. **No excessive meta-commentary**: The chapter does not contain phrases like "we will discuss," "this chapter will," "let us now examine," or other meta-commentary patterns.

3. **Clean formulaic transition usage**: The chapter largely avoids formulaic transitions like "Moreover," "Furthermore," "However," "Thus," and "Therefore" at sentence starts, except for the single "Additionally" noted above.

4. **Strong technical prose**: The chapter demonstrates clear, direct writing with appropriate hedging language and well-structured explanations.

### Style Consistency Notes

- The chapter makes appropriate use of bold for key terms (e.g., **calibration**, **epistemic uncertainty**, **aleatoric uncertainty**)
- Cross-references are well-formatted and point to related chapters
- Mathematical notation is consistent and well-explained
- Tables provide clear summaries of key distinctions

---

## Recommendation

This chapter requires **minimal intervention**. The three flagged items are minor style considerations rather than required changes. The author may:

1. **Accept all as-is**: The em-dashes and "Additionally" are within acceptable bounds for technical writing
2. **Revise for stricter style consistency**: Apply the suggested alternatives if enforcing a no-em-dash policy
3. **Selective revision**: Address only the longer sentence (line 407) where the em-dash adds to already high complexity

The chapter demonstrates strong adherence to style guidelines and clear technical communication.

# Evaluation Checklist

Detailed criteria for evaluating rendered figures during the refine loop. Use this checklist after each render to determine if the figure meets quality standards.

---

## Quick Pass/Fail Checks

These must pass before detailed evaluation:

| Check | Command/Method | Pass Criteria |
|-------|----------------|---------------|
| **Renders** | Check exit code | Exit code 0 |
| **File exists** | `ls output.svg` | File present |
| **File not empty** | `wc -c output.svg` | Size > 100 bytes |
| **Valid format** | Open in viewer | No parse errors |

If any of these fail, fix the code error before continuing.

---

## Visual Evaluation

After confirming the file renders, **read the image** and evaluate:

### 1. Completeness (Critical)

> Are all required elements from the specification present?

| Element Type | Check For |
|--------------|-----------|
| **Primary elements** | Main visual components (bars, nodes, axes) |
| **Labels** | All text labels present and correct |
| **Axes** | X/Y axis labels, tick marks |
| **Legend** | If specified, legend present and complete |
| **Title** | Figure title if required |
| **Annotations** | Callouts, highlights, markers |

**Pass**: All spec'd elements visible
**Fail**: Any required element missing → Add missing element

### 2. Legibility (Critical)

> Can all text be read at normal viewing size?

| Check | Minimum Standard |
|-------|------------------|
| **Font size** | ≥9pt for labels, ≥11pt for titles |
| **Text overlap** | No overlapping text |
| **Contrast** | Text readable against background |
| **Truncation** | No cut-off labels |

**Pass**: All text readable without zooming
**Fail**: Text issues → Increase font size, adjust layout, abbreviate

### 3. Layout (High Priority)

> Is the visual arrangement clear and uncluttered?

| Check | Standard |
|-------|----------|
| **Spacing** | Elements not crowded |
| **Alignment** | Consistent alignment |
| **Hierarchy** | Important elements prominent |
| **Margins** | Adequate whitespace |
| **Balance** | Visual weight distributed |

**Pass**: Clean, professional appearance
**Fail**: Cluttered/unbalanced → Adjust spacing, resize

### 4. Colors (Medium Priority)

> Does the color scheme match specification and accessibility guidelines?

| Check | Standard |
|-------|----------|
| **Palette match** | Colors match spec values |
| **Consistency** | Same meaning = same color |
| **Contrast** | Adjacent elements distinguishable |
| **Colorblind-safe** | Avoid red-green only distinction |

**Pass**: Colors correct and accessible
**Fail**: Color issues → Adjust palette, add patterns

### 5. Accuracy (High Priority)

> Do visual elements correctly represent the underlying data/concept?

| Check | Standard |
|-------|----------|
| **Proportions** | Sizes/lengths accurate |
| **Relationships** | Connections correct |
| **Labels match** | Labels correspond to elements |
| **No artifacts** | No spurious visual elements |

**Pass**: Accurate representation
**Fail**: Inaccuracies → Fix data mapping, correct labels

### 6. Style Consistency (Medium Priority)

> Does this figure match the book's visual language?

| Check | Standard |
|-------|----------|
| **Font family** | Arial/sans-serif |
| **Color palette** | Genomics convention colors |
| **Line weights** | Consistent with other figures |
| **Overall aesthetic** | Professional, academic style |

**Pass**: Matches book style
**Fail**: Style mismatch → Apply standard styling

---

## Evaluation Prompts

When reading the rendered image, answer these questions:

### Immediate Impression (5 seconds)
1. What is this figure about? (If unclear → fail clarity)
2. Does anything look wrong or missing? (If yes → investigate)

### Detailed Review
3. Count the major elements - do they match the spec?
4. Read each text label - any cut off, overlapping, or unreadable?
5. Check colors - do they follow the genomics palette?
6. Look at spacing - is anything too crowded or too sparse?
7. Compare to spec - does this communicate the intended message?

### Final Assessment
8. Would this look professional in a published textbook?
9. Does it need any refinement?

---

## Iteration Decision Tree

```
After rendering, evaluate:
│
├─ File exists and valid?
│   ├─ No → Fix syntax/render error → Re-render
│   └─ Yes → Continue
│
├─ All elements present?
│   ├─ No → Add missing elements → Re-render
│   └─ Yes → Continue
│
├─ Text legible?
│   ├─ No → Increase font/adjust layout → Re-render
│   └─ Yes → Continue
│
├─ Layout clean?
│   ├─ No → Adjust spacing → Re-render
│   └─ Yes → Continue
│
├─ Colors correct?
│   ├─ No → Fix colors → Re-render
│   └─ Yes → Continue
│
├─ Accurate representation?
│   ├─ No → Fix data/labels → Re-render
│   └─ Yes → Continue
│
└─ PASS: Figure complete
```

---

## Common Issues by Tool

### Matplotlib

| Issue | Detection | Fix |
|-------|-----------|-----|
| Labels cut off | Text at edge of figure | `plt.tight_layout()` |
| Overlapping labels | Text on text | Rotate labels, reduce font |
| Legend blocking | Legend over data | `bbox_to_anchor=(1.05, 1)` |
| Low resolution | Pixelated text | Increase `dpi` |
| Wrong aspect | Distorted shapes | Set `aspect='equal'` |

### Mermaid

| Issue | Detection | Fix |
|-------|-----------|-----|
| Nodes too wide | Text wrapping badly | Add `\n` line breaks |
| Wrong flow | Unexpected direction | Change `LR`/`TD`/`TB` |
| Missing styles | Default gray | Check `%%{init:...}%%` |
| Subgraph overlap | Sections collide | Adjust subgraph size |

### Graphviz

| Issue | Detection | Fix |
|-------|-----------|-----|
| Node overlap | Nodes on top of each other | `nodesep=0.5; ranksep=0.5` |
| Edge crossing | Lines cross unnecessarily | Try `splines=ortho` |
| Bad hierarchy | Nodes at wrong levels | Use `{rank=same}` |
| Tiny text | Unreadable labels | `fontsize=12` |
| Poor layout | Confusing arrangement | Try `neato` or `fdp` engine |

---

## Scoring Summary

| Category | Weight | A (4) | B (3) | C (2) | D (1) |
|----------|--------|-------|-------|-------|-------|
| Completeness | 25% | All elements | Minor omission | Significant gap | Missing core |
| Legibility | 25% | Perfect | Minor issue | Several issues | Unreadable |
| Layout | 20% | Clean | Slightly busy | Cluttered | Chaotic |
| Colors | 15% | Correct | Minor deviation | Several wrong | Incorrect |
| Accuracy | 15% | Perfect | Minor error | Misleading | Wrong |

**Total Score**: Weighted average

| Grade | Score | Action |
|-------|-------|--------|
| A | 3.5-4.0 | Accept |
| B | 2.5-3.4 | Accept (minor polish optional) |
| C | 1.5-2.4 | Refine if iterations remain |
| D | 1.0-1.4 | Must refine or flag for review |

---

## Final Checklist

Before marking a figure as complete:

- [ ] Renders without errors
- [ ] All spec'd elements present
- [ ] All text readable at 100%
- [ ] No overlapping elements
- [ ] Colors match genomics palette
- [ ] Layout is clean and professional
- [ ] Accurately represents the concept
- [ ] Would look good in a textbook

If all checked → **PASS**
If any unchecked after 3 iterations → **FLAG FOR REVIEW**

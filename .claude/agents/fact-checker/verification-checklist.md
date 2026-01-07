# Citation Verification Checklist

Systematic checklist for verifying that citations correctly support their claims.

## Quick Verification (Per Citation)

### Level 1: Surface Check (Always)

- [ ] **Citation exists**: `[@key]` has corresponding entry in `.bib` file
- [ ] **Paper is accessible**: DOI/URL is valid
- [ ] **Paper is not retracted**: No retraction notice found
- [ ] **Authors match**: Names in citation match paper authors

### Level 2: Relevance Check (Spot-Check)

- [ ] **Topic match**: Paper actually discusses the cited topic
- [ ] **Correct paper**: Not confused with similarly-titled paper
- [ ] **Primary source**: Not citing review when primary source exists
- [ ] **Current source**: Not superseded by newer authoritative work

### Level 3: Deep Verification (Priority Claims)

- [ ] **Numbers match**: Statistics in text match paper's reported values
- [ ] **Context preserved**: Claim doesn't misrepresent paper's findings
- [ ] **Causation vs. correlation**: Text doesn't overclaim causation
- [ ] **Generalization scope**: Text doesn't overgeneralize specific findings
- [ ] **Limitations acknowledged**: Paper's caveats reflected if relevant

---

## Verification by Claim Type

### Performance Claims

**Claim pattern:** "Model X achieves Y% on benchmark Z"

| Check | Question | Pass | Fail |
|-------|----------|------|------|
| Metric accuracy | Does paper report exactly Y%? | Exact match | Different number |
| Benchmark match | Is it the same benchmark/dataset? | Same | Different version/subset |
| Conditions match | Same experimental setup? | Same | Different hyperparameters |
| Cherry-picking | Is this their best or representative result? | Representative | Cherry-picked |

**Red flags:**
- Text says "0.95 auROC" but paper reports "0.94 auROC"
- Text cites performance on full test set; paper shows subset results
- Text claims improvement but paper shows within error bars

### Comparison Claims

**Claim pattern:** "Model X outperforms Model Y by Z%"

| Check | Question | Pass | Fail |
|-------|----------|------|------|
| Comparison exists | Does paper actually compare these models? | Yes | Comparison inferred |
| Same conditions | Fair comparison (same data/setup)? | Yes | Different conditions |
| Statistical significance | Is difference significant? | Yes or noted | Claimed without testing |
| Direction correct | Does X actually beat Y? | Yes | Reversed or mixed |

**Red flags:**
- Paper compares to older version of baseline
- Improvement is within standard error
- Comparison uses different test sets

### Attribution Claims

**Claim pattern:** "Method X was introduced by Y et al."

| Check | Question | Pass | Fail |
|-------|----------|------|------|
| First use | Did this paper actually introduce it? | Yes | Earlier work exists |
| Correct authors | Are these the actual originators? | Yes | Different team |
| Method description | Is the method correctly described? | Yes | Mischaracterized |

**Red flags:**
- Method actually introduced in earlier paper
- Citing application paper instead of methods paper
- Multiple simultaneous originators

### Mechanism Claims

**Claim pattern:** "X causes/regulates/controls Y"

| Check | Question | Pass | Fail |
|-------|----------|------|------|
| Evidence level | Direct evidence or inference? | Direct shown | Correlation only |
| Biological context | Same organism/tissue/conditions? | Yes | Different context |
| Causation proven | Causal or correlational evidence? | Matches claim | Overclaimed |

**Red flags:**
- Correlation cited as causation
- In vitro evidence cited for in vivo claims
- Model organism results generalized to human

### Dataset Claims

**Claim pattern:** "Dataset X contains Y samples"

| Check | Question | Pass | Fail |
|-------|----------|------|------|
| Number accuracy | Does dataset actually have Y samples? | Yes | Different count |
| Version match | Is this the current version? | Yes or noted | Outdated count |
| Subset clarity | Is the subset specified correctly? | Yes | Ambiguous |

**Red flags:**
- Citing v1 statistics for v4 dataset
- Total count vs. after QC filtering
- Training set vs. full dataset confusion

---

## Common Mismatch Patterns

### Type A: Wrong Citation (Paper doesn't discuss topic)

**Detection:**
- Paper title doesn't mention claimed topic
- Abstract doesn't contain relevant keywords
- Different research area entirely

**Common causes:**
- Copy-paste error from reference manager
- Confused with similarly-named paper
- Citation intended for different sentence

**Fix:** Find correct paper or remove citation

### Type B: Overclaim (Text exaggerates paper's findings)

**Detection:**
- Paper uses hedging language; text uses definitive
- Paper shows marginal improvement; text claims breakthrough
- Paper notes limitations; text ignores them

**Common causes:**
- Enthusiasm for results
- Summarization loses nuance
- Telephone game through multiple reviews

**Fix:** Soften claim language to match paper

### Type C: Underclaim (Text undersells paper's findings)

**Detection:**
- Paper shows strong results; text is dismissive
- Paper has broader applicability than text suggests
- Missing important finding from paper

**Common causes:**
- Older text not updated for revised paper
- Conservative interpretation
- Narrative needs shaped claim

**Fix:** Update text to reflect actual findings (if relevant)

### Type D: Outdated Citation (Superseded information)

**Detection:**
- Preprint now published with different results
- Newer paper contradicts or supersedes
- Dataset/method has been updated

**Common causes:**
- Text written before publication
- Didn't check for updates
- Original source preference over primary

**Fix:** Update to current source with current findings

### Type E: Misattribution (Wrong paper credited)

**Detection:**
- Method originated in earlier paper
- Multiple papers claim credit
- Review cited instead of primary source

**Common causes:**
- Citing familiar paper over original
- Following existing citation chains
- Different contribution being credited

**Fix:** Cite primary/original source

---

## Retraction Detection

### Retraction Sources

1. **Retraction Watch Database**
   - Most comprehensive
   - Search by title, author, DOI
   - http://retractiondatabase.org

2. **PubMed**
   - Retraction notices linked to original
   - Search: `[PMID] retracted`
   - Retracted articles marked in search results

3. **Publisher Sites**
   - Retraction notices on article page
   - "RETRACTED" watermark on PDF
   - Linked expression of concern

4. **Google Scholar**
   - Sometimes shows retraction notices
   - May link to retraction announcement

### Retraction Web Search Template

```
"[exact paper title]" retraction OR retracted
"[first author surname]" "[year]" retracted
site:retractionwatch.com "[paper title keywords]"
```

### Retraction Severity Assessment

| Factor | Higher Severity | Lower Severity |
|--------|-----------------|----------------|
| Centrality | Main evidence for claim | Supporting citation |
| Retraction reason | Fraud, fabrication | Honest error, duplicate |
| Affected content | Specific data cited | General method cited |
| Alternatives | No other sources | Multiple corroborating sources |

---

## Preprint Audit

### Identifying Preprints

**BibTeX indicators:**
```bibtex
@misc{...}  % Often used for preprints
  eprint = {...}
  archiveprefix = {arXiv}
  journal = {arXiv preprint}
  journal = {bioRxiv}
```

**URL patterns:**
- `arxiv.org/abs/XXXX.XXXXX`
- `biorxiv.org/content/10.1101/`
- `medrxiv.org/content/10.1101/`
- `ssrn.com/abstract=`

### Publication Status Check

1. **Google Scholar**
   - Search exact title in quotes
   - Look for journal version in results
   - Check "All versions" for updates

2. **Semantic Scholar**
   - Often tracks preprint-to-publication links
   - Shows publication venue

3. **Author Pages**
   - Google Scholar profile
   - Personal/lab website
   - ORCID profile

4. **Publisher/Journal Search**
   - Search author name + keywords
   - Check recent issues of likely venues

### Preprint Age Thresholds

| Age | ML (arXiv cs/stat) | Bio (bioRxiv/medRxiv) |
|-----|-------------------|----------------------|
| < 6 months | Normal | Normal |
| 6-12 months | Normal | Check for publication |
| 12-18 months | Check | Recommend publication check |
| 18-24 months | Note | Flag as stale |
| > 24 months | Flag | Strongly flag, verify validity |

### Preprint Update BibTeX Template

When updating from preprint to published:

```bibtex
% Before (preprint)
@misc{author2023preprint,
  title = {Paper Title},
  author = {Author, First and Second, Author},
  year = {2023},
  eprint = {2301.12345},
  archiveprefix = {arXiv},
  primaryclass = {cs.LG}
}

% After (published)
@article{author2024published,
  title = {Paper Title},
  author = {Author, First and Second, Author},
  journal = {Nature Methods},
  volume = {21},
  pages = {123--135},
  year = {2024},
  doi = {10.1038/s41592-024-01234-5}
}
```

**Note:** Update citation key if semantically appropriate (year changed, etc.)

---

## Verification Priority Matrix

| Claim Type | Verification Level | Frequency |
|------------|-------------------|-----------|
| Performance numbers | Deep | All instances |
| Comparisons | Deep | All instances |
| Dataset statistics | Surface + spot | 20% sample |
| Attribution | Relevance | First mention |
| Mechanism | Relevance | Key claims |
| Historical | Surface | First mention |
| General background | Surface | Rare |

---

## Reporting Template

For each verified citation:

```markdown
### [@citation_key] Line N

**Claim in text:**
> [Exact quote of claim]

**Paper says:**
> [Relevant quote from paper or summary]

**Verification status:** [Verified / Mismatch / Unverifiable]

**Issues (if any):**
- [Specific discrepancy]

**Recommendation:**
- [Action to take]
```

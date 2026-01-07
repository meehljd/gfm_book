# Fact Checker Agent

Validate that factual claims are properly cited, verify citation-claim alignment, detect paper retractions, and flag preprints that should be updated to peer-reviewed versions.

## When to Use This Agent

This agent should be automatically invoked when:
- User asks to "fact check" or "verify citations" in a chapter
- User wants to check if claims are "properly supported" or "cited"
- User asks about "missing citations" or "unsupported claims"
- User mentions "retractions" or "retracted papers"
- User wants to replace "preprints" with "published versions"
- User asks to audit "citation quality" or "reference accuracy"

## Invocation

```
/fact-check <chapter> [--mode <mode>]
```

**Examples:**
- `/fact-check p3-ch14-dna-lm` - Full fact-checking audit
- `/fact-check p3-ch14-dna-lm --mode claims` - Only identify unsupported claims
- `/fact-check p3-ch14-dna-lm --mode verify` - Verify existing citations support their claims
- `/fact-check p3-ch14-dna-lm --mode retractions` - Check for retracted papers
- `/fact-check p3-ch14-dna-lm --mode preprints` - Audit preprint status
- `/fact-check` - Book-wide citation health audit

## Modes

### Mode 1: Full Audit (default)
Complete citation integrity check: unsupported claims, citation-claim verification, retraction check, and preprint audit.

### Mode 2: Claims (`--mode claims`)
Identify factual claims lacking citations. Flag with `*[Citation Needed]*`.

### Mode 3: Verify (`--mode verify`)
Verify that each citation actually supports the claim it accompanies.

### Mode 4: Retractions (`--mode retractions`)
Check all cited papers against known retraction databases.

### Mode 5: Preprints (`--mode preprints`)
Identify preprints and check if peer-reviewed versions are now available.

---

## Claim Identification

### Claims Requiring Citations

Not all statements need citations. Target factual claims that are:

| Claim Type | Needs Citation | Example |
|------------|----------------|---------|
| Quantitative results | YES | "achieves 0.94 auROC on variant classification" |
| Performance comparisons | YES | "outperforms *CADD* by 15%" |
| Historical firsts | YES | "the first model to use..." |
| Biological mechanisms | USUALLY | "enhancers regulate gene expression over 1Mb" |
| Model architecture details | IF SPECIFIC | "uses 12 transformer layers with 768 hidden dimensions" |
| Dataset statistics | YES | "contains 125,748 exomes" |
| Attribution claims | YES | "introduced by Avsec et al." |
| Method descriptions | IF NOVEL | "the attention mechanism computes..." |
| General ML knowledge | NO | "transformers use self-attention" |
| Mathematical definitions | NO | "softmax normalizes scores to probabilities" |

### Claim Detection Patterns

**High-priority patterns (likely need citations):**
1. Specific numbers: percentages, counts, measurements
2. Comparative claims: "better than", "outperforms", "improves over"
3. Temporal claims: "first", "originally", "pioneered", "introduced"
4. Attribution phrases: "proposed by", "developed at", "according to"
5. Benchmark results: "on [dataset], achieves..."
6. Biological facts: specific distances, rates, mechanisms

**Medium-priority patterns (context-dependent):**
1. Architecture specifications: layer counts, dimensions, context lengths
2. Training details: dataset sizes, compute requirements
3. Mechanism descriptions: how models/biology works
4. Historical context: when methods emerged

**Low-priority patterns (usually no citation needed):**
1. Definitions of standard terms
2. Mathematical formulations
3. General domain knowledge
4. Logical conclusions from cited work

### Task 1: Claim Scan

For each section:
1. Identify all factual claims using patterns above
2. Check if claim has accompanying citation `[@...]`
3. Assess claim severity: Critical / Important / Minor
4. Flag uncited claims with `*[Citation Needed]*` or `*[Citation Needed: specific-topic]*`

---

## Citation-Claim Verification

### Verification Framework

For each citation, verify:

| Check | Question | Red Flag |
|-------|----------|----------|
| **Relevance** | Does paper actually discuss this topic? | Citation to tangentially related work |
| **Support** | Does paper's data support the specific claim? | Claim extrapolates beyond paper's findings |
| **Accuracy** | Are numbers/details correctly quoted? | Misquoted statistics or methods |
| **Context** | Is the citation used in appropriate context? | Paper cited for claim it contradicts |
| **Currency** | Is this the best/latest source? | Superseded by newer definitive work |

### Common Citation Problems

**Type A: Wrong Citation**
- Paper doesn't discuss the claimed topic
- Likely copy-paste error or citation confusion

**Type B: Overclaim**
- Paper shows modest effect; text claims dramatic improvement
- Paper shows correlation; text claims causation
- Paper shows specific case; text generalizes broadly

**Type C: Underclaim**
- Paper actually makes stronger claims than text suggests
- Missed opportunity to strengthen argument

**Type D: Outdated Citation**
- Preprint now published with different findings
- Superseded by more definitive study
- Methods since shown to be flawed

**Type E: Misattribution**
- Credit given to wrong paper/author for contribution
- Review article cited instead of primary source

### Task 2: Citation Verification

For each citation in the chapter:
1. Identify the claim the citation supports
2. Assess whether paper actually supports claim (may require web lookup)
3. Check if numbers/details are accurately quoted
4. Flag mismatches with severity: Error / Warning / Note

---

## Retraction Detection

### Retraction Check Process

1. **Extract all citations** from chapter's `.bib` file
2. **Check against retraction databases:**
   - Retraction Watch Database
   - PubMed retraction notices
   - Publisher retraction notices
3. **Flag any retracted papers** with severity based on:
   - How central is the citation to the chapter's argument?
   - Is the retraction for the specific findings cited?
   - Are alternative citations available?

### Retraction Severity

| Severity | Criteria | Action |
|----------|----------|--------|
| CRITICAL | Retracted paper is primary source for key claim | Must replace immediately |
| HIGH | Retracted paper supports important claim | Find alternative source |
| MEDIUM | Retracted paper is one of several sources | Consider removing |
| LOW | Retracted for issues unrelated to cited content | Note but may keep |

### Task 3: Retraction Scan

1. Parse bibliography for all paper identifiers (DOI, PMID, arXiv ID)
2. Check retraction status via web search
3. For retracted papers, assess impact on chapter content
4. Recommend replacement citations where possible

---

## Preprint Audit

### ML/Genomics Preprint Policy

This is an ML/genomics textbook. Our preprint policy:

| Venue | Policy | Notes |
|-------|--------|-------|
| **arXiv (cs.*, stat.*)** | ALLOWED | Standard in ML; many never formally published |
| **bioRxiv/medRxiv** | PREFER PUBLISHED | Biological claims warrant peer review |
| **SSRN, other preprints** | CASE-BY-CASE | Assess field norms |

### Preprint Identification

Detect preprints by:
- URL patterns: `arxiv.org`, `biorxiv.org`, `medrxiv.org`
- BibTeX fields: `eprint`, `archiveprefix`
- Journal field: "arXiv preprint", "bioRxiv"
- Year/status: No volume/pages, recent date

### Preprint Check Workflow

For each identified preprint:

1. **Check publication status:**
   - Search paper title in Google Scholar
   - Check author pages for updated publication list
   - Search venue proceedings/journal archives

2. **If now published:**
   - Note published venue, DOI
   - Compare findings (any changes from preprint?)
   - Recommend bibliography update

3. **If still preprint:**
   - Assess time since posting (>18 months = concerning for non-ML)
   - Check for concerning comments/critiques
   - For bioRxiv/medRxiv: recommend finding alternative or noting limitation

### Task 4: Preprint Audit

1. Identify all preprints in chapter bibliography
2. Check each for peer-reviewed publication
3. For ML preprints (arXiv cs/stat): Note but accept
4. For bio preprints: Strongly recommend update if published version exists
5. Flag stale preprints (>18 months, no publication) for review

---

## Output Format

Save report to `meta/reports/fact-check-[chapter]-YYYY-MM-DD.md`:

```markdown
# Fact Check Report: [Chapter Title]

Generated: [timestamp]
File: [path]
Total citations: N
Claims checked: N

## Executive Summary

| Check | Status | Count |
|-------|--------|-------|
| Unsupported claims | [pass/warn/fail] | N claims flagged |
| Citation-claim alignment | [pass/warn/fail] | N mismatches |
| Retracted papers | [pass/warn/fail] | N found |
| Preprint status | [pass/warn/fail] | N need update |

**Overall Assessment**: [CLEAN / NEEDS ATTENTION / CRITICAL ISSUES]

---

## Unsupported Claims

### Critical (Must Cite)

| Line | Claim | Suggested Citation Topic |
|------|-------|-------------------------|
| 145 | "achieves 0.95 auROC on pathogenic variants" | Model benchmark paper |

### Important (Should Cite)

| Line | Claim | Suggested Citation Topic |
|------|-------|-------------------------|

### Minor (Consider Citing)

| Line | Claim | Notes |
|------|-------|-------|

---

## Citation-Claim Verification

### Mismatches Found

#### [@citation_key] at Line N

**Claim in text:**
> [Quote the claim]

**Issue**: [Type A-E from framework]

**Details**: [Explanation of mismatch]

**Recommendation**: [Suggested fix]

---

### Verified (Spot Checks)

| Citation | Claim | Status |
|----------|-------|--------|
| [@key1] | "[brief claim]" | Verified |
| [@key2] | "[brief claim]" | Verified |

---

## Retraction Check

### Retracted Papers Found

| Citation Key | Paper | Retraction Date | Reason | Impact |
|--------------|-------|-----------------|--------|--------|

### Retraction-Free

All N papers checked against Retraction Watch Database. No retractions found.

---

## Preprint Audit

### Now Published (Update Required)

| Citation Key | Preprint | Published Version | DOI |
|--------------|----------|-------------------|-----|
| [@key] | arXiv:2301.xxxxx | Nature Methods 2024 | 10.xxxx |

**Recommended BibTeX update:**
```bibtex
@article{key,
  ...updated entry...
}
```

### ML Preprints (Acceptable)

| Citation Key | Venue | Age | Status |
|--------------|-------|-----|--------|
| [@key1] | arXiv cs.LG | 8 mo | OK - standard for ML |

### Bio Preprints (Review Recommended)

| Citation Key | Venue | Age | Concern |
|--------------|-------|-----|---------|
| [@key2] | bioRxiv | 24 mo | Stale - no publication, check validity |

---

## Recommendations

### High Priority
1. [Specific action item with line numbers]

### Medium Priority
1. [Action item]

### Low Priority
1. [Action item]

---

## Methodology Notes

- Claims identified using pattern matching for quantitative/comparative statements
- Citation verification performed via [web search / paper review / spot check]
- Retraction status checked via [source]
- Preprint status checked via [Google Scholar / publisher sites]
```

---

## Reference Files

This agent has access to:
- `claim-patterns.md` - Detailed patterns for claim identification
- `verification-checklist.md` - Citation verification checklist
- Chapter `.bib` files in `bib/pN/`
- Chapter `.qmd` files in `part_*/`

---

## Workflow

### Single Chapter Audit

1. **Read chapter**: Load full `.qmd` content
2. **Load bibliography**: Parse corresponding `.bib` file
3. **Claim scan**: Identify all factual claims, check for citations
4. **Citation verification**: Spot-check N citations for claim support
5. **Retraction check**: Search for retraction notices on all papers
6. **Preprint audit**: Identify preprints, check publication status
7. **Generate report**: Save to `meta/reports/`

### Book-Wide Audit

1. **Aggregate bibliographies**: Collect all citations across chapters
2. **Deduplicate**: Identify papers cited multiple times
3. **Batch retraction check**: Check all unique papers
4. **Preprint inventory**: List all preprints with status
5. **Coverage analysis**: Which chapters have most unsupported claims?
6. **Summary report**: Book-wide citation health metrics

---

## Web Search Strategies

### For Retraction Checks

```
"[paper title]" retracted OR retraction
"[first author] [year]" retracted
site:retractionwatch.com "[paper title]"
```

### For Preprint Publication Status

```
"[paper title]" site:doi.org
"[paper title]" journal OR published -arxiv -biorxiv
"[first author] [year]" "[shortened title]"
```

### For Citation Verification

```
"[paper title]" "[specific claim or number]"
"[first author] [year]" "[claimed finding]"
```

---

## Coordination with Other Agents

This agent complements:
- `paper-review` - Evaluates new papers; fact-checker validates existing citations
- `review-chapter` - Reviews content quality; fact-checker focuses on citation integrity
- `/bib-audit` - Checks bibliography formatting; fact-checker checks content accuracy

---

## Special Considerations

### Foundational Papers

For seminal works (pre-2015), verification may be limited to:
- Confirming paper exists and is correctly attributed
- Checking for subsequent retractions or corrections
- Verifying claims haven't been superseded

### Industry Papers (Google, Meta, etc.)

- May lack formal peer review but underwent internal review
- Treat as equivalent to peer-reviewed for citation purposes
- Note if methods require unavailable resources

### Consortium Data

For claims about datasets (gnomAD, GTEx, ENCODE):
- Verify statistics against official documentation
- Check if numbers reflect current release vs. cited version
- Note version discrepancies

### Model Benchmark Claims

For performance comparisons:
- Verify benchmark dataset and version
- Check if comparison is apples-to-apples (same test set)
- Note if leaderboard has been updated since publication

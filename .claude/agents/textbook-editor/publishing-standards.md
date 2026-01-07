# Publishing Standards

Industry standards for scientific textbook manuscript preparation and submission.

---

## Manuscript Specifications

### Word Count Guidelines

| Book Type | Typical Range | Notes |
|-----------|---------------|-------|
| Undergraduate textbook | 100,000-200,000 | More explanatory text |
| Graduate textbook | 80,000-150,000 | Denser, assumes more background |
| Reference/handbook | 150,000-300,000 | Comprehensive coverage |
| Monograph | 60,000-100,000 | Focused, specialized |
| Trade science | 60,000-90,000 | Accessible, narrative-driven |

### Chapter Specifications

| Metric | Typical Range | Notes |
|--------|---------------|-------|
| Chapters per book | 12-25 | More chapters = more modularity |
| Words per chapter | 4,000-10,000 | 6,000-8,000 is sweet spot |
| Variance tolerance | ±30% from mean | Larger variance signals structural issues |
| Figures per chapter | 3-10 | 1 per 1,000 words minimum |
| Tables per chapter | 1-5 | Complement but don't replace prose |
| References per chapter | 30-100 | Field-dependent |

### Section Hierarchy

Standard levels:
1. **Part** (optional) - Major book divisions
2. **Chapter** - Primary unit
3. **H1 Section** - Major sections within chapter (3-7 typical)
4. **H2 Subsection** - Subdivisions (2-5 per section)
5. **H3 Subsubsection** - Use sparingly (avoid if possible)

**Rule**: Avoid more than 3 levels of nesting within a chapter.

---

## Formatting Requirements

### Standard Manuscript Format

| Element | Specification |
|---------|---------------|
| Font | 12pt Times New Roman or similar |
| Spacing | Double-spaced body text |
| Margins | 1 inch all sides |
| Alignment | Left-aligned (ragged right) |
| Paragraphs | First-line indent OR block with space between |
| Page numbers | Bottom center or top right |
| Headers | Chapter/section running heads |

### Chapter Structure Template

```
CHAPTER N: TITLE

[Chapter opener/hook - 1-2 paragraphs]

LEARNING OBJECTIVES (optional)
• Objective 1
• Objective 2
• Objective 3

SECTION 1.1: FIRST MAJOR SECTION
[Content]

    1.1.1 Subsection
    [Content]

SECTION 1.2: SECOND MAJOR SECTION
[Content]

[Continue sections...]

CHAPTER SUMMARY (optional)
[Key takeaways in prose or bullet form]

KEY TERMS
term1, term2, term3...

DISCUSSION QUESTIONS (optional)
1. Question 1
2. Question 2

REFERENCES
[Chapter-specific references or pointer to book-end bibliography]
```

---

## Figure Requirements

### Technical Specifications

| Format | Use Case | Resolution |
|--------|----------|------------|
| TIFF | Primary for print | 300 DPI minimum, 600 for line art |
| EPS | Vector graphics | Resolution-independent |
| PDF | Vector graphics | Resolution-independent |
| PNG | Web/supplementary | 150 DPI minimum |
| JPEG | Photos only | 300 DPI, minimal compression |

### Figure Sizing

| Placement | Width | Notes |
|-----------|-------|-------|
| Full page | 6.5" / 165mm | Maximum for standard book |
| Column width | 3.25" / 82mm | Two-column layouts |
| Half page | 4.5" / 114mm | Common for diagrams |

### Figure Labeling

- Sequential numbering within chapter: Figure 3.1, 3.2, 3.3...
- Alternatively: Figure 3-1, 3-2, 3-3...
- Consistent format throughout book
- Every figure must be referenced in text

### Figure Files

For submission:
- Separate high-resolution files (not embedded)
- Named consistently: `ch03_fig01.tiff`, `ch03_fig02.eps`
- Accompanied by figure list with captions
- Permissions documented for all third-party figures

---

## Table Requirements

### Formatting Standards

- No vertical lines (modern style)
- Horizontal lines: top, under headers, bottom
- Column heads aligned with data
- Units in column heads, not repeated in cells
- Notes below table for clarifications

### Table Template

```
Table N.N: Descriptive Title in Sentence Case

| Column A | Column B (units) | Column C (units) |
|----------|------------------|------------------|
| Row 1    | value            | value            |
| Row 2    | value            | value            |

Note: Explanation of abbreviations or special cases.
Source: Citation if adapted from elsewhere.
```

---

## Citation and Reference Requirements

### Citation Style Options

| Style | Common In | Format |
|-------|-----------|--------|
| Author-date | Sciences | (Smith 2023) |
| Numbered | Engineering | [1], [2] |
| Superscript | Biomedical | text^1,2 |
| Footnote | Humanities | (less common in science) |

### Reference Entry Components

Required:
- Author(s) - full list or et al. format
- Year
- Title
- Source (journal, book, conference)
- Volume/issue/pages OR DOI

Strongly recommended:
- DOI for all journal articles
- URL for online-only resources
- Access date for web resources

### Reference List Format

Alphabetical by author (author-date) or numbered by order of citation (numbered style).

Example (author-date):
```
Smith, J. A., & Jones, B. C. (2023). Deep learning for genomics:
    A comprehensive review. Nature Genetics, 55(3), 234-245.
    https://doi.org/10.1038/s41588-023-01234-5
```

---

## Front Matter Requirements

### Standard Components

| Component | Required | Notes |
|-----------|----------|-------|
| Half-title page | Yes | Title only |
| Title page | Yes | Title, subtitle, authors, publisher |
| Copyright page | Yes | Publisher provides template |
| Dedication | Optional | Brief |
| Table of contents | Yes | Chapter and section levels |
| List of figures | Optional | For figure-heavy books |
| List of tables | Optional | For table-heavy books |
| Preface | Recommended | Author's framing of book |
| Acknowledgments | Recommended | Often part of preface |
| About the authors | Recommended | Brief bios |

### Preface Elements

A strong preface includes:
1. Why this book exists (gap it fills)
2. Who it's for (target audience)
3. How to use it (reading paths)
4. What's included/excluded (scope)
5. Acknowledgments (people who helped)
6. How to provide feedback (optional)

---

## Back Matter Requirements

### Standard Components

| Component | Required | Notes |
|-----------|----------|-------|
| Appendices | If needed | Supplementary technical material |
| Glossary | Recommended | Essential for technical books |
| Bibliography | If not per-chapter | Consolidated references |
| Index | Required for print | Author-generated keywords, professional indexer |
| About the author | If not in front | Author bio and photo |

### Glossary Format

```
**Term**: Definition in complete sentence. Context for usage if needed.

**Another term**: Definition. See also: *related term*.
```

### Index Preparation

Authors typically provide:
- Keyword list (main entries)
- Cross-reference suggestions
- Subentry groupings

Professional indexer produces final index from typeset pages.

---

## Permissions and Rights

### What Requires Permission

| Content Type | Permission Needed? |
|--------------|-------------------|
| Figures you created | No |
| Figures adapted from others | Usually yes, cite original |
| Figures reproduced exactly | Yes, formal permission |
| Tables with others' data | Usually yes if substantial |
| Extended quotations (>300 words) | Yes |
| Short quotations (<100 words) | No, but cite |
| Paraphrased ideas | No, but cite |
| Public domain content | No, but cite |
| Open access (CC-BY) | No, but cite and note license |
| Open access (CC-BY-NC) | Depends on commercial use |

### Permission Documentation

For each third-party figure/table:
1. Source citation (original publication)
2. License type OR permission letter
3. Any required attribution language
4. Fee paid (if applicable)
5. Restrictions (if any)

---

## Publisher Submission Package

### Proposal Components

| Document | Purpose |
|----------|---------|
| Cover letter | Introduction, why this publisher |
| Book overview | 1-2 page summary |
| Table of contents | Chapter titles, brief descriptions |
| Sample chapters | 2-3 polished chapters |
| Author bio | Credentials, platform |
| Competitive analysis | Similar books, differentiation |
| Market analysis | Target audience, course adoption potential |
| Timeline | Estimated completion |

### Full Manuscript Submission

| Component | Format |
|-----------|--------|
| Manuscript files | Word/LaTeX, one file per chapter |
| Figure files | Separate, high-resolution, named consistently |
| Figure captions | Separate document |
| Table files | Embedded or separate |
| References | Bibliography file (BibTeX if LaTeX) |
| Permissions log | Documentation for third-party content |
| Supplementary materials | Code, datasets, online resources |

---

## Production Timeline

### Typical Phases

| Phase | Duration | Activities |
|-------|----------|------------|
| Proposal to contract | 2-6 months | Negotiation, review |
| Writing | 12-24 months | Drafting, revision |
| Developmental edit | 2-4 months | Structural feedback |
| Copy edit | 1-2 months | Line-level corrections |
| Typesetting | 1-2 months | Layout, design |
| Proofreading | 2-4 weeks | Author reviews pages |
| Indexing | 2-4 weeks | After final pages |
| Printing/release | 1-2 months | Manufacturing, distribution |

**Total**: 18-36 months from contract to publication

---

## Quality Checklist

### Before Submission

- [ ] All chapters complete and consistent length
- [ ] Figures high-resolution with captions
- [ ] References complete and consistent format
- [ ] Cross-references all resolve
- [ ] Permissions documented for third-party content
- [ ] Front matter drafted (preface, acknowledgments)
- [ ] Glossary terms compiled
- [ ] Index keywords identified
- [ ] Spelling and grammar checked
- [ ] Style guide applied consistently

### Common Issues to Avoid

- Inconsistent formatting across chapters
- Missing or low-resolution figures
- Incomplete references (missing DOIs, pages)
- Broken cross-references
- Undefined acronyms
- Inconsistent terminology
- Placeholder text remaining
- Copyright issues with figures
- Chapters that differ drastically in length
- Front/back matter incomplete

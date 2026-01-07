# GFM Book Project

A Quarto-based textbook on **Genomic Foundation Models** covering deep learning architectures for DNA, RNA, and protein sequence analysis.

## Book Structure

The book has **31 chapters** organized into **6 parts** plus appendices:

| Part | Title | Chapters | Focus |
|------|-------|----------|-------|
| 1 | Data Foundations | 1-4 | Sequencing, datasets, GWAS, classical VEP |
| 2 | Learning & Evaluation | 5-12 | Representations, CNNs, attention, pretraining, benchmarks |
| 3 | Foundation Model Families | 13-17 | DNA-LMs, protein-LMs, regulatory models, VEP |
| 4 | Multi-Modal Models | 18-22 | RNA, single-cell, 3D genome, networks, multi-omics |
| 5 | Responsible Deployment | 23-26 | Uncertainty, interpretability, causality, regulation |
| 6 | Applications & Frontiers | 27-31 | Clinical risk, rare disease, drug discovery, design |

## File Naming Conventions

```
part_N/pN-chXX-topic.qmd     # Chapter files (e.g., part_3/p3-ch14-dna-lm.qmd)
part_N/pN--partname.qmd      # Part intro files (double dash)
appendix/app-X-topic.qmd     # Appendix files
bib/pN/pN-chXX.bib           # Per-chapter bibliography files
```

**Cross-reference IDs** follow `sec-chXX-topic` pattern (see `_quarto.yml` comments).

## Directory Structure

```
/
├── part_1/ through part_6/  # Chapter content (.qmd files)
├── appendix/                # Appendices A-F
├── bib/                     # Bibliography files organized by part
│   ├── p1/ through p6/      # Per-chapter .bib files
│   ├── apx/                 # Appendix bibliographies
│   └── references.qmd       # References page
├── figs/                    # Figures organized by part/chapter
├── docs/                    # Rendered HTML output (git-tracked for GitHub Pages)
├── meta/                    # Project metadata and documentation
│   ├── qmd_headings.md      # Extracted headings from all chapters
│   ├── cross-reference-proposals.md
│   ├── papers-to-add.md     # Papers to potentially incorporate
│   ├── _instructions/       # Detailed writing instructions
│   ├── glossary/            # Glossary management files
│   ├── paper-reviews/       # Paper review notes
│   └── reports/             # Output from slash commands
├── scripts/                 # Utility scripts (see below)
├── TODO/                    # Planning documents
├── .claude/                 # Claude Code configuration
│   ├── commands/            # Slash command definitions
│   └── agents/              # Agent definitions
└── _quarto.yml              # Book configuration
```

## Scripts

### Extract Headers (`scripts/extract_headers.py`)
Regenerates `meta/qmd_headings.md` with all chapter headings:
```bash
python scripts/extract_headers.py
```

### Combine Book (`scripts/combine_quarto_book.py`)
Combines all chapters into a single file (useful for full-text analysis):
```bash
python scripts/combine_quarto_book.py combined.qmd
```

### Count Words (`scripts/count_book_words.sh`)
Counts words across all chapters with exclusion support:
```bash
./scripts/count_book_words.sh
```

### Watermark PNGs (`scripts/watermark_pngs.py`)
Adds watermarks to placeholder figures:
```bash
python scripts/watermark_pngs.py ./figs --inplace --text "PLACEHOLDER"
```

## Slash Commands

Run these for quality checks (output to `meta/reports/`):

| Command | Purpose | Example |
|---------|---------|---------|
| `/structure` | Analyze section structure and balance | `/structure` or `/structure p3-ch14` |
| `/glossary` | Check glossary term usage | `/glossary`, `/glossary coverage` |
| `/xref-check` | Validate cross-references | `/xref-check` or `/xref-check p3-ch14` |
| `/todos` | Organize TODOs and editing tasks | `/todos` or `/todos p3-ch14` |
| `/bib-audit` | Audit bibliography integrity | `/bib-audit` or `/bib-audit p3-ch14` |
| `/figures` | Inventory figures and placeholders | `/figures` or `/figures p3-ch14` |
| `/redundancy` | Find repeated content | `/redundancy` or `/redundancy ClinVar` |
| `/style-check` | Check style guide compliance | `/style-check` or `/style-check p3-ch14` |

## Agents

More complex review tools in `.claude/agents/`:

| Agent | Purpose |
|-------|---------|
| `review-chapter` | Deep chapter review (36 checks) |
| `paper-review` | Evaluate papers for book inclusion |
| `pedagogy-review` | Learning science optimization |
| `pre-commit` | Pre-commit content/style review |
| `figure-design` | Figure opportunities, design, captions, AI image prompts |

### Figure Design Agent

The `figure-design` agent specializes in visual communication:

```bash
# Full audit: opportunities + design + captions + AI prompts
/figure-design p3-ch14-dna-lm

# Just identify what needs figures
/figure-design p3-ch14-dna-lm --mode identify

# Generate AI prompts for placeholders
/figure-design p3-ch14-dna-lm --mode prompts

# Review/rewrite captions
/figure-design p3-ch14-dna-lm --mode captions
```

Generates prompts optimized for:
- **ChatGPT/DALL-E**: Scientific diagrams, conceptual illustrations
- **Sora**: Process animations, temporal sequences
- **Fallback**: Manual creation descriptions

## Key Reference Files

| File | Purpose |
|------|---------|
| `meta/qmd_headings.md` | All chapter headings (regenerate with `extract_headers.py`) |
| `meta/_instructions/section_titles.md` | Canonical section titles |
| `meta/_instructions/ref-instructions.md` | Citation/reference guidelines |
| `meta/glossary/glossary-core-245.md` | Core glossary terms |
| `meta/papers-to-add.md` | Papers under consideration |
| `meta/cross-reference-proposals.md` | Cross-reference suggestions |
| `TODO/restructure-plan.md` | Restructuring documentation |

## Common Tasks

### After restructuring chapters
```bash
python scripts/extract_headers.py  # Update headings file
```

### Before editing a chapter
```bash
# Get chapter overview
/structure p3-ch14

# Check existing issues
/xref-check p3-ch14
/todos p3-ch14
```

### Quality review workflow
```bash
/style-check      # Style compliance
/glossary         # Term consistency
/bib-audit        # Citation integrity
/redundancy       # Content overlap
/figures          # Figure completeness
```

### Building the book
```bash
quarto preview    # Live preview
quarto render     # Full render to docs/
```

## Style Notes

- Use `@citation-key` for citations (keys defined in per-chapter .bib files)
- Cross-references: `@sec-chXX-topic` for sections, `@fig-name` for figures
- Math: Use `$...$` for inline, `$$...$$` for display
- Callouts: `:::{.callout-note}`, `:::{.callout-warning}`, etc.
- Figures: Place in `figs/part_N/chXX/` with descriptive names

## Important Notes

- The `docs/` directory is the rendered output for GitHub Pages - avoid editing directly
- Each chapter has its own `.bib` file in `bib/pN/`
- Reports from slash commands go to `meta/reports/` with date stamps
- When adding new chapters, update `_quarto.yml` and create corresponding `.bib` file

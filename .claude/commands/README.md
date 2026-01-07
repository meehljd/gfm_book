# GFM Book Slash Commands

Custom Claude Code slash commands for editing the Genomic Foundation Models book.

## Available Commands

| Command | Purpose | Usage |
|---------|---------|-------|
| `/xref-check` | Validate cross-references | `/xref-check` or `/xref-check p3-ch11` |
| `/bib-audit` | Audit bibliography integrity | `/bib-audit` or `/bib-audit p3-ch11` |
| `/style-check` | Check style guide compliance | `/style-check` or `/style-check p3-ch11` |
| `/structure` | Analyze section structure | `/structure` or `/structure p3-ch11` |
| `/figures` | Inventory figures/placeholders | `/figures` or `/figures p3-ch11` |
| `/todos` | Organize editing tasks | `/todos` or `/todos p3-ch11` |
| `/glossary` | Check glossary term usage | `/glossary`, `/glossary coverage`, `/glossary missing` |
| `/redundancy` | Find repeated content | `/redundancy` or `/redundancy ClinVar` |

## Available Agents

Agents are more complex tools in `.claude/agents/` that run with isolated context:

| Agent | Purpose | Location |
|-------|---------|----------|
| `paper-review` | Evaluate papers for book inclusion | `.claude/agents/paper-review/` |
| `review-chapter` | Deep chapter review (36 checks) | `.claude/agents/review-chapter/` |
| `pre-commit` | Pre-commit content/style review | `.claude/agents/pre-commit/` |
| `pedagogy-review` | Learning science optimization | `.claude/agents/pedagogy-review/` |
| `figure-design` | Figure opportunities, design, captions, AI prompts | `.claude/agents/figure-design/` |

## Output Location

All reports are saved to `meta/reports/` with timestamps:
- `meta/reports/xref-check-2025-01-06.md`
- `meta/reports/bib-audit-2025-01-06.md`
- etc.

## Recommended Workflow

### Initial Assessment
```
/structure          # Understand book balance
/todos              # See what's flagged for editing
```

### Before Editing a Chapter
```
# Use the review-chapter agent for deep review:
# Ask Claude to "review chapter p3-ch11-dna-lm using the review-chapter agent"
/xref-check p3-ch11               # Check its references
```

### Quality Pass
```
/style-check        # Enforce style guide
/glossary           # Check term consistency
/bib-audit          # Verify citations
# Use pedagogy-review agent for learning science optimization
```

### Final Review
```
/redundancy         # Find content to consolidate
/figures            # Verify all figures present
```

## Command Files

Each command is defined in a `.md` file in this directory:
- [xref-check.md](xref-check.md) - Cross-reference validation
- [bib-audit.md](bib-audit.md) - Bibliography auditing
- [style-check.md](style-check.md) - Style enforcement
- [structure.md](structure.md) - Structure analysis
- [figures.md](figures.md) - Figure inventory
- [todos.md](todos.md) - TODO organization
- [glossary.md](glossary.md) - Glossary checking
- [redundancy.md](redundancy.md) - Redundancy detection

## Agent Files

Each agent is defined in an `AGENT.md` file in `.claude/agents/<agent-name>/`:
- `paper-review/AGENT.md` - Paper evaluation for book inclusion
- `review-chapter/AGENT.md` - Deep chapter review with 36 checks
- `pre-commit/AGENT.md` - Pre-commit content loss and style review
- `pedagogy-review/AGENT.md` - Learning science optimization (12 evidence-based principles)
- `figure-design/AGENT.md` - Figure opportunities, visual design, captions, AI image prompts

## Customization

Edit the command `.md` files to adjust:
- What the command checks
- Output format
- Rules and thresholds
- Implementation notes

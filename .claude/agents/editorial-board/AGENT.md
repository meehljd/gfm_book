# Editorial Board Agent

Orchestration agent that coordinates comprehensive book reviews by dispatching specialized review agents and synthesizing their findings into unified editorial recommendations.

## When to Use This Agent

This agent should be automatically invoked when:
- User asks for a "comprehensive review" or "full editorial review"
- User wants to "review the book" or "review a part"
- User mentions needing "all the review agents"
- User asks about "publication readiness" for multiple chapters
- User wants coordinated feedback across multiple dimensions

## Invocation

```
/editorial-board <scope> [--focus <focus>] [--depth <depth>]
```

**Examples:**
- `/editorial-board p3-ch14-dna-lm` - Full review of one chapter
- `/editorial-board part_3` - Coordinated review of Part 3
- `/editorial-board` - Book-wide editorial assessment
- `/editorial-board p3-ch14 --focus content` - Major members only (no minor specialists)
- `/editorial-board p3-ch14 --depth quick` - Fast pass with key findings only

## Parameters

### `--focus` Options

| Focus | Agents Dispatched | Use When |
|-------|-------------------|----------|
| `full` (default) | All major + minor | Comprehensive pre-publication review |
| `content` | Major members only | Focus on substance, not polish |
| `polish` | textbook-editor, lean-out, figure-design | Final manuscript polish |
| `pedagogy` | pedagogy-review, course-designer, figure-design | Optimize for learning/teaching |

### `--depth` Options

| Depth | Behavior | Use When |
|-------|----------|----------|
| `full` (default) | Complete reports from each agent | Detailed review needed |
| `standard` | Key findings only from each agent | Regular review cycle |
| `quick` | Executive summaries only | Quick status check |

---

## The Editorial Board

### Major Members (Core Review Team)

These agents provide the primary editorial perspective:

| Agent | Role | Focus |
|-------|------|-------|
| **`chapter-auditor`** | Content Quality Director | Structural integrity, openings/closings, cross-chapter consistency, style rule enforcement |
| **`textbook-editor`** | Line Editor & Publisher Liaison | Prose polish, readability, publication readiness, market positioning |
| **`pedagogy-review`** | Learning Science Specialist | Cognitive load, retrieval practice, spacing, dual coding, transfer |
| **`course-designer`** | Curriculum Development Lead | Teachability, course materials, assessment alignment |

### Minor Members (Specialist Consultants)

These agents provide targeted expertise when needed:

| Agent | Role | Focus |
|-------|------|-------|
| **`fact-checker`** | Citation Integrity Specialist | Unsupported claims, citation-claim alignment, retractions, preprint status |
| **`figure-design`** | Visual Communication Specialist | Figure opportunities, caption quality, visual consistency |
| **`lean-out`** | Content Efficiency Specialist | Diminishing returns content, appendix candidates, redundancy |
| **`math-pedagogy`** | Mathematics Presentation Specialist | Equation formatting, numbering, variable definitions, identifying prose that needs formalization |

### External Consultant (Not Part of Board)

| Agent | Role | When to Engage |
|-------|------|----------------|
| **`literature-critic`** | Literature Evaluation | When considering new papers for inclusion (separate workflow) |

---

## Orchestration Workflow

### Phase 1: Scope Assessment

1. **Determine review scope**: Chapter, Part, or Book
2. **Check review history**: What reviews have been run recently?
3. **Assess content state**: Draft vs. edited vs. near-final
4. **Select agent roster**: Based on `--focus` parameter

### Phase 2: Parallel Dispatch

The Editorial Board dispatches agents in parallel where possible:

```
┌─────────────────────────────────────────────────────────────┐
│                    EDITORIAL BOARD                          │
│                    (Orchestrator)                           │
└─────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
    ┌───────────────┬───────────────┬───────────────┐
    │ MAJOR REVIEWS │ MAJOR REVIEWS │ MAJOR REVIEWS │
    │   (parallel)  │   (parallel)  │   (parallel)  │
    ├───────────────┼───────────────┼───────────────┤
    │ chapter-      │ textbook-     │ pedagogy-     │
    │ auditor       │ editor        │ review        │
    └───────────────┴───────────────┴───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │    SPECIALIST REVIEWS         │
            │        (as needed)            │
            ├───────────────┬───────────────┤
            │ fact-checker  │ figure-design │
            │ lean-out      │               │
            └───────────────┴───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │      SYNTHESIS & REPORT       │
            │    (Editorial Board)          │
            └───────────────────────────────┘
```

### Phase 3: Report Synthesis

1. **Collect individual reports** from each dispatched agent
2. **Identify cross-cutting themes**: Issues flagged by multiple agents
3. **Resolve conflicts**: When agents disagree, provide editorial judgment
4. **Prioritize recommendations**: Critical → High → Medium → Low
5. **Generate unified report**

---

## Review Coordination Logic

### When to Run Each Agent

| Agent | Always Run | Conditional |
|-------|------------|-------------|
| `chapter-auditor` | For chapter/part scope | Skip for quick book-wide |
| `textbook-editor` | For near-final content | Skip for early drafts |
| `pedagogy-review` | Always | - |
| `course-designer` | For teaching prep | Skip unless teaching focus |
| `fact-checker` | For chapters with citations | Skip for intro/overview chapters |
| `figure-design` | For chapters with figures | Skip if no visual content |
| `lean-out` | For long chapters | Skip if under target word count |
| `math-pedagogy` | For chapters with math content | Skip for narrative chapters |

### Agent Dependencies

Some agents benefit from others running first:

```
pedagogy-review  ──► course-designer (pedagogy informs curriculum)
pedagogy-review  ──► math-pedagogy (learning science informs math decisions)
chapter-auditor  ──► textbook-editor (structure before polish)
math-pedagogy    ──► textbook-editor (equations affect prose flow)
textbook-editor  ──► lean-out (polish before cuts)
```

### Conflict Resolution

When agents provide conflicting recommendations:

| Conflict Type | Resolution |
|---------------|------------|
| Style vs. Pedagogy | Pedagogy wins if learning impact is clear |
| Polish vs. Cuts | Evaluate if cut content needs polish at all |
| Structure vs. Flow | Preserve structure unless flow critically impaired |
| Brevity vs. Clarity | Clarity wins for core concepts |

---

## Output Format

Save report to `meta/reports/editorial-board-[scope]-YYYY-MM-DD.md`:

```markdown
# Editorial Board Review: [Scope]

Generated: [timestamp]
Scope: [chapter/part/book]
Focus: [full/content/polish/pedagogy]
Depth: [full/standard/quick]

## Executive Summary

**Overall Assessment**: [Ready / Needs Work / Major Revision]

**Key Findings**:
1. [Most critical cross-cutting issue]
2. [Second priority]
3. [Third priority]

**Readiness by Dimension**:
| Dimension | Grade | Status |
|-----------|-------|--------|
| Structural Quality | A-D | [One-line summary] |
| Prose Polish | A-D | [One-line summary] |
| Pedagogical Effectiveness | A-D | [One-line summary] |
| Visual Communication | A-D | [One-line summary] |
| Citation Integrity | A-D | [One-line summary] |
| Content Efficiency | A-D | [One-line summary] |

---

## Cross-Cutting Themes

Issues identified by multiple agents:

### Theme 1: [Name]
**Flagged by**: [agent-1], [agent-2]
**Details**: [Synthesis of findings]
**Recommendation**: [Unified recommendation]

---

## Individual Agent Reports

### Chapter Auditor

[Summary of chapter-auditor findings]

**Grade**: [A-D]
**Key Issues**:
- [Issue 1]
- [Issue 2]

[Link to full report: meta/reports/audit-[chapter]-YYYY-MM-DD.md]

### Textbook Editor

[Summary of textbook-editor findings]

**Grade**: [A-D]
**Key Issues**:
- [Issue 1]
- [Issue 2]

[Link to full report: meta/reports/editor-[chapter]-YYYY-MM-DD.md]

### Pedagogy Review

[Summary of pedagogy-review findings]

**Grade**: [A-D]
**Key Issues**:
- [Issue 1]
- [Issue 2]

[Link to full report: meta/reports/pedagogy-[chapter]-YYYY-MM-DD.md]

### Course Designer (if run)

[Summary of course-designer findings]

**Teachability Assessment**: [High/Medium/Low]

[Link to full report if applicable]

### Fact Checker (if run)

[Summary of fact-checker findings]

**Citation Health**: [Clean/Needs Attention/Critical Issues]

[Link to full report: meta/reports/fact-check-[chapter]-YYYY-MM-DD.md]

### Figure Design (if run)

[Summary of figure-design findings]

**Visual Coverage**: [Complete/Gaps Identified/Major Gaps]

[Link to full report: meta/reports/figures-[chapter]-YYYY-MM-DD.md]

### Lean-Out (if run)

[Summary of lean-out findings]

**Cut Potential**: [X% validated]

[Link to full report: meta/reports/lean-out-[chapter]-YYYY-MM-DD.md]

---

## Prioritized Action Items

### Critical (Before Any Release)

1. [ ] [Action item with specific location]
2. [ ] [Action item with specific location]

### High (Before Publication)

1. [ ] [Action item]
2. [ ] [Action item]

### Medium (Should Address)

1. [ ] [Action item]
2. [ ] [Action item]

### Low (Nice to Have)

1. [ ] [Action item]

---

## Dissenting Views

Where agents disagreed and editorial judgment was applied:

| Topic | Agent A View | Agent B View | Board Decision |
|-------|--------------|--------------|----------------|
| [Topic] | [Position] | [Position] | [Decision + rationale] |

---

## Review Coverage

| Agent | Status | Report Location |
|-------|--------|-----------------|
| chapter-auditor | [Run/Skipped] | [path or N/A] |
| textbook-editor | [Run/Skipped] | [path or N/A] |
| pedagogy-review | [Run/Skipped] | [path or N/A] |
| course-designer | [Run/Skipped] | [path or N/A] |
| fact-checker | [Run/Skipped] | [path or N/A] |
| figure-design | [Run/Skipped] | [path or N/A] |
| lean-out | [Run/Skipped] | [path or N/A] |

---

## Follow-Up Schedule

Recommended next reviews:

| Timeframe | Recommended Action |
|-----------|-------------------|
| Immediate | [Address critical items] |
| Next week | [Run specific agent on specific scope] |
| Pre-publication | [Final editorial-board review] |
```

---

## Workflow by Scope

### Single Chapter Review

```bash
# Full review of one chapter
/editorial-board p3-ch14-dna-lm

# Workflow:
1. Run chapter-auditor on p3-ch14
2. Run textbook-editor on p3-ch14 (parallel)
3. Run pedagogy-review on p3-ch14 (parallel)
4. If chapter has figures: run figure-design
5. If chapter has citations: run fact-checker
6. If chapter >6000 words: run lean-out
7. Synthesize findings
8. Generate unified report
```

### Part Review

```bash
# Coordinated review of entire Part
/editorial-board part_3

# Workflow:
1. Run chapter-auditor on each chapter (parallel)
2. Run cross-chapter consistency checks
3. Sample 2-3 chapters for textbook-editor deep dive
4. Run pedagogy-review on Part structure
5. Run figure-design inventory for Part
6. Aggregate findings by chapter
7. Identify Part-level themes
8. Generate unified report with chapter breakdown
```

### Book-Wide Review

```bash
# Book-wide editorial assessment
/editorial-board --depth standard

# Workflow:
1. Review Part introductions for narrative arc
2. Sample chapters from each Part for spot checks
3. Run cross-book terminology consistency
4. Assess figure density and style consistency
5. Check for book-wide redundancy
6. Generate strategic recommendations
```

---

## Reference Files

This agent coordinates:
- `chapter-auditor/AGENT.md` - Structural review agent
- `textbook-editor/AGENT.md` - Line editing agent
- `pedagogy-review/AGENT.md` - Learning science agent
- `course-designer/AGENT.md` - Curriculum agent
- `fact-checker/AGENT.md` - Citation integrity agent
- `figure-design/AGENT.md` - Visual communication agent
- `lean-out/AGENT.md` - Content reduction agent

Report outputs go to `meta/reports/`.

---

## Coordination with Other Workflows

### Before Editorial Board Review

Ensure basic quality first:
```bash
/style-check <chapter>   # Fix obvious style issues
/xref-check <chapter>    # Fix broken references
/bib-audit <chapter>     # Fix bibliography issues
```

### After Editorial Board Review

Address findings, then:
```bash
/pre-commit <chapter>    # Pre-commit quality gate
```

### Separate Workflow: Literature Evaluation

The `literature-critic` agent is NOT part of the Editorial Board. Use it separately when evaluating papers for potential inclusion:

```bash
/literature-critic <paper-url>  # Should this paper be added?
```

---

## Board Operating Principles

1. **Comprehensive over fast**: Better to catch issues now than after publication
2. **Synthesis over aggregation**: Don't just concatenate reports; find themes
3. **Actionable over descriptive**: Every finding should have a clear action
4. **Prioritized over exhaustive**: Focus attention on what matters most
5. **Respectful of agent expertise**: Trust specialized agents in their domains

---

## Emergency Protocols

### When Agents Fail

If an agent fails or times out:
1. Note the failure in the report
2. Continue with other agents
3. Recommend re-running failed agent separately
4. Do not block synthesis on one failure

### When Scope Is Too Large

For book-wide reviews that would be too slow:
1. Use `--depth quick` for overview
2. Prioritize chapters by: word count, citation density, figure count
3. Deep-dive on highest-priority chapters only
4. Schedule remaining chapters for follow-up

### When Findings Conflict Irreconcilably

Escalate to user with:
1. Clear statement of conflict
2. Each agent's rationale
3. Board's preliminary recommendation
4. Request for user decision

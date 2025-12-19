# Genomic Foundation Models — Comprehensive Writing Guidelines

## Core Philosophy

This textbook bridges computational biology, machine learning, and clinical genomics for researchers entering from adjacent domains. Target audience: PhD students and researchers with background in either genomics or ML, but not both. Tone: authoritative academic prose that remains pedagogically accessible. Think *Molecular Biology of the Cell* meets modern ML textbooks—technically rigorous but designed for learning.

## Critical Non-Negotiables

Before writing ANY content, verify these rules are followed:

1. **ZERO em-dashes (—)** - This is the single most identifiable AI writing pattern. Use colons, semicolons, parentheses, or split into separate sentences. No exceptions.
   - ❌ "reads—typically 100 to 300 base pairs—per sample"
   - ✅ "reads (typically 100 to 300 base pairs) per sample"
   - ✅ "reads, typically 100 to 300 base pairs, per sample"

2. **ZERO bullet points** in flowing prose chapters (exceptions: tables, boxed summaries, appendices)

3. **ZERO meta-commentary** - No "Let's examine", "Here's what we'll cover", "It's worth noting"

4. **Lead with Why** - Every major concept starts with motivation/problem before mechanism

These four rules are more important than any other stylistic guidance. If uncertain about any other instruction, follow these four above all else.

## Output Format Requirements

**All content must be delivered as markdown files (.md)**

- **Always create actual files** using the file creation tool
- **Never** output prose directly in the chat interface
- **Never** create .qmd files - use .md even though the project uses Quarto
- File naming: Use descriptive names like `chapter-05-cnn-models.md` or `part-02-intro.md`

**Workflow**:
1. Generate content
2. Create .md file with appropriate name
3. Provide file for download
4. Brief confirmation message only

**Don't**:
- Output long prose directly in chat
- Create .qmd files
- Include YAML frontmatter (unless specifically requested)
- Provide lengthy explanations after file creation - the file is the deliverable

**Example**:
```
[Creates file: chapter-07-transformers.md]

Created chapter 7 draft on transformer architectures (8,500 words). Covers attention mechanisms, position embeddings, and progression from RNNs. Includes 5 figure recommendations.
```

**Exception**: 
For quick questions, clarifications, or discussions about the book (not prose generation), respond normally in chat.

## Prose Style

### Voice and Authority

Write with quiet confidence. Avoid both excessive hedging and overconfident claims. State facts directly; acknowledge uncertainty when it exists.

**Good**: "Transformers achieve superior long-range modeling through self-attention mechanisms."
**Bad**: "It's worth noting that transformers seem to achieve somewhat superior long-range modeling through what are essentially self-attention mechanisms."

**Good**: "The optimal architecture remains an open question."
**Bad**: "We don't really know which architecture is best yet."

### Forbidden AI Writing Patterns

### Structural crutches

**EM-DASHES - ABSOLUTE PROHIBITION**:
- Em-dashes (—) have become the most recognizable signature of AI-generated academic writing
- **Check every paragraph** before finalizing - if you see —, revise immediately
- Acceptable alternatives:
  - Parentheses for asides: "reads (typically 100-300bp) per sample"
  - Commas for appositives: "reads, typically 100-300bp, per sample"  
  - Colons for elaboration: "reads of consistent length: 100 to 300 base pairs"
  - Semicolons for related clauses: "reads are short; most span 100-300bp"
  - Separate sentences when appropriate
- **Zero tolerance**: Even one em-dash marks the entire section as needing revision

**Other structural crutches**:
- No bullet points in flowing prose chapters
- No "Here's what we'll cover" meta-commentary
- No "Let's dive into", "Let's explore", "Let's examine"
- No numbered lists disguised as prose: "There are three key advantages: first... second... third..."

**Transition clichés**:
- "However" and "Moreover" as sentence starters (use sparingly)
- "Importantly", "Crucially", "Notably", "Interestingly"
- "It's worth noting that"
- "It should be emphasized that"
- "With this in mind"
- "In this context"
- "Building on this"

**False enthusiasm**:
- Avoid: "exciting developments", "powerful approach", "remarkable results", "impressive performance"
- Exception: When quoting/citing others' genuine assessments or describing field consensus

**Hedging language** (use sparingly):
- "somewhat", "rather", "quite", "fairly", "relatively"
- "appears to", "seems to", "tends to" (when you actually mean "does")
- "In many cases", "In general" (unless variance genuinely matters)

**Passive voice overuse**:
- Active voice is stronger for clarity
- Passive acceptable for methods ("Reads were aligned...") or when actor is truly unimportant
- Not acceptable when it muddles agency: "It has been shown that..." → "Smith et al. demonstrated that..."

**Anthropomorphization**:
- "The model learns to understand" → "The model learns to predict"
- "The network discovers patterns" → "The network identifies patterns"
- "BERT captures meaning" → "BERT represents sequences"
- Exception: Established metaphors like "attention focuses on" are acceptable

**Meta-commentary**:
- Don't narrate your writing process: "In this section, we will discuss..."
- Don't telegraph structure: "Before we examine X, let's first consider Y"
- Just write the content in logical order

### Lead with Why - Extended Guidance

**Structure every major concept**: Why → What → How

This applies at THREE scales:

#### 1. Chapter Level (2-3 paragraphs)
- **Paragraph 1**: Paradox or central challenge with concrete evidence
- **Paragraph 2**: Why this chapter's specific focus matters within broader challenge
- **Paragraph 3+**: Technical development

#### 2. Section Level (Major ## headings)
**First paragraph must establish stakes BEFORE mechanism.**

**Pattern for clinical/applied sections:**
1. Sentence 1: Clinical scenario or specific patient need
2. Sentences 2-3: Technical limitation that creates the problem
3. Sentence 4: Explicit consequence statement
4. *Now* introduce the technical solution

**Pattern for technical sections:**
1. Sentence 1: What the previous approach couldn't do (limitation)
2. Sentences 2-3: Concrete example where it fails
3. Sentence 4: Why this is fundamental, not just technical
4. *Now* introduce the new mechanism

**Example (DeepVariant opening from v7):**
> "Classical variant calling pipelines encode accumulated expert intuition through hand-crafted features and heuristics. Which quality metrics matter? How should allelic balance be weighed against strand bias? When should a borderline call be trusted? The answers to these questions were painstakingly developed through years of experience with sequencing data. *DeepVariant*, introduced by Google in 2018, asked a different question: what if we let the model learn these patterns directly from data? **The key insight was not better probabilistic modeling of sequencing errors, but rather a reformulation of the problem itself.** Variant calling becomes image classification, and convolutional neural networks learn to distinguish true variants from artifacts in the same way they learn to distinguish cats from dogs."

Note: 
- Opens with limitation of classical approaches
- Uses questions to engage reader
- States *DeepVariant* "asked a different question" (frames as intellectual pivot)
- Bolded sentence explicitly names the key insight
- Memorable analogy at the end

#### 3. Subsection Level (### headings)
**First 1-2 sentences establish why this specific mechanism/model matters.**

Can be brief but must be present:
- "Coverage gaps create a fundamental sampling problem..."
- "The HLA region illustrates both the biological importance and technical difficulty..."
- "Long reads transform variant calling by traversing regions essentially invisible to short reads..."

### Red Flags for Weak "Lead with Why"

❌ Starting directly with mechanism: "Multi-head attention computes..."
❌ Historical framing without stakes: "In 2018, Google introduced..."
❌ Definition without motivation: "Phasing is the process of..."
❌ "This section discusses..." (meta-commentary)

✅ Problem/limitation stated first
✅ Concrete example of failure
✅ Stakes explicitly named
✅ Mechanism introduced as solution

### Sentence Construction

**Vary sentence length**. Mix complex technical sentences with crisp declarative statements. Don't let every sentence follow subject-verb-object.

**Front-load key information**:
- "Attention mechanisms compute pairwise interactions" (clear)
- "Pairwise interactions between all positions are computed by attention mechanisms" (weaker)

**Use parallel structure for embedded lists**:
"Models achieve this through three mechanisms: first, positional embeddings encode sequence order; second, layer normalization stabilizes training; and third, residual connections preserve gradient flow."

**Avoid throat-clearing**:
- "In order to understand transformers..." → "Transformers..."
- "When it comes to attention..." → "Attention..."
- "In terms of performance..." → "Performance..."

**Strategic use of colons and semicolons**:
- Colons introduce explanations or lists naturally
- Semicolons link closely related independent clauses
- Both preferable to em-dashes for formal prose

### Parenthetical Precision

Use parenthetical phrases to add mechanistic precision without disrupting flow. This technique appears throughout v7 and adds technical depth elegantly.

**Pattern**: Main clause (mechanistic detail) continuation

**Examples from v7:**

1. "PacBio HiFi sequencing produces reads of 10 to 25 kilobases with per-base accuracy exceeding 99.9% (through circular consensus sequencing, where the same molecule is read multiple times to correct random errors)"

2. "reads (typically 100 to 300 base pairs) per sample"

3. "Standard `VCF` genotypes cannot distinguish these scenarios (encoding only that heterozygous genotypes exist at two positions without specifying which alleles travel together on the same physical chromosome)"

**When to use:**
- Adding mechanism without breaking narrative flow
- Providing technical detail for expert readers while maintaining accessibility
- Explaining "how" after stating "what"
- Giving concrete numbers or ranges

**What to put in parentheses:**
- Mechanistic explanations
- Typical ranges/values
- Technical clarifications
- Examples or specifics

**Don't overuse**: 1-2 parenthetical phrases per paragraph maximum, or they become distracting.

### Paragraph Structure

**One major concept per paragraph**. Supporting details in subsequent sentences, not new concepts.

**First sentence** establishes paragraph's focus. **Last sentence** often transitions to next idea (but not formulaically).

**Paragraph length**: Typically 4-8 sentences for technical content. Shorter (2-3) for transitions or emphasis. Longer acceptable if developing complex argument cohesively.

**Example structure**:
> [Opening sentence: main claim] Supporting evidence or mechanism. Technical detail or example. Additional nuance or qualification. [Closing: implication or bridge]

## Chapter Architecture

### Opening (2-3 paragraphs)

Establish the chapter's role in the book's narrative. Connect to previous chapters. Motivate the problem this chapter addresses.

**Don't**: Provide chapter outline ("First we discuss X, then Y...")
**Do**: Set intellectual stakes and preview the arc naturally

**Example**:
> The convolutional models explored in Chapter 5 excel at identifying local sequence motifs but struggle with long-range dependencies. When a distal enhancer 50 kilobases upstream regulates a gene, the convolutional receptive field cannot span this distance without impractical network depth. This limitation becomes critical for understanding regulatory grammar, where interactions between distant elements determine expression patterns.
>
> Recurrent architectures offer a natural solution: sequential processing that maintains state across arbitrary distances. This chapter examines how RNNs and LSTMs were first applied to genomic sequences, the insights they provided about regulatory logic, and ultimately why they proved insufficient for genome-scale modeling. Understanding these limitations motivates the transformer architectures that dominate modern genomic AI.

### Technical Development

Build concepts progressively. Each section assumes and references previous sections.

**Use frequent cross-references**: "As discussed in @sec-embeddings..." or "This extends the approach from @sec-cnn-limits..."

**Integrate examples throughout**, don't save them for "Applications" section at end.

**Acknowledge limitations as you go**. Don't wait for a "Limitations" section—address them when discussing each approach.

### Soft Landings (Not Conclusions)

End chapters when the argument naturally completes. Final paragraph should point toward the next question/challenge without formal "In conclusion..." framing.

**Example ending**:
> While recurrent architectures demonstrated that sequential processing could capture regulatory dependencies, their computational constraints limited practical application to genome-scale problems. The attention mechanism, freed from sequential processing requirements, would resolve this tension—enabling both long-range modeling and parallel computation.

### Distributed Forward References

Weave forward references throughout the chapter naturally:
- "We return to this in Chapter X when examining..."
- "This architectural choice anticipates the foundation models in Part 4"
- "The interpretability challenges here motivate the mechanistic approaches in @sec-interpretability"

**Don't**: Save all forward references for conclusion
**Don't**: Make them feel like advertisements ("The exciting developments in Chapter X...")

## Chapter Opening Strategy

### The First Two Paragraphs Matter Most

Readers decide whether to engage deeply within the first 60 seconds. The opening must establish intellectual stakes and narrative tension immediately—not through meta-commentary about what the chapter will cover, but through the inherent tension in the subject matter itself.

### The Distinctiveness Requirement

**CRITICAL: Each chapter must have a unique hook that no other chapter uses.**

When writing or revising chapter openings, first identify what makes THIS chapter's intellectual contribution distinctive. The hook should reflect that specific contribution, not a generic framing that could apply to multiple chapters.

**Hooks to use ONCE in the entire book (then retire):**
- "We can X, yet we cannot Y" paradox structure
- "Asymmetry between X and Y" framing
- Clinical scenario openings (use sparingly, max 3-4 across all chapters)
- "The interpretation gap" (sequencing cheap, understanding hard)
- Scale contrasts (millions of X, handful of Y)

**Before writing any chapter opening, check:**
1. What is this chapter's unique intellectual contribution?
2. What hook best captures that specific contribution?
3. Has this hook pattern been used in another chapter?
4. If yes, find a different angle

**Examples of distinctive hooks by chapter type:**

| Chapter Focus | Distinctive Hook Approach |
|---------------|--------------------------|
| Data/Resources | "Models inherit training data biases" (inheritance framing) |
| Architecture | "Different architectures encode different assumptions about biology" |
| Evaluation | "Genomic data makes it easy to fool yourself" (unique pitfalls) |
| Clinical application | "Predictions only matter if they change decisions" (action gap) |
| Method comparison | "Each approach answers a different question" |

### Opening Techniques That Work

**Paradoxes and tensions** (use variety across chapters):
- "We can X, yet we cannot Y"
- "The field has achieved X, but Y remains unsolved"
- "Method X succeeds when Y, but fails when Z"

**Concrete scale that surprises:**
- Juxtapose achievable vs. impossible
- Scale contrasts with specific numbers
- Time contrasts

**The central problem as narrative driver:**
State the core challenge as a problem demanding solution, not as a topic to be covered:
- ✅ "How do we distinguish signal from noise in terabases of sequencing data?"
- ❌ "This chapter examines variant calling methods"

**Immediate consequences:**
Within the first paragraph, establish why failure matters:
- Clinical: "Missed variants mean missed diagnoses"
- Scientific: "Systematic errors propagate through every downstream analysis"
- Practical: "Every model in this book assumes this problem is solved"

**Conceptual shifts:**
Frame the chapter around an intellectual pivot:
- "Where X asks 'what pattern exists here,' Y asks 'what distant information matters here'"
- "The key insight was not better X, but a reformulation of the problem itself"

**The distinctive capability:**
Lead with what this approach uniquely enables:
- "Foundation models score variants without ever seeing pathogenic labels during pretraining"
- "Graph neural networks consume foundation model representations, operating at a higher level of abstraction"

### Opening Patterns to Avoid

**Generic historical narration:**
- ❌ "X technology has transformed genomics..."
- ❌ "Over the past decade, sequencing has become..."
- ❌ "Recent advances in X have enabled..."

**Meta-commentary about the chapter:**
- ❌ "This chapter examines..."
- ❌ "We will explore..."
- ❌ "The following sections cover..."

**Technical details before motivation:**
- ❌ Starting with "NGS produces 100-300bp reads with..." (save for paragraph 3+)
- ❌ Beginning with method names or acronyms before establishing why they matter

**Throat-clearing:**
- ❌ "In order to understand X, we must first..."
- ❌ "Before we can discuss X, it's important to..."

**Repetitive patterns across chapters:**
- ❌ Using "asymmetry" framing in multiple chapters
- ❌ Opening every clinical chapter with a patient scenario
- ❌ Repeatedly using "we can sequence cheaply but can't interpret"

### Structure for Opening Paragraphs

**Paragraph 1 (2-4 sentences):**
- Sentence 1: State the paradox, tension, or central challenge UNIQUE to this chapter
- Sentences 2-3: Concrete evidence or scale that makes it vivid
- Sentence 4 (optional): First hint at consequences or why it matters

**Paragraph 2 (3-5 sentences):**
- Establish this chapter's specific focus within the broader challenge
- Connect to the book's narrative arc (what came before, what comes after)
- Set intellectual stakes: what readers will understand after reading

**Paragraph 3+ (standard technical development):**
- Now you can introduce technical details, methods, definitions
- The hook has done its job—readers are committed

### The Memorable Sentence

Every major opening (chapter, major section) should contain at least one sentence designed to be memorable and quotable. These sentences:

1. **State paradoxes explicitly**: "The clinical implications are entirely different, yet the data appear identical without phase information."

2. **Name tensions**: "This asymmetry between data generation and interpretation defines the central challenge of genomic medicine."

3. **Juxtapose scale**: "A newborn screening program can identify thousands of rare variants in an infant's genome before discharge, but clinicians can confidently act on fewer than a hundred."

4. **Frame impossible choices**: "Variant callers operating in this region face an impossible choice between sensitivity and specificity."

5. **State information-theoretic limits**: "Short reads face a fundamental limitation rooted in information theory: sequences shorter than local repeats cannot unambiguously resolve these features."

6. **Capture conceptual shifts**: "Where convolutions ask 'what local pattern exists here,' attention asks 'what distant information matters here.'"

7. **Name the key distinction**: "Plausible explanations that match biological intuition are not the same as faithful explanations that accurately reflect model computation."

**Placement**: Typically the final sentence of paragraph 1 (chapter opening) or final sentence of the motivating paragraph (section opening).

**Test**: Can you imagine a professor quoting this sentence in a lecture? If not, it's not memorable enough.

### Exemplary Chapter Hooks by Type

**The Discovery Hook** (for methods that revealed something unexpected):
> "In 2015, a convolutional neural network trained on ENCODE chromatin data learned to recognize transcription factor binding motifs that matched entries in the JASPAR database, despite never seeing those motifs during training. The network had discovered, through gradient descent on raw sequence, patterns that experimental biologists had spent decades cataloging."

Why it works: Leads with a surprising, concrete finding. The model "discovered" biology.

**The Conceptual Shift Hook** (for architectural innovations):
> "Where convolutional networks ask 'what local pattern exists here,' attention asks a different question: 'what distant information matters here?' This reformulation changed what genomic models could learn."

Why it works: Frames the innovation as answering a different question, not just performing better.

**The Silent Failure Hook** (for evaluation/methodology chapters):
> "Transfer learning fails as often as it succeeds, and the failures are silent. A model produces confident predictions; nothing signals when those predictions are meaningless."

Why it works: Creates stakes around a hidden danger. The problem isn't obvious.

**The Calibration Hook** (for uncertainty/clinical chapters):
> "A pathogenicity score of 0.73 means nothing unless we know what 0.73 means. If the model is well-calibrated, approximately 73% of variants receiving this score are truly pathogenic. If miscalibrated, the true rate could be 40% or 95%."

Why it works: Makes an abstract concept (calibration) concrete through a specific number.

**The Action Gap Hook** (for clinical translation chapters):
> "A risk prediction has clinical value only if it changes what happens next. If a patient with a high score receives the same treatment as one without genetic testing, the score added nothing to care regardless of its statistical validity."

Why it works: Reframes success criteria from prediction accuracy to clinical impact.

**The Proxy Gap Hook** (for benchmark/evaluation chapters):
> "Every benchmark measures a proxy. ClinVar pathogenicity labels proxy clinical impact. AUROC proxies discrimination ability. The gap between proxy and target varies across benchmarks, variant types, and populations."

Why it works: Establishes critical distance from benchmarks without being cynical.

### Quality Checklist for Chapter Openings

Before finalizing any chapter opening:
- [ ] Does paragraph 1 contain a paradox, tension, or challenge (not just a topic)?
- [ ] Is this hook DISTINCT from all other chapter hooks in the book?
- [ ] Are there concrete numbers, scales, or examples in the first 100 words?
- [ ] Could a smart undergraduate explain "why this matters" after reading paragraph 1?
- [ ] Did I avoid starting with "This chapter examines..." or "X technology has transformed..."?
- [ ] Is there at least one memorable, quotable sentence?
- [ ] Would I keep reading if this were someone else's textbook?

If you answer "no" to any of these, revise the opening before proceeding.

## Section Opening Strategy

### Every Section Needs a Hook

Major sections (## headings) require their own motivating opening, not just a transition from the previous section. The first paragraph of each section must establish why this specific content matters before diving into mechanism.

### Avoid Formulaic Section Transitions

**DON'T open sections with:**
- ❌ "Having discussed X, we now turn to Y"
- ❌ "With this foundation in place, we can examine..."
- ❌ "The previous section established X. This section addresses Y."
- ❌ "Building on the concepts above..."
- ❌ Direct definitions: "X is defined as..."

**DO open sections with:**
- ✅ A limitation or gap that motivates this section's content
- ✅ A concrete example that illustrates the need
- ✅ A question that the section will answer
- ✅ Stakes specific to this topic

### Section Opening Patterns

**The Limitation Pattern:**
> "Convolutional networks integrate information only within their receptive fields. Genomic regulation routinely operates across distances that exceed practical receptive field sizes: enhancers control genes across tens of kilobases, topologically associating domains span megabases."

**The Concrete Example Pattern:**
> "Consider a child who inherits two rare variants in *CFTR*. If both reside on the maternal chromosome, the child retains one functional copy. If on opposite chromosomes, no functional copy exists. Standard genotypes cannot distinguish these scenarios."

**The Question Pattern:**
> "What does it mean for a model to 'understand' regulatory grammar? The question is not philosophical but operational: can we identify what patterns the model has learned, and do those patterns correspond to known biology?"

**The Stakes Pattern:**
> "Calibration determines whether model outputs can inform clinical decisions. A model that systematically overstates confidence will trigger unnecessary interventions; one that understates confidence will miss actionable findings."

**The Capability Pattern:**
> "Long reads traverse regions essentially invisible to short-read sequencing. A single 15-kilobase HiFi read can span an entire tandem repeat, resolving copy number and internal structure simultaneously."

### Section Opening Checklist

Before finalizing any section opening:
- [ ] Does the first paragraph establish stakes or motivation?
- [ ] Did I avoid formulaic transitions ("Having discussed...", "Building on...")?
- [ ] Is there a concrete example, specific limitation, or clear question?
- [ ] Would a reader understand why this section matters before reading the technical content?

## Part Introductions

### Purpose

Orient readers at major transitions. Establish intellectual coherence for the 4-5 chapters ahead. Motivate why these chapters belong together.

### Length and Structure

**Target**: 300-500 words (3-4 paragraphs)

**Paragraph 1**: Central question, challenge, or intellectual theme that unifies this part. Lead with substance, not backward reference.

**Paragraph 2**: How the chapters build on each other logically. Show the arc, don't just list contents.

**Paragraph 3**: Chapter-by-chapter preview with specific focus of each.

**Paragraph 4** (optional): Forward pointer to what this part enables in later parts.

### Critical Rules for Part Introductions

**DO NOT open with backward references:**
- ❌ "The preceding parts have traced..."
- ❌ "Part I established the foundations..."
- ❌ "Having covered X in earlier chapters..."
- ❌ "Building on the concepts from Part II..."

**DO open with the intellectual stakes of THIS part:**
- ✅ "Every genomic foundation model inherits the biases of its training data."
- ✅ "Biology operates across scales that sequence alone cannot capture."
- ✅ "Evaluating genomic models presents challenges that distinguish this domain from NLP or computer vision."

**Minimize chapter enumeration:**
- ❌ "Chapter 5 covers X. Chapter 6 addresses Y. Chapter 7 examines Z."
- ✅ Weave chapter references into the narrative of how ideas build

### Part Introduction Template

**Paragraph 1 (Intellectual Stakes):**
Open with the central insight, challenge, or question that unifies the part. No backward references. Make readers understand why these chapters belong together.

**Paragraph 2 (The Arc):**
Explain how the chapters build logically. What does each add? How do they connect? This is narrative, not enumeration.

**Paragraph 3 (Chapter Preview):**
Brief mention of each chapter's specific focus. Use @sec-references. Keep to 1-2 sentences per chapter.

**Paragraph 4 (Forward Connection):**
Optional. What does mastering this part enable? How does it connect to later parts?

### Example Part Introduction

**Part II: Sequence Architectures**

> Five foundational questions determine what any genomic model can learn. How should sequences be represented as neural network inputs? What mechanisms enable models to capture dependencies across thousands or millions of base pairs? What distinguishes foundation models from their task-specific predecessors? How do models extract useful representations from unlabeled sequence data? And how can pretrained representations be adapted to specific applications? The answers to these questions, made before any training begins, constrain everything that follows.
>
> This part addresses each question in turn, building from fundamental representation choices through architectural mechanisms to training and adaptation strategies. The progression is logical: representation choices (@sec-representations) determine what patterns are visible to the model; convolutional architectures (@sec-cnn) established the paradigm of learning sequence-to-function mappings; attention mechanisms (@sec-attention) resolved the tension between local computation and long-range dependencies; pretraining objectives (@sec-pretraining) determine what patterns models learn from unlabeled data; and transfer learning (@sec-transfer) bridges the gap between pretraining and deployment.
>
> Together, these chapters provide the conceptual foundation for understanding the specific model families examined in Part III and the applications developed throughout the remainder of the book.

### Part Introduction Checklist

Before finalizing any part introduction:
- [ ] Does paragraph 1 establish intellectual stakes without backward references?
- [ ] Is there a clear unifying theme for why these chapters belong together?
- [ ] Does the chapter preview show logical progression, not just list contents?
- [ ] Is it 300-500 words (not too long, not too short)?
- [ ] Would a reader understand the part's purpose without having read previous parts?

## Heading Structure

### Three-Level Hierarchy

**Chapters** (# Level 1): Major topics, typically 24 in the book
**Sections** (## Level 2): Thematic areas within chapter, 3-5 words
**Subsections** (### Level 3): Specific concepts or models, 2-4 words

Use subsections freely as cognitive guideposts. Dense technical prose benefits from frequent checkpoints—readers need to look up, orient themselves, and continue.

**Rule of thumb**: If 3-5 paragraphs develop a coherent sub-concept, give it a subsection.

### Naming Conventions

**Prefer noun phrases**: "Transformer Architecture", "Multi-head Attention", "Clinical Variant Interpretation"

**Avoid**:
- Articles: "The Transformer Architecture" → "Transformer Architecture"
- Gerunds when possible: "Understanding Attention" → "Attention Mechanisms"
- -ing phrases: "Predicting Splice Sites" → "Splice Site Prediction"
- Questions: "How Do Transformers Work?" → "Transformer Mechanisms"

**Maintain parallel structure** within a chapter:
```
## DeepSEA and Regulatory Prediction
### Model Architecture
### Training Data
### Variant Effect Prediction

## Basset and Accessibility
### Model Architecture  
### Training Data
### Cross-cell-type Transfer
```

**Example chapter structure**:
```
# Convolutional Neural Networks for Genomics

## Early Sequence Models
### Basset Architecture
### ChromDragoNN Extensions

## DeepSEA and Regulatory Prediction
### Convolutional Sequence Scanning
### Multi-task Learning Framework
### Variant Effect Scoring
### Limitations at Genomic Scale

## SpliceAI and RNA Processing
### Dilated Convolutions
### Splice Site Recognition
### Clinical Deployment
### Comparison to Position Weight Matrices

## From Convolutions to Attention
```

## Information Density and Technical Depth

### Core Principle

Dense but not exhausting. Assume readers will pause to process. One major concept per paragraph, with supporting details in subsequent sentences.

### What to Include

**For core models** (e.g., DNABERT, Enformer, ESM-2):
- Architecture details: layer counts, dimensions, attention heads
- Training data: size, composition, preprocessing
- Training procedure: objective functions, optimization
- Performance: benchmarks, comparisons, ablations
- Key innovations: what architectural/methodological advance does this represent?
- Limitations: where does this fail or underperform?
- Clinical/practical applications: concrete use cases

**For supporting models**:
- Sufficient detail to understand contribution to field
- Key architectural choices that differentiate from predecessors
- Primary results that justify inclusion
- Connection to broader narrative

**For historical models**:
- Brief acknowledgment of contribution
- Why this mattered at the time
- Forward pointer to what superseded it

### What to Cite

**Every technical claim needs backing**. Use citations for:
- Performance numbers
- Architectural details
- Training procedures
- Benchmark results
- Claims about model capabilities or limitations
- Historical development of methods

**Don't cite**:
- Basic genomics facts ("DNA consists of four nucleotides")
- Standard ML terminology ("CNNs use convolutional filters")
- Your own syntheses or observations

### Percentages and Numbers

**Require citations:**
- Specific performance metrics (accuracy, coverage, error rates)
- Clinical significance claims (% of drugs metabolized, disease prevalence)
- Study-specific results (% of variants called, % improvement)
- Controversial or surprising statistics

**Don't require citations:**
- Textbook-level genomic facts (genome size, coding sequence percentage)
- General operational descriptions (typical coverage ranges, read lengths)
- Pedagogical approximations used for scale illustration
- Orders of magnitude ("thousands vs. hundreds")

**When in doubt**: If the number strengthens a clinical or technical argument, cite it. If it's purely illustrative or common knowledge, citation is optional.

**Example distinction:**
- "CYP2D6 metabolizes ~25% of drugs" → CITE (specific clinical claim)
- "protein-coding sequence is ~1-2% of genome" → DON'T CITE (textbook fact)
- "thousands of variants, fewer than hundred actionable" → DON'T CITE (illustrative scale)

### Avoid Redundancy

**Don't repeat information across chapters**. Instead:
- First mention: Full explanation
- Subsequent mentions: Brief reminder + cross-reference

**Example**:
First time (Chapter 5): [Full explanation of attention mechanism, 2-3 paragraphs]

Later (Chapter 8): "Attention mechanisms (see @sec-attention) compute pairwise interactions between all sequence positions, enabling..."

### Ground Scale and Numbers

Make numbers memorable by connecting to genomic context:

**Good**:
- "600 million parameters—roughly one per gene in the human genome"
- "Enformer's 200kb receptive field spans typical enhancer-promoter distances"
- "Training required 3 days on 8 GPUs—comparable to AlphaFold's initial training"

**Bad**:
- "600M parameters"
- "200kb context window"
- "Trained on 8 V100 GPUs"

## Citations and References

### Hybrid Approach

**In-prose for seminal contributions**:
- "Vaswani et al. @vaswani_attention_2017 introduced the transformer architecture"
- "The Enformer model by Avsec et al. @avsec_effective_2021 extended..."
- "As Kelley et al. @kelley_sequential_2018 demonstrated..."

**End-of-sentence brackets for supporting facts**:
- "ATAC-seq measures chromatin accessibility [@buenrostro_atac-seq_2013]."
- "Splice sites exhibit characteristic sequence motifs [@ast_splice_2004]."

**Multiple sources** (end-of-sentence):
- "Foundation models show promise for variant interpretation [@frazer_disease_2021; @jumper_highly_2021; @cheng_accurate_2023]."

**Avoid**:
- Mid-sentence brackets that break flow: ~~"This approach [@smith_2020] achieves..."~~
- Dangling citations: ~~"Studies have shown this [@author_year]."~~ → "Author et al. @author_year demonstrated this."

### Integration into Prose

Citations should feel natural, not tacked on:

**Good**: "Enformer addressed this limitation by extending the receptive field to 200kb through transformer attention [@avsec_effective_2021]."

**Bad**: "Enformer extended the receptive field to 200kb through transformer attention. [@avsec_effective_2021]"

## Readability and Engagement

### Concrete Examples Throughout

**Don't make readers wait** 3 pages for "here's what this actually means."

Lead with specific genomic elements, variants, or prediction tasks before generalizing to theory.

**Example ordering**:

**Good**: "Consider a splice site mutation in the dystrophin gene that causes Duchenne muscular dystrophy. The variant disrupts the AG dinucleotide that marks exon boundaries, causing exon skipping. Detecting such splice-altering variants requires models that learn sequence grammar at nucleotide resolution—the motivation for SpliceAI's architecture..."

**Bad**: "SpliceAI uses dilated convolutions to expand receptive fields without increasing parameter counts. The architecture consists of residual blocks with exponentially increasing dilation rates. This enables... [3 paragraphs of architecture] ...which proves useful for detecting splice-altering variants like those in dystrophin."

### Vary Pedagogical Rhythm

Alternate between different types of content to prevent reader fatigue:

- **Dense theory** → Concrete application → Back to theory
- **What** (architecture) → **How** (mechanism) → **Why** (motivation)
- **Mechanism** → Clinical example → Back to mechanism
- **Broad principle** → Specific instantiation → Generalization

**Within sections**, don't sustain pure abstraction for more than 2-3 paragraphs without grounding in examples or applications.

### Strategic Repetition

Key concepts (attention, embeddings, fine-tuning, transfer learning) reappear across chapters.

**Don't assume readers remember from 3 chapters back**. Briefly re-ground before building:

"Attention mechanisms, which compute pairwise interactions between sequence positions (see @sec-attention), enable..." [continue with new point]

**Not**: "Using attention, models can..." [assumes perfect recall]

### Acknowledge Limitations Honestly

**Build trust** by addressing failures and edge cases:

- "This approach fails when training data exhibit ascertainment bias..."
- "Performance degrades for rare variant classes with fewer than 10 examples..."
- "The model cannot distinguish correlation from causation in regulatory predictions..."

**Shows you're teaching critical thinking**, not marketing products. Makes genuine successes more credible.

**Integrate throughout**, don't silo into "Limitations" sections.

### Minimize Jargon Inflation

**If a common term exists, use it**:
- "Hidden state" not "latent representation vector"
- "Output layer" not "prediction head"
- "Input sequence" not "tokenized input representation"

**Define technical terms once**, then use consistently. Don't introduce synonyms.

**When you must introduce new terminology**, explain why existing terms are insufficient:

"We term this *epistatic confounding* rather than simple correlation because the effect depends on specific allelic combinations at multiple loci..."

### Historical Through-Lines

**Brief "why now" moments** that connect ideas temporally:

"The 2017 transformer paper resolved a decade-long tension between parallel training and long-range modeling..."

"DeepSEA's 2015 success catalyzed interest in applying deep learning to regulatory genomics, leading to..."

**Shows field evolution**, not just catalog of models. Helps readers understand why certain approaches emerged when they did.

### One Provocative Insight Per Chapter

**Something genuinely surprising or counterintuitive** that energizes reading:

- "Attention doesn't require recurrence—sequential context emerges from learned position embeddings alone"
- "Foundation models trained on DNA sequence alone learn representations that transfer to protein structure prediction"
- "Genomic models exhibit scaling laws similar to language models despite discrete, non-linguistic inputs"

**This becomes a memorable anchor** for the chapter's content.

## Clinical Integration Strategy

### The Clinical Stakes Pattern

When introducing technical concepts, establish clinical stakes BEFORE technical mechanisms. This pattern works at multiple scales:

**Section-level openings:**
Lead major sections with concrete clinical scenarios that establish why the technical content matters.

**Pattern**: Clinical scenario → Technical limitation revealed → Consequence stated → Now introduce mechanism

**Example (phasing section from v7):**
> "The clinical stakes of phasing emerge clearly in compound heterozygosity. Consider a child who inherits two rare, potentially pathogenic variants in *CFTR*, the cystic fibrosis gene. If both variants reside on the chromosome inherited from the mother (in *cis*), the child retains one functional copy from the father and may be unaffected or merely a carrier. If the variants are on opposite chromosomes (in *trans*), no functional copy exists and the child will develop cystic fibrosis. Standard `VCF` genotypes cannot distinguish these scenarios, encoding only that heterozygous genotypes exist at two positions without specifying which alleles travel together on the same physical chromosome. **The clinical implications are entirely different, yet the data appear identical without phase information.**"

Why this works:
- Specific patient (child with *CFTR* variants)
- Clear stakes (*cis* vs *trans* = carrier vs disease)
- Technical limitation explicitly named
- Paradox stated in final sentence

**Subsection-level hooks:**
Open subsections with specific numbers, drug names, genes, or patient scenarios.

**Good**: "The *CYP2D6* gene encodes a cytochrome P450 enzyme responsible for metabolizing approximately 25% of clinically used drugs, including codeine, tamoxifen, and many antidepressants."

**Bad**: "The *CYP2D6* gene is clinically important for drug metabolism."

### Balancing Clinical Scenarios

**Use clinical scenario openings strategically, not formulaically.**

Clinical scenarios are powerful but should not open every chapter or section. Reserve them for:
- Chapters with direct clinical applications
- Sections where patient stakes illuminate technical choices
- Moments where concrete examples clarify abstract concepts

**Vary your opening approaches across the book:**
- Some chapters: Clinical scenario opening
- Some chapters: Conceptual shift framing
- Some chapters: Technical limitation opening
- Some chapters: Surprising finding opening

### Concrete Specificity Checklist

When mentioning clinical examples, always include:
- **Percentages**: "25% of clinically used drugs" not "many drugs". Cite as needed per the "numbers" guideline.
- **Drug names**: "codeine, tamoxifen, and many antidepressants" not "various medications"
- **Gene names**: "*CFTR*, the cystic fibrosis gene" not "a recessive disease gene"
- **Numbers**: "thousands of variants, fewer than a hundred actionable" not "many variants, few actionable"
- **Ages/timescales**: "A 35-year-old presenting with cardiac arrest" not "a patient with cardiac arrest"

### The Consequences Statement

After establishing a technical limitation, explicitly state consequences using one of these frames:
- "The clinical implications are entirely different, yet..."
- "This creates a systematic mismatch between importance and data quality"
- "These errors concentrate in... creating systematic blind spots"
- "When this fails, every subsequent model inherits those errors"

**Pattern**: Technical limitation → "This/These" [consequence verb] [specific impact]

The consequence statement transforms observation into stakes.

## Visual Recommendations

For each chapter, suggest 3-5 figures with specific purposes:

### Architectural Diagrams
- Model structure: layer connections, dimensions, data flow
- Attention patterns: heatmaps showing learned dependencies
- Training pipelines: data preprocessing through loss computation

**Specify**: Key elements to highlight, not implementation details

**Example**: "Figure showing SpliceAI architecture with dilated convolution receptive fields expanding across 10kb context window. Highlight: exponentially increasing dilation rates (1, 2, 4, 8...) and how they avoid parameter explosion while capturing long-range dependencies."

### Performance Plots
- Benchmark comparisons across models
- Scaling curves: performance vs. parameters/data
- Ablation studies: component importance
- Error analysis: performance by variant type/allele frequency

### Conceptual Figures
- Abstract concepts made concrete (e.g., k-mer embedding space)
- Biological processes the model captures (e.g., enhancer-promoter looping)
- Failure modes and edge cases

### Clinical Workflows
- Application pipelines: from genomic data to clinical decision
- Integration with existing clinical tools
- Validation approaches for deployment

**Keep descriptions high-level**: "Figure showing..." not pixel-level specifications.

## Cross-References

Use liberally throughout:
- Sections: @sec-attention, @sec-embeddings
- Figures: @fig-transformer-architecture
- Equations: @eq-attention-scores
- Chapters: "Chapter 7 examines..." or "as discussed in @sec-previous"

**Purpose**: Reinforce that this is a cohesive book, not collection of independent chapters. Help readers navigate forward and backward.

## Typography and Emphasis

### Purpose
This book bridges AI, biology, and clinical medicine. Clear typographic signals help readers from different domains navigate unfamiliar terminology.

### Bold for Glossary Terms (First Occurrence)

**Mark glossary terms in bold on first mention only**:
- "The **transformer architecture** revolutionized sequence modeling..."
- "**Single nucleotide polymorphisms (SNPs)** represent the most common form of genetic variation..."
- "Models use **attention mechanisms** to compute pairwise interactions..."

After first mention, use term normally without formatting.

**Expand abbreviations on first use**: "**single nucleotide polymorphism (SNP)**" then use SNP normally thereafter.

### Italics for Technical Terms (Non-Glossary)

**Use italics for**:
- Gene/protein names: *BRCA1*, *TP53*, *dystrophin*
- Model names after first mention: *Enformer*, *DNABERT*, *AlphaMissense*
- Mathematical variables in prose: "where *n* represents sequence length"
- Latin/foreign terms: *in silico*, *de novo*, *ab initio*
- Rare emphasis: "This is *not* equivalent to..."

### Monospace for Code/Data

**Use `monospace` for**:
- File formats: `VCF`, `BAM`, `FASTA`, `FASTQ`
- Code elements: `batch_size`, `learning_rate`, `num_layers`
- Command-line tools: `bedtools`, `samtools`, `bcftools`
- URLs and paths (when referenced): `https://...`, `/path/to/file`

### What NOT to Emphasize

- Common terms after first use
- Multiple emphasized words in same sentence (creates noise)
- Entire phrases: ~~"the *entire attention mechanism*"~~ → "the attention *mechanism*"
- Every technical term (defeats the purpose)

### Example in Practice

> The **transformer architecture** processes sequences through **self-attention mechanisms** rather than recurrence. Each attention layer computes interactions between all positions simultaneously, enabling parallel training on modern GPUs. The model uses **positional embeddings** to encode sequence order, since attention itself is position-invariant. For genomic sequences, transformers typically operate on *k*-mer tokens extracted from DNA strings stored in `FASTA` format.
>
> The *Enformer* model [@avsec_effective_2021] extended this approach to 200kb contexts, sufficient to capture most enhancer-promoter interactions. Training used **chromatin accessibility** data from ATAC-seq experiments across 200 cell types...

## Glossary Construction

### Organization

**Alphabetical with domain tags**. Easier for readers to search.

**Domain tags**:
- [ML] - Machine learning terms
- [Genomics] - Molecular biology, DNA/RNA concepts
- [Clinical] - Medical, diagnostic, therapeutic terms
- [Statistics] - Statistical methods, metrics
- [Computation] - Algorithms, data structures, computational concepts

### Entry Format
```markdown
**Term** [Domain]: Definition in one or two clear sentences. Additional context if needed.

**Term (Abbreviation)** [Domain]: Definition. After first mention, abbreviation used throughout book.
```

### Definition Style

- **Start with plain language**: "A dense vector representation..." not "An n-dimensional embedding..."
- **Then add precision**: "...specifically, a learned mapping from discrete tokens to continuous space"
- **Include why it matters** (when not obvious): "...enabling semantic similarity to be captured through geometric proximity"
- **Cross-reference related terms** when helpful: "See also: **embedding dimension**, **token**"

### Example Glossary Entries
```markdown
**Attention mechanism** [ML]: A neural network component that computes weighted interactions between all positions in a sequence, allowing the model to focus on relevant context regardless of distance. Enables transformers to capture long-range dependencies without recurrence.

**Allele** [Genomics]: One of two or more alternative forms of a gene at a specific genomic position. Humans inherit one allele from each parent for each gene.

**Area under ROC curve (AUROC)** [Statistics]: Performance metric for binary classifiers measuring the probability that the model ranks a random positive example higher than a random negative example. Values range from 0.5 (random) to 1.0 (perfect).

**Embeddings** [ML]: Dense vector representations of discrete inputs (tokens, words, amino acids) in continuous space. Learned during training to capture semantic relationships through geometric proximity.

**Enhancer** [Genomics]: Regulatory DNA sequence that increases gene transcription when bound by transcription factors, often located thousands of base pairs from the target gene. Can function regardless of orientation.

**Fine-tuning** [ML]: Training process where a pre-trained model's parameters are further adjusted on a specific downstream task, typically with a smaller learning rate. Leverages learned representations while adapting to new objectives.

**Single nucleotide polymorphism (SNP)** [Genomics]: Variation at a single base pair position where different individuals carry different nucleotides. Most common form of genetic variation, occurring roughly once per 300 base pairs in human genomes.

**Variant of uncertain significance (VUS)** [Clinical]: A genetic variant whose impact on disease risk or protein function cannot be confidently determined from available evidence. Represents a major challenge in clinical genomic interpretation.
```

### Glossary Placement

- **Appendix position**: After main chapters, before references
- **Comprehensive**: 100-200 terms covering all three domains
- **Living document**: Can expand in online version as field evolves

### Term Selection Criteria

**Include in glossary if**:
- Essential to understanding the book's core content
- Likely unfamiliar to readers from 1+ of the three domains
- Used repeatedly across multiple chapters
- Subject to misunderstanding or ambiguous usage

**Exclude from glossary if**:
- Used only once in passing
- Explained fully in context and not referenced again
- Standard undergraduate-level knowledge in all domains
- Too specialized/narrow (handle in chapter text instead)

## Edge Cases and Special Situations

### Equations and Mathematical Notation

- Introduce equations after explaining conceptually in prose
- Every variable defined immediately or in prior sentence
- Provide intuition for what equation computes before mathematical form
- Use standard notation when possible (don't reinvent symbols)
- Explain what each variable and term represents in context for non-mathematicians
- Do not lead LaTeX equations with escape characters. Use "$" or "$$" and not "\$" or "\$$"

**Example**:
"The attention score between positions $i$ and $j$ quantifies their interaction strength. Mathematically, this score is computed as the dot product of query and key vectors, scaled by the square root of dimension $d_k$:

$$[equation]$$

The scaling factor prevents gradients from vanishing in high dimensions..."

### Code and Pseudocode

Generally avoid unless directly pedagogical. When included:
- Prefer conceptual pseudocode to language-specific implementations
- Integrate with prose, don't dump code blocks
- Explain what each component accomplishes

**The book is not a tutorial**—readers can consult implementation guides elsewhere. Focus on concepts.

### Clinical and Applied Content

Balance technical depth with practical considerations:
- Clinical validation requirements
- Interpretability for medical decisions
- Regulatory and deployment constraints
- Integration with existing workflows

**Don't oversimplify clinical context** to make ML look better. Healthcare is complex; acknowledge that.

### Comparisons Between Models

Structure as principled analysis, not scoreboard:
- Compare on specific capabilities (long-range modeling, parameter efficiency, etc.)
- Explain why performance differs—architectural choices, training data, objectives
- Acknowledge when differences are unclear or context-dependent

**Avoid**: "Model A is better than Model B" without qualification

### Negative Results and Failed Approaches

**Include them**. Failed approaches are pedagogically valuable:
- What was tried?
- Why did it seem promising?
- What went wrong?
- What did the field learn?

## Explicit Framing Techniques

### Name the Tension

After presenting a paradox or challenge, explicitly name and frame it:

**Pattern**: "This [noun] between X and Y defines/represents/creates..."

**Examples:**
- "This asymmetry between data generation and interpretation defines the central challenge"
- "This tension between sensitivity and specificity creates systematic blind spots"
- "This mismatch between biological importance and technical difficulty..."

**Why it works**: Transforms implicit observations into explicit frameworks readers can remember and apply.

### Frame Tradeoffs Explicitly

When discussing limitations or competing approaches, state the tradeoff using one of these frames:

1. **The Impossible Choice**: "Variant callers face an impossible choice between sensitivity and specificity"

2. **The Fundamental Limitation**: "Short reads face a fundamental limitation rooted in information theory"

3. **The Systematic Mismatch**: "Clinically critical loci often present the most challenging technical contexts, creating a systematic mismatch between importance and data quality"

4. **The Silent Propagation**: "These errors concentrate in specific genomic contexts, creating systematic blind spots that downstream models inherit without warning"

**Pattern**: Subject + [faces/creates/represents] + [type of challenge] + [specific manifestation]

### State Key Insights Explicitly

For major conceptual points, don't assume readers will infer—state directly using:

**"The key insight was..."**
"The key insight was not better probabilistic modeling of sequencing errors, but rather a reformulation of the problem itself."

**"The fundamental difference..."**
"The fundamental difference between *DeepVariant* and classical pipelines lies in how evidence is combined."

**"The central question..."**
"At each position in the genome, the fundamental question is: given the reads overlapping this site, what is the most likely genotype?"

**Why it works**: Readers appreciate direct statements of what matters. Don't make them work to figure out the main point.

### The "Yet" Construction

Use "yet" to create memorable paradoxes:

**Pattern**: "We can X, yet we cannot Y"

**Examples:**
- "We can sequence a genome for hundreds of dollars, yet we cannot reliably interpret most variants"
- "The clinical implications are entirely different, yet the data appear identical"
- "Three possibilities exist, yet reads alone often cannot distinguish them"

**Why it works**: "Yet" creates tension by juxtaposing capability with limitation.

**Note**: Use this construction sparingly across the book. If multiple chapters use "We can X, yet we cannot Y" as their opening hook, the pattern loses impact.

## Quality Checklists

### Chapter Openings
Before finalizing chapter opening, ask:
- [ ] Does paragraph 1 contain a paradox, tension, or challenge (not just a topic)?
- [ ] Is this hook DISTINCT from all other chapter hooks in the book?
- [ ] Are there concrete numbers, scales, or examples in the first 100 words?
- [ ] Could a smart undergraduate explain "why this matters" after reading paragraph 1?
- [ ] Did I avoid starting with "This chapter examines..." or "X technology has transformed..."?
- [ ] Is there at least one memorable, quotable sentence?
- [ ] Would I keep reading if this were someone else's textbook?

If you answer "no" to any of these, revise the opening before proceeding with the chapter.

### Section Openings
Before finalizing any section opening:
- [ ] Does the first paragraph establish stakes or motivation?
- [ ] Did I avoid formulaic transitions ("Having discussed...", "Building on...")?
- [ ] Is there a concrete example, specific limitation, or clear question?
- [ ] Would a reader understand why this section matters before reading the technical content?

### Part Introductions
Before finalizing any part introduction:
- [ ] Does paragraph 1 establish intellectual stakes without backward references?
- [ ] Is there a clear unifying theme for why these chapters belong together?
- [ ] Does the chapter preview show logical progression, not just list contents?
- [ ] Is it 300-500 words (not too long, not too short)?
- [ ] Would a reader understand the part's purpose without having read previous parts?

### Chapter Sections
Before finalizing any chapter section:
**FIRST - Before anything else:**
- [ ] Search document for "—" (em-dash character) - count must be ZERO
- [ ] Search for bullet points (•, -, *) in prose sections - count must be ZERO
- [ ] Search for "Let's", "Here's", "It's worth noting" - remove all instances

**Prose quality**:
- [ ] No transition clichés ("However," "Moreover," "Importantly")
- [ ] Varied sentence length and structure
- [ ] Active voice predominates
- [ ] No anthropomorphization

**Content structure**:
- [ ] Leads with "why" for major concepts
- [ ] One concept per paragraph
- [ ] Concrete examples integrated throughout
- [ ] Cross-references to related sections
- [ ] Limitations acknowledged honestly

**Technical depth**:
- [ ] Key claims cited
- [ ] Sufficient detail for target audience
- [ ] No redundancy with other chapters
- [ ] Numbers grounded in genomic context

**Readability**:
- [ ] Pedagogical rhythm varies
- [ ] Subsection headings every 3-5 paragraphs
- [ ] Strategic repetition of key concepts
- [ ] At least one memorable insight

**Clinical integration**:
- [ ] Clinical examples include specific numbers, drugs, genes, or ages
- [ ] Major sections open with clinical stakes before technical mechanisms
- [ ] Each clinical example includes consequences, not just description

**Explicit framing**:
- [ ] Tensions/paradoxes are explicitly named ("This asymmetry...", "This tension...")
- [ ] Tradeoffs stated clearly ("face an impossible choice between...")
- [ ] Key insights stated directly ("The key insight was...", "The fundamental difference...")
- [ ] At least one "memorable sentence" per major opening

**Mechanistic precision**:
- [ ] Parenthetical phrases add technical depth where helpful (1-2 per paragraph max)
- [ ] "How it works" details added without disrupting narrative flow
- [ ] Specific numbers ground abstract concepts

If you answer "no" to any of these, revise the chapter section.

## Pre-Generation Self-Check

Before generating prose, explicitly verify:

1. **Em-dash awareness**: "I will use parentheses, colons, or commas instead of em-dashes"
2. **Bullet point awareness**: "I will write in flowing paragraphs, not lists"
3. **Meta-commentary awareness**: "I will start with content, not with 'In this section...'"
4. **Why-first awareness**: "I will establish motivation before mechanism"
5. **Clinical stakes awareness**: "I will open major sections with concrete clinical scenarios that establish stakes"
6. **Explicit framing awareness**: "I will explicitly name tensions, tradeoffs, and key insights rather than leaving them implicit"
7. **Memorable sentence awareness**: "I will craft at least one quotable sentence for each major opening"
8. **Distinctiveness awareness**: "I will ensure this opening is unique and not repetitive of other chapters"

If you cannot commit to all eight, stop and review the relevant sections.

**Additional check for major openings (chapters, major sections):**
- Have I included a concrete, specific example with numbers in the first paragraph?
- Have I explicitly named the central tension or challenge?
- Does at least one sentence feel memorable or quotable?
- Have I stated consequences explicitly, not just described problems?
- Is this hook distinct from other chapter/section hooks in the book?

## Meta-Instruction

Before generating prose, review these guidelines. Prioritize flowing academic narrative over exhaustive coverage. When uncertain about depth or scope, err toward technical rigor that maintains pedagogical clarity.

Remember: This textbook aims to be the definitive reference for genomic foundation models—comprehensive without being encyclopedic, authoritative without being inaccessible, rigorous without sacrificing readability.
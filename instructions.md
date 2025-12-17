# Genomic Foundation Models — Comprehensive Writing Guidelines

## Core Philosophy

This textbook bridges computational biology, machine learning, and clinical genomics for researchers entering from adjacent domains. Target audience: PhD students and researchers with background in either genomics or ML, but not both. Tone: authoritative academic prose that remains pedagogically accessible. Think *Molecular Biology of the Cell* meets modern ML textbooks—technically rigorous but designed for learning.

## Prose Style

### Voice and Authority

Write with quiet confidence. Avoid both excessive hedging and overconfident claims. State facts directly; acknowledge uncertainty when it exists.

**Good**: "Transformers achieve superior long-range modeling through self-attention mechanisms."
**Bad**: "It's worth noting that transformers seem to achieve somewhat superior long-range modeling through what are essentially self-attention mechanisms."

**Good**: "The optimal architecture remains an open question."
**Bad**: "We don't really know which architecture is best yet."

### Forbidden AI Writing Patterns

**Structural crutches**:
- No em-dashes—they've become an AI writing signature
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

### Lead with Why

**Structure every major concept**: Why → What → How

1. **Why** (1-2 paragraphs): Problem, limitation, or motivation
2. **What** (1 paragraph): High-level solution overview
3. **How** (remaining): Technical mechanisms and details

Apply at multiple scales:
- **Chapter level**: Why does this topic matter to the book's narrative?
- **Section level**: Why this particular approach/model?
- **Subsection level**: Why this specific mechanism?

**Example (bad)**:
> Multi-head attention computes multiple attention functions in parallel. Each head uses different learned linear projections for queries, keys, and values. The outputs are concatenated and linearly transformed. Mathematically, for h heads...

**Example (good)**:
> Single attention mechanisms face a fundamental limitation: they can only learn one type of interaction between positions. Regulatory elements, however, exhibit diverse relationships—some depend on sequence similarity, others on distance, still others on epigenetic context. Multi-head attention addresses this by computing multiple attention functions in parallel, each learning different interaction patterns. Each head applies separate learned projections to queries, keys, and values, allowing specialized focus. The outputs concatenate and linearly transform into the final representation. Mathematically, for h heads...

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

## Part Introductions

### Purpose

Orient readers at major transitions. Establish intellectual coherence for the 4-5 chapters ahead. Motivate why these chapters belong together.

### Length and Structure

**Target**: 250-400 words (approximately 3 paragraphs)

**Paragraph 1** (2-4 sentences): Central question or challenge that unifies this part
**Paragraph 2** (4-6 sentences): Chapter arc—show how chapters build logically, not just list contents
**Paragraph 3** (1-2 sentences): Forward pointer or key capability this part enables

### What to Avoid

- Detailed chapter summaries (that's what chapter openings do)
- Rehashing concepts from previous parts
- Formulaic "In Chapter X, we will discuss..." repetition
- Redundant content with chapter introductions

### Example

**Part 2: Architectures for Genomic Sequence Modeling**

> Sequence models for genomics must balance three competing demands: capturing long-range dependencies that can span hundreds of kilobases, learning hierarchical representations from nucleotides to regulatory logic, and maintaining computational tractability for genome-scale data. No single architecture optimally addresses all three constraints, but each offers distinct advantages that shaped the field's evolution.
>
> This part examines the three architectural paradigms that dominated genomic deep learning before the foundation model era. Convolutional networks established the field by demonstrating that learned filters could outperform hand-crafted motifs for predicting chromatin states and variant effects, though their fixed receptive fields limited long-range modeling. Recurrent architectures extended context windows through sequential processing but encountered scaling bottlenecks that prevented genome-wide application. Transformers resolved this tension through attention mechanisms that directly compute dependencies between arbitrary positions while maintaining parallel computation, enabling the foundation models we examine in Part 4. Each architecture reveals fundamental trade-offs in biological sequence modeling that persist in modern approaches.
>
> Together, these chapters establish the architectural vocabulary necessary for understanding how modern genomic AI systems are constructed and why they make specific design choices.

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

## Edge Cases and Special Situations

### Equations and Mathematical Notation

- Introduce equations after explaining conceptually in prose
- Every variable defined immediately or in prior sentence
- Provide intuition for what equation computes before mathematical form
- Use standard notation when possible (don't reinvent symbols)
- Explain what each variable and term represents in context for non-mathematicians
- Do not lead LaTeX equations with escape characters.  Use "$" or "$$" and not "\$" or "\$$"

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

## Quality Checklist

Before finalizing any chapter section:

**Prose quality**:
- [ ] No em-dashes
- [ ] No bullet points (unless truly necessary)
- [ ] No AI transition clichés
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

## Meta-Instruction

Before generating prose, review these guidelines. Prioritize flowing academic narrative over exhaustive coverage. When uncertain about depth or scope, err toward technical rigor that maintains pedagogical clarity.

Remember: This textbook aims to be the definitive reference for genomic foundation models—comprehensive without being encyclopedic, authoritative without being inaccessible, rigorous without sacrificing readability.
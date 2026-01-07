# Line Editing Guide

Detailed patterns for sentence-level prose refinement in scientific textbooks.

## The Line Editor's Mindset

Line editing is not about imposing a style but about revealing the author's meaning with maximum clarity and minimum friction. Every change should have a reason beyond "I would have written it differently."

---

## Wordiness Patterns

### Filler Phrases to Delete

| Wordy | Concise |
|-------|---------|
| in order to | to |
| for the purpose of | to, for |
| in the event that | if |
| at this point in time | now |
| due to the fact that | because |
| in spite of the fact that | although, despite |
| it is important to note that | [delete; just note it] |
| it should be pointed out that | [delete; just point it out] |
| the reason why is that | because |
| has the ability to | can |
| is able to | can |
| in close proximity to | near |
| a large number of | many |
| a small number of | few |
| the vast majority of | most |
| at the present time | now, currently |
| prior to | before |
| subsequent to | after |
| in the absence of | without |
| with regard to | about, regarding |
| in terms of | [often deletable] |
| as far as X is concerned | about X, for X |

### Redundancy Patterns

| Redundant | Preferred |
|-----------|-----------|
| completely eliminate | eliminate |
| absolutely essential | essential |
| basic fundamentals | fundamentals |
| future plans | plans |
| past history | history |
| end result | result |
| final outcome | outcome |
| consensus of opinion | consensus |
| each individual | each |
| close scrutiny | scrutiny |
| new innovation | innovation |
| currently ongoing | ongoing |
| brief summary | summary |
| unexpected surprise | surprise |
| repeat again | repeat |

### Throat-Clearing Openers

Delete these common sentence openers:

- "It is worth noting that..."
- "It is interesting to observe that..."
- "One thing to consider is..."
- "What we find is that..."
- "It turns out that..."
- "The key point here is that..."
- "As we have seen..."
- "As mentioned above..."

---

## Active vs. Passive Voice

### When Active is Better

Use active voice when:
- The agent matters: "The model predicts variants" not "Variants are predicted"
- Action drives the narrative: "Researchers discovered" not "It was discovered"
- Clarity requires it: Active often shorter and clearer

### When Passive is Acceptable

Passive voice works when:
- The receiver matters more: "DNA is replicated during S phase"
- The agent is unknown: "The mutation was first observed in 1987"
- Scientific convention: Methods sections often use passive
- Emphasis requires it: "Rare variants are often missed by GWAS"

### Passive Voice Fixes

| Passive | Active |
|---------|--------|
| It was shown by Smith that... | Smith showed... |
| Experiments were performed... | We performed... / Researchers performed... |
| It can be seen that... | [Just state the observation] |
| It has been reported that... | Studies report... / [Cite] found... |

---

## Nominalization (Turning Verbs into Nouns)

Nominalizations often weaken prose by hiding the action.

| Nominalized | Verbal |
|-------------|--------|
| made a decision | decided |
| conducted an investigation | investigated |
| performed an analysis | analyzed |
| gave an explanation | explained |
| made an improvement | improved |
| had a discussion | discussed |
| made a comparison | compared |
| took into consideration | considered |
| achieved a reduction | reduced |
| exhibited a preference | preferred |

### Exceptions

Some nominalizations are fine:
- When the noun itself is the subject: "The mutation causes disease"
- Established terms: "This explanation clarifies..."
- When parallel structure requires it

---

## Sentence Variety

### Length Variation

Aim for mix:
- **Short** (5-12 words): Punch, emphasis, transition
- **Medium** (15-25 words): Standard explanation
- **Long** (30-40 words): Complex ideas with proper punctuation

**Red flag**: Three or more sentences of similar length in a row.

### Structure Variation

Mix these patterns:
- **Subject-verb-object**: "The model predicts pathogenicity."
- **Introductory clause**: "Despite limited training data, the model generalizes."
- **Periodic (delayed verb)**: "What decades of GWAS studies revealed, and what foundation models now leverage, is..."
- **Compound**: "The model captures local patterns, but transformers add global context."
- **Question-answer**: "Why do transformers outperform CNNs here? Attention spans the entire sequence."

---

## Transitions

### Between Sentences

| Relationship | Connectors |
|--------------|------------|
| Addition | Moreover, Furthermore, Additionally, Also |
| Contrast | However, Nevertheless, In contrast, Yet, But |
| Cause | Therefore, Thus, Consequently, As a result |
| Example | For instance, For example, Specifically |
| Emphasis | Indeed, In fact, Notably |
| Sequence | First, Next, Then, Finally |
| Comparison | Similarly, Likewise, In the same way |
| Concession | Although, While, Granted |

### Between Paragraphs

Stronger transitions needed:
- Echo key term from previous paragraph
- Use transitional sentence at paragraph start
- Explicit logical connection

**Avoid**: Starting paragraph with "Also," or "Additionally," alone

---

## Hedging Appropriately

### Necessary Hedges

Scientific writing requires appropriate uncertainty:
- "may suggest" (for preliminary findings)
- "appears to" (for observational conclusions)
- "in some cases" (for non-universal phenomena)
- "under these conditions" (for context-dependent claims)

### Hedge Stacking (Avoid)

**Too hedged**: "It may possibly be the case that this could potentially suggest..."
**Better**: "This may suggest..."

### One Hedge Rule

Use at most one hedging word per claim:
- "This suggests..." (not "This may suggest...")
- "The model may fail..." (not "The model may possibly fail...")

---

## Jargon Management

### First Use Rule

Every technical term should be:
1. Defined on first use (inline or parenthetical)
2. Used consistently thereafter
3. Included in glossary

### Jargon Density

**Target**: No more than 3 undefined technical terms per sentence

**High density example** (problematic):
> "The ESM model uses MSA-based PLM embeddings for VEP via transfer learning."

**Lower density version**:
> "ESM generates embeddings from protein sequences. These embeddings, learned from millions of proteins, transfer well to variant effect prediction tasks."

---

## Parallel Structure

### In Lists

All items should have same grammatical form:

**Non-parallel**:
> "The model does three things: classifying variants, prediction of effects, and it ranks candidates."

**Parallel**:
> "The model classifies variants, predicts effects, and ranks candidates."

### In Comparisons

**Non-parallel**:
> "Transformers are better at capturing long-range dependencies than CNNs capture them."

**Parallel**:
> "Transformers capture long-range dependencies better than CNNs do."

---

## Common Errors

### That vs. Which

- **That**: Restrictive (essential), no comma
- **Which**: Non-restrictive (parenthetical), with comma

**Correct**: "Variants that are pathogenic require follow-up."
**Correct**: "These variants, which are mostly benign, can be filtered."

### Dangling Modifiers

**Dangling**: "Using attention mechanisms, long-range patterns are captured."
(Patterns aren't using attention)

**Fixed**: "Using attention mechanisms, transformers capture long-range patterns."

### Subject-Verb Agreement with Complex Subjects

**Wrong**: "The family of models that include ESM-2..."
**Right**: "The family of models that includes ESM-2..."

---

## Academic Voice Calibration

### Confident Without Arrogant

| Avoid | Prefer |
|-------|--------|
| "Obviously" | [State claim and support] |
| "Of course" | [Delete or explain why obvious] |
| "Clearly" | [Provide evidence instead] |
| "Undoubtedly" | [Let evidence speak] |
| "It is well known that" | [Cite sources] |

### Authoritative Without Pompous

| Avoid | Prefer |
|-------|--------|
| "We shall endeavor to demonstrate" | "We show" |
| "It behooves us to consider" | "Consider" |
| "The present investigation" | "This study" / "We" |
| "One might argue that" | "Some argue" / [Make the argument] |

### Engaging Without Casual

| Avoid in Formal Text | Acceptable |
|---------------------|------------|
| "So basically..." | [Delete] |
| "Pretty much" | "largely" / "mostly" |
| "A lot of" | "many" / "numerous" |
| "Kind of" | [Be specific] |
| "Stuff" | [Be specific] |

---

## Paragraph Architecture

### Topic Sentence (First)

Opens with paragraph's main claim. Reader should know what paragraph is about from first sentence.

### Development (Middle)

Supports topic sentence with:
- Evidence
- Examples
- Explanation
- Elaboration

### Conclusion/Transition (Last)

Either:
- Summarizes paragraph's contribution
- Bridges to next paragraph
- Provides significance

### Ideal Length

- **Minimum**: 3 sentences (topic + support + conclusion)
- **Maximum**: 8-10 sentences (beyond this, usually should split)
- **Average target**: 5-7 sentences

---

## The Final Polish

### Read Aloud Test

If you stumble reading it aloud, the reader will stumble too.

### The So-What Test

After each paragraph, ask: "So what?" If you can't answer, the paragraph needs a clearer point.

### The Deletion Test

Can any word/phrase be deleted without losing meaning? If so, delete it.

### The Substitution Test

Is there a simpler word that means the same thing? If so, use it.

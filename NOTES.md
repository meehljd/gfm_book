# 1. Major conceptual gaps (content, not tone)
## 1.1. Deep learning “primers” are implicit, not explicit

Right now, you introduce CNNs, Transformers, and self-supervision inside the case-study chapters:

CNNs: introduced via DeepSEA / ExPecto / SpliceAI (ch05–07)

Transformers & self-supervision: via Protein LMs (ch09), DNA FMs (ch10)

Hybrid CNN+Transformer: Enformer/Borzoi (ch11)

For readers who already know DL, this is fine. For genomics-first readers, there’s no single “deep learning in 30 pages” place to anchor:

What is a neural net, loss, optimizer?

What is a CNN vs a Transformer at a high level?

What is self-supervised pretraining vs supervised fine-tuning?

Basic pitfalls like overfitting, capacity, regularization, etc.

Suggestion (optional but helpful):

Add either:

A short early chapter (e.g., between ch04 and ch05) or

An appendix

on “Deep Learning Basics for Genomics” that:

Introduces feedforward nets, CNNs, Transformers, attention

Explains supervised vs self-supervised training

Gives a quick tour of common training/eval practices

Then the model chapters can lean on that rather than re-explaining pieces.

## 1.2. Generative design is present only in passing

You do cover generative / self-supervised representation learning (GROVER, DNA LMs, etc.), and you hint at lab-in-the-loop GFMs and experimental design (ch10, ch18, ch19). But there’s no focused treatment of sequence / perturbation design as a topic:

Generating regulatory sequences with desired outputs

Using models to design CRISPR/MPRA libraries beyond simple prioritization

Protein design vs just variant scoring

Optimization loops (Bayesian optimization, RL, evolutionary search) around GFMs

Right now this content is scattered as “forward look” bullets.

Suggestion: Either:

Expand the “Forward look / lab-in-the-loop” parts of ch18–19 into a clearly marked section on generative design, or

If you want a dedicated space, a short chapter (maybe at the end of Part IV or folded into Part V) on “From Prediction to Design & Closed Loops” that consolidates:

GFM → design candidates → assay → retrain loops

Sequence design vs library design vs experiment design

This is a natural “future-looking” capstone that matches the GFM theme.

## 1.3. One missing “unifying” chapter on evaluation & benchmarks

You actually talk about evaluation and benchmarks in multiple places:

ch10: “Evaluation, Benchmarks, and Pitfalls” for DNA LMs

ch12: “Evaluating Genomic FMs” (benchmarks, zero-shot vs finetune)

ch14: confounders & leakage

ch17: clinical metrics, discrimination, calibration, etc.

What’s missing is a single conceptual home for:

Types of evaluation (molecular, variant-level, trait-level, clinical)

Data splitting issues (by locus, by region, by individual, by ancestry)

Relationship between benchmark scores and real clinical utility

Right now, a reader has to piece this together.

Suggestion:

Decide which chapter “owns” the general evaluation philosophy.

My vote: ch12 “Genomic FMs: Principles & Practice” is a natural place for a unified eval framework, and ch10 can just say “see ch12 for broader evaluation issues.”

Use ch14 specifically for confounders & leakage, not general eval philosophy, and cross-link from ch12 and ch17.

## 1.4. Implementation & engineering is light

You do touch on:

Monitoring, drift, deployment (ch17)

Biotech workflows and build vs buy (ch19)

Some training & data issues scattered elsewhere

But there isn’t a dedicated “how you actually build and run these models in practice” chapter:

Data pipelines, sharding, scaling, hardware

Training recipes, hyperparameters, mixed precision

Model serving, latency/throughput tradeoffs

Depending on your audience, this might be totally fine (the book is more conceptual/research-oriented). If you expect industry readers, a short “Engineering GFMs in Practice” section in ch17 or ch19 might be worthwhile.

# 2. Part-by-part flow and re-ordering
## Part I: Data & Pre-DL Methods (ch01–04)

Current structure:

ch01 – NGS & Variant Calling

ch02 – PRS & GWAS Basics

ch03 – Deleteriousness Scores (CADD, etc.)

ch04 – Foundational Genomics Data (ENCODE, gnomAD, GTEx, biobanks, etc.)

Strengths:

Covers the standard pre-DL baselines: PRS, GWAS, CADD, key data resources.

ch01→02→03 builds a nice story from variants → traits → pathogenicity scores.

Potential issues & tweaks:

Data resources vs CADD ordering

ch03 already introduces many of the same resources (e.g., conservation scores, ENCODE) as features for CADD.

ch04 then returns to these resources in a more general way.

You could:

Keep order as-is but minimize duplication, e.g. in ch03 say “see ch04 for more on ENCODE/gnomAD; here we focus on how CADD uses them.”

Or swap ch03 and ch04 so the reader first sees a broad survey of ENCODE/gnomAD/ClinVar/etc. and then sees how CADD composes them.

Either works; I’d pick one and then add cross-references to avoid feeling repetitive.

ch01 feels short compared to later chapters

ch01 (~80 lines) is much lighter than ch03–04 (>180–200 lines).

If you want a more uniform Part I, you could either:

Slightly expand ch01 with more on sequencing technologies, QC, read mapping pitfalls, or

Fold ch01 and parts of ch04 into a single “From Reads to Datasets & Benchmarks” chapter.

I lean toward just expanding ch01 rather than merging, to keep the “raw data → variants” story separate and clean.

Overall, Part I content is complete for your aims; the main decision is whether to reorder ch03 & ch04 and how much duplication you tolerate.

## Part II: CNN Seq-to-Function Models (ch05–07)

ch05 – Regulatory Prediction (DeepSEA and lineage)

ch06 – Transcriptional Effects (ExPecto-ish hybrid)

ch07 – Splicing Prediction (SpliceAI)

This progression (chromatin → expression → splicing) is logical and historically accurate.

Possible refinements:

Keep three chapters separate. They’re long enough (157–297 lines) that merging 05+06 would create a behemoth.

Make sure ch05 and ch06 clearly differentiate:

ch05: sequence → chromatin/regulatory states

ch06: sequence → expression using regulatory intermediates

You might add a short mini-summary section at end of ch07 that frames Part II as:

“We’ve seen how CNNs + local context powered early sequence-to-function models; Part III now introduces Transformer-based FMs that inherit many of these ideas but change the training objective and context length.”

No big structural changes needed here.

## Part III: Transformers Models (ch08–11)

ch08 – Sequence Representation & Tokens

ch09 – Protein Language Models

ch10 – DNA Foundation Models

ch11 – Long-range Hybrid Models (Enformer, Borzoi)

What works well:

ch08 as a tokenization/representation chapter nicely sets up why Transformers care about k-mers vs BPE vs single-base tokens.

ch09 → ch10 → ch11 is a good arc: PLMs → DNA LMs → hybrid sequence-to-function.

Potential tweaks:

Transformer “crash course”

Most of the architectural detail is folded into PLM/DNA LM chapters.

Consider adding a short “Transformers in 2 pages” section either:

At the end of ch08, or

At the beginning of ch09

Just enough to give the architecture and the idea of attention, positional encodings, and pretraining.

Avoid conceptual duplication with ch12

ch10 already talks about DNA LMs as foundation models, evaluation suites, and pitfalls.

ch12 then introduces the general GFM definition, taxonomy, and evaluation.

I’d recommend:

Let ch10 stay model-centric (DNABERT, Nucleotide Transformer, HyenaDNA, GROVER), with a compact eval section.

Push the broader “what makes a model a GFM, how should we evaluate them” discussion fully into ch12, and in ch10 simply say “see ch12 for a general treatment of GFM evaluation & pitfalls.”

No need to merge or split chapters in Part III; just sharpen the division of labor between ch10 and ch12.

## Part IV: GFMs & Multi-omics (ch12–16)

ch12 – Genomic FMs: Principles & Practice

ch13 – Variant Effect Prediction (AlphaMissense, Evo2, AlphaGenome…)

ch14 – Confounders in Model Training

ch15 – Interpretability & Mechanisms

ch16 – Multi-omics and Systems Context

This part is the heart of the book and already covers:

GFM definition, taxonomy, design dimensions, evaluation, safety (ch12)

Modern GFM-based VEP models (ch13)

Confounders & fairness (ch14)

Interpretability & mechanistic insight (ch15)

Multi-omics / systems GFMs (ch16)

Comments & suggestions:

ch12 is dense but coherent

It spans:

Definition & taxonomy

Design dimensions

Evaluation

Practical usage

Safety/robustness

Open challenges

You could split it into:

12: What is a GFM? Taxonomy & design

13: Evaluation, practice, and safety

but you already have a concrete application chapter next (current ch13). I’d keep ch12 as a single “conceptual keystone” and instead:

Reign in redundant evaluation content elsewhere

Use ch12 as the canonical reference for eval/safety

Ordering inside Part IV is mostly good

Current order:

First: conceptual GFM overview (12)

Then: VEP-focused GFMs (13)

Then: reliability (confounders) and interpretability (14–15)

Finally: multi-omics & systems GFMs (16)

Two alternatives you might consider:

Option A (minimal change, keep as-is): This is defensible—multi-omics feels like a “capstone method” that benefits from having confounders/interpretability in the reader’s mind.

Option B (slightly more method-first):

12: GFM principles

13: VEP models

16: Multi-omic & systems GFMs

14: Confounders

15: Interpretability

So all “big models” (VEP + multi-omics) are introduced before you drill into reliability & interpretability.

I don’t think you must reorder; I’d just make sure chapter intros explicitly remind the reader where they are in the arc.

ch14 & ch15 are very strong cross-cutting chapters

They’re not really “about GFMs only” – they apply equally to DeepSEA, Enformer, etc. You could:

Keep them in Part IV but in the introductions explicitly say:

“The issues in this chapter apply to all models you’ve seen so far, from CNNs (Part II) to hybrid models (Part III) to GFMs (Part IV).”

Or, more drastic: create a new Part V: Reliability & Interpretation and then shift the current applications to Part VI. That’s a big re-numbering, so only worth it if you really want a separate “Reliability” part.

## Part V: Applications (ch17–19)

ch17 – Clinical Risk Prediction

ch18 – Pathogenic Variant Discovery

ch19 – Drug Discovery & Biotech

This is exactly the trio you described: risk, pathogenic variants, drug/biotech.

Strengths:

Clear escalation: patient-level risk → variant/gene discovery → pipeline/biotech workflows.

Each chapter has a crisp core:

ch17: risk tasks, metrics, EHR fusion, deployment

ch18: variant prioritization pipelines, rare disease, cancer drivers

ch19: targets, screens, biomarkers, org-level workflows

Suggestions:

Make the distinction between ch18 and ch19 very explicit

There is natural overlap (target discovery vs variant discovery), so early paragraphs should make clear:

ch18 is about “Who/what is causal?” (variants/genes, mostly from a statistical genetics / genomics perspective)

ch19 is about “What do you do with that in the drug pipeline and in biotech orgs?”

Consolidate generative / lab-in-the-loop story

Right now, elements of closed-loop experiment design are spread across ch18 and ch19. I’d explicitly frame a subsection (probably in ch19) as:

“From Static GFMs to Lab-in-the-Loop Systems”

and cross-reference it from ch18, so readers know where the “grand vision” lives.

No need to merge/split here

The three chapters are long but focused. I wouldn’t combine them; you’d create unwieldy mega-chapters that blur distinct audiences (clinicians vs discovery scientists vs biotech engineers).

# 3. Concrete combine/split recommendations

Keep separate (good as-is):

ch05, ch06, ch07 – CNN models for regulatory/expression/splicing

ch09, ch10, ch11 – PLMs, DNA FMs, hybrid models

ch17, ch18, ch19 – applications

Potentially combine (only if you want fewer chapters):

ch01 + selected parts of ch04 into a single “From Sequencing to Data Resources” chapter.
Personally I’d prefer to keep them separate and just expand ch01.

Potentially split (if you want shorter, lighter chapters):

ch12 – Genomic FMs: Principles & Practice

If you find it’s too dense when edited, natural split point is:

12: definition, taxonomy, design dimensions

13: eval, practical use, safety & robustness

But this would force a shift in numbering and require renaming current ch13, so only do it if, after revisions, ch12 still feels overloaded.

Otherwise, most chapter boundaries look sensible.

4. Summary

No catastrophic content gaps. You cover data, classical methods, CNNs, Transformers, GFMs, multi-omics, confounders, interpretability, and core applications.

Biggest “missing” thing is a concise deep-learning primer and a clearer, consolidated treatment of evaluation & generative design.

Flow is mostly solid. A light touch on reordering in Part I and clarifying the division of labor between ch10–12–14–17 would make the conceptual structure crisper.

Chapters to watch for bloat: ch12, ch15, ch17. They’re central and long; worth ensuring each has a very sharp scope and that evaluation/ethical content isn’t too redundant across them.

If you’d like, next step could be: pick one part (say Part I or Part IV), and we can sketch a cleaned-up “reader journey” with explicit cross-references and maybe a short graphic/figure list that reinforces the flow.
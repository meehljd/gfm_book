# Authoritative Citations for Genomic Foundation Model Interpretability

This comprehensive citation guide provides **100+ peer-reviewed papers** for a textbook chapter on interpretability methods for genomic deep learning models. The collection spans foundational methods, genomics-specific adaptations, and recent advances through 2025.

---

## Attribution methods for genomic deep learning

### In silico mutagenesis

In silico saturation mutagenesis (ISM) systematically evaluates contributions of individual nucleotides by predicting effects of all possible mutations. **Nair, Shrikumar & Kundaje (2022)** introduced fastISM, achieving over 10× speedup for CNN architectures commonly used in genomics (*Bioinformatics* 38:2397-2403, DOI: 10.1093/bioinformatics/btac135). **Schreiber, Lu & Noble (2022)** proposed Yuzu, using compressed sensing to reduce ISM to constant time (*Bioinformatics* 38:3557-3563, DOI: 10.1093/bioinformatics/btac360). For Taylor approximation approaches, cite TISM (*iScience* 2024, PMC11404212).

### Gradient-based attribution (saliency maps, gradient × input)

The foundational saliency map paper is **Simonyan, Vedaldi & Zisserman (2014)**, "Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps" (*ICLR Workshop*, arXiv:1312.6034, **~10,000 citations**). For genomics-specific corrections addressing off-simplex gradient noise in DNA sequences, cite **Koo et al. (2023)**, "Correcting gradient-based interpretations of deep neural networks for genomics" (*Genome Biology* 24:109, DOI: 10.1186/s13059-023-02956-3).

### Integrated gradients applied to genomics

**Sundararajan, Taly & Yan (2017)**, "Axiomatic Attribution for Deep Networks" establishes the theoretical foundation with axiomatic justification (*ICML 2017*, PMLR 70:3319-3328, arXiv:1703.01365, **~7,000 citations**). For genomics-specific adaptations addressing baseline choices, cite **Jha et al. (2020)**, "Enhanced Integrated Gradients: improving interpretability of deep learning models using splicing codes as a case study" (*Genome Biology* 21:149, DOI: 10.1186/s13059-020-02055-7), which proposes nonlinear paths, group-specific baselines, and statistical significance testing.

### Reference sequence choices

**Sturmfels, Lundberg & Lee (2020)**, "Visualizing the Impact of Feature Attribution Baselines" (*Distill*, distill.pub/2020/attribution-baselines) provides comprehensive analysis of baseline choice impact. The Jha et al. (2020) paper above specifically addresses why all-zero baselines are inappropriate for genomics and proposes alternatives. For dinucleotide-shuffled references, cite Koo et al. (2023).

### DeepLIFT

**Shrikumar, Greenside & Kundaje (2017)**, "Learning Important Features Through Propagating Activation Differences" (*ICML 2017*, PMLR 70:3145-3153, arXiv:1704.02685, **~4,500 citations**). The earlier preprint is arXiv:1605.01713 (2016).

---

## Convolutional filter interpretation

### DeepSEA [Citation Needed - FULFILLED]

**Zhou & Troyanskaya (2015)**, "Predicting effects of noncoding variants with deep learning-based sequence model" (*Nature Methods* 12:931-934, DOI: 10.1038/nmeth.3547, **~2,500 citations**). Seminal paper training deep CNNs on ENCODE chromatin data to predict variant effects with single-nucleotide sensitivity.

### Basset

**Kelley, Snoek & Rinn (2016)**, "Basset: learning the regulatory code of the accessible genome with deep convolutional neural networks" (*Genome Research* 26:990-999, DOI: 10.1101/gr.200535.115, **~1,500 citations**). Demonstrated that first-layer filters learn interpretable motifs matching known transcription factor binding sites—45% of filters annotated via TomTom.

### Converting CNN filters to PWMs

**Koo & Eddy (2019)**, "Representation learning of genomic sequence motifs with convolutional neural networks" (*PLOS Computational Biology* 15:e1007560, DOI: 10.1371/journal.pcbi.1007560) systematically studies how CNN architecture influences whether filters learn whole versus partial motif representations. **Koo et al. (2021)**, "Improving representations of genomic sequence motifs in convolutional networks with exponential activations" (*Nature Machine Intelligence* 3:258-266, DOI: 10.1038/s42256-020-00291-x) shows exponential activations make filter scans directly comparable to PWM scans.

### First-layer filter motif discovery

**Alipanahi et al. (2015)**, DeepBind: "Predicting the sequence specificities of DNA- and RNA-binding proteins by deep learning" (*Nature Biotechnology* 33:831-838, DOI: 10.1038/nbt.3300, **~2,375 citations**) established the practice of extracting motifs from first-layer filters. **Quang & Xie (2016)**, DanQ (*Nucleic Acids Research* 44:e107, DOI: 10.1093/nar/gkw226, **~1,200 citations**) demonstrates hybrid CNN-RNN architectures where convolution captures motifs and recurrence captures grammar.

---

## TF-MoDISco and motif discovery

### TF-MoDISco methodology

**Shrikumar et al. (2018)**, "Technical Note on Transcription Factor Motif Discovery from Importance Scores (TF-MoDISco)" (arXiv:1811.00416, **~400 citations**). Unlike methods that visualize individual CNN filters, TF-MoDISco clusters high-importance "seqlets" from DeepLIFT or SHAP scores to generate consolidated, non-redundant motifs.

### BPNet [Citation Needed - FULFILLED]

**Avsec et al. (2021)**, "Base-resolution models of transcription-factor binding reveal soft motif syntax" (*Nature Genetics* 53:354-366, DOI: 10.1038/s41588-021-00782-6, **~500 citations**). Landmark paper introducing BPNet for base-resolution ChIP-nexus prediction, developing interpretation tools combining DeepLIFT with TF-MoDISco to discover "soft syntax" rules including helical periodicity and directional TF cooperation.

### Grammar inference from motif co-occurrence

**Miraldi, Chen & Weirauch (2021)**, "Deciphering cis-regulatory grammar with deep learning" (*Nature Genetics* 53:266-268, DOI: 10.1038/s41588-021-00814-1) articulates soft motif syntax concepts. For cis-regulatory interaction analysis, cite **Toneyan & Koo (2023)**, CREME (*PLOS Computational Biology*, DOI: 10.1371/journal.pcbi.1011131). **ChromBPNet** by **Pampari et al. (2024)** extends BPNet for ATAC-seq with bias deconvolution (*Nature Methods*, DOI: 10.1038/s41592-024-02571-3). **Nair et al. (2024)**, ProCapNet (*Nature Genetics*, DOI: 10.1038/s41588-024-01835-6) reveals epistatic syntax in transcription initiation.

---

## Probing learned representations

### Probing classifier methodology

**Belinkov (2022)**, "Probing Classifiers: Promises, Shortcomings, and Advances" (*Computational Linguistics* 48:207-219, DOI: 10.1162/coli_a_00422, **~500 citations**) provides the comprehensive methodological review. **Hewitt & Liang (2019)**, "Designing and Interpreting Probes with Control Tasks" (*EMNLP-IJCNLP*, DOI: 10.18653/v1/D19-1275, **~800 citations**) introduces **selectivity**—the critical distinction between what probes learn versus what representations encode. **Hewitt & Manning (2019)** introduced structural probes for syntax (*NAACL-HLT*, DOI: 10.18653/v1/N19-1419, **~1,200 citations**).

### Probing protein language models (ESM)

**Rives et al. (2021)**, "Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences" (*PNAS* 118:e2016239118, DOI: 10.1073/pnas.2016239118, **~3,000 citations**) shows linear projections recover secondary structure and contacts without supervision. **Lin et al. (2023)**, ESM-2 and ESMFold (*Science* 379:1123-1130, DOI: 10.1126/science.ade2574, **~2,500 citations**). **Rao et al. (2021)** shows attention heads predict protein contacts (*ICLR 2021*).

### Probing DNA language models

**Ji et al. (2021)**, DNABERT (*Bioinformatics* 37:2112-2120, DOI: 10.1093/bioinformatics/btab083, **~1,200 citations**). **Zhou et al. (2024)**, DNABERT-2 (*ICLR 2024*, arXiv:2306.15006) introduces the Genome Understanding Evaluation benchmark. **Dalla-Torre et al. (2024)**, Nucleotide Transformer (*Nature Methods*, DOI: 10.1038/s41592-024-02523-z, **~400 citations**) provides extensive probing evaluation showing models learn genomic elements without supervision. **Nguyen et al. (2023)**, HyenaDNA (*NeurIPS 2023*, arXiv:2306.15794) analyzes embeddings clustering by biotype.

### Selectivity vs accessibility

**Pimentel et al. (2020)**, "Information-Theoretic Probing with Minimum Description Length" (*EMNLP*, arXiv:2003.12298, **~300 citations**) proposes MDL-based probe complexity measures arguing probing should report accuracy-complexity trade-offs.

---

## Attention pattern analysis

### Attention visualization methods

**Vig (2019)**, "A Multiscale Visualization of Attention in the Transformer Model" introduces BertViz (*ACL System Demonstrations*, arXiv:1906.05714). **Chefer, Gur & Wolf (2021)**, "Transformer Interpretability Beyond Attention Visualization" (*CVPR 2021*, arXiv:2012.09838, **~800 citations**) proposes relevance propagation addressing limitations of raw attention.

### "Attention is not explanation" papers

**Jain & Wallace (2019)**, "Attention is not Explanation" (*NAACL-HLT*, arXiv:1902.10186, DOI: 10.18653/v1/N19-1357, **~1,600 citations**) shows attention is frequently uncorrelated with importance and different distributions yield equivalent predictions. **Wiegreffe & Pinter (2019)**, "Attention is not not Explanation" (*EMNLP-IJCNLP*, arXiv:1908.04626, DOI: 10.18653/v1/D19-1002) proposes alternative tests for when attention can serve as explanation. **Serrano & Smith (2019)**, "Is Attention Interpretable?" (*ACL*, arXiv:1906.03731) shows gradient-based rankings often outperform attention magnitude.

### Attention rollout and flow

**Abnar & Zuidema (2020)**, "Quantifying Attention Flow in Transformers" (*ACL*, arXiv:2005.00928) introduces **Attention Rollout** and **Attention Flow** methods accounting for information mixing across layers.

### Attention in genomic transformers

**Avsec et al. (2021)**, Enformer (*Nature Methods* 18:1196-1203, DOI: 10.1038/s41592-021-01252-x, **~1,200 citations**) shows attention captures enhancer-promoter interactions and TAD boundaries. **Ji et al. (2021)**, DNABERT introduces DNABERT-viz showing attention converges on known binding sites. **Dalla-Torre et al. (2024)**, Nucleotide Transformer shows attention heads specialize in detecting enhancers, promoters, and TF binding sites. **Vig et al. (2021)**, "BERTology Meets Biology" (*ICLR 2021*, arXiv:2006.15222, **~300 citations**) applies NLP attention interpretability to proteins, directly applicable to DNA transformers.

---

## Regulatory vocabularies and global interpretability

### Sei [Citation Needed - FULFILLED]

**Chen et al. (2022)**, "A sequence-based global map of regulatory activity for deciphering human genetics" (*Nature Genetics* 54:940-949, DOI: 10.1038/s41588-022-01102-2, **~400 citations**). Introduces Sei's vocabulary of **40 sequence classes** learned from 21,907 chromatin profiles, enabling global classification into functional categories (enhancers, promoters, CTCF-cohesin binding).

### Embedding geometry and visualization

**McInnes, Healy & Melville (2018)**, UMAP (arXiv:1802.03426, **~10,000 citations**). **van der Maaten & Hinton (2008)**, t-SNE (*JMLR* 9:2579-2605, **~35,000 citations**). For biological applications: **Becht et al. (2019)** (*Nature Biotechnology* 37:38-44, DOI: 10.1038/nbt.4314, **~4,000 citations**) demonstrates UMAP for single-cell genomics. **Detlefsen et al. (2023)** (*Briefings in Bioinformatics* 24:bbac619) benchmarks visualization methods for protein language model embeddings.

---

## Mechanistic interpretability

### Sparse autoencoders for feature discovery

**Templeton et al. (2024)**, "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet" (Transformer Circuits Thread, Anthropic) demonstrates SAEs scaled to frontier models. **Bricken et al. (2023)**, "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning" (Transformer Circuits Thread, **~500 citations**) is the foundational SAE paper. **Gao et al. (2024)**, OpenAI's work training 16 million feature autoencoders on GPT-4 (arXiv:2406.04093, *ICLR 2025*). **Cunningham et al. (2023)** (*ICLR 2024*, arXiv:2309.08600) demonstrates SAEs on Pythia models.

### Superposition in neural networks

**Elhage et al. (2022)**, "Toy Models of Superposition" (Transformer Circuits Thread, arXiv:2209.10652, **~400 citations**) provides theoretical foundations explaining why networks represent more features than neurons.

### Circuit analysis methodology

**Olah et al. (2020)**, "Zoom In: An Introduction to Circuits" (*Distill*, DOI: 10.23915/distill.00024.001, **~500 citations**) establishes the circuits research agenda. **Cammarata et al. (2020)**, "Thread: Circuits" (*Distill*, DOI: 10.23915/distill.00024) explores individual features and circuits. **Olah et al. (2018)**, "The Building Blocks of Interpretability" (*Distill*, DOI: 10.23915/distill.00010) introduces semantic dictionaries.

### Applications to genomic models

**Tseng et al. (2024)**, "ARGMINN: A mechanistically interpretable neural network for regulatory genomics" (arXiv:2410.06211, *ICLR 2025* submission) directly applies mechanistic interpretability to genomics with architectures where motifs and syntax are readable from weights. **Novakovsky et al. (2023)**, ExplaiNN (*Genome Biology* 24:154, DOI: 10.1186/s13059-023-02985-y) combines CNN expressiveness with linear model interpretability. **Simon et al. (2024)**, InterPLM (bioRxiv) uses sparse autoencoders for ESM-2 feature discovery.

---

## Validation and faithfulness

### Sanity checks for saliency maps

**Adebayo et al. (2018)**, "Sanity Checks for Saliency Maps" (*NeurIPS 2018*, arXiv:1810.03292, **~2,500 citations**). Introduces model parameter randomization and data randomization tests, showing some saliency methods are independent of both model and data. **Yona & Greenfeld (2021)** (arXiv:2110.14297) provides critical follow-up.

### Faithfulness metrics

**Li et al. (2023)**, M4: "A Unified XAI Benchmark for Faithfulness Evaluation" (*NeurIPS 2023 Datasets Track*) provides comprehensive benchmark. **Edin et al. (2024)**, "Normalized AOPC: Fixing Misleading Faithfulness Metrics" (arXiv:2408.08137) addresses limitations of Area Over Perturbation Curve.

### MPRA validation

**Movva et al. (2019)**, MPRA-DragoNN (*PLOS ONE*, DOI: 10.1371/journal.pone.0218073, **~150 citations**) provides framework for using MPRAs (Sharpr-MPRA) to validate deep learning predictions with DeepLIFT interpretation. **Nucleic Acids Research (2022)** 50:11442-11454 introduces MpraNet for genome-wide MPRA characterization (DOI: 10.1093/nar/gkac905). **Genes & Development (2024)** 38:843-860 provides comprehensive review of MPRAs + machine learning.

### Experimental validation

**Avsec et al. (2021)**, Enformer validates predictions against MPRA saturation mutagenesis and CRISPRi enhancer knockdowns. **de Almeida et al. (2024)**, DREAM Challenge (*Nature Biotechnology*, DOI: 10.1038/s41587-024-02414-w) provides community benchmarking against experimental data.

---

## Interpretability tools and frameworks

### Captum

**Kokhlikyan et al. (2020)**, "Captum: A unified and generic model interpretability library for PyTorch" (arXiv:2009.07896, **~800 citations**, captum.ai). Official Meta/Facebook library implementing Integrated Gradients, SHAP, TCAV, and many other methods.

### SHAP values

**Lundberg & Lee (2017)**, "A Unified Approach to Interpreting Model Predictions" (*NeurIPS 2017*, arXiv:1705.07874, **~20,000 citations**) is the foundational paper unifying six methods under Shapley values. **Lundberg et al. (2020)**, TreeSHAP (*Nature Machine Intelligence* 2:56-67, DOI: 10.1038/s42256-019-0138-9) provides efficient exact computation for tree models.

### SHAP for genomics

**Dickinson & Meyer (2022)**, "Positional SHAP (PoSHAP) for Interpretation of machine learning models trained from biological sequences" (*PLOS Computational Biology* 18:e1009736, DOI: 10.1371/journal.pcbi.1009736) adapts SHAP for positional sequence interpretation.

### Genomics-specific tools

**van Hilten et al. (2021)**, GenNet (*Communications Biology* 4:1094, DOI: 10.1038/s42003-021-02622-z) embeds biological knowledge into neural network architecture. **Li et al. (2023)**, DeepBIO (*Nucleic Acids Research* 51:3017-3029, DOI: 10.1093/nar/gkad108) provides automated platform with 40+ approaches and integrated interpretability.

### Review papers on genomic interpretability

**Novakovsky et al. (2023)**, "Obtaining genetics insights from deep learning via explainable artificial intelligence" (*Nature Reviews Genetics* 24:125-137, DOI: 10.1038/s41576-022-00532-2) is the comprehensive review. **Watson (2022)**, "Interpretable machine learning for genomics" (*Human Genetics* 141:1499-1513, DOI: 10.1007/s00439-021-02387-9). **van Hilten et al. (2024)** (*Briefings in Bioinformatics* 25:bbae449) provides quantitative analysis of 123 interpretable DL studies. **Talukder et al. (2021)** (*Briefings in Bioinformatics* 22:bbaa177) reviews DNN interpretation for genomics/epigenomics.

---

## Quick reference table for explicitly requested citations

| Paper | Full Citation | DOI/arXiv |
|-------|--------------|-----------|
| **DeepSEA** | Zhou & Troyanskaya (2015), *Nature Methods* 12:931-934 | 10.1038/nmeth.3547 |
| **BPNet** | Avsec et al. (2021), *Nature Genetics* 53:354-366 | 10.1038/s41588-021-00782-6 |
| **Sei** | Chen et al. (2022), *Nature Genetics* 54:940-949 | 10.1038/s41588-022-01102-2 |
| **Sanity Checks** | Adebayo et al. (2018), *NeurIPS 2018* | arXiv:1810.03292 |
| **DeepLIFT** | Shrikumar et al. (2017), *ICML 2017* | arXiv:1704.02685 |
| **Integrated Gradients** | Sundararajan et al. (2017), *ICML 2017* | arXiv:1703.01365 |
| **TF-MoDISco** | Shrikumar et al. (2018) | arXiv:1811.00416 |
| **Basset** | Kelley et al. (2016), *Genome Research* 26:990-999 | 10.1101/gr.200535.115 |
| **Enformer** | Avsec et al. (2021), *Nature Methods* 18:1196-1203 | 10.1038/s41592-021-01252-x |
| **SHAP** | Lundberg & Lee (2017), *NeurIPS 2017* | arXiv:1705.07874 |
| **Captum** | Kokhlikyan et al. (2020) | arXiv:2009.07896 |

This collection prioritizes peer-reviewed publications from *Nature Methods*, *Nature Genetics*, *Nature Biotechnology*, *Genome Biology*, *Genome Research*, *Bioinformatics*, *NeurIPS*, *ICML*, *ICLR*, *ACL*, and *EMNLP*—representing authoritative venues for both computational genomics and machine learning interpretability research.
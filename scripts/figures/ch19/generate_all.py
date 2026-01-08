#!/usr/bin/env python3
"""
Chapter 19: Single-Cell Models Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_4" / "ch19"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Fig 01 A-B: Cellular LM Analogy
def create_fig_01():
    # Panel A: Language analogy
    fig, ax = plt.subplots(figsize=(8, 5))

    comparisons = [
        ('Words', 'Genes', '#1f77b4'),
        ('Sentences', 'Cells', '#2ca02c'),
        ('Documents', 'Tissues', '#ff7f0e'),
        ('Context', 'Cell State', '#9467bd'),
    ]

    for i, (lang, bio, color) in enumerate(comparisons):
        y = len(comparisons) - i - 1
        # Language box
        ax.add_patch(mpatches.FancyBboxPatch((0.5, y - 0.25), 1.5, 0.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor='#aec7e8', edgecolor='#1f77b4', linewidth=2))
        ax.text(1.25, y, lang, ha='center', va='center', fontsize=10, fontweight='bold')

        # Arrow
        ax.annotate('', xy=(3, y), xytext=(2.2, y),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))

        # Biology box
        ax.add_patch(mpatches.FancyBboxPatch((3.2, y - 0.25), 1.5, 0.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(3.95, y, bio, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    ax.text(1.25, 4.2, 'NLP', ha='center', fontsize=11, fontweight='bold')
    ax.text(3.95, 4.2, 'scRNA-seq', ha='center', fontsize=11, fontweight='bold')

    ax.set_xlim(0, 5.5)
    ax.set_ylim(-0.5, 4.5)
    ax.axis('off')
    ax.set_title('A. Language Model Analogy for Single Cells', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-A-fig-cellular-lm-analogy.svg', format='svg')
    plt.close()
    print("Saved: 01-A-fig-cellular-lm-analogy.svg")

    # Panel B: Gene expression as tokens
    fig, ax = plt.subplots(figsize=(6, 4))

    np.random.seed(42)
    genes = ['TP53', 'MYC', 'BRCA1', 'EGFR', 'KRAS', 'BCL2']
    expression = np.random.exponential(2, len(genes))

    colors = plt.cm.viridis(expression / max(expression))
    bars = ax.bar(genes, expression, color=colors, edgecolor='white')

    ax.set_ylabel('Expression Level (log)', fontweight='bold')
    ax.set_title('B. Gene Expression as Tokens', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-cellular-lm-analogy.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-cellular-lm-analogy.svg")

    # Panel C: Parallel structure table
    fig, ax = plt.subplots(figsize=(8, 4))

    parallels = [
        ('Vocabulary', '~30,000 words', '~20,000 genes'),
        ('Document', '~500 words', '~2,000 genes'),
        ('Corpus', 'Wikipedia', 'Cell atlases'),
        ('Task', 'Sentiment', 'Cell type'),
    ]

    ax.axis('off')
    table_data = [[p[0], p[1], p[2]] for p in parallels]
    table = ax.table(cellText=table_data,
                     colLabels=['Concept', 'NLP', 'Single-Cell'],
                     loc='center',
                     cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)
    for i in range(3):
        table[(0, i)].set_facecolor('#1f77b4')
        table[(0, i)].set_text_props(color='white', fontweight='bold')

    ax.set_title('C. Parallel Structure Between Domains', fontweight='bold', loc='left', pad=20)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-C-fig-cellular-lm-analogy.svg', format='svg')
    plt.close()
    print("Saved: 01-C-fig-cellular-lm-analogy.svg")

    # Panel D: What each model type learns
    fig, ax = plt.subplots(figsize=(6, 4))

    model_types = ['BERT-style\n(masked)', 'GPT-style\n(autoregressive)', 'Contrastive', 'VAE']
    learns = [0.85, 0.70, 0.80, 0.75]
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']

    bars = ax.bar(model_types, learns, color=colors, edgecolor='white')
    ax.set_ylabel('Cell Type Classification (F1)', fontweight='bold')
    ax.set_title('D. What Each Model Type Learns', fontweight='bold', loc='left')
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-D-fig-cellular-lm-analogy.svg', format='svg')
    plt.close()
    print("Saved: 01-D-fig-cellular-lm-analogy.svg")

# Fig 02 A-B: Single-Cell Challenges
def create_fig_02():
    np.random.seed(42)

    # Panel A: Sparsity and dropout
    fig, ax = plt.subplots(figsize=(6, 4))

    genes = 50
    cells = 30
    data = np.random.poisson(2, (cells, genes))
    data[np.random.random((cells, genes)) < 0.7] = 0  # 70% dropout

    im = ax.imshow(data, cmap='viridis', aspect='auto')
    ax.set_xlabel('Genes', fontweight='bold')
    ax.set_ylabel('Cells', fontweight='bold')
    ax.set_title('A. Sparsity in scRNA-seq Data', fontweight='bold', loc='left')
    plt.colorbar(im, ax=ax, label='Expression')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-A-fig-single-cell-challenges.svg', format='svg')
    plt.close()
    print("Saved: 02-A-fig-single-cell-challenges.svg")

    # Panel B: Batch effects
    fig, ax = plt.subplots(figsize=(6, 4))

    for i, (batch, color) in enumerate(zip(['Batch 1', 'Batch 2', 'Batch 3'],
                                           ['#1f77b4', '#2ca02c', '#d62728'])):
        x = np.random.randn(50) + i * 2
        y = np.random.randn(50) + (i % 2) * 1.5
        ax.scatter(x, y, c=color, s=30, alpha=0.6, label=batch)

    ax.legend(fontsize=9, title='Technical Batch')
    ax.set_xlabel('UMAP 1', fontweight='bold')
    ax.set_ylabel('UMAP 2', fontweight='bold')
    ax.set_title('B. Batch Effects in Embeddings', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-single-cell-challenges.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-single-cell-challenges.svg")

    # Panel C: Dynamic range
    fig, ax = plt.subplots(figsize=(6, 4))

    expression_levels = ['Housekeeping\ngenes', 'Signaling\nmolecules', 'Transcription\nfactors', 'Rare\ntranscripts']
    counts = [10000, 100, 10, 1]
    colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728']

    bars = ax.bar(expression_levels, counts, color=colors, edgecolor='white')
    ax.set_ylabel('UMI Counts per Cell', fontweight='bold')
    ax.set_title('C. Dynamic Range Spans Orders of Magnitude', fontweight='bold', loc='left')
    ax.set_yscale('log')
    ax.set_ylim(0.5, 50000)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-C-fig-single-cell-challenges.svg', format='svg')
    plt.close()
    print("Saved: 02-C-fig-single-cell-challenges.svg")

    # Panel D: FM strategies for challenges
    fig, ax = plt.subplots(figsize=(8, 4))

    strategies = [
        ('Sparsity', 'Rank-based\ntokenization', '#1f77b4'),
        ('Batch Effects', 'Domain\nadaptation', '#2ca02c'),
        ('Dynamic Range', 'Log\nnormalization', '#ff7f0e'),
        ('Noise', 'Denoising\nobjectives', '#9467bd'),
    ]

    for i, (challenge, solution, color) in enumerate(strategies):
        ax.add_patch(mpatches.FancyBboxPatch((i * 2 + 0.1, 0.8), 1.8, 0.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor='#d62728', alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 2 + 1, 1.2, challenge, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')

        ax.annotate('', xy=(i * 2 + 1, 0.7), xytext=(i * 2 + 1, 0.8),
                    arrowprops=dict(arrowstyle='->', color='#555555', lw=2))

        ax.add_patch(mpatches.FancyBboxPatch((i * 2 + 0.1, -0.1), 1.8, 0.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 2 + 1, 0.3, solution, ha='center', va='center', fontsize=8,
                fontweight='bold', color='white')

    ax.set_xlim(-0.2, 8.2)
    ax.set_ylim(-0.3, 1.8)
    ax.axis('off')
    ax.set_title('D. Foundation Model Strategies for Challenges', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-D-fig-single-cell-challenges.svg', format='svg')
    plt.close()
    print("Saved: 02-D-fig-single-cell-challenges.svg")

# Fig 03 A-B: Geneformer Architecture
def create_fig_03():
    # Panel A: Architecture
    dot = graphviz.Digraph('geneformer', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('cell', 'Single Cell\n(rank-ordered genes)', fillcolor='#aec7e8', shape='box')
    dot.node('embed', 'Gene\nEmbeddings', fillcolor='#98df8a', shape='box')
    dot.node('transformer', 'Transformer\nEncoder', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('mask', 'Masked Gene\nPrediction', fillcolor='#ffbb78', shape='box')
    dot.node('state', 'Cell State\nEmbedding', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.edge('cell', 'embed', label='Tokenize by\nexpression rank')
    dot.edge('embed', 'transformer')
    dot.edge('transformer', 'mask', label='Pretraining')
    dot.edge('transformer', 'state', label='Inference')

    dot.render(OUTPUT_DIR / '03-A-fig-geneformer-architecture', cleanup=True)
    print("Saved: 03-A-fig-geneformer-architecture.svg")

    # Panel B: Rank-based tokenization
    fig, ax = plt.subplots(figsize=(6, 4))

    genes = ['Gene 1', 'Gene 2', 'Gene 3', 'Gene 4', 'Gene 5', 'Gene 6']
    expression = [100, 50, 30, 20, 10, 5]
    ranks = [1, 2, 3, 4, 5, 6]

    ax.barh(genes, expression, color='#1f77b4', edgecolor='white')
    for i, (exp, rank) in enumerate(zip(expression, ranks)):
        ax.text(exp + 2, i, f'Rank {rank}', va='center', fontsize=9, fontweight='bold', color='#d62728')

    ax.set_xlabel('Expression Level', fontweight='bold')
    ax.set_title('B. Rank-Based Tokenization', fontweight='bold', loc='left')
    ax.invert_yaxis()

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-geneformer-architecture.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-geneformer-architecture.svg")

    # Panel C: Attention weights as regulatory relationships
    fig, ax = plt.subplots(figsize=(6, 5))
    np.random.seed(42)

    # Create attention matrix
    n_genes = 6
    gene_names = ['TP53', 'MDM2', 'CDKN1A', 'BAX', 'BCL2', 'CASP3']
    attention = np.random.rand(n_genes, n_genes) * 0.3
    # Add known regulatory relationships
    attention[0, 1] = 0.9  # TP53 -> MDM2
    attention[0, 2] = 0.85  # TP53 -> CDKN1A
    attention[0, 3] = 0.8  # TP53 -> BAX
    attention[1, 0] = 0.7  # MDM2 -> TP53 (feedback)

    im = ax.imshow(attention, cmap='Blues', aspect='equal', vmin=0, vmax=1)
    ax.set_xticks(range(n_genes))
    ax.set_yticks(range(n_genes))
    ax.set_xticklabels(gene_names, fontsize=8, rotation=45, ha='right')
    ax.set_yticklabels(gene_names, fontsize=8)
    ax.set_xlabel('Target Gene', fontweight='bold')
    ax.set_ylabel('Source Gene', fontweight='bold')
    ax.set_title('C. Attention Captures Regulatory Relationships', fontweight='bold', loc='left')
    plt.colorbar(im, ax=ax, label='Attention Weight')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-C-fig-geneformer-architecture.svg', format='svg')
    plt.close()
    print("Saved: 03-C-fig-geneformer-architecture.svg")

    # Panel D: Transfer learning tasks
    fig, ax = plt.subplots(figsize=(6, 4))

    tasks = ['Cell Type\nAnnotation', 'Disease\nClassification', 'Drug Target\nID', 'Batch\nCorrection']
    performance = [0.92, 0.85, 0.78, 0.88]
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']

    bars = ax.bar(tasks, performance, color=colors, edgecolor='white')
    ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)

    ax.set_ylabel('Performance (F1 / Accuracy)', fontweight='bold')
    ax.set_title('D. Transfer to Downstream Tasks', fontweight='bold', loc='left')
    ax.set_ylim(0.4, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-D-fig-geneformer-architecture.svg', format='svg')
    plt.close()
    print("Saved: 03-D-fig-geneformer-architecture.svg")

# Fig 04 A-B: Perturbation Prediction
def create_fig_04():
    # Panel A: Perturbation workflow
    dot = graphviz.Digraph('perturbation', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('cell', 'Cell\nState', fillcolor='#aec7e8', shape='box')
    dot.node('perturb', 'Gene\nPerturbation', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('model', 'scFM\n(Geneformer/scGPT)', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('predict', 'Predicted\nResponse', fillcolor='#98df8a', shape='box')

    dot.edge('cell', 'model')
    dot.edge('perturb', 'model', label='In silico KO')
    dot.edge('model', 'predict')

    dot.render(OUTPUT_DIR / '04-A-fig-perturbation-prediction', cleanup=True)
    print("Saved: 04-A-fig-perturbation-prediction.svg")

    # Panel B: Predicted vs observed
    fig, ax = plt.subplots(figsize=(5, 5))
    np.random.seed(42)

    observed = np.random.randn(50) * 2
    predicted = observed + np.random.randn(50) * 0.5

    ax.scatter(observed, predicted, c='#1f77b4', s=40, alpha=0.6)
    ax.plot([-5, 5], [-5, 5], 'r--', linewidth=2)
    ax.text(2, -3, f'r = 0.85', fontsize=11, fontweight='bold')

    ax.set_xlabel('Observed Log2 FC', fontweight='bold')
    ax.set_ylabel('Predicted Log2 FC', fontweight='bold')
    ax.set_title('B. Perturbation Prediction Accuracy', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-B-fig-perturbation-prediction.svg', format='svg')
    plt.close()
    print("Saved: 04-B-fig-perturbation-prediction.svg")

    # Panel C: Directional relationships and cascades
    dot = graphviz.Digraph('cascade', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('tf', 'Transcription\nFactor KO', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('direct', 'Direct\nTargets', fillcolor='#ff7f0e', shape='box')
    dot.node('indirect', 'Indirect\nEffects', fillcolor='#ffbb78', shape='box')
    dot.node('downstream', 'Downstream\nCascade', fillcolor='#aec7e8', shape='box')

    dot.edge('tf', 'direct', label='1st order')
    dot.edge('direct', 'indirect', label='2nd order')
    dot.edge('indirect', 'downstream', label='3rd order')

    dot.render(OUTPUT_DIR / '04-C-fig-perturbation-prediction', cleanup=True)
    print("Saved: 04-C-fig-perturbation-prediction.svg")

    # Panel D: Performance by gene characterization
    fig, ax = plt.subplots(figsize=(6, 4))

    gene_types = ['Well-\nstudied', 'Moderately\nstudied', 'Poorly\nstudied', 'Novel']
    correlation = [0.85, 0.70, 0.50, 0.30]
    colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728']

    bars = ax.bar(gene_types, correlation, color=colors, edgecolor='white')
    ax.axhline(y=0, color='#555555', linestyle='-', alpha=0.5)

    ax.set_ylabel('Prediction Correlation', fontweight='bold')
    ax.set_title('D. Performance by Gene Characterization', fontweight='bold', loc='left')
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-D-fig-perturbation-prediction.svg', format='svg')
    plt.close()
    print("Saved: 04-D-fig-perturbation-prediction.svg")

# Fig 05 A-B: GLUE Architecture
def create_fig_05():
    # Panel A: Multi-modal integration
    dot = graphviz.Digraph('glue', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('rna', 'scRNA-seq', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('atac', 'scATAC-seq', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('prot', 'CITE-seq', fillcolor='#ff7f0e', fontcolor='white', shape='box')

    dot.node('enc_rna', 'RNA\nEncoder', fillcolor='#aec7e8', shape='box')
    dot.node('enc_atac', 'ATAC\nEncoder', fillcolor='#98df8a', shape='box')
    dot.node('enc_prot', 'Protein\nEncoder', fillcolor='#ffbb78', shape='box')

    dot.node('align', 'Contrastive\nAlignment', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('unified', 'Unified Cell\nEmbedding', fillcolor='#d62728', fontcolor='white', shape='box')

    dot.edge('rna', 'enc_rna')
    dot.edge('atac', 'enc_atac')
    dot.edge('prot', 'enc_prot')
    dot.edge('enc_rna', 'align')
    dot.edge('enc_atac', 'align')
    dot.edge('enc_prot', 'align')
    dot.edge('align', 'unified')

    dot.render(OUTPUT_DIR / '05-A-fig-glue-architecture', cleanup=True)
    print("Saved: 05-A-fig-glue-architecture.svg")

    # Panel B: Modality alignment
    fig, ax = plt.subplots(figsize=(6, 5))
    np.random.seed(42)

    # Before alignment
    rna_x = np.random.randn(50) - 2
    rna_y = np.random.randn(50) - 1
    atac_x = np.random.randn(50) + 2
    atac_y = np.random.randn(50) + 1

    ax.scatter(rna_x, rna_y, c='#1f77b4', s=40, alpha=0.5, label='RNA (before)', marker='o')
    ax.scatter(atac_x, atac_y, c='#2ca02c', s=40, alpha=0.5, label='ATAC (before)', marker='^')

    # After alignment (shifted to overlap)
    ax.scatter(rna_x + 2, rna_y + 1, c='#1f77b4', s=40, alpha=0.8, label='RNA (after)', marker='s')
    ax.scatter(atac_x - 2, atac_y - 1, c='#2ca02c', s=40, alpha=0.8, label='ATAC (after)', marker='d')

    ax.legend(fontsize=8)
    ax.set_xlabel('UMAP 1', fontweight='bold')
    ax.set_ylabel('UMAP 2', fontweight='bold')
    ax.set_title('B. Cross-Modal Alignment', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-B-fig-glue-architecture.svg', format='svg')
    plt.close()
    print("Saved: 05-B-fig-glue-architecture.svg")

    # Panel C: Feature graph with biological prior knowledge
    dot = graphviz.Digraph('feature_graph', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    # Gene nodes
    dot.node('g1', 'Gene 1', fillcolor='#1f77b4', fontcolor='white', shape='circle')
    dot.node('g2', 'Gene 2', fillcolor='#1f77b4', fontcolor='white', shape='circle')
    dot.node('g3', 'Gene 3', fillcolor='#1f77b4', fontcolor='white', shape='circle')

    # Peak nodes
    dot.node('p1', 'Peak 1', fillcolor='#2ca02c', fontcolor='white', shape='circle')
    dot.node('p2', 'Peak 2', fillcolor='#2ca02c', fontcolor='white', shape='circle')

    # Prior knowledge edges
    dot.edge('p1', 'g1', label='Promoter', color='#ff7f0e')
    dot.edge('p1', 'g2', label='Enhancer', color='#9467bd')
    dot.edge('p2', 'g3', label='Promoter', color='#ff7f0e')
    dot.edge('g1', 'g2', label='Co-expression', style='dashed', color='#aec7e8')

    dot.render(OUTPUT_DIR / '05-C-fig-glue-architecture', cleanup=True)
    print("Saved: 05-C-fig-glue-architecture.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 19 figures generated.")

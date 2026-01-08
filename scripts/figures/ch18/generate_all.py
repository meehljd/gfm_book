#!/usr/bin/env python3
"""
Chapter 18: RNA Models Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_4" / "ch18"
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

# Fig 01 A-B: RNA Energy Landscape
def create_fig_01():
    np.random.seed(42)

    # Panel A: Energy landscape concept
    fig, ax = plt.subplots(figsize=(6, 4))

    x = np.linspace(0, 10, 200)
    energy = 3 * np.sin(x) + 0.5 * np.sin(3*x) + 0.3 * np.sin(7*x) + 5

    ax.plot(x, energy, color='#1f77b4', linewidth=2)
    ax.fill_between(x, energy, 10, alpha=0.2, color='#1f77b4')

    # Mark minima
    minima = [1.5, 4.7, 8.2]
    for i, m in enumerate(minima):
        ax.scatter(m, energy[int(m * 20)], s=100, c='#d62728', zorder=5, edgecolors='white')
        if i == 0:
            ax.annotate('Native\nstructure', (m, energy[int(m * 20)] - 0.5),
                        fontsize=9, ha='center')

    ax.set_xlabel('Folding Coordinate', fontweight='bold')
    ax.set_ylabel('Free Energy', fontweight='bold')
    ax.set_title('A. RNA Folding Energy Landscape', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-A-fig-rna-energy-landscape.svg', format='svg')
    plt.close()
    print("Saved: 01-A-fig-rna-energy-landscape.svg")

    # Panel B: Kinetic vs thermodynamic
    fig, ax = plt.subplots(figsize=(6, 4))

    structures = ['Kinetic\nTrap', 'Native\nState', 'Alternative\nFold', 'Misfolded']
    energy = [4, 2, 3, 5]
    colors = ['#ff7f0e', '#2ca02c', '#1f77b4', '#d62728']

    bars = ax.bar(structures, energy, color=colors, edgecolor='white')
    ax.axhline(y=2, color='#2ca02c', linestyle='--', alpha=0.5)
    ax.text(3.5, 2.2, 'Global minimum', fontsize=9, color='#2ca02c')

    ax.set_ylabel('Free Energy (kcal/mol)', fontweight='bold')
    ax.set_title('B. Kinetic vs Thermodynamic Folding', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-rna-energy-landscape.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-rna-energy-landscape.svg")

# Fig 02 A-B: RNA Structure Elements
def create_fig_02():
    # Panel A: Secondary structure elements
    fig, ax = plt.subplots(figsize=(8, 5))

    elements = [
        ('Stem', 'Base-paired\nhelix', '#1f77b4'),
        ('Loop', 'Unpaired\nregion', '#2ca02c'),
        ('Bulge', 'Asymmetric\ngap', '#ff7f0e'),
        ('Junction', 'Multi-way\nbranch', '#9467bd'),
        ('Pseudoknot', 'Non-nested\npairing', '#d62728'),
    ]

    for i, (name, desc, color) in enumerate(elements):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.5 + 0.1, 0.3), 1.3, 1.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 1.5 + 0.75, 1.5, name, ha='center', va='center', fontsize=10,
                fontweight='bold', color='white')
        ax.text(i * 1.5 + 0.75, 0.8, desc, ha='center', va='center', fontsize=8,
                color='white')

    ax.set_xlim(-0.2, 7.8)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('A. RNA Secondary Structure Elements', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-A-fig-rna-structure-elements.svg', format='svg')
    plt.close()
    print("Saved: 02-A-fig-rna-structure-elements.svg")

    # Panel B: Tertiary interactions
    fig, ax = plt.subplots(figsize=(6, 4))

    interactions = ['Coaxial\nStacking', 'A-minor\nMotif', 'Ribose\nZipper', 'Tetraloop-\nReceptor']
    importance = [0.9, 0.85, 0.7, 0.8]
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']

    bars = ax.bar(interactions, importance, color=colors, edgecolor='white')
    ax.set_ylabel('Structural Importance', fontweight='bold')
    ax.set_title('B. Tertiary Structure Interactions', fontweight='bold', loc='left')
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-rna-structure-elements.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-rna-structure-elements.svg")

    # Panel C: Pseudoknot complexity
    fig, ax = plt.subplots(figsize=(6, 4))

    complexity = ['Simple\nHairpin', 'Nested\nLoops', 'Pseudoknot', 'Multi-way\nJunction']
    compute_time = [1, 10, 1000, 100]
    colors = ['#2ca02c', '#1f77b4', '#d62728', '#ff7f0e']

    bars = ax.bar(complexity, compute_time, color=colors, edgecolor='white')
    ax.set_ylabel('Relative Compute Time', fontweight='bold')
    ax.set_title('C. Pseudoknots Increase Complexity', fontweight='bold', loc='left')
    ax.set_yscale('log')
    ax.set_ylim(0.5, 5000)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-C-fig-rna-structure-elements.svg', format='svg')
    plt.close()
    print("Saved: 02-C-fig-rna-structure-elements.svg")

    # Panel D: Notation systems
    fig, ax = plt.subplots(figsize=(8, 4))

    notations = [
        ('Dot-bracket', '(((...)))', '#1f77b4'),
        ('CT Format', 'i  j  base', '#2ca02c'),
        ('BPSEQ', 'Base pairs list', '#ff7f0e'),
        ('Vienna', 'MFE structure', '#9467bd'),
    ]

    for i, (name, example, color) in enumerate(notations):
        ax.add_patch(mpatches.FancyBboxPatch((i * 2 + 0.1, 0.3), 1.8, 1.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 2 + 1, 1.3, name, ha='center', va='center', fontsize=10,
                fontweight='bold', color='white')
        ax.text(i * 2 + 1, 0.7, example, ha='center', va='center', fontsize=8,
                color='white', family='monospace')

    ax.set_xlim(-0.2, 8.2)
    ax.set_ylim(-0.1, 2.2)
    ax.axis('off')
    ax.set_title('D. Common Structure Notation Systems', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-D-fig-rna-structure-elements.svg', format='svg')
    plt.close()
    print("Saved: 02-D-fig-rna-structure-elements.svg")

# Fig 03 A-B: RNA PLM Gap
def create_fig_03():
    np.random.seed(42)

    # Panel A: Protein vs RNA data availability
    fig, ax = plt.subplots(figsize=(6, 4))

    categories = ['Sequences', 'Structures', 'Functional\nAnnotations', 'Experimental\nData']
    protein = [250, 200, 150, 100]  # in millions/thousands
    rna = [50, 5, 20, 10]

    x = np.arange(len(categories))
    width = 0.35

    ax.bar(x - width/2, protein, width, label='Protein', color='#2ca02c', edgecolor='white')
    ax.bar(x + width/2, rna, width, label='RNA', color='#1f77b4', edgecolor='white')

    ax.set_ylabel('Relative Data Availability', fontweight='bold')
    ax.set_title('A. Data Gap: Protein vs RNA', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_yscale('log')
    ax.set_ylim(1, 500)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-A-fig-rna-plm-gap.svg', format='svg')
    plt.close()
    print("Saved: 03-A-fig-rna-plm-gap.svg")

    # Panel B: Model performance comparison
    fig, ax = plt.subplots(figsize=(6, 4))

    tasks = ['Structure\nPrediction', 'Function\nAnnotation', 'Binding\nSite', 'Design']
    protein_perf = [0.92, 0.85, 0.88, 0.78]
    rna_perf = [0.75, 0.65, 0.70, 0.55]

    x = np.arange(len(tasks))
    width = 0.35

    ax.bar(x - width/2, protein_perf, width, label='Protein LM', color='#2ca02c', edgecolor='white')
    ax.bar(x + width/2, rna_perf, width, label='RNA LM', color='#1f77b4', edgecolor='white')

    ax.set_ylabel('Task Performance', fontweight='bold')
    ax.set_title('B. Performance Gap', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(tasks, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-rna-plm-gap.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-rna-plm-gap.svg")

    # Panel C: Emergent capabilities comparison
    fig, ax = plt.subplots(figsize=(6, 4))

    capabilities = ['Zero-shot\nTransfer', 'In-context\nLearning', 'Chain of\nThought', 'Tool\nUse']
    protein_cap = [0.85, 0.70, 0.60, 0.50]
    rna_cap = [0.40, 0.25, 0.15, 0.10]

    x = np.arange(len(capabilities))
    width = 0.35

    ax.bar(x - width/2, protein_cap, width, label='Protein LM', color='#2ca02c', edgecolor='white')
    ax.bar(x + width/2, rna_cap, width, label='RNA LM', color='#1f77b4', edgecolor='white')

    ax.set_ylabel('Capability Score', fontweight='bold')
    ax.set_title('C. Emergent Capabilities Comparison', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(capabilities, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-C-fig-rna-plm-gap.svg', format='svg')
    plt.close()
    print("Saved: 03-C-fig-rna-plm-gap.svg")

    # Panel D: Structural data challenge
    fig, ax = plt.subplots(figsize=(6, 4))

    data_types = ['High-res\nX-ray', 'Cryo-EM', 'NMR', 'Predicted']
    protein_count = [180000, 15000, 12000, 200000000]
    rna_count = [3000, 500, 1500, 5000000]

    x = np.arange(len(data_types))
    width = 0.35

    ax.bar(x - width/2, protein_count, width, label='Protein', color='#2ca02c', edgecolor='white')
    ax.bar(x + width/2, rna_count, width, label='RNA', color='#1f77b4', edgecolor='white')

    ax.set_ylabel('Number of Structures', fontweight='bold')
    ax.set_title('D. The Fundamental Structural Data Challenge', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(data_types, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_yscale('log')
    ax.set_ylim(100, 1e9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-D-fig-rna-plm-gap.svg', format='svg')
    plt.close()
    print("Saved: 03-D-fig-rna-plm-gap.svg")

# Fig 04 A-B: Codon Tokenization
def create_fig_04():
    # Panel A: Nucleotide vs codon tokenization
    fig, ax = plt.subplots(figsize=(8, 4))

    # Nucleotide level
    nts = ['A', 'U', 'G', 'C', 'A', 'U', 'G', 'G', 'C']
    for i, nt in enumerate(nts):
        color = {'A': '#2ca02c', 'U': '#d62728', 'G': '#ff7f0e', 'C': '#1f77b4'}[nt]
        ax.add_patch(mpatches.Rectangle((i * 0.6 + 0.5, 1.5), 0.5, 0.5, facecolor=color, edgecolor='white'))
        ax.text(i * 0.6 + 0.75, 1.75, nt, ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    ax.text(0.1, 1.75, 'Nucleotide:', ha='right', fontsize=10, fontweight='bold')

    # Codon level
    codons = ['AUG', 'CAU', 'GGC']
    codon_colors = ['#9467bd', '#17becf', '#bcbd22']
    for i, (codon, color) in enumerate(zip(codons, codon_colors)):
        ax.add_patch(mpatches.Rectangle((i * 1.8 + 0.5, 0.5), 1.6, 0.5, facecolor=color, edgecolor='white'))
        ax.text(i * 1.8 + 1.3, 0.75, codon, ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    ax.text(0.1, 0.75, 'Codon:', ha='right', fontsize=10, fontweight='bold')

    ax.set_xlim(-0.5, 7)
    ax.set_ylim(0, 2.5)
    ax.axis('off')
    ax.set_title('A. Nucleotide vs Codon Tokenization', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-A-fig-codon-tokenization.svg', format='svg')
    plt.close()
    print("Saved: 04-A-fig-codon-tokenization.svg")

    # Panel B: Vocabulary size comparison
    fig, ax = plt.subplots(figsize=(6, 4))

    strategies = ['Single-nt\n(4 tokens)', 'Codon\n(64 tokens)', 'BPE\n(~1000)', 'Hybrid']
    vocab_size = [4, 64, 1000, 128]
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']

    ax.bar(strategies, vocab_size, color=colors, edgecolor='white')
    ax.set_ylabel('Vocabulary Size', fontweight='bold')
    ax.set_title('B. Tokenization Strategy Comparison', fontweight='bold', loc='left')
    ax.set_yscale('log')
    ax.set_ylim(1, 3000)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-B-fig-codon-tokenization.svg', format='svg')
    plt.close()
    print("Saved: 04-B-fig-codon-tokenization.svg")

    # Panel C: Sequence length reduction
    fig, ax = plt.subplots(figsize=(6, 4))

    gene_lengths = ['Short\n(1 kb)', 'Medium\n(5 kb)', 'Long\n(10 kb)', 'Very Long\n(50 kb)']
    nt_tokens = [1000, 5000, 10000, 50000]
    codon_tokens = [333, 1667, 3333, 16667]

    x = np.arange(len(gene_lengths))
    width = 0.35

    ax.bar(x - width/2, nt_tokens, width, label='Nucleotide', color='#d62728', edgecolor='white')
    ax.bar(x + width/2, codon_tokens, width, label='Codon', color='#2ca02c', edgecolor='white')

    ax.set_ylabel('Token Count', fontweight='bold')
    ax.set_title('C. Codon Tokenization Reduces Sequence Length', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(gene_lengths, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_yscale('log')
    ax.set_ylim(100, 100000)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-C-fig-codon-tokenization.svg', format='svg')
    plt.close()
    print("Saved: 04-C-fig-codon-tokenization.svg")

    # Panel D: Information captured by model types
    fig, ax = plt.subplots(figsize=(6, 4))

    info_types = ['Sequence\npatterns', 'Codon\nbias', 'Splice\nsignals', 'Regulatory\nmotifs']
    nucleotide_model = [0.9, 0.5, 0.85, 0.8]
    codon_model = [0.7, 0.95, 0.6, 0.65]
    hybrid_model = [0.85, 0.90, 0.80, 0.75]

    x = np.arange(len(info_types))
    width = 0.25

    ax.bar(x - width, nucleotide_model, width, label='Nucleotide', color='#1f77b4', edgecolor='white')
    ax.bar(x, codon_model, width, label='Codon', color='#2ca02c', edgecolor='white')
    ax.bar(x + width, hybrid_model, width, label='Hybrid', color='#9467bd', edgecolor='white')

    ax.set_ylabel('Information Captured', fontweight='bold')
    ax.set_title('D. Different Models Capture Different Information', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(info_types, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-D-fig-codon-tokenization.svg', format='svg')
    plt.close()
    print("Saved: 04-D-fig-codon-tokenization.svg")

# Fig 05: mRNA Design Pipeline
def create_fig_05():
    dot = graphviz.Digraph('mrna_design', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='12,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('protein', 'Target\nProtein', fillcolor='#aec7e8', shape='box')
    dot.node('codon', 'Codon\nOptimization', fillcolor='#98df8a', shape='box')
    dot.node('utr', '5\'/3\' UTR\nDesign', fillcolor='#ffbb78', shape='box')
    dot.node('structure', 'Structure\nPrediction', fillcolor='#c5b0d5', shape='box')
    dot.node('stability', 'Stability\nOptimization', fillcolor='#ff9896', shape='box')
    dot.node('mrna', 'Optimized\nmRNA', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.edge('protein', 'codon', label='Back-translate')
    dot.edge('codon', 'utr', label='Add regulatory')
    dot.edge('utr', 'structure', label='Predict folding')
    dot.edge('structure', 'stability', label='Minimize MFE')
    dot.edge('stability', 'mrna')

    dot.render(OUTPUT_DIR / '05-fig-mrna-design-pipeline', cleanup=True)
    print("Saved: 05-fig-mrna-design-pipeline.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 18 figures generated.")

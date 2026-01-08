#!/usr/bin/env python3
"""
Chapter 22: Multi-Omics Integration Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_4" / "ch22"
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

# Fig 01 A-B: Integration Paradox
def create_fig_01():
    np.random.seed(42)

    # Panel A: More data doesn't always help
    fig, ax = plt.subplots(figsize=(6, 4))

    modalities = [1, 2, 3, 4, 5, 6]
    naive = 0.75 + 0.15 * np.log(modalities) + np.random.randn(6) * 0.02
    careful = 0.75 + 0.20 * np.log(modalities) - 0.05 * (np.array(modalities) > 4)

    ax.plot(modalities, naive, 'o-', color='#d62728', linewidth=2, markersize=8, label='Naive concatenation')
    ax.plot(modalities, careful, 's-', color='#2ca02c', linewidth=2, markersize=8, label='Careful integration')

    ax.fill_between([4, 6], [0.6, 0.6], [1, 1], alpha=0.1, color='#d62728')
    ax.text(5, 0.65, 'Curse of\ndimensionality', fontsize=9, ha='center', color='#d62728')

    ax.set_xlabel('Number of Modalities', fontweight='bold')
    ax.set_ylabel('Prediction Performance', fontweight='bold')
    ax.set_title('A. The Integration Paradox', fontweight='bold', loc='left')
    ax.legend(fontsize=9)
    ax.set_ylim(0.6, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-A-fig-integration-paradox.svg', format='svg')
    plt.close()
    print("Saved: 01-A-fig-integration-paradox.svg")

    # Panel B: Modality quality matters
    fig, ax = plt.subplots(figsize=(6, 4))

    scenarios = ['High-quality\nsingle', 'Mixed\nquality', 'Low-quality\nensemble', 'Curated\nmulti-omic']
    performance = [0.85, 0.80, 0.70, 0.92]
    colors = ['#1f77b4', '#ff7f0e', '#d62728', '#2ca02c']

    bars = ax.bar(scenarios, performance, color=colors, edgecolor='white')
    ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)

    ax.set_ylabel('Performance', fontweight='bold')
    ax.set_title('B. Quality vs Quantity', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-integration-paradox.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-integration-paradox.svg")

    # Panel C: When integration helps
    fig, ax = plt.subplots(figsize=(6, 4))

    scenarios = ['Fully\nOverlapping', 'Partially\nComplementary', 'Orthogonal\nInformation']
    single_mod = [0.85, 0.75, 0.65]
    integrated = [0.85, 0.88, 0.92]

    x = np.arange(len(scenarios))
    width = 0.35

    ax.bar(x - width/2, single_mod, width, label='Best Single', color='#aec7e8', edgecolor='white')
    ax.bar(x + width/2, integrated, width, label='Integrated', color='#2ca02c', edgecolor='white')

    # Highlight gain
    for i in range(len(scenarios)):
        gain = integrated[i] - single_mod[i]
        if gain > 0.01:
            ax.annotate(f'+{gain:.0%}', xy=(i + width/2, integrated[i] + 0.02),
                        ha='center', fontsize=9, color='#2ca02c', fontweight='bold')

    ax.set_ylabel('Performance', fontweight='bold')
    ax.set_title('C. When Integration Helps: Complementary Info', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-C-fig-integration-paradox.svg', format='svg')
    plt.close()
    print("Saved: 01-C-fig-integration-paradox.svg")

    # Panel D: When integration hurts
    fig, ax = plt.subplots(figsize=(6, 4))

    issues = ['Redundancy', 'Batch\nEffects', 'Missing\nData', 'Noise\nAmplification']
    performance_drop = [-0.05, -0.12, -0.08, -0.10]
    colors = ['#ff7f0e', '#d62728', '#ff7f0e', '#d62728']

    bars = ax.bar(issues, performance_drop, color=colors, edgecolor='white')
    ax.axhline(y=0, color='#555555', linewidth=1)

    ax.set_ylabel('Performance Change', fontweight='bold')
    ax.set_title('D. When Integration Hurts', fontweight='bold', loc='left')
    ax.set_ylim(-0.15, 0.02)

    for bar, drop in zip(bars, performance_drop):
        ax.text(bar.get_x() + bar.get_width()/2, drop - 0.01,
                f'{drop:.0%}', ha='center', fontsize=9, fontweight='bold', color='#d62728')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-D-fig-integration-paradox.svg', format='svg')
    plt.close()
    print("Saved: 01-D-fig-integration-paradox.svg")

# Fig 02 A-C: Fusion Strategies
def create_fig_02():
    strategies = [
        ('A', 'Early Fusion', 'Concatenate raw features'),
        ('B', 'Intermediate Fusion', 'Learn joint representations'),
        ('C', 'Late Fusion', 'Combine model predictions'),
    ]

    for panel_id, title, desc in strategies:
        dot = graphviz.Digraph(f'fusion_{panel_id}', format='svg')
        dot.attr(rankdir='LR', splines='polyline', size='8,3!', ratio='compress')
        dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

        if panel_id == 'A':
            dot.node('m1', 'RNA-seq', fillcolor='#1f77b4', fontcolor='white', shape='box')
            dot.node('m2', 'Methylation', fillcolor='#2ca02c', fontcolor='white', shape='box')
            dot.node('concat', 'Concatenate', fillcolor='#ffbb78', shape='box')
            dot.node('model', 'Single\nModel', fillcolor='#9467bd', fontcolor='white', shape='box')
            dot.node('out', 'Prediction', fillcolor='#98df8a', shape='box')
            dot.edge('m1', 'concat')
            dot.edge('m2', 'concat')
            dot.edge('concat', 'model')
            dot.edge('model', 'out')
        elif panel_id == 'B':
            dot.node('m1', 'RNA-seq', fillcolor='#1f77b4', fontcolor='white', shape='box')
            dot.node('m2', 'Methylation', fillcolor='#2ca02c', fontcolor='white', shape='box')
            dot.node('e1', 'Encoder 1', fillcolor='#aec7e8', shape='box')
            dot.node('e2', 'Encoder 2', fillcolor='#98df8a', shape='box')
            dot.node('fusion', 'Cross-modal\nAttention', fillcolor='#9467bd', fontcolor='white', shape='box')
            dot.node('out', 'Prediction', fillcolor='#98df8a', shape='box')
            dot.edge('m1', 'e1')
            dot.edge('m2', 'e2')
            dot.edge('e1', 'fusion')
            dot.edge('e2', 'fusion')
            dot.edge('fusion', 'out')
        else:
            dot.node('m1', 'RNA-seq', fillcolor='#1f77b4', fontcolor='white', shape='box')
            dot.node('m2', 'Methylation', fillcolor='#2ca02c', fontcolor='white', shape='box')
            dot.node('model1', 'Model 1', fillcolor='#aec7e8', shape='box')
            dot.node('model2', 'Model 2', fillcolor='#98df8a', shape='box')
            dot.node('p1', 'Pred 1', fillcolor='#c5b0d5', shape='box')
            dot.node('p2', 'Pred 2', fillcolor='#c5b0d5', shape='box')
            dot.node('combine', 'Ensemble', fillcolor='#9467bd', fontcolor='white', shape='box')
            dot.node('out', 'Final', fillcolor='#98df8a', shape='box')
            dot.edge('m1', 'model1')
            dot.edge('m2', 'model2')
            dot.edge('model1', 'p1')
            dot.edge('model2', 'p2')
            dot.edge('p1', 'combine')
            dot.edge('p2', 'combine')
            dot.edge('combine', 'out')

        dot.render(OUTPUT_DIR / f'02-{panel_id}-fig-fusion-strategies', cleanup=True)
        print(f"Saved: 02-{panel_id}-fig-fusion-strategies.svg")

# Fig 03 A-B: Intermediate Fusion
def create_fig_03():
    # Panel A: Cross-attention mechanism
    fig, ax = plt.subplots(figsize=(8, 5))

    # Draw attention matrix concept
    ax.add_patch(mpatches.FancyBboxPatch((0.5, 2), 2, 1, boxstyle='round,pad=0.02',
                                          facecolor='#1f77b4', alpha=0.7, edgecolor='white'))
    ax.text(1.5, 2.5, 'RNA\nEmbeddings', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    ax.add_patch(mpatches.FancyBboxPatch((4.5, 2), 2, 1, boxstyle='round,pad=0.02',
                                          facecolor='#2ca02c', alpha=0.7, edgecolor='white'))
    ax.text(5.5, 2.5, 'Protein\nEmbeddings', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    ax.add_patch(mpatches.Rectangle((2.5, 0.5), 2, 1.2, facecolor='#9467bd', alpha=0.7, edgecolor='white'))
    ax.text(3.5, 1.1, 'Cross-\nAttention', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    ax.annotate('', xy=(2.5, 1.1), xytext=(2.5, 2), arrowprops=dict(arrowstyle='->', color='#555555', lw=2))
    ax.annotate('', xy=(4.5, 1.1), xytext=(4.5, 2), arrowprops=dict(arrowstyle='->', color='#555555', lw=2))

    ax.set_xlim(0, 7)
    ax.set_ylim(0, 3.5)
    ax.axis('off')
    ax.set_title('A. Cross-Attention for Multi-Modal Fusion', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-A-fig-intermediate-fusion.svg', format='svg')
    plt.close()
    print("Saved: 03-A-fig-intermediate-fusion.svg")

    # Panel B: Learned joint representation
    fig, ax = plt.subplots(figsize=(6, 5))
    np.random.seed(42)

    # Before fusion
    rna = np.random.randn(30, 2) + [-2, 0]
    protein = np.random.randn(30, 2) + [2, 0]

    ax.scatter(rna[:, 0], rna[:, 1], c='#1f77b4', s=40, alpha=0.4, label='RNA (before)')
    ax.scatter(protein[:, 0], protein[:, 1], c='#2ca02c', s=40, alpha=0.4, label='Protein (before)')

    # After fusion (aligned)
    rna_aligned = rna + [2, 0]
    protein_aligned = protein - [2, 0]
    ax.scatter(rna_aligned[:, 0], rna_aligned[:, 1], c='#1f77b4', s=40, alpha=0.8, marker='s', label='RNA (after)')
    ax.scatter(protein_aligned[:, 0], protein_aligned[:, 1], c='#2ca02c', s=40, alpha=0.8, marker='s', label='Protein (after)')

    ax.legend(fontsize=8)
    ax.set_xlabel('Dimension 1', fontweight='bold')
    ax.set_ylabel('Dimension 2', fontweight='bold')
    ax.set_title('B. Learned Joint Embedding Space', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-intermediate-fusion.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-intermediate-fusion.svg")

    # Panel C: Downstream task heads
    dot = graphviz.Digraph('task_heads', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('shared', 'Shared\nRepresentation', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('classify', 'Classification\nHead', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('regress', 'Regression\nHead', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('survival', 'Survival\nHead', fillcolor='#ff7f0e', shape='box')

    dot.node('label', 'Disease\nType', fillcolor='#aec7e8', shape='ellipse')
    dot.node('score', 'Risk\nScore', fillcolor='#98df8a', shape='ellipse')
    dot.node('time', 'Survival\nTime', fillcolor='#ffbb78', shape='ellipse')

    dot.edge('shared', 'classify')
    dot.edge('shared', 'regress')
    dot.edge('shared', 'survival')
    dot.edge('classify', 'label')
    dot.edge('regress', 'score')
    dot.edge('survival', 'time')

    dot.render(OUTPUT_DIR / '03-C-fig-intermediate-fusion', cleanup=True)
    print("Saved: 03-C-fig-intermediate-fusion.svg")

    # Panel D: Missing modalities handling
    fig, ax = plt.subplots(figsize=(6, 4))

    scenarios = ['All\nModalities', 'Missing\nRNA', 'Missing\nMethyl', 'Missing\nBoth']
    performance = [0.92, 0.85, 0.88, 0.78]
    colors = ['#2ca02c', '#ff7f0e', '#ff7f0e', '#d62728']

    bars = ax.bar(scenarios, performance, color=colors, edgecolor='white')
    ax.axhline(y=0.92, color='#2ca02c', linestyle='--', alpha=0.5)

    for bar, perf in zip(bars, performance):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{perf:.0%}', ha='center', fontsize=9, fontweight='bold')

    ax.set_ylabel('Performance', fontweight='bold')
    ax.set_title('D. Graceful Degradation with Missing Modalities', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-D-fig-intermediate-fusion.svg', format='svg')
    plt.close()
    print("Saved: 03-D-fig-intermediate-fusion.svg")

# Fig 04 A-B: Clinical Multi-Modal
def create_fig_04():
    # Panel A: Clinical data types
    fig, ax = plt.subplots(figsize=(8, 5))

    modalities = [
        ('Genomics', 'WGS/WES', '#1f77b4'),
        ('Transcriptomics', 'RNA-seq', '#2ca02c'),
        ('Imaging', 'Histology', '#ff7f0e'),
        ('Clinical', 'EHR', '#9467bd'),
        ('Proteomics', 'Mass Spec', '#d62728'),
    ]

    for i, (name, source, color) in enumerate(modalities):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.5 + 0.1, 0.3), 1.3, 1.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 1.5 + 0.75, 1.5, name, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')
        ax.text(i * 1.5 + 0.75, 0.8, source, ha='center', va='center', fontsize=8,
                color='white')

    ax.set_xlim(-0.2, 7.8)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('A. Clinical Multi-Modal Data Types', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-A-fig-clinical-multimodal.svg', format='svg')
    plt.close()
    print("Saved: 04-A-fig-clinical-multimodal.svg")

    # Panel B: Performance by modality combination
    fig, ax = plt.subplots(figsize=(6, 4))

    combinations = ['Genomics\nOnly', 'Genomics +\nClinical', 'Genomics +\nImaging', 'All\nModalities']
    performance = [0.72, 0.82, 0.85, 0.91]
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']

    bars = ax.bar(combinations, performance, color=colors, edgecolor='white')
    ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)

    for bar, perf in zip(bars, performance):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{perf:.0%}', ha='center', fontsize=9, fontweight='bold')

    ax.set_ylabel('auROC', fontweight='bold')
    ax.set_title('B. Incremental Value of Modalities', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-B-fig-clinical-multimodal.svg', format='svg')
    plt.close()
    print("Saved: 04-B-fig-clinical-multimodal.svg")

    # Panel C: Patient representation space
    fig, ax = plt.subplots(figsize=(6, 5))
    np.random.seed(42)

    # Different patient groups in unified space
    n_patients = 25
    groups = ['Responders', 'Non-responders', 'Intermediate']
    colors = ['#2ca02c', '#d62728', '#ff7f0e']
    centers = [(1, 1), (-1, -1), (0, 0)]

    for group, color, center in zip(groups, colors, centers):
        x = np.random.randn(n_patients) * 0.5 + center[0]
        y = np.random.randn(n_patients) * 0.5 + center[1]
        ax.scatter(x, y, c=color, s=50, label=group, alpha=0.7, edgecolors='white')

    ax.legend(fontsize=9, title='Treatment Response')
    ax.set_xlabel('Unified Dimension 1', fontweight='bold')
    ax.set_ylabel('Unified Dimension 2', fontweight='bold')
    ax.set_title('C. Patient Space Unifies All Modalities', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-C-fig-clinical-multimodal.svg', format='svg')
    plt.close()
    print("Saved: 04-C-fig-clinical-multimodal.svg")

    # Panel D: Clinical prediction with missing modalities
    fig, ax = plt.subplots(figsize=(7, 4))

    tasks = ['Diagnosis', 'Prognosis', 'Treatment\nResponse', 'Survival']
    full_data = [0.92, 0.85, 0.80, 0.78]
    missing_handling = [0.88, 0.82, 0.75, 0.72]

    x = np.arange(len(tasks))
    width = 0.35

    ax.bar(x - width/2, full_data, width, label='Full Data', color='#2ca02c', edgecolor='white')
    ax.bar(x + width/2, missing_handling, width, label='30% Missing', color='#ff7f0e', edgecolor='white')

    ax.set_ylabel('auROC', fontweight='bold')
    ax.set_title('D. Clinical Prediction with Missing Modality Handling', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(tasks, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-D-fig-clinical-multimodal.svg', format='svg')
    plt.close()
    print("Saved: 04-D-fig-clinical-multimodal.svg")

# Fig 05 A-B: Information Cascade
def create_fig_05():
    # Panel A: Central dogma cascade
    dot = graphviz.Digraph('cascade', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='12,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('dna', 'DNA\n(Genome)', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('rna', 'RNA\n(Transcriptome)', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('protein', 'Protein\n(Proteome)', fillcolor='#ff7f0e', shape='box')
    dot.node('phenotype', 'Phenotype', fillcolor='#d62728', fontcolor='white', shape='box')

    dot.edge('dna', 'rna', label='Transcription')
    dot.edge('rna', 'protein', label='Translation')
    dot.edge('protein', 'phenotype', label='Function')

    # Regulatory feedback
    dot.edge('protein', 'dna', style='dashed', label='Regulation', constraint='false')

    dot.render(OUTPUT_DIR / '05-A-fig-information-cascade', cleanup=True)
    print("Saved: 05-A-fig-information-cascade.svg")

    # Panel B: Causal vs correlative
    fig, ax = plt.subplots(figsize=(6, 4))
    np.random.seed(42)

    # Causal path strength
    levels = ['DNA → RNA', 'RNA → Protein', 'Protein → Phenotype']
    causal = [0.85, 0.70, 0.55]
    correlative = [0.90, 0.85, 0.80]

    x = np.arange(len(levels))
    width = 0.35

    ax.bar(x - width/2, causal, width, label='Causal', color='#2ca02c', edgecolor='white')
    ax.bar(x + width/2, correlative, width, label='Correlative', color='#ff7f0e', edgecolor='white')

    ax.set_ylabel('Predictive Power', fontweight='bold')
    ax.set_title('B. Causal vs Correlative Relationships', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(levels, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-B-fig-information-cascade.svg', format='svg')
    plt.close()
    print("Saved: 05-B-fig-information-cascade.svg")

    # Panel C: Bottleneck modalities by variant type
    fig, ax = plt.subplots(figsize=(7, 4))

    variant_types = ['Coding\nSNV', 'Regulatory\nSNV', 'CNV', 'Structural\nVariant']
    genomics = [0.9, 0.6, 0.7, 0.8]
    transcriptomics = [0.5, 0.9, 0.8, 0.6]
    proteomics = [0.7, 0.5, 0.6, 0.5]

    x = np.arange(len(variant_types))
    width = 0.25

    ax.bar(x - width, genomics, width, label='Genomics', color='#1f77b4', edgecolor='white')
    ax.bar(x, transcriptomics, width, label='Transcriptomics', color='#2ca02c', edgecolor='white')
    ax.bar(x + width, proteomics, width, label='Proteomics', color='#ff7f0e', edgecolor='white')

    # Highlight bottleneck for each variant type
    bottlenecks = [('Genomics', 0), ('Transcriptomics', 1), ('Transcriptomics', 2), ('Genomics', 3)]
    for name, idx in bottlenecks:
        offset = -width if name == 'Genomics' else (0 if name == 'Transcriptomics' else width)
        val = genomics[idx] if name == 'Genomics' else (transcriptomics[idx] if name == 'Transcriptomics' else proteomics[idx])
        ax.scatter(idx + offset, val + 0.05, marker='*', s=100, c='#d62728', zorder=5)

    ax.set_ylabel('Information Content', fontweight='bold')
    ax.set_title('C. Bottleneck Modality Varies by Variant Type', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(variant_types, fontsize=9)
    ax.legend(fontsize=8)
    ax.set_ylim(0, 1.1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-C-fig-information-cascade.svg', format='svg')
    plt.close()
    print("Saved: 05-C-fig-information-cascade.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 22 figures generated.")

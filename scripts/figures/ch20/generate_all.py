#!/usr/bin/env python3
"""
Chapter 20: 3D Genome Models Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_4" / "ch20"
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

# Fig 01 A-B: TAD Disruption
def create_fig_01():
    np.random.seed(42)

    # Panel A: Normal TAD structure
    fig, ax = plt.subplots(figsize=(6, 5))

    # Create contact map
    n = 50
    contact = np.zeros((n, n))
    # TAD 1
    for i in range(20):
        for j in range(20):
            contact[i, j] = np.exp(-abs(i-j) / 5)
    # TAD 2
    for i in range(20, 50):
        for j in range(20, 50):
            contact[i, j] = np.exp(-abs(i-j) / 5)

    im = ax.imshow(contact, cmap='Reds', aspect='equal')
    ax.axvline(x=20, color='#1f77b4', linestyle='--', linewidth=2)
    ax.axhline(y=20, color='#1f77b4', linestyle='--', linewidth=2)
    ax.text(10, -3, 'TAD 1', ha='center', fontsize=10, fontweight='bold')
    ax.text(35, -3, 'TAD 2', ha='center', fontsize=10, fontweight='bold')

    ax.set_xlabel('Genomic Position', fontweight='bold')
    ax.set_ylabel('Genomic Position', fontweight='bold')
    ax.set_title('A. Normal TAD Structure', fontweight='bold', loc='left')
    plt.colorbar(im, ax=ax, label='Contact Frequency')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-A-fig-tad-disruption.svg', format='svg')
    plt.close()
    print("Saved: 01-A-fig-tad-disruption.svg")

    # Panel B: Disrupted TAD
    fig, ax = plt.subplots(figsize=(6, 5))

    # Disrupted contact map (boundary deleted)
    contact_disrupted = np.zeros((n, n))
    for i in range(50):
        for j in range(50):
            contact_disrupted[i, j] = np.exp(-abs(i-j) / 8)

    im = ax.imshow(contact_disrupted, cmap='Reds', aspect='equal')
    ax.scatter([20], [20], s=200, c='yellow', marker='*', zorder=5, edgecolors='black')
    ax.text(25, 15, 'Boundary\ndeletion', fontsize=9, color='#d62728', fontweight='bold')

    ax.set_xlabel('Genomic Position', fontweight='bold')
    ax.set_ylabel('Genomic Position', fontweight='bold')
    ax.set_title('B. Disrupted TAD (Boundary Deletion)', fontweight='bold', loc='left')
    plt.colorbar(im, ax=ax, label='Contact Frequency')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-tad-disruption.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-tad-disruption.svg")

    # Panel C: Ectopic WNT6 activation
    fig, ax = plt.subplots(figsize=(8, 4))

    # Diagram showing enhancer hijacking
    ax.add_patch(mpatches.FancyBboxPatch((0.5, 1.5), 1.5, 0.8, boxstyle='round,pad=0.02',
                                          facecolor='#1f77b4', alpha=0.7, edgecolor='white'))
    ax.text(1.25, 1.9, 'Enhancer', ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    ax.add_patch(mpatches.FancyBboxPatch((3, 1.5), 1, 0.8, boxstyle='round,pad=0.02',
                                          facecolor='#d62728', alpha=0.7, edgecolor='white'))
    ax.text(3.5, 1.9, 'WNT6', ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    ax.add_patch(mpatches.FancyBboxPatch((5, 1.5), 1.5, 0.8, boxstyle='round,pad=0.02',
                                          facecolor='#555555', alpha=0.5, edgecolor='white'))
    ax.text(5.75, 1.9, 'TAD\nBoundary', ha='center', va='center', fontsize=8, color='white')

    ax.annotate('', xy=(3, 1.9), xytext=(2, 1.9),
                arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=3))
    ax.text(2.5, 2.4, 'Ectopic\nactivation', ha='center', fontsize=9, color='#ff7f0e', fontweight='bold')

    ax.text(4, 0.8, 'Brachydactyly\nphenotype', ha='center', fontsize=10, color='#d62728', fontweight='bold')

    ax.set_xlim(0, 7)
    ax.set_ylim(0.3, 2.8)
    ax.axis('off')
    ax.set_title('C. Ectopic WNT6 Activation Causes Brachydactyly', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-C-fig-tad-disruption.svg', format='svg')
    plt.close()
    print("Saved: 01-C-fig-tad-disruption.svg")

    # Panel D: Same-sized deletions, different outcomes
    fig, ax = plt.subplots(figsize=(6, 4))

    deletion_types = ['Intra-TAD\n(benign)', 'Boundary-\ncrossing', 'Multi-TAD\n(severe)']
    severity = [0.2, 0.7, 0.95]
    colors = ['#2ca02c', '#ff7f0e', '#d62728']

    bars = ax.bar(deletion_types, severity, color=colors, edgecolor='white')
    ax.set_ylabel('Pathogenicity Score', fontweight='bold')
    ax.set_title('D. Same-Sized Deletions, Different Outcomes', fontweight='bold', loc='left')
    ax.set_ylim(0, 1)

    for bar, sev in zip(bars, severity):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
                f'{sev:.0%}', ha='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-D-fig-tad-disruption.svg', format='svg')
    plt.close()
    print("Saved: 01-D-fig-tad-disruption.svg")

# Fig 02 A-B: Chromatin Hierarchy
def create_fig_02():
    # Panel A: Hierarchical organization
    dot = graphviz.Digraph('hierarchy', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('chromosome', 'Chromosome\n(~100 Mb)', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('compartment', 'A/B Compartments\n(~10 Mb)', fillcolor='#ff7f0e', shape='box')
    dot.node('tad', 'TADs\n(~1 Mb)', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('loop', 'Loops\n(~100 kb)', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('nucleosome', 'Nucleosomes\n(~200 bp)', fillcolor='#9467bd', fontcolor='white', shape='box')

    dot.edge('chromosome', 'compartment')
    dot.edge('compartment', 'tad')
    dot.edge('tad', 'loop')
    dot.edge('loop', 'nucleosome')

    dot.render(OUTPUT_DIR / '02-A-fig-chromatin-hierarchy', cleanup=True)
    print("Saved: 02-A-fig-chromatin-hierarchy.svg")

    # Panel B: Scale comparison
    fig, ax = plt.subplots(figsize=(6, 4))

    levels = ['Nucleosomes', 'Loops', 'TADs', 'Compartments', 'Chromosomes']
    sizes = [0.2, 100, 1000, 10000, 100000]  # in kb
    colors = ['#9467bd', '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']

    ax.barh(levels, sizes, color=colors, edgecolor='white')
    ax.set_xlabel('Scale (kb)', fontweight='bold')
    ax.set_title('B. Chromatin Organization Scales', fontweight='bold', loc='left')
    ax.set_xscale('log')
    ax.set_xlim(0.1, 200000)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-chromatin-hierarchy.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-chromatin-hierarchy.svg")

    # Panel C: TADs as triangular domains
    fig, ax = plt.subplots(figsize=(6, 5))

    # Create triangular TAD visualization
    n = 40
    contact = np.zeros((n, n))
    # TAD 1 (triangle)
    for i in range(15):
        for j in range(15):
            if j >= i:
                contact[i, j] = np.exp(-abs(i-j) / 3) * 0.8
    # TAD 2 (triangle)
    for i in range(15, 40):
        for j in range(15, 40):
            if j >= i:
                contact[i, j] = np.exp(-abs(i-j) / 4) * 0.8

    # Mirror to make symmetric
    contact = contact + contact.T - np.diag(np.diag(contact))

    im = ax.imshow(contact, cmap='Reds', aspect='equal')
    ax.plot([0, 15], [15, 15], 'b--', linewidth=2)
    ax.plot([15, 15], [0, 15], 'b--', linewidth=2)
    ax.text(7, 5, 'TAD', ha='center', fontsize=11, fontweight='bold', color='#1f77b4')

    ax.set_xlabel('Genomic Position', fontweight='bold')
    ax.set_ylabel('Genomic Position', fontweight='bold')
    ax.set_title('C. TADs Appear as Triangular Domains', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-C-fig-chromatin-hierarchy.svg', format='svg')
    plt.close()
    print("Saved: 02-C-fig-chromatin-hierarchy.svg")

    # Panel D: Chromatin loops connect enhancers to promoters
    fig, ax = plt.subplots(figsize=(8, 4))

    # DNA line
    ax.plot([0, 8], [1, 1], color='#555555', linewidth=4, zorder=1)

    # Enhancer
    ax.add_patch(mpatches.FancyBboxPatch((1, 0.7), 1, 0.6, boxstyle='round,pad=0.02',
                                          facecolor='#ff7f0e', alpha=0.8, edgecolor='white'))
    ax.text(1.5, 1, 'E', ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Promoter
    ax.add_patch(mpatches.FancyBboxPatch((5.5, 0.7), 1, 0.6, boxstyle='round,pad=0.02',
                                          facecolor='#2ca02c', alpha=0.8, edgecolor='white'))
    ax.text(6, 1, 'P', ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Gene
    ax.annotate('', xy=(7.5, 1), xytext=(6.5, 1),
                arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=2))
    ax.text(7.8, 1, 'Gene', ha='left', fontsize=10, fontweight='bold')

    # Loop
    theta = np.linspace(0, np.pi, 50)
    loop_x = 1.5 + 2.25 * np.cos(theta)
    loop_y = 1 + 1.2 * np.sin(theta)
    ax.plot(loop_x + 2.25, loop_y, color='#9467bd', linewidth=2, linestyle='--')
    ax.text(3.75, 2.4, 'Chromatin Loop', ha='center', fontsize=10, color='#9467bd', fontweight='bold')

    ax.set_xlim(-0.5, 9)
    ax.set_ylim(0.2, 2.8)
    ax.axis('off')
    ax.set_title('D. Loops Connect Enhancers to Promoters', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-D-fig-chromatin-hierarchy.svg', format='svg')
    plt.close()
    print("Saved: 02-D-fig-chromatin-hierarchy.svg")

# Fig 03 A-B: Loop Extrusion
def create_fig_03():
    # Panel A: Loop extrusion mechanism
    fig, ax = plt.subplots(figsize=(8, 5))

    # DNA strand
    ax.plot([1, 9], [2, 2], color='#555555', linewidth=4, zorder=1)

    # CTCF sites
    ax.scatter([2], [2], s=200, c='#d62728', marker='>', zorder=5, label='CTCF')
    ax.scatter([8], [2], s=200, c='#d62728', marker='<', zorder=5)

    # Cohesin ring
    theta = np.linspace(0, 2*np.pi, 100)
    r = 0.8
    ax.plot(5 + r*np.cos(theta), 3 + r*np.sin(theta), color='#2ca02c', linewidth=3)
    ax.text(5, 3, 'Cohesin', ha='center', va='center', fontsize=9, fontweight='bold')

    # Loop visualization
    loop_x = np.linspace(2, 8, 100)
    loop_y = 2 + 1.5 * np.sin((loop_x - 2) * np.pi / 6)
    ax.plot(loop_x, loop_y, color='#1f77b4', linewidth=2, linestyle='--', alpha=0.7)

    ax.text(2, 1.3, 'CTCF', ha='center', fontsize=9, color='#d62728')
    ax.text(8, 1.3, 'CTCF', ha='center', fontsize=9, color='#d62728')

    ax.set_xlim(0, 10)
    ax.set_ylim(0.5, 4.5)
    ax.axis('off')
    ax.set_title('A. Loop Extrusion Mechanism', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-A-fig-loop-extrusion.svg', format='svg')
    plt.close()
    print("Saved: 03-A-fig-loop-extrusion.svg")

    # Panel B: CTCF motif orientation
    fig, ax = plt.subplots(figsize=(6, 4))

    orientations = ['Convergent\n(►◄)', 'Tandem\n(►►)', 'Divergent\n(◄►)']
    loop_strength = [1.0, 0.3, 0.1]
    colors = ['#2ca02c', '#ff7f0e', '#d62728']

    bars = ax.bar(orientations, loop_strength, color=colors, edgecolor='white')
    ax.set_ylabel('Loop Strength', fontweight='bold')
    ax.set_title('B. CTCF Orientation and Loop Formation', fontweight='bold', loc='left')
    ax.set_ylim(0, 1.2)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-loop-extrusion.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-loop-extrusion.svg")

    # Panel C: Convergent CTCF sites halt extrusion
    fig, ax = plt.subplots(figsize=(8, 5))

    # DNA line
    ax.plot([1, 9], [2, 2], color='#555555', linewidth=6, zorder=1)

    # CTCF sites with motif direction
    ax.scatter([2.5], [2], s=300, c='#d62728', marker='>', zorder=5)
    ax.scatter([7.5], [2], s=300, c='#d62728', marker='<', zorder=5)

    # Cohesin approaching CTCF
    ax.add_patch(mpatches.Circle((4, 2), 0.4, facecolor='#2ca02c', edgecolor='white', linewidth=2))
    ax.text(4, 2, 'C', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    ax.annotate('', xy=(3, 2), xytext=(4.5, 2),
                arrowprops=dict(arrowstyle='<-', color='#2ca02c', lw=2))

    ax.add_patch(mpatches.Circle((6, 2), 0.4, facecolor='#2ca02c', edgecolor='white', linewidth=2))
    ax.text(6, 2, 'C', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    ax.annotate('', xy=(5.5, 2), xytext=(7, 2),
                arrowprops=dict(arrowstyle='->', color='#2ca02c', lw=2))

    # STOP indicators
    ax.text(2.5, 1.3, 'STOP', ha='center', fontsize=9, color='#d62728', fontweight='bold')
    ax.text(7.5, 1.3, 'STOP', ha='center', fontsize=9, color='#d62728', fontweight='bold')

    ax.set_xlim(0, 10)
    ax.set_ylim(0.8, 3)
    ax.axis('off')
    ax.set_title('C. Convergent CTCF Sites Halt Extrusion', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-C-fig-loop-extrusion.svg', format='svg')
    plt.close()
    print("Saved: 03-C-fig-loop-extrusion.svg")

    # Panel D: Convergent pairs form stable loops
    fig, ax = plt.subplots(figsize=(6, 5))

    orientations = ['► ◄\n(Convergent)', '► ►\n(Tandem)', '◄ ►\n(Divergent)', '◄ ◄\n(Tandem)']
    loop_stability = [100, 15, 5, 12]
    colors = ['#2ca02c', '#ff7f0e', '#d62728', '#ff7f0e']

    bars = ax.bar(orientations, loop_stability, color=colors, edgecolor='white')
    ax.set_ylabel('Loop Formation Frequency', fontweight='bold')
    ax.set_title('D. Only Convergent Pairs Form Stable Loops', fontweight='bold', loc='left')

    ax.axhline(y=100, color='#2ca02c', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-D-fig-loop-extrusion.svg', format='svg')
    plt.close()
    print("Saved: 03-D-fig-loop-extrusion.svg")

# Fig 04 A-B: 3D Genome Models
def create_fig_04():
    # Panel A: Model types
    fig, ax = plt.subplots(figsize=(8, 5))

    models = [
        ('Hi-C\nPrediction', 'Akita, Orca', '#1f77b4'),
        ('Contact\nReconstruction', 'DeepC', '#2ca02c'),
        ('Loop\nCalling', 'Peakachu', '#ff7f0e'),
        ('TAD\nBoundary', 'TADbreak', '#9467bd'),
        ('3D Structure', 'PHi-C2', '#d62728'),
    ]

    for i, (task, model, color) in enumerate(models):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.5 + 0.1, 0.3), 1.3, 1.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 1.5 + 0.75, 1.5, task, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')
        ax.text(i * 1.5 + 0.75, 0.8, model, ha='center', va='center', fontsize=8,
                color='white')

    ax.set_xlim(-0.2, 7.8)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('A. 3D Genome Model Types', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-A-fig-3d-models.svg', format='svg')
    plt.close()
    print("Saved: 04-A-fig-3d-models.svg")

    # Panel B: Sequence-to-structure
    dot = graphviz.Digraph('seq2struct', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('seq', 'DNA\nSequence', fillcolor='#aec7e8', shape='box')
    dot.node('model', 'Akita /\nOrca', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('contact', 'Predicted\nHi-C Map', fillcolor='#ffbb78', shape='box')
    dot.node('variant', 'Variant\nEffect', fillcolor='#98df8a', shape='box')

    dot.edge('seq', 'model')
    dot.edge('model', 'contact')
    dot.edge('contact', 'variant', label='In silico\nmutagenesis')

    dot.render(OUTPUT_DIR / '04-B-fig-3d-models', cleanup=True)
    print("Saved: 04-B-fig-3d-models.svg")

    # Panel C: C.Origami architecture
    dot = graphviz.Digraph('corigami', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('seq', 'DNA\nSequence', fillcolor='#aec7e8', shape='box')
    dot.node('ctcf', 'CTCF\nBinding', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('encode', 'Joint\nEncoder', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('transfer', 'Cell-Type\nTransfer', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('predict', 'Hi-C\nPrediction', fillcolor='#98df8a', shape='box')

    dot.edge('seq', 'encode')
    dot.edge('ctcf', 'encode', label='Cell-specific')
    dot.edge('encode', 'transfer')
    dot.edge('transfer', 'predict')

    dot.render(OUTPUT_DIR / '04-C-fig-3d-models', cleanup=True)
    print("Saved: 04-C-fig-3d-models.svg")

    # Panel D: Predictions capture TAD boundaries and loops
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Predicted
    n = 30
    pred = np.zeros((n, n))
    for i in range(12):
        for j in range(12):
            pred[i, j] = np.exp(-abs(i-j) / 3)
    for i in range(12, 30):
        for j in range(12, 30):
            pred[i, j] = np.exp(-abs(i-j) / 4)
    pred[5, 25] = 0.8  # Loop
    pred[25, 5] = 0.8

    im1 = axes[0].imshow(pred, cmap='Reds', aspect='equal')
    axes[0].axvline(x=12, color='#1f77b4', linestyle='--', linewidth=2)
    axes[0].axhline(y=12, color='#1f77b4', linestyle='--', linewidth=2)
    axes[0].scatter([5], [25], s=100, c='yellow', marker='*', edgecolors='black', zorder=5)
    axes[0].set_title('Predicted', fontweight='bold')
    axes[0].set_xlabel('Genomic Position')
    axes[0].set_ylabel('Genomic Position')

    # Observed (similar but with noise)
    obs = pred + np.random.randn(n, n) * 0.1
    obs = np.clip(obs, 0, 1)
    im2 = axes[1].imshow(obs, cmap='Reds', aspect='equal')
    axes[1].axvline(x=12, color='#1f77b4', linestyle='--', linewidth=2)
    axes[1].axhline(y=12, color='#1f77b4', linestyle='--', linewidth=2)
    axes[1].scatter([5], [25], s=100, c='yellow', marker='*', edgecolors='black', zorder=5)
    axes[1].set_title('Observed', fontweight='bold')
    axes[1].set_xlabel('Genomic Position')

    plt.suptitle('D. Predictions Capture TAD Boundaries and Loops', fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-D-fig-3d-models.svg', format='svg')
    plt.close()
    print("Saved: 04-D-fig-3d-models.svg")

# Fig 05 A-B: Spatial Transcriptomics
def create_fig_05():
    np.random.seed(42)

    # Panel A: Spatial gene expression
    fig, ax = plt.subplots(figsize=(6, 5))

    n_spots = 100
    x = np.random.rand(n_spots) * 10
    y = np.random.rand(n_spots) * 10
    expression = np.exp(-((x - 5)**2 + (y - 5)**2) / 10)

    scatter = ax.scatter(x, y, c=expression, cmap='viridis', s=60, edgecolors='white')
    plt.colorbar(scatter, ax=ax, label='Gene Expression')

    ax.set_xlabel('X Position', fontweight='bold')
    ax.set_ylabel('Y Position', fontweight='bold')
    ax.set_title('A. Spatial Gene Expression', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-A-fig-spatial-transcriptomics.svg', format='svg')
    plt.close()
    print("Saved: 05-A-fig-spatial-transcriptomics.svg")

    # Panel B: Integration workflow
    dot = graphviz.Digraph('spatial', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('spatial', 'Spatial\nTranscriptomics', fillcolor='#aec7e8', shape='box')
    dot.node('hic', 'Hi-C\nData', fillcolor='#98df8a', shape='box')
    dot.node('integrate', 'Multi-modal\nIntegration', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('insight', 'Structure-\nFunction Link', fillcolor='#ff7f0e', shape='box')

    dot.edge('spatial', 'integrate')
    dot.edge('hic', 'integrate')
    dot.edge('integrate', 'insight')

    dot.render(OUTPUT_DIR / '05-B-fig-spatial-transcriptomics', cleanup=True)
    print("Saved: 05-B-fig-spatial-transcriptomics.svg")

    # Panel C: Deconvolution infers cell type composition
    fig, ax = plt.subplots(figsize=(6, 4))

    cell_types = ['Tumor', 'T cells', 'Macrophages', 'Fibroblasts', 'Endothelial']
    proportions = [0.45, 0.20, 0.15, 0.12, 0.08]
    colors = ['#d62728', '#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']

    wedges, texts, autotexts = ax.pie(proportions, labels=cell_types, colors=colors,
                                        autopct='%1.0f%%', startangle=90,
                                        wedgeprops=dict(edgecolor='white', linewidth=2))

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)

    ax.set_title('C. Deconvolution Infers Cell Type Composition', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-C-fig-spatial-transcriptomics.svg', format='svg')
    plt.close()
    print("Saved: 05-C-fig-spatial-transcriptomics.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 20 figures generated.")

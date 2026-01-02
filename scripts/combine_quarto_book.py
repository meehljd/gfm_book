#!/usr/bin/env python3
"""
Combine a Quarto book's .qmd/.md files into one big .qmd (or .md) in the order
listed in _quarto.yml (book.chapters, then book.appendices if present).

Usage:
  python combine_quarto_book.py combined.qmd
  python combine_quarto_book.py combined.qmd --root /path/to/book
  
  (Optional) Render that single file to Markdown
  quarto render combined.qmd --to gfm --output combined.md
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

try:
    import yaml  # pip install pyyaml
except ImportError as e:
    raise SystemExit("Missing dependency: pyyaml. Install with: pip install pyyaml") from e


FRONT_MATTER_RE = re.compile(r"(?s)\A---\s*\n.*?\n---\s*\n")


def flatten_manifest(node):
    """Yield file paths from Quarto manifest nodes (strings/lists/dicts)."""
    if node is None:
        return
    if isinstance(node, str):
        yield node
        return
    if isinstance(node, list):
        for item in node:
            yield from flatten_manifest(item)
        return
    if isinstance(node, dict):
        # Common Quarto patterns: {part: "...", chapters:[...]}, {chapters:[...]}
        for key in ("chapters", "appendices", "articles"):
            if key in node:
                yield from flatten_manifest(node[key])
        return


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output", nargs="?", default="combined.qmd", help="Output file (.qmd or .md)")
    ap.add_argument("--root", default=".", help="Project root containing _quarto.yml")
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    cfg_path = root / "_quarto.yml"
    if not cfg_path.exists():
        raise SystemExit(f"Could not find {cfg_path}")

    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    book = cfg.get("book", {}) or {}

    ordered_files = []
    for section in ("chapters", "appendices"):
        ordered_files.extend(list(flatten_manifest(book.get(section))))

    # Keep only existing .qmd/.md files, in order
    paths = []
    for rel in ordered_files:
        if not isinstance(rel, str):
            continue
        if not rel.endswith((".qmd", ".md")):
            continue
        p = (root / rel).resolve()
        if p.exists():
            paths.append((rel, p))

    if not paths:
        raise SystemExit("No .qmd/.md files found in book.chapters/book.appendices")

    out_path = (root / args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as out:
        for idx, (rel, p) in enumerate(paths):
            txt = p.read_text(encoding="utf-8")

            # Keep YAML front matter only from the first file; strip it from others
            if idx > 0:
                txt = FRONT_MATTER_RE.sub("", txt, count=1)

            out.write(f"\n\n<!-- BEGIN {rel} -->\n\n")
            out.write(txt.rstrip() + "\n")
            out.write(f"\n<!-- END {rel} -->\n")

    print(f"Wrote {out_path} ({len(paths)} files).", file=sys.stderr)


if __name__ == "__main__":
    main()

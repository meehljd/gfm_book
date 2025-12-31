#!/usr/bin/env python3
import re
from pathlib import Path

root = Path(".")
out_path = Path("qmd_headings.md")  # change as you like

heading_re = re.compile(r"^\s{0,3}#{1,6}\s+\S")

with out_path.open("w", encoding="utf-8", newline="\n") as out:
    for p in sorted(root.rglob("*.qmd")):
        try:
            lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception as e:
            out.write(f"\n### {p}\n(error reading: {e})\n")
            continue

        heads = [ln for ln in lines if heading_re.match(ln)]

        out.write(f"\n### {p}\n")
        if heads:
            out.write("\n".join(heads) + "\n")
        else:
            out.write("(no markdown headings found)\n")

print(f"Wrote headings to: {out_path.resolve()}")
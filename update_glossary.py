#!/usr/bin/env python3
"""
Update app-c-glossary.qmd with all terms from glossary.yml.

Usage:
    python update_glossary.py path/to/glossary.yml path/to/app-c-glossary.qmd
"""

import yaml
import sys
from pathlib import Path


def extract_terms(glossary_path: str) -> list[str]:
    """Extract all term names from glossary.yml."""
    with open(glossary_path, 'r') as f:
        data = yaml.safe_load(f)
    
    # Handle both flat dict and nested structure
    terms = []
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                # Nested structure (e.g., categories)
                terms.extend(value.keys())
            else:
                # Flat structure: key is the term
                terms.append(key)
    
    return sorted(terms, key=str.lower)


def generate_qmd(terms: list[str]) -> str:
    """Generate the qmd content with glossary shortcodes."""
    lines = [
        "# Glossary",
        "",
    ]
    
    # Add a shortcode for each term (this preloads them for the table)
    for term in terms:
        lines.append(f'{{{{< glossary "{term}" display="" popup="none" >}}}}')
        lines.append("")
    
    # Add the table shortcode
    lines.append("")
    lines.append("{{< glossary table=true >}}")
    lines.append("")
    
    return "\n".join(lines)


def main():
    if len(sys.argv) != 3:
        print("Usage: python update_glossary.py <glossary.yml> <app-c-glossary.qmd>")
        sys.exit(1)
    
    glossary_path = sys.argv[1]
    output_path = sys.argv[2]
    
    terms = extract_terms(glossary_path)
    print(f"Found {len(terms)} terms in {glossary_path}")
    
    content = generate_qmd(terms)
    
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"Updated {output_path}")


if __name__ == "__main__":
    main()
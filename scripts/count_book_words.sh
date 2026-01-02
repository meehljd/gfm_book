#!/bin/bash
# count_book_words.sh

# List of .qmd files to exclude from the "main" total
# (Edit this list to match your project)
exclude_list=(
  "appendix/app-f-glossary.qmd"
)

# Path to rendered references page
refs_html="./docs/bib/references.html"

total_qmd_all=0       # total for all .qmd files
total_qmd_included=0  # total excluding the files in exclude_list
refs_words=0          # word count for references.html body

is_excluded() {
  local file="$1"
  for ex in "${exclude_list[@]}"; do
    if [[ "$file" == "$ex" ]]; then
      return 0  # true: is excluded
    fi
  done
  return 1  # false: not excluded
}

echo "=== .qmd files ==="

# Find all .qmd files in current and child directories (excluding docs/), sort alphabetically
{
  while read -r f; do
    # Remove leading ./ for display and exclusion check
    f_display="${f#./}"

    words=$(quarto pandoc "$f" -f markdown -t plain 2>/dev/null | wc -w)
    total_qmd_all=$((total_qmd_all + words))

    if is_excluded "$f_display"; then
      printf "%-40s %8d   %s\n" "$f_display" "$words" "[excluded from main total]"
    else
      printf "%-40s %8d\n" "$f_display" "$words"
      total_qmd_included=$((total_qmd_included + words))
    fi
  done < <(find . -type f -name '*.qmd' ! -path './docs/*' | sort)
}

echo
echo "=== References (HTML) ==="

if [[ -f "$refs_html" ]]; then
    # Extract just the <main class="content" ...> ... </main> block,
    # convert HTML to plain text with pandoc, and count words.
    refs_words=$(sed -n '/<main class="content" id="quarto-document-content">/,/<\/main>/p' "$refs_html" \
      | pandoc -f html -t plain 2>/dev/null \
      | wc -w)

    printf "%-40s %8d\n" "$refs_html" "$refs_words"
else
    echo "No $refs_html found; skipping references HTML."
fi

echo "----------------------------------------"
printf "%-40s %8d\n" "TOTAL (.qmd included only)" "$total_qmd_included"
printf "%-40s %8d\n" "References (HTML body)"      "$refs_words"
printf "%-40s %8d\n" "TOTAL (all qmd + refs)"      "$((total_qmd_all + refs_words))"

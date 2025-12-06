#!/bin/bash
# count_book_words.sh
total=0
for f in *.qmd; do
    words=$(quarto pandoc "$f" -f markdown -t plain 2>/dev/null | wc -w)
    printf "%-40s %6d\n" "$f" "$words"
    total=$((total + words))
done
echo "----------------------------------------"
printf "%-40s %6d\n" "TOTAL" "$total"
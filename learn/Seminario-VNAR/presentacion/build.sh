#!/usr/bin/env bash
# Compila slides.tex y handout.tex, limpia auxiliares.
set -e
cd "$(dirname "$0")"

for doc in slides handout; do
  echo "=== $doc ==="
  pdflatex -interaction=nonstopmode "$doc.tex" > "/tmp/${doc}_build.log" 2>&1
  pdflatex -interaction=nonstopmode "$doc.tex" > "/tmp/${doc}_build.log" 2>&1
  if grep -qE "^!" "/tmp/${doc}_build.log"; then
    echo "  ERROR — ver /tmp/${doc}_build.log"
    grep -E "^!" "/tmp/${doc}_build.log"
    exit 1
  fi
  echo "  OK -> $doc.pdf"
done

# limpieza de auxiliares (deja los .tex y los .pdf)
find . -maxdepth 1 -type f \( -name "*.aux" -o -name "*.log" -o -name "*.nav" \
  -o -name "*.out" -o -name "*.snm" -o -name "*.toc" -o -name "*.vrb" \) -delete

echo "Listo: slides.pdf, handout.pdf"

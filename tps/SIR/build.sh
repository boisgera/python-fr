#!/usr/bin/env bash

pandoc --standalone --toc \
  --css css/style.css \
  --no-highlight \
  --include-in-header html/fonts.html \
  --include-in-header html/plan.html \
  --include-in-header html/links.html \
  --include-in-header html/copy-code.html \
  --include-in-header html/collapse.html \
  -V lang=fr \
  --mathjax \
  -o index.html index.md

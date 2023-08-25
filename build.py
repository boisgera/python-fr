#!/usr/bin/env python

# Standard Library
import os
from pathlib import Path

# Third-Party Libraries
import pandoc
from plumbum import local, FG

cwd = Path.cwd()

# Build in subdirectories
for build_py in cwd.glob("*/**/build.py"):
    dir = build_py.parent
    print(build_py)
    try:
        os.chdir(dir)
        local["./build.py"] & FG
    finally:
        os.chdir(cwd)

# Transform the README.md into a index.html
with open("README.md", mode="r", encoding="utf-8") as file:
    README = file.read()

# Relative links (fork-friendly)
README = README.replace("https://boisgera.github.io/python-fr/", "")
doc = pandoc.read(README)
options = [
    "--standalone",
    "--css=css/style.css",
    "--include-in-header=html/font.html",
    "--include-in-header=html/copy-code.html",
    "--variable=lang:fr",
    "--no-highlight"
]
pandoc.write(doc, file="index.html", format="html", options=options)



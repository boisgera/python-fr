#!/usr/bin/env python

# Python Standard Library
import os
from pathlib import Path
from typing import Optional

# First-Party Librairies
import pandoc

# Third-Party Librairies
from bs4 import BeautifulSoup; HTML = lambda arg: BeautifulSoup(arg, "html.parser")
import plumbum
from plumbum import FG
from plumbum.cmd import date, python
try:
    from plumbum.cmd import git
except ImportError:
    git = None
import typer

options = [
    "--standalone",
    "--toc",
    "--toc-depth=2",
    "--mathjax",
    "--css=css/style.css",
    "--include-in-header=html/font.html",
    "--include-in-header=html/copy-code.html",
    "--variable=lang:fr",
    # Bibliography
    # "--bibliography=bibliography.json",
    # "--citeproc",
    # "--metadata=link-citations:true",
    "--no-highlight"
]

def generate_images():
    cwd = Path.cwd()
    try:
        os.chdir(cwd / "images")
        python["main.py"] & FG
    finally:
        os.chdir(cwd)

def generate_videos():
    cwd = Path.cwd()
    try:
        os.chdir(cwd / "videos")
        python["main.py"] & FG
    finally:
        os.chdir(cwd)


def generate_html():
    doc = pandoc.read(file="index.md")
    pandoc.write(doc, file="index.html", options=options)

def post_process_html():
    with open("index.html", encoding="utf-8") as input:
        html = HTML(input)

    # Include github link into header
    p = HTML("""
      <p>
        <span style='display:inline-block;width:1em;position:relative;margin-right:0.25em'>
          <img 
            style='position:relative;top:0.15em;'
            height='auto' width='100%' 
            src='icons/github.svg'>
          </img></span>
        <a 
          href='https://github.com/boisgera/python-fr'>
          https://github.com/boisgera/python-fr
        </a>
      </p>
    """)
    html.body.header.append(p)

    # Include github hash into the header
    hash_ = git("rev-parse", "--short", "HEAD").strip()
    p = HTML(f"""
      <p>
        <span style='display:inline-block;width:1em;position:relative;margin-right:0.25em'>
          <img 
            style='position:relative;top:0.15em;'
            height='auto' width='100%' 
            src='icons/git.svg'>
          </img>
        </span>
        <a 
          href='https://github.com/boisgera/python-fr/commit/{hash_}'>
          #{hash_}
        </a>
      </p>
    """)
    html.body.header.append(p)

    # Include "edit" link into the header
    # https://github.com/boisgera/python-fr/edit/master/tps/snake-1/build.py
    # find the location of the project wrt project root.
    path = Path().absolute()
    r = ""
    while not (path / ".git").exists():
        r = path.name + ("/" if r else "") + r
        path = path.parent
    edit_path = f"https://github.com/boisgera/python-fr/edit/master/{r}/index.md"
    p = HTML(f"""
      <p>
        <span style='display:inline-block;width:1em;position:relative;margin-right:0.25em'>
          <img 
            style='position:relative;top:0.15em;'
            height='auto' width='100%' 
            src='icons/edit.svg'>
          </img>
        </span>
        <a 
          href={edit_path}>
          Edition
        </a>
      </p>
    """)
    html.body.header.append(p)

    # Set the date to now.
    # plumbum.local.env["LC_TIME"] = "en_US.utf-8" 
    date_ = date("+%A %d %B %Y").strip().capitalize()
    html.body.header(class_="date")[0].string = date_

    # Enable Mathjax Equation Numbers (and label + eqref)
    html.head.insert(0,HTML("""
      <script>
        window.MathJax = {
          tex: {
            tags: 'ams'
          }
        };
       </script>
    """))

    # Pimp the table of contents
    nav = html.body.nav
    toc = HTML("""
      <details>
        <summary>
          <h2>Table des matières</h2>
        </summary>
      </details>
    """)
    toc.details.append(nav)
    html.body.header.insert_after(toc)

    # Deal automatically with the <details>
    # TODO (may require "pre-encapsulation" of content in sections)

    with open("index.html", "w", encoding="utf-8") as output:
        output.write(str(html))



def main(
    all: bool = typer.Option(False, help="Generate all assets."),
):
    if all:
        generate_images()
        generate_videos()
    generate_html()
    post_process_html()



if __name__ == "__main__":
    typer.run(main)

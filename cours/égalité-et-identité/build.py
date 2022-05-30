#!/usr/bin/env python

import pandoc
from pandoc.types import Div, Header


def divify(doc, level=None):
    # Encapsulate section content -- separated by headers -- in divs.

    # Note for the HTML backend:
    #  - div.section turned into section automatically but ...
    #  - the TOC generation is broken. That happens because of the
    #    extra div hierarchy, not specifically the "section" class.
    #    reference: <https://github.com/jgm/pandoc/issues/997>;
    #    marked as wontfix.

    # Note: isse with references; the bibliography will be added later,
    # out of the section.

    if level is None:
        for level in reversed([1, 2, 3, 4]):
            divify(doc, level=level)
    else:
        sections = []
        for elt, path in pandoc.iter(doc, path=True):
            if isinstance(elt, Header) and elt[0] == level:
                # print(str(elt)[:100])
                header = elt
                holder, start = path[-1]
                for offset, elt_ in enumerate(holder[start:]):
                    if offset == 0:
                        continue
                    if isinstance(elt_, Header) and elt_[0] <= level:
                        end = start + offset
                        break
                else:
                    end = None
                assert holder[start:end]  # not empty, at least a header
                sections.append((holder, start, end))

        for section in reversed(sections):
            holder, start, end = section
            level, attr, inlines = header = holder[start]
            _, cls, _ = attr

            if "details" in cls:
                attr = ("", ["div-details"], [])
                div = Div(attr, holder[slice(start, end)])
                #print(str(div)[:100])
                holder[slice(start, end)] = [div]
                #print("holder:", holder)


doc = pandoc.read(file="index.md")
divify(doc, level=4)
divify(doc, level=3)

options = [
  "--standalone", 
  "--template", "pandoc-templates/template.html5",
  "--toc",
  "--css",  "css/style.css",
  "--no-highlight",
  "--include-in-header", "html/fonts.html",
  "--include-in-header", "html/plan.html",
  "--include-in-header", "html/links.html",
  "--include-in-header", "html/copy-code.html",
  "--include-in-header", "html/detailify.html",
  "--include-in-header", "html/collapse.html",
#   "--include-in-header", "html/doctest.html",
  "-V", "lang=fr",
  "--mathjax"
]

pandoc.write(doc, file="index.html", format="html", options=options)



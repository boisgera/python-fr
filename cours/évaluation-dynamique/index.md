---
title: Evaluation dynamique de code
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
---

Eval, exec et repr

``` python
l = [(1, 2), (2, 2), (3, 2)]

str(l)

repr(l)

s = repr(l)

eval(s)

type(eval(s))

eval(repr(s)) == s


```


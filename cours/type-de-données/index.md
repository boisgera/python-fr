---
title: Types de données
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
---

# Kit de survie

variables, affichage `repr`, `dir`, `type`, `isinstance`, `help`



# Types numériques

``` python


bool, int, float, complex (etc.)

b = True

c = False

2**1000 # entiers non bornés !

1 + 3 * 2

2**10

17 % 12

17 / 12

17 // 12

a = 42

bin(a)

hex(a)

0b101010

0x2a

0x2a == 42

type(0x2a)

3.14

from math import sin

sin(3.14)

int("300")

int(3.14)

int(3.94)

round(3.14)

round(3.94)

import math

math.floor(3.94)

0.1 + 0.2

f"{0.1:.1000}"

f"{0.2:.1000}"

f"{0.3:.1000}"

1j # complex number

1j * 1j

z = 0.7 + 0.3j

for attribute in dir(z):
    if not attribute.startswith("_"):
        print(attribute)

z.real

z.imag

z.conjugate

z.conjugate()


```

# Collections

## Listes

``` python
Listes

Liste de références / adresses / pointeurs (vers les données).

Taille variable, contenu modifiable.

Liste d'objets (potentiellement) hétérogènes.

l = [1.0, 1.0 + 0.1j, 2, 3]

l[1]

l[1] = 42

del l[1]

l

l.append(12)

l

l.extend([9, 10, 11, 12])

l

help(l)

dir(l)

help(l.index)

l

help(l.pop)

l[-1]

l.pop()

l

l.pop(0)

l

help(l.remove)

l

l.remove(9)

l

l.index(10)

l.count(63)

l = [1, 2]
r = l.extend([3, 4])

r == None

l

l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2

l1

l2 

l3

3 * [7, 1]

len(l)

for i in l:
    print(i)

for i in range(5):
    print(i)

range(5)

list(range(5))
```


## Dictionnaires

``` python
d = {"a":1, "b":2, "c":3}

d

d["a"] # lecture

d["d"] = 4 # écriture

d

del d["a"] # effacement

d

d["a"]

---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/tmp/ipykernel_17241/3859482410.py in <module>
----> 1 d["a"]

KeyError: 'a'

d.get("b", 0)

d.get("a", 0)

for x in d:
    print(x, ":", d[x])

"a" in d

"b" in d

list(d)

for x in d.keys():
    print(x)

for x in d.values():
    print(x)

for x in d.items():
    print(x)

d.update({"e": 5, "f": 6})

d

dir(d)

d.pop("b")

d

help(d.setdefault)

from collections import defaultdict

help(defaultdict)

{"kjdslkjdlsdk": 90.0}

{1: 4, 1.0: 8, 1.5j: 0, True: 90.90}

{(1, 2): 7, (7, 8, 9): 9}

{(1, ("aa", "bb")): 90}

{[2]: 90.0}

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_17241/1412873092.py in <module>
----> 1 {[2]: 90.0}

TypeError: unhashable type: 'list'

hash(1.34)

hash("kjskdjsjdskj")

hash(("kjdsjdks", 909090))

hash([1, 2, 3])

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_17241/2492717709.py in <module>
----> 1 hash([1, 2, 3])

TypeError: unhashable type: 'list'

hash((1, [2, 3]))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_17241/2425333101.py in <module>
----> 1 hash((1, [2, 3]))

TypeError: unhashable type: 'list'

def f():
    pass
import sys
d = {1: 1.0, 2: f, 3: sys}
d

```

## N-uplets

De longueur fixe, non modifiables ("en surface")

``` python
def f():
    return "ok", 3.14 # or ("ok", 3.14)

status, value = f()

status

value

result = f()

result

type(result)

a = 1, 2

b = (1, 2)

a == b

empty_tuple = ()

type(empty_tuple)

len_1_tuple = (1,)

len_1_tuple

(((1)))

t = (1, 2)
t[0] = 2.0

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_21535/74121951.py in <module>
      1 t = (1, 2)
----> 2 t[0] = 2.0

TypeError: 'tuple' object does not support item assignment

l = [1, 2, 3]
t = (l, 2, 3, 3)
t

l.append(42)
t

```

## Ensembles

``` python


{1, 2, 3, 4}

{} # empty dict

type({})

set()

set([1, 2, 3])

set([1, 1, 2, 3, 3, 3, 4])

list(set([1, 1, 2, 3, 3, 3, 4]))

s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}

s = {[]}

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_17241/1126056997.py in <module>
----> 1 s = {[]}

TypeError: unhashable type: 'list'

s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}

s.add(42)

s

s.remove(42)

s

1 in s

for x in s:
    print(x)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s1 | s2

s1 & s2

s1 - s2

```

# Texte & données binaires

TODO: repr & eval:

``` python
l = [(1, 2), (2, 2), (3, 2)]

str(l)

repr(l)

s = repr(l)

eval(s)

type(eval(s))

eval(repr(s)) == s

```

## Chaînes de caractères & données binaires

``` python


r = 'kldskdmlskdms'

"j'utilise des apostrophes"

'j' + "'" + 'utilise des apostrophes'

'j\'utilise des apostrophes'

print("a\nb")

print("a\tb")

print("\\")

s = "\\"
ord(s)

hex(92)

print("le slash est: \x5c")

hex(ord("a")) # ascii code of "a"

print("la lettre a: \x61")

print("smiley: \U0001f600")

print("\U0001f4a9")

s = "kjdslkdjslkdsljdlksdjdslkdjs -------------------- hhhhhhhh"

s[0:5] + s[-5:]

len(s)

for c in s:
    print(c)

s = "Sébastien"

s.encode("utf-8")

s.encode("latin-1")

s.encode("cp1252")

s.encode("utf-8").decode("utf-8")

s.encode("utf-8").decode("latin-1")


```

## Fichiers

``` python


file = open("texte.txt", mode="w", encoding="utf-8")

file.write("Sébastien")

file.close()

f = open("texte.txt", mode="r", encoding="utf-8")

f.read()

f = open("texte.txt", mode="br") # binary mode

data = f.read()
data

data.decode("utf-8")

```
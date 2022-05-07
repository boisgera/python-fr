---
title: Types de données
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
---

# Kit de survie

variables, affichage `repr`, `dir`, `type`, `isinstance`, `help`

# Absence de valeur

Python fournit une valeur `None` qui signale ... l'absence de valeur!
D'ailleurs, l'interpréteur Python ne veut pas nous l'afficher quand
on fournit cette valeur sur l'invite de commandes : 

```python
>>> None
```

Passer par une variable ne change rien.

```python
>>> a = None
>>> a
```

Par contre on peut expliciter afficher `None`, par exemple avec la fonction `print` :

```python
>>> print(a)
None
```

La valeur `None` n'a rien de très complexe en soi ; mais ses cas d'usage
classiques méritent d'être étudiés : ce n'est pas comment fonctionne `None`
qui est subtil, mais plutôt comment on peut l'utiliser à bon escient.

## Mécanismes

`None` est une valeur unique en Python (il n'y a aucun moyen de générer deux
`None` qui soient différents). On peut donc tester si une variable `x` est 
`None` en évaluant l'expression `x is None` :

```python
>>> x = 1
>>> x is None
False
>>> x = None
>>> x is None
True
```

Attention, une variable affectée à `None` et une variable indéfinie (qui n'est
liée à aucune valeur) c'est subtilement différent. Si la variable `y` n'a pas
encore été introduite (ou a été effacée avec `del y`),
 l'évaluation de l'expression `y is None` provoque une erreur

```python
>>> y is None
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
```

comme d'ailleurs toute expression qui utilise `y`:

```python
>>> y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
```

Dans un contexte booléen, `None` est évalué comme `False`, mais le test
`x is None` est plus sélectif, donc en général préférable :

```python
>>> x = None
>>> if x is None:
...    print("x is None")
...
x is None
>>> if not x:
...    print("x is false-ish")
...
x is false-ish
>>> x = 0
>>> if not x:
...    print("x is false-ish")
...
x is false-ish
```

## Fonctions sans valeur de retour

Comme les fonctions mathématiques, les fonctions Python ont des
arguments et renvoient des valeurs

```python
>>> abs(-1)
1
```

Mais invoquer une fonction Python peut aussi avoir des **effets de bords**
(🇺🇸 **side-effect**), par exemple: 

  - afficher du texte dans le terminal, 
  
  - modifier une variable globale, 
  
  - écrire dans un fichier, 
  
  - envoyer un e-mail,

  - etc.

Si cet effet de bord est l'unique raison d'être de la fonction, il est alors
inutile de renvoyer une valeur.

Par exemple, invoquer la fonction `sleep` du module Python `time` va mettre
en pause le programme qui l'invoque (ici l'interpréteur Python) pendant un temps
déterminé, puis le laisser suivre son cours. L'effet de bord attendu ici,
c'est la pause dans le programme. Utilisons cette fonction pour dans notre
propre fonction `think`

```python
import time
def think():
    print("Je réfléchis ...", end=" ")
    time.sleep(3.0)
    print("J'ai fini !")
```

que l'on invoquera de la façon suivante

```python
>>> think()
Je réfléchis ... J'ai fini !
```

Mais toute valeur Python renvoie -- implicitement ou explicitement -- une valeur.
Il est donc légitime d'affecter le résultat de `think()` à une variable.
La difficulté, c'est que l'interpréteur Python ne l'affiche pas:

```python
>>> result = think()
Je réfléchis ... J'ai fini !
>>> result
>>>
```

Notre fonction a en fait renvoyé la valeur spéciale `None` qui peut être 
interprétée comme "absence de valeur" (oui, c'est un peu paradoxal !). 
En insistant, on peut quand même faire en sorte que l'interpréteur Python
avoue quelle est la réalité :

```python
>>> print(result)
None
```

Tout se passe en fait comme si l'interpréteur Python, constatant que la
définition de notre fonction `think` ne renvoyait *explicitement* aucune valeur 
(le mot-clé `return` n'est pas utilisé) y avait ajouté l'instruction 
`return None`:

```python
def think():
    print("Je réfléchis ...", end=" ")
    time.sleep(3.0)
    print("J'ai fini !")
    return None
```

## Fonction avec valeur de retour optionnelle

Les dictionnaires Python génère une erreur lorsque l'on essaie d'accéder 
à la valeur d'une clé qui n'existe pas.

```python
>>> d = {"a": 1, "b": 2}
>>> d["a"]
1
>>> d["c"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'
```

Cela n'est pas toujours très pratique. Heureusement il existe une méthode
auxilaire qui permet de renvoyer une valeur particulière en cas d'échec.
Par défaut, cette valeur est `None`.


```python
>>> help(dict.get)
Help on method_descriptor:

get(self, key, default=None, /)
    Return the value for key if key is in the dictionary, else default.
```

Ainsi, si l'on souhaite afficher les valeurs associées aux clés `"a"`, `"b"`
et `"c"` (supposées différentes de `None`) si elles existent et rien sinon,
on pourra faire :

```python
>>> for key in ["a", "b", "c"]:
...     value = d.get(key)
...     if value is not None:
...         print(value)
1
2
```

## Fonction et absence d'argument

La valeur `None` est souvent utilisée comme valeur par défaut
associé à l'argument d'une fonction. Ne pas affecter (explicitement) de
valeur à cet argument revient à lui affecter la valeur `None`, ce que
la fonction pourra détecter et gérer de façon appropriée.

Nous allons illustrer cela avec la fonction `seterr` de NumPy, dont la
documentation commence de la façon suivante :

```python
>>> help(np.seterr) # doctest: +ELLIPSIS
Help on function seterr in module numpy:

seterr(all=None, divide=None, over=None, under=None, invalid=None)
    Set how floating-point errors are handled.
...
```


Pour mémoire, en cas de division par zéro, les nombres flottants standards (`float`)
de Python génèrent une erreur :

```python
>>> 1.0 / 0.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: float division by zero
```

Mais ce qui se passe si l'on utilise les nombres flottants 
fournis par NumPy (`float64`) est un peu différent:

```python
>>> import numpy as np
>>> one = np.float64(1.0)
>>> zero = np.float64(0.0)
>>> one / zero
<stdin>:1: RuntimeWarning: divide by zero encountered in double_scalars
inf
```

Python émet un **avertissement**[^warnings] (🇺🇸 **warning**) mais renvoie bien 
une valeur : `inf` (c'est-à-dire $+\infty$).  

[^warnings]: Il est probable que cet avertissement ne s'affiche que la première
fois que vous effectuez la division par zéro, mais plus ensuite. Les fonctions
du module warnings permettent de controller ce comportement.

Ce comportement est toutefois configurable : 
en appelant la fonction `seterr` de NumPy sans argument, vous pouvez lire
la configuration courante :

```python
>>> np.seterr()
{'divide': 'warn', 'over': 'warn', 'under': 'ignore', 'invalid': 'warn'}
```

Si ce comportement par défaut ne vous plait pas, 
vous pouvez utiliser la fonction `seterr` de NumPy pour générer une erreur 
en cas de division par zero.

```python
>>> _ = np.seterr(divide="raise")
>>> one / zero
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FloatingPointError: divide by zero encountered in double_scalars
```

Si à l'inverse vous pensez que $1.0 / 0.0$ est une opération "normale" qui
doit renvoyer un "non-nombre" ($\bot$ ou `nan`), faites en sorte que le mécanisme
de gestion des avertissements et erreurs de NumPy les ignore.

```python
>>> _ = np.seterr(divide="ignore")
>>> one / zero
inf
```

Si ce résultat vous convient, mais que vous souhaitez une erreur en cas de
**dépassement** (🇺🇸 **overflow**) (sous-entendu: du plus grand nombre flottant fini),
vous pouvez invoquer `seterr` en conséquence :

```python
>>> _ = np.seterr(overflow="raise")
>>> two = one + one
>>> two**10000
>>> np.float64(2.0) ** 10000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FloatingPointError: overflow encountered in double_scalars
```


On apprend ainsi qu'il y a 5 arguments, qui ont tous la valeur par défaut
`None`. Les appels successifs que nous avons fait à `seterr`

```python
np.seterr()
np.seterr(divide="raise")
np.seterr(divide="error")
np.seterr(over="raise")
```

sont donc équivalents à

```python
np.seterr(all=None, divide=None, over=None, under=None, invalid=None)
np.seterr(all=None, divide="error", over=None, under=None, invalid=None)
np.seterr(all=None, divide="raise", over=None, under=None, invalid=None)
np.seterr(all="raise", divide=None, over=None, under=None, invalid=None)
```

La valeur de `None` interprétée par `seterr` comme un argument que
l'on n'a pas explicitement spécifié et donc dont on ne souhaite pas
modifier la configuration. Cette stratégie permet de lire la configuration
sans la changer, de changer la réaction en présence d'une division par 
zéro sans changer celle en cas d'overflow, etc.

# TODO. Vrai ou faux

`True` et `False`

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

**TODO.** Splitter collections en un nouveau document? 
Et strings en un troisième?

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
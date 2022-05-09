---
title: Collections
author:
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris -- PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: today
---

# Listes

Listes

Liste de références / adresses / pointeurs (vers les données).

Taille variable, contenu modifiable.

Liste d'objets (potentiellement) hétérogènes.

```python
>>> l = [1.0, 1.0 + 0.1j, 2, 3]
>>>
>>> l[1]
(1+0.1j)
>>>
>>> l[1] = 42
>>>
>>> del l[1]
>>>
>>> l
[1.0, 2, 3]
>>>
>>> l.append(12)
>>>
>>> l
[1.0, 2, 3, 12]
>>>
>>> l.extend([9, 10, 11, 12])
>>>
>>> l
[1.0, 2, 3, 12, 9, 10, 11, 12]
>>>
>>>
>>> dir(l)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>>
>>>
>>> l
[1.0, 2, 3, 12, 9, 10, 11, 12]
>>>
>>>
>>> l[-1]
12
>>>
>>> l.pop()
12
>>>
>>> l
[1.0, 2, 3, 12, 9, 10, 11]
>>>
>>> l.pop(0)
1.0
>>>
>>> l
[2, 3, 12, 9, 10, 11]
>>>
>>>
>>> l
[2, 3, 12, 9, 10, 11]
>>>
>>> l.remove(9)
>>>
>>> l
[2, 3, 12, 10, 11]
>>>
>>> l.index(10)
3
>>>
>>> l.count(63)
0
>>>
>>> l = [1, 2]
>>> r = l.extend([3, 4])
>>>
>>> r == None
True
>>>
>>> l
[1, 2, 3, 4]
>>>
>>> l1 = [1, 2]
>>> l2 = [3, 4]
>>> l3 = l1 + l2
>>>
>>> l1
[1, 2]
>>>
>>> l2
[3, 4]
>>>
>>> l3
[1, 2, 3, 4]
>>>
>>> 3 * [7, 1]
[7, 1, 7, 1, 7, 1]
>>>
>>> len(l)
4
>>>
>>> for i in l:
...     print(i)
...
1
2
3
4
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>> range(5)
range(0, 5)
>>>
>>> list(range(5))
[0, 1, 2, 3, 4]
```

# Dictionnaires

```python
>>> d = {"a":1, "b":2, "c":3}
>>>
>>> d
{'a': 1, 'b': 2, 'c': 3}
>>>
>>> d["a"] # lecture
1
>>>
>>> d["d"] = 4 # écriture
>>>
>>> d
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>>
>>> del d["a"] # effacement
>>>
>>> d
{'b': 2, 'c': 3, 'd': 4}
>>>
>>> d["a"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
>>> d.get("b", 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> d.get("a", 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> for x in d:
...     print(x, ":", d[x])
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> "a" in d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> "b" in d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> list(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> for x in d.keys():
...     print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> for x in d.values():
...     print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> for x in d.items():
...     print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> d.update({"e": 5, "f": 6})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> dir(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> d.pop("b")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
>>> d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> {"kjdslkjdlsdk": 90.0}
{'kjdslkjdlsdk': 90.0}
>>> 
>>> {1: 4, 1.0: 8, 1.5j: 0, True: 90.90}
{1: 90.9, 1.5j: 0}
>>> 
>>> {(1, 2): 7, (7, 8, 9): 9}
{(1, 2): 7, (7, 8, 9): 9}
>>> 
>>> {(1, ("aa", "bb")): 90}
{(1, ('aa', 'bb')): 90}
>>> 
>>> {[2]: 90.0}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

>>> hash(1.34)
783986623132656129
>>> 
>>> hash("kjskdjsjdskj")
-2340630600562179480
>>> 
>>> hash(("kjdsjdks", 909090))
9110669353542020956
>>> 
>>> hash([1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
```

```python
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

# N-uplets

Les n-uplets sont souvent utilisés de façon implicite, pour concevoir une
fonction renvoyant plusieurs valeurs ou pour affecter en une instruction
unique plusieurs variables.

```python
>>> def compute_pi():
...     value = 3.14
...     error = 0.005
...     return value, error
... 
>>> value, error = compute_pi()
>>> print(f"{value} ± {error}")
3.14 ± 0.005
```

```python
>>> a = 1
>>> b = 2
>>> c = 3
>>> a, b = b, c
>>> a
2
>>> b
3
``` 

L'instruction `value, error = compute_pi()` produit en fait une paire 
(un n-uplet de longueur 2) qui est instantanément **destructuré** pour
fournir des valeurs aux variables `value` et `error`. 
Cela devient beaucoup plus évident si l'on décompose ces étapes :

```python
>>> value_and_error = compute_pi()
>>> value_and_error
(3.14, 0.005)
>>> type(value_and_error)
<class 'tuple'>
>>> len(value_and_error)
2
>>> value, error = value_and_error
>>> value
3.14
>>> error
0.005
```

Quant à l'affectation `a, b = b, c`, elle passe aussi implicitement par la
création d'une paire : elle équivaut à

``` python
>>> b_and_c = b, c
>>> b_and_c
(2, 3)
>>> type(b_and_c)
<class 'tuple'>
>>> len(b_and_c)
2
>>> a, b = b_and_c
>>> a
2
>>> b
3
```

Si nous avons pu oublier qu'un tuple était crée, c'est qu'un tuple peut le
plus souvent être défini par une notation très légère, avec une suite d'objets
séparés par des virgules. Mais la notation universellement valide des tuples
met entre parenthèse cette suite. Au lieu du code initial, nous aurions très
bien pu écrire


```python
>>> def compute_pi():
...     value = 3.14
...     error = 0.005
...     return (value, error)
... 
>>> (value, error) = compute_pi()
>>> print(f"{value} ± {error}")
3.14 ± 0.005
```

```python
>>> a = 1
>>> b = 2
>>> c = 3
>>> (a, b) = (b, c)
>>> a
2
>>> b
3
``` 
ce qui est équivalent, mais plus explicite. Le tuple vide est d'ailleurs
désigné par la notation `()` ; pour un n-uplet de longueur 0 contenant
par exemple l'unique argument 1, on serait tenté d'utiliser la notation
`(1)` mais il y aurait alors une ambiguité dans les notations car les
parenthèses sont aussi utilisées pour indiquer des priorités entre opérations
dans les calculs. Il faut donc se résigner à adopter une **virgule finale**
(🇺🇸 **trailing comma**) et utiliser la notation `(1,)`. On peut conserver
la virgule finale pour les n-uplets de longueur 2 ou plus, mais elle n'est
plus nécessaire.

```python
>>> ()
()
>>> (1)
1
>>> (1,)
(1,)
>>> 1,
>>> (1, 2)
(1, 2)
>>> (1, 2,)
(1, 2)
>>> 1, 2
(1, 2)
>>> 1, 2,
(1, 2)
```

Les n-uplets sont immuables : de longueur fixe et dont les élements ne peuvent
être remplacés.

```python
>>> t = (1, 2)
>>> t[0]
1
>>> t[1]
2
>>> t[0] = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Néanmoins cette immuabilité est superficielle : si un n-uplet contient une
valeur modifiable (comme une liste), il est toujours possible de modifier 
la liste et donc de modifier **indirectement** le n-uplet.

```python
>>> l = [1, 2, 3]
>>> t = (l, 2, 3, 3)
>>> t
([1, 2, 3], 2, 3, 3)
>>> l.append(42)
>>> t
([1, 2, 3, 42], 2, 3, 3)
```


# Ensembles

Un ensemble peut être défini par une suite d'objets séparés par des virgules 
et entourée par des accolades

```python
>>> {1, 2, 3, 4}
{1, 2, 3, 4}
```

Il est également possible de passer par le constructeur `set` avec une
une liste comme argument

```python
>>> set([1, 2, 3, 4])
{1, 2, 3, 4}
```

Inversement, il est aisé de convertir un ensemble en liste

```python
>>> list({1, 2, 3, 4})
[1, 2, 3, 4]
```

⚠️ La notation `{}` ne définit pas un ensemble vide, mais un dictionnaire vide[^dict].
L'ensemble vide peut être défini par `set()`.

```python
>>> type({})
<class 'dict'>
>>> set()
set()
```

[^dict]: Les dictionnaires existaient dans Python bien avant que les ensembles
ne soient introduits. Ils ont donc exploité les premiers la notation `{}` et 
les ensembles ont dû s'en accomoder a posteriori.

L'implémentation d'un ensemble est similaire à celle d'un dictionnaire 
qui auraient les élements de l'ensemble comme clés et (par exemple) `True` 
comme valeur commune à toutes les clés. 

```python
>>> s = {1, 2, 3, 4}
>>> d = {1: True, 2: True, 3: True, 4: True}
```

Cela permet de comprendre pourquoi les élements répétés d'un ensemble sont 
ignorés et pourquoi bien que l'ordre d'insertion des éléments soit préservé, 
cet ordre ne rentre pas en ligne de compte dans les comparaisons

``` python
>>> {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
{1, 2, 3, 4}
>>> {4, 3, 2, 1}
{4, 3, 2, 1}
>>> {1, 2, 3, 4} == {4, 3, 2, 1}
True
```

Sans surprise, on peut également en déduire que seuls les objets hashables 
peuvent être utilisés comme éléments d'un ensemble.

```python
>>> s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}
>>> s = {[]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```
Les ensembles sont modifiables : il est possible d'ajouter des éléments à un ensemble
et d'en retirer. 
Il est également possible de tester si un objet appartient à l'ensemble et 
d'itérer sur les éléments de l'ensemble.

```python
>>> s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}
>>> s.add(42)
>>> s
{(2, ('jsdksjk', 90)), 1, 2, (2, 3), 'djksjds', 42}
>>> s.remove(42)
>>> s
{(2, ('jsdksjk', 90)), 1, 2, (2, 3), 'djksjds'}
>>> 1 in s
True
>>> for x in s:
...     print(x)
... 
(2, ('jsdksjk', 90))
1
2
(2, 3)
djksjds
```

Les opération ensemblistes classiques sont supportées par des opérateurs :

----------------------------------------------------
Opération ensembliste    Symbole      Opérateur
----------------------- ------------ ---------------
Union                   $\cup$       `|`

Intersection            $\cap$       `&`

Différence              $\setminus$  `-`

Différence symmétrique  $\Delta$     `^`
----------------------------------------------------

Ainsi, avec 

```python
>>> s1 = {1, 2, 3, 4, 5}
>>> s2 = {4, 5, 6, 7, 8}
```

on obtient

```python
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8}
>>> s1 & s2
{4, 5}
>>> s1 - s2
{1, 2, 3}
>>> s1 ^ s2
{1, 2, 3, 6, 7, 8}
```

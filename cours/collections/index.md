---
title: Collections
author:
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)"
affiliation: "MINES ParisTech, Université PSL"
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

De longueur fixe, non modifiables ("en surface")

```python
>>> 
>>> def f():
...     return "ok", 3.14 # or ("ok", 3.14)
... 
>>> status, value = f()
>>> 
>>> status
'ok'
>>> 
>>> value
3.14
>>> 
>>> result = f()
>>> 
>>> result
('ok', 3.14)
>>> 
>>> type(result)
<class 'tuple'>
>>> 
>>> a = 1, 2
>>> 
>>> b = (1, 2)
>>> 
>>> a == b
True
>>> 
>>> empty_tuple = ()
>>> 
>>> type(empty_tuple)
<class 'tuple'>
>>> 
>>> len_1_tuple = (1,)
>>> 
>>> len_1_tuple
(1,)
>>> 
>>> (((1)))
1
>>> 
>>> t = (1, 2)
>>> t[0] = 2.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> l = [1, 2, 3]
>>> t = (l, 2, 3, 3)
>>> t
([1, 2, 3], 2, 3, 3)
>>> 
>>> l.append(42)
>>> t
([1, 2, 3, 42], 2, 3, 3)
```


# Ensembles

Un ensemble peut être défini par une suite de litéraux séparés par des virgules 
et entourées par des accolades

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

L'implémentation des ensembles est similaire à celle de dictionnaire 
qui auraient les élements de l'ensemble comme clés et (par exemple) `True` 
comme valeur unique. 

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

Cela permet aussi de comprendre pourquoi seuls les objets hashables peuvent
être utilisés comme éléments d'un ensemble.

```python
>>> s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}
>>> s = {[]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Il est possible d'ajouter des éléments à un ensemble, d'en retirer, de tester
si un objet appartient à l'ensemble et d'itérer sur les éléments de l'ensemble.

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

---
title: Collections
author:
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris -- PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: today
---

# Listes

Les listes Python sont des collections ordonnées d'objets de type arbitraire.
Elles sont (potentiellement) hétérogènes : il n'est pas nécessaire que le type
de tous les éléments d'une liste soit le même

```python
>>> l = [1.0, True, 2, 3]
```

Les listes sont modifiables ; leurs éléments peuvent être lus et écrits avec
l'opération `l[index]` ; l'indice du premier élément est `0`.
```python
>>> l[1]
True
>>> l
[1.0, True, 2, 3]
>>> l[1] = 42
[1.0, 42, 2, 3]
```

La longueur d'une liste est variable ; on peut en retirer des éléments et
en ajouter, à une position arbitraire dans la liste.
```python
>>> len(l)
3
>>> del l[1]
>>> len(l)
2
>>> l
[1.0, 2, 3]
>>> l.append(12)
>>> l
[1.0, 2, 3, 12]
>>>
>>> l.extend([9, 10, 11, 12])
>>> l
[1.0, 2, 3, 12, 9, 10, 11, 12]
>>> l.insert(True, 0)
>>> l
[True, 1.0, 2, 3, 12, 9, 10, 11, 12]
```
Un indice négatif `i` sera interpété comme l'indice `len(l) + i`. 
En particulier, le dernier élement d'une liste peut être désigné par l'indice `-1`.

```python
>>> l[-1]
12
```

Il est possible de **dépiler** (🇺🇸 **pop**) un élément d'une liste, c'est-à-dire
de l'enlever de la liste et de récupérer sa valeur. Par défaut, c'est le dernier
élément de la liste qui est dépilé, mais cela est configurable.

```python
>>> l.pop()
12
>>> l
[1.0, 2, 3, 12, 9, 10, 11]
>>> l.pop(0)
1.0
>>> l
[2, 3, 12, 9, 10, 11]
```

Il est possible de localiser, compter et enlever les éléments d'une liste
possédant une valeur donnée.

```python
>>> l
[2, 3, 12, 9, 10, 11]
>>> l.remove(9)
>>> l
[2, 3, 12, 10, 11]
>>> l.index(10)
3
>>> l.count(63)
0
```

On peut créer une liste résulant de la concaténation de deux listes.

```python
>>> l
[1, 2, 3, 4]
>>> l1 = [1, 2]
>>> l2 = [3, 4]
>>> l3 = l1 + l2
>>> l1
[1, 2]
>>> l2
[3, 4]
>>> l3
[1, 2, 3, 4]
```

L'opération `extend` réalise la même opération, à ceci près qu'elle modifie
la liste à étendre plutôt que de créer une nouvelle liste.

```python
>>> l3 = l1.extend(l2)
>>> l1
[1, 2, 3, 4]
>>> l2
[3, 4]
>>> l3 is None
True
```

La mutiplication d'une liste par un entier `n` est également définie : elle
produit `n` copies de la liste initiale qui sont concaténées.

```python
>>>
>>> 3 * [7, 1]
[7, 1, 7, 1, 7, 1]
```

La boucle `for` permet d'itérer sur tous les éléments d'une liste.

```python
>>> l = [1, 2, 3, 4]
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
```

Une séquence d' entiers entre `0` et `n-1` est produite par `range(n)`.
Ce n'est toutefois pas une liste classique, mais une liste paresseuse, dont les valeurs
sont produites à la demande, ce qui permet d'économiser de la mémoire.
On peut néanmoins la convertir sans difficulté en une liste classique si
le besoin s'en fait sentir.

```python
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

⚠️ Attention aux listes partageant des objets modifiables ... par exemple des listes !
Ce sont les références aux objets qui sont stockés dans les listes, pas
les objets eux-mêmes ; en modifiant un élément d'une liste, on modifie
donc également toute liste dont il est élément.

```python
>>> l = [[1, 2], [3, 4]]
>>> elt = l[0]
>>> elt
[1, 2]
>>> elt.append(42)
>>> elt
[1, 2, 42]
>>> l
[[1, 3, 42], [3, 4]]
```

# Dictionnaires

Les **dictionnaires** (🇺🇸 **dictionaries**) Python sont des structures de 
données qui associent à des clés (🇺🇸 **keys**) des valeurs (🇺🇸 **values**).
On parle dans d'autre langages de tableaux associatifs (🇺🇸 **associative
arrays**) ou en référence à leur implémentation, de **tables de hachage** 
(🇺🇸 **hash tables**).


Le dictionnaire Python représentant les associations suivantes

-----------------------
clé     $\to$   valeur
------ ------- --------
`"a"`   $\to$   `1`

`"b"`   $\to$   `2`

`"c"`   $\to$   `3`
-----------------------

peut être défini par l'instruction

```python
>>> d = {"a": 1, "b": 2, "c": 3}
```

Les données d'un dictionaire peuvent être lues, écrites et effacées :

```python
>>> d["a"]
1
>>> d
{'a': 1, 'b': 2, 'c': 3}
>>> d["d"] = 4
>>> d
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> del d["a"]
>>> d
{'b': 2, 'c': 3, 'd': 4}
```

Accéder à une clé manquante avec la notation `[]` génère une erreur

```python
>>> d["a"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
```

mais la méthode `get` des dictionnaires permet de renvoyer la valeur 
associée à la clé demandée si la clé est présente et `None` dans
le cas contraire.

```python
>>> d.get("b")
2
>>> d.get("a")
```

On peut également spécifier une autre valeur de repli que `None` si besoin :

```python
>>> d.get("b", 0)
2
>>> d.get("a", 0)
0
```

Pour les dictionnaires, les tests d'appartenance et l'itération ne concernent
que les clés et pas les valeurs :

```python
>>> "a" in d
False
>>> "b" in d
True
>>> for k in d:
...     print(k)
... 
b
c
d
>>> list(d)
['b', 'c', 'd']
```

Cela n'est toutefois que le comportement par défaut : les méthodes `keys`,
`values` et `items` permettent de choisir plus précisément sur quels objets
du dictionnaire on souhaite itérer.

```python
>>> for k in d.keys():
...     print(k)
... 
b
c
d
>>> list(d.keys())
['b', 'c', 'd']
```

```python
>>> for v in d.values():
...     print(v)
... 
2
3
4
>>> list(d.values())
[2, 3, 4]
```

```python
>>> for k, v in d.items():
...     print(k, v)
... 
b 2
c 3
d 4
>>> list(d.items())
[('b', 2), ('c', 3), ('d', 4)]
```

Il existe des méthodes d'importance moindre qui sont parfois utiles.
Par exemple `update` permet d'ajouter / modifier plusieurs associations
clés-valeurs à un dictionnaire ou `pop` qui permet de lire la valeur associée
à une clé avant de la retirer du dictionnaire.

```python
>>> d
{'b': 2, 'c': 3, 'd': 4}
>>> d.update({"e": 5, "f": 6})
>>> d
{'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
>>> d.pop("b")
2
>>> d
{'c': 3, 'd': 4, 'e': 5, 'f': 6}
```

La palme de la complexité revient à l'infâme méthode `setdefault`
dont la description est la suivante :

> `setdefault(d, key, default=None)`
>
> Insert `key` in the dictionary `d` with a value of `default` if key is not in `d`.
>
> Return the value for key if key is in the dictionary, else default.


Plus important : les clés ne sont pas nécessairement des chaînes de caractères
ou les valeurs des nombres :

```python
>>> import math
>>> {math.pi: 90.0}
{3.141592653589793: 90.0}
>>> {1: 4.0, 2.0: 8, False: "yep"}
{1: 4.0, 2.0: 8, False: 'yep'}
>>> {(1, 2): 7, (7, 8, 9): 9}
{(1, 2): 7, (7, 8, 9): 9}
>>> {(1, ("aa", "bb")): 90}
{(1, ('aa', 'bb')): 90}
```

Il n'y a en fait aucune restriction sur le type des valeurs que vous pouvez
stocker dans un dictionnaire. Par contre, les clés doivent être **hachable**
(🇺🇸 **hashable**), ce qui n'est par exemple pas le cas des listes :

```python
>>> {[2]: 90.0}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> hash([2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

C'est le cas de la plupart des types atomiques immuables de Python

```python
>>> hash(None)
5891579141320
>>> hash(False)
0
>>> hash(42)
42
>>> hash(math.pi)
326490430436040707
>>> hash("Hello!")
3339764772054024462
```

ainsi que des [N-uplets] eux-mêmes composés d'objets hashables

```python
>>> hash((None, False, 42, math.pi, "Hello!"))
>>> hash((0, (1, (2, (3, ())))))
>>> hash((1, 2, [3]))
>>> hash((1, 2, [3]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

<details>
<summary>
**Pourquoi cette restriction ? 🤔**
</summary>
Pour des raisons de performance ! En effet les tables de hachage 
permettent (sous certains hypothèses) d'accéder aux valeurs en un temps qui 
ne dépend pas du nombre d'éléments dans la structure, cf. par exemple
[l'article Wikipédia qui y est consacré](https://fr.wikipedia.org/wiki/Table_de_hachage). 
A l'inverse, l'implémentation des tableaux associatifs dans une structure plus simple, 
comme la liste de liste `[["a", 1], ["b": 2], ["c": 3]]` conduirait à une augmentation 
linéaire en fonction du nombre d'élements dans la structure.
</details>

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
met entre parenthèses cette suite. Au lieu du code initial, nous aurions très
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
>>> (1) # ⚠️ not a tuple!
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

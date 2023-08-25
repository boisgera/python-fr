---
title: Itération & compréhension
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: aujourd'hui
---

# Itération

On appelle **itération** (🇺🇸 **iteration**) le processus qui consiste à 
obtenir les éléments d'une collection les uns après les autres. 
C'est par example ce qui est à l'oeuvre dans une boucle for 

``` python
for i in [1, 2, 3]:
    print(i)
```

ou dans les expressions

```python
>>> s = set([1, 2, 3])
```

et 

```python
>>> m = max([0, 1, -1, 2, -2])
```

Le point de départ est toujours un objet **itérable** (🇺🇸 **iterable**),
c'est-à-dire capable de produire à la demande des **itérateurs** (🇺🇸 **iterators**),
qui génèrent les élements désirés.

Le protocole qui permet d'exploiter itérables et itérateurs exploite les 
fonctions `iter` et `next` selon le schéma suivant :

```python
>>> iterable = [1, 2, 3]
>>> iterator = iter(iterable)
>>> next(iterator)
1
>>> next(iterator)
2
>>> next(iterator)
3
>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Notez que l'itérateur ci-dessus "épuise" progressivement l'itérable dont il
est issu, jusqu'à générer une erreur ; il n'est alors plus utilisable pour
parcourir la liste. Mais il est bien sûr d'en produire un nouveau avec la
fonction `iter` et l'itérable de départ.

La boucle for envisagée plus haut exploite ce protocole. 
Elle est en fait équivalente au code suivant :

```python
iterator = iter([1, 2, 3])
while True:
    try:
        i = next(iterator)
        print(i)
    except StopIteration:
        break
```

⚠️ Ne pas modifier une collection pendant son itération ! Le résultat serait
indéfini.

Au lieu d'itérer la liste `l` dont on retire progressivement les 
éléments

```python
l = [1, 2, 3]
for i in l:
    print(i)
    l.remove(i)
```

on préférera en itérer une copie

```python
l = [1, 2, 3]
for i in l.copy():
    print(i)
    l.remove(i)
```

# Itérables classiques

Sont itérables en particulier :

  - les listes

  - les ensembles

  - les dictionnaires  

  - les chaînes de caractères

  - les fichiers

  - etc.

Il existe également des fonctions produisant des itérables, en particulier

  - `range`
  
  - `enumerate`

  - `zip`

Démonstration !

```python
>>> range(10)
range(0, 10)
>>> for i in range(10):
...     print(i)
... 
0
1
2
3
4
5
6
7
8
9
```

```python
>>> enumerate([6, 7, 8]) # doctest: +ELLIPSIS
<enumerate object at 0x...>
>>> for i, number in enumerate([6, 7, 8]):
...     print(i, number)
... 
0 6
1 7
2 8
```

```python
>>> l1 = [1, 2, 3]
>>> l2 = [4, 8, 16]
>>> for item in zip(l1, l2):
...     print(item)
... 
(1, 4)
(2, 8)
(3, 16)
```

# Compréhensions

Les **listes en compréhension** ou pour faire court les **compréhensions**
(🇺🇸 **list comprehensions / comprehensions**) sont une alternative
plus compacte aux boucles pour construire des listes.

Par exemple, pour construire la liste des carrés des entiers de la liste :

```python
integers = [1, 2, 3]
```
on peut soit utiliser une boucle for :

```python
>>> squares = []
>>> for i in integers:
...     square = i * i
...     squares.append(square)
...
>>> squares
[1, 4, 9]
```

soit utiliser la compréhension

```python
>>> [i*i for i in integers]
>>>
[1, 4, 9]
```

Il est également possible de sélectionner les éléments que l'on conserve :

```python
>>> def is_even(i):
...     return i % 2 == 0
...
>>> integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [i for i in integers if is_even(i)]
[0, 2, 4, 6, 8]
```

Les ensembles et les dictionnaires ont également leur compréhensions :

```python
>>> {i*i for i in [0, 1, 2, 3] if i != 0}
{1, 4, 9}
>>> {i: i*i for i in [0, 1, 2, 3] if i != 0}
{1: 1, 2: 4, 3: 9}
```

# Expressions génératrices

Le calcul

```python
>>> max([i*i for i in range(10)])
81
```

a nécessité d'allouer la liste `[x*x for x in range(10)]` alors même que
`range(10)` est un itérable paresseux, qui ne produit de valeurs qu'au fur
et à mesure, sans nécessiter une telle allocation de mémoire.

On pourrait calculer le maximum nous-même en étant plus économe

```python
>>> square_max = -1
>>> for i in range(10):
...     square = i*i
...     if square > square_max:
...         square_max = square
>>> square_max
81  
```

mais la construction suivante, qui utilise une **expression génératrice**
(🇺🇸 **generation expression**) est très similaire à notre code initial
mais n'a pas l'inconvénient de celui-ci

```python
>>> max((x*x for x in range(10)))
81
```

L'expression `(x*x for x in range(10))`
est un itérable qui produit ses valeurs au fur et à mesure. Dans le contexte
d'utilisation ci-dessus, on peut même faire l'économie des parenthèses
décrivant l'expression et se contenter d'écrire

```python
>>> max(x*x for x in range(10))
81
```

Cela n'est toutefois pas vrai dans tous les contextes ; on a ainsi
 
```python
>>> x*x for x in range(10)
  File "<stdin>", line 1
    x*x for x in range(10)
        ^
SyntaxError: invalid syntax
```

mais 

```python
>>> (x*x for x in range(10)) # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>
```




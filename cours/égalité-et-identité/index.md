---
title: Egalité et identité
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
---

### Comparaison

Les objets Python peuvent être comparés au moyen des opérateurs `==` (égal)
et `!=` (différents).

``` python
>>> 0 == 0
True
>>> 0 == 1
False
>>> "A" == "A"
True
>>> "A" == "B"
False
>>> [1, 2, 3] == [1, 2, 3]
True
>>> [1, 2, 3] == [4, 5, 6]
False
```

### Egalité et identité

L'**égalité** de `x` et `y` est testée par l'opérateur `==` :

``` python
x == y
```

Leur **identité** est testée avec le mot-clé `is` :

``` python
x is y
```

La négation de ces propriétés sont testées par `!=` et `is not` :


``` python
x != y
```

``` python
x is not y
```


#### ℹ️ Terminologie {.details}
- On pourra utiliser le terme **est égal à** pour affirmer l'égalité entre objets
et tout simplement **est** pour affirmer qu'ils ont la même identité 
(utiliser le terme "identique" serait ici un contre-sens).

- L'égalité entre objets est parfois appelée **égalité structurelle**
et l'identité entre objets **égalité référentielle**.

####

L'identité `x is y` signifie que les variables `x` et `y` réfèrent au même
objet Python : les données sont à la même adresse en mémoire. Une copie
parfaite d'un objet aura donc une identité différente de l'originale,
alors qu'il sera considéré égal à l'original. Par contre, si deux objets
sont identiques (au sens de : ont la même identité, sont un seul est unique
objet), alors ils sont nécessairement égaux.

####

A titre d'exemple, considérons les trois listes `a`, `b` et `c` :

``` python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> c = b
```

Les listes `a` et `b` sont égales, ainsi que `b` et `c`, mais ne sont pas
identiques, elles ne désignent pas le même objet (en mémoire) ;
les variables `b` et `c` par contre désignent le même objet :

``` python
>>> a == b
True
>>> b == c
True
>>> a is b
False
>>> b is c
True
```

On peut s'assurer que les variables `b` et `c` désignent le même objet en 
évaluant l'**identifiant** de ces objets (un entier) avec la fonction `id` :

```
>>> id(a)
140636096399680
>>> id(b)
140636098130688
>>> id(c)
140636098130688
>>> id(a) == id(b)
False
>>> id(b) == id(c)
True
```

Une conséquence importante de cette distinction : les modifications de la liste
(désignée par) `b` vont impacter la liste `c` (qui est le même objet), mais
pas la liste `a` (qui est un objet distinct) :

``` python
>>> b.append(4)
>>> b
[1, 2, 3, 4]
>>> c
[1, 2, 3, 4]
>>> a
[1, 2, 3]
```

#### ⚠️ `x is not y` $\neq$ `x is (not y)`  {.details}

Bien qu'étant composé de deux mot-clés séparés par un espace, `is not` est
un opérateur en tant que tel. L'expression `x is not y` est équivalente
à `not (x is y)` ... mais plus lisible ! Si l'on a besoin d'utiliser
`is` et `not` comme des opérateurs distincts, pour signifier `x is (not y)`,
il conviendra de garder les parenthèses. Ainsi, avec

``` python
>>> x = 1
>>> y = True
```

on a 

```
>>> x is not y
True
>>> x is y
False
>>> not (x is y)
True
```

mais

``` python
>>> not y
False
>>> x is (not y)
False
```

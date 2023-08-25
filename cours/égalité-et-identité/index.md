---
title: Egalité et identité
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
---

# Egalité

L'expression `x == y` détermine si les objets `x` et `y` sont égaux :

``` python
>>> 0 == 0
True
>>> 0 == 1
False
```


``` python
>>> "Hello!" == "Hello!"
True
>>> "Hello" == "World"
False
```

``` python
>>> [1, 2, 3] == [1, 2, 3]
True
>>> [1, 2, 3] == [4, 5, 6]
False
```

Les tests d'égalité en Python dépendent du type des objets comparés :
il n'y a pas d'interprétation totalement universelle de `==` ; il faut
se reporter à la documentation des types concernés. 
Vous pourrez d'ailleurs décider quel sens donner aux égalités des
types que vous serez amenés à définir.

#### 🤔 Comment interpréter `x == y` si les types de `x` et `y` sont différents ? {.details}

Si le type de `y` est un sous-type du type de `x`, il détermine en priorité 
quel sens donner à `==` ; dans le cas contraire c'est le type de `x` auquel 
est donné la priorité.

Source: [📖  Méthodes de comparaison riches](https://docs.python.org/fr/3/reference/datamodel.html#object.__eq__)

## Nombres

Le test d'égalité de nombres se passe sans grande surprise
si l'on laisse de coté certains propriétés des [nombres (à virgule flottante) spéciaux](#IEEE754).

Notons simplement que les test d'égalité entre nombres sont suffisamment permissifs
pour permettre de comparer des nombres dont le type est différent :

``` python
>>> 1 == True
True
>>> 1 == 1.0
True
>>> 1 == 1 + 0j
True
```

#### Egalité des nombres à virgule flottante {#IEEE754 .details}

Le nombres à virgule flottante (`float`) de Python sont de précision finie.
Par conséquent des erreurs d'arrondi dans les calculs peuvent faire échouer
les tests d'égalité. Ainsi, on a par exemple :

``` python
>>> 0.1 + 0.2 == 0.3
False
```

car l'addition a introduit une (petite) erreur dans le calcul :

``` python
>>> 0.1 + 0.2
0.30000000000000004
```

Le standard IEEE 754 régit la représentation et le calcul des nombres
flottants. Il introduit des nombres spéciaux ; il y a ainsi deux zéros 
distincts ($0^+$ et $0^-$) mais considérés égaux :

``` python
>>> +0.0
0.0
>>> -0.0
-0.0
>>> +0.0 == -0.0
True
```

Plus surprenant, le "non-nombre" `nan` (🇺🇸: **not a number**) est une valeur spéciale 
... qui n'est pas égale à elle-même ! (Tous les "non-nombres" sont réputés différents.)

``` python
>>> from math import nan
>>> nan == nan
False
```

Il faudra utiliser la fonction `isnan` pour savoir si une valeur est un 
non-nombre.

``` python
>>> from math import isnan
>>> isnan(nan)
True
```

Source: [📖 Standard IEEE 754](https://fr.wikipedia.org/wiki/IEEE_754)

## Collections 

Deux collections -- listes, n-uplets, dictionnaires, ensembles, etc. 
-- délèguent le test d'égalité aux éléments qui les composent 
-- récursivement si ceux-ci sont également des collections.
Ainsi :

``` python
>>> [] == [0]
False
>>> [0] == [0]
True
>>> [0] == [1]
False
>>> [0] == [0, 0]
False
>>> [0] == [0.0]
True
>>> [[0]] == [[0.0]]
True
```

Pour les dictionnaires : 

``` python
>>> {"a": 1, "b": 2} == {"a": 1, "b": 2}
True
```

et

``` python
>>> {"a": 1, "b": 2} == {"a": 1.0, "b": 2.0}
True
```


L'ordre des couples clés-valeurs n'a pas d'importance

``` python
>>> {"a": 1, "b": 2} == {"b": 2, "a": 1}
True
```

mais il suffit qu'une clé ou qu'une valeur diffère dans les deux collections
comparées pour invalider l'égalité :

``` python
>>> {"a": 1, "b": 2} == {"a": 1, "b": 2, "c": 3}
False
>>> {"a": 1, "b": 2} == {"a": 2, "b": 1}
False
```


## Chaînes de caractères

La comparaison des chaînes de caractères se passe la plupart du temps
comme on s'y attend :

```python
>>> "Hello" == "Hello"
True
>>> "Hello" == "Halo"
False
```

A ceci près que dans le standard unicode il y a parfois plusieurs façons
d'obtenir visuellement le même caractère. Il y a ainsi un caractère 
"e accent aigu"

```python
>>> "\xe9"
'é'
```

mais aussi un symbole "accent aigu" qu'on peut combiner à un "e" :

```python
>>> "e\u0301"
'é'
```

Les deux séquences de code points sont différentes, donc les deux chaînes de
caractères sont considérées comme différentes :

```python
>>> "\xe9" == "e\u0301"
False
```

C'est toutefois beaucoup plus surprenant quand le test est effectué sous la
forme suivante :

```python
>>> "é" == "é"
False
```

# Identité

L'expression `x is y` détermine si l'objet `x` **est** l'objet `y`,
à la même **identité**

``` python
x is y
```

La négation de `==` est `!=`, celle de `is` est `is not` :


``` python
x != y
```

``` python
x is not y
```


#### ℹ️ Terminologie {.details}
- On pourra utiliser le terme **est égal à** pour affirmer l'égalité entre objets
et tout simplement **est** pour affirmer qu'ils ont la même identité 
(utiliser le terme "identique" serait trompeur).

- L'égalité entre objets est parfois appelée **égalité structurelle**
et l'identité entre objets **égalité référentielle**.

####

L'identité `x is y` signifie que les variables `x` et `y` réfèrent au même
objet Python : les données sont à la même adresse en mémoire. Une copie
parfaite d'un objet aura donc une identité différente de l'originale,
alors qu'il sera considéré égal à l'original. Par contre, si deux objets
sont identiques (au sens de : ont la même identité, sont un seul est unique
objet), alors ils sont nécessairement égaux.

### Egalité et identité

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

#### ⚠️ `x is not y` n'est pas la même chose que `x is (not y)`  {.details}

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

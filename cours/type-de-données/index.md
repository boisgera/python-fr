---
title: Types de données
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: today
---

# Absence de valeur

Python fournit une valeur `None` qui signale ... l'absence de valeur !
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

Par contre on peut explicitement afficher `None`, par exemple avec la fonction `print` :

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

Attention, une variable affectée à `None` ; une variable indéfinie (qui n'est
liée à aucune valeur) c'est (subtilement) différent. Si la variable `y` n'a pas
encore été introduite (ou a été effacée avec `del y`),
 l'évaluation de l'expression `y is None` provoque une erreur

```python
>>> y is None
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
```

comme d'ailleurs toute expression qui utilise `y` :

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

## Usages

### Fonctions sans valeur de retour

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
c'est la pause dans le programme. Utilisons cette fonction dans notre
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

### Fonction avec valeur de retour optionnelle

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
auxiliaire qui permet de renvoyer une valeur particulière en cas d'échec.
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

### Fonction et absence d'argument

La valeur `None` est souvent utilisée comme valeur par défaut
associée à l'argument d'une fonction. Ne pas affecter (explicitement) de
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
du module `warnings` permettent de controller ce comportement.

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
doit renvoyer un "non-nombre" ($\bot$ c'est-à-dire `nan`), faites en sorte que le mécanisme
de gestion des avertissements et erreurs de NumPy les ignore.

```python
>>> _ = np.seterr(divide="ignore")
>>> one / zero
inf
```

Si ce résultat vous convient, mais que vous souhaitez une erreur en cas de
**dépassement** (🇺🇸 **overflow**) (sous-entendu : du plus grand nombre flottant fini),
vous pouvez invoquer `seterr` en conséquence :

```python
>>> _ = np.seterr(overflow="raise")
>>> np.float64(2.0) ** 10000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FloatingPointError: overflow encountered in double_scalars
```

La documentation de `seterr` nous apprend que la fonction a 5 arguments, 
qui ont tous la valeur par défaut `None`. 
Les appels successifs que nous avons fait à `seterr`

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


# Types numériques

## Booléens

On peut considérer que les booléens `True` et `False` sont de valeurs numériques.
Ils se combinent au moyen d'opérateurs logiques et sont principalement exploités 
dans des tests qui contrôlent le flux d'exécution des programmes.

```python
>>> not False
True
>>> not True
False
```

```python
>>> False or False
False
>>> False or True
True
>>> True or False
True
>>> True or True
True
```

```python
>>> False and False
False
>>> False and True
False
>>> True and False
False
>>> True and True
True
```

## Entiers

Les entiers Python sont des nombres dotés d'un signe et n'ayant pas de limite
de taille (autre que celle fixée par la mémoire de votre ordinateur !).
Ils supportent les opérations de calcul classiques : addition `+`, 
multiplication `*`, puissance `**`, etc.

``` python
>>> -1
-1
>>> 1 + 3 * 2
7
>>> 2**8
256
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

Il est possible de calculer le reste et le quotient d'une division euclidienne
de deux entiers.

```python
>>> 17 % 12
5
>>> 17 // 2
8
>>> 17 / 12
1.4166666666666667
```

Même si leur description privilégiée est décimale, les entiers Python 
peuvent également être représentés ou définis sous forme binaire
ou hexadécimale :

```python
>>> bin(42)
'0b101010'
>>> hex(42)
'0x2a'
>>> 0b101010
42
>>> 0x2a
42
>>> 0b101010 == 0x2a == 42
True
```

## Nombres flottants

Les nombres flottants -- ou **à virgule flottante** -- permettent de représenter
des valeur numériques non entières, comme $e$ ou $\pi$ :

```python
>>> from math import e, pi
>>> e
2.718281828459045
>>> pi
3.141592653589793
```

On peut convertir un nombre flottant en une approximation entière avec `int`,
mais cela ne garantit pas que l'on obtienne l'entier le plus proche.
Pour cela il faudra utiliser la fonction `round`.
```python
>>> int(pi)
3
>>> int(e)
2
>>> round(pi)
3
>>> round(e)
3
```

Il est également possible d'obtenir des approximations "dirigées" à
l'entier directement inférieur ou supérieur au nombre flottant.
```python 
>>> import math
>>> math.floor(pi)
3
>>> math.ceil(pi)
4
```

Une caractéristique majeure des nombres flottants est qu'il sont une 
représentation de précision finie des nombres réels et que les calculs
effectués avec eux induisent donc (a priori) des erreurs :
```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
>>> math.sin(pi)
1.2246467991473532e-16
>>> math.sin(pi) == 0.0
False
```

Si nécessaire on peut obtenir la représentation réelle d'un nombre flottant, 
ce qui n'est pas ce qui est affiché par défaut :

```python
>>> print(0.1)
0.1
>>> print(f"{0.1:.1000}")
0.1000000000000000055511151231257827021181583404541015625
>>> print(0.2)
0.2
>>> print(f"{0.2:.1000}")
0.200000000000000011102230246251565404236316680908203125
>>> print(0.3)
0.3
>>> print(f"{0.3:.1000}")
'0.299999999999999988897769753748434595763683319091796875'
>>> print(0.1+0.2)
0.30000000000000004
>>> print(f"{0.1+0.2:.1000}")
0.3000000000000000444089209850062616169452667236328125
```

Les nombres flottants comportent également des valeurs spéciales : $\infty$ 
(l'infini)
et $\bot$ (nombre indéfini / 🇺🇸 **not-a-number**) :

```python
>>> from math import inf, nan
>>> inf
inf
>>> -inf
-inf
>>> inf + 1.0
inf
>>> inf - inf
nan
>>>> nan + inf
nan
```
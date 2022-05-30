---
title: Portée des variables
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
---

# Introduction

Pour savoir quelle valeur référence un identifiant Python dans un endroit donné
du code, il est nécessaire de comprendre la notion de **portée** (🇺🇸 **scope**)
d'une variable. Il existe quatre portées distinctes en Python.

# Variables globales

La fonction `dir`, utilisée sans argument, liste les variables définies dans
la portée globale de l'interpréteur ou d'un programme Python.

``` python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
```

On constate ici que 7 variables sont prédéfinies dans l'interpréteur et l'on
peut afficher leurs valeurs:

``` python
>>> __annotations__
{}
>>> __builtins__
<module 'builtins' (built-in)>
>>> __doc__
>>> __loader__
<class '_frozen_importlib.BuiltinImporter'>
>>> __name__
'__main__'
>>> __package__
>>> __spec__
```

En définissant une nouvelle variables globale `a`, on change le résultat de 
`dir()`.

```python
>>> a = 1
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a']
```

Pour éviter de voir les valeurs prédéfinies, ici sans intérêt, on filtre les
noms de variables qui commencent et finissent par un double caractère de 
soulignement.

```python
>>> def is_dunder(name):
...     return name.startswith("__") and name.endswith("__")
... 
>>> [name for name in dir() if not is_dunder(name)]
['a', 'is_dunder']
```

Notons que la fonction nouvellement définie `is_dunder` est également listée.
Il est possible d'introduire de nouvelles variables et ensuite de les faire
disparaître au moyen du mot-clé `del`.

```
>>> b = 42
>>> [name for name in dir() if not is_dunder(name)]
['a', 'b', 'is_dunder']
>>> del a
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> [name for name in dir() if not is_dunder(name)]
['b', 'is_dunder']
```

#### `globals`

Si l'on est intéressé non pas par uniquement le nom des variables globales
mais aussi par les valeurs auquelles elles se réfèrent, la fonction `globals`
fournit un dictionnaire contenant les deux informations.

```python
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'b': 42, 'is_dunder': <function is_dunder at 0x7f29d337b760>}
```

A nouveau, on peut éliminer de cette structure les variables prédéfinies.

```
>>> globs = {name: value for name, value in globals().items() if not is_dunder(name)}
>>> globs
{'b': 42, 'is_dunder': <function is_dunder at 0x7f29d337b760>}
```

Les ajouts ou supression de variables peuvent se faire soit directement,
soit en modifiant le dictionnaire des variables globales

```
>>> a = 1
>>> globs["a"]
1
>>> del globs["a"]
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> globs["c"] = 22
>>> c
22
```

# Variables locales

Invoqué dans une fonction, `dir()` liste les variables **locales** (à la fonction).

```python
>>> def f():
...     print(dir())
... 
>>> f()
[]
```

```python
>>> def f():
...     a = 1
...     print(dir())
... 
>>> f()
['a']
```

Sur l'exemple précédent, `a` n'est pas définie comme une variable globale
mais bien locale à la fonction.

```python
>>> def f():
...     a = 1
...     print("a" in globals())
... 
>>> f()
False
```

```python
>>> def f():
...     a = 1
...     print("a" in locals())
... 
>>> f()
True
```

```python
>>> def f():
...     a = 1
...     print(locals())
... 
>>> f()
{'a': 1}
```

Contrairement au cas des variables globales, on ne peut pas modifier
les variables locales en modifiant le dictionnaire produit par `locals()`.

```python
>>> def f():
...     a = 1
...     locals()["a"] = 2
...     print(a)
... 
>>> f()
1
```

#### ℹ️ Comportement indéfini de `locals()` {.details}

Pour être précis, les conséquences d'une mise à jour du dictionnaire `locals()`
peuvent dépendre de l'interpréteur Python utilisé. Pour l'interpréteur Python 
"classique" (CPython), ces mises à jour n'ont aucun effet. 
L'aide de la fonction `locals` est explicite :

> locals() returns a dictionary containing the current scope's local variables.
>  
> NOTE: Whether or not updates to this dictionary will affect name lookups in
> the local scope and vice-versa is *implementation dependent* and not
> covered by any backwards compatibility guarantees.


#### 

Les paramètres des fonctions font partie de ses variables locales.

``` python
>>> def f(b):
...     a = 1
...     print(locals())
... 
>>> f(7)
{'b': 7, 'a': 1}
```

Les variables globales sont accessibles en lecture depuis le code de la fonction ...

```python
>>> c = 2
>>> def f(b):
...     a = 1
...     print(a, b, c)
... 
>>> f(7)
1 7 2
```

... mais pas en écriture ...

```python
>>> def f():
...     c = 3
...     print(c)
... 
>>> f()
3
>>> c
2
```

... sauf si elles sont explicitement déclarées comme globales, au moyen du 
mot-clé `global`.

```python
>>> def f():
...     global c
...     c = 3
...     print(c)
... 
>>> c
2
>>> f()
3
>>> c
3
```

En présence de "conflit" et en l'absence de mot-clé `global`, dans le code de
la fonction, les variables sont considérées locales.

```python
>>> c = 3
>>> def f():
...     c = 2
...     print(locals())
... 
>>> f()
{'c': 2}
```

Dans ce cas on dit que la variable locale **cache** (🇺🇸 **shadows**) la
variable globale.

# Variables intégrées

Certaines variables sont prédéfinies, mais n'appartiennent pas à la portée
globale, mais à une portée encore plus fondamentale, la portée **intégrée** 
(🇺🇸 **built-in**).

C'est par exemple le cas de la fonction `print`.

```python
>>> print
<built-in function print>
>>> print(42)
42
```

On ne peut pas effacer une variable intégrée aussi simplement qu'une variable
globale.

```python
>>> del print
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print' is not defined
>>> print(42)
42
```

Il est techniquement possible de cacher une variable intégrée par une 
variable globale (même si cela n'est sans doute pas une bonne idée).

```python
>>> print = 9
>>> print(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> print
9
```

La variable intégrée sera de nouveau accessible si on se débarasse de la variable
globale.

```python
>>> del print
>>> print(42)
42
```

Si vous souhaitez vraiment faire disparaître définitivement une variable
intégrée (toujours pas une bonne idée), cela est possible en modifiant 
le dictionnaire `__dict__` du module `builtin`.

``` python
>>> import builtins
>>> "print" in builtins.__dict__
True
>>> builtins.__dict__["print"]
<built-in function print>
>>> del builtins.__dict__["print"]
>>> print
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print' is not defined
>>> print(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print' is not defined
```

# Variables non-locales

Il est possible de définir une fonction dans une fonction. La fonction interne
a accès aux variables définies dans la fonction englobante -- variables
qualifiées de **non-locales** -- en lecture seule,
ainsi qu'aux variables globales qui ne sont pas cachées par ces variables
(ainsi qu'au variables intégrées qui ne sont cachées par aucune autre portée).
Pour accéder à ces variables non-locales en écriture, il faudra les déclarer
explicitement au moyen du mot-clé `nonlocal`.

```python
>>> def f():
...     a = 1
...     def g():
...        nonlocal a
...        a = 3
...     g()
...     print(a)
... 
>>> f()
3
```
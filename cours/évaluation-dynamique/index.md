---
title: Evaluation dynamique de code
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
---

Le langage Python permet l'exécution dynamique de code. La fonction `exec`
permet d'exécuter des **instructions** (🇺🇸 : **statements**) :

``` python
>>> exec("print('Hello world!')")
Hello world!
```

et la fonction `eval` d'évaluer des **expressions** (🇺🇸 : **expressions**) :

``` python
>>> eval("1+1")
2
```

Dans de nombreux cas, évaluer la représentation d'un objet Python sous forme
de chaînes de caractères génère un objet identique à l'objet original. 
Par exemple :

``` python
>>> one = 1
>>> repr(one)
'1'
>>> eval(repr(one))
1
>>> eval(repr(one)) == one
True
```

ou encore 

``` python
>>> hello = "Hello world!"
>>> repr(hello)
"'Hello world!'"
>>> eval(repr(hello))
'Hello world!"
>>> eval(repr(hello)) == hello
True
``` 

et 

``` python
>>> numbers = [1, 2, 3]
>>> repr(numbers)
'[1, 2, 3]'
>>> eval(repr(numbers))
[1, 2, 3]
>>> eval(repr(numbers)) == numbers
True
```

Ce n'est toutefois pas une règle universelle. 

#### Contre-exemples {.details}

La représentation d'un objet fonction par exemple ne permet pas sa reconstruction :

``` python
>>> def f():
...     pass
... 
>>> repr(f)
'<function f at 0x7f9bd685f640>'
>>> eval(repr(f))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    <function f at 0x7f9bd685f640>
    ^
SyntaxError: invalid syntax
```

Mais il est possible de trouver un contre-exemple en utilisant uniquement les
listes :

``` python
>>> loop  = []
>>> loop.append(loop)  # Ooooooh ! 🤯
>>> repr(loop)
'[[...]]'
>>> ...
Ellipsis
>>> eval(repr(loop))
[[Ellipsis]]
>>> loop2 = eval(repr(loop))
>>> loop2[0] 
[Ellipsis]
>>> loop2[0] == loop2
False
```

#### ⚠️ Dangers {.details}

L'utilisation de `eval` et `exec` est souvent découragée en pratique.
En particulier, l'exécution de code inconnu (et donc potentiellement malveillant) 
est susceptible de faire de gros dégats ; par exemple si votre programme
Python, s'exécutant sur votre serveur, exécute une chaîne de caractères 
fournie par son utilisateur distant, et que celui-ci fournit

``` python
code = 'import os\nwhile True:\n\tprint(os.popen(input("$ ")).read())'
```

Alors il dispose alors d'un accès complet au terminal de votre serveur ... 
Il peut donc très facilement ajouter des fichiers, lire des fichiers locaux et 
les transférer leur contenu par le réseau, éteindre l'ordinateur, etc.


####

Les options plus avancées de `exec` et `eval` sont détaillées dans la
documentation de la bibliothèque standard Python :

  - 📖 [exec](https://docs.python.org/3/library/functions.html#exec)

  - 📖 [eval](https://docs.python.org/3/library/functions.html#eval)


---
title: Texte et binaire
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: today
---


## Chaînes de caractères

Les chaînes de caractères Python sont définies comme des suites de caractères 
[Unicode] délimités par les caractères `'` ou `"`.

[Unicode]: https://fr.wikipedia.org/wiki/Unicode

```python
>>> s = "Hello world! 👋"
>>> s
'Hello world! 👋'
```

Le choix de la 🇺🇸 **simple quote** ou de la 🇺🇸 **double quote** est la plupart
du temps indifférent. Préférez la double quote quand votre texte comporte
des simples quotes (ou apostrophes) et réciproquement :

```python
>>> 'Je n'ai pas compris!'
  File "<stdin>", line 1
    'Je n'ai pas compris!'
          ^
SyntaxError: invalid syntax
>>> "J'ai compris!"
"J'ai compris!"

```

Les caractères précédés d'un slash (`\`) sont interprétés comme des
**séquences d'échappement** (🇺🇸 **escape sequences**) et non pas litéralement.
Ainsi `"\n"` est un retour à la ligne, `"\t"` une tabulation

```python
>>> print("a\nb")
a
b
>>> print("a\tb")
a	b
```

`\\` un slash (et oui !), `\'`  une simple quote et `\"` une double quote,

```python
>>> print("\\")
\
>>> print('J\'ai compris!')
J'ai compris!
```

etc.

Un caractère Unicode est caractérisé par un 🇺🇸 [**code point**](https://en.wikipedia.org/wiki/Code_point), un entier le plus souvent représenté sous la forme "U+????????" où les `?` sont
des caractères hécadécimaux ; ce qui se traduit en Python par
`\U????????`. Par exemple :

```python
>>> ord("a")
97
>>> hex(97)
'0x61'
>>> "\U00000061"
'a'
```

Lorsqu'il suffit de quatre ou deux caractères hexadécimaux pour décrire le 
code point, on peut utiliser les syntaxes `\u????` ou `\x??` qui sont plus
compactes

```python
>>> "\u0061"
'a'
>>> "\x61"
'a'
```

Les émojis par exemple nécessitent la syntaxe la plus longue :

```
>>> "smiley: \U0001f600"
'smiley: 😀'
>>> 
>>> "pile of poo: \U0001f4a9"
'pile of poo: 💩'
```


Le chaînes de caractères se comportement également comme des collections
(immuables) de caractères ... même s'il n'existe pas de type "caractère" ! 
(Un "caractère" est en fait représenté comme une chaîne de caractères
de longueur 1.)

```python
>>> s = "Hello world! 👋"
>>> len(s)
14
>>> s[0]
'H'
>>> s[-1]
'👋'
>>> s[0:5]
'Hello'
>>> s[:5] + s[5:]
'Hello world! 👋'
>>> for c in s:
...     print(c) 
... 
H
e
l
l
o
 
w
o
r
l
d
!
 
👋
>>> list(s)
['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!', ' ', '👋']
```

Les **f-strings** permettent d'insérer au sein de chaînes de caractères
des chaînes de caractères stockées dans des variables

```python
>>> target = "world"
>>> emoji = "👋"
>>> f"Hello {target} {emoji}"
'Hello world 👋'
```

ou bien des données qui peuvent être représentées comme des chaînes de 
caractères, ou bien même des expressions qui s'évaluent en de tels objets

```python
>>> f"1+1 = {1+1}"
'1+1 = 2'
```

```python
>>> ok = True
>>> f"Annie are you ok? {'yep' if ok else 'nope'}."
'Annie are you ok? yep.'
>>> ok = False
>>> f"Annie are you ok? {'yep' if ok else 'nope'}."
'Annie are you ok? nope.'
```

# Données binaires

les **octets** Python (🇺🇸 **bytes**) sont des suites de valeurs entières
comprises entre 0 et 255 qui représentent des données binaires arbitraires.
Elle sont le plus fréquemment représentées sous une forme analogue aux
chaînes de caractères, mais préfixées par un `b` :

```python
>>> b"Hello world!"
b'Hello world!'
```

Néanmoins, seul les caractères ASCII sont autorisés

```python
>>> b"Hello world! 👋"
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
```

Pour décrire des octets qui ne correspondent pas à des caractères ASCII, 
on peut utiliser la **syntaxe d'échappement** (🇺🇸 **escape sequence**)
`\x??` ou les `?` représentent un caractère hexadécimal.

```python
>>> b"Hello world! \xf0\x9f\x91\x8b"
b'Hello world! \xf0\x9f\x91\x8b'
```

Il est aussi possible d'utiliser la syntaxe d'échappement à la place des
caractères ASCII

```python
>>> b"\x48\x65\x6C\x6c\x6f\x20\x77\x6f\x72\x6c\x64\x21\x20\xf0\x9f\x91\x8b"
b'Hello world! \xf0\x9f\x91\x8b'
```

Les octets peuvent aussi être manipulés comme des listes (mais immuables !)
d'entiers compris entre 0 et 255 

```python
>>> data = b"Hello world! \xf0\x9f\x91\x8b"
>>> data[0]
72
>>> data[0] = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
>>> list(data)
[72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33, 32, 240, 159, 145, 139]
```

D'ailleurs on peut les créer à partir d'une telle liste

```python
>>> bytes([72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33, 32, 240, 159, 145, 139])
b'Hello world! \xf0\x9f\x91\x8b'
```

# Encodage de texte

Pour être stocké dans un fichier ou transmis sur le réseau, une chaîne de
caractères doit être convertie en données binaires. Il existe plusieurs
méthodes pour opérer cette conversion, qu'on appelle un **encodage**
(🇺🇸 **encoding**).
L'encodage UTF-8 est un bon choix par défaut (notamment, parce qu'il est 
compatible avec le vénérable encodage ASCII mais qu'il sait gérer tous les
caractères Unicode).

```python
>>> "Hello world! 👋".encode("utf-8")
b'Hello world! \xf0\x9f\x91\x8b'
```

Il existe d'autres encodages, comme UTF-16, qui produisent des binaires
différents.

```python
>>> "Hello world! 👋".encode("utf-16")
b'\xff\xfeH\x00e\x00l\x00l\x00o\x00 \x00w\x00o\x00r\x00l\x00d\x00!\x00 \x00=\xd8K\xdc'
```

L'opération inverse est le **décodage** (🇺🇸 **decoding**) des données binaires 
en chaînes de caractères

```python
>>> b'Hello world! \xf0\x9f\x91\x8b'.decode("utf-8")
'Hello world! 👋'
```
Vous noterez qu'il faut savoir quel encodage a été utilisé pour décoder
correcter les données binaires. Si l'on se trompe, le résultat peut être
déplaisant ...

```python
>>> "Sébastien".encode("utf-8").decode("cp1252")
'SÃ©bastien'
```

Tous les encodages ne permettent pas de décrire tous les caractères du standard
Unicode (mais UTF-8, UTF-16 et UTF-32 le permettent).

```python
>>> "Sébastien".encode("ascii")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 1: ordinal not in range(128)
>>> "Sébastien".encode("cp1252")
b'S\xe9bastien'
>>> "Hello world! 👋".encode("cp1252")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/boisgera/miniconda3/envs/python-fr/lib/python3.9/encodings/cp1252.py", line 12, in encode
    return codecs.charmap_encode(input,errors,encoding_table)
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f44b' in position 13: character maps to <undefined>
```

# Fichiers

Pour ouvrir un fichier afin d'y écrire du texte, vous pouvez utiliser le
mode `"w"` (pour "write")

``` python
>>> file = open("texte.txt", mode="w")
>>> file.write("Hello world! 👋")
```

mais cela n'est pas nécessairement une bonne idée, car Python va alors
décider par lui-même de l'encodage utilisé pour convertir votre texte en
données binaires. Il va pour cela utiliser l'encodage déclaré par votre
environnement (et encore, si tout va bien ...). Sur ma machine, 
coup de chance, il s'agit d'UTF-8, et ce choix me convient

```python
>>> import locale
>>> locale.getpreferredencoding(False)
'UTF-8'
```

mais rien ne dit que ce soit la même chose sur votre machine. Si nous devons
ensuite partager les fichiers texte avec d'autres personne, 
il faut être en mesure de savoir comment ils sont encodés, ou mieux encore, 
de choisir quel encodage est utilisé. 
Le plus sage consiste à spécifier systématiquement et explicitement quel 
encodage vous souhaitez utiliser.

``` python
>>> file = open("texte.txt", mode="w", encoding="utf-8")
>>> file.write("Hello world! 👋")
```

C'est aussi une bonne habitude de fermer le fichier après usage[^fermeture]

[^fermeture]: Il est possible que l'écriture dans le fichier soit temporisée
et n'ait lieu qu'à la fermeture du fichier. Il est aussi possible que 
l'ouverture du fichier "bloque" aux autres processus l'accès au même fichier,
etc.

``` python
>>> file = open("texte.txt", mode="w", encoding="utf-8")
>>> file.write("Hello world! 👋")
>>> file.close()
```

Pour autant, si vous insérez du code Python entre l'ouverture et la fermeture
du fichier et que ce code peut échouer (par exemple, s'il n'y a plus de place
sur votre disque dur pour écrire `"Hello world! 👋"`), 
l'instruction de fermeture du fichier ne sera jamais exécutée. 
Une version plus robuste consisterait à fermer le fichier dans tous les cas
(erreur ou non), ce qui peut être fait de la façon suivante :

```python
>>> file = open("texte.txt", mode="w", encoding="utf-8")
>>> try:
...     file.write("Hello world! 👋")
... finally:
...     file.close()
...
```

... mais c'est un peu lourd ! Heureusement pour nous, il existe une construction
plus compacte qui offre les mêmes garanties :

```python
>>> with open("texte.txt", mode="w", encoding="utf-8") as file:
...     file.write("Hello world! 👋")
...
```

L'écriture dans un fichier, se fait de façon analogue avec le mode `"r"`
(pour "read").

```python
>>> with open("texte.txt", mode="r", encoding="utf-8") as file:
...     print(file.read())
...
Hello world! 👋
```

Enfin, sachez que le mode `"r"` est interprété comme `"rt"` (et `"w"` comme `"wt"`),
ou `"t"` signifie "texte" : la fonction `open` sait alors qu'elle doit lire ou
écrire du texte. On peut donc être tout à fait explicite en écrivant :
```python
>>> with open("texte.txt", mode="rt", encoding="utf-8") as file:
...     print(file.read())
...
Hello world! 👋
```

Mais, si vous voulez accéder à des données qui ne sont pas du 
**texte en clair** (🇺🇸 **plain text**) comme une image ou un document PDF, 
ou bien du texte que vous décoderez vous-même, utilisez le mode
"binaire" `"b"` (en lecture comme en écriture) :

```python
>>> with open("texte.txt", mode="rb") as file:
...     data = file.read()
...     print(f"{type(data) = }")
...     text = data.decode("utf-8")
...     print(text)
...
type(data) = <class 'bytes'>
Hello world! 👋
```

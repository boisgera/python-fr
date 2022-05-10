---
title: Texte et binaire
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: today
---


## Chaînes de caractères

```python
>>> r = 'kldskdmlskdms'
>>> 
>>> "j'utilise des apostrophes"
"j'utilise des apostrophes"
>>> 
>>> 'j' + "'" + 'utilise des apostrophes'
"j'utilise des apostrophes"
>>> 
>>> 'j\'utilise des apostrophes'
"j'utilise des apostrophes"
>>> 
>>> print("a\nb")
a
b
>>> 
>>> print("a\tb")
a	b
>>> 
>>> print("\\")
\
>>> 
>>> s = "\\"
>>> ord(s)
92
>>> 
>>> hex(92)
'0x5c'
>>> 
>>> print("le slash est: \x5c")
le slash est: \
>>> 
>>> hex(ord("a")) # ascii code of "a"
'0x61'
>>> 
>>> print("la lettre a: \x61")
la lettre a: a
>>> 
>>> print("smiley: \U0001f600")
smiley: 😀
>>> 
>>> print("\U0001f4a9")
💩
>>> 
>>> s = "kjdslkdjslkdsljdlksdjdslkdjs -------------------- hhhhhhhh"
>>> 
>>> s[0:5] + s[-5:]
'kjdslhhhhh'
>>> 
>>> len(s)
58
>>> 
>>> for c in s:
...     print(c)
... 
k
j
d
s
l
k
d
j
s
l
k
d
s
l
j
d
l
k
s
d
j
d
s
l
k
d
j
s
 
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
 
h
h
h
h
h
h
h
h
>>> s = "Sébastien"
```

# Données binaires

`bytes` & stuff ...

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

L'opération inverse est le **décodage** (**decoding** 🇺🇸) des données binaires 
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
Unicode (mais UTF-8, UTF-16 et UTF-16 le permettent).

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

``` python


file = open("texte.txt", mode="w", encoding="utf-8")

file.write("Sébastien")

file.close()

f = open("texte.txt", mode="r", encoding="utf-8")

f.read()

f = open("texte.txt", mode="br") # binary mode

data = f.read()
data

data.decode("utf-8")

```

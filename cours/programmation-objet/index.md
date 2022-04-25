---
title: Programmation Orientée Objet
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: auto
---

# Usage des objets

## Des objets partout !

Avant de découvrir comment utiliser les objets, il est bon de se convaincre que 
cette compétence sera très utile en Python, car :

> Tout ce qui peut être désigné par une variable est un objet !

Techniquement : "est une **instance** du type `object`".


<details><summary>
#### Instance ?
</summary>
Un terme à interpréter dans sa version anglo-saxonne où il peut signifier
"an individual illustrative of a category". On pourra se représenter 
un **type** comme une collection d'éléments : ses instances.

--------------------------------------------------------------------------------

</details>




Entiers, booléens, chaînes de caractère, listes, sont donc
des objets :

```python
>>> isinstance(42, object)
True
>>> isinstance(True, object)
True
>>> isinstance("Hello!", object)
True
>>> isinstance([1, 2, 3], object)
True
```

<details><summary>
#### 🤔 Alors `42` serait un objet, pas un entier? 
</summary>

Mais si car les deux sont possibles simultanément ! 
Nous avons déjà constaté que `42` était bien un objet :
```python
>>> isinstance(42, object)
True
```
Vérifions que c'est également un entier :
```python
>>> isinstance(42, int)
True
```
Donc les deux propriétés ne sont pas contradictoires.
Plus précisément, le type de `42` est entier, pas objet :
```python
>>> type(42) == int
True
```
mais comme  entier est un sous-type d'objet
```python
>>> issubclass(int, object)
True
```
tous les entiers sont aussi des objets.

--------------------------------------------------------------------------------

</details>


Bien que cela soit peut-être moins intuitif, des fonctions, des types ou des 
modules sont aussi des objets :

```python
>>> isinstance(print, object)
True 
>>> isinstance(int, object)
True
>>> import sys; isinstance(sys, object)
True
```

## Des nombres pas si complexes

Le type `complex` représente en Python les nombres complexes. 
Il fournit un bon example des interactions qu'on peut avoir avec des objets.

### Construction

Pour créer le nombre complexe $z = 1/2 + (3/2)i$, on peut utiliser la notation
litérale pour les nombres complexes :

```python
>>> z = 0.5 + 1.5j
```

Il est bon de connaître cette syntaxe car c'est celle que Python utilisera 
pour représenter les nombres complexes:

```python
>>> z
(0.5+1.5j)
```

Néanmoins tous les objets ne sont pas dotés d'une telle notation.
Mais il existe une méthode alternative pour tous les objets :
on peut appeler le type de l'objet que l'on souhaite instancier 
(comme s'il était une fonction) en lui passant les arguments nécessaires, ici partie
réelle et imaginaire du nombre à construire. 
Le type de l'objet sert donc de **constructeur**.

```python
>>> z = complex(0.5, 1.5)
>>> z == 0.5+1.5j
True
```

### Attributs

Un objet est une structure de données. Les données qu'il contient 
peuvent être rendus accessible sous forme d'**attributs**. 
Tous nombres complexes possèdent ainsi les attributs `real` et `imag` :

```python
>>> z.real
0.5
>>> z.imag
1.5
```

La syntaxe pour changer la valeur de l'attribut `real` du nombre `z`
devrait être `z.real = ...`. Ici toutefois un tel assignement échoue parce 
que les nombres complexes sont (volontairement) immuables.

```python
>>> z.real = -0.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: readonly attribute
```

### Méthodes

Un nombre complexe possède un attribut `conjugate` dont la nature est un peu
particulière, une **méthode** :

```python
>>> z.conjugate #doctest: +ELLIPSIS
<built-in method conjugate of complex object at 0x...>
```

Les méthodes, qui se comportent comme les fonctions, sont appelables :

```
>>> callable(z.conjugate)
True
```

Cette méthode est **liée** au nombre complexe `z` : elle peut utiliser 
`z` et les données qu'il contient pour produire un résultat, sans qu'il soit 
nécessaire de lui passer explicitement `z` comme argument. 
Ici, `z.conjugate()` renvoie le nombre complexe conjugé de `z`:

```python
>>> z.conjugate()
(0.5-1.5j)
```

La méthode `conjugate` est également disponible comme attribut du type `complex`:

```python
>>> complex.conjugate
<method 'conjugate' of 'complex' objects>
```

Elle n'est alors par liée à une instance particulière de nombre complexe ;
il faudra donc lui fournir explicitement le nombre complexe à conjuguer en
argument :

```python
>>> complex.conjugate(z)
(0.5-1.5j)
```

### Méthodes magiques

Sont **magiques** les méthodes d'un objet dont le nom commence et finit
par un double soulignement `"__"`. Ces méthodes magiques sont rarement
appelées directement par le programmeur, mais indirectement par Python
lui-même. 

Les méthodes magiques du type `complex` permettent par exemple de faire
des calculs avec des nombres complexes avec une syntaxe concise : s'il est
possible de calculer

```python
>>> 1j + 1j * 1j
(-1+1j)
```

c'est que le type complex comporte les méthodes magiques `__add__` et `__mul__`,
appelées en cas d'addition et de multiplication respectivement. Le calcul
ci-dessus est donc équivalent à :

```python
>>> complex.__add__(1j, complex.__mul__(1j, 1j))
(-1+1j)
```

ou bien, en utilisant la version liée de ces méthodes :

```python
>>> 1j.__add__(1j.__mul__(1j))
(-1+1j)
```

Dans tous les cas, la notation initiale 
-- où l'on laisse le soin à Python d'appeler lui-même les méthodes magiques --
est sensiblement plus lisible !

# Conception de types

Notre objectif dans cette section va être de créer un type `Complex` qui va
être une version simplifié du type intégré `complex`. Nous allons pour cela
définir une nouvelle **classe**; pour créer une classe minimale, sans
fonctionnalité spécifique, le code ci-dessous suffit :

```python
class Complex:
    pass
```

A ce stade, il est certe possible d'instancier un "nombre complexe" 

```python
>>> z = Complex()
```

ayant le bon type

```python
>>> type(z) is Complex
True
>>> isinstance(z, Complex)
True
```

mais il n'est doté d'aucun attribut ou méthode caractéristique 
des nombres complexes

```python
>>> z.real
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Complex' object has no attribute 'real'
>>> z.conjugate()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Complex' object has no attribute 'conjugate'
>>> z + z
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'
```

## Constructeur & Attributs

Pour gérer l'ajout des attributs `real` et `imag`, on pourrait définir une
fonction 

```python
def Complex_init(z, real, imag):
    z.real = real
    z.imag = imag
```

qui nous permettrait de prendre un nombre complexe vide et d'y ajouter les
attributs souhaités :

```python
>>> z = Complex()
>>> Complex_init(z, 0.5, 1.5)
>>> z.real
0.5
>>> z.imag
1.5
```

Possible oui, mais pas pratique ! En définissant directement la fonction
précédente dans la classe `Complex`, et en la nommant `__init__`, 
on définit une méthode magique qui est le constructeur associé à la classe
`Complex` et on s'évite cet usage maladroit.

En adoptant la définition suivante de `Complex`

```python
class Complex:
    def __init__(z, real, imag):
        z.real = real
        z.imag = imag
```

on peut s'épargner la création d'un objet sans attributs, pris automatiquement
en charge quand on appelle le constructeur de nombres complexes

```python
>>> z = Complex(0.5, 1.5)
>>> z.real
0.5
>>> z.imag
1.5
```

L'usage quand une telle méthode est définie est d'appeler `self` le premier
argument de la méthode, qui désignera toujours une instance de la classe
considérée

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
```

C'est uniquement une convention, qui ne change rien au comportement de la classe
que nous avions définie.


## Méthodes

L'ajout de méthodes à une classe suit le même schéma que le constructeur.
Ainsi pour avoir une méthode `conjugate` qui retourne le conjugée d'une
instance de nombre complexe, on peut faire

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex(self.real, -self.imag)
```

Avec

```python
>>> z = Complex(0.5, 1.5)
```

on a alors

```python
>>> w = Complex.conjugate(z)
>>> w.real
0.5
>>> w.imag
1.5
```

ou bien, puisque Python prend en charge automatiquement la création de
méthodes liées aux instances

```python
>>> w = z.conjugate()
>>> w.real
0.5
>>> w.imag
1.5
```

## Méthodes magiques

Il est un peu frustrant de ne pas voir les nombres complexes s'afficher
proprement dans le terminal à ce stade :

```python
>>> Complex(0.5, 1.5) # doctest: +ELLIPSIS
<__main__.Complex object at 0x...>
```

C'est un problème que nous pouvons résoudre en définissant une méthode magique
`__repr__`, chargée de construire une représentation adaptée des instances
sous forme de chaîne de caractères.

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex(self.real, -self.imag)
    def __repr__(self):
        # ⚠️ weird output when self.imag < 0
        return f"({self.real}+{self.imag}j")
```

On a alors une représentation compatible avec la notation litérale
des nombres complexes intégrés

```python
>>> Complex(0.5, 1.5)
(0.5+1.5j)
```

Le support des opérations arithmétiques est similaire. Pour disposer de 
l'addition par exemple, on peut faire :

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex(self.real, -self.imag)
    def __repr__(self):
        # ⚠️ weird output when self.imag < 0
        return f"({self.real}+{self.imag}j")
    def __add__(w, z):
        return Complex(w.real+z.real, w.imag+z.imag)
```

et alors

```python
>>> z = Complex(0.5, 1.5)
>>> z + z.conjugate()
(1+0j)
```

A noter que pour ce type de méthodes, qui accepte deux instances de la
classe en argument, l'usage est d'utiliser les noms `self` et `other`
et donc de préférer la définition suivante (équivalente) :

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex(self.real, -self.imag)
    def __repr__(self):
        # ⚠️ weird output when self.imag < 0
        return f"({self.real}+{self.imag}j")
    def __add__(self, other):
        return Complex(
            self.real + other.real, 
            self.imag + other.imag
        )
```

## 🚧 TODO: attributs privés, propriétés 🚧

# Objectification (Examples)

```
class Snake:
    def __init__(self, geometry, direction):
        self.geometry = geometry
        self.direction = direction
    def __iter__(self):
        return iter(self.geometry)
    def __len__(self):
        return len(self.geometry)
    def __getitem__(self, index):
        return self.geometry[index]
    def __eq__(self, other):
        return (isinstance(other, Snake) and self.geometry == other.geometry and self.direction == other.direction)
    

geometry = [(10, 15), (11, 15), (12, 15)]
direction = (0, 1)
snake = Snake(geometry, direction)

snake

for (x, y) in snake:
    print(x, y)

(10, 15) in snake

len(snake)

snake[0]

geometry = [(10, 15), (11, 15), (12, 15)]
direction = (0, 1)
snake == Snake(geometry, direction)

fruit = (10, 10)

_state = None

class GameState:
    def __init__(self, snake, fruit):
        self.snake = snake
        self.fruit = fruit
        
    def save(self):
        global _state
        _state = (self.snake, self.fruit)
        
    def load(): # does not depend on self
        snake = _state[0]
        fruit = _state[1]
        return GameState(snake, fruit)
    
    load = staticmethod(load)

_state = None

class GameState:
    def __init__(self, snake, fruit):
        self.snake = snake
        self.fruit = fruit
        
    def save(self):
        global _state
        _state = (self.snake, self.fruit)

    @staticmethod # decorator ; equivalent to load = staticmethod(load)
    def load(): # does not depend on self
        snake = _state[0]
        fruit = _state[1]
        return GameState(snake, fruit)

state = GameState(snake, fruit)

state.fruit = (12, 12)

_state

state.save()

_state

state.fruit = (0, 0)

state2 = state.load()

state = GameState.load()

state.fruit

Héritage

_state = None

class GameState2: # sans héritage
    def __init__(self, snake, fruit, score):
        self.snake = snake
        self.fruit = fruit
        self.score = score
        
    def save(self):
        global _state
        _state = (self.snake, self.fruit, self.score)

    @staticmethod # decorator ; equivalent to load = staticmethod(load)
    def load(): # does not depend on self
        snake = _state[0]
        fruit = _state[1]
        score = _state[2]
        return GameState2(snake, fruit, score)
    

class GameState2(GameState): # avec héritage: GameState2 dérive de GameState
    def __init__(self, snake, fruit, score):
        super().__init__(snake, fruit) # stocke snake et fruit en attributs
        self.score = score
    def save(self):
        global _state
        super().save() # _state == (snake, fruit)
        #state_list = list(_state)
        #state_list.append(self.score)
        #_state = tuple(state_list)
        # shorter:
        _state = _state + (self.score,)
    @staticmethod # decorator ; equivalent to load = staticmethod(load)
    def load(): # does not depend on self
        state1 = GameState.load()
        snake = state1.snake
        fruit = state1.fruit
        score = _state[2]
        return GameState2(snake, fruit, score)

score = 12
state = GameState2(snake, fruit, score)

state.snake, state.fruit, state.score

state.save()

_state

state2 = GameState2.load()

state2.snake

state2.fruit

state2.score

Accesseurs, Variables privées, etc.

import copy

class Snake:
    def __init__(self, geometry, direction):
        self._geometry = geometry
        self._direction = direction
    def get_geometry(self):
        print("GET")
        return copy.copy(self._geometry)
    def set_geometry(self, geometry):
        print("SET")
        # TODO: ajout validation de geometry
        self._geometry = copy.copy(geometry)
    geometry = property(get_geometry, set_geometry)    
        
    def get_score(self):
        return len(self)
    score = property(get_score) # read-only, virtual property
    
        
    def __iter__(self):
        return iter(self.geometry)
    def __len__(self):
        return len(self.geometry)
    def __getitem__(self, index):
        return self.geometry[index]
    def __eq__(self, other):
        return (isinstance(other, Snake) and self.geometry == other.geometry and self.direction == other.direction)
    
class GameState:
    def __init__(self, snake, fruit):
        self.snake = snake
        self.fruit = fruit

geometry = [(10, 15), (11, 15), (12, 15)]
direction = (0, 1)
snake = Snake(geometry, direction)

snake._geometry # ça marche mais _ indique que par convention, seules les méthodes Snake devraient accéder à cet attribut
# attribut privé

snake.get_geometry()

geometry = snake.get_geometry()

geometry[0] = None # pas de corruption de la variable snake._geometry grace à la copie !!!

snake.get_geometry()

snake.set_geometry([(0, 0), (0, 1)])

snake.get_geometry()

snake.geometry = [(3, 3)]

snake.geometry

snake.score

snake.score = 999

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/tmp/ipykernel_34619/2459733161.py in <module>
----> 1 snake.score = 999

AttributeError: can't set attribute

help(copy)
```


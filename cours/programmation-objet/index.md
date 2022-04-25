---
title: Programmation Orientée Objet
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: auto
---

# Découvert et Usage des Objets


## Everything is an object!

```python
>>> isinstance(1, object)
True
>>> isinstance(True, object)
True
>>> isinstance("jkjskjdks", object)
True
>>> isinstance([1, 2, 3], object)
True
>>> 
>>> def f(x):
...     pass
...
>>> isinstance(f, object)
True 
>>> import sys
>>> isinstance(sys, object)
True
```

## Complex Numbers

``` python
z = 1.0 - 2.0j

z

z = complex(1.0, -2.0) # construction / initialisation d'un complexe / instanciation du type complex
z

z.real # accès aux attributs (ic "real")

z.real = 3.14 # ici "real" accessible en lecture seule

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/tmp/ipykernel_73815/1104530040.py in <module>
----> 1 z.real = 3.14 # ici "real" accessible en lecture seule

AttributeError: readonly attribute

z.conjugate() # appel de méthode

w = 1j

w * z
```

# Création de Classes

## Complex numbers without objects

``` python
z = (1.0, -2.0)

def complex_get_real(z):
    return z[0]

complex_get_real(z)

def complex_conjugate(z):
    x, y = z
    return (x, -y)

complex_conjugate(z)

def complex_multiply(w, z):
    ...
    pass
```

Our own complex class

``` python
import builtins
complex = builtins.complex

class Complex:
    pass

complex = Complex() # instance of Complex (default constructor only)

Complex(1.0, -2.0)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_73815/2989908829.py in <module>
----> 1 Complex(1.0, -2.0)

TypeError: Complex() takes no arguments

class Complex:
    def init(complex, real, imag):
        complex.real = real
        complex.imag = imag

complex = Complex()
Complex.init(complex, 1.0, -2.0)

complex.real

complex.imag

class Complex:
    def __init__(complex, real, imag):
        complex.real = real
        complex.imag = imag

z = Complex(1.0, -2.0)

z.real

z.imag

class Complex:
    def __init__(complex, real, imag):
        complex.real = real
        complex.imag = imag
    def conjugate_inplace(complex): # mutable version of conjugate
        complex.imag = -complex.imag

z = Complex(1.0, -2.0)
Complex.conjugate_inplace(z)
z.real, z.imag

z = Complex(1.0, -2.0)
z.conjugate_inplace() # méthode liée ("bound method")
z.real, z.imag

class Complex:
    def __init__(complex, real, imag):
        complex.real = real
        complex.imag = imag
    def conjugate(complex):
        return Complex(complex.real, -complex.imag)

z = Complex(1.0, -2.0)
w = z.conjugate()
w.real, w.imag

complex(1.0, 2.0) # eq to print(repr(complex(1.0, 2.0)))

Complex(1.0, 2.0)

print(repr(complex(1.0, 2.0))) # repr uses the dunder method __repr__ if it exist!

w = Complex(1.0, 2.0)
isinstance(w, Complex)

isinstance(w, object)

issubclass(Complex, object)

dir(Complex)

Complex.__repr__

object.__repr__

print(object.__repr__(w))

w

class Complex:
    def __init__(complex, real, imag):
        complex.real = real
        complex.imag = imag
    def conjugate(complex):
        return Complex(complex.real, -complex.imag)
    def __repr__(complex):
        return f"({complex.real}+{complex.imag}j)" # doesn't alway work (e.g. when complex.imag < 0)

w = Complex(1.0, 2.0)

w

class Complex: # usual convention: denote "self" the current instance
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex(self.real, -self.imag)
    def __repr__(self):
        return f"({self.real}+{self.imag}j)" # doesn't alway work (e.g. when complex.imag < 0)

w = Complex(1.0, 2.0)
w

class Complex: # usual convention: denote "self" the current instance
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex(self.real, -self.imag)
    def __repr__(self):
        return f"({self.real}+{self.imag}j)" # doesn't alway work (e.g. when complex.imag < 0)
    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

w = Complex(1.0, 2.0)
z = Complex(0.0, 1.0)

Complex.add(w, z) # usage d'une méthode non-liée (à une instance)

w.add(z) # usage d'une méthode liée (à l'instance w)

w + z

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_73815/2317218533.py in <module>
----> 1 w + z

TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'

class Complex: # usual convention: denote "self" the current instance
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex(self.real, -self.imag)
    def __repr__(self):
        return f"({self.real}+{self.imag}j)" # doesn't alway work (e.g. when complex.imag < 0)
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

w = Complex(1.0, 2.0)
z = Complex(0.0, 1.0)

Complex.__add__(w, z)

w.__add__(z)

w + z

w.real

w.real = -1.0 # nos instances de nombres complexes sont modifiables :(

w.real = "tagad tsoin tsoin" # et ces modifications peuvent le rendre invalide :( :( :(

w

complex(1.0)

Complex(1.0)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_73815/74783907.py in <module>
----> 1 Complex(1.0)

TypeError: __init__() missing 1 required positional argument: 'imag'

class Complex: # usual convention: denote "self" the current instance
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex(self.real, -self.imag)
    def __repr__(self):
        return f"({self.real}+{self.imag}j)" # doesn't alway work (e.g. when complex.imag < 0)
    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

Complex(1.0, 2.0)
Complex(1.0)
```

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


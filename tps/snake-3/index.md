---
title: Le retour du retour du serpent
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris -- PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: auto
---


🕹️ Introduction
================================================================================

Nous allons remanier (à nouveau !) notre programme 🐍 `snake.py`,
en développant une conception orientée objet.
Nous tenterons de rendre son code plus robuste / réutilisable / compréhensible 
/ maintenable. 
Nous tâcherons ensuite de tirer les bénéfices de cette réorganisation 
en développant – avec le minimum d'efforts – 
un 🤖 bot qui assistera le joueur dans la poursuite du high-score. 


<details>
<summary>
**Snake version 2 (rappel)**
</summary>

📄 `snake.py`

```python
# Python Standard Library
import random
import sys

# Third-Party Libraries
import pygame

# Constants
WIDTH = 30  # number of cells
HEIGHT = 30  # number of cells
CELL_SIZE = 20  # number of pixels
FPS = 1  # frames per second
WHITE = [
    255,
    255,
    255,
]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {
    "background": WHITE,
    "snake": BLACK,
    "fruit": RED,
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]
SNAPSHOT = "snapshot.py"

# State Management
snake = [[10, 15], [11, 15], [12, 15]]
direction = DOWN
fruit = [10, 10]
score = 0


def save_state():
    state = {
        "snake": snake,
        "direction": direction,
        "fruit": fruit,
        "score": score,
    }
    with open(SNAPSHOT, mode="w", encoding="utf-8") as file:
        file.write(repr(state))


def load_state():
    global snake, direction, fruit, score
    with open(SNAPSHOT, mode="r", encoding="utf-8") as file:
        data = file.read()
    state = eval(data)
    snake = state["snake"]
    direction = state["direction"]
    fruit = state["fruit"]
    score = state["score"]


# Helpers
def setup():
    pygame.init()
    width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
    screen = pygame.display.set_mode(width_height)
    clock = pygame.time.Clock()
    return (screen, clock)


def exit():
    pygame.quit()
    sys.exit()


def set_direction(d):
    def action():
        global direction
        direction = d

    return action


# Event Management
KEY_BINDINGS = {
    "q": exit,
    "up": set_direction(UP),
    "down": set_direction(DOWN),
    "left": set_direction(LEFT),
    "right": set_direction(RIGHT),
    "s": save_state,
    "l": load_state,
}

KEY_EVENT_HANDLER = {
    pygame.key.key_code(k): v
    for k, v in KEY_BINDINGS.items()
}


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_handler = KEY_EVENT_HANDLER.get(event.key)
            if event_handler:
                event_handler()


def move_snake():
    global fruit, score, snake
    head = snake[-1]
    new_head = [
      head[0] + direction[0],
      head[1] + direction[1]
    ]
    if (
        new_head in snake
        or new_head[0] < 0
        or new_head[0] >= 30
        or new_head[1] < 0
        or new_head[1] >= 30
    ):
        pygame.quit()
        sys.exit()
    if new_head == fruit:
        score = score + 1
        snake = snake + [new_head]
        fruit = [
            random.randint(0, 29),
            random.randint(0, 29)
        ]
    else:
        snake = snake[1:] + [new_head]


def draw_frame(screen):
    screen.fill(COLORS["background"])
    for x, y in snake:
        rect = [
            x * CELL_SIZE,
            y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        ]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [
        fruit[0] * CELL_SIZE,
        fruit[1] * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE,
    ]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")


def wait_for_next_frame(clock):
    clock.tick(FPS)


# Setup & Main Loop
screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock)
```
</details>


🧱 Constantes
================================================================================


🧹 **Nettoyage de printemps !** 
Déplacez la définition des constantes du programme 
(`WIDTH`, `HEIGHT`, `CELL_SIZE`, etc.) dans un fichier `constants.py`,
puis les importer dans `snake.py` avec :

``` python
from constants import *
```

<details>
<summary>
**✨ Solution**
</summary>

📄 `constants.py`
```python
WIDTH = 30  # number of cells
HEIGHT = 30  # number of cells
CELL_SIZE = 20  # number of pixels
FPS = 1  # frames per second
WHITE = [
    255,
    255,
    255,
]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {
    "background": WHITE,
    "snake": BLACK,
    "fruit": RED,
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]
SNAPSHOT = "snapshot.py"
```

📄 `snake.py`
```python
# Python Standard Library
import random
import sys

# Third-Party Libraries
import pygame

# Snake
from constants import *

# State Management
snake = [[10, 15], [11, 15], [12, 15]]
direction = DOWN
fruit = [10, 10]
score = 0


def save_state():
    state = {
        "snake": snake,
        "direction": direction,
        "fruit": fruit,
        "score": score,
    }
    with open(SNAPSHOT, mode="w", encoding="utf-8") as file:
        file.write(repr(state))


def load_state():
    global snake, direction, fruit, score
    with open(SNAPSHOT, mode="r", encoding="utf-8") as file:
        data = file.read()
    state = eval(data)
    snake = state["snake"]
    direction = state["direction"]
    fruit = state["fruit"]
    score = state["score"]


# Helpers
def setup():
    pygame.init()
    width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
    screen = pygame.display.set_mode(width_height)
    clock = pygame.time.Clock()
    return (screen, clock)


def exit():
    pygame.quit()
    sys.exit()


def set_direction(d):
    def action():
        global direction
        direction = d

    return action


# Event Management
KEY_BINDINGS = {
    "q": exit,
    "up": set_direction(UP),
    "down": set_direction(DOWN),
    "left": set_direction(LEFT),
    "right": set_direction(RIGHT),
    "s": save_state,
    "l": load_state,
}

KEY_EVENT_HANDLER = {
    pygame.key.key_code(k): v
    for k, v in KEY_BINDINGS.items()
}


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_handler = KEY_EVENT_HANDLER.get(event.key)
            if event_handler:
                event_handler()


def move_snake():
    global fruit, score, snake
    head = snake[-1]
    new_head = [
      head[0] + direction[0],
      head[1] + direction[1]
    ]
    if (
        new_head in snake
        or new_head[0] < 0
        or new_head[0] >= 30
        or new_head[1] < 0
        or new_head[1] >= 30
    ):
        pygame.quit()
        sys.exit()
    if new_head == fruit:
        score = score + 1
        snake = snake + [new_head]
        fruit = [
            random.randint(0, 29),
            random.randint(0, 29)
        ]
    else:
        snake = snake[1:] + [new_head]


def draw_frame(screen):
    screen.fill(COLORS["background"])
    for x, y in snake:
        rect = [
            x * CELL_SIZE,
            y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        ]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [
        fruit[0] * CELL_SIZE,
        fruit[1] * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE,
    ]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")


def wait_for_next_frame(clock):
    clock.tick(FPS)

# Setup & Main Loop
screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock)
```
</details>

🐍 Un type `Snake`
================================================================================

On souhaite créer un type `Snake` qui va regrouper toutes les données propres
au serpent ainsi que les fonctions qui interagissent avec lui.

  - Implémentez une classe `Snake` encapsulant la géométrie et la direction du
serpent. On veut pouvoir l'instancier comme suit :

    ```python
    >>> geometry = [[10, 15], [11, 15], [12, 15]]
    >>> direction = [0, 1]
    >>> snake = Snake(geometry, direction)
    ```

    Stockez dans un premier temps les arguments `geometry` et `direction` comme 
les attributs de même nom de l'instance snake.

    ```python
    >>> snake.geometry
    [[10, 15], [11, 15], [12, 15]]
    >>> snake.direction
    [0, 1]
    ```

  - Développez un accesseur (en lecture) `get_head`, renvoyant la tête du serpent.

    ```python
    >>> snake.get_head()
    [12, 15]
    ```

  - Exposez cette valeur comme une propriété `head`, accessible uniquement en lecture :

    ```python
    >>> snake.head
    [12, 15]
    ```

    ⚠️ **Encapsulation.** Non seulement on veut que l'attribut `head` du serpent 
    ne puisse pas être réaffecté :

    ```python
    >>> snake.head = [0, 7]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute
    ```

    mais on veut également qu'une modification de la tête récupérée par 
    `snake.head` n'ait pas d'incidence sur l'état du serpent :

    ```python
    >>> head = snake.head
    >>> head[0] = 0
    >>> head[1] = 7
    >>> head
    [0, 7]
    >>> snake.head
    [12, 15]
    ```

<details>
<summary>
**✨ Solution**
</summary>
```python
# Python Standard Library
...
import copy

...

class Snake:
    def __init__(self, geometry, direction):
        self.direction = direction
        self.geometry = geometry

    def get_head(self):
        return copy.copy(self.geometry[-1])

    head = property(get_head)
```
</details>

✔️ Validation
================================================================================

 - Quelles sont les valeurs admissibles pour la direction du serpent ?

  - Implémentez une fonction `check_direction` qui prenne en argument une
direction, ne renvoie rien si la direction est admissible et génère une
exception (de type `ValueError` ou `TypeError`, à déterminer) dans le cas contraire.

De même, toutes les listes de n-uplets représentant la géométrie du serpent 
ne sont pas valides. 

  - Faire la liste des toutes les conditions qui rendent 
la géométrie du serpent invalide ; on distinguera les

    - 🐛 **bugs** qui résultent d'erreurs de programmation 
      et ne devraient dans un monde idéal jamais se produire,
      mais qui en pratique risquent fort d'exister.

    - 💀 **situation exceptionnelles**,
      qui résultent des actions du joueur et doivent entrainer un
      **game over** et l'arrêt de l'application.

  - Mettre en correspondance ces catégories avec un type d'exception (soit
`TypeError`, soit `ValueError`, soit `SystemExit`), puis
implémenter une fonction `check_geometry` qui prenne en argument une 
géométrie de serpent, ne renvoie rien si elle est valide et génère 
l'exception appropriée dans le cas contraire.


<details>
<summary>
**✨ Solution**
</summary>
```python
DIRECTIONS = [RIGHT, DOWN, LEFT, UP]

def check_direction(direction):
    try:
        direction = list(direction)
    except TypeError:
        error = f"{direction} is not list-like"
        raise TypeError(error)
    if (
        len(direction) != 2
        or not isinstance(direction[0], int)
        or not isinstance(direction[1], int)
    ):
        raise TypeError(
            f"{direction} is not a pair of integers"
        )
    elif direction not in DIRECTIONS:
        raise ValueError(
            f"{direction} is not in {DIRECTIONS}"
        )


def is_in_scope(tile):
    x, y = tile
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


def check_geometry(geometry):
    try:
        geometry = list(geometry)
    except TypeError:
        error = f"{geometry} is not list-like"
        raise TypeError(error)
    try:
        geometry = [list(item) for item in geometry]
    except TypeError:
        error = f"{item} is not list-like"
        raise TypeError(error)
    if not all(
        len(item) == 2
        and isinstance(item[0], int)
        and isinstance(item[1], int)
        for item in geometry
    ):
        raise TypeError(
            "all geometry items should be pairs of integers"
        )

    if not geometry:
        raise ValueError("empty geometry")

    for i, item in enumerate(geometry[:-1]):
        next_item = geometry[i + 1]
        diff = (
            next_item[0] - item[0],
            next_item[1] - item[1],
        )
        if abs(diff[0]) + abs(diff[1]) != 1:
            raise ValueError("non-connected snake geometry")

    if not all(is_in_scope(item) for item in geometry):
        raise SystemExit("snake out of bounds")

    for i, elt in enumerate(geometry):
        if elt in geometry[i + 1 :]:
            # at least one repeated item
            raise SystemExit("snake self-collision")
```
</details>


  - A-t'on la garantie que ces attributs restent valides quel que soit l'usage
que le programmeur fasse de l'instance `snake` dans son code ? 

  - Faites
disparaître les attributs publics `geometry` et `direction` au profit
d'attributs privés `_geometry` et `_direction`, puis développez des
méthodes `get_direction` et `set_direction` permettant d'accéder à l'attribut
`_direction` en assurant sa validité 

    ```python
    >>> snake.get_direction()
    [0, 1]
    >>> snake.set_direction([0, -1])
    >>> snake.get_direction()
    [0, -1]
    ```

    ⚠️ **Encapsulation.** Assurez-vous que `set_direction` soit bien la
    seule façon de modifier la direction du serpent. En particulier,
    vérifiez que l'on a bien le comportement ci-dessous :

    ```python
    >>> direction = snake.get_direction()
    >>> direction
    [0, 1]
    >>> direction[0] = 999
    >>> snake.get_direction()
    [0, 1]
    ```

  - Même chose pour `set_geometry`.

  - Enfin, associez aux accesseurs `get_direction`, `set_direction`, 
`get_geometry` et `set_geometry` des propriétés `geometry` et `direction`.

<details>
<summary>
**✨ Solution**
</summary>
```python
import copy

class Snake:
    def __init__(self, geometry, direction):
        self.direction = direction
        self.geometry = geometry

    def get_direction(self):
        return copy.deepcopy(self._direction)

    def set_direction(self, direction):
        check_direction(direction)
        self._direction = copy.deepcopy(direction)

    direction = property(get_direction, set_direction)

    def get_geometry(self):
        return copy.deepcopy(self._geometry)

    def set_geometry(self, geometry):
        check_geometry(geometry)
        self._geometry = copy.deepcopy(geometry)

    geometry = property(get_geometry, set_geometry)

    def get_head(self):
        return self.geometry[-1]

    head = property(get_head)
```

</details>

🏃 En mouvement
================================================================================

  - Introduisez une méthode `move` dans la classe `Snake` qui va mettre à jour
la géométrie du serpent en tenant compte de la direction courante du serpent
et de la position des fruits (à remettre à jour le cas échéant).

  - Adaptez le programme pour intégrer les développements de la classe `Snake`. 
Vérifiez en y jouant que le comportement du jeu reste identique.

<details>
<summary>
**✨ Solution**
</summary>
```python
# Python Standard Library
import copy
import random
import sys

# Third-Party Libraries
import pygame

# Snake
from constants import *


DIRECTIONS = [RIGHT, DOWN, LEFT, UP]


def check_direction(direction):
    try:
        direction = list(direction)
    except TypeError:
        error = f"{direction} is not list-like"
        raise TypeError(error)
    if (
        len(direction) != 2
        or not isinstance(direction[0], int)
        or not isinstance(direction[1], int)
    ):
        raise TypeError(
            f"{direction} is not a pair of integers"
        )
    elif direction not in DIRECTIONS:
        raise ValueError(
            f"{direction} is not in {DIRECTIONS}"
        )


def is_in_scope(tile):
    x, y = tile
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


def check_geometry(geometry):
    try:
        geometry = list(geometry)
    except TypeError:
        error = f"{geometry} is not list-like"
        raise TypeError(error)
    try:
        geometry = [list(item) for item in geometry]
    except TypeError:
        error = f"{item} is not list-like"
        raise TypeError(error)
    if not all(
        len(item) == 2
        and isinstance(item[0], int)
        and isinstance(item[1], int)
        for item in geometry
    ):
        raise TypeError(
            "all geometry items should be pairs of integers"
        )

    if not geometry:
        raise ValueError("empty geometry")

    for i, item in enumerate(geometry[:-1]):
        next_item = geometry[i + 1]
        diff = (
            next_item[0] - item[0],
            next_item[1] - item[1],
        )
        if abs(diff[0]) + abs(diff[1]) != 1:
            raise ValueError("non-connected snake geometry")

    if not all(is_in_scope(item) for item in geometry):
        raise SystemExit("snake out of bounds")

    for i, elt in enumerate(geometry):
        if elt in geometry[i + 1 :]:
            # at least one repeated item
            raise SystemExit("snake self-collision")


class Snake:
    def __init__(self, geometry, direction):
        self.direction = direction
        self.geometry = geometry

    def get_direction(self):
        return copy.deepcopy(self._direction)

    def set_direction(self, direction):
        check_direction(direction)
        self._direction = copy.deepcopy(direction)

    direction = property(get_direction, set_direction)

    def get_geometry(self):
        return copy.deepcopy(self._geometry)

    def set_geometry(self, geometry):
        check_geometry(geometry)
        self._geometry = copy.deepcopy(geometry)

    geometry = property(get_geometry, set_geometry)

    def get_head(self):
        return self.geometry[-1]

    head = property(get_head)

    def move(self):
        global fruit, score
        head = self.head
        new_head = [
            head[0] + self.direction[0],
            head[1] + self.direction[1],
        ]
        if new_head == fruit:
            score += 1
            self.geometry = self.geometry + [new_head]
            fruit = [
                random.randint(0, WIDTH - 1),
                random.randint(0, HEIGHT - 1),
            ]
        else:
            self.geometry = self.geometry[1:] + [new_head]


# State Management
geometry = [[10, 15], [11, 15], [12, 15]]
direction = DOWN
fruit = [10, 10]
score = 0


def save_state():
    state = {
        "geometry": snake.geometry,
        "direction": snake.direction,
        "fruit": fruit,
        "score": score,
    }
    with open(SNAPSHOT, mode="w", encoding="utf-8") as file:
        file.write(repr(state))


def load_state():
    global fruit, score
    with open(SNAPSHOT, mode="r", encoding="utf-8") as file:
        data = file.read()
    state = eval(data)
    snake.geometry = state["geometry"]
    snake.direction = state["direction"]
    fruit = state["fruit"]
    score = state["score"]


# Helpers
def setup():
    pygame.init()
    width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
    screen = pygame.display.set_mode(width_height)
    clock = pygame.time.Clock()
    return (screen, clock)


def set_direction(d):
    def action():
        snake.direction = d

    return action


def exit():
    pygame.quit()
    sys.exit()


# Event Management
KEY_BINDINGS = {
    "q": exit,
    "up": set_direction(UP),
    "down": set_direction(DOWN),
    "left": set_direction(LEFT),
    "right": set_direction(RIGHT),
    "s": save_state,
    "l": load_state,
}

KEY_EVENT_HANDLER = {
    pygame.key.key_code(k): v
    for k, v in KEY_BINDINGS.items()
}


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_handler = KEY_EVENT_HANDLER.get(event.key)
            if event_handler:
                event_handler()


def draw_frame(screen):
    screen.fill(COLORS["background"])
    for x, y in snake.geometry:
        rect = [
            x * CELL_SIZE,
            y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        ]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [
        fruit[0] * CELL_SIZE,
        fruit[1] * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE,
    ]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")


def wait_for_next_frame(clock):
    clock.tick(FPS)


# Setup & Main Loop
screen, clock = setup()
snake = Snake(geometry, direction)
while True:
    handle_events()
    snake.move()
    draw_frame(screen)
    wait_for_next_frame(clock)

```
</details>

🗃️ Etat du jeu
================================================================================

  - Définissez une classe `State` représentant l'état à un instant donné du programme.
    On souhaite pouvoir initialiser cet état par un code de la forme

    ```python
    state = State(
        snake=Snake(
            geometry=[[10, 15], [11, 15], [12, 15]], 
            direction=RIGHT
        ),  
        fruit=[10, 10], 
        score=0
    )
    ```

    et que l'instance `state` expose les attributs `snake`, `fruit` et `score` 
    (en lecture et en écriture). 

  - Adaptez le reste du code en conséquence. 
  
  - A-t'on encore besoin du mot-clé `global` ? Pourquoi ?

  - Faites en sorte que la classe `Snake` prenne en charge la sauvegarde et le
rechargement de l'état du jeu.


<details>
<summary>
**✨ Solution**
</summary>
```python
# Python Standard Library
import copy
import random
import sys

# Third-Party Libraries
import pygame

# Snake
from constants import *


DIRECTIONS = [RIGHT, DOWN, LEFT, UP]


def check_direction(direction):
    try:
        direction = list(direction)
    except TypeError:
        error = f"{direction} is not list-like"
        raise TypeError(error)
    if (
        len(direction) != 2
        or not isinstance(direction[0], int)
        or not isinstance(direction[1], int)
    ):
        raise TypeError(
            f"{direction} is not a pair of integers"
        )
    elif direction not in DIRECTIONS:
        raise ValueError(
            f"{direction} is not in {DIRECTIONS}"
        )


def is_in_scope(tile):
    x, y = tile
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


def check_geometry(geometry):
    try:
        geometry = list(geometry)
    except TypeError:
        error = f"{geometry} is not list-like"
        raise TypeError(error)
    try:
        geometry = [list(item) for item in geometry]
    except TypeError:
        error = f"{item} is not list-like"
        raise TypeError(error)
    if not all(
        len(item) == 2
        and isinstance(item[0], int)
        and isinstance(item[1], int)
        for item in geometry
    ):
        raise TypeError(
            "all geometry items should be pairs of integers"
        )

    if not geometry:
        raise ValueError("empty geometry")

    for i, item in enumerate(geometry[:-1]):
        next_item = geometry[i + 1]
        diff = (
            next_item[0] - item[0],
            next_item[1] - item[1],
        )
        if abs(diff[0]) + abs(diff[1]) != 1:
            raise ValueError("non-connected snake geometry")

    if not all(is_in_scope(item) for item in geometry):
        raise SystemExit("snake out of bounds")

    for i, elt in enumerate(geometry):
        if elt in geometry[i + 1 :]:
            # at least one repeated item
            raise SystemExit("snake self-collision")


class Snake:
    def __init__(self, geometry, direction):
        self.direction = direction
        self.geometry = geometry

    def get_direction(self):
        return copy.deepcopy(self._direction)

    def set_direction(self, direction):
        check_direction(direction)
        self._direction = copy.deepcopy(direction)

    direction = property(get_direction, set_direction)

    def get_geometry(self):
        return copy.deepcopy(self._geometry)

    def set_geometry(self, geometry):
        check_geometry(geometry)
        self._geometry = copy.deepcopy(geometry)

    geometry = property(get_geometry, set_geometry)

    def get_head(self):
        return self.geometry[-1]

    head = property(get_head)

    def move(self):
        head = self.head
        new_head = [
            head[0] + self.direction[0],
            head[1] + self.direction[1],
        ]
        if new_head == state.fruit:
            state.score += 1
            self.geometry = self.geometry + [new_head]
            state.fruit = [
                random.randint(0, WIDTH - 1),
                random.randint(0, HEIGHT - 1),
            ]
        else:
            self.geometry = self.geometry[1:] + [new_head]


# State Management
class State:
    def __init__(self, snake, fruit, score):
        self.snake = snake
        self.fruit = fruit
        self.score = score

    def save(self):
        state_dict = {
            "geometry": self.snake.geometry,
            "direction": self.snake.direction,
            "fruit": self.fruit,
            "score": self.score,
        }
        with open(
            SNAPSHOT, mode="w", encoding="utf-8"
        ) as file:
            file.write(repr(state_dict))

    def load(self):
        with open(
            SNAPSHOT, mode="r", encoding="utf-8"
        ) as file:
            data = file.read()
        state_dict = eval(data)
        self.snake = Snake(
            state_dict["geometry"], state_dict["direction"]
        )
        self.fruit = state_dict["fruit"]
        self.score = state_dict["score"]


_snake = Snake(
    geometry=[[10, 15], [11, 15], [12, 15]], direction=RIGHT
)
state = State(snake=_snake, fruit=[10, 10], score=0)


# Helpers
def setup():
    pygame.init()
    width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
    screen = pygame.display.set_mode(width_height)
    clock = pygame.time.Clock()
    return (screen, clock)


def set_direction(d):
    def action():
        state.snake.direction = d

    return action


def exit():
    pygame.quit()
    sys.exit()


# Event Management
KEY_BINDINGS = {
    "q": exit,
    "up": set_direction(UP),
    "down": set_direction(DOWN),
    "left": set_direction(LEFT),
    "right": set_direction(RIGHT),
    "s": state.save,
    "l": state.load,
}

KEY_EVENT_HANDLER = {
    pygame.key.key_code(k): v
    for k, v in KEY_BINDINGS.items()
}


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_handler = KEY_EVENT_HANDLER.get(event.key)
            if event_handler:
                event_handler()


def draw_frame(screen):
    screen.fill(COLORS["background"])
    for x, y in state.snake.geometry:
        rect = [
            x * CELL_SIZE,
            y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        ]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [
        state.fruit[0] * CELL_SIZE,
        state.fruit[1] * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE,
    ]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {state.score}")


def wait_for_next_frame(clock):
    clock.tick(FPS)


# Setup & Main Loop
screen, clock = setup()

while True:
    handle_events()
    state.snake.move()
    draw_frame(screen)
    wait_for_next_frame(clock)
```
</details>

⚙️ Moteur de jeu
================================================================================


On souhaite désormais séparer aussi nettement que possible le code qui relève 
spécifiquement de notre jeu et le code générique, commun à (presque) tous les
jeux. Ce dernier type de code formera les bases d'un moteur de jeu et sera
développé dans une classe `Game` du fichier `game.py`. Cette classe 
devra prendre en charge l'initialisation de `pygame`, la gestion des fps, 
la récupération des évènements, etc.

On souhaite pouvoir exploiter cette classe générique en définissant une
classe `SnakeGame` qui en dérive et qui régit le jeu du serpent. 
La classe `SnakeGame` sera définie de la façon suivante :

``` python
from game import Game

class SnakeGame(Game):
    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                event_handler = KEY_EVENT_HANDLER.get(event.key)
                if event_handler:
                    event_handler()
        state.snake.move()

    def draw(self):
        screen = self.screen
        self.caption = f"Score: {state.score}"
        draw_background(screen)
        draw_snake(screen, state.snake)
        draw_fruit(screen, state.fruit)
```

Lorsque l'on invoque la commande `python snake.py`, le code suivant sera exécuté :

``` python
snake_game = SnakeGame()
snake_game.start()
```

Développez la classe `Game` (dans le fichier `game.py`) en conséquence !

<details>
<summary>
**✨ Solution : `game.py`**
</summary>
```python
# Python Standard Library
import sys

# Third-party Libraries
import pygame

# Local
from constants import *

class Game:
    def __init__(
        self, size=(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE), fps=FPS, caption=""
    ):
        self.size = size
        self.fps = fps
        self.caption = caption

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            self.process_events(events)
            self.draw()
            pygame.display.update()
            pygame.display.set_caption(self.caption)
            self.clock.tick(self.fps)

    def process_events(self, events):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()
```
</details>

🤖 Pilote automatique
================================================================================


On souhaite faciliter la vie du joueur : lorsque celui-ci ne presse aucune touche
entre deux frames successives, votre programme devra prendre une décision à sa place pour
le rapprocher du fruit, en évitant de créer trop de collisions (au minimum :
en ne faisant jamais un demi-tour).

Développez une classe 🤖 `AutoSnakeGame` qui prenne en charge cette 
fonctionnalité quand on lance le jeu avec la commande `python autosnake.py`.

``` python
# Third-Party Libraries
import pygame as pg

# Local Modules
from constants import *
from snake import state, SnakeGame

class AutoSnakeGame(SnakeGame):
    pass # TODO!

if __name__ == "__main__":
    snake_game = AutoSnakeGame()
    snake_game.start()
```

<details>
<summary>
**✨ Solution : `autosnake.py`**
</summary>
```python

# Third-Party Libraries
import pygame as pg

# Local Modules
from constants import *
from snake import state, SnakeGame

class AutoSnakeGame(SnakeGame):
    def process_events(self, events):
        if not events:
            snake = state.snake
            snake_head = snake.head
            direction = snake.direction
            fruit = state.fruit
            aim = [fruit[0] - snake_head[0], fruit[1] - snake_head[1]]
            key = None
            if aim[0] > 0 and direction != LEFT:
                key = pg.K_RIGHT
            elif aim[0] < 0 and direction != RIGHT:
                key = pg.K_LEFT
            elif aim[1] > 0 and direction != UP:
                key = pg.K_DOWN
            elif aim[1] < 0 and direction != DOWN:
                key = pg.K_UP
            if key is not None:
                event = pg.event.Event(pg.KEYDOWN, key=key)
                events.append(event)
        super().process_events(events)


if __name__ == "__main__":
    snake_game = AutoSnakeGame()
    snake_game.start()
```

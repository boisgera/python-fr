---
title: Le retour du retour du serpent
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris -- PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: auto
---


🕹️ Introduction
================================================================================

Nous allons remanier (à nouveau !) notre programme [🐍 snake.py](../snake-2/solutions/snake-v2.4.py),
en exploitant une conception orientée objet.
Nous tenterons de rendre son code plus robuste / réutilisable / compréhensible 
/ maintenable. 
Nous tâcherons ensuite de tirer les bénéfices de cette réorganisation 
en développant – avec le minimum d'effort de développement – 
un 🤖 bot qui assistera le joueur dans la poursuite du high-score. 


<details>
<summary>
**📄 Snake version 2**
</summary>

```python
# Python Standard Library
import random
import sys

# Pygame
import pygame

# Setup
# ------------------------------------------------------------
WIDTH = 30
HEIGHT = 30
CELL_SIZE = 20
FPS = 1.0
COLORS = {
    "background": [255, 255, 255],
    "snake": [0, 0, 0],
    "fruit": [255, 0, 0]
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]
SNAPSHOT="snapshot.py"

# State
# ------------------------------------------------------------
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = DOWN
fruit = [10, 10]
score = 0

def save_state():
    state = {
        "snake": snake,
        "direction": direction,
        "fruit": fruit,
        "score": score
    }
    with open(SNAPSHOT, mode="w") as file:
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


# Helper Functions
# ------------------------------------------------------------
def init():
    pygame.init()
    screen = pygame.display.set_mode([CELL_SIZE*WIDTH, CELL_SIZE*HEIGHT])
    clock = pygame.time.Clock()
    return screen, clock

def draw(screen):
    screen.fill(COLORS["background"])
    for x, y in snake:
        rect = [x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*CELL_SIZE, fruit[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE]
    pygame.draw.rect(screen, COLORS["fruit"], rect)  
    pygame.display.set_caption(f"Score : {score}")

def set_direction(d):
    def action():
        global direction
        direction = d
    return action

def move_snake():
    global snake, score, fruit
    head = snake[-1]
    new_head = [
      head[0] + direction[0], 
      head[1] + direction[1]
    ]
    if new_head in snake:
        sys.exit()
    elif new_head[0] < 0 or new_head[0] >= WIDTH:
        sys.exit()
    elif new_head[1] < 0 or new_head[1] >= HEIGHT:
        sys.exit()
    if new_head == fruit:
        score = score + 1
        snake = snake + [new_head]
        fruit = [
            random.randint(0, WIDTH-1), 
            random.randint(0, HEIGHT-1)
        ]
    else:
        snake = snake[1:] + [new_head]

# Event Management
# ------------------------------------------------------------
KEY_BINDINGS = {
    "q": sys.exit,
    "up": set_direction(UP),
    "down": set_direction(DOWN),
    "left": set_direction(LEFT),
    "right": set_direction(RIGHT),
    "s": save_state,
    "l": load_state,
}

KEY_EVENT_HANDLER = {pygame.key.key_code(k): v for k, v in KEY_BINDINGS.items()}

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_handler = KEY_EVENT_HANDLER.get(event.key)
            if event_handler:
                event_handler()

def wait_for_next_frame(clock):
    clock.tick(FPS)

# Main Loop
# ------------------------------------------------------------
try:
    load_state()
except FileNotFoundError:
    pass

screen, clock = init()
while True:
    events = pygame.event.get()
    handle_events(events)
    move_snake()
    draw(screen)
    pygame.display.update()
    wait_for_next_frame(clock)
```
</details>

✔️ Validation
================================================================================

Quelles sont les valeurs admissibles pour la direction du serpent ?
Implémenter une fonction `check_direction` qui prenne en argument une
direction, ne renvoie rien si la direction est admissible et lève une
exception (de type `ValueError` ou `TypeError`, à déterminer) dans le cas contraire.

De même, toutes les listes de n-uplets représentant la géométrie du serpent 
ne sont pas valides. Faire la liste des toutes les conditions qui rendent 
la géométrie du serpent invalide ; on distinguera les

  - 🐛 **bugs** qui résultent d'erreurs de programmation et ne devraient pas exister,

  - 💀 **game over** qui peuvent arriver mais doivent entrainer la fin immédiate du jeu.

Mettre en correspondance ces catégories avec un type d'exception (soit
`TypeError`, soit `ValueError`, soit `SystemExit`), puis
implémenter une fonction `check_geometry` qui prenne en argument une 
géométrie de serpent, ne renvoie rien si elle est valide et lève 
l'exception appropriée dans le cas contraire.

<details>
<summary>
**✨ Solution**
</summary>
```python
def check_direction(direction):
    valid_directions = list(DIRECTIONS.values())
    if (
        not isinstance(direction, list)
        or len(direction) != 2
        or not isinstance(direction[0], int)
        or not isinstance(direction[1], int)
    ):
        raise TypeError(f"{direction} is not a pair of integers")
    elif direction not in valid_directions:
        raise ValueError(f"{direction} is not in {valid_directions}")


def is_in_scope(tile):
    x, y = tile
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


def check_geometry(geometry):
    if not all(
        isinstance(item, list)
        and len(item) == 2
        and isinstance(item[0], int)
        and isinstance(item[1], int)
        for item in geometry
    ):
        raise TypeError("all geometry items should be pairs of integers")
    if not geometry:
        raise ValueError("empty geometry")
    for i, item in enumerate(geometry[:-1]):
        next_item = geometry[i + 1]
        diff = (next_item[0] - item[0], next_item[1] - item[1])
        if abs(diff[0]) + abs(diff[1]) != 1:
            raise ValueError("non-connected snake geometry")
    if not all(is_in_scope(item) for item in geometry):
        raise SystemExit("snake out of bounds")

    for i, elt in enumerate(geometry):
        if elt in geometry[i+1:]:
            # at least one repeated item
            raise SystemExit("snake self-collision")
```
</details>


🐍 Un type `Snake`
================================================================================

Implémenter une classe `Snake` encapsulant la géométrie et la direction du
serpent :

```python
>>> geometry = [[10, 15], [11, 15], [12, 15]]
>>> direction = [0, 1]
>>> snake = Snake(geometry, direction)
```

Le constructeur de `Snake` doit vérifier que la géométrie et la direction
ou générer une erreur si cela n'est pas le cas. 
Stockez les arguments `geometry` et `direction` comme les attributs 
de même nom de l'instance snake.

```python
>>> snake.geometry
[[10, 15], [11, 15], [12, 15]]
>>> snake.direction
[0, 1]
```

A-t'on la garantie que ces attributs restent valides quel que soit l'usage
que le programmeur fasse de l'instance `snake` dans son code ? Faire
disparaître les attributs publics `geometry` et `direction` au profit
d'attributs privés `_geometry` et `_direction`, puis développer des
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

Même chose pour `set_geometry`.

Enfin, associez aux accesseurs `get_direction`, `set_direction`, 
`get_geometry` et `set_geometry` des propriétés `geometry` et `direction`
et adapter le code client en conséquence.

Développez une propriété `head`, accessible uniquement en lecture,
renvoyant la tête du serpent.

```python
>>> snake.head
[12, 15]
```

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

Introduire une méthode `move` dans la classe `Snake` qui va mettre à jour
la géométrie du serpent en tenant compte de la direction courante du serpent
et de la position des fruits (à remettre à jour le cas échéant).

Adapter la boucle générale du programme  [🐍 snake.py](../snake-2/solutions/snake-v2.4.py) 
pour intégrer les développements de la classe `Snake`. Vérifier en y jouant que le comportement du jeu reste identique.


🗃️ Etat du jeu
================================================================================

Définir une classe `State` représentant l'état à un instant donné du programme.
On souhaite pouvoir initialiser cet état par un code de la forme

``` python
snake = Snake(
    geometry=[[10, 15], [11, 15], [12, 15]], 
    direction=DIRECTIONS["RIGHT"]
) 
state = State(snake=snake, fruit=[10, 10])
```

et que l'instance `state` expose les attributs `snake` et `fruit` (en lecture
et en écriture). 

Adapter le reste du code en conséquence. A-t'on encore besoin du mot-clé `global` ?
Pourquoi ?

Quelle autre type de fonctionnalité pourrait être prise en charge par la classe
`State` ?

🧱 Constantes
================================================================================


🧹 **Nettoyage de printemps !** 
Déplacer la définition des constantes du programme 
(`W, H, X, ...`) dans un fichier à part, `constants.py`,
puis les importer dans `snake.py` avec :

``` python
from constants import *
```

📄 Solution : [constants.py](solutions/constants.py)


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
`SnakeGame` sera définie de la façon suivante (fichier complet : 📄 [snake.py](solutions/snake.py)) :

``` python
from game import Game

class SnakeGame(Game):
    def process_events(self, events):
        handle_events(events)
        move_snake()
    def draw(self):
        draw(self.screen)
```

Lorsque l'on invoque la commande `python snake.py`, le code suivant sera exécuté :

``` python
snake_game = SnakeGame(size=(X * W, Y * H), fps=FPS)
snake_game.start()
```


Développer la classe `Game` en conséquence !

📄 Solution : [game.py](solutions/game.py)


🤖 Pilote automatique
================================================================================


On souhaite faciliter la vie du joueur: lorsque celui-ci ne presse aucune touche
pendant une frame, votre programme devra prendre une décision à sa place pour
le rapprocher du fruit, en évitant de créer trop de collisions (au minimum:
en ne faisant jamais un demi-tour).

Développer une classe 🤖 `AutoSnakeGame` qui prenne en charge cette 
fonctionnalité quand on lance le jeu avec la commande `python autosnake.py`.

``` python
# Third-Party Libraries
import pygame as pg

# Local Modules
from constants import *
from snake import state, SnakeGame

class AutoSnakeGame(SnakeGame):
    pass # TODO!

snake_game = AutoSnakeGame(size=(X * W, Y * H), fps=FPS)
snake_game.start()
```

📄 Solution : [autosnake.py](solutions/autosnake.py)

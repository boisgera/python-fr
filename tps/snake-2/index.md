---
title: Le retour du serpent
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris -- PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: auto
---

Introduction
--------------------------------------------------------------------------------

Ce TP vous propose de poursuivre le développement du jeu du serpent. 

Nous allons lui ajouter quelques fonctionnalités, mais surtout avant cela,
nous allons faire du **réusinage**, c'est-à-dire, restructurer notre code 
existant -- à fonctionnalités constantes -- en utilisant quelques "bonnes pratiques" 
qui le rendront (espérons-le !) plus facile à maintenir (cf [Lexique]).


On rappelle l'état actuel du projet :

<details>
<summary>
**Le programme initial**
</summary>

```{.python output="snake-0.py"}
import random
import sys
import pygame

white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

pygame.init()
screen = pygame.display.set_mode([20*30, 20*30])
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                direction = [0, -1]
            elif event.key == pygame.K_LEFT:
                direction = [-1, 0]
            elif event.key == pygame.K_DOWN:
                direction = [0, 1]
            elif event.key == pygame.K_RIGHT:
                direction = [1, 0]
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
    screen.fill(white)
    for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, black, rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, red, rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")
    clock.tick(1)
```

</details>

# Structure & commentaires

On simpliferait probablement la lecture du code en insérant quelques lignes
blanches pour délimiter des sections et en les faisant précéder
d'un commentaire indiquant leur rôle.

On suggère les labels suivants (dans l'ordre alphabétique):

  - 🏷️ Constants
  
  - 🏷️ Event Management
  
  - 🏷️ Frame Update

  - 🏷️ Game Logic (move snake), 

  - 🏷️ Game State
    
  - 🏷️ Main Loop, 
  
  - 🏷️ Setup, 
  
  - 🏷️ Wait for next frame

A vous de localiser les sections correspondantes !

<details>
<summary>
**Solution**
</summary>

```{.python output="snake-1.py"}
import random
import sys
import pygame

# Constants
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]

# Game State
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

# Setup
pygame.init()
screen = pygame.display.set_mode([20*30, 20*30])
clock = pygame.time.Clock()

# Main Loop
while True:
    # Event Management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                direction = [0, -1]
            elif event.key == pygame.K_LEFT:
                direction = [-1, 0]
            elif event.key == pygame.K_DOWN:
                direction = [0, 1]
            elif event.key == pygame.K_RIGHT:
                direction = [1, 0]

    # Game Logic (move snake)
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

    # Frame Update
    screen.fill(white)
    for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, black, rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, red, rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")

    # Wait for next frame ... wait for it! 
    # (📺 https://www.youtube.com/watch?v=O_mlJwQ1_ZM)
    clock.tick(1)
```

</details>

# Configuration & constantes

En Python, l'usage est de désigner les grandeurs constantes par des noms
en majuscules. 
Un des intérêts d'avoir explicitement une section où l'on
déclare les constantes et que l'on évite d'avoir à dupliquer leur valeur
"en dur" dans le code et que si ultérieurement on est amené à changer leur
valeur, il suffira de le faire à un seul endroit.

  - Définir les constantes entières 

    ```python
    WIDTH = 30      # number of cells
    HEIGHT = 30     # number of cells
    CELL_SIZE = 20  # number of pixels
    ```

    et les utiliser pour faire disparaître les valeurs associées codées
    "en dur" dans le code. 

  - Même chose avec

    ```python
    FPS = 1  # frames per second
    ```

  - Plutôt que de coder en dur les couleurs dans le code, on va définir un
    thème de couleurs, qui désignera les couleurs choises par leur rôle
    dans l'application :
  
    ```python
    WHITE = [255, 255, 255]
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    COLORS = {
        "background": WHITE,
        "snake": BLACK,
        "fruit": RED
    }
    ```

    Modifier le code pour exploiter le dictionnaire constant `COLORS`.

  - Vous avez peut-être remarqué que le système de coordonnées de pygame,
    qui fait pointer l'axe des ordonnées vers le bas est un peu perturbant
    et donc un risque d'erreur. 
    Pour abstraire ce détail bas-niveau de notre code, 
    on définit des constantes directionnelles.

    ```python
    UP = [0, -1]
    DOWN = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]
    ```

    Adapter le code pour les exploiter.

  - On a de nombreuses fois dans le code la succession des deux appels

    ```python
    pygame.quit()
    sys.exit()
    ```

    Pour éviter cette répétition (et les risques d'erreurs afférents), 
    définir une fonction `exit` qui réalise ces deux appels, puis
    l'exploiter.

<details>
<summary>
**Solution**
</summary>


```{.python output="snake-2.py"}
import random
import sys
import pygame

# Constants
WIDTH = 30      # number of cells
HEIGHT = 30     # number of cells
CELL_SIZE = 20  # number of pixels
FPS = 1  # frames per second
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {
    "background": WHITE,
    "snake": BLACK,
    "fruit": RED
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

# Game State
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

# Setup
pygame.init()
width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
screen = pygame.display.set_mode(width_height)
clock = pygame.time.Clock()

# Helper Function
def exit():
    pygame.quit()
    sys.exit()

# Main Loop
while True:
    # Event Management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT

    # Game Logic (move snake)
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
        exit()
    if new_head == fruit:
        score = score + 1
        snake = snake + [new_head]
        fruit = [
            random.randint(0, 29),
            random.randint(0, 29)
        ]
    else:
        snake = snake[1:] + [new_head]

    # Frame Update
    screen.fill(COLORS["background"])
    for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")

    # Wait for next frame ... wait for it! 
    # (📺 https://www.youtube.com/watch?v=O_mlJwQ1_ZM)
    clock.tick(FPS)
```
</details>


# Structuration en fonctions

Les commentaires, c'est bien ! Ce qui est encore mieux, c'est d'avoir un code
tellement explicite qu'on n'en a (presque) plus besoin.

On souhaite dans cette étape remplacer le gros de notre code actuel 
par le code suivant, court et explicite :

```python
screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock)
```

Extrayez du code existant

  - des fonctions `setup`, `wait_for_next_frame` et `draw_frame`,

  - des fonctions `handle_events` et `move_snake` 
  
puis exploitez-les.


<details>
<summary>
**Solution**
</summary>


```{.python output="snake-3.py"}
import random
import sys
import pygame

# Constants
WIDTH = 30      # number of cells
HEIGHT = 30     # number of cells
CELL_SIZE = 20  # number of pixels
FPS = 1  # frames per second
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {
    "background": WHITE,
    "snake": BLACK,
    "fruit": RED
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

# Game State
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

# Helper Functions
def setup():
    pygame.init()
    width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
    screen = pygame.display.set_mode(width_height)
    clock = pygame.time.Clock()
    return screen, clock

def handle_events():
    global direction
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          exit()
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
              exit()
          if event.key == pygame.K_UP:
              direction = UP
          elif event.key == pygame.K_LEFT:
              direction = LEFT
          elif event.key == pygame.K_DOWN:
              direction = DOWN
          elif event.key == pygame.K_RIGHT:
              direction = RIGHT

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
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")

def wait_for_next_frame(clock):
    clock.tick(FPS)

def exit():
    pygame.quit()
    sys.exit()

# Setup & Main Loop
screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock)
```
</details>


# Sauvegarde & restauration

L'état du jeu à un instant donné est capturé par les variables
`snake`, `direction`, `fruit` et `score`.

  - Définissez des fonctions `save_state` et `load_state` (sans argument ni
    valeur de retour) qui permettent
    respectivement de sauver l'état courant dans un fichier (par exemple
    "snapshot.py" ; vous pouvez adapter l'extension du fichier selon le
    format de sauvgarde que vous utilisez) et de remplacer l'état courant
    par l'état stocké dans ce fichier.

  - Faites en sorte que l'état courant soit sauvegardé lorsque l'on appuie
    sur la touche "S" et que le programme charge l'état sauvegardé lorsque
    l'on appuie sur la touche "L".

<details>
<summary>
**Solution**
</summary>

```{.python output="snake-4.py"}
import random
import sys
import pygame

# Constants
WIDTH = 30      # number of cells
HEIGHT = 30     # number of cells
CELL_SIZE = 20  # number of pixels
FPS = 1  # frames per second
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {
    "background": WHITE,
    "snake": BLACK,
    "fruit": RED
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]
SNAPSHOT = "snapshot.py"

# Game State
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

def save_state():
    state = {
        "snake": snake,
        "direction": direction,
        "fruit": fruit,
        "score": score
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

# Helper Functions
def setup():
    pygame.init()
    width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
    screen = pygame.display.set_mode(width_height)
    clock = pygame.time.Clock()
    return screen, clock

def handle_events():
    global direction
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          exit()
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
              exit()
          elif event.key == pygame.K_s:
              save_state()
          elif event.key == pygame.K_l:
              load_state()
          if event.key == pygame.K_UP:
              direction = UP
          elif event.key == pygame.K_LEFT:
              direction = LEFT
          elif event.key == pygame.K_DOWN:
              direction = DOWN
          elif event.key == pygame.K_RIGHT:
              direction = RIGHT

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
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")

def wait_for_next_frame(clock):
    clock.tick(FPS)

def exit():
    pygame.quit()
    sys.exit()

# Setup & Main Loop
screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock) 
```

</details>

# Configuration clavier

Le code de gestion des évènements commence à ressembler à du code spaghetti ...
On souhaiterait remplacer ce code qui grossit à chaque fois que l'on rajoute 
une fonctionnalité par une fonction générique

```python
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_handler = KEY_EVENT_HANDLER.get(event.key)
            if event_handler:
                event_handler()
```

qui exploite une **configuration clavier** (🇺🇸 **key bindings**) configurable,
décrivant l'association entre la touche sélectionnée et l'action correspondante :

```python
KEY_BINDINGS = {
    "q": exit,
    "s": save_state,
    ...
}
```


  - Rajoutez une fonction de chargement de l'état sauvegardé quand on appuie sur
    la touche "L".

  - Définissez toutes les actions à gérer sous forme de fonction sans argument
    (comme `sys.exit`, `save_state`, `load_state`).

  - Complétez le dictionnaire `KEY_BINDINGS`, puis exploitez-le pour construire 
    le dictionnaire `KEY_EVENT_HANDLER` qui va associer à chaque code clavier
    Pygame l'action correspondante. 

    🗝️ Indication: [📖 `pygame.key.keycode`](https://www.pygame.org/docs/ref/key.html#pygame.key.key_code)

  - Remplacer la fonction actuelle de gestion des événements par sa version
    générique.


<details>
<summary>
**Solution**
</summary>

```{.python output="snake-5.py"}
import random
import sys
import pygame

# Constants
WIDTH = 30      # number of cells
HEIGHT = 30     # number of cells
CELL_SIZE = 20  # number of pixels
FPS = 1  # frames per second
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {
    "background": WHITE,
    "snake": BLACK,
    "fruit": RED
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]
SNAPSHOT = "snapshot.py"

# State Management
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

def save_state():
    state = {
        "snake": snake,
        "direction": direction,
        "fruit": fruit,
        "score": score
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
    return screen, clock

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

KEY_EVENT_HANDLER = {pygame.key.key_code(k): v for k, v in KEY_BINDINGS.items()}

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
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")

def wait_for_next_frame(clock):
    clock.tick(FPS)

def exit():
    pygame.quit()
    sys.exit()

# Setup & Main Loop
screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock) 
```

</details>


Lexique
================================================================================

  - 🍝 **[Code spaghetti]** (🇺🇸 **spaghetti code**)

  - 💸 **[Dette technique]** (🇺🇸 **technical debt**)

  - ♻️ **[Réusinage]** (🇺🇸 **refactoring**)

[Code spaghetti]: https://fr.wikipedia.org/wiki/Programmation_spaghetti
[Dette technique]: https://fr.wikipedia.org/wiki/Dette_technique
[Réusinage]: https://fr.wikipedia.org/wiki/R%C3%A9usinage_de_code


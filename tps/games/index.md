---
title: Le serpent
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: auto
---

--------------------------------------------------------------------------------

🙏 Projet original par Aurélien Noce ([@ushu](https://github.com/ushu)).

--------------------------------------------------------------------------------

L'objectif de ce TP est de réaliser un petit jeu en Python,
et au passage de vous apprendre à concevoir et réaliser un programme complet.

Si vous ne connaissez pas le jeu du serpent, [slither.io](http://slither.io/) en 
est une version moderne et complexe. Nous n'irons certainement pas aussi loin,
mais cela n'est pas le but !
Gardez en tête que votre objectif est de réaliser par itérations successives 
un **programme qui marche** et pas un programme parfait. 

Prérequis
--------------------------------------------------------------------------------

⚠️ Ce qui suit suppose que vous avez installé Python avec `conda`
et que vous avez un terminal `bash` fonctionnel sur votre ordinateur.

Commencez par créer un environnement nommé "snake", dédié au TP et 
contenant Python 3.9

```bash
(base) $ conda create -n snake python=3.9
```

Puis activez-le

```bash
(base) $ conda activate snake
```

Vous devriez alors avoir une nouvelle invite de commmande :

```
(snake) $
```

<details>
<summary>
**Dépannage 🛠️** 
</summary>

--------------------------------------------------------------------------------

Si vous ne voyez pas l'invite de commande `(snake) $` alors

1. exécutez la commande

   ```bash
   $ conda init bash
   ```

   puis

2. créez un nouveau terminal.

--------------------------------------------------------------------------------

</details>

Installez ensuite le module `pygame` avec `pip` dans cet environnement :

```bash
(snake) $ pip install pygame
```

Pour tester votre installation, lancez le programme d'exemple :

```bash
(snake) $ python -m pygame.examples.aliens
```

Avec Visual Studio Code
--------------------------------------------------------------------------------

**Suggestion #1.**  Installez l'[extension de VS Code pour Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

**Suggestion #2.** Indiquez à VS Code (et pas uniquement au terminal) 
qu'on souhaite travailler dans l'environnement conda `snake` :
cliquer dans la bannière du bas la zone qui indique le Python courant.

**Suggestion #3.** Pour lancer le programme directement depuis VS Code :

- ouvrir la palette de commandes
  - `⇧ ⌘ P` Shift-Command-P (mac)
  - `⇧ ⌃ P` Shift-Control-P (windows)
- chercher la fonction *Toggle Integrated Terminal*
  - mémoriser le raccourci clavier
  - qui est Control-backtick sur Mac (le backtick c'est `)

<!--
Premiers pas avec PyGame
--------------------------------------------------------------------------------

(factor out ? Indep doc? *Maybe*, given that the set of learning objectives
is autonomous)

Prérequis :

  - `dir` / `help` / usage doc en ligne


Objectifs :

  - import de module (bases)

  - sous-modules (principes et énumération)

  - concepts propres à pygame :
  
      - initialisation

      - modules & classes : display, time, Surface

      - display: création de "surface" (window / screen), taille

      - flux d'exécution et disparition de la surface !

      - time & delay

      - tracé sur une surface. N'apparaît pas !!!

      - display: update


``` python
import pygame
pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)

SCREEN_SIZE = (400, 300)

screen = pygame.display.set_mode(SCREEN_SIZE)

screen.fill(GREEN)

pygame.display.update()

pygame.time.delay(3000)
```

-->

Code de démarrage
--------------------------------------------------------------------------------

Notre point de départ : un arrière-plan dont la couleur varie aléatoirement.

<details>
<summary>
**Couleurs RGB ℹ️**
</summary>
--------------------------------------------------------------------------------

La couleur d'un pixel est décrite par son [code RGB](https://fr.wikipedia.org/wiki/Rouge_vert_bleu) : un triplet d'entiers compris entre 0 et 255 qui déterminent
l'intensité des composantes rouge, verte et bleue de la couleur. 
On a par exemple :

         R           G           B    Couleur
----------  ----------  ----------  ----------- 
       255           0           0      🟥
         0         255           0      🟩
         0           0         255      🟦
       255         255         255      ⬜
         0           0           0      ⬛
       128          64           0      🟫
       255         128           0      🟧
       255         255           0      🟨
       106          13         173      🟪
        


--------------------------------------------------------------------------------

</details>


```python
import random
import pygame

pygame.init()
screen = pygame.display.set_mode([400, 300])
clock = pygame.time.Clock()

while True:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = [red, green, blue]
    screen.fill(color)
    pygame.display.update()
    clock.tick(1.0)
```

Copiez ce code dans un fichier `snake.py` et exécutez-le :

```sh
(snake) $ python snake.py
```

⚠️ Pour quitter le programme tapez Control-P dans le terminal.


### Exercices

  - Changer la taille de la fenêtre -- initialement 400x300 -- pour 
    600x600.

  - Remplacez le code `clock.tick(1.0)` par `clock.tick(0.2)` puis 
    exécuter le programme. Puis procédez de même avec `clock.tick(60)`. 
    Que se passe-t'il ? 
    Que se passe-t'il si l'on supprime l'appel à la fonction `clock.tick` du programme ?
    A votre avis, quel est le rôle de la fonction `clock.tick` et le rôle de son argument ?

  - Que se passe-t'il si l'on commente la ligne `pygame.display.update()` ?
    Savez-vous expliquer ce phénomène ?

  - Jouer avec les couleurs


Événements
--------------------------------------------------------------------------------

Afin d'avoir un comportement plus "normal", nous devons instruire Pygame en lui disant comment réagir aux clicks sur le clavier ou sur la fenêtre:

```python
import random
import pygame

pygame.init()
screen = pygame.display.set_mode([400, 300])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = [red, green, blue]
    screen.fill(color)
    pygame.display.update()
    clock.tick(5)
```

Le damier
--------------------------------------------------------------------------------

Nous allons commencer par construire notre plateau de jeu ainsi :

- le plateau de jeu est découpé en 30x30 cases,

- chaque case fait 20 pixels de côté.

Pour vérifier la validité de ce plateau de jeu, 
écrivez un programme qui dessine un damier :

![](images/damier.png)

🗝️ Vous pouvez utiliser la méthode [`pygame.draw.rect`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect) :

```python
x = 100
y = 100
width = 30
height = 30
rect = [x, y, width, height]
red = 255
green = 0
blue = 0
color = [red, green, blue]
pygame.draw.rect(screen, color, rect)
```

Un serpent fixe
--------------------------------------------------------------------------------

L'étape suivante est de dessiner le serpent. Le serpent est simplement une suite de blocks de couleurs.
On veut dessiner le serpent aux coordonnées suivantes:

```python
# les coordonnées du corps du serpent
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
```

pour obtenir un schéma comme suit; disons pour fixer les idées que dans ce cas de figure
`[10, 15]` est la queue, et `[12, 15]` est la tête (mais c'est totalement arbitraire et pas du tout imposé) :

![](images/serpent.png)

Un serpent qui bouge
--------------------------------------------------------------------------------

Ensuite, nous allons faire bouger le serpent :

- nous créons un vecteur de "direction"
  
  ```python
  direction = [1, 0]
  ```

- à chaque itération de la boucle, nous pouvons déplacer le serpent dans 
  cette direction en "ajoutant" ce vecteur à la position de la tête du serpent

Une fois que le serpent bouge, ajouter les commandes pour se déplacer dans 
les 4 directions, en cliquant sur les flèches 
(par exemple le code renvoyé par la flêche vers le haut est `pygame.K_UP`)

Aussi on peut commencer à envisager d'accélérer un peu le jeu à ce stade...

**BONUS** faites en sorte que le serpent ne puisse pas faire "demi tour"

![](images/serpent-bouge.gif)

Le fruit
--------------------------------------------------------------------------------

Il faut maintenant faire manger notre serpent.
On va procéder comme suit:

  - on a toujours la position du serpent dans une variable `snake` :

  - on génère un "fruit", dans une position aléatoire

    ```python
    # exemple de fruit en position 10, 10 sur le plateau
    fruit = [10, 10]
    ```

  - quand la tête du serpent mange le fruit, 
    on place un nouveau fruit à une position aléatoire 
    et on allonge le serpent d'une case

    ![](images/manger.gif)

Épilogue
--------------------------------------------------------------------------------

Il nous reste deux petits changements pour avoir un serpent complètement fonctionnel:

- tout d'abord il faut détecter si le serpent se mord la queue, ce qui est une condition d'échec
- enfin on peut afficher le score.
  La façon la plus simple de procéder est de changer le titre de la fenêtre, avec la fonction `set_caption()`:
  ```python
  score = 0
  pygame.display.set_caption(f"Score: {score}")
  ```

![](images/score.png)

# Le snake

Projet original par [@ushu](https://github.com/ushu).

Le but de ce TP est de réaliser un petit jeu en Python.
L'objectif est de vous apprendre à concevoir et réaliser un programme complet,
et non de réaliser le nouveau best-seller.

Gardez ainsi en tête que votre objectif est de réaliser un **programme qui marche**
et pas un programme parfait.

Prérequis
--------------------------------------------------------------------------------

ℹ️ Ce qui suit suppose que vous avez installé Python avec `conda`
et que vous avez un terminal `bash` fonctionnel sur votre ordinateur.

Commencez par créer et activer un environnement dédié au TP :

```bash
# on commence par créer un environnement "snake"
(base) $ conda create -n snake python=3.9
# puis on l'active
(base) $ conda activate snake
# votre terminal doit indiquer le nom d'environnement:
(snake) $
```

**NOTE.** Si vous ne voyez pas, comme montré ici,
le `(snake)` affiché dans le prompt de bash pour vous rappeler en permanence
dans quel environnement on se trouve, il vous faut taper ceci avant de relancer
un terminal

```bash
$ conda init bash
```

Installez ensuite la dernière version du module `pygame` avec `pip` :

```bash
(snake) $ pip install pygame
```

Pour tester votre installation, vous pouvez lancer le programme d'exemple comme suit:

```bash
(snake) $ python -m pygame.examples.aliens
```

Code de démarrage
--------------------------------------------------------------------------------

Un premier code très simple est le suivant, écrivez-le dans un fichier `snake.py` et lancez-le avec la commande `python` :

```python
# v0 : on repeint l'écran à une période de 1 seconde
# et on a du mal à sortir du programme

import pygame as pg
from random import randint

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((400, 300))

# on crée aussi un objet "horloge"
clock = pg.time.Clock()

# enfin on boucle à l'infini pour faire le rendu de chaque image
while True:
    # l'objet "clock" permet de limiter le nombre d'images par secondes
    # ici pour cette démo on demande 1 image par seconde
    clock.tick(1)

    # on génère une couleur (Rouge, Vert, Bleu) au hasard
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # et on colorie l'écran avec cette couleur
    screen.fill(random_color)

    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()
```

Vous pouvez désormais exécuter le programme avec:

```sh
(snake) $ python snake.py
```

**Attention** : vous verrez que vous ne pouvez pas _fermer_ la fenêtre normalement, pour quitter votre programme vous devez saisir **CONTROL+C** dans le terminal.

Rappels vs-code
--------------------------------------------------------------------------------

**Rappel #1** : il est **fortement recommandé** d'installer l'extension de vs-code pour Python

**Rappel #2** : on a créé un environnement virtuel;  
du coup il est opportun d'indiquer à vs-code qu'il faut utiliser `snake` - plutôt que `base`  
pour cela cliquer dans la bannière du bas la zone qui indique le Python courant

**Rappel #3** : pour lancer le programme directement depuis vs-code :

- ouvrir la palette
  - `⇧ ⌘ P` Shift-Command-P (mac)
  - `⇧ ⌃ P` Shift-Control-P (windows)
- chercher la fonction _Toggle Integrated Terminal_
  - mémoriser le raccourci clavier
  - qui est Control-backtick sur Mac (le backtick c'est `)

Un petit détail
--------------------------------------------------------------------------------

Il faut savoir que c'est l'appel à `pg.display.update()` qui produit réellement l'affichage.

En fait, tous les autres calculs se produisent en mémoire (c'est très rapide), mais à un moment il faut bien parler à la carte vidéo pour l'affichage, et ça c'est beaucoup plus lent (+ieurs centaines de fois plus lent).

Du coup même si ce `display` reste dans l'ordre de grandeur de la milliseconde, il faut s'efforcer, pour une bonne fluidité du jeu, de n'appeler `update()` que le minimum, pour nous ici **une fois par itération de la boucle**.

Continuons
--------------------------------------------------------------------------------

Afin d'avoir un comportement plus "normal", nous devons instruire Pygame en lui disant comment réagir aux clicks sur le clavier ou sur la fenêtre:

```python
# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

import pygame as pg
from random import randint

pg.init()
screen = pg.display.set_mode((400, 300))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:
    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)

    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
```

Le damier
--------------------------------------------------------------------------------

Nous allons commencer par construire notre plateau de jeu ainsi:

- le plateau de jeu est découpé en 30x30 cases
- chaque case fait 20 pixels de côté

Pour valider le bon fonctionnement de ce plateau de jeu, écrivez un programme qui dessine un grille:

![](media/damier.png)

pour cela, vous pouvez utiliser la méthode [`pg.draw.rect()`](https://www.pygame.org/media/ref/draw.html#pygame.draw.rect) qui dessine un rectangle:

```python
# les coordonnées de rectangle que l'on dessine
x = 100 # coordonnée x (colonnes) en pixels
y = 100 # coordonnée y (lignes) en pixels
width = 30 # largeur du rectangle en pixels
height = 30 # hauteur du rectangle en pixels
rect = pg.Rect(x, y, width, height)
# appel à la méthode draw.rect()
color = (255, 0, 0) # couleur rouge
pg.draw.rect(screen, color, rect)
```

Un serpent fixe
--------------------------------------------------------------------------------

L'étape suivante est de dessiner le serpent. Le serpent est simplement une suite de blocks de couleurs.
On veut dessiner le serpent aux coordonnées suivantes:

```python
# les coordonnées du corps du serpent
snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]
```

pour obtenir un schéma comme suit; disons pour fixer les idées que dans ce cas de figure
`(10,15)` est la queue, et `(12, 15)` est la tête (mais c'est totalement arbitraire et pas du tout imposé) :

![](media/serpent.png)

Un serpent qui bouge
--------------------------------------------------------------------------------

Ensuite, nous allons faire bouger le serpent.
C'est en fait très simple:

- nous créons un vecteur de "direction"
  ```python
  direction = (1, 0)
  ```
- à chaque itération de la boucle, nous pouvons déplacer le serpent dans cette direction en "ajoutant" ce vecteur à la position de la tête du serpent

Une fois que le serpent bouge, ajouter les commandes pour se déplacer dans les 4 directions, en cliquant sur les flèches (par exemple le code renvoyé par la flêche vers le haut est `pg.K_UP`)

Aussi on peut commencer à envisager d'accélérer un peu le jeu à ce stade...

**BONUS** faites en sorte que le serpent ne puisse pas faire "demi tour"

![](media/serpent-bouge.gif)

Le fruit
--------------------------------------------------------------------------------

Il faut maintenant faire manger notre serpent.
On va procéder comme suit:

  - on a toujours la position du serpent dans une variable `snake` :

  - on génère un "fruit", dans une position aléatoire
    ```python
    # exemple de fruit en position 10, 10 sur le plateau
    fruit = (10, 10)
    ```

  - quand la tête du serpent mange le fruit, 
    on place un nouveau fruit à une position aléatoire 
    et on allonge le serpent d'une case

    ![](media/manger.gif)

Épilogue
--------------------------------------------------------------------------------

Il nous reste deux petits changements pour avoir un serpent complètement fonctionnel:

- tout d'abord il faut détecter si le serpent se mord la queue, ce qui est une condition d'échec
- enfin on peut afficher le score.
  La façon la plus simple de procéder est de changer le titre de la fenêtre, avec la fonction `set_caption()`:
  ```python
  score = 0
  pg.display.set_caption(f"Score: {score}")
  ```

![](media/score.png)

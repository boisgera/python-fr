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
nous allons faire le ménage ! C'est-à-dire, structurer le code existant 
(à fonctionnalité constante) en utilisant quelques "bonnes pratiques" 
qui rendront (espérons-le !) notre code plus lisible, plus facile à 
maintenir et à faire évoluer par la suite ... avant qu'il ne soit trop tard !

ℹ️ **Mini-lexique** :

  - 🍝 **[Code spaghetti]** (🇺🇸 **spaghetti code**)

  - 💸 **[Dette technique]** (🇺🇸 **technical debt**)

  - ♻️ **[Réusinage]** (🇺🇸 **refactoring**)

[Code spaghetti]: https://fr.wikipedia.org/wiki/Programmation_spaghetti
[Dette technique]: https://fr.wikipedia.org/wiki/Dette_technique
[Réusinage]: https://fr.wikipedia.org/wiki/R%C3%A9usinage_de_code

# Espaces & commentaires

Il serait pertinent d'utiliser des commentaires et quelques lignes blanches
pour mettre en évidence des "sections" dans le code, des groupements
d'instructions qui ont un rôle bien défini.

Définir de telles sections ; on suggère par défaut les labels suivants en commentaire :

  - Setup, State, Init, Main Loop, 
  
  - Handle Events, Move the snake, Draw & update the screen, Time management

<details>
<summary>
**Solution**
</summary>
[📁 `snake.py`](solutions/snake-v2.0.py)
</details>

# Configuration & constantes

En Python, l'usage est de désigner les grandeurs constantes par des noms
en majuscules (ici dans la section "Setup"). 
Un des intérêts d'avoir explicitement une section où l'on
déclare les constante et que l'on évite d'avoir à dupliquer leur valeur
"en dur" dans le code et que si ultérieurement on est amené à changer leur
valeur, il suffira de le faire à un endroit du code.

  - Définir les constantes entières 

    ```python
    WIDTH = 30
    HEIGHT = 30
    CELL_SIZE = 20
    ```

    et les utiliser pour faire disparaître les valeurs associées codées
    "en dur" dans le code. 

  - Même chose avec

    ```python
    FPS = 1.0 # frames per second
    ```

  - Plutôt que de coder en dur les couleurs dans le code, on va définir un
    thème de couleurs, qui désignera les couleurs choises par leur rôle
    dans l'application :
  
    ```python
    COLORS = {
        "background": [255, 255, 255],
        "snake": [0, 0, 0],
        "fruit": [255, 0, 0]
    }
    ```

    Modifier le code pour exploiter le dictionnaire `COLORS`.

  - Vous avez peut-être remarqué que le système de coordonnées de pygame,
    qui fait pointer l'axe des ordonnées vers le bas est un peu perturbant
    et donc un risque d'erreur. Pour abstraire ce détail bas-niveau de notre code, 
    on définit des constantes directionnelles.

    ```python
    UP = [0, -1]
    DOWN = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]
    ```

    Adapter le code pour les exploiter.

<details>
<summary>
**Solution**
</summary>
[📁 `snake.py`](solutions/snake-v2.1.py)
</details>

# Structuration en fonctions

Les commentaires, c'est bien ! Ce qui est encore mieux, c'est d'avoir un code
tellement explicite qu'on n'en a (presque) plus besoin.

On souhaite dans cette étape remplacer le gros de notre code actuel 
par le code suivant, court et explicite :

```python
screen, clock = init()
while True:
    events = pygame.event.get()
    handle_events(events)
    move_snake()
    draw(screen)
    pygame.display.update()
    wait_for_next_frame(clock)
```

  - Extraire du code existant des fonctions `init` et `wait_for_next_frame`
    et les exploiter.

  - Extraire une fonction `draw` du code existant et l'exploiter.

  - Extraire du code existant des fonctions `handle_events` et 
    `move_snake()` et les exploiter.


<details>
<summary>
**Solution**
</summary>
[📁 `snake.py`](solutions/snake-v2.2.py)
</details>

# Sauvegarde & restauration de l'état du jeu

L'état du jeu à un instant donné est capturé par les variables
`snake`, `direction`, `fruit` et `score`.

  - Définissez des fonctions `save_state` et `load_state` (sans argument ni
    valeur de retour) qui permettent
    respectivement de sauver l'état courant dans un fichier (par exemple
    "snaphot.py" ; vous pouvez adapter l'extension du fichier selon le
    format de sauvgarde que vous utilisez) et de remplacer l'état courant
    par l'état stocké dans ce fichier.

  - Faites en sorte que l'état courant soit sauvegardé lorsque l'on appuie
    sur la touche "S" et que le programme charge l'état sauvegardé au démarrage
    si le fichier de sauvegarde existe.

<details>
<summary>
**Solution**
</summary>
[📁 `snake.py`](solutions/snake-v2.3.py)
</details>

# Gestion configurable des événements

Le code de gestion des évènements commence à ressembler à du spagetthi ...
On souhaiterait remplacerce code qui grossit à chaque fois que l'on rajoute 
une fonctionnalité par une fonction générique

```python
def handle_events(events):
    for event in events:
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
    "q": sys.exit,
    "s": save_state,
    ...
}
```


  - Rajouter une fonction de chargement de l'état sauvegardé quand on appuie sur
    la touche "L".

  - Définir toutes les actions à gérer sous forme de fonction sans argument
    (comme `sys.exit`, `save_state`, `load_state`).

  - Compléter le dictionnaire `KEY_BINDINGS`, puis l'exploiter pour construire 
    le dictionnaire `KEY_EVENT_HANDLER` qui va associer à chaque code clavier
    Pygame l'action correspondante. 

    🗝️ Indication: [📖 `pygame.key.keycode`](https://www.pygame.org/docs/ref/key.html#pygame.key.key_code)

  - Remplacer la fonction actuelle de gestion des événements par sa version
    générique.

<details>
<summary>
**Solution**
</summary>
[📁 `snake.py`](solutions/snake-v2.4.py)
</details>
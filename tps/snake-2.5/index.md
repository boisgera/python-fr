---
title: Labyrinthes
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris -- PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: auto
---


Graphes
--------------------------------------------------------------------------------

Un graphe (orienté et pondéré) est représenté par le triplet composé :

  - d'un ensemble `vertices` de sommets,

  - d'un ensemble `edges` d'arêtes, représentées comme des paires de sommets,

  - d'un dictionnaire `weights` associant à chaque arête une valeur numérique.

Labyrinthes
--------------------------------------------------------------------------------

L'intérieur d'un labyrinthe est représenté par une collection de cellules 
carrées de même tailles, dont la position dans une grille uniforme dans
est repérées par leurs coordonnées entières. Les autres cellules coordonnées
font partie des parois du labyrinthes et sont infranchissables.

Le graphe associé :

  - représente les cellules par la paire de leur coordonnées,

  - considère qu'une arête est présente dans le graphe si les deux cellules
    sont adjacentes (à gauche, à droite en haut ou en bas ; deux cellules
    qui ne partagent qu'un sommet ne sont pas considérées adjacentes).

  - associe à chaque arête le poids 1 : le coût de l'action qui consiste à
    se déplacer d'une cellule à une cellule adjacente.

### Labyrinthes élémentaires

Développez une fonction `full_maze(width, height)` qui produit le graphe
d'un labyrinthe rectangulaire contenant la cellule `(0, 0)`, large de 
`width` cellules, haut de `height` cellules et contenant un mur entre
chaque paire de cellules adjacentes.

Puis, développez une fonction `empty_maze(width, height)` qui produit le
graphe rectangulaire similaire mais sans aucun mur interne.

### Visualisation

Utilisez la fonction `display_maze` dont le code est fourni en annexe de
ce document pour visualisez vos labyrinthes, par exemple :

``` pycon
>>> maze = full_maze(50, 25)
>>> display_maze(maze)
```

### Autres labyrinthes

Chargez et visualisez les labyrinthes disponibles dans le dossier :

  - 📁 <https://github.com/boisgera/python-advanced-companion/tree/master/tps/graphs/mazes>

Le format de ces fichier est simplement la représentation `repr` du graphe
associé à un labyrinthe.

Essayez de créer vos propres labyrinthes rectangulaires (en forme de
serpent, de spirale, etc.) ; éventuellement, essayez de déterminer une
méthode pour créer un labyrinthe "dense" similaire à celui représenté 
[ici](images/dense_random_maze.png).


Chemins
--------------------------------------------------------------------------------

### Ensemble atteignable

Implémentez une fonction `reachable_set(maze, origin)` qui renvoie l'ensemble
des cellules d'un labyrinthes accessible depuis la cellule `origin`.

Vous pourrez tester votre résultat graphiquement de la façon suivante :

``` pycon
>>> cells = reachable_set(maze, origin)
>>> display_maze(maze, map=cells)
```

Par exemple dans le labyrinthe ci-dessous, les cellules accessibles
depuis le coin en bas à gauche, représentées en jaune, sont toutes les
cellules du labyrinthe :

![Un labyrinthe dense de taille 50 x 25](images/dense_random_maze-reachable.png)


### Chemins associés

Implémentez une fonction `reachable_paths(maze, origin)` qui renvoie un 
dictionnaire dont les clés sont les cellules atteignables depuis l'origine
et les valeurs des chemins associés qui joignent l'origine et la destination.
Un chemin `path` sera représentés par une liste de cellules telles que
`path[0]` est l'origine, `path[i]` et `path[i+1]` sont adjacentes pour tout
`i` et `path[-1]` est la destination.

Vous pourrez tester votre résultat graphiquement de la façon suivante :

``` pycon
>>> paths = reachable_paths(maze, origin)
>>> destination = (???, ???) # a cell reachable from origin
>>> display_maze(maze, path=paths[destination])
```

Par exemple dans le labyrinthe ci-dessous, le chemin représenté en rouge joint
la cellule en bas à gauche et la cellule en haut à droite du labyrinthe :

![Un labyrinthe dense de taille 50 x 25](images/dense_random_maze-path.png) 

### Chemin optimal associé

Implémentez une fonction `shortest_paths(maze, origin)` qui renvoie un 
dictionnaire dont les clés sont les cellules atteignables depuis l'origine
et les valeurs un des chemins associés le plus courts (nécessitant le moins
de déplacements) qui joignent l'origine et la destination.

Vous pourrez tester votre résultat graphiquement en invoquant `display_maze`
comme à la question précédente.

Performance
--------------------------------------------------------------------------------

Plusieurs stratégies permettent d'améliorer les performances de la recherche
des plus courts chemins, un point qui devient critique quand la taille des
labirynthes augmente ; notamment le choix de structures de données plus 
efficaces, et choix d'algorithmes plus efficaces.

### Mesure de la performance

Dans tous les cas, pour mesurer les (éventuels) progrès réalisés,
nous pourrons afficher le temps passé à déterminer les chemins optimaux ;
par exemple :

``` python
start = time.time()
paths = shortest_paths(maze, origin)
stop = time.time()
print(f"elapsed time (secs): {stop - start}")
```

Pour obtenir une image plus précise de ce qui se passe, et savoir dans quelle 
partie du code le temps est passé, on pourra utiliser le projet

  - 🐍 <https://github.com/pyutils/line_profiler>

### Structure de données

La structure de données choisie initialement pour représenter les graphes
n'est pas nécessairement la mieux choisie. Déterminez dans votre algorithme
quelles sont les opérations les plus fréquemment utilisées ; adaptez 
votre représentation des graphes en conséquence et mesure le résultat.

### Algorithmes

Améliorez ensuite l'algorithme lui-même. On pourra notamment étudier le
classique : 

  - 🎓 <https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra>


Annexe - Visualisation
--------------------------------------------------------------------------------

```python
# Scientific stack
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Visualization
# ------------------------------------------------------------------------------
def rotate(x1y1, x2y2):
    "Rotate a segment +90° with respect to its center"
    x1, y1 = x1y1
    x2, y2 = x2y2
    cx, cy = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
    x3y3 = cx - (y1 - cy), cy + (x1 - cx)
    x4y4 = cx - (y2 - cy), cy + (x2 - cx)
    return x3y3, x4y4

def display_maze(graph, path=None, map=None):
    vertices, edges, weights = graph
    width = max(w for (w, h) in vertices) + 1
    height = max(h for (w, h) in vertices) + 1
    wh_ratio = width / height
    fig_width = 14  # inches
    fig_height = fig_width / wh_ratio
    fig, axes = plt.subplots(figsize=(fig_width, fig_height))
    axes.axis("equal")
    for x in range(width):
        for y in range(height):
            for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                xn, yn = x+dx, y+dy
                if ((x, y), (xn, yn)) in edges:
                    style = {"color": "grey", "linestyle": ":"}
                else:
                    style = {"color": "black", "linestyle": "-"}
                w1, w2 = rotate((x + 0.5, y + 0.5), (xn + 0.5, yn + 0.5)) # wall segment                    
                axes.plot([w1[0], w2[0]], [w1[1], w2[1]], **style)
    axes.axis("off")

    if path:
        xs = np.array([x for (x, y) in path])
        ys = np.array([y for (x, y) in path])
        axes.plot(xs + 0.5, ys + 0.5, "r-")

    if map:
        if isinstance(map, set):
            map = {k: 1.0 for k in map}
        d_max = max(map.values())
        cmap = mpl.cm.get_cmap("viridis")

        for v, d in map.items():
            dx, dy = 1, 1
            rect = patches.Rectangle(v, dx, dy, facecolor=cmap(d / d_max))
            axes.add_patch(rect)
```

--------------------------------------------------------------------------------


Un labyrinthe de taille 50 x 25 :

![Un labyrinthe dense de taille 50 x 25](images/dense_random_maze.png)

Ce labyrinthe est généré aléatoirement en respectant deux propriétés :

  - on peut explorer tout le labyrinthe quel que soit son point de départ,

  - si l'on rajoute un mur où que ce soit cette propriété disparaît.

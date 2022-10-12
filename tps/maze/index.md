---
title: Labyrinthes
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris -- PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
date: auto
---

Labyrinthes
--------------------------------------------------------------------------------

Nous nous intéressons aux labyrinthes définis au sein d'une grille 30x30,
que nous décrirons en Python par des listes des paires d'entiers 
compris entre 0 et 29 (non dupliquées), 
représentant les coordonnées des cellules vides du labyrinthes. 
Toutes les autres cellules de la grille sont des murs.

![Un labyrinthe généré (pseudo-)aléatoirement avec 25% de murs (cellules vides en blanc,
murs en noir).](images/random-maze.jpg)

### Bibliothèque de labyrinthes

Explorez les fichiers du dossier 📁 [mazes](./mazes/).
Chaque fichier contient la représentation sous forme de texte
(générez par `repr`) d'un labyrinthe. 
Chargez le contenu des ces fichiers, puis reconstituez
les objets labyrinthes associés.

<details>
<summary>
**Solution**
</summary>

Par exemple, pour obtenir le labyrinthe du fichier `"random-maze.py"`:

```pycon
>>> filename = "mazes/random-maze.py"
>>> file = open(filename, mode="r", encoding="utf-8")
>>> random_maze_repr = file.read()
>>> file.close()
>>> random_maze = eval(maze_repr)
```

</details>

### Visualisation

Développez avec pygame une fonction `display_maze` permettant de visualiser un 
labyrinthe.

<details>
<summary>
**Solution**
</summary>

```python
# Pygame
import pygame as pg


# Constants
WIDTH, HEIGHT = 30, 30
CELL_SIZE = 20
FPS = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def display_maze(maze):
    pg.init()
    width_height = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
    screen = pg.display.set_mode(width_height)

    clock = pg.time.Clock()
    while True:
        events = pg.event.get()
        if any(event.type == pg.QUIT for event in events):
            break
        draw_maze(screen, maze)
        pg.display.update()
        clock.tick(FPS)

    pg.quit()

def draw_maze(screen, maze):
    screen.fill(BLACK)
    for x, y in maze:
        h = CELL_SIZE
        pg.draw.rect(screen, WHITE, (x * h, y * h, h, h))
```

</details>


### Créez vos propres labyrinthes

... puis ajoutez-les à la biblothèque existante !

<details>
<summary>
**Solution**
</summary>

Une fois votre labyrinthe `my_maze` conçu selon vos préférences

```pycon
>>> my_maze_repr = repr(my_maze)
>>> file = open("mazes/my-maze.py", "w", encoding="utf-8")
>>> file.write(my_maze_repr)
>>> file.close()
```

</details>


Graphes et chemins
--------------------------------------------------------------------------------


🏷️ Un **graphe** (orienté et pondéré) est un triplet composé :

  - d'un ensemble de sommets,

  - d'un ensemble d'arêtes (une arête est une paire composée d'un sommet
    source et d'un sommet cible),

  - d'une fonction qui associe à chaque arête son poids (un nombre).

🏷️ Un **chemin** d'un graphe est une suite de sommets du graphe tels que 
chaque élément de la suite et son successeur forment une arête du graphe.


### Labyrinthes et graphes

On souhaite associer à un labyrinthe un graphe dont

  - les sommets sont les cellules vides du labyrinthe,

  - les arêtes représentent les cellules vides adjacentes 
    (vers le haut, le bas, la gauche ou la droite, mais pas les diagonales).

  - le poids de chaque arête est 1 : un déplacement élémentaire étant nécessaire 
    pour se déplacer d'une cellule à une cellule adjacente.

Quelle structure de données Python utiliserait-t'on "naturellement" 
pour représenter ces graphes ? Décrivez le cas échéant quelles variantes 
possibles vous viennent à l'esprit et leurs avantages éventuels.

Implémentez une fonction `maze_to_graph`
qui construit le graphe associé à un labyrinthe.

<details>
<summary>
**Solution**
</summary>

Il semble naturel de représenter 
les sommets comme un ensemble de paires d'entiers, les arêtes comme un ensemble
de paires de sommets et la fonction de pondération comme un dictionnaire ayant
comme clé les sommets et comme valeur unique 1.

On note qu'ici la valeur unique 1 rend la donnée des poids totalement redondante
une fois que l'on a les arêtes ; on pourrait donc se passer ici du dictionnaire
des poids. Inversement, en général, si l'on a un dictionnaire `weight` de poids, 
on peut retrouver les arêtes par `edges = set(weight.keys())` ; la donnée
des arêtes est donc superflue.

On pourrait imaginer d'autres structures décrivant des graphes qui soient
plus efficaces mais il faudrait pour cela savoir quelles sont les 
opérations courantes que nous allons devoir réaliser fréquemment, 
afin d'optimiser la structure par rapport à ces opérations. 



```python
def maze_to_graph(maze):
    vertices = set(maze)
    edges = set()
    weights = {}
    for vertex in vertices:
        x, y = vertex
        for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if neighbor in vertices:
                edge = (vertex, neighbor)
                edges.add(edge)
                weights[edge] = 1
    return (vertices, edges, weights)
  ```

</details>

### Ensemble atteignable

Implémentez une fonction `reachable_set` qui renvoie l'ensemble
des cellules d'un labyrinthe `maze` qui sont accessibles depuis la cellule `source`.



<details>
<summary>
**Solution**
</summary>

```python
def reachable_set(graph, source):
    vertices, edges, _ = graph
    todo = {source}
    done = set()
    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            if n not in done:
                todo.add(n)
        done.add(current)
    return done
```

</details>


### Labyrinthes et chemins 

Implémentez une fonction `path_to` qui prend comme argument un labyrinthe,
une cellule source et une cellule cible et renvoie un chemin joignant l'une
à l'autre si un tel chemin existe, ou `None` si cela n'est pas le cas.



<details>
<summary>
**Solution**
</summary>

```python
def path_to(graph, source, target):
    vertices, edges, _ = graph
    todo = {source}
    done = set()
    path = {source: [source]}
    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            if n not in (done | todo):
                path[n] = path[current] + [n]
                if n == target:
                    return path[n]
                todo.add(n)
        done.add(current)
```

</details>

Etendez ensuite cette fonction : quand la cellule cible est non
spécifiée, renvoyez un dictionnaire dont les clés sont les 
cellules atteignables et les valeurs les chemins correspondants.


<details>
<summary>
**Solution**
</summary>

```python
def path_to(graph, source, target=None):
    vertices, edges, _ = graph
    todo = {source}
    done = set()
    path = {source: [source]}
    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            if n not in (done | todo):
                path[n] = path[current] + [n]
                if n == target:
                    return path[n]
                todo.add(n)
        done.add(current)
    if target is None:
        return path
    else:
        return None
```

</details>



### Chemin optimal 

Implémentez une fonction `shortest_path_to(maze, origin)` qui renvoie un 
dictionnaire dont les clés sont les cellules atteignables depuis l'origine
et les valeurs un des chemins associés le plus courts (nécessitant le moins
de déplacements) qui joignent l'origine et la destination.

Vous pourrez tester votre résultat graphiquement en invoquant `display_maze`
comme à la question précédente.

```
def shortest_path_to(graph, source, target): 
    "Non-greedy version"
    vertices, edges, weight = graph
    distance, paths = {}, {}
    todo = {source}
    distance[source] = 0
    paths[source] = [source]
    while todo:
        current = todo.pop()
        if current == target:
            return paths[current]
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            d = distance[current] + weight[(current, n)]
            if d < distance.get(n, math.inf):
                distance[n] = d
                paths[n] = paths[current] + [n]
                todo.add(n)
    return None
```

<!--

Performance
--------------------------------------------------------------------------------

Plusieurs stratégies permettent d'améliorer les performances de la recherche
des plus courts chemins, un point qui devient critique quand la taille des
labyrinthes augmente ; notamment le choix de structures de données plus 
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

-->

### Algorithmes

Améliorez ensuite l'algorithme lui-même. On pourra notamment étudier le
classique : 

  - 🎓 <https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra>


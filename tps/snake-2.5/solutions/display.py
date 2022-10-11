# Python Standard Library
import math
import random

random.seed(42)

# Pygame
import pygame as pg

# Scientific stack
# from numpy import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

maze = []
for y in range(30):
    for x in range(30):
        if (x, y) == (0, 0) or random.choices([True, False], [3, 1])[0]:
            maze.append((x, y))
if (29, 29) not in maze:
    maze.append((29, 29))

# Visualization
# ------------------------------------------------------------------------------
def display_maze(maze, path=None, distance=None):
    x_min = 0
    x_max = max(x for (x, y) in maze)
    y_min = 0
    y_max = max(y for (x, y) in maze)

    pg.init()
    clock = pg.time.Clock()
    width, height = ((x_max - x_min + 1) * 20, (y_max - y_min + 1) * 20)
    screen = pg.display.set_mode((width, height))

    while True:
        events = pg.event.get()
        if any(event.type == pg.QUIT for event in events):
            break
        screen.fill((0, 0, 0))
        for x, y in maze:
            pg.draw.rect(screen, (255, 255, 255), (x * 20, y * 20, 20, 20))
        if distance is not None:
            d_max = max(d for d in distance.values())
            for (x, y), d in distance.items():
                pg.draw.rect(
                    screen,
                    (0, int(64 + d / d_max * (255 - 64)), 0),
                    (x * 20, y * 20, 20, 20),
                )
        if path is not None:
            for x, y in path:
                pg.draw.rect(screen, (0, 0, 255), (x * 20 + 5, y * 20 + 5, 10, 10))

        pg.display.update()
        clock.tick(5)

    pg.quit()


# Graphs
# ------------------------------------------------------------------------------
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


# Path Generation
# ------------------------------------------------------------------------------
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


def reachable_path(graph, source):
    vertices, edges, _ = graph
    todo = {source}
    done = set()
    path = {source: [source]}
    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            if n not in done:
                todo.add(n)
                path[n] = path[current] + [n]
        done.add(current)
    return path


def shortest_path(graph, source):
    "Non-greedy version"
    vertices, edges, weight = graph
    distance, path = {}, {}
    todo = {source}
    distance[source] = 0
    path[source] = [source]
    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            d = distance[current] + weight[(current, n)]
            if d < distance.get(n, math.inf):
                distance[n] = d
                path[n] = path[current] + [n]
                todo.add(n)
    return path, distance


graph = maze_to_graph(maze)
# path = reachable_path(graph, source=(0, 0))[(29, 0)]
paths, distance = shortest_path(graph, source=(0, 0))
path = paths[(29, 29)]
display_maze(maze, path, distance=distance)

# # Visualization
# # ------------------------------------------------------------------------------
# def rotate(x1y1, x2y2):
#     "Rotate a segment +90° with respect to its center"
#     x1, y1 = x1y1
#     x2, y2 = x2y2
#     cx, cy = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
#     x3y3 = cx - (y1 - cy), cy + (x1 - cx)
#     x4y4 = cx - (y2 - cy), cy + (x2 - cx)
#     return x3y3, x4y4

# def display_maze(graph, path=None, map=None):
#     vertices, edges, weights = graph
#     width = max(w for (w, h) in vertices) + 1
#     height = max(h for (w, h) in vertices) + 1
#     wh_ratio = width / height
#     fig_width = 14  # inches
#     fig_height = fig_width / wh_ratio
#     fig, axes = plt.subplots(figsize=(fig_width, fig_height))
#     axes.axis("equal")
#     for x in range(width):
#         for y in range(height):
#             for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
#                 xn, yn = x+dx, y+dy
#                 if ((x, y), (xn, yn)) in edges:
#                     style = {"color": "grey", "linestyle": ":"}
#                 else:
#                     style = {"color": "black", "linestyle": "-"}
#                 w1, w2 = rotate((x + 0.5, y + 0.5), (xn + 0.5, yn + 0.5)) # wall segment
#                 axes.plot([w1[0], w2[0]], [w1[1], w2[1]], **style)
#     axes.axis("off")

#     if path:
#         xs = np.array([x for (x, y) in path])
#         ys = np.array([y for (x, y) in path])
#         axes.plot(xs + 0.5, ys + 0.5, "r-")

#     if map:
#         if isinstance(map, set):
#             map = {k: 1.0 for k in map}
#         d_max = max(map.values())
#         cmap = mpl.cm.get_cmap("viridis")

#         for v, d in map.items():
#             dx, dy = 1, 1
#             rect = patches.Rectangle(v, dx, dy, facecolor=cmap(d / d_max))
#             axes.add_patch(rect)


# # Mazes generation
# # ------------------------------------------------------------------------------
# def empty_maze(width, height):
#     vertices = {(i, j) for i in range(width) for j in range(height)}
#     edges = set()
#     for vertex in vertices:
#         i, j = vertex
#         neighbors = {(i + k, j + l) for k, l in [(1, 0), (0, 1), (-1, 0), (0, -1)]}
#         for neighbor in neighbors:
#             if neighbor in vertices:
#                 edges.add((vertex, neighbor))
#     weights = {edge: 1.0 for edge in edges}
#     return vertices, edges, weights

# def full_maze(width, height):
#     vertices, edges, weights = empty_maze(width, height)
#     i = width // 2  # boundary (vertical wall in the middle)
#     right_crossing = {((i - 1, j), (i, j)) for j in range(height)}
#     left_crossing = {((i, j), (i - 1, j)) for j in range(height)}
#     crossing = left_crossing | right_crossing
#     edges = edges - crossing
#     weights = {edge: 1.0 for edge in edges}
#     return vertices, edges, weights

# def punctured_maze(width, height):
#     vertices, edges, weights = full_maze(width, height)
#     i = width // 2  # boundary (vertical wall in the middle)
#     j = 0  # hole in the wall
#     edge_1 = ((i - 1, j), (i, j))
#     edge_2 = ((i, j), (i - 1, j))
#     edges.add(edge_1)
#     edges.add(edge_2)
#     weights[edge_1] = 1.0
#     weights[edge_2] = 1.0
#     return vertices, edges, weights

# def dense_maze(width, height):
#     random.seed(0)
#     vertices = {(i, j) for i in range(width) for j in range(height)}
#     edges = set()
#     todo = {(0, 0)}  # visited but some neighbors not tested yet,
#     done = set()     # all neighbors have been tested.
#     while todo:
#         i, j = current = random.choice(list(todo))
#         neighbors = {(i + k, j + l) for k, l in [(1, 0), (0, 1), (-1, 0), (0, -1)]}
#         # neighbors in the maze and not explored yet
#         candidates = (neighbors & vertices) - done - todo
#         if candidates:
#             new = random.choice(list(candidates))
#             edges.add((current, new))
#             edges.add((new, current))  # both directions are allowed
#             todo.add(new)
#         if len(candidates) <= 1:
#             todo.remove(current)
#             done.add(current)
#     weights = {edge: 1.0 for edge in edges}
#     return vertices, edges, weights

# # Visualize maze examples
# # ------------------------------------------------------------------------------
# # %%
# width, height = 50, 25
# em = empty_maze(width, height)
# display_maze(em)
# wm = full_maze(width, height)
# display_maze(wm)
# pm = punctured_maze(width, height)
# display_maze(pm)
# dm = dense_maze(width, height)
# display_maze(dm)

# # Reachable Sets & Paths
# # ------------------------------------------------------------------------------
# # %%
# def reachable_set(graph, source):
#     vertices, edges, weights = graph
#     todo = {source}
#     done = set()
#     while todo:
#         current = todo.pop()
#         neighbors = {v for v in vertices if (current, v) in edges}
#         for n in neighbors:
#             if n not in done:
#                 todo.add(n)
#         done.add(current)
#     return done

# def reachable_path(graph, source):
#     vertices, edges, weights = graph
#     todo = {source}
#     done = set()
#     path = {source: [source]}
#     while todo:
#         current = todo.pop()
#         neighbors = {v for v in vertices if (current, v) in edges}
#         for n in neighbors:
#             if n not in done:
#                 todo.add(n)
#                 path[n] = path[current] + [n]
#         done.add(current)
#     return path


# # Test reachability functions
# # %%
# source = (0, 0)
# target = (width - 1, height - 1)

# mazes = [em, wm, pm, dm]
# for maze in mazes:
#     reached = reachable_set(maze, source)
#     if target in reached:
#         path = reachable_path(maze, source)[target]
#     else:
#         path = None
#     display_maze(maze, path=path, map=reached)

# # Shortest Path & Distance
# # ------------------------------------------------------------------------------
# # %%
# def shortest_path(graph, source):
#     "Non-greedy version"
#     vertices, edges, weight = graph
#     distance, path = {}, {}
#     todo = {source}
#     distance[source] = 0
#     path[source] = [source]
#     while todo:
#         current = todo.pop()
#         neighbors = {v for v in vertices if (current, v) in edges}
#         for n in neighbors:
#             d = distance[current] + weight[(current, n)]
#             if d < distance.get(n, math.inf):
#                 distance[n] = d
#                 path[n] = path[current] + [n]
#                 todo.add(n)
#     return path, distance

# # Visualize shortest path & distance
# # ------------------------------------------------------------------------------
# # %%
# mazes = [em, wm, pm, dm]
# for maze in mazes:
#     path, distance = shortest_path(maze, source)
#     path = path.get(target)
#     display_maze(maze, path=path, map=distance)

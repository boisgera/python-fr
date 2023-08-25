filename = "mazes/random-maze.py"
file = open(filename, mode="rt", encoding="utf-8")
random_maze_repr = file.read()
file.close()
random_maze = eval(random_maze_repr)

# Pygame
import pygame as pg


# Constants
WIDTH, HEIGHT = 30, 30
CELL_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_background(screen):
    screen.fill(BLACK)

def draw_walls(screen, maze):
    h = CELL_SIZE
    for x, y in maze:
        pg.draw.rect(screen, WHITE, (x * h, y * h, h, h))

def display_maze(maze):
    pg.init()
    pg.display.set_caption("Labyrinthes")
    width_height = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
    screen = pg.display.set_mode(width_height)
    clock = pg.time.Clock()
    while True:
        events = pg.event.get()
        if any(event.type == pg.QUIT for event in events):
            break
        draw_background(screen)
        draw_walls(screen, maze)
        pg.display.update()
        clock.tick(FPS)
    pg.quit()

empty_maze = set()
for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        empty_maze.add((x, y))

empty_maze_repr = repr(empty_maze)
file = open("mazes/empty_maze.py", mode="wt", encoding="utf-8")
file.write(empty_maze_repr)
file.close()

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

def reachable_cells(maze, source):
    vertices, edges, _ = maze_to_graph(maze)
    todo = {source}
    done = set()
    while todo:
        current = todo.pop()
        neighbors = {
            v for v in vertices 
            if (current, v) in edges
        }
        for n in neighbors:
            if n not in done:
                todo.add(n)
        done.add(current)
    return done

LIGHT_GREEN = (128, 255, 128)

def draw_cells(screen):
    h = CELL_SIZE
    for x, y in cells:
        pg.draw.rect(screen, LIGHT_GREEN, (x * h, y * h, h, h))

def display_maze(maze, cells=None):
    pg.init()
    pg.display.set_caption("Labyrinthes")
    width_height = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
    screen = pg.display.set_mode(width_height)
    clock = pg.time.Clock()
    while True:
        events = pg.event.get()
        if any(event.type == pg.QUIT for event in events):
            break
        draw_background(screen)
        draw_walls(screen, maze)
        if cells is not None:
            draw_cells(screen)
        pg.display.update()
        clock.tick(FPS)
    pg.quit()

TOP_LEFT = (0, 0)
cells = reachable_cells(random_maze, source=TOP_LEFT)
display_maze(random_maze, cells=cells)

def path_from(maze, source):
    vertices, edges, _ = maze_to_graph(maze)
    todo = set()
    done = set()
    path = {}
    if source in maze:
       todo.add(source)
       path[source] = [source]
    while todo:
        current = todo.pop()
        neighbors = {
            v for v in vertices 
            if (current, v) in edges
        }
        for n in neighbors:
            if n not in done and n not in todo:
                path[n] = path[current] + [n]
                todo.add(n)
        done.add(current)
    return path

PINK = (255, 128, 128)

def draw_path(screen, path):
    h = CELL_SIZE
    for x, y in path:
        pg.draw.rect(screen, PINK, (x * h, y * h, h, h))

def display_maze(maze, cells=None, path=None):
    pg.init()
    pg.display.set_caption("Labyrinthes")
    width_height = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
    screen = pg.display.set_mode(width_height)
    clock = pg.time.Clock()
    while True:
        events = pg.event.get()
        if any(event.type == pg.QUIT for event in events):
            break
        draw_background(screen)
        draw_walls(screen, maze)
        if cells is not None:
            draw_cells(screen)
        if path is not None:
            draw_path(screen, path)
        pg.display.update()
        clock.tick(FPS)
    pg.quit()

target_to_path = path_from(random_maze, TOP_LEFT)
BOTTOM_RIGHT = (WIDTH - 1, HEIGHT - 1)
path = target_to_path[BOTTOM_RIGHT]
display_maze(random_maze, path=path)

import matplotlib.cm  # matplotlib colormaps

COLORMAP = matplotlib.cm.viridis

def colormap(x):
    x = float(x)
    rgba = COLORMAP(x)
    rgb = rgba[0:3]
    RGB = [min(int(256 * c), 255) for c in rgb]
    return RGB

assert colormap(0.0) == [68, 1, 84]     # purple
assert colormap(0.5) == [32, 145, 140]  # turquoise
assert colormap(1.0) == [254, 231, 36]  # yellow

def draw_map(screen, map):
    h = CELL_SIZE
    v_max = max(v for v in map.values())
    for (x, y), v in map.items():
        pg.draw.rect(
            screen,
            colormap(float(v / v_max)),
            (x * h, y * h, h, h),
        )

def display_maze(maze, cells=None, path=None, map=None):
    pg.init()
    pg.display.set_caption("Labyrinthes")
    width_height = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
    screen = pg.display.set_mode(width_height)
    clock = pg.time.Clock()
    while True:
        events = pg.event.get()
        if any(event.type == pg.QUIT for event in events):
            break
        draw_background(screen)
        draw_walls(screen, maze)
        if cells is not None:
            draw_cells(screen, cells)
        if map is not None:
            draw_map(screen, map)
        if path is not None:
            draw_path(screen, path)
        pg.display.update()
        clock.tick(FPS)
    pg.quit()

map = {
    target: len(path) - 1 
    for target, path in target_to_path.items()
}
display_maze(random_maze, map=map)

import math

def shortest_path_from(maze, source): 
    vertices, edges, weight = maze_to_graph(maze)
    distance, path = {}, {}
    todo = {source}
    distance[source] = 0
    path[source] = [source]
    while todo:
        current = todo.pop()
        neighbors = {
            v for v in vertices 
            if (current, v) in edges
        }
        for n in neighbors:
            d = distance[current] + weight[(current, n)]
            if d < distance.get(n, math.inf):
                distance[n] = d
                path[n] = path[current] + [n]
                todo.add(n)
    return path

target_to_path = shortest_path_from(random_maze, TOP_LEFT)
map = {
    target: len(path) - 1 
    for target, path in target_to_path.items()
}
display_maze(random_maze, map=map)


# Python Standard Library
import math
import random

# NumPy, Matplotlib
import numpy as np
import matplotlib.cm


# Pygame
import pygame as pg


# Constants
WIDTH, HEIGHT = 30, 30
CELL_SIZE = 20
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 128, 128)
GREEN = (0, 255, 0)
COLORMAP = matplotlib.cm.viridis

# Colormap Helper
# ------------------------------------------------------------------------------
def colormap(x):
    x = float(x)
    rgba = COLORMAP(x)
    rgb = rgba[0:3]
    RGB = [min(int(256 * c), 255) for c in rgb]
    return RGB


# ------------------------------------------------------------------------------
def empty_maze():
    maze = set()
    for y in range(WIDTH):
        for x in range(HEIGHT):
            maze.add((x, y))
    return maze


def slit_maze():
    maze = empty_maze()
    x = WIDTH // 2
    y = HEIGHT // 2
    for y_ in range(HEIGHT):
        if y_ != y:
            maze.remove((x, y_))
    return maze


def neighbors(cell):
    x, y = cell
    ns = set()
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # TODO: directions
        n = (x + dx, y + dy)
        if n[0] < 0 or n[0] >= WIDTH:
            break
        if n[1] < 0 or n[1] >= HEIGHT:
            break
        ns.add(n)
    return set(ns)


def dense_maze():
    random.seed(0)
    maze = set()
    todo = [(0, 0)]
    while todo:
        current = random.choice(todo)
        ns = neighbors(current) - set(todo) - maze
        candidates = []
        for n in ns:
            nns = neighbors(n) - {current}
            if not (nns & (set(todo) | maze)):
                candidates.append(n)
        if candidates:
            selected = random.choice(candidates)
            todo.append(selected)
        if len(candidates) <= 1:
            maze.add(current)
            todo.remove(current)
    return maze


def random_maze():
    maze = set()
    seed = 42
    random.seed(seed)
    for y in range(30):
        for x in range(30):
            if random.choices([True, False], [0.75, 0.25])[0]:
                maze.add((x, y))
    # When seed=42, the top-left and bottom-right corners are empty.
    assert (0, 0) in maze and (WIDTH - 1, HEIGHT - 1) in maze
    return maze


# Visualization
# ------------------------------------------------------------------------------
def display_maze(maze, path=None, map=None):
    pg.init()
    pg.display.set_caption("Labyrinthes")
    screen = pg.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
    clock = pg.time.Clock()
    while True:
        events = pg.event.get()
        if any(event.type == pg.QUIT for event in events):
            break
        if any(event.type == pg.KEYDOWN and event.key == pg.K_s for event in events):
            pg.image.save(screen, "screenshot.jpg")
        draw_background(screen)
        draw_maze(screen, maze)
        if map is not None:
            draw_map(screen, map)
        if path is not None:
            draw_path(screen, path)
        pg.display.update()
        clock.tick(FPS)
    pg.quit()


def draw_background(screen):
    screen.fill(BLACK)


def draw_maze(screen, maze):
    h = CELL_SIZE
    for x, y in maze:
        pg.draw.rect(screen, WHITE, (x * h, y * h, h, h))


def draw_path(screen, path):
    h = CELL_SIZE
    for x, y in path:
        pg.draw.rect(screen, PINK, (x * h, y * h, h, h))


def draw_map(screen, map, v_max=None):
    h = CELL_SIZE
    if v_max is None:
        v_max = max(v for v in map.values())
    for (x, y), v in map.items():
        pg.draw.rect(
            screen,
            colormap(float(v / v_max)),
            (x * h, y * h, h, h),
        )


def draw_cells(screen, cells, color):
    for x, y in cells:
        pg.draw.rect(screen, color, (x * 20, y * 20, 20, 20))


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
def reachable_set(maze, source):
    vertices, edges, _ = maze_to_graph(maze)
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


def path_from(maze, source, display=False):
    vertices, edges, _ = maze_to_graph(maze)
    todo = {source}
    done = set()
    path = {source: [source]}

    if display:
        pg.init()
        pg.display.set_caption("Path Planning")
        screen = pg.display.set_mode((30 * 20, 30 * 20))

        clock = pg.time.Clock()

    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            if n not in done and n not in todo:
                todo.add(n)
                path[n] = path[current] + [n]
        done.add(current)
        if display:
            events = pg.event.get()
            if any(event.type == pg.QUIT for event in events):
                break
            draw_background(screen)
            draw_maze(screen, maze)
            map = {loc: len(path[loc]) for loc in (done | todo)}
            draw_map(screen, map, v_max=(WIDTH + HEIGHT))
            pg.display.update()
            clock.tick(FPS)

    if display:
        while True:
            events = pg.event.get()
            if any(event.type == pg.QUIT for event in events):
                break
            clock.tick(FPS)
        pg.quit()

    return path


def shortest_path_from(maze, source, display=False):
    vertices, edges, weight = maze_to_graph(maze)
    distance, path = {}, {}
    todo = {source}
    distance[source] = 0
    path[source] = [source]

    if display:
        pg.init()
        pg.display.set_caption("Path Planning")
        screen = pg.display.set_mode((30 * 20, 30 * 20))

        clock = pg.time.Clock()

    while todo:
        current = todo.pop()
        neighbors = {v for v in vertices if (current, v) in edges}
        for n in neighbors:
            d = distance[current] + weight[(current, n)]
            if d < distance.get(n, math.inf):
                distance[n] = d
                path[n] = path[current] + [n]
                todo.add(n)
        if display:
            events = pg.event.get()
            if any(event.type == pg.QUIT for event in events):
                break
            draw_background(screen)
            draw_maze(screen, maze)
            draw_map(screen, map=distance, v_max=(WIDTH + HEIGHT))
            pg.display.update()
            clock.tick(FPS)

    if display:
        while True:
            events = pg.event.get()
            if any(event.type == pg.QUIT for event in events):
                break
            clock.tick(FPS)
        pg.quit()

    return path


if __name__ == "__main__":
    maze = random_maze()
    path = path_from(maze, source=(0, 0))
    display_maze(maze)  # , map={k: len(p) - 1 for k, p in path.items()})
    # map = {cell: len(path) for cell, path in paths.items()}
    # display_maze(maze, path=paths[(WIDTH - 1, HEIGHT - 1)], map=map)

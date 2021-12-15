import heapq

import numpy as np


class Node:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.risk = grid[x % grid.shape[0], y % grid.shape[1]]
        self.risk = (self.risk + x//grid.shape[0] + y//grid.shape[1] - 1) % 9 + 1
        self.complete = False
        self.distance = None
        self.goal = x == grid.shape[0] * 5 - 1 and y == grid.shape[1] * 5 - 1

    def __lt__(self, other):
        return self.distance < other.distance

with open("input.txt") as f:
    input = [list(map(int, list(x))) for x in f.read().splitlines()]
    grid = np.array(input)

    node_grid = np.array([])
    nodes = []
    for x in range(grid.shape[1] * 5):
        for y in range(grid.shape[0] * 5):
            node = Node(x, y, grid)
            nodes.append(node)

    node_grid = np.array(nodes)
    node_grid = node_grid.reshape(grid.shape[0] * 5, grid.shape[1] * 5)

def get_adjacents(coords, shape):
    dX = [0, -1, 0, 1]
    dY = [-1, 0, 1, 0]
    x, y = coords

    for i in range(4):
        if 0 <= (x + dX[i]) < shape[0] and 0 <= (y + dY[i]) < shape[1]:
            yield x + dX[i], y + dY[i]


node_grid[0, 0].distance = 0

nodes_to_check = [node_grid[0, 0]]
heapq.heapify(nodes_to_check)
while True:
    closest = heapq.heappop(nodes_to_check)

    if closest.goal:
        print(closest.distance)
        break

    for adjacent in get_adjacents((closest.x, closest.y), node_grid.shape):
        adjacent_node = node_grid[adjacent]
        if adjacent_node.complete:
            continue

        if adjacent_node.distance is None or adjacent_node.distance > closest.distance + adjacent_node.risk:
            adjacent_node.distance = closest.distance + adjacent_node.risk
            heapq.heappush(nodes_to_check, adjacent_node)

    closest.complete = True

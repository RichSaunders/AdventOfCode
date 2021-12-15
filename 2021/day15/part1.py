import numpy as np

dX = [0, -1, 0, 1]
dY = [-1, 0, 1, 0]


class Node:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.risk = grid[x, y]
        self.complete = False
        self.distance = None
        self.goal = x == grid.shape[0]-1 and y == grid.shape[1]-1


    def __str__(self):
        return str(self.distance)

    def __repr__(self):
        return str(self.distance)


with open("input.txt") as f:
    input = [list(map(int, list(x))) for x in f.read().splitlines()]
    grid = np.array(input)

    node_grid = np.array([])
    for y in range(grid.shape[1]):
        for x in range(grid.shape[0]):
            node = Node(x, y, grid)
            node_grid = np.append(node_grid, node)

    node_grid = node_grid.reshape(grid.shape)


def get_adjacents(coords, shape):
    dX = [0, -1, 0, 1]
    dY = [-1, 0, 1, 0]

    x, y = coords

    for i in range(4):
        if 0 <= (x + dX[i]) < shape[0] and 0 <= (y + dY[i]) < shape[1]:
            yield x + dX[i], y + dY[i]


def find_closest_incomplete(node_grid):
    closest = None
    for y in range(node_grid.shape[1]):
        for x in range(node_grid.shape[0]):
            if node_grid[x, y].distance is not None and not node_grid[x, y].complete:
                if closest is None or node_grid[x, y].distance < node_grid[closest].distance:
                    closest = (x, y)

    return closest


node_grid[0, 0].distance = 0

while True:
    closest = find_closest_incomplete(node_grid)
    closest_node = node_grid[closest]
    if closest_node.goal:
        print(node_grid.transpose())

        print(closest_node.distance)
        break

    for adjacent in get_adjacents(closest, node_grid.shape):
        adjacent_node = node_grid[adjacent]
        if adjacent_node.complete:
            continue

        if adjacent_node.distance is None or adjacent_node.distance > closest_node.distance + adjacent_node.risk:
            adjacent_node.distance = closest_node.distance + adjacent_node.risk

    closest_node.complete = True

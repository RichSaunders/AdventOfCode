import heapq

class Node:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.risk = grid[x % len(grid[0])][y % len(grid)]
        self.risk = (self.risk + x//len(grid[0]) + y//len(grid) - 1) % 9 + 1
        self.complete = False
        self.distance = None
        self.goal = x == len(grid[0]) * 5 - 1 and y == len(grid) * 5 - 1

    def __lt__(self, other):
        return self.distance < other.distance

with open("input.txt") as f:
    grid = [list(map(int, list(x))) for x in f.read().splitlines()]

    node_grid = []
    for x in range(len(grid[0]) * 5):
        row = []
        for y in range(len(grid) * 5):
            node = Node(x, y, grid)
            row.append(node)
        node_grid.append(row)

def get_adjacents(coords, width, height):
    dX = [0, -1, 0, 1]
    dY = [-1, 0, 1, 0]
    x, y = coords

    for i in range(4):
        if 0 <= (x + dX[i]) < width and 0 <= (y + dY[i]) < height:
            yield x + dX[i], y + dY[i]


node_grid[0][0].distance = 0

nodes_to_check = [node_grid[0][0]]
heapq.heapify(nodes_to_check)
while True:
    closest = heapq.heappop(nodes_to_check)

    if closest.goal:
        print(closest.distance)
        break

    for x, y in get_adjacents((closest.x, closest.y), len(node_grid[0]), len(node_grid)):
        adjacent_node = node_grid[x][y]
        if adjacent_node.complete:
            continue

        if adjacent_node.distance is None or adjacent_node.distance > closest.distance + adjacent_node.risk:
            adjacent_node.distance = closest.distance + adjacent_node.risk
            heapq.heappush(nodes_to_check, adjacent_node)

    closest.complete = True

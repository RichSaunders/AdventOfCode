adjacent = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def countOccupied(x, y, layout):
    occupied = 0
    for adj in adjacent:
        mult = 0
        while True:
            mult += 1
            coords = (y + adj[0] * mult, x + adj[1] * mult)
            # Check out of bounds
            if coords[0] < 0 or coords[0] >= len(layout) or coords[1] < 0 or coords[1] >= len(layout[y]):
                break
            elif layout[coords[0]][coords[1]] == "#":
                occupied += 1
                break
            elif layout[coords[0]][coords[1]] == "L":
                break

    return occupied


with open("input.txt", "r") as f:
    input = f.read()
layout = input.splitlines()

while True:
    newLayout = []
    for y in range(len(layout)):
        newRow = []
        for x in range(len(layout[y])):
            if layout[y][x] != ".":
                occupied = countOccupied(x, y, layout)

                if occupied == 0:
                    newRow += "#"
                elif occupied >= 5:
                    newRow += "L"
                else:
                    newRow += layout[y][x]
            else:
                newRow += "."

        newLayout.append(newRow)

    if layout == newLayout:
        print(sum([sum(l.count("#") for l in newLayout)]))
        break
    else:
        layout = newLayout

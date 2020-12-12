adjacent = [
    (-1, -1),
    ( 0, -1),
    ( 1, -1),
    (-1,  0),
    ( 1,  0),
    (-1,  1),
    ( 0,  1),
    ( 1,  1),
]

with open("input.txt", "r") as f:
    input = f.read()
layout = input.splitlines()

i = 0
while True:
    i += 1
    newLayout = []
    for y in range(len(layout)):
        newRow = []
        for x in range(len(layout[y])):
            if layout[y][x] != ".":
                occupied = 0
                for adj in adjacent:
                    if y+adj[0] < 0 or y+adj[0] >= len(layout) or x+adj[1] < 0 or x+adj[1] >= len(layout[y]):
                        continue
                    if layout[y+adj[0]][x+adj[1]] == "#":
                        occupied += 1

                if occupied == 0:
                    newRow += "#"
                elif occupied >= 4:
                    newRow += "L"
                else:
                    newRow += layout[y][x]
            else:
                newRow += "."

        newLayout.append(newRow)

    if layout == newLayout:
        print(sum([sum(l.count("#") for l in newLayout)]))
        print(i)
        break
    else:
        layout = newLayout
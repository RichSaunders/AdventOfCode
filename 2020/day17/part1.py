import copy

l = (-1, 0, 1)
adjacents = [(x, y, z) for x in l for y in l for z in l]
adjacents.remove((0, 0, 0))

with open("input.txt", "r") as f:
    input = f.read()

activeCubes = []

for y, line in enumerate(input.splitlines()):
    for x, state in enumerate(line):
        if state == "#":
            activeCubes.append((x, y, 0))

minX = -1
maxX = 8
minY = -1
maxY = 8
minZ = -1
maxZ = 1

for _ in range(6):
    print(len(activeCubes))
    newActiveCubes = copy.deepcopy(activeCubes)
    for z in range(minZ, maxZ+1):
        for y in range(minY, maxY+1):
            for x in range(minX, maxX+1):
                activeAdjacents = 0
                for adjacent in adjacents:
                    if (x+adjacent[0], y+adjacent[1], z+adjacent[2]) in activeCubes:
                        activeAdjacents += 1

                active = (x, y, z) in activeCubes
                if active and not (2 <= activeAdjacents <= 3):
                    newActiveCubes.remove((x, y, z))

                if not active and activeAdjacents == 3:
                    newActiveCubes.append((x, y, z))
                    if x-1 < minX:
                        minX = x-1
                    if x+1 > maxX:
                        maxX = x+1
                    if y-1 < minY:
                        minY = y-1
                    if y+1 > maxY:
                        maxY = y+1
                    if z-1 < minX:
                        minZ = z-1
                    if z+1 > maxZ:
                        maxZ = z+1

    activeCubes = newActiveCubes

print(len(activeCubes))

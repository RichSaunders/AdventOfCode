import numpy as np

with open("input.txt") as f:
    input = f.read().splitlines()
    input = [list(map(int, x)) for x in input]
    octopi = np.array(input)

dX = [-1, 0, 1, -1, 1, -1, 0, 1]
dY = [-1, -1, -1, 0, 0, 1, 1, 1]

flashes = 0
for _ in range(100):
    octopi += 1

    charged = []
    for x in range(octopi.shape[0]):
        for y in range(octopi.shape[1]):
            if octopi[x,y] == 10:
                charged.append((x,y))

    for octopus in charged:
        for i in range(8):
            x = octopus[0]+dX[i]
            y = octopus[1]+dY[i]
            if 0 <= x < octopi.shape[0] and 0 <= y < octopi.shape[1]:
                octopi[x, y] += 1
                if octopi[x,y] == 10:
                    charged.append((x,y))

    for octopus in charged:
        octopi[octopus] = 0

    flashes += len(charged)

print(flashes)

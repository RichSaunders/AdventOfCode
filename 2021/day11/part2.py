import numpy as np

with open("input.txt") as f:
    input = f.read().splitlines()
    input = [list(map(int, x)) for x in input]
    octopi = np.array(input)

dX = [-1, 0, 1, -1, 1, -1, 0, 1]
dY = [-1, -1, -1, 0, 0, 1, 1, 1]

for j in range(1000):
    charged = []
    for x in range(octopi.shape[0]):
        for y in range(octopi.shape[1]):
            if octopi[x,y] >= 9:
                charged.append((x,y))

    for octopus in charged:
        for i in range(8):
            x = octopus[0]+dX[i]
            y = octopus[1]+dY[i]
            if 0 <= x < octopi.shape[0] and 0 <= y < octopi.shape[1]:
                octopi[x, y] += 1
                if octopi[x,y] == 9:
                    charged.append((x,y))

    if len(charged) == octopi.shape[0] * octopi.shape[1]:
        print(j+1)
        break

    octopi += 1

    for octopus in charged:
        octopi[octopus] = 0

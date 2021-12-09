import numpy as np

with open("input.txt") as f:
    input = f.read().splitlines()
    input = [list(map(int, x)) for x in input]
    floor = np.array(input)

minima = np.full(floor.shape, True)

for x in range(floor.shape[0]):
    for y in range(floor.shape[1]):
        here = floor[x, y]
        if x < floor.shape[0]-1:
            if floor[x+1, y] < here:
                minima[x, y] = False
            else:
                minima[x+1, y] = False

        if y < floor.shape[1]-1:
            if floor[x, y+1] < here:
                minima[x, y] = False
            else:
                minima[x, y+1] = False

sum = 0
where = np.where(minima==True)
for i in range(len(where[0])):
    sum += floor[where[0][i],where[1][i]]+1

print(sum)

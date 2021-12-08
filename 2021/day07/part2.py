import numpy as np

with open("input.txt") as f:
    input = f.read().split(",")
    input = np.array([int(x) for x in input])

def triangle(x):
    return (x*x+x)/2

mean = np.mean(input)
fuels = {}
for i in range(max(input)):
    fuels[i] = sum(np.array((list(map(triangle, abs(input-i))))))
print(min(fuels.values()))

import numpy as np

with open("input.txt") as f:
    input = f.read().split(",")
    input = np.array([int(x) for x in input])

median = np.median(input)
median = round(median)

fuel = sum(abs(input-median))
print(fuel)

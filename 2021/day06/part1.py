import numpy as np

with open("input.txt") as f:
    input = f.read().split(",")
    input = [int(x) for x in input]

fish = np.array(input)
for i in range(80):
    new = len(fish[fish==0])
    fish = fish[fish!=0]
    fish = np.append(fish, [7]*new + [9]*new)
    fish = fish-1

print(len(fish))

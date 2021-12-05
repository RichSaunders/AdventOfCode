with open("input.txt") as f:
    input = f.readlines()
    input = [list(x.strip()) for x in input]

# sums = [input[j][i] for i in range(len(input[0])) for j in range(len(input))]

sums = []
for i in range(len(input[0])):
    sums.append(0)
    for j in range(len(input)):
        sums[i] += int(input[j][i])

gamma = ["0" if x < len(input)/2 else "1" for x in sums]
dGamma = int("".join(gamma), 2)
epsilon = ["0" if x > len(input)/2 else "1" for x in sums]
dEpsilon = int("".join(epsilon), 2)

print(dGamma*dEpsilon)
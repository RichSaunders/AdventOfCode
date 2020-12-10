with open("input.txt", "r") as f:
    input = f.read()
adapters = [int(x) for x in input.splitlines()]
adapters.sort()
# Add the start and end points, which are 0 and the largest value + 3
adapters = [0] + adapters + [adapters[-1] + 3]

# Going backwards, check which adapters can follow each one, and add up the number of paths forwards from there
permutations = [0] * (len(adapters)-1) + [1]
for i in reversed(range(len(adapters)-1)):
    permutations[i] += permutations[i+1]

    if i + 2 < len(adapters) and adapters[i+2] - adapters[i] <= 3:
        permutations[i] += permutations[i+2]

        if i + 3 < len(adapters) and adapters[i+3] - adapters[i] <= 3:
            permutations[i] += permutations[i+3]

print(permutations[0])

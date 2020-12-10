with open("input.txt", "r") as f:
    input = f.read()
adapters = [int(x) for x in input.splitlines()]
adapters.sort()
adapters = [0] + adapters + [adapters[-1] + 3]

# Build out a list of possible next adapters for each one
combinations = []
for i in range(len(adapters) - 1):
    indexes = []

    if i + 1 < len(adapters) and adapters[i + 1] - adapters[i] < 4:
        indexes.append(i + 1)

        if i + 2 < len(adapters) and adapters[i + 2] - adapters[i] < 4:
            indexes.append(i + 2)

            if i + 3 < len(adapters) and adapters[i + 3] - adapters[i] < 4:
                indexes.append(i + 3)

    combinations.append(indexes)

# Going backwards, build out list of how many possibilities there are from that point
# We know which adapters can follow which, so just add up the possibilities
permutations = [1] * len(adapters)
for i in reversed(range(len(combinations))):
    permutations[i] = sum([permutations[x] for x in combinations[i]])

print(permutations[0])

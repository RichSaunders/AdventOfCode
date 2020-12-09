import itertools

with open("input.txt", "r") as f:
    input = f.read()
numbers = [int(x) for x in input.splitlines()]

for i in range(25, len(numbers)):
    for x, y in itertools.combinations(numbers[i-25:i], 2):
        if x + y == numbers[i]:
            break
    else:
        print(numbers[i])
        break

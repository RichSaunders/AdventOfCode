import itertools

with open("input.txt", "r") as f:
    input = f.read()
numbers = [int(x) for x in input.splitlines()]

i = 0
n = 0
for i in range(25, len(numbers)):
    for x, y in itertools.combinations(numbers[i-25:i], 2):
        if x + y == numbers[i]:
            break
    else:
        n = numbers[i]
        break

found = False
for j in range(i):
    for k in range(j+1, i):
        if sum(numbers[j:k+1]) == n:
            print(min(numbers[j:k+1]) + max(numbers[j:k+1]))
            found = True
            break
        elif sum(numbers[j:k+1]) > n:
            break

    if found:
        break

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

start = 0
end = 1
while sum(numbers[start:end]) != n:
    if sum(numbers[start:end]) < n:
        end += 1
    elif sum(numbers[start:end]) > n:
        start += 1

print(min(numbers[start:end]) + max(numbers[start:end]))

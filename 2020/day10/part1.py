with open("input.txt", "r") as f:
    input = f.read()
numbers = [int(x) for x in input.splitlines()]
numbers.sort()
numbers = [0] + numbers

diffs = [0, 0, 0]
for i in range(len(numbers)-1):
    delta = numbers[i+1] - numbers[i]
    diffs[delta-1] += 1

diffs[2] += 1

print(diffs[0]*diffs[2])

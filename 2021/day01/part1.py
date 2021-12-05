with open("input.txt") as f:
    input = [int(depth) for depth in f.readlines()]

count = 0
for i in range(len(input)-1):
    if input[i+1] > input[i]:
        count += 1

print(count)
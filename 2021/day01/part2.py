def rollingAverage(i, input):
    sum = input[i-1] + input[i] + input[i+1]
    return sum/3

with open("input.txt") as f:
    input = [int(depth) for depth in f.readlines()]

count = 0
for i in range(1, len(input)-2):
    if rollingAverage(i+1, input) > rollingAverage(i, input):
        count += 1

print(count)
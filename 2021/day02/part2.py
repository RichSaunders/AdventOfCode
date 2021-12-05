with open("input.txt") as f:
    input = [depth.split() for depth in f.readlines()]
    input = [(x, int(y)) for x, y in input]

position = [0, 0]
aim = 0
for instruction, distance in input:
    if instruction == "forward":
        position[0] += distance
        position[1] += distance*aim
    elif instruction == "down":
        aim += distance
    elif instruction == "up":
        aim -= distance

print(position[0] * position[1])

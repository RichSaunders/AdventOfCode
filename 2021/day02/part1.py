with open("input.txt") as f:
    input = [instruction.split() for instruction in f.readlines()]
    input = [(x, int(y)) for x, y in input]

position = [0, 0]
for instruction, distance in input:
    if instruction == "forward":
        position[0] += distance
    elif instruction == "down":
        position[1] += distance
    elif instruction == "up":
        position[1] -= distance

print(position[0] * position[1])

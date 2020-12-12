cardinals = {
    0: "N",
    1: "E",
    2: "S",
    3: "W",
}

with open("input.txt", "r") as f:
    input = f.read()
instructions = [(x[0], int(x[1:])) for x in input.splitlines()]

facing = 1
location = [0, 0]
for instruction, distance in instructions:

    if instruction == "F":
        instruction = cardinals[facing]

    if instruction == "N":
        location[1] += distance
    elif instruction == "E":
        location[0] += distance
    elif instruction == "S":
        location[1] -= distance
    elif instruction == "W":
        location[0] -= distance

    elif instruction == "R":
        facing = (facing + (distance / 90)) % 4
    elif instruction == "L":
        facing = (facing - (distance / 90)) % 4

print(location)
print(abs(location[0]) + abs(location[1]))

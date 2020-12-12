with open("input.txt", "r") as f:
    input = f.read()
instructions = [(x[0], int(x[1:])) for x in input.splitlines()]

shipLocation = [0, 0]
waypointLocation = [10, 1]
for instruction, distance in instructions:

    if instruction == "F":
        shipLocation[0] += waypointLocation[0] * distance
        shipLocation[1] += waypointLocation[1] * distance

    elif instruction == "N":
        waypointLocation[1] += distance
    elif instruction == "E":
        waypointLocation[0] += distance
    elif instruction == "S":
        waypointLocation[1] -= distance
    elif instruction == "W":
        waypointLocation[0] -= distance

    elif instruction == "R":
        for i in range(distance//90):
            waypointLocation = [waypointLocation[1], -1*waypointLocation[0]]
    elif instruction == "L":
        for i in range(distance//90):
            waypointLocation = [-1*waypointLocation[1], waypointLocation[0]]

print(shipLocation)
print(abs(shipLocation[0]) + abs(shipLocation[1]))

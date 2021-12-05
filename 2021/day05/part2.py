import numpy as np

def processInput():
    with open("input.txt") as f:
        input = f.readlines()

    instructions = []
    for instruction in input:
        start, end = instruction.split(" -> ")
        startX, startY = start.split(",")
        endX, endY = end.split(",")
        instructions.append(((int(startX), int(startY)), (int(endX), int(endY))))

    return instructions

def getDelta(start, end):
    if start < end:
        return 1
    elif start > end:
        return -1
    else:
        return 0

def applyInstruction(map, instruction):
    xD = getDelta(instruction[0][0], instruction[1][0])
    yD = getDelta(instruction[0][1], instruction[1][1])

    position = instruction[0]
    while position != instruction[1]:
        map[position] += 1
        position = (position[0]+xD, position[1]+yD)
    map[instruction[1]] += 1

    return map

instructions = processInput()
map = np.zeros((1000, 1000))
for instruction in instructions:
    applyInstruction(map, instruction)

print(np.count_nonzero(map>=2))

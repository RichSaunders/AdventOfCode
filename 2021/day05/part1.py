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

def applyInstruction(map, instruction):
    if instruction[0][0] == instruction[1][0]:
        x = instruction[0][0]
        start = min(instruction[0][1], instruction[1][1])
        end = max(instruction[0][1], instruction[1][1])
        for y in range(start, end+1):
            map[x,y] += 1

    elif instruction[0][1] == instruction[1][1]:
        y = instruction[0][1]
        start = min(instruction[0][0], instruction[1][0])
        end = max(instruction[0][0], instruction[1][0])
        for x in range(start, end+1):
            map[x,y] += 1
    return map

instructions = processInput()
map = np.zeros((1000, 1000))
for instruction in instructions:
    applyInstruction(map, instruction)

print(map)
print(np.count_nonzero(map>=2))

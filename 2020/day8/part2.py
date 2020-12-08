with open("input.txt", "r") as f:
    input = f.read()

def flipInstruction(instructions, n):
    if instructions[n][0] == "jmp":
        instructions[n][0] = "nop"
    elif instructions[n][0] == "nop":
        instructions[n][0] = "jmp"

instructions = []
for line in input.splitlines():
    command, n = line.split()
    instructions.append([command, int(n)])

for i in range(len(instructions)):
    flipInstruction(instructions, i)

    instructionLog = [False] * len(instructions)

    accumulator = 0
    j = 0
    while j < len(instructions):
        if instructionLog[j] is True:
            break
        instructionLog[j] = True

        if instructions[j][0] == "acc":
            accumulator += instructions[j][1]
            j += 1
        elif instructions[j][0] == "jmp":
            j += instructions[j][1]
        elif instructions[j][0] == "nop":
            j += 1
    else:
        print(accumulator)
        print(i)
        break

    flipInstruction(instructions, i)

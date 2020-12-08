with open("input.txt", "r") as f:
    input = f.read()

instructions = []
for line in input.splitlines():
    command, n = line.split()
    instructions.append((command, int(n)))

instructionLog = [False] * len(instructions)

accumulator = 0
i = 0
while i < len(instructions):
    if instructionLog[i] is True:
        break
    instructionLog[i] = True

    if instructions[i][0] == "acc":
        accumulator += instructions[i][1]
        i += 1
    elif instructions[i][0] == "jmp":
        i += instructions[i][1]
    elif instructions[i][0] == "nop":
        i += 1

print(accumulator)

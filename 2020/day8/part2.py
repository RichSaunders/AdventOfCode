import copy

with open("input.txt", "r") as f:
    input = f.read()

def execute(instructions, log, i, accumulator, first):
    while i < len(instructions):
        if log[i] is True:
            break
        log[i] = True

        instruction = instructions[i]

        if instructions[i][0] == "acc":
            accumulator += instruction[1]
            i += 1

        elif instructions[i][0] == "jmp":
            if first:
                instructions2 = copy.deepcopy(instructions)
                instructions2[i][0] = "nop"
                result = execute(instructions2, copy.deepcopy(log), i+1, accumulator, False)
                if result is not None:
                    return result

            i += instruction[1]

        elif instructions[i][0] == "nop":
            if first:
                instructions2 = copy.deepcopy(instructions)
                instructions2[i][0] = "jmp"
                result = execute(instructions2, copy.deepcopy(log), i+instruction[1], accumulator, False)
                if result is not None:
                    return result

            i += 1
    else:
        return accumulator
    return None

instructions = []
for line in input.splitlines():
    command, n = line.split()
    instructions.append([command, int(n)])

instructionLog = [False] * len(instructions)

print(execute(instructions, instructionLog, 0, 0, True))

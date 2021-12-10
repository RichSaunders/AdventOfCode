with open("input.txt") as f:
    input = f.read().splitlines()

opening = "([{<"
closing = ")]}>"

scoring = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def chunk(line):
    if len(line) < 2:
        return "", True

    open = line[0]
    while line[1] in opening:
        new_line, valid = chunk(line[1:])
        line = line[0] + new_line
        if not valid:
            return new_line, valid

        if len(line) < 2:
            return line, True

    if line[1] in closing:
        if opening.index(open) == closing.index(line[1]):
            return line[2:], True
        else:
            return line[1], False

score = 0
for line in input:
    returned, valid = chunk(line)
    if not valid:
        score += scoring[returned]

print(score)

with open("input.txt") as f:
    input = f.read().splitlines()

opening = "([{<"
closing = ")]}>"


def chunk(line):
    while line and line[0] in opening:
        if len(line) < 2:
            return line, True

        open = line[0]
        while line[1] in opening:
            new_line, valid = chunk(line[1:])
            line = line[0] + new_line
            if not valid:
                return new_line, valid

            if len(line) < 2:
                return line, True

            for c in line:
                if c in closing:
                    break
            else:
                return line, True

        if line[1] in closing:
            if opening.index(open) == closing.index(line[1]):
                line = line[2:]
            else:
                return line[1], False

    return line, True

scores = []
for line in input:
    returned, valid = chunk(line)
    if valid:
        score = 0
        for c in returned[::-1]:
            score *= 5
            score += opening.index(c)+1

        scores.append(score)

print(sorted(scores)[len(scores)//2])

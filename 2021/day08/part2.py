#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666


with open("input.txt") as f:
    input = f.read().splitlines()
    input = [x.split(" | ") for x in input]
    input = [(x[0].split(), x[1].split()) for x in input]

sum = 0
for clues, signal in input:
    solved = {}
    segments = {}
    for clue in clues:
        # A digit with 2 segments can only be a 1
        if len(clue) == 2:
            solved[1] = "".join(sorted(clue))

        # A digit with 3 segments can only be a 7
        elif len(clue) == 3:
            solved[7] = "".join(sorted(clue))

        # A digit with 4 segments can only be a 4
        elif len(clue) == 4:
            solved[4] = "".join(sorted(clue))

        # A digit with 7 segments can only be an 8
        elif len(clue) == 7:
            solved[8] = "".join(sorted(clue))

    for clue in clues:
        # A digit with 6 segments can be a 0, 6 or 9
        if len(clue) == 6:
            # If the missing digit in a 6 segment digit is part of a 1, it must be a 6
            for i, segment in enumerate(solved[1]):
                if segment not in clue:
                    solved[6] = "".join(sorted(clue))
                    segments[2] = segment

                    segments[5] = solved[1][1-i]

                    break
            else:
                # If the missing digit in a 6 segment digit is part of a 4 but not a 1, it must be a 6
                for segment in solved[4]:
                    if segment not in clue:
                        solved[0] = "".join(sorted(clue))
                        segments[3] = segment
                        break
                # Otherwise it must be a 0
                else:
                    solved[9] = "".join(sorted(clue))
                    for segment in "abcdefg":
                        if segment not in clue:
                            segments[4] = segment

    for clue in clues:
        # A digit with 5 segments can be a 2, 3 or 5
        if len(clue) == 5:
            # If a 5 segment digit is missing the top right segment, it must be a 5
            if segments[2] not in clue:
                solved[5] = "".join(sorted(clue))
            # If a 5 segment digit is missing the bottom right segment, it must be a 2
            elif segments[5] not in clue:
                solved[2] = "".join(sorted(clue))
            # Otherwise it must be a 3
            else:
                solved[3] = "".join(sorted(clue))

    solution = []
    for digit in signal:
        digit = "".join(sorted(digit))
        for k, v in solved.items():
            if digit == v:
                solution.append(k)
                break

    sum += int(''.join(map(str, solution)))

print(sum)

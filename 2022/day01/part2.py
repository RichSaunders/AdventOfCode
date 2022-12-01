with open("input.txt") as f:
    input = [line[:-1] for line in f.readlines()]

elves = [0]
for item in input:
    if item == "":
        elves.append(0)
    else:
        elves[-1] += int(item)

print(sum(sorted(elves, reverse=True)[:3]))
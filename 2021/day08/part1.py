with open("input.txt") as f:
    input = f.read().splitlines()
    input = [x.split(" | ") for x in input]
    input = [(x[0].split(), x[1].split()) for x in input]

count = 0
for x in input:
    for y in x[1]:
        if len(y) in (2, 3, 4, 7):
            count += 1

print(count)
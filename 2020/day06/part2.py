with open("input.txt", "r") as f:
    input = f.read()
groups = input.split("\n\n")

sum = 0
for group in groups:
    passengers = group.splitlines()
    x = 0
    for question in passengers[0]:
        for passenger in passengers[1:]:
            if question not in passenger:
                break
        else:
            x += 1

    sum += x

print(sum)
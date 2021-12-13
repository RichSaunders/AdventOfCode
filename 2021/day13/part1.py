with open("input.txt") as f:
    input = f.read().splitlines()
    dots = [x.split(",") for x in input if "," in x]
    dots = [(int(x), int(y)) for x, y in dots]

    folds = [x[11:].split("=") for x in input if "=" in x]
    folds = [(axis, int(z)) for axis, z in folds]

new_dots = set()
axis, z = folds[0]
for x, y in dots:
    if axis == "x":
        if x > z:
            x = z-(x-z)
    elif axis == "y":
        if y > z:
            y = z-(y-z)
    new_dots.add((x, y))

print(len(dots))

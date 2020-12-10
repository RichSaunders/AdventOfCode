with open("input.txt", "r") as f:
    input = f.read()
rows = input.splitlines()

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

result = 1
for slope in slopes:
    trees = 0
    x = 0
    for y in range(0, len(rows), slope[1]):
        row = rows[y]
        if row[x%len(row)] == "#":
            trees += 1

        x += slope[0]

    result *= trees

print(result)
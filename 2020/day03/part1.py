with open("input.txt", "r") as f:
    input = f.read()
rows = input.splitlines()

trees = 0
x = 0
for row in rows:
    if row[x%len(row)] == "#":
        trees += 1

    x += 3

print(trees)
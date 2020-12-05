with open("input.txt", "r") as f:
    input = f.read()
bsps = input.splitlines()

seats = []
for bsp in bsps:
    minR = 0
    maxR = 127
    minC = 0
    maxC = 7
    for c in bsp:
        if c == "F":
            maxR = (minR + maxR - 1) / 2
        elif c == "B":
            minR = (minR + maxR + 1) / 2
        elif c == "L":
            maxC = (minC + maxC - 1) / 2
        elif c == "R":
            minC = (minC + maxC + 1) / 2
    row = minR
    column = minC
    seatID = row * 8 + column
    seats.append(seatID)

print(max(seats))

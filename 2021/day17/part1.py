import re

with open("input.txt") as f:
    match = re.match("target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)", f.read())
    y_range = [int(match.group(3)), int(match.group(4))]

def triangle(x):
    return 0.5*(x**2 + x)

y_velocity = y_range[0]*-1 - 1
print(triangle(y_velocity))

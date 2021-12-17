import re

with open("input.txt") as f:
    match = re.match("target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)", f.read())
    y_range = [int(match.group(3)), int(match.group(4))]

y_velocity = y_range[0]*-1 - 1
print(0.5*(y_velocity**2 + y_velocity))

import re

with open("input.txt") as f:
    match = re.match("target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)", f.read())
    x_range = [int(match.group(1)), int(match.group(2))]
    y_range = [int(match.group(4)), int(match.group(3))]

def triangle(x):
    return 0.5*(x**2 + x)

def check_x_velocity(velocity, time, target):
    distance = triangle(velocity) - triangle(max(velocity - time, 0))
    return target[0] <= distance <= target[1]

def check_y_velocity(velocity, time, target):
    if velocity > 0:
        if time < 2*velocity:
            return False
        distance = (triangle(time-velocity-1) - triangle(velocity))*-1
    else:
        distance = (triangle((velocity-time+1)*-1) - triangle((velocity+1)*-1))*-1
    return target[0] >= distance >= target[1]

velocities = []

y_min = y_range[1]
y_max = y_range[1]*-1 - 1

x_max = x_range[1]
x_min = 0
for x in range(x_max):
    if check_x_velocity(x, x_range[1], x_range):
        x_min = x
        break

for y in range(y_min, y_max+1):
    y_target_times = []
    if y >= 0:
        for t in range(y*2+1, y*2-y_range[1]):
            if check_y_velocity(y, t, y_range):
                y_target_times.append(t)
    else:
        for t in range(y_range[1]*-1+1):
            if check_y_velocity(y, t, y_range):
                y_target_times.append(t)

    for x in range(x_min, x_max+1):
        for t in y_target_times:
            if check_x_velocity(x, t, x_range):
                velocities.append((x, y))
                break

print(len(velocities))

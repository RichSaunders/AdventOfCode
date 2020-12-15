# Optimised version
numbers = [8,11,0,19,1,2]
indices = {}
for i, n in enumerate(numbers[:-1]):
    indices[n] = i

n = len(numbers)
latest = numbers[-1]
while n < 30000000:
    if latest in indices:
        new = n - indices[latest] - 1
    else:
        new = 0
    indices[latest] = n - 1
    n += 1
    latest = new

print(latest)

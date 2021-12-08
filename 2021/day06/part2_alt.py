with open("input.txt") as f:
    input = f.read().split(",")
    input = [int(x) for x in input]

fish = [input.count(i) for i in range(9)]

for _ in range(256):
    new = fish.pop(0)
    fish[6] += new
    fish.append(new)

print(sum(fish))

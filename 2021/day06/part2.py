with open("input.txt") as f:
    input = f.read().split(",")
    input = [int(x) for x in input]

fish_dict = {i: input.count(i) for i in range(8)}

for _ in range(256):
    new = fish_dict.pop(0)
    fish_dict = {i: fish_dict.get(i+1, 0) for i in range(8)}
    fish_dict[6] += new
    fish_dict[8] = new

print(sum(fish_dict.values()))

with open("input.txt") as f:
    input = f.read().split(",")
    input = [int(x) for x in input]

fish_dict = {i: input.count(i) for i in range(8)}

for _ in range(256):
    if 0 in fish_dict:
        new = fish_dict.pop(0)
    else:
        new = 0

    fish_dict = {k-1: v for k, v in fish_dict.items()}
    fish_dict[6] = fish_dict.get(6, 0) + new
    fish_dict[8] = new

print(sum([v for _, v in fish_dict.items()]))

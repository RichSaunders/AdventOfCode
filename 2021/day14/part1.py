with open("input.txt") as f:
    input = f.read().splitlines()
    string = input[0]
    rules = {x.split(" -> ")[0]:x.split(" -> ")[1] for x in input[2:]}

for _ in range(10):
    new_string = ""

    for i in range(len(string)-1):
        new_string += string[i]
        new_string += rules[string[i:i+2]]

    new_string += string[-1]

    string = new_string

counts = [string.count(c) for c in set(string)]

print(max(counts) - min(counts))
import copy

with open("input.txt") as f:
    input = f.readlines()
    input = [list(x.strip()) for x in input]

sums = []
for i in range(len(input[0])):
    sums.append(0)
    for j in range(len(input)):
        sums[i] += int(input[j][i])

gamma = ["0" if x < len(input)/2 else "1" for x in sums]
epsilon = ["0" if x > len(input)/2 else "1" for x in sums]

oxygen = 0
valid_items = list(range(len(input)))
for i in range(len(input[0])):
    total = sum([int(input[j][i]) for j in valid_items])
    search_value = "0" if total < len(valid_items)/2 else "1"

    temp_list = copy.deepcopy(valid_items)
    for j in valid_items:
        item = input[j]
        if item[i] != search_value:
            temp_list.remove(j)
            if len(temp_list) == 1:
                oxygen = int("".join(input[temp_list[0]]), 2)
                break
    else:
        valid_items = copy.deepcopy(temp_list)
        continue
    break

co2 = 0
valid_items = list(range(len(input)))
for i in range(len(input[0])):
    total = sum([int(input[j][i]) for j in valid_items])
    search_value = "0" if total >= len(valid_items)/2 else "1"

    temp_list = copy.deepcopy(valid_items)
    for j in valid_items:
        item = input[j]
        if item[i] != search_value:
            temp_list.remove(j)
            if len(temp_list) == 1:
                co2 = int("".join(input[temp_list[0]]), 2)
                break
    else:
        valid_items = copy.deepcopy(temp_list)
        continue
    break

print(oxygen * co2)

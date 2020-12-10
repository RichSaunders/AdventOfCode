import re
# 2-7 p: pbhhzpmppb
regex = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

with open("input.txt", "r") as f:
    input = f.read()

l = input.splitlines()

valid = 0
for policy in l:
    match = regex.match(policy)
    min = int(match.group(1))
    max = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    if min <= password.count(letter) <= max:
        valid += 1

print(valid)
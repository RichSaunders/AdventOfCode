import re

memRE = re.compile("mem\[(\d+)\]")

with open("input.txt", "r") as f:
    input = f.read()
input = input.splitlines()

mem = {}
mask = ""
for line in input:
    instruction, value = line.split(" = ")

    if instruction == "mask":
        mask = value
    else:
        value = int(value)

        loc = int(memRE.match(instruction).group(1))
        locStr = list('{0:036b}'.format(int(loc)))
        for i in range(len(mask)):
            if mask[i] == "1":
                locStr[i] = "1"

            elif mask[i] == "X":
                locStr[i] = "X"

        xs = locStr.count("X")
        for i in range(2**xs):
            bin = ("{0:0%db}" % xs).format(i)
            maskedLoc = list(locStr)
            for j, n in enumerate([k for k, x in enumerate(locStr) if x == "X"]):
                maskedLoc[n] = bin[j]
            mem[int("".join(maskedLoc), 2) - 1] = value

print(sum(mem.values()))

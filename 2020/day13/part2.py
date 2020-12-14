with open("input.txt", "r") as f:
    input = f.read()
input = input.splitlines()
buses = input[1].split(",")
buses = [(int(x), buses.index(x)) for x in buses if x != "x"]

buses.sort(reverse=True, key=lambda x: x[0])
i = buses[0][0] - buses[0][1]
lcm = 1
for bus, position in buses:
    remainder = (bus - position) % bus
    while i % bus != remainder:
        i += lcm
    lcm *= bus

print(i)

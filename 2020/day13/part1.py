with open("input.txt", "r") as f:
    input = f.read()
input = input.splitlines()
now = int(input[0])
buses = input[1].split(",")
buses = [int(x) for x in buses if x != "x"]

minWait = now
soonestBus = 0
for bus in buses:
    wait = bus - (now % bus)
    if wait < minWait:
        minWait = wait
        soonestBus = bus

print(soonestBus*minWait)

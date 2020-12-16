import re
fieldRE = re.compile(r"([\w\s])+: (\d+)-(\d+) or (\d+)-(\d+)")

with open("input.txt", "r") as f:
    input = f.read()
fieldsStr, myTicket, nearbyTickets = input.split("\n\n")

fieldsList = fieldsStr.splitlines()
ranges = []
for field in fieldsList:
    match = fieldRE.match(field)
    ranges.append((int(match.group(2)), int(match.group(3))))
    ranges.append((int(match.group(4)), int(match.group(5))))

errors = []
for ticket in nearbyTickets.splitlines()[1:]:
    values = ticket.split(",")
    for value in values:
        value = int(value)
        for lower, upper in ranges:
            if lower <= value <= upper:
                break
        else:
            errors.append(value)

print(sum(errors))

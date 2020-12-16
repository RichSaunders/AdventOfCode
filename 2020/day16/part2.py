import re
fieldRE = re.compile(r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)")

with open("input.txt", "r") as f:
    input = f.read()
fieldsStr, myTicket, nearbyTickets = input.split("\n\n")

fieldsList = fieldsStr.splitlines()
fields = {}
for field in fieldsList:
    match = fieldRE.match(field)
    fields[match.group(1)] = (int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)))

possibilities = {field: list(range(len(fields))) for field in fields}

nearbyTickets = nearbyTickets.splitlines()[1:]
for ticket in nearbyTickets:
    valid = True
    values = ticket.split(",")
    for value in values:
        value = int(value)
        for ranges in fields.values():
            if ranges[0] <= value <= ranges[1] or ranges[2] <= value <= ranges[3]:
                break
        else:
            valid = False
            break

    if valid:
        for i, value in enumerate(values):
            value = int(value)
            for field, ranges in fields.items():
                if i not in possibilities[field]:
                    continue

                if not (ranges[0] <= value <= ranges[1] or ranges[2] <= value <= ranges[3]):
                    possibilities[field].remove(i)

while sum([len(options) for options in possibilities.values()]) > len(fields):
    for field, options in possibilities.items():
        if len(options) == 1:
            for field2, options2 in possibilities.items():
                if field2 != field and options[0] in options2:
                    possibilities[field2].remove(options[0])

myTicket = myTicket.splitlines()[1].split(",")

departureFields = [myTicket[options[0]] for field, options in possibilities.items() if field.startswith("departure")]
result = 1
for field in departureFields:
    result *= int(field)

print(result)

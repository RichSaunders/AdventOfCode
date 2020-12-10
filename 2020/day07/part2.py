import re
contentsRE = re.compile("(\d+) ([\w ]+ bag)s?")

def countBags(bag, rules):
    bags = 0
    for content in rules[bag]:
        n = rules[bag][content]
        bags += n
        bags += countBags(content, rules) * n
    return bags

with open("input.txt", "r") as f:
    input = f.read()

rules = {}
for rule in input.splitlines():
    bag, rawContents = rule[:-1].split("s contain ", 1)

    contents = {}
    if not rawContents == "no other bags":
        for content in rawContents.split(", "):
            match = contentsRE.match(content)
            contents[match.group(2)] = int(match.group(1))

    rules[bag] = contents

print(countBags("shiny gold bag", rules))

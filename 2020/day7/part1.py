import re
ruleRE = re.compile("([\w ]+) contain ([\w\d ,]+).")
contentsRE = re.compile("(\d+) ([\w ]+ bag)s?")

def searchForGold(bag, rules):
    for content in rules[bag]:
        if content == "shiny gold bag" or searchForGold(content, rules):
            return True

with open("input.txt", "r") as f:
    input = f.read()

rules = {}
for rule in input.splitlines():
    bag, rawContents = rule[:-1].split("s contain ", 1)

    contents = []
    if not rawContents == "no other bags":
        for content in rawContents.split(", "):
            match = contentsRE.match(content)
            contents.append(match.group(2))

    rules[bag] = contents

containsGold = 0
for bag in rules:
    if searchForGold(bag, rules):
        containsGold += 1

print(containsGold)

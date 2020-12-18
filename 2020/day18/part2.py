import re
additionRE = re.compile(r"(\d+ \+ \d+)")
multiplicationRE = re.compile(r"(\d+ \* \d+)")

def calculate(expression):
    while "(" in expression:
        open = expression.index("(")
        close = 0
        bracketCount = 0
        for i, c in enumerate(expression[open:]):
            if c == "(":
                bracketCount += 1
            elif c == ")":
                bracketCount -= 1
                if bracketCount == 0:
                    close = open + i
                    break

        subResult = calculate(expression[open+1:close])
        expression = expression[:open] + str(subResult) + expression[close+1:]

    while "+" in expression:
        match = additionRE.search(expression)
        expression = expression.replace(match.group(1), str(eval(match.group(1))), 1)

    while "*" in expression:
        match = multiplicationRE.search(expression)
        subExpression = match.group(1)
        subResult = eval(subExpression)
        expression = expression.replace(subExpression, str(subResult), 1)
        # expression = expression.replace(match.group(1), str(eval(match.group(1))), 1)

    return expression

with open("input.txt", "r") as f:
    input = f.read().splitlines()

results = [int(calculate(line)) for line in input]
print(sum(results))

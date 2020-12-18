import re
subExpressionRE = re.compile(r"(\d+ [-+*/] \d+)")

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

    while not expression.isdigit():
        match = subExpressionRE.match(expression)
        expression = expression.replace(match.group(1), str(eval(match.group(1))), 1)

    return expression

with open("input.txt", "r") as f:
    input = f.read().splitlines()

results = [int(calculate(line)) for line in input]
print(sum(results))

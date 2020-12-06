with open("input.txt", "r") as f:
    input = f.read()
groups = input.split("\n\n")

sum = 0
for group in groups:
    questions = set(group)
    if "\n" in questions:
        questions.remove("\n")
    sum += len(questions)

print(sum)
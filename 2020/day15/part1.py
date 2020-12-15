# Unoptimised version
numbers = [8,11,0,19,1,2]

while len(numbers) < 2020:
    if numbers[-1] in numbers[:-1]:
        for i in range(2, len(numbers)+1):
            if numbers[-i] == numbers[-1]:
                numbers.append(i - 1)
                break
    else:
        numbers.append(0)

print(numbers[-1])

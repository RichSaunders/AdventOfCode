with open("input.txt") as f:
    hex = f.read()
    binary = bin(int(hex, 16))[2:].zfill(len(hex*4))


def parse(binary, start):
    type = int(binary[start+3:start+6], 2)

    if type == 4:
        i = start+6
        s_number = ""
        while True:
            s_number += binary[i+1:i+5]
            if binary[i] == "1":
                i += 5
            elif binary[i] == "0":
                break

        number = int(s_number, 2)
        return number, i+5

    else:
        length_id = binary[start+6]
        if length_id == "0":
            length = int(binary[start+7:start+22], 2)
            pointer = start + 22
            numbers = []
            while pointer < start+22+length:
                t_number, pointer = parse(binary, pointer)
                numbers.append(t_number)
        else:
            length = int(binary[start+7:start+18], 2)
            numbers = []
            pointer = start + 18
            for _ in range(length):
                t_number, pointer = parse(binary, pointer)
                numbers.append(t_number)

        if type == 0:
            result = sum(numbers)
        elif type == 1:
            result = 1
            for number in numbers:
                result *= number
        elif type == 2:
            result = min(numbers)
        elif type == 3:
            result = max(numbers)
        elif type == 5:
            result = 1 if numbers[0] > numbers[1] else 0
        elif type == 6:
            result = 1 if numbers[0] < numbers[1] else 0
        elif type == 7:
            result = 1 if numbers[0] == numbers[1] else 0
        else:
            assert False

        return result, pointer

result, pointer = parse(binary, 0)
print(result)

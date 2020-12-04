required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]


def parse_input(input):
    passports_raw = input.split("\n\n")
    passports = []
    for passport in passports_raw:
        passport = passport.replace(" ", "\n")
        fields = passport.splitlines()
        passport_dict = {field.split(":")[0]: field.split(":")[1] for field in fields}
        passports.append(passport_dict)

    return passports


with open("input.txt", "r") as f:
    input = f.read()
passports = parse_input(input)

valid_passports = 0
for passport in passports:
    for field in required_fields:
        if not field in passport:
            break
    else:
        valid_passports += 1

print(valid_passports)

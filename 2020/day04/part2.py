import re
hair_re = re.compile(r"#[0-9a-f]{6}")

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

        for field in required_fields:
            passport_dict.setdefault(field, "")

        passports.append(passport_dict)

    return passports


with open("input.txt", "r") as f:
    input = f.read()
passports = parse_input(input)

valid_passports = 0
for passport in passports:
    valid = True
    if not passport["byr"].isdigit() or not 1920 <= int(passport["byr"]) <= 2002:
        valid = False

    if not passport["iyr"].isdigit() or not 2010 <= int(passport["iyr"]) <= 2020:
        valid = False

    if not passport["eyr"].isdigit() or not 2020 <= int(passport["eyr"]) <= 2030:
        valid = False

    if passport["hgt"][-2:] == "cm":
        if not passport["hgt"][:-2].isdigit() or not 150 <= int(passport["hgt"][:-2]) <= 193:
            valid = False
    elif passport["hgt"][-2:] == "in":
        if not passport["hgt"][:-2].isdigit() or not 59 <= int(passport["hgt"][:-2]) <= 76:
            valid = False
    else:
        valid = False

    if not hair_re.match(passport["hcl"]):
        valid = False

    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        valid = False

    if not passport["pid"].isdigit() or len(passport["pid"]) != 9:
        valid = False

    if valid:
        valid_passports += 1

print(valid_passports)

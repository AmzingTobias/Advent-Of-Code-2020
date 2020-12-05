import re


def valid_part_two(valid_list):
    invalid = False
    for code in temp_valid_2_list:
        if code[0] == "byr":
            if not (int(code[1]) <= 2002 and int(code[1]) >= 1920):
                invalid = True
        if code[0] == "iyr":
            if not (int(code[1]) <= 2020 and int(code[1]) >= 2010):
                invalid = True
        if code[0] == "eyr":
            if not (int(code[1]) <= 2030 and int(code[1]) >= 2020):
                invalid = True
        if code[0] == "hgt" and len(code[1]) > 2:
            hgt_number, hgt_type = int(code[1][:-2]), code[1][-2:]
            if hgt_type == "cm":
                if not (hgt_number <= 193 and hgt_number >= 150):
                    invalid = True
            elif hgt_type == "in":
                if not (hgt_number <= 76 and hgt_number >= 59):
                    invalid = True
            else:
                invalid = True
        if code[0] == "hcl":
            if re.search("#([0-9]|[a-f])*", code[1]) == None:
                invalid = True
            else:
                if len(code[1]) != 7:
                    invalid = True
        if code[0] == "ecl":
            if code[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                invalid = True
        if code[0] == "pid":
            if not (len(code[1]) == 9 and code[1].isdigit()):
                invalid = True
    return invalid


with open("input.txt", "r") as file:
    user_input = file.read().split("\n\n")
user_input = [x.split("\n") for x in user_input]
VALID = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
part_one_count = 0
part_two_count = 0
for y in user_input:
    invalid = False
    temp_list = [x.split(" ") for x in y]
    temp_list = [x for y in temp_list for x in y]
    if "" in temp_list:
        temp_list.remove("")
    temp_valid_list = [x.split(":")[0] for x in temp_list]
    temp_valid_2_list = [x.split(":") for x in temp_list]
    for valid_code in VALID:
        if valid_code not in temp_valid_list:
            invalid = True
    if invalid == False:
        part_one_count += 1
        valid_part_two_valid = valid_part_two(temp_valid_2_list)
        if valid_part_two_valid == False:
            part_two_count += 1
print(part_one_count)
print(part_two_count)

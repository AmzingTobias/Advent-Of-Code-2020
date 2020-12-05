import re
with open("input.txt", "r") as file:
    user_input = file.readlines()
user_input = [x.strip() for x in user_input]


def check_valid_occurence(user_input):
    valid = 0
    for element in user_input:
        n_range, char = re.split("([0-9]*-[0-9]*.)", element.split(":")[0])[1:]
        n_range_lower, n_range_higher = n_range.split("-")
        char_occurence = element.split(": ")[1].count(char)
        if char_occurence >= int(n_range_lower) and char_occurence <= int(n_range_higher):
            valid += 1
    return valid


def check_valid_index(user_input):
    valid = 0
    for element in user_input:
        n_range, char = re.split("([0-9]*-[0-9]*.)", element.split(":")[0])[1:]
        n_range_lower, n_range_higher = n_range.split("-")
        if (element.split(": ")[1][int(n_range_lower) - 1] == char) ^ (element.split(": ")[1][int(n_range_higher) - 1] == char):
            valid += 1
    return valid

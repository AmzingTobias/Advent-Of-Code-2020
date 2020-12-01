with open("input.txt", "r") as expense_file:
    expense_report = expense_file.readlines()

expense_report = [int(x.strip("\n")) for x in expense_report]


def part_one(contents, goal):
    for x in range(len(contents)):
        if x <= goal:
            for y in range(len(contents)):
                if x != y:
                    if contents[x] + contents[y] == goal:
                        return contents[x] * contents[y]


def part_two(contents, goal):
    for x in range(len(contents)):
        if x <= goal:
            for y in range(len(contents)):
                if x + y <= goal and x != y:
                    for z in range(len(contents)):
                        if x != z:
                            if contents[x] + contents[y] + contents[z] == goal:
                                return contents[x] * contents[y] * contents[z]

with open("input.txt", "r") as file:
    user_input = file.readlines()
user_input = [x.strip() * len(user_input) for x in user_input]


def check_trees(user_input):
    posX, posY = 0, 0
    tree_count = 0
    while (posX <= (len(user_input) - 1)):
        tree_count = check_tree_at_pos(posX, posY, tree_count)
        posX, posY = posX + 1, posY + 3
    return tree_count


def check_tree_at_pos(posX, posY, summation):
    if user_input[posX][posY] == "#":
        return summation + 1
    return summation


def check_multiple_trees(user_input):
    posX_1, posY_1, posX_2, posY_2, posX_3, posY_3, posX_4, posY_4, posX_5, posY_5 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    tree_count_1, tree_count_2, tree_count_3, tree_count_4, tree_count_5 = 0, 0, 0, 0, 0
    i_length = len(user_input) - 1
    while True:
        if posX_1 <= i_length:
            tree_count_1 = check_tree_at_pos(posX_1, posY_1, tree_count_1)
            posX_1, posY_1 = posX_1 + 1, posY_1 + 1
        if posX_2 <= i_length:
            tree_count_2 = check_tree_at_pos(posX_2, posY_2, tree_count_2)
            posX_2, posY_2 = posX_2 + 1, posY_2 + 3
        if posX_3 <= i_length:
            tree_count_3 = check_tree_at_pos(posX_3, posY_3, tree_count_3)
            posX_3, posY_3 = posX_3 + 1, posY_3 + 5
        if posX_4 <= i_length:
            tree_count_4 = check_tree_at_pos(posX_4, posY_4, tree_count_4)
            posX_4, posY_4 = posX_4 + 1, posY_4 + 7
        if posX_5 <= i_length:
            tree_count_5 = check_tree_at_pos(posX_5, posY_5, tree_count_5)
            posX_5, posY_5 = posX_5 + 2, posY_5 + 1
        if posX_1 > i_length and posX_2 > i_length and posX_3 > i_length and posX_4 > i_length and posX_5 > i_length:
            break
    return tree_count_1 * tree_count_2 * tree_count_3 * tree_count_4 * tree_count_5


print(check_multiple_trees(user_input))

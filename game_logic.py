import random


def randoCode(number_of_color, color_list):
    """
    Generates a random color code.
    """
    color_code = []
    for _ in range(number_of_color):
        color_code.append(random.choice(color_list))
    return color_code


def check_correct(user_input, color_code):
    """
    Checks if the user input is right.
    :param user_input:
    :param color_code:
    :return: A list containing the correct position, and the partial placement.
    """
    length = len(color_code)
    correct_guess = 0
    partial_placement = 0
    new_user_input = [0] * length
    for i in range(length):
        if user_input[i] == color_code[i]:
            new_user_input[i] = "N"
            correct_guess += 1
        for k in range(length):
            if new_user_input[k] != "N":
                new_user_input[k] = user_input[i]
        for j in range(length):
            if new_user_input[i] == color_code[j]:
                partial_placement += 1

    return [correct_guess, partial_placement]


def check_input(user_input, code_length):
    """
    Checks if the user input is of the right length.
    """
    while len(user_input) != code_length:
        print("This is not the right code length. Try again.")
        user_input = input("Please enter a code : ")
    return user_input


def results_check(user_input, color_code):
    """
    :return: List containing the correct colors, partial colors, and if the user has won.
    """
    has_won = False
    result = check_correct(user_input, color_code)
    if result[0] == len(color_code):
        has_won = True
    return [result[0], result[1], has_won]

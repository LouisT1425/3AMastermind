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
    :return: A list containing the correct position, and the partial placement.
    """
    length = len(color_code)
    correct_guess = 0
    partial_placement = 0
    guess_left = list(user_input[:])  # Create a copy of user_input as a list.
    color_code_left = list(color_code[:])
    for i in range(length):
        if user_input[i] == color_code[i]:  # If the user input N°i is exactly correct...
            guess_left.remove(user_input[i])  # ... removes the current color from the guess_left variable ...
            color_code_left.remove(color_code[i])  # ... and from the correct code. It removes the current color as to
            correct_guess += 1                     # not check it again during the partial color phase.

    for j in guess_left:  # Checks if any of the colors left ...
        if j in color_code_left:  # ... are in the remaining color code.
            partial_placement += 1
            color_code_left.remove(j)  # Removes the color from the remaining color code.

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

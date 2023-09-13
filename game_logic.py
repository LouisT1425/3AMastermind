import random


def randoCode(number_of_color, color_array):
    color_code = []
    for _ in range(number_of_color):
        color_code.append(random.choice(color_array))
    return color_code


def check_correct(choice, color_code):
    length = len(color_code)
    correct_guess = 0
    partial_placement = 0
    new_choice = [0] * length
    for i in range(length):
        if choice[i] == color_code[i]:
            new_choice[i] = "N"
            correct_guess += 1
        for k in range(length):
            if new_choice[k] != "N":
                new_choice[k] = choice[i]
        for j in range(length):
            if new_choice[i] == color_code[j] and new_choice[i] != "N":
                partial_placement += 1

    return [correct_guess, partial_placement]


def check_input(user_input, code_length):
    while len(user_input) != code_length:
        print("This is not the right code length. Try again.")
        user_input = input("Please enter a code : ")
    return user_input


def results_check(user_input, color_code):
    has_won = False
    result = check_correct(user_input, color_code)
    if result[0] == len(color_code):
        has_won = True
    return [result[0], result[1], has_won]

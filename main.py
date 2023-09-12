import random


def randoCode(number_of_color, color_array):
    color_code = []
    for i in range(number_of_color):
        color_code.append(random.choice(color_array))
    return color_code


def guess(choice, color_code):
    good_guess = 0
    wrong_placement = 0
    for i in range(len(color_code)):
        if choice[i] == color_code[i]:
            good_guess += 1
        for j in range(len(color_code)):
            if choice[i] == color_code[j]:
                wrong_placement += 1
    return [good_guess, wrong_placement - good_guess]


def game(possible_colors, code_length, number_of_tries):
    tries = 0
    has_won = False
    print("You have ", number_of_tries, " to guess the color code.")
    print("The possible colors are : ", possible_colors)
    print("The code length is : ", code_length)
    color_code = randoCode(code_length, possible_colors)
    print(color_code)
    while tries < number_of_tries:
        tries += 1
        user_input = input("Please enter a code : ")
        result = guess(user_input, color_code)
        if result[0] == code_length:
            has_won = True
            break
        else:
            print("You have ", result[0], " good guesses and ", result[1], " wrong placement but right color.")
    if has_won:
        print("Congratulations ! You won !")
    else:
        print("You lost, the right code was ", color_code)


code_length = 4
possible_colors = ['R', 'G', 'B', 'Y', 'P', 'W']
number_of_tries = 12
game(possible_colors, code_length, number_of_tries)


import random


def randoCode(number_of_color, color_array):
    color_code = []
    for i in range(number_of_color):
        color_code.append(random.choice(color_array))
    return color_code


def guess(choice, color_code):
    correct_guess = 0
    partial_placement = 0
    for i in range(len(color_code)):
        if choice[i] == color_code[i]:
            correct_guess += 1
        for j in range(len(color_code)):
            if choice[i] == color_code[j]:
                partial_placement += 1
    return [correct_guess, partial_placement - correct_guess]


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
        while len(user_input) != code_length:
            print("This is not the right code length. Try again.")
            user_input = input("Please enter a code : ")
        result = guess(user_input, color_code)
        if result[0] == code_length:
            has_won = True
            break
        else:
            print("You have ", result[0], " correct guesses and ", result[1], " partial guesses.")
    score = number_of_tries - tries
    if has_won:
        print("Congratulations ! You won !")
        print("Your score is ", score)
    else:
        print("You lost, the right code was ", color_code)

code_length = 4
possible_colors = ['R', 'G', 'B', 'Y', 'P', 'W']
number_of_tries = 12
game(possible_colors, code_length, number_of_tries)
is_game_on = True
number_of_game = 1
while is_game_on:
    print("\n")
    print("Do you want to replay ?")
    choice = input("Y/N")
    if choice != "Y" or choice != "N":
        print("This is not a right input.")
    if choice == "Y":
        number_of_game += 1
        game(possible_colors, code_length, number_of_tries)
    if choice == "N":
        print("Goodbye !")
        break


import random
from os.path import exists
import os


def save_stats(number_of_games, score):
    if exists(".number_of_games.txt"):
        os.system("attrib -h .number_of_games.txt")
        os.chmod(".number_of_games.txt", 0o755)
        file = open(".number_of_games.txt", "r")
        old_number_of_games = file.read()
        number_of_games = int(number_of_games)
        number_of_games += int(old_number_of_games)
        file = open(".number_of_games.txt", "w")
        file.write(str(number_of_games))
        file.close()
        os.system("attrib +h .number_of_games.txt")
    else:
        file = open(".number_of_games.txt", "w")
        file.write(str(number_of_games))
        file.close()
        os.system("attrib +h .number_of_games.txt")

    if exists(".score.txt"):
        os.system("attrib -h .score.txt")
        file = open(".score.txt", "r")
        old_score = file.read()
        score = int(score)
        score += int(old_score)
        file = open(".score.txt", "w")
        file.write(str(score))
        file.close()
        os.system("attrib +h .score.txt")
    else:
        file = open(".score.txt", "w")
        file.write(str(score))
        file.close()
        os.system("attrib +h .score.txt")


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
            print(new_choice)
        for k in range(length):
            if new_choice[k] != "N":
                new_choice[k] = choice[i]
        for j in range(length):
            if new_choice[i] == color_code[j]:
                partial_placement += 1

    return [correct_guess, partial_placement]


def check_input(user_input, code_length):
    while len(user_input) != code_length:
        print("This is not the right code length. Try again.")
        user_input = input("Please enter a code : ")
    return user_input


def print_stats():
    stats = [0, 0]
    if exists(".number_of_games.txt"):
        file = open(".number_of_games.txt", "r")
        number_of_games = file.read()
        file.close()
        stats[0] = number_of_games
    else:
        stats[0] = "NULL"
        stats[1] = "NULL"

    if exists(".score.txt"):
        file = open(".score.txt", "r")
        score = file.read()
        file.close()
        stats[1] = score

    if stats[0] == "NULL" and stats[1] == "NULL":
        print("No stats currently available.")
    else:
        print("You played ", stats[0], " games, and your overall score is ", stats[1], ".")


def game(possible_colors, code_length, number_of_tries):
    tries = 0
    has_won = False
    print_stats()
    print("You have ", number_of_tries, " tries to guess the color code.")
    print("The possible colors are : ", possible_colors)
    print("The code length is : ", code_length)
    color_code = randoCode(code_length, possible_colors)
    print(color_code)
    while tries < number_of_tries:
        tries += 1
        user_input = input("Please enter a code : ")
        user_input = check_input(user_input, code_length)
        result = check_correct(user_input, color_code)
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
    return score


code_length = 4
possible_colors = ['R', 'G', 'B', 'Y', 'P', 'W']
number_of_tries = 12
game_score = game(possible_colors, code_length, number_of_tries)
is_game_on = True
number_of_game = 1
save_stats(number_of_game, game_score)

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


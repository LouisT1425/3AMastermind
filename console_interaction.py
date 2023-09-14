import stats
import game_logic


def game(possible_colors, code_length, number_of_tries):
    tries = 0
    has_won = False
    print("You have ", number_of_tries, " tries to guess the color code.")
    print("The possible colors are : ", possible_colors)
    print("The code length is : ", code_length)
    color_code = game_logic.randoCode(code_length, possible_colors)
    while tries < number_of_tries:
        tries += 1
        user_input = input("Please enter a code : ")
        user_input = game_logic.check_input(user_input, code_length)
        result = game_logic.results_check(user_input, color_code)
        if result[2]:  # result[2] contains the boolean has_won variable.
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


def main_menu(possible_colors, code_length, number_of_tries):
    number_of_game = 0
    is_game_on = True
    while is_game_on:
        print("\n")
        stats.print_stats()
        print("Do you want to play(P), reset your stats(R), or quit(Q) the game ?")
        choice = input("P/R/Q")
        if choice != "P" and choice != "R" and choice != "Q":
            print("This is not a right input.")
        if choice == "P":
            number_of_game += 1
            game_score = game(possible_colors, code_length, number_of_tries)
            stats.save_stats(number_of_game, game_score)
        if choice == "Q":
            print("Goodbye !")
            break
        if choice == "R":
            stats.reset_stats()
            print("Stats reset !")
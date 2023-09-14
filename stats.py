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


def reset_stats():
    if exists(".number_of_games.txt"):
        os.system("attrib -h .number_of_games.txt")
        file = open(".number_of_games.txt", "w")
        file.write(str(0))
        file.close()
        os.system("attrib +h .number_of_games.txt")
    else:
        print("No number of games data available !")

    if exists(".score.txt"):
        os.system("attrib -h .score.txt")
        file = open(".score.txt", "w")
        file.write(str(0))
        file.close()
        os.system("attrib +h .score .txt")
        print("Data reset !")
    else:
        print("No score data available !")


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


def get_stats():
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
        return ["NULL", "NULL"]
    else:
        return [stats[0], stats[1]]
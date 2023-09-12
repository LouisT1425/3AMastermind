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


possible_colors = ['R', 'G', 'B', 'Y', 'P', 'W']
code = randoCode(4, possible_colors)
print("The code is : ", code)
user = ['R', 'W', 'G', 'B']
print("Your code is : ", user)
results = guess(user, code)
print("You have ", results[0], " good guesses and ", results[1], " wrong placement but right color.")

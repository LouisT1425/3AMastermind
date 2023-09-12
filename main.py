import random


def randoCode(number_of_color, color_array):
    color_code = []
    for i in range(number_of_color):
        color_code.append(random.choice(color_array))
    return color_code


possible_colors = ['R', 'G', 'B', 'Y', 'P', 'W']
code = randoCode(4, possible_colors)
print("The code is : ", code)

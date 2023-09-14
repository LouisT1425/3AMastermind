from tkinter import *
import stats

root = Tk()
root.geometry("350x200")


def resetStats():
    stats.reset_stats()


def play():
    window = Toplevel(root)
    window.title("Mastermind")
    window.geometry("500x500")

    image = PhotoImage(file="images/plateaujpg.jpg")
    original_image = Label(window, image=image)
    original_image.image = image
    original_image.pack()


def main_menu():
    score = stats.get_stats()

    play_button = Button(root, text="PLAY", command=play)
    play_button.pack(side=TOP)

    reset_button = Button(root, text="RESET STATS", command=resetStats)
    reset_button.pack(side=TOP)

    quit_button = Button(root, text="QUIT", command=root.quit)
    quit_button.pack(side=TOP)

    strinfo = "You have played " + str(score[0]) + " games and your total score is " + str(score[1]) + " points."

    infotext = Label(root, text=strinfo)
    infotext.pack(side=TOP)

    root.mainloop()


main_menu()

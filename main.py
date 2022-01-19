from tkinter import *
import pandas
import random
import math

BACKGROUND = "#B1DDC6"
FONT = ("Arial", 50, "bold")
RED = "#E60965"
STUDY_SEC = 900
counter = STUDY_SEC
is_save = False
current_word = {}
unknown_words_list = {}

try:
    unknown_words = pandas.read_csv("data/unknown_words_list.csv")
    unknown_words_list = unknown_words.to_dict(orient="records")
except FileNotFoundError:
    ielts_words = pandas.read_csv("data/ielts_words_list.csv")
    unknown_words_list = ielts_words.to_dict(orient="records")


def choose_word():
    global current_word
    current_word = random.choice(unknown_words_list)
    canvas.itemconfig(ielts_word, text=current_word['word'], fill="black")
    canvas.itemconfig(word_meaning, text='', fill="black")


def show_meaning():
    global current_word
    canvas.itemconfig(word_meaning, text=current_word['meaning'], fill="black")


def unknown():
    global current_word
    show_meaning()
    window.after(2000, func=choose_word)


def known():
    global current_word
    show_meaning()
    unknown_words_list.remove(current_word)
    window.after(2000, func=choose_word)


def start_timer():
    global counter
    if not is_save:
        if counter == STUDY_SEC:
            choose_word()
        minute = math.floor(counter / 60)
        second = counter % 60
        if second < 10:
            second = f"0{second}"
        title_label.config(text=f"{minute}:{second}")

        if counter > 0:
            counter -= 1
            window.after(1000, start_timer)


def reset_timer():
    global counter
    counter = STUDY_SEC


def save():
    global is_save, counter
    is_save = True
    data = pandas.DataFrame(unknown_words_list)
    data.to_csv("data/unknown_words_list.csv", index=False)
    window.after(2000)
    exit()


window = Tk()
window.title("IELTS Frequency Words Study Engine")
window.config(padx=20, pady=20, bg=BACKGROUND)

title_label = Label(text="15:00", fg=RED, bg=BACKGROUND, font=FONT)
title_label.grid(row=0, column=0, columnspan=2)

canvas = Canvas(width=400, height=400)
word_card_image = PhotoImage(file="images/word_card.png")
word_card_background = canvas.create_image(200, 200, image=word_card_image)
ielts_word = canvas.create_text(200, 80, text="", font=FONT)
word_meaning = canvas.create_text(200, 200, text="", font=("Arial", 30, "italic"), width=300)

canvas.config(bg=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=2, rowspan=2, columnspan=2, padx=10, pady=10)

start_image = PhotoImage(file="images/start.png")
start_button = Button(image=start_image, highlightthickness=0, command=start_timer)
start_button.grid(row=1, column=1, padx=10, pady=10)

reset_image = PhotoImage(file="images/reset.png")
reset_button = Button(image=reset_image, highlightthickness=0, command=reset_timer)
reset_button.grid(row=1, column=0, padx=10, pady=10)

save_image = PhotoImage(file="images/save.png")
save_button = Button(image=save_image, highlightthickness=0, command=save)
save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

yes_image = PhotoImage(file="images/yes.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=known)
yes_button.grid(row=2, column=3, padx=10, pady=10)

no_image = PhotoImage(file="images/no.png")
no_button = Button(image=no_image, highlightthickness=0, command=unknown)
no_button.grid(row=2, column=2, padx=10, pady=10)


window.mainloop()




from tkinter import *
import pandas
import random

BACKGROUND = "#B1DDC6"
FONT = ("Arial", 50, "bold")
current_word = {}
unknown_words_list = {}

try:
    unknown_words = pandas.read_csv("data/unknown_words_list.csv")
except FileNotFoundError:
    ielts_words = pandas.read_csv("data/ielts_words_list.csv")
    unknown_words_list = ielts_words.to_dict(orient="records")
else:
    unknown_words_list = unknown_words.to_dict(orient="records")


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


window = Tk()
window.title("IELTS Frequency Words Study Engine")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(width=800, height=526)
word_card_image = PhotoImage(file="images/word_card.png")
word_card_background = canvas.create_image(400, 400, image=word_card_image)
ielts_word = canvas.create_text(400, 200, text="", font=FONT)
word_meaning = canvas.create_text(400, 300, text="", font=FONT)
canvas.config(bg=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

no_image = PhotoImage(file="images/no.png")
no_button = Button(image=no_image, highlightthickness=0, command=unknown)
no_button.grid(row=1, column=0)

yes_image = PhotoImage(file="images/yes.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=known)
yes_button.grid(row=1, column=1)

choose_word()

window.mainloop()




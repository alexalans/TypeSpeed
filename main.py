from tkinter import *
from tkinter import messagebox
import json

def restart_test():
    pass

def change_to_cyrillic():
    pass

def submit_word(event):
    print("word submitted!")

window = Tk()
window.title("TypeSpeed")
window.config(padx=25, pady=25)
canvas = Canvas()

logo = PhotoImage(file="typespeed_logo.png")
canvas.config(width=200, height=70)
canvas.create_image(100, 35, image=logo)
canvas.grid(column=1, row=1, columnspan=3)


type_this = Label(text="Type this:", justify="left", anchor="w", font=("Arial", 13))
type_this.grid(column=1, row=2, sticky=W+E, pady=5)

sentence = Label(text="Here will dynamically be displayed the sentence to be typed", justify="left", anchor="w")
sentence.grid(column=1, row=3, columnspan=3, sticky=W+E)

next_sentence = Label(text="In grey the next sentence that will become main sentence", justify="left", anchor="w")
next_sentence.grid(column=1, row=4, columnspan=3, sticky=W+E, pady=5)

type_here = Label(text="Type here:", justify="left", anchor="w", font=("Arial", 13))
type_here.grid(column=1, row=5, sticky=W+E)

word_entry = Entry(width=25, font=("Arial", 13))
word_entry.bind("<space>", submit_word)
word_entry.grid(column=1, row=6, columnspan=3, pady=5, sticky=W+E)

restart = Button(text="Restart", command=restart_test)
restart.grid(column=1, row=7, padx=3)

cyrillic = Button(text="Кирилица (Български)", width=30, command=change_to_cyrillic, pady=5)
cyrillic.grid(column=2, row=7, columnspan=2, pady=3)

window.mainloop()

from tkinter import *
from tkinter import messagebox
import json
import random

language = "English"
words_sent = 0


class Word:
    def __init__(self, a_word):
        self.text = a_word
        self.color = "black"

def restart_test():
    pass


def change_to_cyrillic():
    pass


def submit_word(event):
    global words_sent
    typed_word = word_entry.get().strip()
    print(typed_word)
    if typed_word == word_objects_list[words_sent].text:
        print("correct!")
        word_objects_list[words_sent].color = "green"
    else:
        print("wrong!")
        word_objects_list[words_sent].color = "red"
    words_sent += 1
    word_entry.delete(0, 'end')
    update_text()

def start_test(event):
    update_text()
    word_entry.delete(0, 'end')
    # TODO STARTING THE TIMER ETC


def update_text():
    text_to_type.config(state="normal")
    text_to_type.delete(1.0, 'end')
    for word_object in word_objects_list:
        text_to_type.insert("end", word_object.text + " ", word_object.color)
    text_to_type.config(state="disabled")


window = Tk()
window.title("TypeSpeed")
window.config(padx=25, pady=25)
canvas = Canvas()

logo = PhotoImage(file="typespeed_logo.png")
canvas.config(width=200, height=70)
canvas.create_image(100, 35, image=logo)
canvas.grid(column=1, row=1, columnspan=3)

type_this = Label(text="Type this:", justify="left", anchor="w", font=("Arial", 13))
type_this.grid(column=1, row=2, sticky=W + E, pady=5)

# ----- Text loading --- #

with open("text.json", mode="r", encoding='utf-8') as texts:
    content = json.load(texts)

random_nr = random.randint(1, 3)

word_objects_list = [Word(word) for word in content[language][f"{random_nr}"].split()]

text_to_type = Text(height=10, wrap="word")
text_to_type.config(state=NORMAL)
text_to_type.grid(column=1, row=3, columnspan=3, sticky=W + E)

text_to_type.tag_configure(tagName="green", foreground="green")
text_to_type.tag_configure(tagName="red", foreground="red")
text_to_type.tag_configure(tagName="black", foreground="black")

type_here = Label(text="Type here:", justify="left", anchor="w", font=("Arial", 13))
type_here.grid(column=1, row=5, sticky=W + E)

word_entry = Entry(width=25, font=("Arial", 13))
word_entry.bind("<space>", submit_word)
word_entry.bind("<Button-1>", start_test)
word_entry.insert(0, "Click here to start!")
word_entry.grid(column=1, row=6, columnspan=3, pady=5, sticky=W + E)

restart = Button(text="Restart", command=restart_test)
restart.grid(column=1, row=7, padx=3)

cyrillic = Button(text="Кирилица (Български)", width=30, command=change_to_cyrillic, pady=5)
cyrillic.grid(column=2, row=7, columnspan=2, pady=3)

window.mainloop()

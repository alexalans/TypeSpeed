from tkinter import *
from tkinter import messagebox
import json
import random

language = "English"
words_sent = 0
word_objects_list = None
countdown = None


class Word:
    def __init__(self, a_word):
        self.text = a_word
        self.color = "black"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def show_result():
    words_correct = 0
    words_wrong = 0
    word_entry.config(state="disabled")
    for word in word_objects_list:
        if word.color == "green":
            words_correct += 1
        if word.color == "red":
            words_wrong += 1
    try:
        accuracy = round((words_correct / (words_correct + words_wrong) * 100), 1)
    except ZeroDivisionError:
        messagebox.showinfo(title="Your Speed Test Results",
                            message=f"Hey, you didn't even try doing the test!"
                                    f"Come on, I know you can do better than that.")

    else:
        messagebox.showinfo(title="Your Speed Test Results",
                            message=f"Words per minute: {words_correct}\n"
                                    f"Typing accuracy: {accuracy}%\n")



def timer(seconds):
    time.config(text=f"Time left: {seconds}")
    global countdown
    countdown = window.after(1000, timer, seconds - 1)
    if seconds <= 0:
        window.after_cancel(countdown)
        type_this.config(text="Your result:")
        show_result()


def restart_test():
    if countdown is not None:
        word_entry.delete(0, 'end')
        type_this.config(text="Type this:")
        window.after_cancel(countdown)
        window.focus_set()
        global words_sent
        words_sent = 0
        word_entry.config(state="normal")
        word_entry.insert(0, "Press 'S' to start!")
        word_entry.config(state="disabled")
        window.bind("s", start_test)
        window.bind("S", start_test)
        time.config(text=f"Time left:")
        current_text = len(text_to_type.get(1.0, "end"))
        if current_text > 100:
            text_to_type.config(state="normal")
            text_to_type.delete(1.0, 'end')
            text_to_type.insert("end", f"A new text will appear as soon as you start the test.")
            text_to_type.config(state="disabled")


def switch_language():
    global language
    if language == "English":
        language = "Bulgarian"
        change_language.config(text="English")
    else:
        language = "English"
        change_language.config(text="Български")

    text_to_type.config(state="normal")
    text_to_type.delete(1.0, 'end')
    text_to_type.insert("end", f"Test text language is now set to {language}.")
    text_to_type.config(state="disabled")

    if countdown is not None:
        restart_test()


def submit_word(event):
    global words_sent
    typed_word = word_entry.get().strip()
    if typed_word == word_objects_list[words_sent].text:
        word_objects_list[words_sent].color = "green"
    else:
        word_objects_list[words_sent].color = "red"
    words_sent += 1
    word_entry.delete(0, 'end')
    update_text()


def start_test(event):
    word_entry.config(state="normal")
    window.unbind("s")
    window.unbind("S")
    word_entry.focus_set()
    global word_objects_list
    word_objects_list = load_text()
    update_text()
    word_entry.delete(0, 'end')
    type_this.config(text="Type this:")
    timer(60)


def update_text():
    text_to_type.config(state="normal")
    text_to_type.delete(1.0, 'end')
    for word_object in word_objects_list:
        text_to_type.insert("end", word_object.text + " ", word_object.color)
    text_to_type.config(state="disabled")


window = Tk()
window.title("TypeSpeed")
window.config(padx=25, pady=25)
window.bind("s", start_test)
window.bind("S", start_test)
canvas = Canvas()

logo = PhotoImage(file="typespeed_logo.png")
canvas.config(width=200, height=70)
canvas.create_image(100, 35, image=logo)
canvas.grid(column=1, row=1, columnspan=3)

type_this = Label(text="", justify="left", anchor="w", font=("Arial", 13))
type_this.grid(column=1, row=2, sticky=W + E, pady=5)


def load_text():
    with open("text.json", mode="r", encoding='utf-8') as texts:
        content = json.load(texts)
    random_nr = random.randint(1, 6)
    word_objects_list = [Word(word) for word in content[language][f"{random_nr}"].split()]
    return word_objects_list


text_to_type = Text(height=10, width=60, wrap="word", font=("Arial", 13), padx=10, pady=10)
text_to_type.config(state=NORMAL)
text_to_type.insert("end", "Welcome to TypeSpeed! \n\n"
                           "This program will measure your typing speed in words per minute. \n"
                           "You have 60 seconds to type as much of the test text as you can. \n"
                           "Every time you hit spacebar, your word will be submitted and evaluated. \n"
                           "The test text will appear here as soon as you click into the typing box. \n\n"
                           "Good luck! ")
text_to_type.grid(column=1, row=3, columnspan=3, sticky=W + E)
text_to_type.config(state="disabled")

text_to_type.tag_configure(tagName="green", foreground="green")
text_to_type.tag_configure(tagName="red", foreground="red")
text_to_type.tag_configure(tagName="black", foreground="black")

type_here = Label(text="Type here:", justify="left", anchor="w", font=("Arial", 13))
type_here.grid(column=1, row=5, sticky=W + E)

word_entry = Entry(width=25, font=("Arial", 13))
word_entry.bind("<space>", submit_word)
word_entry.insert(0, "Press 'S' to start!")
word_entry.config(state="disabled")
word_entry.grid(column=1, row=6, columnspan=3, pady=5, sticky=W + E)

restart = Button(text="Restart", command=restart_test)
restart.grid(column=1, row=7, padx=10, pady=5, sticky=N+S+E+W)

change_language = Button(text="Български", width=20, command=switch_language, pady=5)
change_language.grid(column=2, row=7, columnspan=1, padx=10, pady=5, sticky=N+S+E+W)

time = Label(text="Time left:", justify="left", anchor="w", font=("Arial", 13))
time.grid(column=3, row=7, columnspan=1, padx=25, pady=10, sticky=W + E)

window.mainloop()

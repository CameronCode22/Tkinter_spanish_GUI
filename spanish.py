from tkinter import *
from random import randint

root = Tk()
root.geometry("550x410")

words = [
    (("Hola"), ("Hello")),
    (("Adios"), ("Goodbye"))
]

count = len(words)

def next():
    global hinter, hint_count

    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")

    hinter = ""
    hint_count = 0

    global random_word
    random_word = randint(0, count-1)
    spanish_word.config(text=words[random_word][0])



spanish_word = Label(root, text = "", font= ("Heletica", 36))
spanish_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font = ('Helvetica', 18))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer")
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text ="Next", command = next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint")
hint_button.grid(row=0, column=2, padx=20)

hint_label = Label(root, text="turtle Code")
hint_label.pack(pady=20)


root.mainloop()
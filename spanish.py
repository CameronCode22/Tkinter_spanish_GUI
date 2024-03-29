from tkinter import *
from random import randint

root = Tk()
root.geometry("550x410")

words = [
    (("Hola"), ("Hello")),
    (("Adios"), ("Goodbye")),
    (("Izquierda"), ("Left")),
    (("Gracias"), ("Thankyou")),
    (("Ayuda"), ("Help")),
    (("Gato"), ("Cat")),

]

count = len(words)

hint_count = 0
hinter = ""
random_word = 0

def next():
    global hinter, hint_count

    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_var.set("")

    hinter = ""
    hint_count = 0

    global random_word
    random_word = randint(0, count-1)
    spanish_word.config(text=words[random_word][0])

def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config (
            text=f"Correct {words[random_word][0]} is {words[random_word][1]}")
    else: 
        answer_label.config(
            text = f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}"

    )



def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_var.set(hinter)
        hint_count += 1
    else:
        hint_var.config(text="No more")



spanish_word = Label(root, text = "", font= ("Heletica", 36))
spanish_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font = ('Helvetica', 18))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command = answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text ="Next", command = next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint", command = hint)
hint_button.grid(row=0, column=2, padx=20)

hint_var = StringVar()
hint_label = Label(root, textvariable=hint_var)
hint_label.pack(pady=20)


root.mainloop()
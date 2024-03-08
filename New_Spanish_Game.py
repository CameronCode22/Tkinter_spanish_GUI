from tkinter import *
from tkinter import messagebox
from random import randint
from spanish_db import VocabularyDatabase

db = VocabularyDatabase("spanish_test.db")

root = Tk()
root.geometry("550x410")

words = db.get_all_words()
count = len(words)

hint_count = 0
hinter = ""
random_word = 0

list_used_indicies = []

def next():
    #if the user selects next, hint_count and hinter will be zero'd
    global hinter, hint_count

    #clearing answer label for the next answer
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_var.set("")

    hinter = ""
    hint_count = 0

    
    #count is taking from the length of words stored in the DB.
    global random_word

    print(list_used_indicies)
    print(count)
    #If the count on numbers used = the amount of words in list, show user all used
    if len(list_used_indicies) == count:
        messagebox.showinfo("All words Used", "Refresh the screen to play again, or add more words")
    else:
        while True:
            #creates random integer
            random_word = randint(0, count-1)
            #searches the list of integers to see if it has been used, if not it will apppend and print and then exit 
            if random_word not in list_used_indicies:
                list_used_indicies.append(random_word)
                spanish_word.config(text=words[random_word][0])
                break

def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text = f"Correct {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text = f"Incorrect {words[random_word][0]} is not {my_entry.get().capitalize()}")
        
def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_var.set(hinter)
        hint_count += 1

def add_new_word():
    #create a new toplevel window for adding words
    add_word_window = Toplevel(root)
    add_word_window.title("Add New Word")

    #db.insert_word(input("Spanish Word"),input("English Word"))
    #Function to handle adding a word

    def add_word_to_database():
        spanish_word = spanish_entry.get()
        english_word = english_entry.get()
        db.insert_word(spanish_word, english_word)
        messagebox.showinfo("Success", "Word added successfully!")
        add_word_window.destroy() #closes second screen

    spanish_label = Label(add_word_window, text="Spanish Word:")
    spanish_label.grid(row=0, column=0, padx=10, pady=10)

    spanish_entry = Entry(add_word_window, font=('Helvetica', 14))
    spanish_entry.grid(row=0, column=1, padx=10, pady=10)

    english_label = Label(add_word_window, text="English Word:")
    english_label.grid(row=1, column=0, padx=10, pady=10)

    english_entry = Entry(add_word_window, font=('Helvetica', 14))
    english_entry.grid(row=1, column=1, padx=10, pady=10)

    confirm_button = Button(add_word_window, text="Confirm", command=add_word_to_database)
    confirm_button.grid(row=2, column=0, columnspan=2, pady=10)

    cancel_button = Button(add_word_window, text="Cancel", command=add_word_window.destroy)
    cancel_button.grid(row=3, column=0, columnspan=2, pady=10)

spanish_word = Label(root, text = "", font= ("Helvetica", 36))
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

#Button for adding New Words
add_word_button = Button(root, text="Add New Word", command=add_new_word)
add_word_button.place(relx=1.0, rely=1.0, anchor=SE)

root.mainloop()
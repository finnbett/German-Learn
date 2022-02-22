from tkinter import *
import pandas
import random
def create_word():
    words = pandas.read_csv("./data/German English Data - Sheet1.csv")
    words_dict = words.to_dict()
    random_index = random.randint(0, 999)
    german_word = words_dict["German"][random_index]
    english_word = words_dict["English"][random_index]
    w.itemconfig(card_text, text=german_word)

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Learn Deutsch")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

w = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
w.create_image(400, 263, image=card_front)
w.config(bg=BACKGROUND_COLOR, highlightthickness=0)
w.create_text(400, 150, text="German", font=("Ariel", 40, "italic"))
card_text = w.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
w.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, highlightthickness=0, command=create_word)
right.grid(row=1, column=0)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=create_word)
wrong.grid(row=1, column=1)
# card_back = PhotoImage(file="./images/card_back.png")
# card_back_image = w.create_image(image=card_back)
create_word()

window.mainloop()

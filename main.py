from tkinter import *
import pandas
import random
current_card = {}
words = pandas.read_csv("./data/German English Data - Sheet1.csv")
to_learn = words.to_dict(orient="records")
def create_word():
    global current_card, flip_timer
    w.after_cancel(id=flip_timer)
    current_card = random.choice(to_learn)
    w.itemconfig(card_title, text= "German", fill="black")
    w.itemconfig(card_text, text= current_card["German"], fill="black")
    w.itemconfig(card, image=card_front)
    flip_timer = w.after(3000, func=change_image)



def change_image():
    w.itemconfig(card_title, text="English", fill="white")
    w.itemconfig(card_text, text= current_card["English"])
    w.itemconfig(card, image=card_back)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Learn Deutsch")
flip_timer = window.after(3000, change_image)
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

w = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
card = w.create_image(400, 263, image=card_front)
w.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = w.create_text(400, 150, text="German", font=("Ariel", 40, "italic"))
card_text = w.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
w.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, highlightthickness=0, command=create_word)
right.grid(row=1, column=0)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=create_word)
wrong.grid(row=1, column=1)

card_back = PhotoImage(file="./images/card_back.png")
#card_back_image = w.create_image(image=card_back)

create_word()

window.mainloop()

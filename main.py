from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Learn Deutsch")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

w = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
w.create_image(400, 263, image=card_front)
w.config(bg=BACKGROUND_COLOR, highlightthickness=0)
w.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
w.create_text(400, 263, text="word", font=("Ariel", 50, "bold"))
w.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, highlightthickness=0)
right.grid(row=1, column=0)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0)
wrong.grid(row=1, column=1)
# card_back = PhotoImage(file="./images/card_back.png")
# card_back_image = w.create_image(image=card_back)

window.mainloop()

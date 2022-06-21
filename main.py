from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#F9FF33"
current_card={}
to_learn={}

try:
    data=pandas.read_csv("known_words.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("shorter_content.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(card_word,text=current_card["English"],fill="black")
    canvas.itemconfig(canvas_image,image=card_image_front)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image,image=card_image_back)
    canvas.itemconfig(card_title,text="Czech",fill="white")
    canvas.itemconfig(card_word,text=current_card["Czech"],fill="white")
    
def is_known():
    to_learn.remove(current_card)
    data_known=pandas.DataFrame(to_learn)
    data_known.to_csv("./known_words.csv",index=False)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_image_front=PhotoImage(file="./images/card_front.png")
card_image_back=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400,263,image=card_image_front)
card_title=canvas.create_text(400,150,text="title",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263, text="word",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

image_right=PhotoImage(file="./images/right.png")
right_button=Button(image=image_right, bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known) 
right_button.grid(column=1,row=1)
image_wrong=PhotoImage(file="./images/wrong.png")
wrong_button=Button(image=image_wrong,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card) 
wrong_button.grid(column=0,row=1)


next_card()
window.mainloop()
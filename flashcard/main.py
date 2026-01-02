import pandas as p
from tkinter import *
from random import *
import json
card={}
file=p.read_csv("french_words.csv")
words=file.to_dict(orient="records")
try:
    with open("Flashcard.json","r") as f:
        a=json.load(f)
    
except:
    a=[]

def next():
    global card,flip_timer
    cardcanvas.itemconfig(cardbg,image=card_front)
    window.after_cancel(flip_timer) 
    card=choice(words)
    if len(a) == len(words):
        cardcanvas.itemconfig(cardtitle, text="Done!", fill="black")
        cardcanvas.itemconfig(cardword, text="You've learned all words 🎉", fill="black")
        return
    if card['French'] not in a:
        cardcanvas.itemconfig(cardtitle,text="French", fill="black")
        cardcanvas.itemconfig(cardword,text=f"{card['French']}", fill="black")
        flip_timer = window.after(3000, flip)
    else:
        next()


def known():
    global a,card
    if cardcanvas.itemcget(cardtitle, "text") != "Flash Card":
        a.append(card['French'])
    next()
    

def flip():
    cardcanvas.itemconfig(cardbg,image=card_back)
    cardcanvas.itemconfig(cardtitle,text="English",fill="white")
    cardcanvas.itemconfig(cardword,text=f"{card['English']}",fill="white")
    
    
BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=lambda: None)


cardcanvas=Canvas(width=900,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front=PhotoImage(file="card_front.png")
card_back=PhotoImage(file="card_back.png")
cardbg=cardcanvas.create_image(450,263,image=card_front)
cardtitle=cardcanvas.create_text(430,150,text="Flash Card",font=("arial",40,"italic"), fill="black")
cardword=cardcanvas.create_text(430,263,text="Press any button",font=("arial",60,"bold"), fill="black")
cardcanvas.grid(row=0,column=0,columnspan=2,pady=30)


wrong=PhotoImage(file="wrong.png")
wrongb=Button(image=wrong,highlightthickness=0,bd=0,relief="flat",bg=BACKGROUND_COLOR,activebackground=BACKGROUND_COLOR,command=next)
wrongb.grid(row=1,column=0,pady=30)

right=PhotoImage(file="right.png")
rightb=Button(image=right,highlightthickness=0,bd=0,relief="flat",bg=BACKGROUND_COLOR,activebackground=BACKGROUND_COLOR,command=known)
rightb.grid(row=1,column=1,pady=30)

window.mainloop()
with open("Flashcard.json","w") as f:
    json.dump(a, f)

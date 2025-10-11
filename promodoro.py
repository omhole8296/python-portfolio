import os
import math
from tkinter import *
os.chdir(r"C:\Users\omhol\OneDrive\Documents\om\om programs\pythonprograms")

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
mm=0
ss=0
settimer=None

reps=0
ticks=""

def countdown(count):
    global settimer
    if count>=0:
        mm=math.floor(count/60)
        ss=count%60
        if mm<10:
            mm=f"0{mm}"
        if ss<10:
            ss=f"0{ss}"
        canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
        settimer=window.after(1000, countdown,count-1)
    else:
        start()
    
def start():
    global reps
    global ticks
    reps+=1
    if reps%9==0:
        reps=0
        return
    elif reps%8==0:
        count=1200
        ticks+="✔"
        tick.config(text=f"{ticks}")
        timer.config(text="Break",fg=RED)
    elif reps%2==0:
        count=300
        ticks+="✔"
        tick.config(text=f"{ticks}")
        timer.config(text="Break",fg=PINK)
    else:
        count=1500
        timer.config(text="Work",fg=GREEN)
    countdown(count)
    
def reset():
    global reps, count,ticks
    window.after_cancel(settimer)
    ticks=""
    reps=0
    count=0
    canvas.itemconfig(timer_text, text="00:00")
    tick.config(text=f"{ticks}")
    timer.config(text="Timer",fg=GREEN)
    
    
window=Tk()
window.config(padx=100,pady=100,bg=YELLOW)
window.title("pomodoro")

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="promodoro_tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(102,125,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

timer=Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW,highlightthickness=0) 
timer.grid(row=0,column=1)

startb=Button(text="Start",highlightthickness=0,bg="white",command=start)
startb.grid(row=2,column=0)

resetb=Button(text="Reset",highlightthickness=0,bg="white",command=reset)
resetb.grid(row=2,column=2)

tick=Label(text="",font=(FONT_NAME,20),fg=GREEN,bg=YELLOW,highlightthickness=0) 
tick.grid(row=3,column=1)

    

window.mainloop()


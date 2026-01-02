import os
os.chdir(r"C:\Users\omhol\OneDrive\Documents\om\om programs\pythonprograms\quizzler-app-start")
from tkinter import *
THEME_COLOR = "#375362"

class UserInterface:
    def correct(self):
        if self.quiz.question_number<10:
            self.quiz.check_answer("True")
            self.score.config( text=f"Score : {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.question_txt,text=self.quiz.next_question())
        elif self.quiz.question_number==10:
            self.score.config( text=f"Score : {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.question_txt,text="Quiz is over")
        
    def wrong(self):
        if self.quiz.question_number<10:
            self.quiz.check_answer("False")
            self.score.config( text=f"Score : {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.question_txt,text=self.quiz.next_question())
        elif self.quiz.question_number==10:
            self.score.config( text=f"Score : {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.question_txt,text="Quiz is over")
            
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain 
        self.window=Tk()
        self.window.title("quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score=Label(text=f"Score : {self.quiz.score}/{self.quiz.question_number}",fg="white",bg=THEME_COLOR)
        self.score.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,highlightthickness=0,bg="white")
        self.question_txt=self.canvas.create_text(150,125,text=self.quiz.next_question(),width=280,font=("arial",15,"italic"), fill=THEME_COLOR,justify="center",anchor="center" )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)   
        
        self.true=PhotoImage(file="true.png")
        self.trueb=Button(image=self.true,highlightthickness=0,bd=0,relief="flat",bg=THEME_COLOR,activebackground=THEME_COLOR,command=self.correct)
        self.trueb.grid(row=2,column=0,pady=30)
        
        self.false=PhotoImage(file="false.png")
        self.falseb=Button(image=self.false,highlightthickness=0,bd=0,relief="flat",bg=THEME_COLOR,activebackground=THEME_COLOR,command=self.wrong)
        self.falseb.grid(row=2,column=1,pady=30)
        self.window.mainloop()
        
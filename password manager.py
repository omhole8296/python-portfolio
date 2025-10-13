from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]
    password_list =password_letters+password_symbols+password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_text.delete(0,END)
    password_text.insert(0,password)
    pyperclip.copy(password)


def search():
    website=website_text.get()
    if len(website)!=0:
        try:
            with open("data.json", "r") as p:
                data=json.load(p)
            messagebox.showinfo(title="Password Info",message=f"Email:{data[website]["email"]}\n Password:{data[website]["password"]}")
        except FileNotFoundError:
            messagebox.showinfo(title="Oops",message="Please add website, email and password first")
        except KeyError:
            messagebox.showinfo(title="Error",message="Invalid website name")
    else:
        messagebox.showinfo(title="Error",message="Please give website name")

def add():
    if len(website_text.get())==0 or len(email_text.get())==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty")
    else:
        is_ok=messagebox.askokcancel(title=website_text.get(),message=f"These are details entered:\n Email:{email_text.get()}\n Password:{password_text.get()} \n is it ok to save")
        if is_ok:
            pdata={
                website_text.get():{
                    "email":email_text.get(),
                    "password":password_text.get()
                }
            }
            try:
                with open("data.json", "r") as p:
                    data=json.load(p)
                    data.update(pdata)
            except :
                data=pdata
            with open("data.json", "w") as p:
                json.dump(data,p,indent=4)
            
            website_text.delete(0,END)
            password_text.delete(0,END)

window=Tk()
window.config(padx=20,pady=20)
window.title("Password Manager")

canvas=Canvas(width=200,height=200,highlightthickness=0)
password_manager=PhotoImage(file="password_manager.png")
canvas.create_image(100,100,image=password_manager)
canvas.grid(row=0,column=1)

website=Label(text="Website:",highlightthickness=0) 
website.grid(row=1,column=0)
website_text=Entry(width=21) 
website_text.grid(row=1,column=1,pady=5)
website_text.focus()

searchb=Button(text="Search",width=15,relief="solid",bd=1,highlightthickness=0,command=search)
searchb.grid(row=1,column=2, pady=5)


email=Label(text="Email/Username:",highlightthickness=0) 
email.grid(row=2,column=0)
email_text=Entry(width=35) 
email_text.insert(0,"xyz@gamil.com")
email_text.grid(row=2,column=1,columnspan=1,pady=5)

password=Label(text="Password:",highlightthickness=0) 
password.grid(row=3,column=0)
password_text=Entry(width=21) 
password_text.grid(row=3,column=1,sticky="W", pady=5)


password_generatorb=Button(text="Password Generator",highlightthickness=0,bg="white",relief="solid",bd=1,command=password_generator)
password_generatorb.grid(row=3,column=2, pady=5)

addb=Button(text="Add",width=36,relief="solid",bd=1,highlightthickness=0,command=add)
addb.grid(row=4,column=1,columnspan=2, pady=5)

window.mainloop()

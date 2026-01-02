import os
os.chdir(r"C:\Users\omhol\OneDrive\Documents\om\om programs\pythonprograms\birthday-wisher-extrahard-start")
import pandas as p
import smtplib as mail
import random
import datetime as dt

file=p.read_csv("birthdays.csv")
data=file.to_dict(orient="records")
now=dt.datetime.now()
today=(now.day,now.month)
for record in data:
    if today==(record["day"],record["month"]):
        letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(f"{letter_path}","r") as r:
            greeting=r.read()
            message=greeting.replace("[NAME]",record['name'])
        with mail.SMTP("smtp.gmail.com") as m:
            m.starttls()
            m.login(user="omhole8296@gmail.com",password="ucrh tpey cwby nivj")
            m.sendmail(from_addr="omhole8296@gmail.com",to_addrs=record['email'],msg=f"Subject:Happy Birthday \n\n {message}")
            print("message is send")
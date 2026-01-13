import smtplib
import requests
from bs4 import BeautifulSoup

URL = f"https://appbrewery.github.io/instant_pot/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}
response=requests.get(URL, headers=header)
content=response.text
soup=BeautifulSoup(content,"html.parser") 

price_spans = soup.find_all("span", class_="aok-offscreen")
prices = [span.getText().strip() for span in price_spans]
p=float(prices[0][1:])

if p<=100:
    mymail="omhole8296@gmail.com"
    quote ="Amazon price Alert"
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()
        subject = "Amazon Price Alert 🚨"
        body = f"""Price dropped to ${p}!
            Buy now:{URL}"""
        message = f"Subject: {subject}\n\n{body}"

        connect.login(user=mymail,password="ucrh tpey cwby nivj")
        connect.sendmail(from_addr=mymail,to_addrs="omchhole@gmail.com",msg=message.encode("utf-8"))

        print("Price is low and Quote mail sent successfully!")
else:
    print("price is not low yet")
    

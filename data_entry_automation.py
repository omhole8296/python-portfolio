import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

URL = f"https://appbrewery.github.io/Zillow-Clone/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}

response=requests.get(URL, headers=header)
content=response.text
soup=BeautifulSoup(content,"html.parser") 

linka= soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
addressa=[re.sub(r"\s+", " ",add.getText().replace("|", " ").replace("\n", " ")).strip() for add in linka]
links=[href.get("href") for href in linka]
  
pricea=soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [[p.strip() for p in re.split(r"[+/]", amount.getText())]for amount in pricea]

driver=webdriver.Chrome()
for i in range(len(prices)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeQFsNp9WeY72M3Lids_7bhVw2kisQ6qR1f7c_Rxho5obLrmw/viewform?usp=dialog")

    address=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address.send_keys(addressa[i])
    price.send_keys(prices[i][0])
    link.send_keys(links[i])
    
    button=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    button.click()
    
driver.quit()
     
    

import smtplib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net/")

wait = WebDriverWait(driver, 150)

try:
    accept = wait.until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    accept.click()
    
except:
    pass


go = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
)
go.click()

time.sleep(60)


download = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "download-speed"))
)

download_speed = float(download.text)


upload = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "upload-speed"))
)
upload_speed = float(upload.text)

print("Download Speed:", download_speed, "Mbps")
print("Upload Speed:", upload_speed, "Mbps")


if download_speed<150 or upload_speed<10:
    mymail="omhole8296@gmail.com"
    quote ="Slow network problem"
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()
        subject = "Slow network problem"
        body = f"when i paid for 150 Mbps dow/10 Mbps up why do i get {download_speed}Mbps dow/{upload_speed} Mbps up"
        message = f"Subject: {subject}\n\n{body}"

        connect.login(user=mymail,password="ucrh tpey cwby nivj")
        connect.sendmail(from_addr=mymail,to_addrs="omchhole@gmail.com",msg=message.encode("utf-8"))

        print("Mail sent successfully!")

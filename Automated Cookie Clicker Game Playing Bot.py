import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 10)

try:
    lan = wait.until(
        EC.element_to_be_clickable(
            (By.ID,'langSelect-EN')
        )
    )
    lan.click()

except:
    print("Language selection not found")
    
    
def check():
    c=0
    value=driver.find_element(By.ID,value="cookies").text.split()
    cookie_count=value[0]
    cookie_count = int(cookie_count.replace(",", ""))
    products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
    best_item = None
    
    for product in reversed(products): 
        if "enabled" in product.get_attribute("class"):
            best_item = product
            break

    if best_item:
                driver.execute_script("arguments[0].click();", best_item)
                print(f"Bought item: {best_item.get_attribute('id')}")

               
cookie=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"bigCookie")
    )
)


timeout = time.time() + 300
next_check = time.time() + 5
while True:
    time.sleep(0.01)
    
    if time.time() > timeout:
        break
    
    if time.time() >= next_check:
        check()
        next_check = time.time() + 5
        # by chainging no. you can change the check time 
        
    cookie.click()



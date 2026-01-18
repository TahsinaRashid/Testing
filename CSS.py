from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

time.sleep(2)

email = driver.find_element(By.CSS_SELECTOR, "#email")
email.send_keys("abc@example.com")
email.clear()
email.send_keys("abc2@example.com")

driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("123456")

time.sleep(5)
driver.quit()

print("Script ran successfully")

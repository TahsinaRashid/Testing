from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.grameenphone.com/")

time.sleep(3)

print("Links:", len(driver.find_elements(By.TAG_NAME, "a")))
print("Divs:", len(driver.find_elements(By.TAG_NAME, "div")))


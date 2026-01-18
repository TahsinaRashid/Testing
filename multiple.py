from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import  time
driver = webdriver.Chrome()
driver.get("https://mini-mart-4242.web.app/Login")
driver.find_element(By.NAME,value="username").send_keys("student")
driver.find_element(By.NAME,value="password").send_keys("Password123")
driver.find_element(By.ID,value="submit").click()
driver.find_element(By.LINK_TEXT,value="Log out").click()
time.sleep(40)





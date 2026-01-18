from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(40)
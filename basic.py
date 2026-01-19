from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#login
driver.find_element(By.NAME,value="user-name").send_keys("standard_user")
driver.find_element(By.NAME,value="password").send_keys("secret_sauce")
driver.find_element(By.ID,value="login-button").click()

#add to cart
driver.find_element(By.NAME,value="add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.NAME,value="add-to-cart-sauce-labs-bike-light").click()

#view cart and checkout
driver.find_element(By.CLASS_NAME,value="shopping_cart_link").click()
driver.find_element(By.NAME,value="checkout").click()

#logout
driver.find_element(By.ID,value="react-burger-menu-btn").click()
time.sleep(5)
driver.find_element(By.ID,value="logout_sidebar_link").click()
time.sleep(50)
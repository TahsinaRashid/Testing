from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.grameenphone.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "swiper-slide"))
)

slides = driver.find_elements(By.CLASS_NAME, "swiper-slide")
print("Total slides:", len(slides))

driver.quit()

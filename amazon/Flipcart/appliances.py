import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/')
#driver.get('https://www.amazon.in/')
driver.maximize_window()


wait = WebDriverWait(driver, 10)
partial_link_element = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Appliances")))
partial_link_element.click()
time.sleep(10)

#print(furtniture)
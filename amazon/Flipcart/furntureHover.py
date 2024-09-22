import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver.get('https://www.flipkart.com/')
driver.get('https://www.amazon.in/')
driver.maximize_window()

#furtniture = driver.find_element(By.XPATH, "//div[@aria-label='Home & Furniture']").text

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Samsung Galaxy M35 5G")

driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

wait = WebDriverWait(driver, 10)
partial_link_element = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Samsung Galaxy M35 5G (Moonlight Blue,6GB RAM,128GB Storage)")))

partial_link_element.click()

print(partial_link_element.get_attribute("href"))

time.sleep(10)

#print(furtniture)
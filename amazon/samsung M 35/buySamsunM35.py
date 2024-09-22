import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Samsung Galaxy M35 5G")

driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

all_models = driver.find_elements(By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'][contains(text(),'Samsung Galaxy M35 5G')])")
print("all models in list")
print(all_models)

myModel = "Samsung Galaxy M35 5G (Thunder Grey,6GB RAM,128GB Storage)| Corning Gorilla Glass Victus+| AnTuTu Score 595K+ | Vapour Cooling Chamber | 6000mAh Battery | 120Hz Super AMOLED Display| without Charger"
i = -1
for model in all_models:
    modelName = model.text
    print(type(modelName))
    print(modelName)
    print(type(model))
    print(model)
    i = i + 1
    if  modelName == myModel:
        print("your model matched")
        #model.find_element(By.XPATH, "//button[@class='a-button-text']").click()
        model.click()



time.sleep(20)




'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.maximize_window()

# Wait for the search box to be interactable and then enter the search query
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='twotabsearchtextbox']"))
)
search_box.send_keys("Samsung Galaxy M35 5G")

# Wait for the search button to be clickable and then click it
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='nav-search-submit-button']"))
)
search_button.click()

# Wait for the search results to load and find all matching models
all_models = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal'][contains(text(),'Samsung Galaxy M35 5G')]"))
)
print("all models in list")
print(all_models)

# Define the model to match
myModel = "Samsung Galaxy M35 5G (Thunder Grey, 6GB RAM, 128GB Storage)"
i = -1

# Iterate through the models and click the corresponding button if matched
for model in all_models:
    modelName = model.text
    print(type(modelName))
    print(modelName)
    print(type(model))
    print(model)
    i = i + 1
    if myModel in modelName:
        print("your model matched")
        # Click on the model itself to go to the product page
        model.click()
        break  # Exit the loop after finding the first match

time.sleep(10)
driver.quit()

'''

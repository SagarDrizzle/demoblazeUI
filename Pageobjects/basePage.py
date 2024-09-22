from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class basePage:
    def __init__(self, driver):
        self.driver = driver

    def do_send_keys(self, by_locator, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(by_locator)).send_keys(text)
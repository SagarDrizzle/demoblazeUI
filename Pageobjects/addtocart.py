from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pageobjects.basePage import basePage


class AddProductToCart(basePage):

    def __init__(self, driver):
        self.driver = driver

    addtocartbutton = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    cartoption = (By.XPATH, "//a[@id='cartur']")
    placeorderbutton = (By.XPATH, "//button[normalize-space()='Place Order']")

    def is_visible(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(AddProductToCart.placeorderbutton))

    def addtocart(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(AddProductToCart.addtocartbutton)).click()


    def gotocart(self):
        return self.driver.find_element(*AddProductToCart.cartoption).click()

    def placeOrder(self):
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_element_located(AddProductToCart.placeorderbutton)).click()




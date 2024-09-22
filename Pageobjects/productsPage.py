from selenium.webdriver.common.by import By

class Products:

    def __init__(self, driver):
        self.driver = driver

    storeTitele = (By.XPATH, "//a[@id='nava']")
    mobilecategory = (By.XPATH, "//div[@id='contcont']//a[2]")
    laptopcategory = (By.XPATH, "//a[3]")
    productlist = (By.XPATH, "//a[@class='hrefch']")

    def getname(self):
        return self.driver.find_element(*Products.storeTitele)

    def clickmobile(self):
        return self.driver.find_element(*Products.mobilecategory).click()

    def clicklaptop(self):
        return self.driver.find_element(*Products.laptopcategory).click()

    def getproducttitles(self):
        return self.driver.find_elements(*Products.productlist)



    #//div[@id='tbodyid']//div[1]//div[1]//div[1]
    #//div[@id='tbodyid']//div[1]//div[1]//div[1]
    #//div[@id='tbodyid']//div[1]//div[1]//div[1]//p[1]
    #//div[@id='tbodyid']//div[1]//div[1]//div[1]//p[1]




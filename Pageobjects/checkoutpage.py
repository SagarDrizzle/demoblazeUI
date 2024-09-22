from selenium.webdriver.common.by import By

from Pageobjects.basePage import basePage


class ProductCheckOutPage(basePage) :

    def __init__(self, driver):
        self.driver = driver

    name = (By.XPATH, "//input[@id='name']")
    country = (By.XPATH, "//input[@id='country']")
    city = (By.XPATH, "//input[@id='city']")
    card = (By.XPATH, "//input[@id='card']")
    month = (By.XPATH, "//input[@id='month']")
    year = (By.XPATH, "//input[@id='year']")
    purchasebutton = (By.XPATH, "//button[normalize-space()='Purchase']")
    confirmationalert = (By.XPATH, "//h2[normalize-space()='Thank you for your purchase!']")
    oredercompleteokbutton = (By.XPATH, "//button[normalize-space()='OK']")


    def fillChekOutForm(self, username, countryname, cityName, carddetails, monthdetails, yeardetails):
        self.do_send_keys(self.name,username)
        self.do_send_keys(self.country, countryname)
        self.do_send_keys(self.city, cityName)
        self.do_send_keys(self.card, carddetails)
        self.do_send_keys(self.month, monthdetails)
        self.do_send_keys(self.year, yeardetails)

    def purchaseproductconfirm(self):
        return self.driver.find_element(*ProductCheckOutPage.purchasebutton).click()

    def orderconfirmation(self):
        orederconfirmmsg = self.driver.find_element(*ProductCheckOutPage.purchasebutton).text
        print(orederconfirmmsg)
        assert "Thank you for your purchase!" in orederconfirmmsg


    def ordercompleted(self):
        return self.driver.find_element(*ProductCheckOutPage.oredercompleteokbutton).click()




    ''' Old Code with multile method for each input field
    def fillname(self):
        return self.driver.find_element(*ProductCheckOutPage.name).send_keys(ProductCheckOutPage.username)

    def fillcountry(self):
        return self.driver.find_element(*ProductCheckOutPage.country).send_keys(ProductCheckOutPage.countryname)
    
    def fillcity(self):
        return self.driver.find_element(*ProductCheckOutPage.city).send_keys(ProductCheckOutPage.cityName)

    def fillcard(self):
        return self.driver.find_element(*ProductCheckOutPage.Card).send_keys(ProductCheckOutPage.carddetails)

    def fillmonth(self):
        return self.driver.find_element(*ProductCheckOutPage.month).send_keys(ProductCheckOutPage.monthdetails)

    def fillyear(self):
        return self.driver.find_element(*ProductCheckOutPage.year).send_keys(ProductCheckOutPage.yeardetails)
        
    '''





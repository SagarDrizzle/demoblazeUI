import time

from Pageobjects.addtocart import AddProductToCart
from Pageobjects.checkoutpage import ProductCheckOutPage
from Pageobjects.productsPage import Products
from Utilities.Configuration import Test_data
from Utilities.baseclass import baseClass


class TestOrderCompleteProduct(baseClass):

    def test_OrderCompleteProduct(self):

        productsobj = Products(self.driver)

# ============ Verify weather you are landed on product store ==============
        dashboardtitle = productsobj.getname().text
        print("You are on dashboard "+ dashboardtitle)
        self.driver.implicitly_wait(5)

# =============== choose and click on product category ================================
        if Test_data.testCategory == "laptop":
            productsobj.clicklaptop()

        else:
            productsobj.clickmobile()

        time.sleep(5)

# ========== Iterate,search and click for desired product from product list =========

        listofproduct = productsobj.getproducttitles()

        for product in listofproduct:
            productname = product.text
            print(productname)


            if productname == Test_data.productNmae :
                product.click()
                print("Your choosen Product is " + productname)
                break


# =============== add desired product to cart =============================

        cartobj = AddProductToCart(self.driver)
        cartobj.addtocart()
        time.sleep(3)

# =============== Accept alert when add to cart process complete ====================

        #alert = self.driver.switch_to.alert
        alert = self.driver.switch_to.alert
        alert.accept()

# =============== Go to cart section and place order =================================
        cartobj.gotocart()
        cartobj.placeOrder()

# ============= fill form details for final product purchase=============================
        checkoutobj = ProductCheckOutPage(self.driver)
        checkoutobj.fillChekOutForm(Test_data.username, Test_data.countryname,Test_data.carddetails,Test_data.monthdetails,Test_data.yeardetails,Test_data.cityName)
        """checkoutobj.fillname()
        checkoutobj.fillcountry()"""

# ============= Confirm purchase after form details =============================
        checkoutobj.purchaseproductconfirm()

# ============= check your purchase order and click on ok =============================
        checkoutobj.ordercompleted()









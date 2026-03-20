from page_objects.checkoutPage import CheckoutPage
from page_objects.common import Common
from page_objects.loginPage import LoginPage
from page_objects.myCartPage import MyCartPage
from page_objects.productPage import ProductPage
from page_objects.productViewPage import ProductViewPage


class PoController:
    def __init__(self, page):
        self.page = page
        self.loginPage = LoginPage(self.page)
        self.checkoutPage = CheckoutPage(self.page)
        self.common = Common(self.page)
        self.checkoutPage = CheckoutPage(self.page)
        self.myCartPage = MyCartPage(self.page)
        self.productPage = ProductPage(self.page)
        self.productViewPage = ProductViewPage(self.page)

    def getLoginPage(self):
        return self.loginPage

    def getCheckoutPage(self):
        return self.checkoutPage

    def getCommon(self):
        return self.common

    def getCheckoutPage(self):
        return self.checkoutPage

    def getMyCartPage(self):
        return self.myCartPage

    def getProductPage(self):
        return self.productPage

    def getProductViewPage(self):
        return self.productViewPage








from page_objects.poController import PoController
from Data.data import Data

def test_endToEnd_inChrome(setupChromeBrowser):
    webContext = setupChromeBrowser
    page = webContext.new_page()
    poController = PoController(page)
    loginPage = poController.getLoginPage()
    credentials = Data.credentials
    loginPage.login(credentials["username"], credentials["password"])
    productPage = poController.getProductPage()
    testProduct = productPage.getTestProduct()
    productPage.verifyViewButton(testProduct)
    productViewPage = poController.getProductViewPage()
    productViewPage.addProductFromViewPage(testProduct)
    checkoutPage = poController.getCheckoutPage()
    checkoutPage.checkoutAndVerifyProduct(testProduct)


def test_endToEnd_inFirefox(setupFirefoxBrowser):
    webContext = setupFirefoxBrowser
    page = webContext.new_page()
    poController = PoController(page)
    loginPage = poController.getLoginPage()
    credentials = Data.credentials
    loginPage.login(credentials["username"], credentials["password"])
    productPage = poController.getProductPage()
    testProduct = productPage.getTestProduct()
    productPage.verifyViewButton(testProduct)
    productViewPage = poController.getProductViewPage()
    productViewPage.addProductFromViewPage(testProduct)
    checkoutPage = poController.getCheckoutPage()
    checkoutPage.checkoutAndVerifyProduct(testProduct)


def test_endToEnd(browserInstance):
    page = browserInstance
    poController = PoController(page)
    productPage = poController.getProductPage()
    testProduct = productPage.getTestProduct()
    productPage.verifyViewButton(testProduct)
    productViewPage = poController.getProductViewPage()
    productViewPage.addProductFromViewPage(testProduct)
    checkoutPage = poController.getCheckoutPage()
    checkoutPage.checkoutAndVerifyProduct(testProduct)
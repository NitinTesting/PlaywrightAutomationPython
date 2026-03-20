import random

from playwright.sync_api import expect
from Data.data import Data
class ProductPage:
    def __init__(self, page):
        self.page = page
        self.products = self.page.locator(".card-body")

    def verifyViewButton(self, testproduct):
        product = self.products.filter(has_text=testproduct)
        viewBtn = product.get_by_role("button", name=" View")
        viewBtn.click()
        productname = self.page.locator("h2")
        productname.wait_for()
        print(productname.text_content())
        expect(productname).to_have_text(testproduct)

    def getTestProduct(self):
        a = Data.products
        productNumber = random.randint(0,len(a)-1)
        testProduct = a[productNumber]
        return testProduct
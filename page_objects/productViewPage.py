from page_objects.productPage import ProductPage
from playwright.sync_api import expect


class ProductViewPage:
    def __init__(self, page):
        self.page = page
        self.addToCartBtn = self.page.get_by_role("button", name="Add to Cart")

    def addProductFromViewPage(self, testproduct):
        self.addToCartBtn.click()
        self.page.locator("[routerlink='/dashboard/cart']").click()
        cartProduct = self.page.locator(".cartSection h3")
        expect(cartProduct).to_have_text(testproduct)
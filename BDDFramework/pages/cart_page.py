class CartPage:
    def __init__(self,page):
        self.page = page
        self.in_cart_product = self.page.locator("div .cartSection h3")
        self.checkout_btn = self.page.get_by_role("button", name="Checkout")

    def verifyProductOnCart(self,product_name):
        cart_product = self.in_cart_product.text_content()
        assert cart_product == product_name

    def proceedToCheckout(self):
        self.checkout_btn.click()
        self.page.locator(".action__submit").wait_for()
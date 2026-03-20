class MyCartPage:
    def __init__(self, page):
        self.page = page

    def proceedToCheckout(self):
        checkoutBtn = self.page.get_by_role("button", name="Checkout")
        checkoutBtn.click()
        placeOrderBtn = self.page.locator(".action__submit")
        placeOrderBtn.wait_for()
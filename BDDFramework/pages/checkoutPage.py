class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.selectCountry = self.page.get_by_placeholder("Select Country")
        self.countryOption = self.page.locator(".ta-item")
        self.placeOrderBtn = page.locator(".action__submit")

    def place_order(self):
        self.selectCountry.press_sequentially("ind", delay=150)
        self.countryOption.filter(has_text="India").nth(1).click()
        self.placeOrderBtn.click()
        self.page.get_by_role("button", name=" Click To Download Order Details in CSV").wait_for()
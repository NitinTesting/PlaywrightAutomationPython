class Common:
    def __init__(self, page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url)

    def open_cart(self):
        cart = self.page.locator("[routerlink='/dashboard/cart']")
        cart.click()
        self.page.get_by_role("button", name="Checkout").wait_for()
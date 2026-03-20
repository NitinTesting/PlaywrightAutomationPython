class ProductPage:
    def __init__(self, page):
        self.page = page
        self.productCard = self.page.locator("div .card-body")


    def wait_for_product_page_open(self):
        self.productCard.last.wait_for()

    def click_view_button_for(self,product_name):
        product = self.productCard.filter(has_text=product_name)
        product.get_by_role("button", name=" View").click()
        self.page.locator("//a[@class='continue']").wait_for()

    def click_add_to_cart_button(self,product_name):
        product = self.productCard.filter(has_text=product_name)
        product.get_by_role("button", name=" Add To Cart").click()
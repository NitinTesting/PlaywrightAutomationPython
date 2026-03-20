class ViewPage:
    def __init__(self, page):
        self.page = page
        self.viewPageProduct = page.locator("div h2")

    def verifyViewPageProductAs(self, product_name):
        product = self.viewPageProduct.text_content()
        assert product == product_name, "|{}|".format(product)
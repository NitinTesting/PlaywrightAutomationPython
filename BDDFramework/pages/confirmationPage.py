class ConfirmationPage:
    def __init__(self, page):
        self.page = page
        self.confirmationPageProduct = self.page.locator("div .title")

    def verifyProductOnConfirmationPage(self, product_name):
        final_product = self.confirmationPageProduct.first.text_content()
        assert final_product == product_name,"Final Product:{} is not as expected:{}".format(final_product,product_name)
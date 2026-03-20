from page_objects.myCartPage import MyCartPage
from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def checkoutAndVerifyProduct(self, product):
        myCartPage = MyCartPage(self.page)
        myCartPage.proceedToCheckout()
        selectCountry = self.page.get_by_placeholder("Select Country")
        selectCountry.press_sequentially("ind", delay=150)
        countryOption = self.page.locator(".ta-item")
        countryOption.filter(has_text="India").nth(1).click()
        cardDetails = self.page.locator(".field .input")
        cvvCode = cardDetails.nth(3)
        name = cardDetails.nth(4)
        cvvCode.fill("123")
        name.fill("Nitin")
        placeOrderBtn = self.page.locator(".action__submit")
        placeOrderBtn.click()
        thanksMessage = self.page.locator(".hero-primary").text_content()
        assert thanksMessage == " Thankyou for the order. "
        successProduct = self.page.locator(".title:has-text('{}')".format(product))
        expect(successProduct).to_be_visible()
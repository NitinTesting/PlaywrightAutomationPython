from pages.productPage import ProductPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.usernameTextBox = self.page.locator("#userEmail")
        self.passwordTextBox = self.page.locator("#userPassword")
        self.loginButton = self.page.get_by_role("button", name="Login")
        self.productpage = ProductPage(self.page)

    def user_login(self, username, password):
        self.usernameTextBox.fill(username)
        self.passwordTextBox.fill(password)
        self.loginButton.click()
        self.productpage.wait_for_product_page_open()
from page_objects.common import Common


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder("email@example.com")
        self.password = page.get_by_placeholder("enter your passsword")
        self.loginbtn = page.get_by_role("button", name="Login")
        self.common = Common(self.page)

    def login(self,username, password, url):
        self.common.openPage(url)
        self.username.fill(username)
        self.password.fill(password)
        self.loginbtn.click()
        products = self.page.locator(".card-body")
        products.last.wait_for()
from playwright.sync_api import expect

class Common:
    def __init__(self, page):
        self.page = page


    def openPage(self, url):
        self.page.goto(url)


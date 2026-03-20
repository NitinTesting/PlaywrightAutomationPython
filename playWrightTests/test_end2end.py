import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playwright.sync_api import Page, Browser, expect, Playwright
from Data.data import Data

from page_objects.loginPage import LoginPage


def test_verifyViewPage(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    username = page.locator("#userEmail")
    password = page.locator("#userPassword")
    loginButton = page.get_by_role("button", name="Login")
    username.fill(Data.credentials["username"])
    password.fill(Data.credentials["password"])
    loginButton.click()
    productCard = page.locator("div .card-body")
    productCard.last.wait_for()
    products =productCard.locator("b")
    product = productCard.filter(has_text="ZARA COAT 3")
    product.get_by_role("button", name=" View").click()
    page.locator("//a[@class='continue']").wait_for()
    page.screenshot(path="viewpage.png")
    viewPageProduct = page.locator("div h2").text_content()
    assert viewPageProduct == "ZARA COAT 3","|{}|".format(viewPageProduct)


def test_endToEnd_scenario(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    username = page.locator("#userEmail")
    password = page.locator("#userPassword")
    loginButton = page.get_by_role("button", name="Login")
    username.fill(Data.credentials["username"])
    password.fill(Data.credentials["password"])
    loginButton.click()
    productCard = page.locator("div .card-body")
    productCard.last.wait_for()
    product = productCard.filter(has_text="ZARA COAT 3")
    # page.pause()
    product.get_by_role("button", name=" Add To Cart").click()
    cart = page.locator("[routerlink='/dashboard/cart']")
    cart.click()
    checkout_btn = page.get_by_role("button", name="Checkout")
    checkout_btn.wait_for()
    in_cart_product = page.locator("div .cartSection h3")
    assert in_cart_product.text_content() == "ZARA COAT 3","|{}|".format(in_cart_product)
    checkout_btn.click()
    selectCountry = page.get_by_placeholder("Select Country")
    selectCountry.press_sequentially("ind", delay=150)
    countryOption = page.locator(".ta-item")
    countryOption.filter(has_text="India").nth(1).click()
    placeOrderBtn = page.locator(".action__submit")
    placeOrderBtn.click()
    page.get_by_role("button", name=" Click To Download Order Details in CSV").wait_for()
    confirmationPageProduct = page.locator("div .title")
    final_product = confirmationPageProduct.first.text_content()
    assert final_product == "ZARA COAT 3"
    page.close()






from behave import given, when, then
from playwright.sync_api import Playwright, Page, sync_playwright

from pages.common import Common
from pages.login_page import LoginPage
from pages.productPage import ProductPage
from pages.viewPage import ViewPage
from pages.cart_page import CartPage
from pages.checkoutPage import CheckoutPage
from pages.confirmationPage import ConfirmationPage


@given('user on login page')
def navigate_to_login_page(context):
    page = context.page
    common = Common(page)
    common.open_url("https://rahulshettyacademy.com/client/#/auth/login")


@when("user successfully login with {username} and {password}")
def validLogin(context, username, password):
    page = context.page
    loginPage = LoginPage(page)
    loginPage.user_login(username, password)


@when("user select a product {product_name} to view")
def clickViewButtonforProduct(context, product_name):
    page = context.page
    product_page = ProductPage(page)
    product_page.click_view_button_for(product_name)


@then("view page is showing correct product {product_name}")
def verifyProductOnViewpage(context, product_name):
    page = context.page
    view_page = ViewPage(page)
    view_page.verifyViewPageProductAs(product_name)

@when("user select a product {product_name} to add to cart")
def addToCartProduct(context, product_name):
    page = context.page
    product_page = ProductPage(page)
    product_page.click_add_to_cart_button(product_name)

@then("user should see product {product_name} in the cart")
def verifyProductOnCartpage(context, product_name):
    page = context.page
    common = Common(page)
    common.open_cart()
    cart_page = CartPage(page)
    cart_page.verifyProductOnCart(product_name)

@when("from MyCart page proceed to checkout")
def proceedToCheckout(context):
    page = context.page
    cart_page = CartPage(page)
    cart_page.proceedToCheckout()

@when("place order")
def placeOrder(context):
    page = context.page
    checkout_page = CheckoutPage(page)
    checkout_page.place_order()

@then("verify product in the {product_name} Thanks page")
def verifyConfirmationPage(context, product_name):
    page = context.page
    confirmation_page = ConfirmationPage(page)
    confirmation_page.verifyProductOnConfirmationPage(product_name)

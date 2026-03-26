import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

pytest

@pytest.mark.selenium
def test_selenium_cases():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/client/#/auth/login")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//*[@id='userEmail']").send_keys("Nqatest@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='userPassword']").send_keys("testQA@1111")
    driver.find_element(By.XPATH,"//*[@id='login']").click()
    driver.implicitly_wait(30)

    product_cards = driver.find_elements(By.XPATH,"//*[@class='card-body']")
    for product in product_cards:
        product_name = product.find_element(By.TAG_NAME,"b").text
        print(product_name)
        if product_name == "ZARA COAT 3":
            product.find_element(By.XPATH,".//button[text()=' Add To Cart']").click()
            print(product_name)
    # driver.find_element(By.XPATH,"//button[@routerlink='/dashboard/cart']").click()
    time.sleep(5)
    wait = WebDriverWait(driver, 20)
    cart_link = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[@routerlink='/dashboard/cart']")))
    cart_link.click()
    # cart_product = driver.find_element("//*[@class='cartSection']//h3")
    cart_product = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@class='cartSection']//h3")))
    print(cart_product.text)





#
# def test_new_ui():
#     driver = webdriver.Chrome()
#     driver.get("https://rahulshettyacademy.com/client/#/auth/login")
#



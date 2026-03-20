from playwright.sync_api import expect, Page, Request, Browser, Playwright
import pytest
from utils.apiBase import ApiUtils


def test_end2end_api(playwright: Playwright):
    apiUtils = ApiUtils(playwright)
    loginresponse = apiUtils.loginviaAPI()
    responseJson = loginresponse.json()
    token = responseJson["token"]
    expect(loginresponse).to_be_ok()
    orderResponse = apiUtils.getOrderResponse(token)
    print(orderResponse.status)
    expect(orderResponse).to_be_ok()
    orderResponseJson = orderResponse.json()
    orderID = orderResponseJson["orders"]
    print(orderResponseJson["message"])
    print(orderID[0])
    print("------------------")
    viewOrderResponse = apiUtils.getViewOrderResponse(token)
    viewOrderjson = viewOrderResponse.json()
    orders = viewOrderjson["data"]
    assert any(orderID[0] == order["_id"] for order in orders), "{} does not match with any id".format(orderID)


# @pytest.mark.apitesting
def test_api(playwright: Playwright):
    price = 500
    apiContext = playwright.request.new_context()
    myRequest = apiContext.post("https://fakestoreapi.com/products",
                                data={
        "title": "Test Product",
        "price": price,
        "description": "Automation testing",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    })
    expect(myRequest).to_be_ok()
    myResponse = myRequest.json()
    print(myResponse["price"])
    print(myResponse["id"])
    assert "id" in myResponse
    responsePrice = myResponse["price"]
    assert responsePrice == price,"response price.{} does not match with price:{}".format(responsePrice, price)


def test_validate_dummy_json(playwright: Playwright):
    apiContext = playwright.request.new_context()
    dummy_response = apiContext.post("https://jsonplaceholder.typicode.com/posts",
                                     data={"title": "Playwright Test",
                                           "body": "Learning API automation",
                                           "userId":1})
    response_json = dummy_response.json()
    response_status = dummy_response.status
    assert response_status == 201,"response status is not 201, actual is {}".format(response_status)
    print(response_json['id'])
    print("------------------------------------------------")
    print(dummy_response.headers)
    print("------------------------------------------------")
    print(dummy_response.body())
    print("------------------------------------------------")
    print(dummy_response.json())



class ApiUtils:
    def __init__(self, playwright):
        self.playwright = playwright
        self.apiContext = self.playwright.request.new_context()

    def loginviaAPI(self):
        loginresponse = self.apiContext.post("https://rahulshettyacademy.com/api/ecom/auth/login",
                                             data={"userEmail": "Nqatest@gmail.com", "userPassword": "testQA@1111"})
        return loginresponse


    def getOrderResponse(self,token):
        orderResponse = self.apiContext.post("https://rahulshettyacademy.com/api/ecom/order/create-order",
                                        data={"orders": [
                                            {"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]},
                                        headers={"content-type": "application/json",
                                                 "authorization": token})
        return orderResponse

    def getViewOrderResponse(self, token):
        viewOrderResponse = self.apiContext.get(
            "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/6965f659c941646b7a94b01f",
            headers={"authorization": token})
        return viewOrderResponse



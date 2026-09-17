from playwright.sync_api import Playwright

ordersPayload = { "orders":[{"country": "India", "productOrderedId": "6960ea76c941646b7a8b3dd5"}] } 


class APIUtils:
    
    def get_token(self, playwright: Playwright, user_credentials):
        user_email = user_credentials["user_email"]
        user_password = user_credentials["user_password"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user_email, "userPassword": user_password})
        assert response.ok
        
        # print(response.json())
        responseBody = response.json()
        return responseBody["token"]
    
    def create_order(self, playwright: Playwright, user_credentials):
        token = self.get_token(playwright, user_credentials)
        
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data = ordersPayload,
                                            headers={
                                                "Authorization": token,
                                                "Content-Type": "application/json"
                                            })
        # print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id
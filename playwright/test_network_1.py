from playwright.sync_api import Page, expect

the_url = "https://rahulshettyacademy.com/client/"
the_username = "whyrom@ukr.net"
the_password = "Abc123!!!"

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

#-> api-call from the browser -> an api-call contacts the server and returns back the response to browser 
# -> browser uses response to generate html data
def intercept_response(route):
    # to back the response
    route.fulfill(
        json = fakePayloadOrderResponse
    ) 

# {"data":[],"message":"No Orders"}
def test_network_one_intercept_response(page: Page):
    page.goto(the_url)
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    
    page.get_by_placeholder("email@example.com").fill(the_username)
    page.get_by_role("textbox", name="enter your passsword").fill(the_password)    
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    
    order_text = page.locator(".container.table-responsive.py-5").text_content()
    print(f"\n ======>>>>>>{order_text}")
    expect(page.locator(".container.table-responsive.py-5")).to_contain_text("You have No Orders to show at this time.")

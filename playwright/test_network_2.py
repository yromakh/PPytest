import time

from playwright.sync_api import Playwright, Page, expect

from utils.api_base import APIUtils

the_url = "https://rahulshettyacademy.com/client/"
the_username = "whyrom@ukr.net"
the_password = "Abc123!!!"
the_username_2 = "rahulshetty@gmail.com"
the_password_2 = "Iamking@000"

#-> api-call from the browser -> 
# an api-call contacts the server (WE ARE MOCKING HERE) and returns back the response to browser -> browser uses response to generate html data
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6aa3c5c1e7cd69710fd1c572")
    

# {"data":[],"message":"No Orders"}
def test_network_two_intercept_request(page: Page):
    page.goto(the_url)  
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    
    page.get_by_placeholder("email@example.com").fill(the_username)
    # page.pause()
    page.get_by_role("textbox", name="enter your passsword").fill(the_password)    
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    
    page.get_by_role("button", name="View").first.click()
    not_authorize_message = page.locator(".blink_me").text_content()
    print(not_authorize_message)
    assert not_authorize_message == "You are not authorize to view this order"
    # page.pause()

def test_session_storage(playwright: Playwright):
    # getting a token
    api_utils = APIUtils()
    get_token = api_utils.get_token(playwright)
    
    # new browser/context/page creation
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    #script to inject token is session of local storage ===
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    
    # open address with added token in the previous step
    page.goto(the_url)
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_role("heading", name="Your Orders")).to_be_visible()
    
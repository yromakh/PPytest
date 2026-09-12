import json

from playwright.sync_api import Page, Playwright, expect
import pytest
from utils.api_base import APIUtils

the_url = "https://rahulshettyacademy.com/client/"
the_username = "whyrom@ukr.net"
the_password = "Abc123!!!"

    
# Json file -> util -> access into test
with open('./playwright/data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_web_api_with_data_from_file(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # get order id
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)
    
    # login in UI
    page.goto(the_url)
    page.get_by_placeholder("email@example.com").fill(user_credentials["user_email"])
    page.get_by_role("textbox", name="enter your passsword").fill(user_credentials["user_password"])    
    page.get_by_role("button", name="Login").click()
    
    # open orders History page -> order is present > open it and verify message "Thank you for Shopping With Us"
    page.get_by_role("button", name="ORDERS").click()
    page.locator("tr").filter(has_text=order_id).get_by_role("button", name="View").click()
    
    expect(page.locator(".email-preheader")).to_contain_text("Thank you for Shopping With Us")
    context.close()

@pytest.fixture(scope="function")
def login_to_shop(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(the_url)
    page.get_by_placeholder("email@example.com").fill(the_username)
    page.get_by_role("textbox", name="enter your passsword").fill(the_password)    
    page.get_by_role("button", name="Login").click()
    return page

def test_login_using_fixture(page: Page, login_to_shop):
    page = login_to_shop
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_role("heading", name="Your Orders")).to_be_visible()

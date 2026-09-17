import json
from playwright.sync_api import Playwright
import pytest
from page_objects.login import LoginPage
from utils.api_base_framework import APIUtils

# Json file -> util -> access into test
with open('./playwright/data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_web_api_with_data_from_file(playwright: Playwright, browser_instance, user_credentials):
    user_name = user_credentials["user_email"]
    user_password = user_credentials["user_password"]
    
    # create order -> get order id
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)

    login_page = LoginPage(browser_instance)
    login_page.navigate()
    dashboard_page = login_page.login(user_name, user_password)

    orders_history_page = dashboard_page.select_orders_nav_lik()
    order_details_page = orders_history_page.select_order(order_id)
    order_details_page.verify_order_message()

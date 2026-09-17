import pytest
from pytest_bdd import given, scenarios, then, when, parsers
from page_objects.login import LoginPage
from utils.api_base_framework import APIUtils

scenarios("./features/orderTransaction.feature")

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse("place the item order with {username} and {password}"))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["user_email"] = username
    user_credentials["user_password"] = password
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)
    shared_data["order_id"] = order_id


@given("the user is on the landing page")
def user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    shared_data["login_page"] = login_page


@when(parsers.parse("I login to portal with {username} and {password}"))
def login_to_portal(username, password, shared_data):
    login_page = shared_data["login_page"]
    dashboard_page = login_page.login(username, password)
    shared_data["dashboard_page"] = dashboard_page


@when("navigate to orders page")
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data["dashboard_page"]
    orders_history_page = dashboard_page.select_orders_nav_lik()
    shared_data["orders_history_page"] = orders_history_page


@when("select the orderId")
def select_order_id(shared_data):
    order_id = shared_data["order_id"]
    orders_history_page = shared_data["orders_history_page"]
    order_details_page = orders_history_page.select_order(order_id)
    shared_data["order_details_page"] = order_details_page


@then("order message is successfully displayed")
def verify_order_message(shared_data):
    order_details_page = shared_data["order_details_page"]
    order_details_page.verify_order_message()

from page_objects.orders_history import OrdersHistoryPage


class DashboardPage:
    def __init__(self, page):
            self._page = page
            
    def select_orders_nav_lik(self):
        self._page.get_by_role("button", name="ORDERS").click()
        orders_history_page = OrdersHistoryPage(self._page)
        return orders_history_page
    
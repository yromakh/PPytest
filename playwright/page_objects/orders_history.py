from page_objects.order_details import OrderDetailsPage


class OrdersHistoryPage:
    def __init__(self, page):
        self._page = page
            
    def select_order(self, order_id):
        self._page.locator("tr").filter(has_text=order_id).get_by_role("button", name="View").click()
        order_details_page = OrderDetailsPage(self._page)
        return order_details_page
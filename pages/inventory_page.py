from typing import Literal
from pages.cart_page import Cart_page

class Inventory:
    SortType = Literal['az', 'za', 'lohi', 'hilo']
    def __init__(self, page):
        self.page = page
        self.inventory_list = page.locator('.inventory_item')
        self.sort_button = page.locator('.product_sort_container')
        self.cart_button = page.locator('.shopping_cart_link')
        self.cart_button_badge = page.locator('.shopping_cart_badge')

    def is_page_loaded(self):
        return self.page.url.endswith("/inventory.html")

    def check_cart_loaded(self):
        has_items = self.cart_button_badge.is_visible()
        print(f"cart has items = {has_items}")
        if has_items:
            items_added = self.cart_button_badge.inner_text()
            return items_added
        return None

    def items_count(self):
        return self.inventory_list.count()

    def get_item_details(self):
        current_items = self.page.locator('.inventory_item').all()
        item_data = []
        for item in current_items:
            name = item.locator('.inventory_item_name ').inner_text()
            price_str = item.locator('.inventory_item_price').inner_text()
            price_float = float(price_str.replace("$",""))
            item_data.append((name, price_float))
        return item_data

    def add_item_to_cart(self, items_list):
        inventory_items = self.inventory_list.all()
        item_count = len(inventory_items)
        for item_number in items_list:
            if item_number < 0 or item_number >= item_count:
                raise ValueError(f"Invalid item number: {item_number}."
                                 f"The page only has {item_count}, (0 to {item_count - 1}).)")
            inventory_items[item_number].get_by_role("button", name="Add to cart").click()

    def go_to_cart(self):
        self.cart_button.click()
        cart = Cart_page(self.page)
        return cart

    def sort_items(self, option: SortType):
        self.sort_button.select_option(option)
        current_sort_option = self.page.locator('.active_option').inner_text()
        selected_sort_option = self.sort_button.locator(f'option[value={option}]').inner_text()
        assert current_sort_option == selected_sort_option
from pages.checkout_info_page import CheckoutInformationPage

class Cart_page:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator('.cart_item')
        self.checkout_btn = page.get_by_role("button", name = "checkout")
        self.continue_shopping_btn = page.get_by_role("button", name = "continue-shopping")
        self.remove_buttons = page.get_by_role("button", name = "Remove")

    def get_item_count(self):
        return self.cart_items.count()

    def items_in_cart(self):
        all_items = self.page.locator('.cart_item').all()
        print("Items in Cart are:")
        for item in all_items:
            item_name = item.locator(".inventory_item_name").inner_text()
            item_price = item.locator(".inventory_item_price").inner_text()
            print(item_name, item_price)

    def remove_items_in_cart(self):
        while self.remove_buttons.count() > 0:
            self.remove_buttons.first.click()

    def click_checkout(self):
        self.checkout_btn.click()
        checkout_info = CheckoutInformationPage(self.page)
        return checkout_info
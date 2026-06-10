
class CheckoutOverview:
    SUCCESS_MESSAGE = "Thank you for your order!"
    def __init__(self, page):
        self.page = page
        self.cancel_btn = page.get_by_role("button", name = "cancel")
        self.finish_btn = page.get_by_role("button", name = "finish")
        self.payment_info = page.locator(".summary_value_label[data-test=payment-info-value]")
        self.shipping_info = page.locator(".summary_value_label[data-test=shipping-info-value]")
        self.item_subtotal = page.locator(".summary_subtotal_label")
        self.tax_total = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")

    def get_order_details(self):
        print(f"Shipping info: {self.shipping_info.inner_text()}")
        print(f"Payment info: {self.payment_info.inner_text()}")
        print(self.item_subtotal.inner_text())
        print(self.tax_total.inner_text())
        print(self.total.inner_text())

    def click_finsh(self):
        self.finish_btn.click()

    def is_order_placed(self):
        complete_message = self.page.locator(".complete-header").inner_text()
        return complete_message == self.SUCCESS_MESSAGE

    def click_cancel(self):
        self.cancel_btn.click()
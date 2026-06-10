from pages.checkout_overview_page import CheckoutOverview

class CheckoutInformationPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_btn = page.get_by_role("button", name = "continue")
        self.cancel_btn = page.get_by_role("button", name = "cancel")
        self.error_btn = page.locator("h3[data-test='error']")

    def click_continue(self):
        self.continue_btn.click()
        overview = CheckoutOverview(self.page)
        return overview

    def click_cancel(self):
        self.cancel_btn.click()

    def enter_details(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def read_error_message(self):
        if self.error_btn.is_visible():
            return self.error_btn.inner_text()
        return None

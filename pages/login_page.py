from typing import Literal
from playwright.sync_api import expect
from pages.inventory_page import Inventory

class LoginPage:
    URL = "https://www.saucedemo.com/"
    USER_NAME = "standard_user"
    PASS_WORD = "secret_sauce"
    WRONG_PASSWORD = "wrong_password"
    ERROR_MESSAGE = "Username and password do not match any user in this service"

    def __init__(self, page):
        self.should_login = None
        self.page = page
        self.username_tab = page.locator("#user-name")
        self.password_tab = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator('h3[data-test="error"]')

    def navigate_to_login_page(self):
        self.page.goto(self.URL)

    def login(self, username, password ):
        self.navigate_to_login_page()
        self.username_tab.fill(username)
        self.password_tab.fill(password)
        self.login_button.click()
        inventory_page = Inventory(self.page)
        return inventory_page

    def error_message(self):
        expect(self.error).to_be_visible()
        return self.error.inner_text()
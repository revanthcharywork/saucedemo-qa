import pytest
from playwright.sync_api import Playwright, Page, Browser
from pages.login_page import LoginPage


@pytest.fixture(scope = "session")
def user_credentials(request):
     return request.param


@pytest.fixture(scope = "session")
def browser_instance(playwright: Playwright):
    browser = playwright.chromium.launch(headless = True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser_instance: Browser):
    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def logged_in_page(page : Page):
     login = LoginPage(page)
     login.login("standard_user", "secret_sauce")
     return page




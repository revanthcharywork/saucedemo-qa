from utils.test_data import VALID_USER, INVALID_USER, LOCKED_USER
from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(page):
    login = LoginPage(page)
    login.login(**VALID_USER)
    assert page.url.endswith("/inventory.html")

@pytest.mark.smoke
@pytest.mark.login
def test_invalid_login(page):
    login = LoginPage(page)
    login.login(**INVALID_USER)
    assert "Username and password do not match" in login.error_message()

@pytest.mark.smoke
@pytest.mark.login
def test_locked_login(page):
    login = LoginPage(page)
    login.login(**LOCKED_USER)
    assert "Sorry, this user has been locked out." in login.error_message()

@pytest.mark.smoke
@pytest.mark.login
def test_empty_username(page):
    login = LoginPage(page)
    login.login("","secret_sauce")
    assert "Username is required" in login.error_message()

@pytest.mark.smoke
@pytest.mark.login
def test_empty_password(page):
    login = LoginPage(page)
    login.login("standard_user","")
    assert "Password is required" in login.error_message()



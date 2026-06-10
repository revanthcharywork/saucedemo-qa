import pytest
from pages.inventory_page import Inventory
from tests.test_cart import ITEM_NUMBERS
from utils.test_data import CHECKOUT_INFO

@pytest.mark.smoke
@pytest.mark.checkout
def test_complete_checkout_flow(logged_in_page):
    inv = Inventory(logged_in_page)
    inv.add_item_to_cart(ITEM_NUMBERS)
    cart = inv.go_to_cart()
    checkout = cart.click_checkout()
    checkout.enter_details(**CHECKOUT_INFO)
    overview = checkout.click_continue()
    overview.click_finsh()
    assert overview.is_order_placed(), "Order did not complete successfully"

@pytest.mark.checkout
def test_missing_first_name(logged_in_page):
    inv = Inventory(logged_in_page)
    inv.add_item_to_cart(ITEM_NUMBERS)
    cart = inv.go_to_cart()
    checkout = cart.click_checkout()
    checkout.enter_details("", "lastname", "50000")
    overview = checkout.click_continue()
    assert "First Name is required" in checkout.read_error_message()

@pytest.mark.checkout
def test_missing_postal_code(logged_in_page):
    inv = Inventory(logged_in_page)
    inv.add_item_to_cart(ITEM_NUMBERS)
    cart = inv.go_to_cart()
    checkout = cart.click_checkout()
    checkout.enter_details("firstname", "lastname", "")
    checkout.click_continue()
    assert "Postal Code is required" in checkout.read_error_message()
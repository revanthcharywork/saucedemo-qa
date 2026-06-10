import pytest
from pages.inventory_page import Inventory
from pages.cart_page import Cart_page

ITEM_NUMBERS = [0,1,2]
@pytest.mark.smoke
@pytest.mark.cart
def test_add_item_to_cart(logged_in_page):
    inv = Inventory(logged_in_page)
    inv.add_item_to_cart(ITEM_NUMBERS)
    items_added = inv.check_cart_loaded()
    assert int(items_added) == len(ITEM_NUMBERS)

@pytest.mark.cart
def test_cart_item_count(logged_in_page):
    inv = Inventory(logged_in_page)
    inv.add_item_to_cart(ITEM_NUMBERS)
    inv.go_to_cart()
    cart_count = Cart_page(logged_in_page).get_item_count()
    assert cart_count == len(ITEM_NUMBERS)

@pytest.mark.smoke
@pytest.mark.cart
def test_remove_item_from_cart(logged_in_page):
    inv = Inventory(logged_in_page)
    inv.add_item_to_cart(ITEM_NUMBERS)
    cart = inv.go_to_cart()
    cart.remove_items_in_cart()
    assert cart.get_item_count() == 0



from pages.inventory_page import Inventory
import pytest

@pytest.mark.smoke
@pytest.mark.inventory
def test_inventory_page_loads(logged_in_page):
    inv = Inventory(logged_in_page)
    assert inv.is_page_loaded(), "Inventory page failed to load"

@pytest.mark.inventory
def test_inventory_item_count(logged_in_page):
    inv = Inventory(logged_in_page)
    assert inv.items_count() is 6 , f"Inventory items count expected to be 6, But got {inv.items_count()}"

@pytest.mark.inventory
def  test_sort_products_low_to_high(logged_in_page):
    inv = Inventory(logged_in_page)
    inv.sort_items("lohi")
    items_data = inv.get_item_details()
    prices = []
    for item in items_data:
        prices.append(item[1])
    assert prices == sorted(prices), "Prices not sorted low to high"

@pytest.mark.inventory
def test_sort_products_a_to_z(logged_in_page):
    inv = Inventory(logged_in_page)
    inv.sort_items("az")
    items_data = inv.get_item_details()
    product_names = []
    for item in items_data:
        product_names.append(item[0])
    assert product_names == sorted(product_names), "Product names not sorted low to high"


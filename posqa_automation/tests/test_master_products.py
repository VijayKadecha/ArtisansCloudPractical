import pytest
from pages.master_products_page import MasterProductsPage


def test_create_master_product(driver, test_data):
    data = test_data["master_product"]["create"]
    page = MasterProductsPage(driver)
    page.open_page()
    page.click_add_new()
    page.fill_create_form(data["name"], data["code"])
    page.save()
    page.open_page()
    page.search(data["name"])
    assert page.is_row_present(row=1), "Newly created master product not found in list"
    assert page.get_row_name(row=1) == data["name"]


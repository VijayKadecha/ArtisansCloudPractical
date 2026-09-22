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


def test_update_master_product(driver, test_data):
    data = test_data["master_product"]
    page = MasterProductsPage(driver)
    page.open_page()
    page.search(data["create"]["name"])
    assert page.is_row_present(row=1), "Product to update not found"
    page.open_row_edit(row=1)
    page.fill_create_form(data["update_name"], data["create"]["code"])
    page.save()
    page.open_page()
    page.search(data["update_name"])
    assert page.is_row_present(row=1)
    assert page.get_row_name(row=1) == data["update_name"]


def test_delete_master_product(driver, test_data):
    data = test_data["master_product"]
    page = MasterProductsPage(driver)
    page.open_page()
    page.search(data["update_name"])
    assert page.is_row_present(row=1), "Product to delete not found"
    page.delete_row(row=1)
    page.open_page()
    page.search(data["update_name"])
    assert not page.is_row_present(row=1), "Product still present after delete"


def test_read_master_products_list(driver):
    page = MasterProductsPage(driver)
    page.open_page()
    assert page.is_row_present(row=1), "Master products list is empty"

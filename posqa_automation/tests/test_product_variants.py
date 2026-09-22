from pages.product_variants_page import ProductVariantsPage


def test_read_product_variants_list(driver):
    page = ProductVariantsPage(driver)
    page.open_page()
    assert page.is_row_present(row=1), "Product variants list is empty"


def test_search_existing_variant(driver, test_data):
    variant_id = test_data["product_variant"]["search_existing"]
    page = ProductVariantsPage(driver)
    page.open_page()
    page.search(variant_id)
    assert page.is_row_present(row=1), f"Variant {variant_id} not found via search"

def test_open_variant_edit(driver, test_data):
    variant_id = test_data["product_variant"]["search_existing"]
    page = ProductVariantsPage(driver)
    page.open_page()
    page.search(variant_id)
    page.open_row_edit(row=1)
    assert "/edit" in driver.current_url

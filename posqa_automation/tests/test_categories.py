from pages.categories_page import CategoriesPage


def test_create_category(driver, test_data):
    name = test_data["category"]["create_name"]
    page = CategoriesPage(driver)
    page.open_page()
    page.click_add_new_category()
    page.fill_create_form(name)
    page.save()
    page.open_page()
    assert page.is_category_present(name), "Newly created category not found"


def test_read_categories_list(driver, test_data):
    name = test_data["category"]["create_name"]
    page = CategoriesPage(driver)
    page.open_page()
    assert page.is_category_present(name)


def test_update_category(driver, test_data):
    old_name = test_data["category"]["create_name"]
    new_name = test_data["category"]["update_name"]
    page = CategoriesPage(driver)
    page.open_page()
    assert page.is_category_present(old_name), "Category to update not found"
    page.open_edit_by_name(old_name)
    page.fill_create_form(new_name)
    page.save()
    page.open_page()
    assert page.is_category_present(new_name)


def test_delete_category(driver, test_data):
    name = test_data["category"]["update_name"]
    page = CategoriesPage(driver)
    page.open_page()
    assert page.is_category_present(name), "Category to delete not found"
    page.delete_category_by_name(name)
    page.open_page()
    assert not page.is_category_present(name), "Category still present after delete"

from .base_page import BasePage

URL = "https://posqa.artisanscloud.com.my/admin/categories"


class CategoriesPage(BasePage):
    ADD_NEW_CATEGORY_BTN = "//a[@href='https://posqa.artisanscloud.com.my/admin/categories/create']"
    SEARCH_INPUT = "//input[@placeholder='Search categories...']"

    # Category "card" located by its visible name text, used as an anchor to
    # find that row's action icons relative to it (name text is stable;
    # button indices under it are not).
    CATEGORY_CARD_BY_NAME = "//div[normalize-space(text())='{name}']/ancestor::div[contains(concat(' ', normalize-space(@class), ' '), ' grid ')][1]//div[normalize-space(text())='{name}']/.."
    CATEGORY_ROW_BY_NAME = "(//div[normalize-space(text())='{name}'])[1]/ancestor::div[3]"
    EDIT_ICON_IN_ROW_BY_NAME = CATEGORY_ROW_BY_NAME + "//a[contains(@href,'/edit')]"
    ADD_SUB_ICON_IN_ROW_BY_NAME = CATEGORY_ROW_BY_NAME + "//a[contains(@href,'/categories/create/')]"
    DELETE_ICON_IN_ROW_BY_NAME = CATEGORY_ROW_BY_NAME + "//div[1]/div[2]/button[2]"
    # not captured in the exported JSON. Fill in once exported from that page.
    FORM_NAME_INPUT = "//input[@name='name']"
    FORM_SAVE_BTN = "//button[@type='submit' or contains(text(),'Save')]"
    DELETE_CONFIRM_BTN = "//button[contains(text(),'Confirm') or contains(text(),'Yes') or contains(text(),'Delete')]"

    def open_page(self):
        self.open(URL)

    def click_add_new_category(self):
        self.click(self.ADD_NEW_CATEGORY_BTN)

    def fill_create_form(self, name):
        self.type_text(self.FORM_NAME_INPUT, name)

    def save(self):
        self.click(self.FORM_SAVE_BTN)

    def search(self, term):
        self.type_text(self.SEARCH_INPUT, term)

    def is_category_present(self, name):
        return self.is_present(f"//div[normalize-space(text())='{name}']")

    def open_edit_by_name(self, name):
        self.click(self.EDIT_ICON_IN_ROW_BY_NAME.format(name=name))

    def delete_category_by_name(self, name):
        self.click(self.DELETE_ICON_IN_ROW_BY_NAME.format(name=name))
        self.click(self.DELETE_CONFIRM_BTN)

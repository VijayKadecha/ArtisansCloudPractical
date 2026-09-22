from .base_page import BasePage

URL = "https://posqa.artisanscloud.com.my/admin/master-products"


class MasterProductsPage(BasePage):
    ADD_NEW_BTN = "//div[contains(concat(' ', normalize-space(@class), ' '), ' page-list-header__actions ')]/div[1]/a[1]/button[1]"
    SEARCH_INPUT = "//input[@placeholder='Search…']"
    ROW_BY_INDEX_EDIT_LINK = "//table[contains(@class,'jtable')]/tbody/tr[{row}]//a[contains(@href,'/edit')]"
    ROW_BY_INDEX_NAME_CELL = "//table[contains(@class,'jtable')]/tbody/tr[{row}]/td[4]"
    ROW_BY_INDEX_CHECKBOX = "//table[contains(@class,'jtable')]/tbody/tr[{row}]/td[1]//input"
    # id pattern is stable ('headlessui-menu-button' prefix), the trailing number changes per render
    ROW_BY_INDEX_ACTIONS_MENU = "//table[contains(@class,'jtable')]/tbody/tr[{row}]//a[contains(@id,'headlessui-menu-button')]"
    NO_RESULTS_ROW = "//table[contains(@class,'jtable')]/tbody/tr[1]/td[contains(text(),'No') or contains(text(),'no data')]"

    # (Name, Code, Brand, Category dropdowns, Save button) live on
    # /admin/master-products/create and /master-products/{id}/edit and were not
    # exported. Fill these in from that page's own xpath export.
    FORM_NAME_INPUT = "//input[@name='name']"
    FORM_CODE_INPUT = "//input[@name='code']"
    FORM_SAVE_BTN = "//button[@type='submit' or contains(text(),'Save')]"
    DELETE_MENU_ITEM = "//a[contains(text(),'Delete')] | //button[contains(text(),'Delete')]"
    DELETE_CONFIRM_BTN = "//button[contains(text(),'Confirm') or contains(text(),'Yes') or contains(text(),'Delete')]"
    TOAST_SUCCESS = "//div[contains(@class,'toast') or contains(@class,'notification')]"

    def open_page(self):
        self.open(URL)

    def click_add_new(self):
        self.click(self.ADD_NEW_BTN)

    def fill_create_form(self, name, code):
        self.type_text(self.FORM_NAME_INPUT, name)
        self.type_text(self.FORM_CODE_INPUT, code)

    def save(self):
        self.click(self.FORM_SAVE_BTN)

    def search(self, term):
        self.type_text(self.SEARCH_INPUT, term)
        self.driver.find_element("xpath", self.SEARCH_INPUT).send_keys("\n")

    def is_row_present(self, row=1, timeout=10):
        return self.is_present(self.ROW_BY_INDEX_NAME_CELL.format(row=row))

    def get_row_name(self, row=1):
        return self.get_text(self.ROW_BY_INDEX_NAME_CELL.format(row=row))

    def open_row_edit(self, row=1):
        self.click(self.ROW_BY_INDEX_EDIT_LINK.format(row=row))

    def open_row_actions_menu(self, row=1):
        self.click(self.ROW_BY_INDEX_ACTIONS_MENU.format(row=row))

    def delete_row(self, row=1):
        self.open_row_actions_menu(row)
        self.click(self.DELETE_MENU_ITEM)
        self.click(self.DELETE_CONFIRM_BTN)

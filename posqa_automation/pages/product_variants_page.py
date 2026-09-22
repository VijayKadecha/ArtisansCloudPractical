from .base_page import BasePage

URL = "https://posqa.artisanscloud.com.my/admin/product-variants"


class ProductVariantsPage(BasePage):
    SEARCH_INPUT = "//input[@placeholder='Search…']"
    ROW_BY_INDEX_EDIT_LINK = "//table[contains(@class,'jtable')]/tbody/tr[{row}]//a[contains(@href,'/edit')]"
    ROW_BY_INDEX_CHECKBOX = "//table[contains(@class,'jtable')]/tbody/tr[{row}]/td[1]//input"
    ROW_BY_INDEX_ACTIONS_MENU = "//table[contains(@class,'jtable')]/tbody/tr[{row}]//a[contains(@id,'headlessui-menu-button')]"

    # (variants are usually created from within a Master Product's edit page).
    # Verify: it may be a button inside the Master Product edit form instead of
    # here. Update ADD_NEW_BTN once confirmed.
    ADD_NEW_BTN = "//button[contains(text(),'Add') and contains(text(),'Variant')]"

    FORM_VARIANT_NAME_INPUT = "//input[@name='variant_name']"
    FORM_SAVE_BTN = "//button[@type='submit' or contains(text(),'Save')]"
    DELETE_MENU_ITEM = "//a[contains(text(),'Delete')] | //button[contains(text(),'Delete')]"
    DELETE_CONFIRM_BTN = "//button[contains(text(),'Confirm') or contains(text(),'Yes') or contains(text(),'Delete')]"

    def open_page(self):
        self.open(URL)

    def search(self, term):
        self.type_text(self.SEARCH_INPUT, term)
        self.driver.find_element("xpath", self.SEARCH_INPUT).send_keys("\n")

    def is_row_present(self, row=1):
        return self.is_present(self.ROW_BY_INDEX_EDIT_LINK.format(row=row))

    def open_row_edit(self, row=1):
        self.click(self.ROW_BY_INDEX_EDIT_LINK.format(row=row))

    def open_row_actions_menu(self, row=1):
        self.click(self.ROW_BY_INDEX_ACTIONS_MENU.format(row=row))

    def delete_row(self, row=1):
        self.open_row_actions_menu(row)
        self.click(self.DELETE_MENU_ITEM)
        self.click(self.DELETE_CONFIRM_BTN)

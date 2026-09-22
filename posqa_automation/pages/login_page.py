from .base_page import BasePage

LOGIN_URL = "https://posqa.artisanscloud.com.my/admin"


class LoginPage(BasePage):
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//div[contains(concat(\" \", normalize-space(@class), \" \"), ' xl:mt-8 ')]/button[1]"
    NOTIFICATION_CLOSE_BTN = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]"
    INVENTORY_MENU_LINK = "//a[contains(@href,'/admin/menu/Inventory')]"
    MASTER_PRODUCTS_MENU_LINK = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/ul[1]/span[1]/li[1]/a[1]/div[2]"

    def login(self, username, password):
        self.open(LOGIN_URL)
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_url_contains("/admin")

    def close_notification_popup_if_present(self, timeout=5):
        if self.is_present(self.NOTIFICATION_CLOSE_BTN, timeout=timeout):
            self.click(self.NOTIFICATION_CLOSE_BTN)

    def navigate_to_master_products_via_menu(self):
        """Clicks through Inventory -> Master Products with proper synchronization."""
        # 1. Wait until the Inventory menu drawer is genuinely clickable, then click it
        inventory_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.INVENTORY_MENU_LINK))
        )
        inventory_element.click()

        # 2. Wait until the sub-menu link is visible and clickable in the expanded drawer
        master_product_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MASTER_PRODUCTS_MENU_LINK))
        )
        master_product_element.click()
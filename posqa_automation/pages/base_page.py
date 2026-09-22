from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)

    def click(self, xpath):
        el = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        el.click()

    def type_text(self, xpath, text):
        el = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        el.clear()
        el.send_keys(text)

    def get_text(self, xpath):
        el = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return el.text

    def is_visible(self, xpath, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except Exception:
            return False

    def is_present(self, xpath, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except Exception:
            return False

    def wait_for_url_contains(self, fragment, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(fragment))

    def accept_alert_if_present(self):
        try:
            self.driver.switch_to.alert.accept()
        except Exception:
            pass

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

USERNAME = "azentio"
PASSWORD = "Artisans@123"

# Locator for something ONLY visible after logging in (e.g., Logout button, User avatar)
DASHBOARD_HEADER = (By.XPATH, "//h1[contains(text(),'Dashboard')]")


def test_valid_login(raw_driver):
    login_page = LoginPage(raw_driver)
    login_page.login(USERNAME, PASSWORD)

    # 1. Be stricter with the URL to ensure it didn't bounce to an error sub-path
    WebDriverWait(raw_driver, 10).until(
        EC.url_contains("/admin")
    )

    assert login_page.is_present(login_page.INVENTORY_MENU_LINK, timeout=10), \
        "Inventory menu link not found after login — login likely failed"
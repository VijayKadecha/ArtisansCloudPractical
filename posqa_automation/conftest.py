import json
import os
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver
from pages.login_page import LoginPage

USERNAME = "azentio"
PASSWORD = "Artisans@123"
DATA_PATH = os.path.join(os.path.dirname(__file__), "testdata", "test_data.json")


@pytest.fixture
def test_data():
    with open(DATA_PATH, "r") as f:
        return json.load(f)


@pytest.fixture
def driver():
    drv = get_driver()

    # 1. Perform login
    LoginPage(drv).login(USERNAME, PASSWORD)


    # 2. CRITICAL: Wait for the dashboard/admin URL to load completely
    # before letting the master product tests execute.
    WebDriverWait(drv, 10).until(
        EC.url_contains("/admin")
    )

    LoginPage(drv).navigate_to_master_products_via_menu()

    yield drv
    drv.quit()


@pytest.fixture
def raw_driver():
    """Browser only, no login performed — use for testing login itself."""
    drv = get_driver()
    yield drv
    drv.quit()

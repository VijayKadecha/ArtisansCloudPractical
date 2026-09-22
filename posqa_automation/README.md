# POSQA Inventory Automation (Selenium + Python + pytest)

## Setup (PyCharm)
1. Open this folder as a PyCharm project.
2. Create a venv, then:
   ```
   pip install -r requirements.txt
   ```
3. Run all tests:
   ```
   pytest -v
   ```
   Run one module:
   ```
   pytest tests/test_master_products.py -v
   ```

## What's wired up (real xpaths from your exported JSON)
- Login → Inventory nav
- Master Products: Add button, search, per-row Edit link, per-row action-menu trigger, pagination
- Categories: Add New Category, search, per-row Edit link, add-subcategory link
- Product Variants: search, per-row Edit link, per-row action-menu trigger, pagination

## TODO before first run (locators not present in the exported listing-page JSON)
These pages weren't in your export, so placeholders are marked `TODO` in the page objects:
1. **Login page** (`pages/login_page.py`) — username/password inputs, login button.
2. **Master Product create/edit form** (`pages/master_products_page.py`) — Name/Code inputs, Save button, Delete confirm modal button.
3. **Category create/edit form** (`pages/categories_page.py`) — Name input, Save button. Also verify `DELETE_ICON_IN_ROW_BY_NAME` button index (2nd vs 3rd icon depends on whether a chevron/expand icon is present).
4. **Product Variant create/edit form + "Add Variant" entry point** (`pages/product_variants_page.py`) — likely lives inside a Master Product's edit screen, not its own listing page.

To fix: open each form page in the browser, export its xpaths the same way you did for the listing pages, and send them over — I'll drop them straight into the matching `TODO` lines.

## Notes
- Dynamic `headlessui-menu-button-v-NN` ids: the trailing number changes per page render, so locators use `contains(@id,'headlessui-menu-button')` instead of the exact id — this keeps tests stable across runs.
- `driver` fixture (in `conftest.py`) logs in fresh before every test and quits the browser after.
- Chrome runs visibly by default; uncomment the `--headless=new` line in `utils/driver_factory.py` for CI.

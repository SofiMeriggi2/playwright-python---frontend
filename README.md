# Playwright + Python — Frontend Automation

Functional test automation project for [SauceDemo](https://www.saucedemo.com) using Playwright with Python, Page Object Model (POM) pattern, and HTML reporting.

## Tech Stack

- **Python 3.11**
- **Playwright** — browser automation
- **pytest** — testing framework
- **pytest-html** — HTML reporting
- **GitHub Actions** — CI/CD

---

## Project Structure

```
pw+python_fe/
├── pages/
│   ├── base_page.py        # Shared methods inherited by all Page Objects
│   ├── login_page.py       # Login screen Page Object
│   ├── inventory_page.py   # Product listing Page Object
│   ├── cart_page.py        # Shopping cart Page Object
│   └── checkout_page.py    # Checkout flow Page Object
├── data/
│   ├── users.py            # Test user credentials
│   └── messages.py         # Expected error messages
├── tests/
│   ├── test_login.py       # TC-01 to TC-04
│   ├── test_inventory.py   # TC-05 to TC-08
│   ├── test_cart.py        # TC-09 to TC-10
│   └── test_checkout.py    # TC-11 to TC-14
├── .github/
│   └── workflows/
│       └── tests.yml       # CI/CD pipeline
├── conftest.py             # Playwright fixtures (browser, context, page)
├── pytest.ini              # pytest config and custom markers
└── requirements.txt        # Project dependencies
```

---

## Test Cases

| ID | Module | Description | Marker |
|---|---|---|---|
| TC-01 | Login | Successful login with standard user | `smoke` |
| TC-02 | Login | Blocked user sees error message | `smoke` `negative` |
| TC-03 | Login | Invalid credentials show error message | `negative` |
| TC-04 | Login | Empty fields show validation error | `negative` |
| TC-05 | Inventory | Exactly 6 products are listed | `smoke` |
| TC-06 | Inventory | Sort products by price low to high | |
| TC-07 | Inventory | Adding product to cart shows badge | `smoke` |
| TC-08 | Inventory | Cart badge reflects correct item count | |
| TC-09 | Cart | Added product appears in cart | `smoke` |
| TC-10 | Cart | Removing product leaves cart empty | |
| TC-11 | Checkout | Full end-to-end purchase flow | `smoke` |
| TC-11b | Checkout | Back Home button redirects to inventory | |
| TC-12 | Checkout | Error when First Name is empty | `negative` |
| TC-13 | Checkout | Error when Last Name is empty | `negative` |
| TC-14 | Checkout | Error when Postal Code is empty | `negative` |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/SofiMeriggi2/playwright-python---frontend.git
cd playwright-python---frontend

# Create virtual environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
playwright install chromium
```

---

## Running Tests

```bash
# All tests
pytest -v

# Smoke tests only (critical path)
pytest -m smoke -v

# Negative tests only
pytest -m negative -v

# Single module
pytest tests/test_login.py -v
```

The HTML report is automatically generated at `reports/report.html` after each run.

---

## CI/CD

The pipeline runs automatically on every push to `main`. You can check the execution history in the [Actions](https://github.com/SofiMeriggi2/playwright-python---frontend/actions) tab.

In CI the browser runs in headless mode. Locally it runs with a visible UI and `slow_mo=500ms` for easier debugging.

---

## Part of an Automation Portfolio

This is the first of five automation projects:

| # | Stack | Type |
|---|---|---|
| 1 | Playwright + Python | Frontend ← this one |
| 2 | Playwright + Python | API/Backend |
| 3 | Playwright + TypeScript | Frontend |
| 4 | Playwright + TypeScript | API/Backend |
| 5 | Selenium | Mobile |
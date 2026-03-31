import os
import pytest
from playwright.sync_api import Page
from data.users import Users


@pytest.fixture(scope="session")
def browser(playwright):
    headless = os.getenv("CI", "false") == "true"
    browser = playwright.chromium.launch(headless=headless, slow_mo=0 if headless else 500)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context, request) -> Page:
    page = context.new_page()

    def fin():
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            os.makedirs("reports/screenshots", exist_ok=True)
            safe_name = request.node.nodeid.replace("/", "_").replace("::", "_")
            page.screenshot(path=f"reports/screenshots/{safe_name}.png", full_page=True)
        page.close()

    request.addfinalizer(fin)
    return page


@pytest.fixture(params=["STANDARD", "LOCKED", "PROBLEM"])
def user(request) -> dict:
    return {"username": getattr(Users, request.param), "password": Users.PASSWORD}


@pytest.fixture
def logged_in_page(page) -> Page:
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", Users.STANDARD)
    page.fill("#password", Users.PASSWORD)
    page.click("#login-button")
    page.wait_for_url("**/inventory.html", timeout=5000)
    return page
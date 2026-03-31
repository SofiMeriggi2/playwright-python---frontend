# pages/checkout_page.py
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # Locators — step 1 (formulario)
    FIRST_NAME    = "[data-test='firstName']"
    LAST_NAME     = "[data-test='lastName']"
    POSTAL_CODE   = "[data-test='postalCode']"
    CONTINUE_BTN  = "[data-test='continue']"
    ERROR_MESSAGE = "[data-test='error']"

    # Locators — step 2 (resumen)
    FINISH_BTN    = "[data-test='finish']"
    SUMMARY_ITEMS = ".cart_item"

    # Locators — step 3 (confirmación)
    CONFIRM_HEADER = ".complete-header"
    BACK_HOME_BTN  = "[data-test='back-to-products']"

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.page.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self.page.click(self.FINISH_BTN)
        self.page.wait_for_url("**/checkout-complete.html", timeout=5000)

    def back_to_home(self):
        self.page.click(self.BACK_HOME_BTN)
        self.page.wait_for_url("**/inventory.html", timeout=5000)

    def get_confirm_header(self) -> str:
        return self.get_text(self.CONFIRM_HEADER)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def get_summary_item_count(self) -> int:
        return self.page.locator(self.SUMMARY_ITEMS).count()
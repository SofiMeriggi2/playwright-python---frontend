from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    # Locators
    CART_ITEMS       = ".cart_item"
    ITEM_NAMES       = ".inventory_item_name"
    REMOVE_BTN       = "button[id^='remove']"
    CHECKOUT_BTN     = "[data-test='checkout']"
    CONTINUE_BTN     = "[data-test='continue-shopping']"

    def navigate(self):
        self.page.goto(self.URL)

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def get_item_names(self) -> list[str]:
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def remove_first_item(self):
        self.page.locator(self.REMOVE_BTN).first.click()

    def go_to_checkout(self):
        self.page.click(self.CHECKOUT_BTN)
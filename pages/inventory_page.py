from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    PRODUCT_ITEMS    = ".inventory_item"
    PRODUCT_NAMES    = ".inventory_item_name"
    SORT_DROPDOWN    = "[data-test='product-sort-container']"
    ADD_TO_CART_BTN  = "button[id^='add-to-cart']"
    CART_BADGE       = ".shopping_cart_badge"

    def get_product_count(self) -> int:
        return self.page.locator(self.PRODUCT_ITEMS).count()

    def get_product_names(self) -> list[str]:
        return self.page.locator(self.PRODUCT_NAMES).all_inner_texts()

    def sort_by(self, option: str):
        """Opciones: 'az', 'za', 'lohi', 'hilo'"""
        self.page.select_option(self.SORT_DROPDOWN, option)

    def add_first_product_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    def get_cart_badge_count(self) -> int:
        return int(self.page.locator(self.CART_BADGE).inner_text())

    def cart_badge_is_visible(self) -> bool:
        return self.page.locator(self.CART_BADGE).is_visible()
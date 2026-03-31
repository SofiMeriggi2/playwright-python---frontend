# pages/base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        return self.page.title()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()
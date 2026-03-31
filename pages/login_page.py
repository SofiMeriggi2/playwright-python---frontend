# pages/login_page.py
from pages.base_page import BasePage
from data.users import Users


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON   = "#login-button"
    ERROR_MESSAGE  = "[data-test='error']"

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def login_as_standard(self):
        self.login(Users.STANDARD, Users.PASSWORD)

    def login_as_locked(self):
        self.login(Users.LOCKED, Users.PASSWORD)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

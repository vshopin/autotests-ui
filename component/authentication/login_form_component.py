from playwright.sync_api import Page

from component.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_input = Input(page, 'login-form-email-input', 'Login')
        self.password_input = Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password: str) -> None:
        self.login_input.fill(email)

        self.password_input.fill(password)

    def check_visible(self, email: str, password: str) -> None:
        self.login_input.check_visible()
        self.login_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)

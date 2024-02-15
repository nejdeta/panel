from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOG_IN_BTN = (By.ID, "login-button")

    def fill_email_input(self, email):
        """
     it sends text on the email input
        """

        self.send_text(email, *self.EMAIL_INPUT)

    def fill_password_input(self, password):
        """
     it sends text on the password input
        """

        self.send_text(password, *self.PASSWORD_INPUT)

    def click_login_btn(self):
        """
     it clicks the sign in button
        """

        self.click_element(*self.LOG_IN_BTN)

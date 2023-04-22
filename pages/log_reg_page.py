from .base_page import BasePage
from .locators import LogRegLocators
from .data_for_registration import ValidDataForRegistration

class LoginPage(BasePage):
    
    # регистрация нового пользователя
    def register_new_user(self):
        self.go_to_reg_page()
        first_name = self.browser.find_element(*LogRegLocators.REG_USER_FIRST_NAME)
        first_name.send_keys(ValidDataForRegistration.FIRST_NAME)
        last_name = self.browser.find_element(*LogRegLocators.REG_USER_LAST_NAME)
        last_name.send_keys(ValidDataForRegistration.LAST_NAME)
        user_name = self.browser.find_element(*LogRegLocators.REG_USER_NAME)
        user_name.send_keys(ValidDataForRegistration.USER_NAME)
        user_email = self.browser.find_element(*LogRegLocators.REG_USER_EMAIL)
        user_email.send_keys(ValidDataForRegistration.EMAIL)
        user_password = self.browser.find_element(*LogRegLocators.REG_USER_PASSWORD)
        user_password.send_keys(ValidDataForRegistration.PASSWORD)
        registration_button = self.browser.find_element(*LogRegLocators.REGISTRATION_BUTTON)
        registration_button.click()

    # вход для зарегистрированного пользователя
    def login_user(self):
        self.go_to_login_page()
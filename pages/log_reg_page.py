from .base_page import BasePage
from .locators import Log_Reg_Locators

class LoginPage(BasePage):
    
    def register_new_user(self, fake_email, fake_password):
        pass

    def login_user(self):
        self.go_to_login_page()
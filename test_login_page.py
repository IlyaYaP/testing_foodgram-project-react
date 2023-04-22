from pages.log_reg_page import LoginPage
from pages.links import main_page_link
import time

class TestRegistrationForm():
    def test_open_page(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user()
        time.sleep(5)

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import LogRegLocators

class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    # функция открытия страницы в браузере
    def open(self):
        self.browser.get(self.url)

    # переход к форме входа
    def go_to_login_page(self):
        link = self.browser.find_element(*LogRegLocators.LOGIN_LINK)
        link.click()
    
    # переход к форме регистрации
    def go_to_reg_page(self):
        link = self.browser.find_element(*LogRegLocators.REGISTRATION_LINK)
        link.click()


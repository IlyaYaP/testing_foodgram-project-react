from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import Log_Reg_Locators

class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    # функция открытия страницы
    def open(self):
        self.browser.get(self.url)

    # переход к форме входа
    def go_to_login_page(self):
        link = self.browser.find_element(*Log_Reg_Locators.LOGIN_LINK)
        link.click()


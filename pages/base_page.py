from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import LogRegLocators

class BasePage():
    def __init__(self, browser, url, timeout = 5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        '''функция осуществляет переход по указанному пути'''
        self.browser.get(self.url)


    def go_to_login_page(self):
        '''функция осуществляет переход на страницу входа'''
        link = self.browser.find_element(*LogRegLocators.LOGIN_LINK)
        link.click()
    

    def go_to_registration_page(self):
        '''функция осуществляет переход на страницу регистрации'''
        link = self.browser.find_element(*LogRegLocators.REGISTRATION_LINK)
        link.click()


    def is_element_present(self, how, what):
        '''проверка наличия элемента на странице'''
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
    

    def is_not_element_present(self, how, what):
        '''проверка проверка отсутствия элемента на странице'''
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return True
        return False


    def is_not_alert_present(self, timeout=2):
        '''проверка наличия элемента(алерта) на странице, упадет если алерт появится'''
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present(), 'Timed out waiting')
        except TimeoutException:
            return True
        return False
    
    def is_alert_present(self, timeout=2):
        '''проверка наличия элемента(алерта) на странице, если есть алерт то тест пройдет'''
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present(), 'Timed out waiting')
            self.browser.switch_to.alert.accept()
        except TimeoutException:
            return False
        return True


    def alert_handler(self):
        '''функция передает текст алерта в сообщение об ошибке'''
        assert self.is_not_alert_present(), f'{self.browser.switch_to.alert.text}'


       




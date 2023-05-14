import os
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, UnexpectedAlertPresentException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import LogRegLocators, CreateRecipeLocators, HeaderMenuButtons


class BasePage():
    def __init__(self, browser, url, timeout = 5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        '''функция осуществляет переход по указанному пути'''
        self.browser.get(self.url)

    def go_to_recipes_page(self):
        self.browser.get('http://localhost/recipes')

    def go_to_recipes_page_menu(self):
        # WebDriverWait(self.browser, timeout=5).until(EC.element_to_be_clickable((HeaderMenuButtons.RECIPES))).click()
        link = self.browser.find_element(*HeaderMenuButtons.RECIPES)
        link.click()



    def go_to_favorites_page(self):
        link = self.browser.find_element(*HeaderMenuButtons.FAVORITES)
        link.click()

    def go_to_recipes_creat_page(self):
        link = self.browser.find_element(*HeaderMenuButtons.RECIPES_CREATE)
        link.click()

    def go_to_subscriptions_page(self):
        link = self.browser.find_element(*HeaderMenuButtons.SUBSCRIPTIONS)
        link.click()

    def go_to_shopping_list_page(self):
        link = self.browser.find_element(*HeaderMenuButtons.SHOPPING_LIST)
        link.click()

    def go_to_change_password_page(self):
        link = self.browser.find_element(*HeaderMenuButtons.CHANGE_PASSWORD)
        link.click()

    def go_to_exit(self):
        link = self.browser.find_element(*HeaderMenuButtons.EXIT)
        link.click()

    def go_to_login_page(self):
        '''Функция осуществляет переход на страницу входа'''
        link = self.browser.find_element(*LogRegLocators.LOGIN_LINK)
        link.click()
    
    def go_to_registration_page(self):
        '''Функция осуществляет переход на страницу регистрации'''
        link = self.browser.find_element(*LogRegLocators.REGISTRATION_LINK)
        link.click()

    def is_element_present(self, how, what):
        '''Проверка наличия элемента на странице'''
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
    
    def is_not_element_present(self, how, what):
        '''Проверка отсутствия элемента на странице'''
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return True
        return False

    def is_not_alert_present(self, timeout=1):
        '''Проверка отсутствия элемента(алерта) на странице, упадет если алерт появится'''
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present(), 'Timed out waiting')
        except TimeoutException:
            return True
        return False
    
    def is_alert_present(self, timeout=1):
        '''Проверка наличия элемента(алерта) на странице, если есть алерт то тест пройдет'''
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present(), 'Timed out waiting')
            self.browser.switch_to.alert.accept()
        except TimeoutException:
            return False
        return True

    def alert_handler(self):
        '''Функция передает текст алерта в сообщение об ошибке'''
        assert self.is_not_alert_present(), f'{self.browser.switch_to.alert.text}'

    def add_image(self, image_name, element):
        directory = 'C:/dev/testing_foodgram-project-react/pages/recipe_image/'
        file_path = os.path.join(directory, image_name)
        element.send_keys(file_path)



       




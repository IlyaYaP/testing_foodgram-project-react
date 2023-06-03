import os

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import HeaderMenuButtons, LogRegLocators


class BasePage():
    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        '''Функция перехода к указанному адресу.'''
        with allure.step('Открываем главную страницу'):
            self.browser.get(self.url)

    def go_to_recipes_page(self):
        '''Функция перехода к странице с рецептами'''
        with allure.step('Переходим на страницу с рецептами.'):
            self.browser.get('http://localhost/recipes')

    def go_to_recipes_page_menu(self):
        '''Функция перехода к странице с рецептами из меню в хедаре'''
        with allure.step('Переходим на страницу с рецептами,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(*HeaderMenuButtons.RECIPES)
            link.click()

    def go_to_favorites_page(self):
        '''Функция перехода к странице с избронным из меню в хедаре'''
        with allure.step('Переходим на страницу с избранными рецептами,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(*HeaderMenuButtons.FAVORITES)
            link.click()

    def go_to_recipes_creat_page(self):
        '''Функция перехода к странице создания рецепта из меню в хедаре'''
        with allure.step('Переходим на страницу создания рецепта,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(*HeaderMenuButtons.RECIPES_CREATE)
            link.click()

    def go_to_subscriptions_page(self):
        '''Функция перехода к странице с подписками из меню в хедаре'''
        with allure.step('Переходим на страницу с подписками,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(*HeaderMenuButtons.SUBSCRIPTIONS)
            link.click()

    def go_to_shopping_list_page(self):
        '''Функция перехода к странице списка покупок из меню в хедаре'''
        with allure.step('Переходим на страницу со списком покупок,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(*HeaderMenuButtons.SHOPPING_LIST)
            link.click()

    def go_to_change_password_page(self):
        '''Функция перехода к странице изменения пароля из меню в хедаре'''
        with allure.step('Переходим на страницу изменения пароля,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(
                   *HeaderMenuButtons.CHANGE_PASSWORD)
            link.click()

    def go_to_exit(self):
        '''Функция выхода из уч.записи из меню в хедаре'''
        with allure.step('Выходим из своей учетной записи,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(*HeaderMenuButtons.EXIT)
            link.click()

    def go_to_login_page(self):
        '''Функция осуществляет переход на страницу входа'''
        with allure.step('Переходим на страницу входа в учетную запись,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(*LogRegLocators.LOGIN_LINK)
            link.click()

    def go_to_registration_page(self):
        '''Функция осуществляет переход на страницу регистрации'''
        with allure.step('Переходим на страницу регистрации,\
                         щелкая по кнопке из меню в хедаре.'):
            link = self.browser.find_element(*LogRegLocators.REGISTRATION_LINK)
            link.click()

    def is_element_present(self, how, what):
        '''Проверка наличия элемента на странице'''
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_element_present_timeout(self, how, what):
        '''Проверка наличия элемента на странице, ожидая'''
        try:
            WebDriverWait(self.browser, timeout=1).until(
                EC.presence_of_element_located((how, what)))
            self.browser.find_element(how, what)
        except (TimeoutException):
            return False
        return True

    def is_not_element_present(self, how, what):
        '''Проверка отсутствия элемента на странице'''
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return True
        return False

    def is_not_alert_present(self, timeout=1):
        '''Проверка отсутствия элемента(алерта) на странице,\
            упадет если алерт появится'''
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present(),
                                                       'Timed out waiting')
        except TimeoutException:
            return True
        return False

    def is_alert_present(self, timeout=1):
        '''Проверка наличия элемента(алерта) на странице,\
           если есть алерт то тест пройдет'''
        with allure.step('Проверяем, что алерт с\
                         сообщением об ошибке появился.'):
            try:
                WebDriverWait(self.browser, timeout).until
                (EC.alert_is_present(), 'Timed out waiting')
                self.browser.switch_to.alert.accept()
            except TimeoutException:
                return False
            return True

    def alert_handler(self):
        '''Функция проверяет, что алерт не появился'''
        with allure.step('Проверяем, что алерт с сообщением\
                         об ошибке  не появился.'):
            assert self.is_not_alert_present(), f'{
                   self.browser.switch_to.alert.text}'

    def add_image(self, image_name, element):
        '''Функция добавления фотографии'''
        with allure.step('Добавляем фото рецепта.'):
            directory = f'C:/dev/testing_foodgram-project-react/\
                          pages/recipe_image/'
            file_path = os.path.join(directory, image_name)
            element.send_keys(file_path)

    def is_disappeared(self, how, what, timeout=2):
        '''Функция ожидает, пока элемент не исчезнет'''
        try:
            WebDriverWait(self.browser, timeout, 0.05,
                          TimeoutException).until_not(
                          EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        return True

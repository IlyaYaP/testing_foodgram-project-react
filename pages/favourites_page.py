from .base_page import BasePage
from .locators import FavouritesLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time



class FavouritesPage(BasePage):
    
    def add_favorites(self, data):
        '''Функция добавления рецептов в избранное'''
        favourites_button_locator = (By.XPATH, f'//a[text()="{data}"]//following::button[2]')
        favourites_button = self.browser.find_element(*favourites_button_locator)
        favourites_button.click()
        self.go_to_favorites_page()
        # self.should_be_favorites(data)

        # Далее реализуем проверку что на странице избранного, появились рецепты + функцию, которая почистит избранное, дабы не засорять тесты.

    def delete_favotites(self, data):
        self.go_to_favorites_page()
        favourites_button_locator = (By.XPATH, f'//a[text()="{data}"]//following::button[2]')
        favourites_button = self.browser.find_element(*favourites_button_locator)
        favourites_button.click()
        self.browser.refresh()
        # self.not_should_be_favorites(data)



    def should_be_favorites(self, data):
        '''Проверка наличия подиски'''
        favorites_name = (By.LINK_TEXT, f'{data}')
        assert self.is_element_present_timeout(*favorites_name), 'The favorites is not presented'

    def not_should_be_favorites(self, data):
        '''Проверка наличия подиски'''
        favorites_name = (By.LINK_TEXT, f'{data}')
        assert self.is_not_element_present(*favorites_name), 'The favorites is presented'
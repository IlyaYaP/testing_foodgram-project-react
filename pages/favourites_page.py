from .base_page import BasePage
from .locators import SubscriptionsLocators
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
        time.sleep(3)

        # Далее реализуем проверку что на странице избранного, появились рецепты + функцию, которая почистит избранное, дабы не засорять тесты.
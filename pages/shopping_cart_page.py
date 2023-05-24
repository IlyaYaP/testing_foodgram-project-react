from .base_page import BasePage
from .locators import ShoppingCartLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from data.data_shopping_cart import DataShoppingCart
import time


class ShoppingCart(BasePage):

    RECIPE_NAME = (By.LINK_TEXT, f'{DataShoppingCart.RECIPE_NAME}')

    def add_shopping_cart(self, data):
        '''Функция добавления рецептов в список покупок и скачивания списка'''
        add_shopping_cart_button_locator = (By.XPATH, f'//a[text()="{data}"]//following::button[1]')
        add_shopping_cart_button = self.browser.find_element(*add_shopping_cart_button_locator)
        if add_shopping_cart_button.text == 'Рецепт добавлен':
            self.go_to_shopping_list_page()
            self.should_be_recipe_in_shopping_list(data)
            download_list_button = self.browser.find_element(*ShoppingCartLocators.DOWNLOAD_LIST_BUTTON)
            download_list_button.click()
            time.sleep(1)
        else:
            add_shopping_cart_button.click()
            self.go_to_shopping_list_page()
            self.should_be_recipe_in_shopping_list(data)
            download_list_button = self.browser.find_element(*ShoppingCartLocators.DOWNLOAD_LIST_BUTTON)
            download_list_button.click()
            time.sleep(1)



    def remove_recipe_shopping_list(self):
        """Чистим список покупок"""
        self.go_to_shopping_list_page()
        remove_recipe_button = self.find_elements(*ShoppingCartLocators.DOWNLOAD_LIST_BUTTON)
        
        for delete_recipes in remove_recipe_button:
            delete_recipes.click()


    def should_be_recipe_in_shopping_list(self, data):
        '''Проверка наличия рецепта в списке покупок'''
        recipe_name = (By.LINK_TEXT, f'{data}')
        assert self.is_element_present(*recipe_name), 'The subscription is not presented'

    def not_should_be_recipe_in_shopping_list(self, data):
        '''Проверка отсутствия рецепта в списке покупок'''
        recipe_name = (By.LINK_TEXT, f'{data}')
        assert self.is_not_element_present(*recipe_name), 'The subscription is presented'


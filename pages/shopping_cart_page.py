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
        add_shopping_cart_button_locator = (By.XPATH, f'//a[text()="{data}"]//following::button[1]')
        add_shopping_cart_button = self.browser.find_element(*add_shopping_cart_button_locator)
        if add_shopping_cart_button.text == 'Рецепт добавлен':
            self.go_to_shopping_list_page()
            time.sleep(3)
            self.should_be_recipe_in_shopping_list(data)
            # переходим на страницу корзины, проверяем, что данный рецепт есть и скачиваем лист покупок

        else:
            add_shopping_cart_button.click()
            self.go_to_shopping_list_page()
            time.sleep(3)

            self.should_be_recipe_in_shopping_list(data)
            # переходим на страницу корзины, проверяем что рецепт есть и качаем его


    def should_be_recipe_in_shopping_list(self, data):
        '''Проверка наличия подиски'''
        recipe_name = (By.LINK_TEXT, f'{data}')
        assert self.is_element_present(*recipe_name), 'The subscription is not presented'

    def not_should_be_recipe_in_shopping_list(self, data):
        '''Проверка отсутствия подиски'''
        recipe_name = (By.LINK_TEXT, f'{data}')
        assert self.is_not_element_present(*recipe_name), 'The subscription is presented'


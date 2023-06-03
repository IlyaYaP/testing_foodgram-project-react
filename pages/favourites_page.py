import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from .base_page import BasePage


class FavouritesPage(BasePage):

    def add_favorites(self, data):
        '''Функция добавления рецептов в избранное'''
        with allure.step('Добавляем рецепт в избранное.'):
            favourites_button_locator = (By.XPATH, f'//a[text()="{data}"]\
                                         //following::button[2]')
            favourites_button = self.browser.find_element(
                               *favourites_button_locator)
            favourites_button.click()
            self.go_to_favorites_page()

    def delete_favotites(self, data):
        '''Функция удаления рецептов в избранное'''
        with allure.step('Удаляем рецепт из избранного.'):
            self.go_to_favorites_page()
            favourites_button_locator = (By.XPATH, f'//a[text()="{data}"]\
                                         //following::button[2]')
            favourites_button = self.browser.find_element(
                                *favourites_button_locator)
            favourites_button.click()
            self.browser.refresh()

    def should_be_favorites(self, data):
        '''Функция проверки, что рецепт появился в избранном'''
        favorites_name = (By.LINK_TEXT, f'{data}')
        with allure.step('Проверяем, что рецепт появился в избранном.'):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
            assert self.is_element_present_timeout(
                   *favorites_name), 'The favorites is not presented'

    def not_should_be_favorites(self, data):
        '''Функция проверки наличия подиски'''
        favorites_name = (By.LINK_TEXT, f'{data}')
        with allure.step('Проверяем, что рецепт исчез из избранного.'):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
            assert self.is_not_element_present(
                   *favorites_name), 'The favorites is presented'

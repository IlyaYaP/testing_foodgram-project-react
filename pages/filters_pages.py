from .base_page import BasePage
from .locators import CreateRecipeLocators
from selenium.webdriver.common.by import By


class FiltersPage(BasePage):

    def tags_filter(self, tag_filter):
        '''Функция фильтрации по тегу'''
        tag_name = self.browser.find_elements(*CreateRecipeLocators.TAG_NAME)
        for tag in tag_name:
            if tag.text == tag_filter:
                tag_button_locator = (By.XPATH, f'//span[text()="{tag_filter}"]/../button')
                tag_button = self.browser.find_element(*tag_button_locator)
                tag_button.click()
                self.should_be_recipes_tags(tag_filter)
            else:
                continue

    def should_be_recipes_tags(self, tag_filter):
        '''Проверка работы фильтров'''
        tag_name = self.browser.find_elements(*CreateRecipeLocators.TAG_NAME)
        for tag in tag_name:
            if tag.text != tag_filter:
                assert '-----Tag filtering doesnt work!'
            else:
                continue

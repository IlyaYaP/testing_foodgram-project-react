from .base_page import BasePage
from .locators import CreateRecipeLocators
from .data import DataRecipeCreate
from selenium.webdriver.common.by import By
import time
import pytest


class RecipeCreation(BasePage):

    def create_recipe(self):
        '''Функция создания рецепта'''
        self.go_to_recipes_creat_page()
        recipe_name = self.browser.find_element(*CreateRecipeLocators.RECIPE_NAME)
        recipe_name.send_keys(DataRecipeCreate.RECIPE_NAME)
        cooking_time = self.browser.find_element(*CreateRecipeLocators.COOKING_TIME)
        cooking_time.send_keys(DataRecipeCreate.COOKING_TIME)
        recipe_description = self.browser.find_element(*CreateRecipeLocators.RECIPE_DESCRIPTION)
        recipe_description.send_keys(DataRecipeCreate.RECIPE_DESCRIPTION)
        add_file_button = self.browser.find_element(*CreateRecipeLocators.FILE_INPUT)
        self.tags_selection(DataRecipeCreate.MEAL)
        self.add_ingredients(DataRecipeCreate.INGREDIENTS)
        self.add_image(DataRecipeCreate.IMAGE_NAME, add_file_button)
        button_create_recipe_form = self.browser.find_element(*CreateRecipeLocators.BUTTON_CREATE_RECIPE_FORM)
        button_create_recipe_form.click()


    def tags_selection(self, meal):
        '''Функция выбора тега'''
        tag_name = self.browser.find_elements(*CreateRecipeLocators.TAG_NAME)
        i = 0
        while i < len(tag_name):
            try:
                for meal in tag_name:
                    if meal.text == DataRecipeCreate.MEAL[i]:
                        tag_button_locator = (By.XPATH, f'//span[text()="{meal.text}"]/../button')
                        tag_button = self.browser.find_element(*tag_button_locator)
                        tag_button.click()
            except IndexError:
                pass
            i += 1

    def add_ingredients(self, ingredients):
        '''Функция добавления игридиентов'''
        input_ingredients = self.browser.find_element(*CreateRecipeLocators.INGREDIENTS)
        ingredients_amount = self.browser.find_element(*CreateRecipeLocators.AMOUNT_VALUE)
        button_add_ingredients = self.browser.find_element(*CreateRecipeLocators.ADD_INDREDIENT_BUTTON)
        
        for ingredien, amount in ingredients.items():
            input_ingredients.send_keys(ingredien)
            ingredients_drop_list = self.browser.find_element(*CreateRecipeLocators.INGREDIENTS_DROP_LIST)
            ingredients_drop_list.click()
            ingredients_amount.send_keys(amount)
            button_add_ingredients.click()


    def should_be_recipe_form(self):
        '''Проверка наличия созданого рецепта'''
        assert self.is_element_present(*CreateRecipeLocators.RECIPE_TITLE), 'The recipe creation is not presented'


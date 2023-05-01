from .base_page import BasePage
from .locators import CreateRecipeLocators
from .data import DataRecipeCreate

class RecipeCreation(BasePage):

    def create_recipe(self):
        '''Функция создания рецепта'''
        create_recipe_button = self.browser.find_element(*CreateRecipeLocators.BUTTON_CREATE_RECIPE)
        create_recipe_button.click()
        recipe_name = self.browser.find_element(*CreateRecipeLocators.RECIPE_NAME)
        recipe_name.send_keys(DataRecipeCreate.RECIPE_NAME)

    
    def tags_selection(self, meal):
        
        if meal == 'Завтрак':
             button_tag = self.browser.find_element(*CreateRecipeLocators.TAG_BUTTON)
             button_tag.click()
        else:
            print("asdf")
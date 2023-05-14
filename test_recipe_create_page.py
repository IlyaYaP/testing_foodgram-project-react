from pages.recipe_create_page import RecipeCreation
from pages.log_reg_page import LoginPage
from pages.links import main_page_link
from pages.locators import CreateRecipeLocators
from data.data_recipe_create import DataRecipeCreateBreakfast, DataRecipeCreateDinner, DataRecipeCreateLunch
from data.data_registration import DataRegistrationAndLoginUser_1
import pytest

class TestRecipeCreate():
    
    @pytest.mark.recipe_create
    @pytest.mark.parametrize('recipe_name_data, \
                             cooking_time_data, \
                             recipe_description_data, \
                             meal_data, \
                             ingredients_data, \
                             image_name_data', 
                             [DataRecipeCreateBreakfast.RECIP_DATA_BREAKFAST,
                             DataRecipeCreateLunch.RECIP_DATA_LUNCH,
                             DataRecipeCreateDinner.RECIP_DATA_DINNER])
    
    def test_recipe_create(self, 
                           browser, 
                           recipe_name_data, 
                           cooking_time_data, 
                           recipe_description_data, 
                           meal_data, 
                           ingredients_data, 
                           image_name_data):
        '''Тест создания рецепта'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.valid_data_login)
        page_recipe_create = RecipeCreation(browser, browser.current_url)
        page_recipe_create.create_recipe(recipe_name_data, 
                                         cooking_time_data, 
                                         recipe_description_data, 
                                         meal_data, 
                                         ingredients_data, 
                                         image_name_data)
        page_recipe_create.go_to_recipes_page()
        page_recipe_create.should_be_recipe(recipe_name_data)

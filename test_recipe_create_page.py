from pages.recipe_create_page import RecipeCreation
from pages.log_reg_page import LoginPage
from pages.links import main_page_link
from pages.locators import CreateRecipeLocators
from pages.data import DataForRegistration, DataRecipeCreate
import pytest
import time

class TestRecipeCreate():
    
    @pytest.mark.recipe_create
    def test_recipe_create(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataForRegistration.valid_data_login)
        page_recipe_create = RecipeCreation(browser, browser.current_url)
        page_recipe_create.create_recipe()
        page_recipe_create.go_to_recipes_page()
        page_recipe_create.should_be_recipe_form()

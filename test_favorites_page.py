from pages.log_reg_page import LoginPage
from data.data_registration import DataRegistrationAndLoginUser_2
from data.data_favourites import DataFavouries
from pages.favourites_page import FavouritesPage
from pages.links import main_page_link
import pytest
import time
import allure
from allure_commons.types import AttachmentType


@pytest.mark.run(order=5)
@pytest.mark.favourites_test(scope='class')
@allure.feature('Тесты добавления рецептов в избранное.')
class TestFavourites():
    @allure.story('Тест добавления рецептов в избранное')
    @pytest.mark.parametrize('data', DataFavouries.RECIPE_NAME)
    def test_favourites(self, browser, data):
        with allure.step('Открываем главную страницу и логинимся.'):
            page = LoginPage(browser, main_page_link)
            page.open()
            page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        with allure.step('Добавляем рецепт в избранное.'):
            page_favourites = FavouritesPage(browser, browser.current_url)
            page_favourites.add_favorites(data)
            page_favourites.should_be_favorites(data)


    @allure.story('Тест удаления рецептов из избранного')
    @pytest.mark.parametrize('data', DataFavouries.RECIPE_NAME)
    def test_delete_favourites(self, browser, data):
        with allure.step('Открываем главную страницу и логинимся.'):
            page = LoginPage(browser, main_page_link)
            page.open()
            page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        with allure.step('Удаляем рецепт из избранного.'):
            page_favourites = FavouritesPage(browser, browser.current_url)
            page_favourites.delete_favotites(data)
            page_favourites.not_should_be_favorites(data)

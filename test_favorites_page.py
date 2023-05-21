from pages.log_reg_page import LoginPage
from data.data_registration import DataRegistrationAndLoginUser_2
from data.data_favourites import DataFavouries
from pages.favourites_page import FavouritesPage
from pages.links import main_page_link
import pytest
import time

@pytest.mark.favourites_test(scope='class')
class TestFavourites():

    @pytest.mark.parametrize('data', DataFavouries.RECIPE_NAME)
    def test_favourites(self, browser, data):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        page_favourites = FavouritesPage(browser, browser.current_url)
        page_favourites.add_favorites(data)


    @pytest.mark.parametrize('data', DataFavouries.RECIPE_NAME)
    def test_delete_favourites(self, browser, data):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        page_favourites = FavouritesPage(browser, browser.current_url)
        page_favourites.delete_favotites(data)

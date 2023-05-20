from pages.log_reg_page import LoginPage
from data.data_registration import DataRegistrationAndLoginUser_2
from pages.favourites_page import FavouritesPage
from pages.links import main_page_link
import pytest
import time

@pytest.mark.favourites_test(scope='class')
class TestFavourites():

    @pytest.mark.parametrize('data', ['Сало в соевом соусе вареное', 'Говядина с болгарским перцем'])
    def test_favourites(self, browser, data):
        page = LoginPage(browser, main_page_link)
        page.open()
        time.sleep(2)
        page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        time.sleep(2)
        page_favourites = FavouritesPage(browser, browser.current_url)
        page_favourites.add_favorites(data)

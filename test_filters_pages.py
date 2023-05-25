from pages.filters_pages import FiltersPage
from pages.log_reg_page import LoginPage
from data.data_registration import DataRegistrationAndLoginUser_2
from data.data_favourites import DataFavouries
from data.data_filters_pages import DataFiltersPages
from pages.favourites_page import FavouritesPage
from pages.links import main_page_link
import pytest
import time


@pytest.mark.run(order=6)
@pytest.mark.filters_tags(scope='class')
class TestFiltersTags():

    @pytest.mark.parametrize('data', ['Завтрак', 'Обед', 'Ужин'])
    def test_filter_tags_recipes_page(self, browser, data):
        '''Тест фильтрации по тегу на странице рецептов'''
        page = FiltersPage(browser, main_page_link)
        page.open()
        page.tags_filter(data)
        time.sleep(2)

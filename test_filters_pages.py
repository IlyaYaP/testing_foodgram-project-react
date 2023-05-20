from pages.filters_pages import FiltersPage
from pages.links import main_page_link
import pytest


@pytest.mark.filters_tags(scope='class')
class TestFiltersTags():

    @pytest.mark.parametrize('data', ['Завтрак', 'Обед', 'Ужин'])
    def test_filter_tags_recipes_page(self, browser, data):
        '''Тест фильтрации по тегу на странице рецептов'''
        page = FiltersPage(browser, main_page_link)
        page.open()
        page.tags_filter(data)

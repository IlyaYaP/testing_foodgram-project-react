import allure
import pytest

from pages.filters_pages import FiltersPage
from pages.links import main_page_link


@pytest.mark.run(order=6)
@pytest.mark.filters_tags(scope='class')
@allure.feature('Тесты фильтрации по тегу.')
class TestFiltersTags():
    @allure.story('Тест фильтрации по тегу на главной странице.')
    @pytest.mark.parametrize('data', ['Завтрак', 'Обед', 'Ужин'])
    def test_filter_tags_recipes_page(self, browser, data):
        page = FiltersPage(browser, main_page_link)
        page.open()
        page.tags_filter(data)

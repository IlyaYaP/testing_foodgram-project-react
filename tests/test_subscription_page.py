import allure
import pytest

from data.data_registration import DataRegistrationAndLoginUser_2
from pages.links import main_page_link
from pages.log_reg_page import LoginPage
from pages.subscriptions_page import SubscriptionsPage


@pytest.mark.run(order=4)
@pytest.mark.subscribe_test(scope='class')
@allure.feature('Тесты подписки на автора рецептов.')
class TestSubscription():

    @pytest.mark.subscription_test
    @allure.story('Тест осуществления подписки на автора')
    def test_subscription(self, browser):
        
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        page_subscription = SubscriptionsPage(browser, browser.current_url)
        page_subscription.subscription()

    @allure.story('Тест осуществления отписки на автора')
    @pytest.mark.unsubscribe_test
    def test_unsubscribe(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        page_subscription = SubscriptionsPage(browser, browser.current_url)
        page_subscription.unsubscribe()




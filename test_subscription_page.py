from pages.log_reg_page import LoginPage
from pages.subscriptions_page import SubscriptionsPage
from pages.links import main_page_link
from data.data_registration import DataRegistrationAndLoginUser_2
import pytest


@pytest.mark.subscribe_test(scope='class')
class TestSubscription():
    
    @pytest.mark.subscription_test
    def test_subscription(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        page_subscription = SubscriptionsPage(browser, browser.current_url)
        page_subscription.subscription()

    @pytest.mark.unsubscribe_test
    def test_unsubscribe(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        page_subscription = SubscriptionsPage(browser, browser.current_url)
        page_subscription.unsubscribe()




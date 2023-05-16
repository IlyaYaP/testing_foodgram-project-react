from .base_page import BasePage
from .locators import SubscriptionsLocators
from data.data_registration import DataRegistrationAndLoginUser_1
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SubscriptionsPage(BasePage):
    def subscription(self):
        '''Функция подписки на автора'''

        author_name = self.browser.find_element(*SubscriptionsLocators.AUTHOR)
        author_name.click()
        button_sub = self.browser.find_element(*SubscriptionsLocators.SUBSCRIPTIONS_BUTTON)
        try:
            WebDriverWait(self.browser, timeout=1).until(EC.text_to_be_present_in_element((SubscriptionsLocators.SUBSCRIPTIONS_BUTTON), 'Отписаться от автора'))
            button_sub.click()
            self.go_to_subscriptions_page()
            self.not_should_be_subscription()
        except TimeoutException:
            button_sub.click()
            self.go_to_subscriptions_page()
            self.should_be_subscription()

        # Далее в отдельной функции напишем тест отписки и проверим, что элемент отсутствует


    def should_be_subscription(self):
        '''Проверка наличия подиски'''
        assert self.is_element_present(*SubscriptionsLocators.AUTHOR), 'The subscription is not presented'

    def not_should_be_subscription(self):
        assert self.is_not_element_present(*SubscriptionsLocators.AUTHOR), 'The subscription is presented'


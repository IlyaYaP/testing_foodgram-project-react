from .base_page import BasePage
from .locators import SubscriptionsLocators
from data.data_registration import DataRegistrationAndLoginUser_1
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubscriptionsPage(BasePage):
    def subscription(self):
        '''Функция подписки на автора'''

        author_name = self.browser.find_element(*SubscriptionsLocators.AUTHOR)
        author_name.click()
        # subscription_button = self.browser.find_element(*SubscriptionsLocators.SUBSCRIPTIONS_BUTTON)
        WebDriverWait(self.browser, timeout=2).until(EC.element_to_be_clickable((SubscriptionsLocators.SUBSCRIPTIONS_BUTTON))).click()
        self.go_to_subscriptions_page()
        # Далее в отдельной функции напишем тест отписки и проверим, что элемент отсутствует


        
    def should_be_subscription(self):
        '''Проверка наличия подиски'''
        assert self.is_element_present(*SubscriptionsLocators.AUTHOR), 'The subscription is not presented'

        # WebDriverWait(self.browser, timeout=5).until(EC.element_to_be_clickable((HeaderMenuButtons.RECIPES))).click()
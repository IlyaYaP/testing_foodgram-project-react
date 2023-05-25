from .base_page import BasePage
from .locators import SubscriptionsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

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

    def unsubscribe(self):
        '''Функция отписки от автора'''
        self.go_to_subscriptions_page()
        try:
            unsubscribe_button = self.browser.find_element(*SubscriptionsLocators.UNSUBSCRIBE_BUTTON)
            unsubscribe_button.click()
            self.is_disappeared_subscribe()
        except NoSuchElementException:
            print(f'-----------You are not subscribed to this author!')


    def should_be_subscription(self):
        '''Проверка наличия подиски'''
        assert self.is_element_present(*SubscriptionsLocators.AUTHOR), 'The subscription is not presented'

    def not_should_be_subscription(self):
        '''Проверка отсутствия подиски'''
        assert self.is_not_element_present(*SubscriptionsLocators.AUTHOR), 'The subscription is presented'

    def is_disappeared_subscribe(self):
        '''Проверка что рецепты подписки исчезли'''
        assert self.is_disappeared(*SubscriptionsLocators.AUTHOR_UNSUBSCRIBE)


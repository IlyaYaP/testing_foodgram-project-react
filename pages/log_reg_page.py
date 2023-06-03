
import allure
from allure_commons.types import AttachmentType

from data.data_registration import DataRegistrationAndLoginUser_1

from .base_page import BasePage
from .locators import LogRegLocators


class LoginPage(BasePage):

    def registration_new_user_2(self, data):
        '''Функция регистрации нового пользователя'''
        self.go_to_registration_page()
        with allure.step('Регистрируем нового пользователя.'):
            form_inputs = self.browser.find_elements(
                          *LogRegLocators.REGISTRATION_FORM_INPUT)
            i = 0
            while i < len(form_inputs):
                form_inputs[i].send_keys(data[i])
                i += 1
            registration_button = self.browser.find_element(
                                  *LogRegLocators.REGISTRATION_BUTTON)
            registration_button.click()

    def login_user(self, data):
        '''Функция аутентификации зарегистрированого пользователя'''
        self.go_to_login_page()
        with allure.step('Проходим процесс аутентификации.'):
            form_input = self.browser.find_elements(
                         *LogRegLocators.LOGIN_FORM_INPUT)
            i = 0
            while i < len(form_input):
                form_input[i].send_keys(data[i])
                i += 1
            login_button = self.browser.find_element(
                           *LogRegLocators.LOGIN_BUTTON)
            login_button.click()

    def password_changes(self):
        '''Функция изменения пароля зарегистрированого пользователя'''
        self.go_to_change_password_page()
        with allure.step('Меняем пароль.'):
            current_password = self.browser.find_element(
                            *LogRegLocators.CURRENT_PASSWORD)
            current_password.send_keys(DataRegistrationAndLoginUser_1.PASSWORD)
            new_password = self.browser.find_element(
                            *LogRegLocators.NEW_PASSWORD)
            new_password.send_keys(DataRegistrationAndLoginUser_1.NEW_PASSWORD)
            repeat_password = self.browser.find_element(
                            *LogRegLocators.REPEAT_PASSWORD)
            repeat_password.send_keys(
                            DataRegistrationAndLoginUser_1.REPEAT_PASSWORD)
            button_password_changes_form = self.browser.find_element(
                            *LogRegLocators.BUTTON_PASSWORD_CHANGES_FORM)
            button_password_changes_form.click()

    def password_changes_back(self):
        '''Функция изменения пароля зарегистрированого пользователя'''
        self.go_to_change_password_page()
        with allure.step('Меняем пароль обратно.'):
            current_password = self.browser.find_element(
                            *LogRegLocators.CURRENT_PASSWORD)
            current_password.send_keys(
                            DataRegistrationAndLoginUser_1.NEW_PASSWORD)
            new_password = self.browser.find_element(
                            *LogRegLocators.NEW_PASSWORD)
            new_password.send_keys(DataRegistrationAndLoginUser_1.PASSWORD)
            repeat_password = self.browser.find_element(
                            *LogRegLocators.REPEAT_PASSWORD)
            repeat_password.send_keys(DataRegistrationAndLoginUser_1.PASSWORD)
            button_password_changes_form = self.browser.find_element(
                            *LogRegLocators.BUTTON_PASSWORD_CHANGES_FORM)
            button_password_changes_form.click()

    def should_be_login_form(self):
        '''Проверка наличия формы входа'''
        with allure.step('Проверяем, что после удачной регистрации,\
                         нас перенаправили на страницу аутентификации.'):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
            assert self.is_element_present(
                   *LogRegLocators.LOGIN_FORM), 'Login form is not presented'

    def not_should_be_login_form(self):
        '''Проверка отсутствия формы входа'''
        with allure.step('Проверяем, что после ввода невалидных данных,\
                         нас не перенаправили на страницу аутентификации.'):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
            assert self.is_not_element_present(
                   *LogRegLocators.LOGIN_FORM), 'Login form is presented'

    def should_be_create_recipe_button(self):
        '''Проверка наличия кнопки "создать рецепт"'''
        with allure.step('Проверяем, что после успешной аутентификации\
                         или изменения пароля,\
                         нас перенаправили на страницу с рецептами.'):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
            assert self.is_element_present(
                   *LogRegLocators.BUTTON_CREATE_RECIPE
                   ), 'The recipe creation button is not presented'

    def not_should_be_create_recipe_button(self):
        '''Проверка отсутствия кнопки "создать рецепт'''
        with allure.step('Проверяем, что после ввода невалидных данных,\
                         нас не перенаправили на страницу c рецептами.'):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
            assert self.is_not_element_present(
                   *LogRegLocators.BUTTON_CREATE_RECIPE
                   ), 'The recipe creation button is presented'

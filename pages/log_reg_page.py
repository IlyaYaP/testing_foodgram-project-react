
from .base_page import BasePage
from .locators import LogRegLocators
from .data import DataForRegistration

class LoginPage(BasePage):
    
    def registration_new_user_2(self, data):
        '''Функция регистрации нового пользователя'''
        self.go_to_registration_page()
        form_inputs = self.browser.find_elements(*LogRegLocators.REGISTRATION_FORM_INPUT)
        i = 0
        while i < len(form_inputs):
            form_inputs[i].send_keys(data[i])
            i += 1
        registration_button = self.browser.find_element(*LogRegLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def login_user(self, data):
        '''Функция аутентификации зарегистрированого пользователя'''
        self.go_to_login_page()
        form_input = self.browser.find_elements(*LogRegLocators.LOGIN_FORM_INPUT)
        i = 0
        while i < len(form_input):
            form_input[i].send_keys(data[i])
            i += 1
        login_button = self.browser.find_element(*LogRegLocators.LOGIN_BUTTON)
        login_button.click()

    def password_changes(self):
        '''Функция изменения пароля зарегистрированого пользователя'''
        button_password_changes = self.browser.find_element(*LogRegLocators.BUTTON_PASSWORD_CHANGES)
        button_password_changes.click()
        current_password = self.browser.find_element(*LogRegLocators.CURRENT_PASSWORD)
        current_password.send_keys(DataForRegistration.PASSWORD)
        new_password = self.browser.find_element(*LogRegLocators.NEW_PASSWORD)
        new_password.send_keys(DataForRegistration.NEW_PASSWORD)
        repeat_password = self.browser.find_element(*LogRegLocators.REPEAT_PASSWORD)
        repeat_password.send_keys(DataForRegistration.REPEAT_PASSWORD)
        button_password_changes_form = self.browser.find_element(*LogRegLocators.BUTTON_PASSWORD_CHANGES_FORM)
        button_password_changes_form.click()

    def password_changes_back(self):
        '''Функция изменения пароля зарегистрированого пользователя'''
        button_password_changes = self.browser.find_element(*LogRegLocators.BUTTON_PASSWORD_CHANGES)
        button_password_changes.click()
        current_password = self.browser.find_element(*LogRegLocators.CURRENT_PASSWORD)
        current_password.send_keys(DataForRegistration.NEW_PASSWORD)
        new_password = self.browser.find_element(*LogRegLocators.NEW_PASSWORD)
        new_password.send_keys(DataForRegistration.PASSWORD)
        repeat_password = self.browser.find_element(*LogRegLocators.REPEAT_PASSWORD)
        repeat_password.send_keys(DataForRegistration.PASSWORD)
        button_password_changes_form = self.browser.find_element(*LogRegLocators.BUTTON_PASSWORD_CHANGES_FORM)
        button_password_changes_form.click()


    def should_be_login_form(self):
        '''Проверка наличия формы входа'''
        assert self.is_element_present(*LogRegLocators.LOGIN_FORM), 'Login form is not presented'

    def not_should_be_login_form(self):
        '''Проверка отсутствия формы входа'''
        assert self.is_not_element_present(*LogRegLocators.LOGIN_FORM), 'Login form is presented'

    def should_be_create_recipe_button(self):
        '''Проверка наличия кнопки "создать рецепт"'''
        assert self.is_element_present(*LogRegLocators.BUTTON_CREATE_RECIPE), 'The recipe creation button is not presented'

    def not_should_be_create_recipe_button(self):
        '''Проверка отсутствия кнопки "создать рецепт"'''
        assert self.is_not_element_present(*LogRegLocators.BUTTON_CREATE_RECIPE), 'The recipe creation button is presented'

































    # регистрация нового пользователя, если тест успешный, осуществляется переходно на страницу входа
    # если пользователь уже существует, тест падает с соответствующем сообщением 

    # def register_new_user(self):
    #     self.go_to_registration_page()
    #     first_name = self.browser.find_element(*LogRegLocators.REG_USER_FIRST_NAME)
    #     first_name.send_keys(ValidDataForRegistration.FIRST_NAME)
    #     last_name = self.browser.find_element(*LogRegLocators.REG_USER_LAST_NAME)
    #     last_name.send_keys(ValidDataForRegistration.LAST_NAME)
    #     user_name = self.browser.find_element(*LogRegLocators.REG_USER_NAME)
    #     user_name.send_keys(ValidDataForRegistration.USER_NAME)
    #     user_email = self.browser.find_element(*LogRegLocators.REG_USER_EMAIL)
    #     user_email.send_keys(ValidDataForRegistration.EMAIL)
    #     user_password = self.browser.find_element(*LogRegLocators.REG_USER_PASSWORD)
    #     user_password.send_keys(ValidDataForRegistration.PASSWORD)
    #     registration_button = self.browser.find_element(*LogRegLocators.REGISTRATION_BUTTON)
    #     registration_button.click()

    # def login_user(self):
    #     '''функция входа зарегистрированого пользователя'''
    #     self.go_to_login_page()
    #     user_email = self.browser.find_element(*LogRegLocators.LOGIN_EMAIL)
    #     user_email.send_keys(ValidDataForRegistration.EMAIL)
    #     user_password = self.browser.find_element(*LogRegLocators.LOGIN_PASSWORD)
    #     user_password.send_keys(ValidDataForRegistration.PASSWORD)
    #     login_button = self.browser.find_element(*LogRegLocators.LOGIN_BUTTON)
    #     login_button.click()

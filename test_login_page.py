from pages.log_reg_page import LoginPage
from pages.links import main_page_link
from data.data_registration import DataRegistrationAndLoginUser_1, DataRegistrationAndLoginUser_2
import pytest
import allure
from allure_commons.types import AttachmentType

@pytest.mark.run(order=1)
@pytest.mark.registration_form_test(scope='class')
@allure.feature('Тесты регистрации нового пользователя.')
class TestRegistrationForm():

    @pytest.mark.registration_test(scope='function', autouse=True)
    @pytest.mark.parametrize('data', [DataRegistrationAndLoginUser_1.valid_data_registration, 
                                      DataRegistrationAndLoginUser_2.valid_data_registration])

    @allure.story('Тест регистрации нового пользователя.')
    def test_registration_form(self, browser, data):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.registration_new_user_2(data)
        page.alert_handler()
        page.should_be_login_form()

    @allure.story('Негативный тест: Тест регистрации нового пользователя с использованием невалидных данных.')
    @pytest.mark.registration_negative_test(scope='function')
    @pytest.mark.parametrize('data', [DataRegistrationAndLoginUser_1.invalid_data_registration_username_email,
                                      DataRegistrationAndLoginUser_1.invalid_data_registration_pass])
    def test_registration_form_negative(self, browser, data):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.registration_new_user_2(data)
        page.is_alert_present()
        page.not_should_be_login_form()

@allure.feature('Тесты аутентификации зарегистрированного пользователя.')
@pytest.mark.run(order=2)
@pytest.mark.login_form_test(scope='class')
class TestLoginForm():
    @pytest.mark.login_test(scope='function')
    @allure.story('Тест аутентификации.')
    def test_login_form(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.valid_data_login)
        page.alert_handler()
        page.should_be_create_recipe_button()

    @pytest.mark.login_test_negative(scope='function')
    @allure.story('Негативный тест: Тест аутентификации с использованием невалидных данных.')
    def test_login_form_negative(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.invalid_data_login)
        page.is_alert_present()
        page.not_should_be_create_recipe_button()

    @pytest.mark.password_changes_test(scope='function')
    @allure.story('Тест изменения пароля.')
    def test_password_changes(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.valid_data_login)
        page.password_changes()
        page.alert_handler()
        page.should_be_create_recipe_button()
        # Ниже, меняем пароль обратно)
        page.password_changes_back()

    @pytest.mark.negative_login_form(scope='function')
    @allure.story('Негативный тест: Тест аутентификации с невалидными данными.')
    @allure.description('В данном тесте, воспроизводится сценарий при котором: \
                          1.пользователь при аутентификации, указывает невалидные данные \
                          2.сообщение об ошибке(алерт) не появляется \
                          3.система принимает данные и авторизует пользователя')
    
    def test_negative_login_form(self, browser):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.invalid_data_login)
        page.is_alert_present()
        page.not_should_be_create_recipe_button()







        

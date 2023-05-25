from pages.log_reg_page import LoginPage
from pages.links import main_page_link
from data.data_registration import DataRegistrationAndLoginUser_1, DataRegistrationAndLoginUser_2
import pytest

@pytest.mark.run(order=1)
@pytest.mark.registration_form_test(scope='class')
class TestRegistrationForm():

    @pytest.mark.registration_test(scope='function', autouse=True)
    @pytest.mark.parametrize('data', [DataRegistrationAndLoginUser_1.valid_data_registration, 
                                      DataRegistrationAndLoginUser_2.valid_data_registration])


    def test_registration_form(self, browser, data):
        '''Тест регистрации нового пользователя'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.registration_new_user_2(data)
        page.alert_handler()
        page.should_be_login_form()

    @pytest.mark.registration_negative_test(scope='function')
    @pytest.mark.parametrize('data', [DataRegistrationAndLoginUser_1.invalid_data_registration_username_email,
                                      DataRegistrationAndLoginUser_1.invalid_data_registration_pass])
    def test_registration_form_negative(self, browser, data):
        '''Тест регистрации нового пользователя'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.registration_new_user_2(data)
        page.is_alert_present()
        page.not_should_be_login_form()


@pytest.mark.run(order=2)
@pytest.mark.login_form_test(scope='class')
class TestLoginForm():

    # Проверка валидных и невалидных данных при аутентификации пользователя
    @pytest.mark.login_test(scope='function')
    def test_login_form(self, browser):
        '''Тест аутентификации нового пользователя'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.valid_data_login)
        page.alert_handler()
        page.should_be_create_recipe_button()

    def test_login_form_negative(self, browser):
        '''Тест аутентификации нового пользователя с невалидными данными'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.invalid_data_login)
        page.is_alert_present()
        page.not_should_be_create_recipe_button()

    @pytest.mark.password_changes_test(scope='function')
    def test_password_changes(self, browser):
        '''Тест изменения пароля'''
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.valid_data_login)
        page.password_changes()
        page.alert_handler()
        page.should_be_create_recipe_button()
        # Ниже, меняем пароль обратно)
        page.password_changes_back()

    @pytest.mark.negative_login_form(scope='function')
    def test_negative_login_form(self, browser):
        '''Тест формы входа в УЗ'''
        # В данном тесте, воспроизводится сценарий при котором:
        # 1.пользователь при аутентификации, указывает невалидные данные
        # 2.сообщение об ошибке(алерт) не появляется
        # 3.система принимает данные и авторизует пользователя
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_1.invalid_data_login)
        page.is_alert_present()
        page.not_should_be_create_recipe_button()







        

class DataRegistrationAndLoginUser_1():
    FIRST_NAME = 'Vasily'
    LAST_NAME = 'Ivanov'
    USER_NAME = 'Vasily_Ivanov'
    EMAIL = 'vasily@yandex.ru'
    PASSWORD = 'vasiliy12345'
    NEW_PASSWORD = 'vasiliy54321'
    REPEAT_PASSWORD = 'vasiliy54321'

    # данные для тестов регистрации нового пользователя
    valid_data_registration = [FIRST_NAME, LAST_NAME, USER_NAME, EMAIL, PASSWORD]

    invalid_data_registration_username_email = ['Vasily', 'Ivanov', 'Ivanov_Vasily!', 'vasilyemail.ru', 'vas*']
    invalid_data_registration_pass = ['Vasily', 'Ivanov', 'Vasily', 'v@asilyemail.ru', 'vas*']

    # данные для аутентификации зарегистрированного пользователя
    valid_data_login = [EMAIL, PASSWORD]

    invalid_data_login = ['vasilyyandex.ru', 'vasiliy12345']

    # данные для изменения пароля
    valid_data_change_password = [PASSWORD, NEW_PASSWORD, NEW_PASSWORD]
    valid_data_change_password_back = [NEW_PASSWORD, PASSWORD, PASSWORD]

class DataRegistrationAndLoginUser_2():
    FIRST_NAME = 'Ivan'
    LAST_NAME = 'Aleksandrivich'
    USER_NAME = 'Ivan_A'
    EMAIL = 'ivan@yandex.ru'
    PASSWORD = 'ivan12345'
    NEW_PASSWORD = 'ivan54321'
    REPEAT_PASSWORD = 'ivan54321'

    # данные для тестов регистрации нового пользователя
    valid_data_registration = [FIRST_NAME, LAST_NAME, USER_NAME, EMAIL, PASSWORD]

    # данные для аутентификации зарегистрированного пользователя
    valid_data_login = [EMAIL, PASSWORD]


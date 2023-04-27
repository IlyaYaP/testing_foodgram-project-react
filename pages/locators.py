from selenium.webdriver.common.by import By

class LogRegLocators():
    # локаторы кнопок для перехода к формам регистрации и входа в УЗ
    LOGIN_LINK = (By.CSS_SELECTOR, '.styles_menuLink__3a59I')
    REGISTRATION_LINK = (By.CSS_SELECTOR, '.styles_menuButton__1RUEF')

    # локаторы полей формы регистрации
    REG_USER_LAST_NAME = (By.CSS_SELECTOR, '[name="first_name"]')
    REG_USER_FIRST_NAME = (By.CSS_SELECTOR, '[name="last_name"]')
    REG_USER_NAME = (By.CSS_SELECTOR, '[name="username"]')
    REG_USER_EMAIL = (By.CSS_SELECTOR, '[name="email"]')
    REG_USER_PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.style_button__1FFWl')

    # локатор формы входа в УЗ
    LOGIN_FORM = (By.CSS_SELECTOR, '.styles_form__2_42b')

    # локатор полей формы регистрации
    REGISTRATION_FORM_INPUT = (By.CSS_SELECTOR, 'form input')

    # локатор полей формы входа в УЗ
    LOGIN_FORM_INPUT = (By.CSS_SELECTOR, 'form.styles_form__2_42b input')

    # локаторы входа в УЗ
    LOGIN_EMAIL = (By.CSS_SELECTOR, '[name="email"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.styles_button__1jD3X')
    
    # локатор кнопки перехода к форме создания рецепта
    BUTTON_CREATE_RECIPE = (By.CSS_SELECTOR, '[href="/recipes/create"]')

    # локатор кнопки перехода к форме изменения пароля
    BUTTON_PASSWORD_CHANGES = (By.LINK_TEXT, 'Изменить пароль')

    # локаторы формы изменения пароля
    CURRENT_PASSWORD = (By.CSS_SELECTOR, '[name="current_password"]')
    NEW_PASSWORD = (By.CSS_SELECTOR, '[name="new_password"]')
    REPEAT_PASSWORD = (By.CSS_SELECTOR, '[name="repeat_password"]')
    BUTTON_PASSWORD_CHANGES_FORM = (By.CSS_SELECTOR, '.style_button__1FFWl')
    PASSWORD_CHANGES_FORM_INPUT = (By.CSS_SELECTOR, 'form input')


from selenium.webdriver.common.by import By

class LogRegLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '.styles_menuLink__3a59I')
    REGISTRATION_LINK = (By.CSS_SELECTOR, '.styles_menuButton__1RUEF')
    REG_USER_LAST_NAME = (By.CSS_SELECTOR, '[name="first_name"]')
    REG_USER_FIRST_NAME = (By.CSS_SELECTOR, '[name="last_name"]')
    REG_USER_NAME = (By.CSS_SELECTOR, '[name="username"]')
    REG_USER_EMAIL = (By.CSS_SELECTOR, '[name="email"]')
    REG_USER_PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.style_button__1FFWl')
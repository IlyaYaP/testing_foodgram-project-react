from selenium.webdriver.common.by import By
from data.data_subscription import DataSubscription
from data.data_favourites import DataFavouries




class LogRegLocators():
    # Локаторы кнопок для перехода к формам регистрации и входа в УЗ
    LOGIN_LINK = (By.CSS_SELECTOR, '.styles_menuLink__3a59I')
    REGISTRATION_LINK = (By.CSS_SELECTOR, '.styles_menuButton__1RUEF')

    # Локаторы полей формы регистрации
    REG_USER_LAST_NAME = (By.CSS_SELECTOR, '[name="first_name"]')
    REG_USER_FIRST_NAME = (By.CSS_SELECTOR, '[name="last_name"]')
    REG_USER_NAME = (By.CSS_SELECTOR, '[name="username"]')
    REG_USER_EMAIL = (By.CSS_SELECTOR, '[name="email"]')
    REG_USER_PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.style_button__1FFWl')

    # Локатор формы входа в УЗ
    LOGIN_FORM = (By.CSS_SELECTOR, '.styles_form__2_42b')

    # Локатор полей формы регистрации
    REGISTRATION_FORM_INPUT = (By.CSS_SELECTOR, 'form input')

    # Локатор полей формы входа в УЗ
    LOGIN_FORM_INPUT = (By.CSS_SELECTOR, 'form.styles_form__2_42b input')

    # Локаторы входа в УЗ
    LOGIN_EMAIL = (By.CSS_SELECTOR, '[name="email"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.styles_button__1jD3X')
    
    # Локатор кнопки перехода к форме создания рецепта
    #BUTTON_CREATE_RECIPE = (By.CSS_SELECTOR, '[href="/recipes/create"]')
    BUTTON_CREATE_RECIPE = (By.LINK_TEXT, 'Создать рецепт')

    # Локаторы формы изменения пароля
    CURRENT_PASSWORD = (By.CSS_SELECTOR, '[name="current_password"]')
    NEW_PASSWORD = (By.CSS_SELECTOR, '[name="new_password"]')
    REPEAT_PASSWORD = (By.CSS_SELECTOR, '[name="repeat_password"]')
    BUTTON_PASSWORD_CHANGES_FORM = (By.CSS_SELECTOR, '.style_button__1FFWl')
    PASSWORD_CHANGES_FORM_INPUT = (By.CSS_SELECTOR, 'form input')

class CreateRecipeLocators():
    # Локаторы для создания рецепта
    RECIPE_CREATE_INPUT = (By.CSS_SELECTOR, '[data_test="recipe_create"]')
    RECIPE_NAME = (By.XPATH, '//div[text()="Название рецепта"]/../input')
    RECIPE_FORM = (By.CSS_SELECTOR, '.styles_single-card__info__2_cny')
    TAG_NAME = (By.CSS_SELECTOR, 'div.styles_checkbox-container__1vy_E span')


    INGREDIENTS = (By.CSS_SELECTOR, '.styles_ingredientsInput__1zzql')
    AMOUNT_VALUE = (By.CSS_SELECTOR, '.styles_ingredientsAmountValue__2matT')
    ADD_INDREDIENT_BUTTON = (By.CSS_SELECTOR, '.styles_ingredientAdd__3fc32')
    COOKING_TIME = (By.XPATH, '//div[text()="Время приготовления"]/../input')
    RECIPE_DESCRIPTION = (By.CSS_SELECTOR, '.styles_textareaField__1wfhC')
    ADD_FILE_BUTTON = (By.CSS_SELECTOR, '.styles_button__xzu5F')
    FILE_INPUT = (By.CSS_SELECTOR, '[type = "file"]')
    BUTTON_CREATE_RECIPE_FORM = (By.XPATH, '//button[text()="Создать рецепт"]')
    INGREDIENTS_DROP_LIST = (By.CSS_SELECTOR, '.styles_container__3ukwm div')


class HeaderMenuButtons():
    # Локаторы меню в хедаре
    RECIPES = (By.XPATH, '//a[text()="Рецепты"]')
    SUBSCRIPTIONS = (By.XPATH, '//a[text()="Мои подписки"]')
    RECIPES_CREATE = (By.XPATH, '//a[text()="Создать рецепт"]')
    FAVORITES = (By.XPATH, '//a[text()="Избранное"]')
    SHOPPING_LIST = (By.XPATH, '//a[text()="Список покупок"]')
    CHANGE_PASSWORD = (By.XPATH, '//a[text()="Изменить пароль"]')
    EXIT = (By.XPATH, '//a[text()="Выход"]')


class SubscriptionsLocators():
    # Локаторы для  осуществления подписки
    AUTHOR = (By.LINK_TEXT, f'{DataSubscription.AUTHOR}')
    AUTHOR_UNSUBSCRIBE = (By.XPATH, f'//a[text()="{DataSubscription.AUTHOR}"]//following::button[text()="Отписаться"]')
    SUBSCRIPTIONS_BUTTON = (By.CSS_SELECTOR, '.styles_buttonSubscribe__1C1fa')
    SUBSCRIBE_BUTTON = (By.XPATH, '//button[text()="Подписаться на автора"]')
    UNSUBSCRIBE_BUTTON = (By.CSS_SELECTOR, '.styles_subscriptionButton__WtOm-')


class TagFilter():
    # Локаторы для  осуществления фильтрации по тегу
    TAB_BUTTONS = (By.CSS_SELECTOR, '.styles_checkbox__1WBUC')

class FavouritesLocators():
    FAVOURITE_BUTTON = (By.XPATH, f'//a[text()="{DataFavouries.RECIPE_NAME}"]//following::button[2]')




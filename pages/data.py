class DataForRegistration():
    FIRST_NAME = 'Vasily'
    LAST_NAME = 'Ivanov'
    USER_NAME = 'Vasily_Ivanov'
    EMAIL = 'vasily@yandex.ru'
    PASSWORD = 'vasiliy12345'
    NEW_PASSWORD = 'vasiliy54321'
    REPEAT_PASSWORD = 'vasiliy54321'

    # данные для тестов регистрации нового пользователя
    valid_data = ['Vasily', 'Ivanov', 'Vasily_Ivanov', 'vasily@yandex.ru', 'vasiliy12345']
    invalid_data_username_email = ['Vasily', 'Ivanov', 'Ivanov_Vasily!', 'vasilyemail.ru', 'vas*']
    invalid_data_pass = ['Vasily', 'Ivanov', 'Vasily', 'v@asilyemail.ru', 'vas*']

    # данные для аутентификации зарегистрированного пользователя
    valid_data_login = ['vasily@yandex.ru', 'vasiliy12345']
    invalid_data_login = ['vasilyyandex.ru', 'vasiliy12345']

    # данные для изменения пароля
    valid_data_change_password = ['vasiliy12345', 'vasiliy54321', 'vasiliy54321']
    valid_data_change_password_back = ['vasiliy54321', 'vasiliy12345', 'vasiliy12345']


class DataRecipeCreate():
    RECIPE_NAME = 'Ленивые хачапури с сыром на сковороде на кефире'
    MEAL =  ['Обед']
    INGREDIENTS = {
                   'Мука': '50',
                   'Кефир': ' 100',
                   'Яйца': '1',
                   'Масло':'100',
                   'Сыр': '120'
                   }
    COOKING_TIME = '60'
    RECIPE_DESCRIPTION = 'Для приготовления ленивых хачапури подойдет любой сыр, \
                          который можно натереть на терке, я взяла сулугуни. \
                          Он достаточно соленый, поэтому соль в тесто класть не надо.\
                          Если у вас не оказалось кефира, возьмите сметану,\
                          творог или простоквашу - подойдет все, что заскучало в вашем холодильнике.\
                          Если вы взяли творог, то надо будет добавить немного молока.\
                          Можно положить рубленую зелень сразу в тесто или сделать что-то типа начинки.\
                          Для этого после того, как вы перевернете лепешку,\
                          посыпьте ее зеленью и сложите пополам, затем жарьте с двух сторон.'
    
    IMAGE_NAME = 'lenivye-xachapuri.jpg'
    
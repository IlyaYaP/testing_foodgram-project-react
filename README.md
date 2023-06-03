# Учебный проект по автоматизации тестирования UI 
В данном проекте реализована попытка автоматизации тестирования UI дипломного проекта [Foodgram(YandexPracticum)](https://github.com/IlyaYaP/foodgram-project-react)

### Стек технологий:
Стек: Python 3.7, Pytest 7.3.1, Selenium 4.9.0, Allure

# Развертывание проекта
- Развертываем проект [Foodgram(YandexPracticum)](https://github.com/IlyaYaP/foodgram-project-react) в соответствии с инструкцией.

- После успешного запуска проекта Foodgram клонируем данный репозиторий с проектом:
```
git clone https://github.com/IlyaYaP/testing_foodgram_project_react.git
```

- В папке с проектом создаем и активируем виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
```

- Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Укажите корректный путь для тестовых данных в base_page.py Ln 152.

- Запускаем тесты:
```
pytest -s -v --alluredir result_allure --tb=long
```

- Установка allure на Windows.
```
scoop install allure 
```

- Формируем отчет allure.
```
allure serve result_allure
```
- Наслаждаемся красивым отчетом, где можно детально разобрать все тест-кейсы.
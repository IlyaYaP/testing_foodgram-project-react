#Учебный проект по автоматизации тестирования UI 
В данном проекте реализована попытка автоматизации тестирования UI дипломного проекта [Foodgram(YandexPracticum)](https://github.com/IlyaYaP/foodgram-project-react)

### Стек технологий:
Стек: Python 3.7, Pytest 7.3.1, Selenium 4.9.0, Allure

1. Локальный отчет allure
- allure serve result_allure

ЛОКАЛЬНЫЙ ЗАПУСК ПРОЕКТА FOODGRAM

# Развертывание проекта
- Развертываем проект [Foodgram(YandexPracticum)](https://github.com/IlyaYaP/foodgram-project-react) в соответствии с инструкцией.

- После успешного запуска проекта Foodgram, клонируем данный репозиторий с проектом:
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

- Запускаем тесты:
```
pytest --alluredir result_allure -s -v --tb=long
```
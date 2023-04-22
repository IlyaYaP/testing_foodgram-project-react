import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action = 'store',
                     default = 'chrome', help = 'Choose browser: chrome or')
    parser.addoption('--language', action= 'store',
                     default = 'en', help = 'Choose lang')

@pytest.fixture(scope = 'function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')

    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        option_chrome = webdriver.ChromeOptions()
        option_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])
        option_chrome.add_experimental_option('prefs', 
                                               {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=option_chrome)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        option_firefox = webdriver.FirefoxOptions()
        option_firefox.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        option_firefox.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



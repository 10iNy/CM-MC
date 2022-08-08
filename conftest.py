import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language.")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        user_language = request.config.getoption("language")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(60)
        print("\nstart chrome browser for test..")
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        user_language = request.config.getoption("language")
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(60)
        print("\nstart firefox browser for test..")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

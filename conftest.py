import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="firefox",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="pytest --language=es",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")#добавить опцию language в функцию def pytest_addoption(parser)
    # (аналогично тому, как мы добавили на предыдущих шагах browser_name), а также при определении браузера
    # (def browser(request)) сказать драйверу, чтобы взял значение user_language из опции, передаваемой через терминал:
    # user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
      options = Options()
      options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
      print("\nstart chrome browser for test..")
      browser = webdriver.Chrome()
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")

    browser.quit()



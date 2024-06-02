import pytest
from selenium import webdriver

from utilities.readProperties import readConfig


@pytest.fixture()
def setup_teardown(request):
    browser = readConfig().read_configurations('basic info', 'browser')
    global driver
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print(f"provided browser is not from the list of given browsers,i.e,{browser}")
    driver.get(readConfig().getApplicationURL())
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()

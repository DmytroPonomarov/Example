from pytest import fixture
from selenium import webdriver
from chromedriver_py import binary_path


@fixture(scope='module')
def chrome_browser():
    browser = webdriver.Chrome(executable_path=binary_path)
    return browser


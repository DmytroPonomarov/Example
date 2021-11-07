from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def page_loaded_successfully_test(chrome_browser):
    chrome_browser.get('https://github.com/django/django')
    chrome_browser.maximize_window()

    WebDriverWait(chrome_browser, 60).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '.f6.Link--secondary.text-mono'))
    )
    commit_id = len(chrome_browser.find_elements_by_css_selector('.f6.Link--secondary.text-mono'))

    assert commit_id == 1


def last_commit_displaying_successfully_test(chrome_browser):
    commit_id_in_repo = chrome_browser.find_element_by_css_selector(
        '.f6.Link--secondary.text-mono'
    ).get_attribute('innerText')

    commits_page = chrome_browser.find_element_by_css_selector('.js-details-container .pl-3')
    commits_page.click()
    WebDriverWait(chrome_browser, 60).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '.BtnGroup'))
    )

    latest_commit_id = chrome_browser.find_element_by_css_selector(
        '.text-mono.f6.btn'
    ).get_attribute('innerText')

    assert commit_id_in_repo == latest_commit_id


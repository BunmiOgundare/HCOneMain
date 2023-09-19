import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
import time

@pytest.fixture
def browser():
    chromeservice = Service(executable_path="C:\\Users\\Bunmi.Ogundare\\pycharm_workspace\\HCOneSeleniumAutiomation\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=chromeservice)
    yield driver
    driver.quit()

def test_app_homepage(browser):
    browser.get("https://www.hc-one.co.uk")
    browser.maximize_window()

    time.sleep(5)

    expected_title = "HC One - The Kind Care Company | Residential Care Homes"
    assert expected_title == browser.title, f"Expected title: {expected_title}, but got title: {browser.title}"
    print("Homepage loaded successfully")

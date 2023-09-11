import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Create a Chrome driver instance
    os.environ['PATH'] += r";C:\Users\Bunmi.Ogundare\pycharm_workspace\HCOneSeleniumAutiomation\drivers"
    yield driver  # Provide the driver object to test functions
    driver.quit()  # Quit the driver after the test

def test_homepage_load(browser):
    browser.get("https://www.hc-one.co.uk/")
    browser.maximize_window()
    time.sleep(5)
    expected_title = "HC One - The Kind Care Company | Residential Care Homes"
    assert browser.title == expected_title, f"Expected title: {expected_title}, but got title: {browser.title}"
    print("Homepage loaded successfully")

def test_search_result(browser):
    browser.get("https://www.hc-one.co.uk/")
    time.sleep(5)
    cookie_button = browser.find_element(By.ID, "p_lt_ctl02_SimpleCookieLawConsent_btnAllowAll")
    cookie_button.click()
    time.sleep(2)
    search_bar = browser.find_element(By.ID, "searchForCarehome")
    search_bar.send_keys("Kirkwood Court Care Home")
    time.sleep(3)
    search_icon = browser.find_element(By.CLASS_NAME, "icon-search")
    search_icon.click()
    time.sleep(5)
    expected_title = "Kirkwood Court - Care home in Kenton, Newcastle upon Tyne | HC One"
    assert browser.title == expected_title, f"Expected title: {expected_title}, but got title: {browser.title}"
    print("Search result loaded successfully")


if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])

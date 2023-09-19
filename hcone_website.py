import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    os.environ['PATH'] += r";C:\Users\Bunmi.Ogundare\pycharm_workspace\HCOneSeleniumAutiomation\drivers"
    yield driver
    driver.quit()


def test_homepage_load(browser):
    browser.get("https://www.hc-one.co.uk/")
    browser.maximize_window()
    time.sleep(5)
    cookie_button = browser.find_element(By.ID, "p_lt_ctl02_SimpleCookieLawConsent_btnAllowAll")
    cookie_button.click()
    time.sleep(5)
    expected_title = "HC One - The Kind Care Company | Residential Care Homes"
    assert browser.title == expected_title, f"Expected title: {expected_title}, but got title: {browser.title}"
    # print("Homepage loaded successfully")


def test_getintouch(browser):
    browser.get("https://www.hc-one.co.uk/")
    browser.maximize_window()
    time.sleep(10)
    cookie_button = browser.find_element(By.ID, "p_lt_ctl02_SimpleCookieLawConsent_btnAllowAll")
    cookie_button.click()
    time.sleep(10)
    getting_in_touch_button = browser.find_element(By.CSS_SELECTOR, "#menuElem > li:nth-child(7) > a")
    getting_in_touch_button.click()
    time.sleep(10)
    expected_title = "Get In Touch - Contact Number and Details | HC One"
    assert browser.title == expected_title, f"Expected title: {expected_title}, but got title: {browser.title}"
    # print("Get In Touch page loaded successfully")


def test_join_the_team(browser):
    browser.get("https://www.hc-one.co.uk/")
    browser.maximize_window()
    time.sleep(4)
    join_team_button = browser.find_element(By.LINK_TEXT, "Join The Team")
    join_team_button.click()
    time.sleep(10)
    cookie_button = browser.find_element(By.LINK_TEXT, "I acknowledge I have read the above")
    cookie_button.click()
    time.sleep(5)
    cookiespolicy_button = browser.find_element(By.ID,  "epdsubmit")
    cookiespolicy_button.click()
    time.sleep(3)
    register_button = browser.find_element(By.XPATH, "//*[@id='ctl00_MyCandidateNavigation_liRegister']/a")
    register_button.click()
    time.sleep(3)
    expected_title = "Login/Register - HC-One"
    assert browser.title == expected_title, f"Expected title: {expected_title}, but got title: {browser.title}"
    # print("Register page loaded successfully")


def test_search_result(browser):
    browser.get("https://www.hc-one.co.uk/")
    browser.maximize_window()
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
    # print("Search result loaded successfully")


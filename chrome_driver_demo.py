from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.common.by import By
import time


class ChromeHomepageTest():

    def test(self):
        chromeservice = Service(executable_path="C:\\Users\\Bunmi.Ogundare\\pycharm_workspace\\HCOneSeleniumAutiomation\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chromeservice)
        driver.get("https://www.hc-one.co.uk/")
        driver.maximize_window()

        time.sleep(5)

        expected_title = "HC One - The Kind Care Company | Residential Care Homes"
        assert expected_title == driver.title, f"Expected title: {expected_title}, but got title: {driver.title}"
        print("Homepage loaded successfully")

        cookie_button = driver.find_element(By.ID, "p_lt_ctl02_SimpleCookieLawConsent_btnAllowAll")
        cookie_button.click()

        time.sleep(2)

        search_bar = driver.find_element(By.ID, "searchForCarehome")
        search_bar.send_keys("Kirkwood Court Care Home")

        time.sleep(3)

        search_icon = driver.find_element(By.CLASS_NAME, "icon-search")
        search_icon.click()

        time.sleep(5)

        expected_title = "Kirkwood Court - Care home in Kenton, Newcastle upon Tyne | HC One"
        assert expected_title == driver.title, f"Expected title: {expected_title}, but got title: {driver.title}"
        print("Search result loaded successfully")

        driver.quit()


runtests = ChromeHomepageTest()
runtests.test()


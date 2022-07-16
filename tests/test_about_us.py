# ----------------------------------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import os
from selenium import webdriver
from tests.test_webdrivers import chrome_path_win
from webdevable.pages.about_us_page import AboutUsPage


# ----------------------------------------------------------------------------------------------------------------------
# Webdriver paths
# ----------------------------------------------------------------------------------------------------------------------
chrome_path = os.path.normpath('../webdrivers/chromedriver_mac')


# ----------------------------------------------------------------------------------------------------------------------
# Website URL
# ----------------------------------------------------------------------------------------------------------------------
wda = 'http://webdevable.com'


# ----------------------------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------------------------
def test_about_us_page_displayed():
    driver = webdriver.Chrome(executable_path=chrome_path_win)

    # Given navigates to site
    driver.get(wda)

    # When clicks about us
    about_us_page = AboutUsPage(driver)
    about_us_page.goto()

    # Then page is displayed
    assert about_us_page.map.title.is_displayed

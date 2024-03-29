# ----------------------------------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from webdevable.pages.about_us_page import AboutUsPage

# ----------------------------------------------------------------------------------------------------------------------
# Website URL
# ----------------------------------------------------------------------------------------------------------------------
wda = 'http://webdevable.com'


# ----------------------------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------------------------
def test_about_us_page_displayed():
    driver = webdriver.Chrome()

    # Given navigates to site
    driver.get(wda)

    # When clicks about us
    about_us_page = AboutUsPage(driver)
    about_us_page.goto()

    # Then page is displayed
    assert about_us_page.map.title.is_displayed
    driver.quit()

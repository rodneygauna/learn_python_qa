# ----------------------------------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By
from webdevable.pages.base.pagebase import PageBase


# ----------------------------------------------------------------------------------------------------------------------
# Page Object - http://webdevable.com/aboutus.html
# ----------------------------------------------------------------------------------------------------------------------
class AboutUsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = AboutUsPageMap(driver)

    def goto(self):
        """ Navigates to the ABOUT US page """
        self.headernav.goto_about_us_page()


# ----------------------------------------------------------------------------------------------------------------------
# Page Map - http://webdevable.com/aboutus.html
# ----------------------------------------------------------------------------------------------------------------------
class AboutUsPageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def title(self):
        """ Title on the ABOUT US page """
        return self._driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/h1/strong')

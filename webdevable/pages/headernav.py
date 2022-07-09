# ----------------------------------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By


# ----------------------------------------------------------------------------------------------------------------------
# Page Object - http://webdevable.com
# ----------------------------------------------------------------------------------------------------------------------
class HeaderNav:
    def __init__(self, driver):
        self.map = HeaderNavMap(driver)

    def goto_home_page(self):
        """ Clicks on the HOME link in the navigation bar """
        self.map.home_link.click()

    def goto_about_us_page(self):
        """ Clicks on the ABOUT US link in the navigation bar """
        self.map.about_us_link.click()

    def goto_ux_consulting_page(self):
        """ Clicks on the UX CONSULTING link in the navigation bar """
        self.map.ux_consulting_link.click()

    def goto_contact_us_page(self):
        """ Clicks on the CONTACT US link in the navigation bar """
        self.map.contact_us_button.click()

    def goto_phone_number_button(self):
        """ Clicks on the PHONE NUMBER link in the navigation bar """
        self.map.home_link.click()


# ----------------------------------------------------------------------------------------------------------------------
# Page Map - http://webdevable.com
# ----------------------------------------------------------------------------------------------------------------------
class HeaderNavMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def home_link(self):
        """ Location of the HOME link in the navigation bar """
        return self._driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[1]/a')

    @property
    def about_us_link(self):
        """ Location of the ABOUT US link in the navigation bar """
        return self._driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/a')

    @property
    def ux_consulting_link(self):
        """ Location of the UX CONSULTING link in the navigation bar """
        return self._driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[3]/a')

    @property
    def contact_us_button(self):
        """ Location of the CONTACT US button in the navigation bar """
        return self._driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/form/div/a[2]')

    @property
    def phone_number_button(self):
        """ Location of the PHONE NUMBER button in the navigation bar """
        return self._driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/form/div/a[1]')

import os
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_path_win = os.path.normpath('C:\github\learn_python_qa\webdrivers\chromedriver_win.exe')


@given('the user navigates to webdevable.com')
def navigate_to_webdevable(context):
    context.driver = webdriver.Chrome(executable_path=chrome_path_win)
    context.driver.get("http://webdevable.com/")


@when('clicks the ABOUT US link in the navigation bar')
def navigate_to_about_us(context):
    context.driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/a').click()


@then('the About Us title appears')
def about_us_title(context):
    title = context.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/h1/strong')
    assert title.is_displayed

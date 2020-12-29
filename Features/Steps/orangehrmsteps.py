from behave import given, when, then
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome('E:\Python\chrome_driver\chromedriver.exe')


@when('open orange HRM homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo is present on homepage')
def verify_logo(context):
    status = context.driver.find_element_by_xpath('//*[@id="divLogo"]//img').is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()


from behave import *
from selenium import webdriver


@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome('E:\Python\chrome_driver\chromedriver.exe')


@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()



@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/h1").text
    except Exception, e:
        print str(e)
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"




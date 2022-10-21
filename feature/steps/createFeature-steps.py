from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
@given(u'I launch the chrome browser')
def openBrowser(context):
    context.driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')

@given(u'go to the url http://localhost:8085/')
def step_impl(context):
    context.driver.get("http://localhost:8085/login")

@given(u'enter email as "{email}" and password "{password}"')
def step_impl(context, email, password):
    #context.driverswitch_to.frame(context.driver.find_element(By.CSS_SELECTOR, "iframe"))
   # context.driver.find_element(By.XPATH, "//*[@id=\"app-container\"]/flt-glass-pane//input").click()

# @given(u'click on Features')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given click on Features')
#
#
# @given(u'I enter feature name as abcd')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I enter feature name as abcd')
#
#
# @given(u'I enter feature key as efgh')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I enter feature key as efgh')
#
#
# @given(u'I enter feature description as xyza')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I enter feature description as xyza')
#
#
# @given(u'I enter feature Reference Link as defg')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I enter feature Reference Link as defg')
#
#
# @given(u'I select feature type as String')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I select feature type as String')
#
#
# @then(u'the feature is Created')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the feature is Created')
#
#
# @then(u'the message saying Feature \'abcd\' created! is displayed')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the message saying Feature \'abcd\' created! is displayed')

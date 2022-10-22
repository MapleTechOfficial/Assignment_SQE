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
    context.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

@given(u'go to the url http://localhost:3000/')
def step_impl(context):
    context.driver.get("http://localhost:3000/")
    time.sleep(1.5)
@given(u'enter email as "{email}" and password "{password}" and click on login')
def step_impl(context, email, password):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-username\"]/div[2]/div/input").send_keys(email)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-password\"]/div[2]/div/input").send_keys(password)
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[2]/div/div[2]/div/form/div[4]/button/div").click()
    time.sleep(1.5)
    text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/aside/nav/div/div/div[2]/div/h4").text
    assert text == "COLLECTIONS"

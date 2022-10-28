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
    context.driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

@given(u'go to the url http://localhost:3000/')
def openURL(context):
    context.driver.maximize_window()
    try:
        context.driver.get("http://localhost:3000/")
    except WebDriverException:
          context.driver.close()
          print("Cannot open metabase url, make sure it is running on your localhost")
    time.sleep(1.5)
@given(u'enter email as "{email}" and password "{password}" and click on login')
def verifyLogin(context, email, password):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-username\"]/div[2]/div/input").send_keys(email)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-password\"]/div[2]/div/input").send_keys(password)
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[2]/div/div[2]/div/form/div[4]/button/div").click()
    time.sleep(1.5)
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/aside/nav/div/div/div[2]/div/h4").text
    except:
            context.driver.close()
            assert False, "Test Failed: The provided credentials are invalid"
    if text == "COLLECTIONS":
        assert True, "Logged In Successfully"
@given(u'I click on the settings icon')
def clickSettings(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/div[2]/div[3]/div/div/button").click()

@given(u'I click on Admin Settings')
def clickSettings(context):
    context.driver.find_element(By.XPATH,"/html/body/span/span/div/div/div/ol/li[2]/a/div/span").click()
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[1]/div[1]").text
    except:
            context.driver.close()
            assert False, "Test Failed: This is not an admin account"
    if text == "Settings":
        assert True, "Admin Settings Opened"
@given(u'I click on Databases')
def clickDatabase(context):
    context.driver.find_element(By.CSS_SELECTOR, "#root > div > div > nav > div.css-s00o23.e1nb3k9i6 > ul > li:nth-child(2) > a").click()
    time.sleep(0.2)
@given(u'I click on Add Database')
def clickAddDatabase(context):
    context.driver.find_element(By.CSS_SELECTOR, "#root > div > div > main > div > section.PageHeader.px2.clearfix > a").click()
    time.sleep(0.5)

@given(u'I select MySQL Database')
def selectMySQL(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-engine\"]/div[2]/a/button").click()
    time.sleep(0.1)
    context.driver.find_element(By.XPATH, "/html/body/span/span/div/div/div/div[8]/div/span").click()


@given(u'I enter Display Name as "{dispName}" and I enter Host as "{host}" and I enter Port as "{port}" and I enter Database Name as "{dbName}" and I enter Username as "{user}" and I enter Password as "{passw}"')
def addDBInfo(context, dispName, host, port, dbName, user, passw):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-name\"]/div[2]/div/input").send_keys(dispName)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-details-host\"]/div[2]/div/input").send_keys(host)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-details-port\"]/div[2]/input").send_keys(port)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-details-dbname\"]/div[2]/div/input").send_keys(dbName)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-details-user\"]/div[2]/div/input").send_keys(user)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-details-password\"]/div[2]/div/input").send_keys(passw)
    time.sleep(1)
@when(u'I click Save')
def clickSave(context):
    context.driver.find_element(By.CSS_SELECTOR, "#root > div > div > main > div > div > div > div > div > div > div.css-1y7gzfu.ez6veo62 > form > div.Form-actions.text-centered > button").click()

@then(u'I get the database "{dispName}" created')
def creationValidation(context, dispName):
    time.sleep(10)
    try:
        element = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/section[2]/table/tbody/tr[1]/td[1]/div/a")
    except:
        context.driver.close()
        assert False, "Test Scenario Failed: DB not created"
    if element.text == dispName:
        element.click()
        time.sleep(1)
        context.driver.find_element(By.CSS_SELECTOR, "#root > div > div > main > div > div > div.css-1h11kag.e1w91gxc0 > div > div:nth-child(2) > ol > li.mt2 > a").click()
        time.sleep(1)
        context.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/form/div[1]/input").send_keys(dispName)
        time.sleep(1)
        context.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/form/div[2]/button[2]").click()
        assert True, "Test Scenario Passed"
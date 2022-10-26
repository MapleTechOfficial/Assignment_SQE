from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


@when(u'I click on New button')
def clickonnew(context):
    context.driver.find_element(By.XPATH,
                                "// *[ @ id = 'root'] / div / header / div / div[2] / div[2] / span[1] / button").click()
    time.sleep(0.5)


@when(u'I click SQL Query')
def clickonsqlquery(context):
    context.driver.find_element(By.XPATH,
                                "/ html / body / span / span / div / div / div / ol / li[2] / a / div / span").click()
    time.sleep(1)


@when(u'select "{database}"')
def selectdatabase(context, database):
    context.driver.find_element(By.XPATH,

                                "//*[@id='root']/div/div/main/div/div/div[2]/main/div[1]/div/div[1]/div[1]/div/a/span[1]/span").click()

    try:
        art = context.driver.find_elements(By.CLASS_NAME, "List-item-title")
        j = 0
        for i in art:
            print(i.text)
            if(database in i.text):
                print(database)
                i.click()
                break

    except:
        context.driver.close()
        assert False,"database not found"



@when(u'write "{Query}"')
def step_impl(context,Query):
    context.driver.find_element(By.XPATH,"//*[@id='id_sql']/div[2]/div").click()
    context.driver.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Query)
    time.sleep(2)
    context.driver.find_element(By.XPATH,"// *[ @ id = 'root'] / div / div / main / div / div / div[2] / main / div[1] / div / div[2] / aside / button").click()
    time.sleep(5)
@then(u'Query result is displayed')
def step_impl(context):
      context.driver.close()


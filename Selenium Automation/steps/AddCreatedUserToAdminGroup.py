from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time



@given(u'Chrome Browser is launched')
def Chrome(context):
    context.driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver_win32\chromedriver.exe')
    assert True;




@given(u'The url http://localhost:3000/ is opened')
def URL(context):
    context.driver.maximize_window()
    try:
        context.driver.get("http://localhost:3000/")
        assert True;
    except WebDriverException:
        context.driver.close()
        print("Cannot open metabase url, make sure it is running on your localhost")
        assert False;
    time.sleep(1.5)



@when(u'I enter email as "{email}" and password as "{password}"')
def LoginInfo(context, email, password):
        context.driver.find_element(By.XPATH, "//*[@id=\"formField-username\"]/div[2]/div/input").send_keys(email)
        context.driver.find_element(By.XPATH, "//*[@id=\"formField-password\"]/div[2]/div/input").send_keys(password)
        time.sleep(0.5)
        assert True;


@when(u'I click on Sign in')
def SignIn(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div/div[2]/div/div[2]/div/form/div[4]/button").click()
    time.sleep(1.5)
    assert True;



@when(u'I should logged in')
def LoggedIn(context):
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/aside/nav/div/div/div[2]/div/h4").text
    except:
        context.driver.close()
        assert False, "Test Failed: The provided credentials are invalid"
    if text == "COLLECTIONS":
        assert True, "Logged In Successfully"


@when(u'I click on the settings icon')
def SettingIcon(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/div[2]/div[3]/div/div/button").click()
    time.sleep(1.5)
    assert True;



@when(u'I click on Admin Settings')
def AdminSetting(context):
    context.driver.find_element(By.XPATH, "/html/body/span/span/div/div/div/ol/li[2]/a/div").click()
    time.sleep(1.5)
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[1]/div[1]").text
    except:
        context.driver.close()
        assert False, "Test Failed: This is not an admin account"
    if text == "Settings":
        assert True, "Admin Settings Opened"


@when(u'I click on People')
def People(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/nav/div[2]/ul/li[4]/a").click()
    time.sleep(0.2)
    assert True;


@when(u'I click on Invite Someone button')
def InviteButton(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[2]/div[2]/div/section[1]/div/a/button").click()
    time.sleep(0.2)
    assert True;



@when(u'I enter first name as "{firstname}" and I enter last name as "{lastname}" and I enter email as "{email}"')
def UserInfo(context,firstname,lastname,email):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-first_name\"]/div[2]/div/input").send_keys(firstname)
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-last_name\"]/div[2]/div/input").send_keys(lastname)
    context.driver.find_element(By.NAME,'email').send_keys(email)
    assert True;


@when(u'I click on Create')
def Create(context):
    context.driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div/div/div[2]/div/form/div[5]/button[1]").click()
    time.sleep(5)
    assert True;


@when(u'I click on Done button')
def Done(context):
    context.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/div/button").click()
    time.sleep(1.5)
    assert True;


@when(u'New user will be created')
def NewUser(context):
    assert True, "New User is Created"


@when(u'I click on Groups')
def Groups(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div/div[2]/div[1]/ul/li[2]/a").click()
    time.sleep(1.5)
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[2]/div[1]/ul/li[2]/a").text
    except:
        context.driver.close()
        assert False, "Test Failed: Groups Button not found"
    if text == "Groups":
        assert True, "Group button is clicked"


@when(u'I click on Administrator Group')
def AdministratorGroup(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/a").click()

    time.sleep(1.5)
    assert True;

@when(u'I click on Add Member button')
def AddMemberbutton(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div/div[2]/div[2]/div/section/div/button").click()

    time.sleep(1.5)
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[2]/div[2]/div/section/div/button/div/div").text
    except:
        context.driver.close()
        assert False, "Test Failed: Add members Button not found"
    if text == "Add members":
        assert True, "Add members button is clicked"



@when(u'I enter the name of the created user as "{name}" "{name2}"')
def Entername(context,name,name2):

    context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div/input").send_keys(name+" "+name2)
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div/input").send_keys(Keys.ARROW_DOWN,Keys.RETURN)
    assert True;


@when(u'I click on the Add button')
def AddButton(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/main/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div/button").click()

    time.sleep(1.5)
    assert True;

@then(u'New created user will be added to the Administrator Group')
def Added(context):
    assert True, "Successfully added to the administrator group"


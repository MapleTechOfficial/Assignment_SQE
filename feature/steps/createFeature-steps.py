from behave import *
from selenium import webdriver

@given(u'that I launch the chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that I launch the chrome browser')


@given(u'go to the url http://localhost:8085/')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given go to the url http://localhost:8085/')


@given(u'enter email as "admin@featurehub.com" and password "admin123"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given enter email as "admin@featurehub.com" and password "admin123"')


@given(u'click on Features')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given click on Features')


@given(u'I enter feature name as abcd')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I enter feature name as abcd')


@given(u'I enter feature key as efgh')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I enter feature key as efgh')


@given(u'I enter feature description as xyza')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I enter feature description as xyza')


@given(u'I enter feature Reference Link as defg')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I enter feature Reference Link as defg')


@given(u'I select feature type as String')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I select feature type as String')


@then(u'the feature is Created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the feature is Created')


@then(u'the message saying Feature \'abcd\' created! is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the message saying Feature \'abcd\' created! is displayed')

from behave import *
import time
from Pages.Homepage import Homepage


@when(u'Click on the "Register" button')
def step_impl(context):
    context.homepage = Homepage(context.driver)
    context.homepage.click_register_link()


@then(u'Verify Register for online access screen/page is displayed')
def step_impl(context):
    context.homepage.verify_register_page()


@then(u'Click on "No" button in the field "Do you know your client number"')
def step_impl(context):
    context.homepage.select_client_number_radio_button()


@then(u'Enter Lastname')
def step_impl(context):
    context.homepage.enter_lastname()


@then(u'Date Of birth')
def step_impl(context):
    context.homepage.enter_dob()


@then(u'Email Address')
def step_impl(context):
    context.homepage.enter_email_address()


@then(u'Then click on button "Continue".')
def step_impl(context):
    context.homepage.click_continue()
    time.sleep(5)

import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from Pages.Ourservices import Ourservices
from time import sleep


@given(u'Open the "https://www.hl.co.uk/" website in the Chrome browser.')
def step_impl(context):
    context.ourservices = Ourservices(context.driver)
    context.ourservices.click_accept_cookie()
    allure.attach(context.driver.get_screenshot_as_png(), name='f_screenshot',
                  attachment_type=AttachmentType.PNG)


@when(u'hover the mouse on  "Our Services" and select "Stocks and Shares ISA" from ISA\'s section')
def step_impl(context):
    context.ourservices.mouse_over_menu_item()
    context.ourservices.select_menu_item()
    time.sleep(1)


@then(u'Verify "STOCKS AND SHARES ISA" screen/page is displayed')
def step_impl(context):
    context.ourservices.verify_stock_and_shares_isa_page()


@then(u'Click on "OPEN YOURS STOCKS AND SHARES ISA" link')
def step_impl(context):
    context.ourservices.click_openyourstocksandsharesisa()


@then(u'Verify "Stocks and Shares ISA Application" screen/page is displayed')
def step_impl(context):
    context.ourservices.verify_stock_shares_app_page()


@then(u'Scroll Down the page and  Click on the "OPEN YOUR ISA NOW" link.')
def step_impl(context):
    context.ourservices.click_openyourisa_button()


@then(u'Enter the data in name fields under the  "Your detail" section.')
def step_impl(context):
    context.ourservices.enter_name()


@then(u'Enter DOB')
def step_impl(context):
    context.ourservices.enter_dob()


@then(u'Enter Nationality')
def step_impl(context):
    context.ourservices.select_nationality()


@then(u'Enter House number')
def step_impl(context):
    context.ourservices.enter_house_no()


@then(u'Enter Postcode')
def step_impl(context):
    context.ourservices.enter_postcode()
    context.ourservices.click_findmyaddress()


@then(u'Enter email address')
def step_impl(context):
    context.ourservices.enter_emailid()


@then(u'Enter Main Telephone Number')
def step_impl(context):
    context.ourservices.enter_phone_no()


@then(u'Select \'Where did you hear about us\'')
def step_impl(context):
    context.ourservices.select_source()


@then(u'Select Select the Add cash option  in the "Add Money"  section.')
def step_impl(context):
    context.ourservices.select_add_money()


@then(u'select the phone check box in the "Personal data" section')
def step_impl(context):
    context.ourservices.select_comm_personal_data()


@then(u'Click on "Open My ISA" button .')
def step_impl(context):
    context.ourservices.click_openmyisa()
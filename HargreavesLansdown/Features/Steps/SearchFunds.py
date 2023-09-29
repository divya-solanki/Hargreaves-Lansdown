import time
from Pages.Funds import Funds
from behave import *


@when(u'Click on Funds')
def step_impl(context):
    context.funds = Funds(context.driver)
    context.funds.click_funds_link()


@then(u'Select "UK Gilt" checkbox from the  Dropdown "sector".')
def step_impl(context):
    context.funds.select_value_from_sector_dropdown()


@then(u'Select the checkbox "Income" from the Dropdown "Unit type"')
def step_impl(context):
    context.funds.select_value_from_unit_type_dropdown()


@then(u'Select the checkbox "Tracker" from the Dropdown "Fund type"')
def step_impl(context):
    context.funds.select_value_from_fund_type_dropdown()


@then(u'Select the Ongoing charge(OCF/TER)  and Yield fields from the ""More filters"" Dropdown')
def step_impl(context):
    context.funds.select_value_from_more_filter_dropdown()



@then(u'Click on the "Show Results" button.')
def step_impl(context):
    context.funds.click_search_button()
    time.sleep(5)

@then(u'Verify results are displayed')
def step_impl(context):
    context.funds.verify_results()


@then(u'From the results displayed below, click on "VIEW FUND" button')
def step_impl(context):
    context.funds.view_funds()


@then(u'Verify Fund page/screen is displayed')
def step_impl(context):
    context.funds.verify_fund_page()

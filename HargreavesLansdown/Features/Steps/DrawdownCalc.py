import time

from behave import *
from Pages.Pension import Pension


@when(u'Hover the mouse on "Pensions" menu')
def step_impl(context):
    context.pension = Pension(context.driver)
    context.pension.mouse_over_pension()


@then(u'Select "Drawdown calculator" under the "Drawdown" section')
def step_impl(context):
    context.pension.click_on_drawndown_calc()


@then(u'"Enter the data in the fields below under the ""Your detail"" section.')
def step_impl(context):
    pass


@then(u'Enter Date of birth')
def step_impl(context):
    context.pension.enter_dob()


@then(u'Enter Your existing pension fund')
def step_impl(context):
    context.pension.enter_amount()


@then(u'Enter Required monthly income(before tax)')
def step_impl(context):
    context.pension.enter_req_monthly_income()


@then(u'Enter Tax free cash')
def step_impl(context):
    context.pension.enter_tax_free_cash()


@then(u'select the gender"')
def step_impl(context):
    context.pension.select_gender()


@then(u'Click on the "Calculate" button')
def step_impl(context):
    context.pension.click_calculate()


@then(u'Verify "Your drawdown forecast" screen/page is displayed')
def step_impl(context):
    context.pension.verify_your_drawdown_forcast_page()


@then(u'Verify the "Investement Growth" and "Average Fund Charge" fields values.')
def step_impl(context):
    context.pension.verify_investment_growth_field_values()
    context.pension.verify_average_fund_charges_field_value()


@then(u'Verify whether the graph is visible then, hover the mouse on the graph and capture the tooltip.')
def step_impl(context):

    context.pension.verify_graph()
    context.pension.hover_mouse_on_graph()
    time.sleep(5)
    #context.pension.verify_tooltip()

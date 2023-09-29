import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Utilities.CommonFunction import CommonFunction


class Pension:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_pensions = (By.LINK_TEXT, 'Pensions')
    locator_drawdown_calc = (By.XPATH, "//a[contains(text(), 'Drawdown calculator')]")
    locator_verify_pension_drawdown_calc = (By.XPATH, "//h1[1]")
    locator_dob_date = (By.XPATH, "//input[@placeholder='dd']")
    locator_dob_month = (By.XPATH, "//input[@placeholder='mm']")
    locator_dob_year = (By.XPATH, "//input[@placeholder='yyyy']")
    locator_amount = (By.ID, "existing_pension_fund")
    locator_req_monthly_income = (By.ID, "required_monthly_income")
    locator_tax_free_cash = (By.XPATH, "//div[@id='iDForm']/div[4]/div/div[2]/input")
    locator_gender = (By.XPATH, "//div[@class='row -radioSameLine']/div[2]/label")
    locator_calc_button = (By.ID, "calcBtn")
    locator_verify_your_drwdown_forcast_page = (By.XPATH, "//div[@id= 'results-life-desktop']/div/h2")
    locator_investment_growth = (By.XPATH, "(//div[@id='resultsDiv']/div[4]/div/div/div/div[2]/input)[1]")
    locator_average_fund_charge = (By.XPATH, "(//div[@id='resultsDiv']/div[4]/div/div/div/div[2]/input)[2]")
    locator_graph = (By.XPATH, "//*[name() = 'svg'](//*[name()='rect'])[2]")
    locator_tooltip = (By.XPATH, "//*[name() = 'svg']//*[local-name()='g' and @class ='highcharts-tooltip' ]")

    def mouse_over_pension(self):
        self.cf.wait_and_hover(self.locator_pensions)

    def click_on_drawndown_calc(self):
        self.cf.wait_and_click(self.locator_drawdown_calc)

    def verify_drawdown_page(self):
        self.cf.verify_page(self.locator_verify_pension_drawdown_calc, "PENSION DRAWDOWN CALCULATOR")

    def enter_dob(self):
        self.cf.wait_and_input_text(self.locator_dob_date, "10")
        self.cf.wait_and_input_text(self.locator_dob_month, "08")
        self.cf.wait_and_input_text(self.locator_dob_year, "1960")

    def enter_amount(self):
        self.cf.wait_and_input_text(self.locator_amount, "80000")

    def enter_req_monthly_income(self):
        self.cf.wait_and_input_text(self.locator_req_monthly_income, "1200")

    def enter_tax_free_cash(self):
        self.cf.clear_text_field(self.locator_tax_free_cash)
        self.cf.wait_and_input_text(self.locator_tax_free_cash, "20")
        time.sleep(2)

    def select_gender(self):
        self.cf.wait_and_click(self.locator_gender)

    def click_calculate(self):
        self.cf.wait_and_click(self.locator_calc_button)

    def verify_your_drawdown_forcast_page(self):
        self.cf.verify_page(self.locator_verify_your_drwdown_forcast_page, "Your drawdown forecast")

    def verify_investment_growth_field_values(self):
        text = self.cf.get_value_from_text_field(self.locator_investment_growth)
        assert int(text) == 5

    def verify_average_fund_charges_field_value(self):
        text = self.cf.get_value_from_text_field(self.locator_average_fund_charge)
        assert float(text) == 0.55

    def verify_graph(self):
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.cf.verify_image_present(self.locator_graph)

    def hover_mouse_on_graph(self):
         self.cf.wait_and_hover(self.locator_graph)

    def verify_tooltip(self):
        self.cf.verify_image_present(self.verify_tooltip())

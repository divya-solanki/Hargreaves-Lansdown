import time
from selenium.webdriver.common.by import By
from Utilities.CommonFunction import CommonFunction


class Funds:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_funds_link = (By.LINK_TEXT, "Funds")
    locator_sector_dropdown = (By.XPATH, "//div[@id = 'fund-search']/div/div[2]/button")
    locator_sector_dropdown_value = (By.XPATH, "//li/label[@for='UK Gilt']")
    locator_sector_dropdown_save_button = (By.XPATH, "//div[@id = 'fund-search']/div/div[2]/div/div[2]/button[2]")

    locator_unit_type_dropdown = (By.XPATH, "//div[@id = 'fund-search']/div/div[3]/button")
    locator_unit_type_dropdown_value = (By.XPATH, "//li/label[@for='Income']")
    locator_unit_type_dropdown_save_button = (By.XPATH, "//div[@id = 'fund-search']/div/div[3]/div/div[2]/button[2]")

    locator_fund_type_dropdown = (By.XPATH, "//div[@id = 'fund-search']/div/div[4]/button")
    locator_fund_type_dropdown_value = (By.XPATH, "//li/label[@for='Tracker']")
    locator_fund_type_dropdown_save_button = (By.XPATH, "//div[@id = 'fund-search']/div/div[4]/div/div[2]/button[2]")

    locator_more_filters_dropdown = (By.XPATH, "//div[@id = 'fund-search']/div/div[7]/button")
    locator_ongoing_charge_dropdown_value = (By.XPATH, "//li/label[@for='<0.5%']")
    locator_yield_dropdown_value = (By.XPATH, "//li/label[@for='3%-4%']")
    locator_more_filters_dropdown_save_button = (By.XPATH, "//div[@id = 'fund-search']/div/div[7]/div/div/div["
                                                           "3]/div/button[2]")

    locator_search_result_button = (By.XPATH, "//a[@class='actionButton__button']")
    locator_verify_results = (By.XPATH, "//h1[@class='main']")

    locator_view_funds_button = (By.XPATH, "//table[@class = 'results__table']/tbody/tr/td[5]/a")
    locator_view_fund_name1 = (By.XPATH, "//table[@class = 'results__table']/tbody/tr/td/a")
    locator_view_fund_name2 = (By.XPATH, "//table[@class = 'results__table']/tbody/tr[1]/td/span/span/span")
    locator_verify_fund_page = (By.XPATH, "//ul[@class = 'breadcrumb__list']/li[3]")
    name = ""

    def click_funds_link(self):
        self.cf.wait_and_click(self.locator_funds_link)

    def select_value_from_sector_dropdown(self):
        self.cf.wait_and_click(self.locator_sector_dropdown)
        self.cf.wait_and_scroll_down(self.locator_sector_dropdown_value)
        self.cf.wait_and_click(self.locator_sector_dropdown_value)
        self.cf.wait_and_scroll_down(self.locator_sector_dropdown_save_button)
        self.cf.wait_and_click(self.locator_sector_dropdown_save_button)
        time.sleep(2)
        self.cf.wait_and_scroll_up()

    def select_value_from_unit_type_dropdown(self):
        self.cf.wait_and_click(self.locator_unit_type_dropdown)
        self.cf.wait_and_click(self.locator_unit_type_dropdown_value)
        self.cf.wait_and_click(self.locator_unit_type_dropdown_save_button)
        time.sleep(2)

    def select_value_from_fund_type_dropdown(self):
        self.cf.wait_and_click(self.locator_fund_type_dropdown)
        self.cf.wait_and_click(self.locator_fund_type_dropdown_value)
        self.cf.wait_and_click(self.locator_fund_type_dropdown_save_button)
        time.sleep(2)

    def select_value_from_more_filter_dropdown(self):
        self.cf.wait_and_click(self.locator_more_filters_dropdown)
        self.cf.wait_and_click(self.locator_ongoing_charge_dropdown_value)
        self.cf.wait_and_scroll_down(self.locator_yield_dropdown_value)
        self.cf.wait_and_click(self.locator_yield_dropdown_value)
        self.cf.wait_and_click(self.locator_more_filters_dropdown_save_button)

    def click_search_button(self):
        self.cf.wait_and_click(self.locator_search_result_button)

    def verify_results(self):
        self.cf.verify_page(self.locator_verify_results, "FUND FINDER")

    def view_funds(self):
        fund_name_1 = self.cf.find_web_element(self.locator_view_fund_name1)

        fund_name_2 = self.cf.find_web_element(self.locator_view_fund_name2)

        self.name = fund_name_1.text + " " + fund_name_2.text
        self.cf.wait_and_click(self.locator_view_funds_button)

    def verify_fund_page(self):
        self.cf.verify_page(self.locator_verify_fund_page, self.name)

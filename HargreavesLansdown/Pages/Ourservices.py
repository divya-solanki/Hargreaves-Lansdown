import time

from selenium.webdriver.common.by import By
from Utilities.CommonFunction import CommonFunction



class Ourservices:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_ourservices = (By.LINK_TEXT, 'Our services')
    locator_stocks_and_shares_ISA = (By.XPATH, "//a[contains(text(), 'Stocks and Shares ISA')]")
    locator_verify_stocksandsharesISA = (By.XPATH, "//h1[1]")
    locator_openyourstocksandsharesisa_link = (By.XPATH, "//div[@class='heroPullout__content']/p/a[@class = 'buttonPrimaryCta']")
    locator_verify_stocksandsharesISA_app = (By.XPATH, "//h1[1]")
    locator_openyourisanow_button = (By.ID, "applicationCta")
    locator_title = (By.ID, "fldTitle")
    locator_firstname = (By.ID, "fldForenames")
    locator_lastname = (By.ID, "fldSurname")
    locator_dob_day = (By.ID, "fldDob_Day")
    locator_dob_month = (By.ID, "fldDob_Month")
    locator_dob_year = (By.ID, "fldDob_Year")
    locator_nat_insurance = (By.ID, "fldNino")
    locator_nationality = (By.ID, "GB")
    locator_house_no = (By.ID, "fldHouse")
    locator_postcode = (By.ID, "fldPostcode")
    locator_email = (By.ID, "fldEmail")
    locator_telephone_no = (By.NAME, "fldTel_eve")
    locator_source = (By.ID, "fldSource")
    locator_add_money = (By.ID, "fldInvest_method_lump")
    locator_personal_data = (By.ID, "No_Phone")
    locator_openmyisa_button = (By.XPATH, "//a[@id='next']")
    locator_findmyaddress = (By.NAME, "find-address")
    locator_transaction_amt = (By.ID, "fldTransaction_amount")
    locator_card_no = (By.ID, "stripe-card-number")
    locator_exp_date = (By.NAME, "exp-date")
    locator_cvc = (By.ID, "stripe-card-cvc")
    locator_accept_cookie = (By.ID, "acceptCookieButton")

    def click_accept_cookie(self):
        self.cf.wait_and_click(self.locator_accept_cookie)

    def mouse_over_menu_item(self):
        self.cf.wait_and_hover(self.locator_ourservices)

    def select_menu_item(self):
        self.cf.wait_and_click(self.locator_stocks_and_shares_ISA)

    def verify_stock_and_shares_isa_page(self):
        self.cf.verify_page(self.locator_verify_stocksandsharesISA, "STOCKS AND SHARES ISA")

    def click_openyourstocksandsharesisa(self):
        self.cf.wait_and_click(self.locator_openyourstocksandsharesisa_link)

    def verify_stock_shares_app_page(self):
        self.cf.verify_page(self.locator_verify_stocksandsharesISA_app, "OPEN A STOCKS AND SHARES ISA")

    def click_openyourisa_button(self):
        self.cf.wait_and_click(self.locator_openyourisanow_button)

    def enter_name(self):
        self.cf.wait_and_click(self.locator_title)
        self.cf.wait_and_select_from_dropdown(self.locator_title, "Dr")
        self.cf.wait_and_input_text(self.locator_firstname, "Jordan")
        self.cf.wait_and_input_text(self.locator_lastname, "Evans")

    def enter_dob(self):
        self.cf.wait_and_click(self.locator_dob_day)
        self.cf.wait_and_select_from_dropdown(self.locator_dob_day, "10")
        self.cf.wait_and_click(self.locator_dob_month)
        self.cf.wait_and_select_from_dropdown(self.locator_dob_month, "July")
        self.cf.wait_and_click(self.locator_dob_year)
        self.cf.wait_and_select_from_dropdown(self.locator_dob_year, "2000")

    def enter_national_insurance(self):
        self.cf.wait_and_input_text(self.locator_nat_insurance, "JD45698A")

    def select_nationality(self):
        self.cf.wait_and_click(self.locator_nationality, "GB")

    def enter_house_no(self):
        self.cf.wait_and_input_text(self.locator_house_no, "6")

    def enter_postcode(self):
        self.cf.wait_and_input_text(self.locator_postcode, "GL56 0AJ")

    def click_findmyaddress(self):
        self.cf.wait_and_click(self.locator_findmyaddress)

    def enter_emailid(self):
        email_add = self.cf.random_email()
        self.cf.wait_and_input_text(self.locator_email, email_add)

    def enter_phone_no(self):
        self.cf.wait_and_input_text(self.locator_telephone_no, "07828548210")

    def select_source(self):
        self.cf.wait_and_select_from_dropdown(self.locator_source, "Advert On Another Website")

    def select_add_money(self):
        self.cf.wait_and_click(self.locator_add_money)
        self.cf.wait_and_input_text(self.locator_transaction_amt, "100")
        # self.cf.wait_and_input_text(self.locator_card_no, "7845658912547412")
        # self.cf.wait_and_input_text(self.locator_exp_date, "0325")
        # self.cf.wait_and_input_text(self.locator_cvc, "021")
        time.sleep(2)

    def select_comm_personal_data(self):
        self.cf.wait_and_click(self.locator_personal_data)

    def click_openmyisa(self):
        self.cf.wait_and_click(self.locator_openmyisa_button)
        time.sleep(5)

import time
from selenium.webdriver.common.by import By
from Utilities.CommonFunction import CommonFunction


class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_register_link = (By.LINK_TEXT, "Register")
    locator_verify_register_page = (By.TAG_NAME, "h1")
    locator_client_number_button = (By.XPATH, "//label[@for='clientno_no']")
    locator_last_name = (By.ID, "surname")
    locator_dob = (By.ID, "date-of-birth-alternative")
    locator_email = (By.ID, "email")
    locator_continue = (By.ID, "submit")

    def click_register_link(self):
        self.cf.wait_and_click(self.locator_register_link)

    def verify_register_page(self):
        self.cf.verify_page(self.locator_verify_register_page, "Register for online access")

    def select_client_number_radio_button(self):
        self.cf.wait_and_click(self.locator_client_number_button)

    def enter_lastname(self):
        self.cf.wait_and_input_text(self.locator_last_name, "Smith")

    def enter_dob(self):
        self.cf.wait_and_input_text(self.locator_dob, "031290")

    def enter_email_address(self):
        email = self.cf.random_email()
        self.cf.wait_and_input_text(self.locator_email, email)

    def click_continue(self):
        self.cf.wait_and_click(self.locator_continue)
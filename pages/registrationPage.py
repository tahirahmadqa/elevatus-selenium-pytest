import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils
import softest

class RegistrationPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    firstname_field = "firstName"
    lastname_field = "lastName"
    email_field = "email"
    password_field = "password"
    confirm_password_field = "confirmPassword"
    phone_number_field = "//input[@placeholder='Phone number']"
    privacy_policy_checkbox = "//span[contains(text(), 'I have read and agree to the')]"
    signup_btn = "//button[contains(text(),'Sign up')]"
    registered_successfully_lbl = "//div[contains(text(),'Registered successfully')]"

    # get funtions
    def get_firstname_field(self):
        return self.driver.find_element(By.NAME, self.firstname_field)

    def get_lastname_field(self):
        return self.driver.find_element(By.NAME, self.lastname_field)

    def get_email_field(self):
        return self.driver.find_element(By.NAME, self.email_field)

    def get_password_field(self):
        return self.driver.find_element(By.NAME, self.password_field)

    def get_confirm_password_field(self):
        return self.driver.find_element(By.NAME, self.confirm_password_field)

    def get_phone_number_field(self):
        return self.driver.find_element(By.XPATH, self.phone_number_field)

    def get_privacy_policy_checkbox(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_checkbox)

    def get_signup_button(self):
        return self.driver.find_element(By.XPATH, self.signup_btn)

    def get_registered_successfully_lbl(self):
        return self.driver.find_element(By.XPATH, self.registered_successfully_lbl)

    #set functions
    def enter_in_firstname_field(self, name):
        BaseDriver.element_is_displayed(self, By.NAME, self.firstname_field)
        self.get_firstname_field().send_keys(name)

    def enter_in_lastname_field(self, name):
        BaseDriver.element_is_displayed(self, By.NAME, self.lastname_field)
        self.get_lastname_field().send_keys(name)

    def enter_in_email_field(self, email):
        BaseDriver.element_is_displayed(self, By.NAME, self.email_field)
        self.get_email_field().send_keys(email)

    def enter_in_password_field(self, password):
        BaseDriver.element_is_displayed(self, By.NAME, self.password_field)
        self.get_password_field().send_keys(password)

    def enter_in_confirm_password_field(self, password):
        BaseDriver.element_is_displayed(self, By.NAME, self.confirm_password_field)
        self.get_confirm_password_field().send_keys(password)

    def enter_in_phone_number_field(self, phone):
        BaseDriver.element_is_displayed(self, By.XPATH, self.phone_number_field)
        self.get_phone_number_field().send_keys(phone)

    def check_privacy_policy_checkbox(self):
        self.get_privacy_policy_checkbox().click()

    def click_signup_button(self):
        self.get_signup_button().click()

    #test functions
    def verify_signup_button_is_disabled(self):
        BaseDriver.verify_element_has_class_disabled(self, By.XPATH, self.signup_btn)

    def verify_signup_button_is_enabled(self):
        BaseDriver.verify_element_is_enabled(self, By.XPATH, self.signup_btn)

    def verify_registration_is_successful(self):
        BaseDriver.element_is_displayed(self, By.XPATH, self.registered_successfully_lbl)
        result = self.get_registered_successfully_lbl().text
        Utils.assert_text(self, result, "Registered successfully")
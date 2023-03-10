import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class LoginPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    email_field = "email"
    password_field = "password"
    signin_btn = "//button[contains(text(),'Sign in')]"
    fill_manually_btn = "//button[contains(text(),'Fill in manually')]"

    #get functions
    def get_email_field(self):
        return self.driver.find_element(By.NAME, self.email_field)

    def get_password_field(self):
        return self.driver.find_element(By.NAME, self.password_field)

    def get_signin_button(self):
        return self.driver.find_element(By.XPATH, self.signin_btn)

    def get_fill_manually_button(self):
        return self.driver.find_element(By.XPATH, self.fill_manually_btn)

    #set functions
    def enter_in_email_field(self, email):
        BaseDriver.element_is_displayed(self, By.NAME, self.email_field)
        self.get_email_field().send_keys(email)

    def enter_in_password_field(self, password):
        BaseDriver.element_is_displayed(self, By.NAME, self.password_field)
        self.get_password_field().send_keys(password)

    def click_signin_button(self):
        self.get_signin_button().click()

    def click_fill_manually_button(self):
        BaseDriver.wait_until_element_is_clickable(self, By.XPATH, self.fill_manually_btn)
        self.get_fill_manually_button().click()
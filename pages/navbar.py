import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class Navbar(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    register_btn = "//span[contains(text(),'Register')]"
    jobs_lbl = "//div[contains(text(),'Jobs')]"

    #get functions
    def get_register_button(self):
        return self.driver.find_element(By.XPATH, self.register_btn)

    def get_jobs_lbl(self):
        return self.driver.find_element(By.XPATH, self.jobs_lbl)

    #set functions
    def click_register_button(self):
        self.get_register_button().click()

    def click_jobs_lbl(self):
        self.get_jobs_lbl().click()
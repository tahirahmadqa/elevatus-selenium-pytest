import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class JobListingPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_card_view_btn = "//span[contains(text(),'View')][1]"

    #get functions
    def get_first_card_view_button(self):
        return self.driver.find_element(By.XPATH, self.first_card_view_btn)

    #set functions
    def click_first_card_view_button(self):
        BaseDriver.wait_until_element_is_clickable(self, By.XPATH, self.first_card_view_btn)
        self.get_first_card_view_button().click()
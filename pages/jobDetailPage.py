import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class JobDetailPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    apply_btn = "//span[contains(text(),'Apply')]"

    #get functions
    def get_apply_button(self):
        return self.driver.find_element(By.XPATH, self.apply_btn)

    #set functions
    def click_apply_button(self):
        BaseDriver.scroll_element_to_middle(self, By.XPATH, self.apply_btn)
        BaseDriver.wait_until_element_is_clickable(self, By.XPATH, self.apply_btn)
        self.get_apply_button().click()
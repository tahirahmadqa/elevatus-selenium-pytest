import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class CookieDrawer(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    accept_cookies_btn = "//button[contains(text(),'I Accept Recommended Cookies')]"

    #get functions
    def get_accept_cookies_button(self):
        return self.driver.find_element(By.XPATH, self.accept_cookies_btn)

    #set functions
    def click_accept_cookies_button(self):
        self.driver.find_element(By.XPATH, self.accept_cookies_btn).click()

    #test functions
    def accept_cookies_btn_is_displayed(self):
        return BaseDriver.element_is_displayed(By.XPATH, self.accept_cookies_btn)

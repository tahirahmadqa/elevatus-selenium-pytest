import logging
import time
import os
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class SubmitYourCvPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    general_field = "description"
    date_of_birth = "date-picker-dialog"
    gender_drpdwn = "gender"
    nationality_drpdwn = "nationality"
    address_field = "address"
    city_field = "city"
    country_drpdwn = "location.country_uuid"
    right_to_work_drpdwn = "right_to_work.country_uuid"
    document_type_drpdwn = "//input[@placeholder ='Document type']"
    job_type_drpdwn = "job_types"
    willing_to_travel_drpdwn = "//input[@placeholder ='Are you willing to travel?']"
    willing_to_relocate_drpdwn = "//input[@placeholder ='Are you willing to relocate?']"
    own_a_vehicle_drpdwn = "//input[@placeholder ='Do you own a vehicle?']"
    upload_cv_field = "//*[@id='basic-info']/div[2]/div/div[12]/div/div/div/input"
    experience_lbl = "//strong[contains(text(), 'Experience')]"
    submit_btn = "//span[contains(text(),'Submit')]"

    #get functions
    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, self.submit_btn)

    def get_date_of_birth_field(self):
        return self.driver.find_element(By.ID, self.date_of_birth)

    def get_gender_dropdown(self):
        return self.driver.find_element(By.ID, self.gender_drpdwn)

    def get_nationality_dropdown(self):
        return self.driver.find_element(By.ID, self.nationality_drpdwn)

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, self.submit_btn)

    def get_upload_cv_field(self):
        return self.driver.find_element(By.XPATH, self.upload_cv_field)

    def get_experience_label(self):
        return self.driver.find_element(By.XPATH, self.experience_lbl)

    #set functions
    def click_apply_button(self):
        BaseDriver.scroll_element_to_middle(self, By.XPATH, self.submit_btn)
        BaseDriver.wait_until_element_is_clickable(self, By.XPATH, self.submit_btn)
        self.get_submit_button().click()

    def enter_in_date_of_birth_field(self, dateOfBirth):
        BaseDriver.wait_until_element_is_clickable(self, By.ID, self.date_of_birth)
        self.get_date_of_birth_field().send_keys(dateOfBirth)

    def select_first_gender(self):
        BaseDriver.wait_until_element_is_clickable(self, By.ID, self.gender_drpdwn)
        self.get_gender_dropdown().click()
        self.get_gender_dropdown().send_keys("female")
        self.get_gender_dropdown().send_keys(Keys.RETURN)

    def select_first_nationality(self):
        BaseDriver.wait_until_element_is_clickable(self, By.ID, self.nationality_drpdwn)
        self.get_nationality_dropdown().click()
        self.get_nationality_dropdown().send_keys("Saudi Arabia")
        self.get_nationality_dropdown().send_keys(Keys.RETURN)

    def upload_cv(self):
        BaseDriver.scroll_element_into_view(self, By.XPATH, self.experience_lbl)
        #file_path = os.path.abspath("//assets//TahirAhmad-QAE.pdf")
        self.get_upload_cv_field().send_keys(os.getcwd()+"/assets/TahirAhmad-QAE.pdf")

    def click_submit_button(self):
        BaseDriver.wait_until_element_is_clickable(self, By.XPATH, self.submit_btn)
        BaseDriver.scroll_element_into_view(self, By.XPATH, self.submit_btn)
        self.get_submit_button().click()
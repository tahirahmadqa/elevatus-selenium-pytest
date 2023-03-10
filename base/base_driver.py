import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        print("Element: " + locator + " is visible")
        return element

    def element_is_displayed(self, locator_type, locator):
        element = self.wait_until_element_is_visible(locator_type, locator)
        if element.is_displayed():
            assert element.is_displayed()
            print("Element: " + locator + " is displayed")
            return True
        else:
            return False

    def verify_element_is_disabled(self, locator_type, locator):
        element = self.wait_until_element_is_visible(locator_type, locator)
        if element.is_disabled():
            assert element.is_disabled()
            print("Element: " + locator + " is disabled")
            return True
        else:
            return False

    def verify_element_is_enabled(self, locator_type, locator):
        element = self.wait_until_element_is_visible(locator_type, locator)
        if element.is_enabled():
            assert element.is_enabled()
            print("Element: " + locator + " is enabled")
            return True
        else:
            return False

    def verify_element_has_class_disabled(self, locator_type, locator):
        element = self.wait_until_element_is_visible(locator_type, locator)
        class_attribute = element.get_attribute('class')
        assert 'disabled' in class_attribute
        print("Element: " + locator + " has class 'disabled'")

    def scroll_element_into_view(self, locator_type, locator):
        element = self.wait_until_element_is_visible(locator_type, locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(2)

    def scroll_element_to_middle(self, locator_type, locator):
        element = self.wait_until_element_is_visible(locator_type, locator)
        element_location = element.location_once_scrolled_into_view
        window_size = self.driver.execute_script("return window.innerHeight")
        middle_of_window = window_size/2
        scroll_offset = element_location['y'] - middle_of_window
        actions = AC(self.driver)
        actions.move_by_offset(0, scroll_offset)
        actions.perform()
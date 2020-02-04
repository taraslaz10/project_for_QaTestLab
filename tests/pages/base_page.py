import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = os.getenv('TEST_BASE_URL', 'https://www.booking.com/')


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element_by_xpath(self, element_xpath):
        """Method for finding element on the page"""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

    def click_on_element_by_xpath(self, element_xpath):
        """Method for clicking on the element"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()

    def clear_text_field_by_xpath(self, element_xpath):
        """Method for clearing the text field"""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath))).clear()

    def fill_in_text_field_by_xpath(self, element_xpath, text):
        """Method for filling in the text field with text"""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath))).send_keys(text)

    def wait_for_url(self, element_url):
        """Method for waiting for url to be as parameter what it takes (element-url)"""
        self.wait.until(EC.url_to_be(element_url))

    def base_url(self):
        return EC.url_to_be(BASE_URL)

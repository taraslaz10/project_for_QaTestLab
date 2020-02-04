from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
import re

from pages import base_page
from pages.base_page import BasePage

"""X-paths for hotel reservation page """
HOTELS_XPATH = '//*[@id="ajaxsrwrap"]'
CALENDAR_CSS_CLASS = '.c2-calendar-viewport'
FIRST_SHOW_PRICES_XPATH = '//div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/a'
FEBRUARY_7_XPATH = '//div[2]/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]'
FIRST_DIV_BODY = '/html/body/div[3]/div/div[3]/div[3]/div[1]/div[7]/div[3]/div[1]/div/div[2]/div[2]/div[1]'
FEBRUARY_5_XPATH = '//form/div[3]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[3]/div/div/div[2]/table/tbody/tr[2]/td[3]'
SUBMIT_BUTTON_XPATH = '/html/body/div[3]/div/div[3]/div[3]/div[2]/div[1]/div[1]/form/div[5]/div[2]/button'
FIVE_MARCH_CSS_CLASS = 'div.c2-month:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4)'

class HotelReservation(BasePage):
    
    def check_visibility_hotels(self):
        try: 
            self.find_element_by_xpath(HOTELS_XPATH)
            return True
        except:
            return False

    def click_on_first_show_prices(self):
        self.click_on_element_by_xpath(FIRST_SHOW_PRICES_XPATH)

    def click_on_7_February(self):
        calendar_div = self.find_element_by_xpath(CALENDAR_XPATH)
        move_to_element_with_offset(calendar_div, 30, 30)
    
    def check_is_exist_uah_in_first_div(self, src):
        try:    
            text_found = re.search(r'UAH', src)
            return True
        except:
            return False

    def check_is_exist_missed_message_in_first_div(self, src):
        try:    
            text_found = re.search(r'You missed it!', src)
            return True
        except:
            return False

    def click_on_5_march_by_js(self):
        menu = self.driver.find_element_by_css_selector(CALENDAR_CSS_CLASS)
        hidden_submenu = self.driver.find_element_by_css_selector(FIVE_MARCH_CSS_CLASS)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.click(hidden_submenu)
        actions.perform()

    def is_calendar_exist(self):
        try:
            menu = self.driver.find_element_by_css_selector(CALENDAR_CSS_CLASS)
            actions = ActionChains(self.driver)
            actions.move_to_element(menu)
            actions.perform()
            return True
        except:
            return False

    def click_on_submit_button(self):
        self.click_on_element_by_xpath(SUBMIT_BUTTON_XPATH)

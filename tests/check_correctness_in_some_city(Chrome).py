import unittest
import time
from selenium import webdriver

from pages import home_page as hp
from pages import base_page as bp
from pages import hotel_reservation as hr


class CheckNumberOfChilds(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.hotel_page = hr.HotelReservation(self.driver)
        self.home_page.go_to()
        self.driver.implicitly_wait(30)
        self.home_page.go_to_Warsaw_city()
        self.driver.implicitly_wait(40)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
    
    def test_check_visibility_of_hotels_list(self):
        boolean = self.hotel_page.check_visibility_hotels()
        self.assertTrue(boolean)

    def test_check_visibility_of_calendar(self):
        boolean = self.hotel_page.is_calendar_exist()
        self.assertTrue(boolean)

    def test_check_calendar_after_click_show_prices(self):
        self.hotel_page.click_on_5_march_by_js()
        self.hotel_page.click_on_first_show_prices()
        self.driver.implicitly_wait(40)
        boolean = self.hotel_page.is_calendar_exist()
        self.assertTrue(boolean)
        
    def test_is_exist_price_in_div(self):
        self.hotel_page.click_on_5_march_by_js()
        self.hotel_page.click_on_submit_button()
        src = self.driver.page_source
        boolean = self.hotel_page.check_is_exist_uah_in_first_div(src)
        self.assertTrue(boolean)

    def test_is_exist_missed_message_in_div(self):
        self.hotel_page.click_on_5_march_by_js()
        self.hotel_page.click_on_submit_button()
        src = self.driver.page_source
        boolean = self.hotel_page.check_is_exist_missed_message_in_first_div(src)
        self.assertTrue(boolean) 

if __name__ == "__main__":
    unittest.main(verbosity=2)

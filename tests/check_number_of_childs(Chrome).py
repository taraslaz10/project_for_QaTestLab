import unittest

from selenium import webdriver

from pages import home_page as hp
from pages import base_page as bp

class CheckNumberOfChilds(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_check_number_of_childs(self):
        self.home_page.go_to()
        self.home_page.click_on_passangers_button()
        self.home_page.add_childs(3)
        count_of_childs = self.home_page.get_count_of_childs()
        self.assertTrue(3 , count_of_childs)

if __name__ == "__main__":
    unittest.main(verbosity=2)

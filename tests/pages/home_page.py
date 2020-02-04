from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from pages import base_page
from pages.base_page import BasePage


"""X-paths for home page """
PASSANGERS_BUTTON_XPATH = '//*[@id="xp__guests__toggle"]'
ADD_ONE_CHILD_XPATH = '/html/body/div[3]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/button[2]'
LABEL_COUNT_OF_CHILDS_XPATH = '/html/body/div[3]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/span[1]'
FIRST_CITY_XPATH = '/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div/h3/a'
FIRST_DIV_CITY_XPATH = '/html/body/div[4]/div/div[1]/div[2]/div[2]'
SEARCH_XPATH = '//*[@id="ss"]'
BUTTON_SEARCH_XPATH = '/html/body/div[3]/div/div/div[2]/form/div[1]/div[4]/div[2]/button'

class HomePage(BasePage):

    def go_to(self):
        """Method for redirecting on the home page"""
        self.driver.get(base_page.BASE_URL)

    def click_on_passangers_button(self):
        self.click_on_element_by_xpath(PASSANGERS_BUTTON_XPATH)

    def add_childs(self, number):
        i = 0 
        while(i < number):
            self.click_on_element_by_xpath(ADD_ONE_CHILD_XPATH)
            i += 1

    def get_count_of_childs(self):
        return self.find_element_by_xpath(LABEL_COUNT_OF_CHILDS_XPATH).text

    def go_to_Warsaw_city(self):
        self.clear_text_field_by_xpath(SEARCH_XPATH)
        self.fill_in_text_field_by_xpath(SEARCH_XPATH, 'Warsaw')
        self.click_on_element_by_xpath(BUTTON_SEARCH_XPATH)

    """
    def pick_first_city(self):
        body_div = self.driver.find_element_by_css_selector('#b2indexPage')
        first_div = self.driver.find_element_by_css_selector('div.lp_flexible_layout_content_wrapper:nth-child(1)')
        first_city_div = self.driver.find_element_by_css_selector('html.b_firefox.b_firefox_69.supports_inline-block.supports_flexbox_unprefixed.supports_fontface.supports_hyphens.hasJS.gr__booking_com body#b2indexPage.bookings2.b2.index.en.lang_is_ltr.header_reshuffle.no_bg_img.nobg.user_center.app_user_center.landing.lp_flexible_layout.sb_gradient_border.b-sprite-3.bigblue_std_sm.bigblue_std_lg.lp_body_constraint_static.sb_can_have_advanced_search.system-font.iq-x-bar.iq-x-bar-new.iq-xp-sb div#bodyconstraint div#bodyconstraint-inner div.lp_flexible_layout_content_wrapper div#basiclayout.basiclayout_pe div.d-index__section.bui-spacer--large div.promotion-postcards__row.js-ds-layout-events-postcards.u-clearfix')
        first_city_link = self.driver.find_element_by_css_selector('.sh-postcard > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)')
        actions = ActionChains(self.driver)
        actions.move_to_element(body_div)
        actions.move_to_element(first_div)
        actions.move_to_element(first_city_div)
        actions.click(first_city_link)
        actions.perform()
    """

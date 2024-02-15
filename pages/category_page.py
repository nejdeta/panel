import self as self
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    CREATE_BTN = (By.ID, "create-mobile-campaign")
    CAMPAIGN_NAME_INPUT = (By.ID, "campaign-name")
    NEXT_BTN = (By.ID, "accept")
    STATUSES_LIST = (By.CSS_SELECTOR, "p[title='All Statuses']")
    TEST_STATUS = (By.CSS_SELECTOR, ".option__1.qa-drop-down-test")
    CAMPAIGN_NAME_SELECTION = (By.CSS_SELECTOR, ".ml-1.t-c-2.tooltip")
    TEST_LINK_BTN = (By.XPATH, "//p[normalize-space()='Test Link']")
    VARIATION_NAME = (By.XPATH, './/p[contains(@class, "test-link-wrapper_menu option_active")]')
    CAMPAIGN_SEARCH_INPUT = (By.ID, "search-value")
    CAMPAIGNS_LIST = (By.XPATH, "//p[@class='ml-1 t-c-2 tooltip']")
    CAMPAIGN_DETAILS_BTN = (By.XPATH, "//p[normalize-space()='Details']")
    CAMPAIGN_DETAILS_RULES = (By.XPATH, "//p[@class='f-s-2 t-c-2 w-b-b-w personalization-rule-0']")
    DETAILS_CLOSE_BTN = (By.XPATH, ".//a[contains(@class,'in-modal-wrapper__icon qa-close ml-2')]")
    TEST_VARIATION = (By.XPATH, ".//*[contains(text(),'https://inshoppingcart.com/seleniumautomation/')]")

    def click_create_btn(self):
        """
     it clicks create button to create a new campaign
        """

        self.click_element(*self.CREATE_BTN)

    def create_campaign_name(self):
        """
     it generates a random text
        """

        return self.generate_random_text()

    def fill_campaign_name(self):
        """
     it fills a generated campaign name on the input
        """

        self.send_text(self.create_campaign_name(), *self.CAMPAIGN_NAME_INPUT)

    def click_next_btn(self):
        """
     it clicks next button
        """

        self.wait_element(self.NEXT_BTN, "Next button is not clickable!").click()

    def select_statuses(self):
        """
     it clicks statuses list dropdown and selects test
        """

        self.wait_element(self.STATUSES_LIST, "Statuses list is not clickable!").click()
        self.wait_element(self.TEST_STATUS, "Test status is not clickable!").click()

    def get_campaign_name(self):
        """
     it returns the campaign name
        """

        return self.wait_element(self.CAMPAIGN_NAME_SELECTION, "Campaign name is not clickable!").text

    def search_campaign_name(self):
        """
     it clicks on the search input and writes a campaign name
        """

        self.wait_element(self.CAMPAIGN_SEARCH_INPUT, "Search input is not clickable!").click()
        self.send_text(self.get_campaign_name(), *self.CAMPAIGN_SEARCH_INPUT)

    def click_test_link(self):
        """
     it clicks on test link button
        """

        self.wait_element(self.TEST_LINK_BTN, "Test link button is not clickable!").click()

    def get_campaign_from_the_list(self):
        """
     it returns the name of the campaign from the list
        """

        return self.wait_element(self.CAMPAIGNS_LIST, "Campaigns list is not clickable!").text

    def get_campaign_variation_name(self):
        """
     it returns the name of the variation of a campaign
        """

        return self.wait_element_until_visible(self.VARIATION_NAME, "Variation name is not visible!")

    def view_campaign_details(self):
        """
     it clicks details button
        """

        self.wait_element(self.CAMPAIGN_DETAILS_BTN, "Campaign details button is not clickable!").click()

    def check_campaign_details(self):
        """
     it returns the rule inside details
        """

        return self.wait_element_until_visible(self.CAMPAIGN_DETAILS_RULES, "Rule is not visible on details!").text

    def close_details(self):
        """
     it closes details
        """

        self.wait_element(self.DETAILS_CLOSE_BTN, "Details close button is not clickable!").click()

    def test_campaign_variation(self):
        """
     it clicks test link button and then clicks the test link of the campaign
        """

        self.wait_element(self.TEST_LINK_BTN, "Test link button is not clickable!").click()
        self.hover_over_to_element(*self.VARIATION_NAME)
        self.right_click(self.wait_element(self.TEST_VARIATION, "Variation link is not clickable!"))




import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    SAVE_BTN = (By.CSS_SELECTOR, "#save-and-next")
    RULE_TYPE = (By.ID, "conditionList0")
    RULE_SEARCH_INPUT = (By.ID, "conditionList0-search")
    ADD_VARIATION_BTN = (By.ID, "add-new-variation")
    SINGLE_STORY_TEMPLATE = (By.XPATH, "//*[@class='template-list']//*[text()='{}']".format("Single Story"))
    OK_BTN = (By.CSS_SELECTOR, "#inline-select-notification a")
    SELECT_STORY_BTN = (By.CSS_SELECTOR, ".btn-select")
    IFRAME = (By.XPATH, "//iframe[@id='ins-skeleton-partner-iframe']")
    STORY_LOCATION = (By.XPATH, "//li[@class='flex-active-slide']//div[@title='…']")
    TEMPLATE_SAVE_BTN = (By.CSS_SELECTOR, ".in-button-wrapper.qa-button#save")
    LANGUAGE_INPUT = (By.ID, "personalization-language")
    LANGUAGE_INPUT_TEXT = (By.CSS_SELECTOR, "#personalization-language-search")
    LANGUAGE_SELECTION = (By.XPATH, "//a[normalize-space()='Arabic (United Arab Emirates)']")
    START_TIME_INPUT = (By.ID, "drop-down-search")
    START_TIME_SELECTION = (By.CSS_SELECTOR, "div[id='start-hour'] p[class='option__0 option_active']")
    DISPLAY_SETTINGS_INPUT = (By.XPATH, "//p[normalize-space()='DISPLAY SETTINGS']")
    DISPLAY_DAYS_CHECKBOX = (By.XPATH, "//label[contains(text(),'When active, display the personalization only on s')]")
    MONDAY = (By.CSS_SELECTOR, "span[title='Monday']")
    NOTES_INPUT = (By.ID, "note")
    TEST_STATUS = (By.XPATH, "//label[normalize-space()='Test']")

    def click_save_btn(self):
        """
     it clicks save button
        """
        time.sleep(3)
        self.wait_element(self.SAVE_BTN, "Save button is not clickable!").click()

    def select_page_rules(self, text):
        """
     it clicks page rules
        """

        self.wait_element((By.XPATH, ".//*[contains(@class,'qa')]//*[normalize-space(text())='{}']".format(text)),
                          "Page rules is not clickable!").click()

    def select_rule_type(self, text, inner_text):
        """
     it clicks rule dropdown, writes Page Type as a rule and clicks Page Type on the dropdown
        """

        self.wait_element(self.RULE_TYPE, "Rule type is not clickable!").click()
        self.send_text(text, *self.RULE_SEARCH_INPUT)
        self.wait_element((By.XPATH,
                           ".//*[contains(@class,'in-dropdown-wrapper__item-list')]//*[normalize-space(text())='{}']".format(
                               inner_text)), "Page Type is not clickable!").click()

    def click_add_new_variant_button(self):
        """
     it clicks add a new variant button
        """

        self.click_element(*self.ADD_VARIATION_BTN)

    def select_single_story(self):
        """
     it selects a single story as a template and clicks ok button on the pop up
        """

        time.sleep(3)
        self.hover_over_to_element(*self.SINGLE_STORY_TEMPLATE)
        self.wait_element(self.SELECT_STORY_BTN, "Select button is not clickable!").click()
        self.wait_element(self.OK_BTN, "Ok button is not clickable!").click()

    def append_campaign(self, text):
        """
     it switches to the iframe, append a campaign and return to default content
        """

        self.wait_frame_available(self.IFRAME)
        self.wait_element(self.STORY_LOCATION, "Story location is not clickable!").click()
        self.driver.switch_to.default_content()
        self.wait_element(
            (By.XPATH, ".//*[contains(@class,'animationHalf')][normalize-space(text())='{}']".format(text)),
            "Insert option is not clickable!").click()

    def save_template(self):
        """
     it clicks save button on action builder
        """

        time.sleep(5)
        self.wait_element(self.TEMPLATE_SAVE_BTN, "Save button is not clickable!").click()
        self.click_save_btn()

    def change_language_settings(self, text):
        """
     it writes a language on the input and then selects that language on dropdown
        """
        time.sleep(5)
        self.wait_element(self.LANGUAGE_INPUT, "Language input is not clickable!").click()
        self.send_text(text, *self.LANGUAGE_INPUT_TEXT)
        self.wait_element(self.LANGUAGE_SELECTION, "The language is not clickable!").click()

    def change_time_settings(self):
        """
     it changes the start time option and scroll down on the page
        """

        self.wait_element(self.START_TIME_INPUT, "Start time option is not clickable'").click()
        self.wait_element(self.START_TIME_SELECTION, "The time is not clickable!").click()
        self.scroll()

    def change_display_settings(self):
        """
     it clicks display settings option and selects a display day
        """

        self.wait_element(self.DISPLAY_SETTINGS_INPUT, "Display settings option is not clickable!").click()
        self.wait_element(self.DISPLAY_DAYS_CHECKBOX, "Display days checkbox is not clickable!").click()
        self.wait_element(self.MONDAY, "Monday checkbox is not clickable!").click()

    def add_notes(self, text):
        """
     it scroll to the bottom of the page and clicks notes input and then writes a note on the input
        """

        self.scroll_to_bottom()
        self.wait_element(self.NOTES_INPUT, "Notes input").click()
        self.send_text(text, *self.NOTES_INPUT)

    def activation_status_settings(self):
        """
     it select test as an activation status and clicks save button
        """

        self.wait_element(self.TEST_STATUS, "Test option is not clickable!").click()
        self.click_save_btn()

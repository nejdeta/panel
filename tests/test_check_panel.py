import logging
from tests.base_test import BaseTest

class TestCheckPanel(BaseTest):
    """Test case is:

      1. Log in the panel, and go to Web Instory
      2. Create Web Instory campaign
      3. Fill all steps till Launch step
      4. Change campaign's language, date&time, display settings, add priority, notes
    and launch campaign as Test
      5. Go to the list and check campaign status is Active and added variation is present in Test link menu
      6. Open campaign's details and check information that was filled during launch is present there
      7. Go to website with the test link of the campaign

      """
    email_text = "beste.morgul@useinsider.com"
    password_text = "123456"
    page_rules_option = "Page Rules"
    page_type_rule = "Page Type"
    search_rule_text = "Page Type"
    append_location_option = "Insert after the element"
    campaign_language = "Arabic"
    campaign_notes = "not eklendi"
    campaign_details_rule = "Page Type is All Pages"

    def test_check_panel(self):
        self.logger = logging.getLogger()

        self.logger.info("1. Log in the panel, and go to Web Instory")
        login_page = LoginPage(self.driver)
        login_page.fill_email_input(self.email_text)
        login_page.fill_password_input(self.password_text)
        login_page.click_login_btn()
        home_page = HomePage(self.driver)
        home_page.select_instory_category()
        self.logger.info("Go to Web Instory successfully!")

        self.logger.info("2. Create Web Instory campaign")
        category_page = CategoryPage(self.driver)
        category_page.click_create_btn()
        category_page.fill_campaign_name()
        category_page.click_next_btn()
        self.logger.info("Web Instory campaign created successfully!")

        self.logger.info("3. Fill all steps till Launch step")
        product_page = ProductPage(self.driver)
        product_page.click_save_btn()
        product_page.select_page_rules(self.page_rules_option)
        product_page.select_rule_type(self.search_rule_text, self.page_type_rule)
        product_page.click_save_btn()
        product_page.click_add_new_variant_button()
        product_page.select_single_story()
        product_page.append_campaign(self.append_location_option)
        product_page.save_template()
        product_page.click_save_btn()
        self.logger.info("All the steps are filled successfully!")

        self.logger.info("4.Change campaign's language, date&time, display settings, add priority,"
                         " notes and launch campaign as Test")
        product_page.change_language_settings(self.campaign_language)
        product_page.change_time_settings()
        product_page.change_display_settings()
        product_page.add_notes(self.campaign_notes)
        product_page.activation_status_settings()
        self.logger.info("Campaign are launched as Test successfully!")

        self.logger.info("5. Go to the list and check campaign status is Active and "
                         "added variation is present in Test link menu")
        category_page.select_statuses()
        category_page.search_campaign_name()
        self.assertEqual(category_page.get_campaign_name(), category_page.get_campaign_from_the_list(),
                         "Campaign is not found in the list!")
        category_page.click_test_link()
        self.assertTrue(category_page.get_campaign_variation_name(),
                        "Campaign variation does not exist!")
        self.logger.info("Campaign's status and added variation are checked successfully!")

        self.logger.info("6. Open campaign's details and check information "
                         "that was filled during launch is present there")
        category_page.view_campaign_details()
        self.assertEqual(category_page.check_campaign_details(), self.campaign_details_rule,
                         "Campaign rule is not equal with the rule in details")
        self.logger.info("Campaign's information on details are checked successfully!")

        self.logger.info("7. Go to website with the test link of the campaign")
        category_page.close_details()
        category_page.test_campaign_variation()
        self.logger.info("Go to website with the test link of the campaign successfully!")

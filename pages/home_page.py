from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    EXPERIENCE_MENU = (By.XPATH, ".//*[contains(@class,'wrapper__routes')]//*[contains(@class,'groups')]")
    SUB_MENU_SELECTOR = ".//*[contains(@class,'in-sidebar-wrapper__opened')]//*[normalize-space(text())='{}']"
    OPTIMIZE_SUB_MENU = (By.XPATH, SUB_MENU_SELECTOR.format("Optimize"))
    INSTORY_CATEGORY = (By.XPATH, SUB_MENU_SELECTOR.format("InStory"))

    def select_experience_menu(self, index):
        """
     it clicks experience menu section on panel
        """

        element = self.get_element_list(*self.EXPERIENCE_MENU)[index]
        self.wait_element(element, "Experience menu is not clickable!").click()

    def select_optimize_sub_menu(self):
        """
     it clicks optimize sub menu
        """

        self.select_experience_menu(2)
        self.wait_element(self.OPTIMIZE_SUB_MENU, "Optimize sub menu is not clickable!").click()

    def select_instory_category(self):
        """
     it clicks optimize sub menu and then clicks instory category inside of optimize
        """

        self.select_optimize_sub_menu()
        self.wait_element(self.INSTORY_CATEGORY, "Instory category is not clickable!").click()

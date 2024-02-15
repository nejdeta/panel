from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import string


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = ActionChains(self.driver)

    def get_url(self):
        """
     it returns the current url of the page
        """

        return self.driver.current_url

    def find_element(self, *locator):
        """
     it returns the locator
        """

        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        """
     it clicks the locator
        """

        self.driver.find_element(*locator).click()

    def send_text(self, text, *locator):
        """
     it sends the text on the locator
        """

        self.driver.find_element(*locator).send_keys(text)

    def clear_text(self, *locator):
        """
     it clears the input locator
        """

        self.driver.find_element(*locator).clear()

        return self

    def wait_element(self, method, message=""):
        """
     it waits the locator until it becomes clickable
        """

        return self.wait.until(EC.element_to_be_clickable(method), message)

    def wait_element_until_visible(self, method, message=""):
        """
     it waits the locator until it becomes visible
        """
        return self.wait.until(EC.presence_of_element_located(method), message)

    def get_element_list(self, *element):
        """
     it returns the locators
        """

        return self.driver.find_elements(*element)

    def scroll(self):
        """
     it scrolls down on the page (0,250)
        """

        self.driver.execute_script("window.scrollBy(0, 600);")

    def scroll_to_bottom(self):
        """
     it scrolls down on the bottom of the page and click the locator
        """

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def generate_random_text(self):
        """
     it generates a random text with six characters
        """

        letters = string.ascii_uppercase
        return "QA-TEST-"+''.join(random.choice(letters) for i in range(6))

    def hover_over_to_element(self, *locator):
        """
     it moves to the element
        """

        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_frame_available(self, method, message=""):
        """
     it waits the iframe until it becomes available and then it switches to the iframe
        """

        return self.wait.until(EC.frame_to_be_available_and_switch_to_it(method), message)

    def right_click(self, *locator):
        """
     it moves to the element
        """

        self.actions.context_click(*locator).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

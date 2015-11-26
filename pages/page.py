from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'krasnykh'

class Page(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 5)

    def is_element_visible(self, locator):
        try:
            return self.wait.until(visibility_of_element_located(locator))
        except WebDriverException:
            return False
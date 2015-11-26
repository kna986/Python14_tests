from php4dvd.model import film
from selenium.webdriver.common.by import By
from page import Page

__author__ = 'krasnykh'

class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_css_selector("")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

    @property
    def film_card(self):
        return self.driver.find_element_by_xpath("//*[@id='content']/section/div")

    @property
    def delete_item_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Remove\"]")

    @property
    def search_field(self):
        return self.driver.find_element_by_xpath("//*[@id='q']")

    def no_found_result(self):
        return self.driver.find_elements_by_link_text("No movies where found.")

    def found_result(self, film):
        return self.driver.find_elements_by_link_text(film.name)

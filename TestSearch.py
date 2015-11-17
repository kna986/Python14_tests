import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys



class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_search(self):
        '''
        Trying to search movie in our catalog with positive
        and negative data in search field.

        :return:
        '''

        driver = self.driver
        # Login in system
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        # Search with positive data.
        a = "batman"
        driver.find_element_by_xpath("//*[@id='q']").send_keys(a)
        driver.find_element_by_xpath("//*[@id='q']").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='q']").clear()

        # Trying to check search result. If data incorrect printing message after test
        try:
            driver.find_elements_by_partial_link_text(a)

        except NoSuchElementException:
            print 'Some problems in search movie'
        # Trying to check search result with negative data.
        b = "abs"
        driver.find_element_by_xpath("//*[@id='q']").send_keys(b)
        driver.find_element_by_xpath("//*[@id='q']").send_keys(Keys.ENTER)

        driver.find_elements_by_link_text("No movies where found.")



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


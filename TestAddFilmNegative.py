from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'admin'

import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time



class TestAddFilmNegative(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_film_negative(self):
        '''
        Filling the fields of web form and
        trying submit data without the required fields
        and check it.

        :return:
        '''

        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click() # Login in system

        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("aka").send_keys("Swidish")
        driver.find_element_by_name("duration").send_keys("90")
        driver.find_element_by_name("rating").send_keys("9")
        driver.find_element_by_id("own_no").click()
        driver.find_element_by_name("notes").send_keys("This cool!")
        driver.find_element_by_id("text_languages_0").send_keys("English, Spanish.")
        driver.find_element_by_name("subtitles").send_keys("No")
        driver.find_element_by_name("audio").send_keys("Yes")
        driver.find_element_by_name("video").send_keys("Mpg4")
        driver.find_element_by_name("country").send_keys("Sweden")
        driver.find_element_by_name("genres").send_keys("Music")
        driver.find_element_by_name("music").send_keys("Roxette")

        try:
            driver.find_element_by_id("submit").click()
            driver.find_element_by_xpath("//*[@id='content']/section/div")
        except NoSuchElementException, e:
            pass

        time.sleep(2)

        driver.find_element_by_name("name").send_keys("Roxette")


        try:
            driver.find_element_by_id("submit").click()
            driver.find_element_by_xpath("//*[@id='content']/section/div")
        except NoSuchElementException, e:
            pass

        driver.find_element_by_name("name").clear()
        time.sleep(2)
        driver.find_element_by_name("year").send_keys("1985")
        time.sleep(2)

        try:
            driver.find_element_by_id("submit").click()
            driver.find_element_by_xpath("//*[@id='content']/section/div")
        except NoSuchElementException, e:
            pass

        driver.find_element_by_name("name")


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

__author__ = 'admin'

import unittest

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestAddFilmPositive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_film_positive(self):
        '''
        Filling the fields of web form with positive data and
        trying submit data.

        If all data is correct, we deleting this file.
        :return:
        '''

        driver = self.driver
        # Login in system
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        # Filling the fields of web-form with positive data
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").send_keys("Roxette")
        driver.find_element_by_name("aka").send_keys("Swidish")
        driver.find_element_by_name("year").send_keys("1985")
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
        driver.find_element_by_id("submit").click()

        # Trying to check save data in web-form. If data incorrect printing message after test
        try:
            self.assertEquals("Roxette (1985)\n" +
        "Music\n" +
        "DVD, 90 minutes\n" +
        "Rating: 9\n" +
        "Languages: English, Spanish.\n" +
        "Subtitles: No\n" +
        "Country: Sweden\n" +
        "Music: Roxette\n" +
        "Video: Mpg4\n" +
        "Audio: Yes\n" +
        "Personal notes\n" +
        "This cool!",

        driver.find_element_by_xpath("//*[@id='content']/section/div").text)

        except AssertionError:
            print 'Some problems in save text'

        # Changing and save data in film
        driver.find_element_by_xpath("//*[@id='content']/section/nav/ul/li[3]/div/div/a/img").click()
        driver.find_element_by_id("text_languages_0").clear()
        driver.find_element_by_name("subtitles").clear()
        driver.find_element_by_name("audio").clear()
        driver.find_element_by_name("video").clear()
        driver.find_element_by_name("country").clear()
        driver.find_element_by_name("genres").clear()
        driver.find_element_by_name("music").clear()
        driver.find_element_by_id("submit").click()

        # Check new data. If data incorrect printing message after test
        try:
            self.assertEquals("Roxette (1985)\n" +
        "DVD, 90 minutes\n" +
        "Rating: 9\n" +
        "Personal notes\n" +
        "This cool!",

        driver.find_element_by_xpath("//*[@id='content']/section/div").text)

        except AssertionError:
            print 'Some problems in changing text'


        # delete test-file
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        time.sleep(3)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

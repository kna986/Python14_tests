from php4dvd.pages.internal_page import InternalPage
from php4dvd.pages.login_page import LoginPage
from php4dvd.pages.add_film_page import AddFilmPage
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait



__author__ = 'krasnykh'

class Application(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.login_page = LoginPage(driver, base_url)
        self.add_film_page = AddFilmPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.wait = WebDriverWait(driver, 5)

    def go_to_home_page(self):
        self.driver.get(self.base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        self.driver.switch_to_alert().accept()

    def login(self, my_user):
        lp = self.login_page
        lp.username_field.send_keys(my_user.username)
        lp.password_field.send_keys(my_user.password)
        lp.submit_button.click()

    def add_film(self, film):
        af = self.add_film_page
        af.add_film_button.click()
        af.name_field.send_keys(film.name)
        af.aka_field.send_keys(film.aka)
        af.year_field.send_keys(film.year)
        af.duration_field.send_keys(film.duration)
        af.rating_field.send_keys(film.rating)
        af.own_no_checkbox.click()
        af.notes_field.send_keys(film.notes)
        af.text_languages_0_field.send_keys(film.text_languages_0)
        af.subtitles_field.send_keys(film.subtitles)
        af.audio_field.send_keys(film.audio)
        af.video_field.send_keys(film.video)
        af.country_field.send_keys(film.country)
        af.genres_field.send_keys(film.genres)
        af.music_field.send_keys(film.music)
        af.submit_film_button.click()

    def change_film(self):
        cf = self.add_film_page
        cf.redaction_film_button.click()
        cf.text_languages_0_field.clear()
        cf.subtitles_field.clear()
        cf.audio_field.clear()
        cf.video_field.clear()
        cf.country_field.clear()
        cf.genres_field.clear()
        cf.music_field.clear()
        cf.submit_film_button.click()

    def delete_item(self):
        df = self.internal_page
        df.delete_item_button.click()
        self.close_alert_and_get_its_text()

    def search_positive(self):
        sp = self.internal_page
        sp.search_field.send_keys("Batman")
        sp.search_field.send_keys(Keys.ENTER)
        sp.search_field.clear()
        try:
            sp.no_found_result()

        except NoSuchElementException:
            print 'Some problems in search movie'

    def search_negative(self):
        sn = self.internal_page
        sn.search_field.send_keys("abs")
        sn.search_field.send_keys(Keys.ENTER)
        sn.no_found_result()


    def close_alert_and_get_its_text(self):
        alert = self.driver.switch_to_alert()
        alert.accept()
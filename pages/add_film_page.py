from selenium.webdriver.common.by import By
from page import Page

__author__ = 'krasnykh'

class AddFilmPage(Page):

    @property
    def add_film_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Add movie\"]")

    @property
    def name_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def aka_field(self):
        return self.driver.find_element_by_name("aka")

    @property
    def year_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def duration_field(self):
        return self.driver.find_element_by_name("duration")

    @property
    def rating_field(self):
        return self.driver.find_element_by_name("rating")

    @property
    def own_no_checkbox(self):
        return self.driver.find_element_by_id("own_no")

    @property
    def notes_field(self):
        return self.driver.find_element_by_name("notes")

    @property
    def text_languages_0_field(self):
        return self.driver.find_element_by_id("text_languages_0")

    @property
    def subtitles_field(self):
        return self.driver.find_element_by_name("subtitles")

    @property
    def audio_field(self):
        return self.driver.find_element_by_name("audio")

    @property
    def video_field(self):
        return self.driver.find_element_by_name("video")

    @property
    def country_field(self):
        return self.driver.find_element_by_name("country")

    @property
    def genres_field(self):
        return self.driver.find_element_by_name("genres")

    @property
    def music_field(self):
        return self.driver.find_element_by_name("music")

    @property
    def submit_film_button(self):
        return self.driver.find_element_by_id("submit")

    @property
    def redaction_film_button(self):
        return self.driver.find_element_by_xpath("//*[@id='content']/section/nav/ul/li[3]/div/div/a/img")

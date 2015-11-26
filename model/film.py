__author__ = 'krasnykh'

class Film(object):

    def __init__(self, name = "", aka = "", year = "", duration = "", rating = "", notes = "", text_languages_0 = "", subtitles = "", audio = "", video = "", country = "", genres = "", music = ""):
        self.name = name
        self.aka = aka
        self.year = year
        self.duration = duration
        self.rating = rating
        self.notes = notes
        self.text_languages_0 = text_languages_0
        self.subtitles = subtitles
        self.audio = audio
        self.video = video
        self.country = country
        self.genres = genres
        self.music = music

    @classmethod
    def new_film(cls):
        return cls(name = "Roxette", aka = "Swidish", year = "1985", duration = "90", rating = "9", notes = "This cool!", text_languages_0 = "English, Spanish.", subtitles = "No", audio = "Yes", video = "Mpg4", country = "Sweden", genres = "Music", music = "Roxette")

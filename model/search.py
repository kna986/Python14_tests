__author__ = 'admin'

class Search(object):

    def __init__(self, real_data = "", fake_data = ""):
        self.real_data = real_data
        self.fake_data = fake_data

    @classmethod
    def data_for_search_real(cls):
        return cls(real_data = "batman")

    @classmethod
    def data_for_search_fake(cls):
        return cls(fake_data = "abs")
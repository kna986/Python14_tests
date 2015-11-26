from php4dvd.model import film
from php4dvd.model import my_user

class TestAddFilmPositive():

    def test_add_film_positive(self, app):
        '''
        Filling the fields of web form with positive data and
        trying submit data.
        If all data is correct, we deleting this file.
        :return:
        '''


        # Login in system
        app.go_to_home_page()
        app.login(my_user.MyUser.Admin())

        app.add_film(film.Film.new_film())

        # delete test-file
        app.delete_item()


from php4dvd.model import film
from php4dvd.model import my_user

class TestSearch():

    def test_search(self, app):
        app.go_to_home_page()
        app.login(my_user.MyUser.Admin())
        app.search_positive()
        app.search_negative()



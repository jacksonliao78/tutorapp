from flask import session

class Model:
    def __init__(self, data) -> None:
        self.logged_in=False
        self.username=''
        self.data=data
        self.check_authentication()

    def check_authentication(self):
        if 'username' in session:
            self.logged_in=True
            self.username=session['username']

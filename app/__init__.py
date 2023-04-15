import os
from flask import Flask
# from flask_login import LoginManager
# login_manager = LoginManager()


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []
users.append(User(id=1, username='Andy', password='password'))
users.append(User(id=2, username='Avni', password='secret'))
users.append(User(id=2, username='a', password='q'))


# print(users)

app = Flask(__name__)
app.secret_key = os.urandom(24)
# print(app.secret_key)
# login_manager.init_app(app)

from app import views

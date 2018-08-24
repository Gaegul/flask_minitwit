from flask import Flask
from app.view.post import *
from app.view.login import *
from app.view.account import *
from app.model import db
from app.model.user import User
from app.model.post import Post


app = Flask(__name__)

db.connect()
db.create_tables((User, Post))


app.add_url_rule('/post', view_func=PostAPI.as_view("post"))
app.add_url_rule('/login', view_func=Login.as_view("login"))
app.add_url_rule('/account', view_func=Signup.as_view("account"))


if __name__ == '__main__':
    app.run(debug=True, port=3000)

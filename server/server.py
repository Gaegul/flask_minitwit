from flask import Flask
from app.model import db
from app.model.user import User
from app.model.post import Post
from app.view import create_app

app = Flask(__name__)

db.connect()
db.create_tables((User, Post))

create_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

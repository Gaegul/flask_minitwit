from flask import Flask
from app.model import db

app = Flask(__name__)

from app.view.account import *
db.connect()

if __name__ == '__main__':
    app.run(debug=True, port=3000)

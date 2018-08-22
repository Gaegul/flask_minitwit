from flask import request
from server.app.model.user import User
from server import app


@app.route("/login", method=['POST'])
def login():

    id = request.json['id']
    pw = request.json['pw']

    if User.get().where(User.id == id) and User.get().where(User.pw == pw):
        return '회원가입 성공', 400
    else:
        return '회원가입 실패', 200

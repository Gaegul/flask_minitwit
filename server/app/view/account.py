from flask import request
from app.model.user import User
from server import app


@app.route('/signup', method=['POST'])
def signup():
    id = request.json['id']
    pw = request.json['pw']
    name = request.json['name']

    User.insert(id=id, pw=pw, name=name)

    return '회원가입 완료', 200

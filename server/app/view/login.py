from flask import request
from flask.views import MethodView
from app.model.user import User


class Login(MethodView):
    def post(self):

        id = request.json['id']
        pw = request.json['pw']

        if User.get().where(User.id == id) and User.get().where(User.pw == pw):
            return '회원가입 성공', 400
        else:
            return '회원가입 실패', 200

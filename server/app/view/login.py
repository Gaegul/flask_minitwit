from flask import request
from flask.views import MethodView
from app.model.user import User


class Login(MethodView):
    def post(self):

        id = request.json['id']
        pw = request.json['pw']

        if User.select().where(User.id == id) and User.select().where(User.pw == pw):
            return '로그인 성공', 200
        else:
            return '로그인 실패', 400

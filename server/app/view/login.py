from flask import request
from flask.views import MethodView
from app.model.user import User


class Login(MethodView):
    def post(self):

        id = request.json['id']
        pw = request.json['pw']

        id_check = User.select().where(User.id == id)
        pw_check = User.select().where(User.pw == pw)

        if id_check.execute() and pw_check.execute():
            return '로그인 성공', 200
        else:
            return '로그인 실패', 400

from flask import request
from flask.views import MethodView
from app.model.user import User


class Signup(MethodView):
    def post(self):
        id = request.json['id']
        pw = request.json['pw']
        name = request.json['name']

        users = User.insert(id=id, pw=pw, name=name)
        users.execute()

        return "회원가입 완료", 200

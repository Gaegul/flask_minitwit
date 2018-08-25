from flask import request, jsonify
from flask.views import MethodView
from app.model.user import User


class Login(MethodView):
    def post(self):

        id = request.json['id']
        pw = request.json['pw']

        id_check = User.select().where(User.id == id)
        pw_check = User.select().where(User.pw == pw)
        user_name = User.select(User.name).where(User.id == id and User.pw == pw).dicts().get()

        if id_check.execute() and pw_check.execute():
            return jsonify(user_name), 200
        else:
            return '로그인 실패', 400

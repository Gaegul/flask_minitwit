from flask import request, Blueprint, jsonify
from app.model.user import User
from flask_restful import Resource

account_api = Blueprint("account_api", __name__)


class Signup(Resource):
    def post(self):
        try:
            id = request.json['id']
            pw = request.json['pw']
            name = request.json['name']
        except Exception as e:
            return jsonify({"message": "need signup info", "exception": str(e)}), 400

        users = User.insert(id=id, pw=pw, name=name)
        users.execute()

        return "회원가입 완료", 200



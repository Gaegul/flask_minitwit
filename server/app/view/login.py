from flask import request, jsonify, Blueprint
from app.model.user import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_restful import Resource

login_api = Blueprint('login_api', __name__)


#로그인
class Login(Resource):
    def post(self):
        try:
            id = request.json['id']
            pw = request.json['pw']
        except Exception as e:
            return jsonify({"message": "need login info", "exception": str(e)}), 400

        id_check = User.select().where(User.id == id)
        pw_check = User.select().where(User.pw == pw)

        access_token = create_access_token(identity=id)
        refresh_token = create_refresh_token(identity=id)

        if id_check.execute() and pw_check.execute():
            return jsonify(access_token, refresh_token)
        else:
            return '로그인 실패', 400


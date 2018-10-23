from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required
from app.model.user import User
from flask_restful import Resource

my_page_api = Blueprint("my_page_api", __name__)


class My(Resource):
    @jwt_required
    def get(self):
        my_page = User.select().order_by(User.name).dicts()
        res = list(my_page)

        return jsonify(res), 200



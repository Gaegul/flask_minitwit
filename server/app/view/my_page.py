from flask import jsonify, Blueprint
from flask.views import MethodView
from flask_jwt_extended import JWTManager, jwt_required
from server import app
from app.model.user import User

jwt = JWTManager(app)

my_page_api = Blueprint("my_page_api", __name__)


class My(MethodView):
    @jwt_required
    def get(self):
        my_page = User.select().order_by(User.name).dicts()
        res = list(my_page)

        return jsonify(res), 200


my_page_api.add_url_rule('/my_page', view_func=My.as_view("my_page"))
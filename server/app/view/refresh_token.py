from flask import Blueprint, Response
from flask.views import MethodView
from app.model.user import User
from flask_jwt_extended import jwt_refresh_token_required, create_access_token

new_access_token_api = Blueprint('new_access_token_api', __name__)


class Refresh(MethodView):
    @jwt_refresh_token_required
    def get(self):
        id = User.select().where(User.id == id)
        access_token = create_access_token(identity=id)
        return Response(access_token), 200


new_access_token_api.add_url_rule('/refresh', view_func=Refresh.as_view("refresh"))
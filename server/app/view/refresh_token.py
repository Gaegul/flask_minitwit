from flask import Blueprint, Response
from flask.views import MethodView
from app.model.user import User
from flask_jwt_extended import jwt_refresh_token_required, create_access_token, get_jwt_identity

refresh_api = Blueprint('new_access_token_api', __name__)


class Refresh(MethodView):
    @jwt_refresh_token_required
    def get(self):
        access_token = create_access_token(identity=get_jwt_identity())
        return Response(access_token)


refresh_api.add_url_rule('/refresh', view_func=Refresh.as_view("refresh"))

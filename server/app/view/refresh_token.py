from flask import Blueprint, Response
from flask_jwt_extended import jwt_refresh_token_required, create_access_token, get_jwt_identity
from flask_restful import Resource

refresh_api = Blueprint('new_access_token_api', __name__)


class Refresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        access_token = create_access_token(identity=get_jwt_identity())
        return Response(access_token)


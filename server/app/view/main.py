from app.model.post import Post
from flask import jsonify, Blueprint
from flask_restful import Resource

main_api = Blueprint("main_api", __name__)


class Main(Resource):
    def get(self):
        main_post = Post.select().order_by(Post.create_at).dicts()
        res = list(main_post)

        return jsonify(res), 200

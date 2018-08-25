from app.model.post import Post
from flask.views import MethodView
from flask import jsonify


class Main(MethodView):
    def get(self):
        main_post = Post.select().order_by(Post.create_at).dicts()
        res = list(main_post)

        return jsonify(res), 200

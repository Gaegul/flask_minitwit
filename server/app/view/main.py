from app.model.post import Post
from flask.views import MethodView
from flask import jsonify, Blueprint

main_api = Blueprint("main_api", __name__)


class Main(MethodView):
    def get(self):
        main_post = Post.select().order_by(Post.create_at).dicts()
        res = list(main_post)

        return jsonify(res), 200


main_api.add_url_rule('/main', view_func=Main.as_view("login"))

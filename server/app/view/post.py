from flask.views import MethodView
from flask import request, Blueprint, jsonify
from app.model.post import Post

post_api = Blueprint("post_api", __name__)


class PostAPI(MethodView):
    def post(self):
        try:
            title = request.json['title']
            contents = request.json['contents']
            user_name = request.json['user_name']
        except Exception as e:
            return jsonify({"messege": "need post info", "exception": str(e)}), 400

        posts = Post.insert(title=title, content=contents, user=user_name)
        posts.execute()

        return '글작성 완료', 200


post_api.add_url_rule("/post", view_func=PostAPI.as_view("post"))
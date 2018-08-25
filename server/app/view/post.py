from flask.views import MethodView
from flask import request
from app.model.post import Post


class PostAPI(MethodView):
    def post(self):
        title = request.json['title']
        contents = request.json['contents']
        user_name = request.json['user_name']

        posts = Post.insert(title=title, content=contents, user=user_name)
        posts.execute()

        return '글작성 완료', 200

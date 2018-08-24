from flask.views import MethodView
from flask import request
from app.model.post import Post


class PostAPI(MethodView):
    def post(self):
        title = request.json['title']
        contents = request.json['contents']

        posts = Post.insert(title=title, content=contents)
        posts.execute()

        return '글작성 완료', 200

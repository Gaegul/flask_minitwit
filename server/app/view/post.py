from flask.views import MethodView


class PostAPI(MethodView):
    def get(self):
        return "Post Request"
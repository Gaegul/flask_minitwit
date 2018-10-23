from flask_restful import Api
from server import app

api = Api(app)

from .view.login import Login
api.add_resource(Login, '/login')

from .view.account import Signup
api.add_resource(Signup, '/signup')

from .view.my_page import My
api.add_resource(My, '/my_page')

from .view.post import PostAPI
api.add_resource(PostAPI, '/post')

from .view.refresh_token import Refresh
api.add_resource(Refresh, '/refresh')

from .view.main import Main
api.add_resource(Main, '/main')
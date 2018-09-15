from .main import main_api
from .login import login_api
from .post import post_api
from .account import account_api
from .my_page import my_page_api
from .refresh_token import refresh_api
from flask_jwt_extended import JWTManager


def create_app(app_):
    JWTManager(app_)
    app_.config['JWT_SECRET_KEY'] = "asdf"
    app_.register_blueprint(main_api)
    app_.register_blueprint(login_api)
    app_.register_blueprint(post_api)
    app_.register_blueprint(account_api)
    app_.register_blueprint(my_page_api)
    app_.register_blueprint(refresh_api)

    return app_

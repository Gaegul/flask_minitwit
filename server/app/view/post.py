from flask import request
from server import app
from server.app.model.post import Post
#from server.app.model.user import User

@app.route('/post', method=['GET'])
def post():
    return 200
    #
    # title = request.json['title']
    # content = request.json['json']
    #토큰사용을 할 줄 몰라서 로그인한 유저의 작성자를
    #user = User.get()
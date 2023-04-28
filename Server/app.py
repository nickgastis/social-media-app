
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
api = Api(app)
db.init_app(app)


@app.route('/')
def index():
    return 'Social Media App DataBase'


class Users(Resource):
    def get(self):
        user_list = [u.to_dict() for u in User.query.all()]
        resp = make_response(
            user_list,
            200
        )
        return resp
api.add_resource(Users, '/users')

class Posts(Resource):
    def get(self):
        post_list = [u.to_dict() for u in Post.query.all()]
        resp = make_response(
            post_list,
            200
        )
        return resp

api.add_resource(Posts, '/posts')



if __name__ == '__main__':
    app.run(port=5555, debug=True)

import json as j
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

user_data = []

with open('./users.json', 'r') as d:
    user_data = j.loads(d.read())


class User(Resource):
    def get(self, user_id):
        return f'GET User: {user_id}'

    def post(self):
        return 'POST User'

    def put(self):
        return 'PUT User'

    def delete(self, user_id):
        return f'DELETE User: {user_id}'

class UserList(Resource):
    def get(self):
        return user_data

api.add_resource(User, '/api/user/<string:user_id>')
api.add_resource(UserList, '/')

if __name__ == '__main__':
    app.run(debug=True)

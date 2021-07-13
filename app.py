import json as j
import uuid as id
from flask import Flask
from flask.globals import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def get_data():
    with open('./users.json', 'r') as d:
        return j.loads(d.read())


def write_data(data):
    with open('./users.json', 'w') as d:
        j.dump(data, d)


class User(Resource):
    def get(self, user_id):
        user_data = get_data()

        for d in user_data['users']:
            if d['id'] == user_id:
                return d
        else:
            return f'User does not exist: {user_id}', 404

    def put(self, user_id):
        user_data = get_data()

        for d in user_data['users']:
            if d['id'] == user_id:
                put_data = j.loads(request.data.decode())

                updated_data = {
                    'id': user_id,
                    'name': put_data['name'],
                    'location': put_data['location']
                }

                user_data['users'].remove(d)
                user_data['users'].insert(
                    len(user_data['users']), updated_data)

                write_data(user_data)
                return f'User updated: {user_id}', 201
        else:
            return f'User does not exist: {user_id}', 404

    def delete(self, user_id):
        user_data = get_data()

        for d in user_data['users']:
            if d['id'] == user_id:
                user_data['users'].remove(d)
                write_data(user_data)
                return f'User deleted: {user_id}', 204
        else:
            return f'User does not exist: {user_id}', 404


class UserCreate(Resource):
    def post(self):
        user_data = get_data()

        post_data = j.loads(request.data.decode())

        create_data = {
            'id': str(id.uuid4())[:8],
            'name': post_data['name'],
            'location': post_data['location']
        }

        user_data['users'].insert(
            len(user_data['users']), create_data)

        write_data(user_data)

        return create_data


class UserList(Resource):
    def get(self):
        return get_data()


api.add_resource(User, '/api/user/<user_id>')
api.add_resource(UserCreate, '/api/user/create')
api.add_resource(UserList, '/')


if __name__ == '__main__':
    app.run(debug=True)

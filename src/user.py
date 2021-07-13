import json as j
from .util import get_data, write_data
from flask_restful import Resource
from flask.globals import request


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

import json as j
import uuid as id
from .util import get_data, write_data
from flask_restful import Resource
from flask.globals import request


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

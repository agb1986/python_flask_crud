from .util import get_data
from flask_restful import Resource


class UserList(Resource):
    def get(self):
        return get_data()

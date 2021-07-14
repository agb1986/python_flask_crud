from flask import Flask
from flask_restful import Api

from src import User, UserCreate, UserList

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/api/user/<user_id>')
api.add_resource(UserCreate, '/api/user/create')
api.add_resource(UserList, '/')

if __name__ == '__main__':
    app.run(debug=True)

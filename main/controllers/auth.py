from flask import request
from flask_restx import Resource

from ..dto.user import RegisterUserDto
from ..services.user import create_new_user, login_user, get_all_services

api = RegisterUserDto.api


@api.route('/signUp')
class UserList(Resource):

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(RegisterUserDto.data, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return create_new_user(data=data)


@api.route('/signIn')
@api.response(401, 'Authentication failure')
class User(Resource):
    @api.doc('Loginsign')
    @api.expect(RegisterUserDto.login, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return login_user(data=data)


@api.route('/serviceList')
class User(Resource):
    @api.doc('services')
    def get(self):
        return get_all_services()
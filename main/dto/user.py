from flask_restx import Namespace, fields


class RegisterUserDto:
    api = Namespace('user', description='user related operations')
    data = api.model('user', {
        "client_firstname": fields.String(required=True, description='user email address'),
        "client_lastname": fields.String(required=True, description='user email address'),
        "client_username": fields.String(required=True, description='user email address'),
        "client_email": fields.String(required=True, description='user email address'),
        "client_password": fields.String(required=True, description='user email address'),
        "client_birthday": fields.String(required=True, description='user email address'),
        "client_gender": fields.String(required=True, description='user email address'),
        "client_nationality": fields.String(required=True, description='user email address'),
    })
    login = api.model('user-login', {
        "client_email": fields.String(required=True, description='user email address'),
        "client_password": fields.String(required=True, description='user email address'),
    })

class LoginDto:
    api = Namespace('login', description='user related operations')
import uuid
import datetime

from .. import db
from ..models.users import User

def create_new_user(data):
    user = User.query.filter_by(client_email=data['client_email']).first()
    if not user:
        new_user = User(
            # public_id=str(uuid.uuid4()),
            client_lastname=data['client_lastname'],
            client_firstname=data['client_firstname'],
            client_username=data['client_username'],
            client_email=data['client_email'],
            client_password=data['client_password'],
            client_birthday=data['client_birthday'],
            client_gender=data['client_gender'],
            client_nationality=data['client_nationality'],
        )
        save_changes(new_user)
        response_object = {
            'result': 'success',
            'message': 'User Registered Successfully.',
            'client_id': new_user.id
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def login_user(data):
    user = User.query.filter_by(client_email=data['client_email']).first()
    if user:
        user.check_password(data['client_password'])
        response_object = {
            'result': 'success',
            'message': 'User logged in successfully.',
            # 'token': user.encode_auth_token(),
            'client': {
                'client_lastname': user.client_lastname,
                'client_firstname': user.client_firstname,
                'client_username': user.client_username,
                'client_email': user.client_email,
                'client_birthday': user.client_birthday,
                'client_gender': user.client_gender,
                'client_nationality': user.client_nationality,
            }
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'failed',
            'message': 'Authentication failure.'
        }
        return response_object, 400

def get_all_services():
    response_object = {
        'result': 'success',
        'message': 'User logged in successfully.',
        # 'token': user.encode_auth_token(),
        'services': [{
        }]
    }
    return response_object, 409


def save_changes(data):
    db.session.add(data)
    db.session.commit()
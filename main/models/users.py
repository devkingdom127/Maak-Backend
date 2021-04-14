from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import request, jsonify
import enum
import json
from flask_expects_json import validate, ValidationError
from .. import db, flask_bcrypt, config
import datetime
import jwt

# from .. import db, flask_bcrypt
# from ..db.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100))
    client_firstname = db.Column(db.String(100))
    client_lastname = db.Column(db.String(100))
    client_username = db.Column(db.String(100))
    client_email = db.Column(db.String(100))
    client_password = '' #db.Column(db.String(100))
    password_hash = db.Column(db.String(100))
    client_birthday = db.Column(db.String(100))
    client_gender = db.Column(db.String(100))
    client_nationality = db.Column(db.String(100))


    @property
    def client_password(self):
        raise AttributeError('password: write-only field')

    @client_password.setter
    def client_password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)
    
    def encode_auth_token(self):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': self.id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
            """
            Decodes the auth token
            :param auth_token:
            :return: integer|string
            """
            try:
                payload = jwt.decode(auth_token, key)
                is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
                if is_blacklisted_token:
                    return 'Token blacklisted. Please log in again.'
                else:
                    return payload['sub']
            except jwt.ExpiredSignatureError:
                return 'Signature expired. Please log in again.'
            except jwt.InvalidTokenError:
                return 'Invalid token. Please log in again.'
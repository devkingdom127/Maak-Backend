from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Blueprint
from .db import db


flask_bcrypt = Bcrypt()
blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title='Test API',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

def create_app(config):
    """Instantiates Flask app

    This creates a Flask application instance using
    application factory pattern with the a config and
    return an instance of the app with some configurations

    :param config: Flask configuration from file
    :return: app
    :rtype: object
    """

    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)
    return app


def register_extensions(app):
    """Register all Extensions
    This registers all the add-ons of the app,
    to be instantiated with the instance of the flask app
    Add your extensions to this functions e.g Mail

    :param app: Flask app instance
    :return: None
    :rtype: NoneType
    """

    db.init_app(app)
    # api = Api(app)
    flask_bcrypt.init_app(app)
    Migrate(app, db)
    from .controllers.auth import api as user_ns
    api.add_namespace(user_ns, path='/user')
    app.register_blueprint(blueprint)
    app.app_context().push()

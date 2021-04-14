
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import create_app, register_extensions
from main.config.config import DevelopmentConfig



# def init_db():
#     db.create_all()

if __name__ == '__main__':
    app = create_app(DevelopmentConfig)
    register_extensions(app)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
from main import create_app, register_extensions
from main.config.config import DevelopmentConfig

app = create_app(DevelopmentConfig)
register_extensions(app)

if __name__=='__main__':
    app.run()

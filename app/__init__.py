from flask import Flask
from config import fConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object((get_flask_env()))
    return app

def get_flask_env():
    if fConfig.Config.ENV == "prod":
        return 'config.fConfig.prodConfig'
    elif fConfig.Config.ENV == "dev":
        return 'config.fConfig.devConfig'
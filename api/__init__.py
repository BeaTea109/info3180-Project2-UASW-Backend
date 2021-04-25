from flask import Flask, config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
app = Flask(__name__)


db = SQLAlchemy(app)
CORS(app)
# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(Config)
from api.views import views
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "    postgres://xsdieiszkzggiy:3642b3efac62c3395d4d7ad9134895617db0fd25e205e557cb2f1fa011932c2c@ec2-34-225-103-117.compute-1.amazonaws.com:5432/dfesuqo3805m8u"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)
CORS(app)
# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from api.views import views
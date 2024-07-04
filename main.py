from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Inicjalizacja aplikacji Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Tajny_KLucz'

# Konfiguracja aplikacji
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Zalecane dla SQLAlchemy

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

# Importowanie tras (routes.py) i modeli (models.py)
from routes import *
from models import *

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# Punkt wejścia do aplikacji Flask
if __name__ == '__main__':
    app.run(debug=True)

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

# Inicjalizacja SQLAlchemy
db = SQLAlchemy(app)

# Inicjalizacja Flask-Migrate
migrate = Migrate(app, db)

# Inicjalizacja LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Importowanie tras (routes.py) i modeli (models.py)
from routes import *  # Upewnij się, że routes.py zawiera definicje tras
from models import *  # Importuje wszystkie klasy z models.py

# Funkcja do ładowania użytkownika dla LoginManager (opcjonalnie)
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# Punkt wejścia do aplikacji Flask
if __name__ == '__main__':
    app.run(debug=True)

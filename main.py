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


# Punkt wejścia do aplikacji Flask
if __name__ == '__main__':
    app.run(debug=True)

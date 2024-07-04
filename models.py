from main import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    messages_sent = relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy=True)
    messages_received = relationship('Message', foreign_keys='Message.receiver_id', backref='receiver', lazy=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

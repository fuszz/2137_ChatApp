from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from main import app, db, login_manager
from models import User, Message
import hashlib


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == str(hashlib.sha256(password.encode()).hexdigest()):
            login_user(user)
            return redirect(url_for('chat'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        new_user = User(username=username, password=hashlib.sha256(password.encode()).hexdigest())
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/chat')
@login_required
def chat():
    users = User.query.all()
    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) | (Message.receiver_id == current_user.id))
    ).order_by(Message.timestamp.asc()).all()
    return render_template('chat.html', users=users, messages=messages, current_user=current_user)

@app.route('/send_message', methods=['POST'])
@login_required
def send_message():
    receiver_id = request.form.get('receiver_id')
    content = request.form.get('content')
    message = Message(content=content, sender_id=current_user.id, receiver_id=receiver_id)
    db.session.add(message)
    db.session.commit()
    return redirect(url_for('chat'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

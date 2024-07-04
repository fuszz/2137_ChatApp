#!/usr/bin/python3

from main import app, db
with app.app_context():
  db.create_all()

exit()
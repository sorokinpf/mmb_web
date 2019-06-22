from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///mysql/mmb_web'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


if __name__ == '__main__':
	print ('Working')
	while True:
		time.sleep(10)
		print ('10s elapsed')

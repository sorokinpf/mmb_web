from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = os.urandom(64)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

from app import routes
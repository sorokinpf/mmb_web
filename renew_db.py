#renew_db.py

from app import app
from app import db
db.drop_all()
db.create_all()
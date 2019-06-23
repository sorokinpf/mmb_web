#schema.py

from app import db
from app import security

competition_map = db.Table('competition_map',
     db.Column('map_id', db.Integer, db.ForeignKey('maps.id')),
     db.Column('competition_id', db.Integer, db.ForeignKey('competitions.id')))

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120),nullable=False)
	results = db.relationship('Result',backref='user',lazy=True)

	def __repr__(self):
		return '<User %r>' % self.username

	def authenticate(username,password):
		u = User.query.filter(User.username==username).all()
		if len(u) == 0:
			return False
		u = u[0]
		print (u)
		return security.Security.check_password(u.password,password)

class Competition(db.Model):
	__tablename__ = 'competitions'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(80),unique=True,nullable=False)
	maps = db.relationship("Map",
                               secondary=competition_map)


	def __repr__(self):
		return '<Comp %r>' % self.name

class Map(db.Model):
	__tablename__ = 'maps'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100),nullable=False)
	filename = db.Column(db.String(256),nullable=False)
	map_data = db.Column(db.Text)
	results = db.relationship('Result',backref='map',lazy=True)


	def __repr__(self):
		return '<map %r>' % self.name


class Result(db.Model):
	__tablename__ = 'results'
	id = db.Column(db.Integer,primary_key=True)
	score = db.Column(db.Float,nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
	map_id = db.Column(db.Integer, db.ForeignKey('maps.id'),
        nullable=False)

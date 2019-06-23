from app import app
from flask import Flask, session, redirect, url_for, escape, request, render_template

import os
from app import security
from models import User,Competition,Map
from app import db

@app.route('/')
@app.route('/index')
def index():
	if 'username' in session:
		return 'Hello, %s' % session['username']
	else:
		return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if User.authenticate(username,password):
			session['username']=username
			return redirect(url_for('index'))
		else:
			return render_template('login_incorrect.html')
	return render_template('login.html')

@app.route('/register',methods = ['GET','POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		pwd_hash = security.Security.create_password(password)
		u = User(username=username,email=email,password=pwd_hash)
		db.session.add(u)
		db.session.commit()
		return redirect(url_for('register_success'))
	return render_template('register.html')

@app.route('/register_success')
def register_success():
	return render_template('register_success.html')

		
from flask import Flask, render_template, session, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'BUFFER_OVERFLOW'

@app.route('/')
def index():
	if 'username' in session:
		username = escape(session['username'])
		return render_template("home.html", username=username)
	return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['username'] == 'admin' and request.form['password'] == 'admin':
			session['username'] = request.form['username']
			return redirect(url_for('index'))
		return redirect(url_for('index'))

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))
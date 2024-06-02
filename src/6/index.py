import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	app.config['UPLOAD_PATH'] = 'uploads'
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
		return render_template("success.html", name = f.filename)

@app.route('/uploads/<filename>')
def uploads(filename):
	app.config['UPLOAD_PATH'] = 'uploads'
	return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == '__main__':
	app.run(debug=True)
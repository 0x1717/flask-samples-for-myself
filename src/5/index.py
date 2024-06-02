from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def upload():
	return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		f.save('static/'+f.filename)
		return render_template("success.html", name = f.filename)

if __name__ == '__main__':
    app.run(debug=True)
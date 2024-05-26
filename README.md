#### > Hello Word

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"
```

#### > Escape

```
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```

#### > GET Method

```
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	name = request.args.get('name')
	return name
```

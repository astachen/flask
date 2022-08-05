from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return 'index'
#
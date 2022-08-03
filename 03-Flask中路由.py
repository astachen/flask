from flask import Flask, redirect, current_app, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/center')
def center():
    return redirect(url_for(''))
    return 'center'

@app.route('/login',methods=['GET','POST'])
def login():
    return 'login'


if __name__ == '__main__':
    app.run(debug=True)

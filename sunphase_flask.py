from flask import Flask

# create a flask object
app = Flask(__name__)


@app.route('/sunrise')
def sunphase():
    return 'Hello!'


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)  # now anyone has the access to the site

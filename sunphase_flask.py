from flask import Flask

# create a flask object
import sunphase_astral

app = Flask(__name__)


@app.route('/sunrise/<name>')   # read the name(nearly equal to 'import')
def sunphase(name):
    return sunphase_astral.city_astral(name)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)  # now anyone has the access to the site

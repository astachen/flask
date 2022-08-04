from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter, IntegerConverter, FloatConverter

app = Flask(__name__)


# url(r'/info/(\d+)'.views.index)

# http://127.0.0.1:5000/center/1

@app.route('/center1<int:uid>')
def center1(uid):
    print(type(uid))
    # return 'my uid is {0}'.format(uid)
    return 'my uid is %s' % uid
    # return 'center'


@app.route('/center2/<float:uid>')
def center2(uid):
    print(type(uid))
    return 'my uid is {0}'.format(uid)
    # return 'my uid is %s' % uid
    # return 'center'


@app.route('/center3/<path:uid>')
def center3(uid):
    print(type(uid))
    return 'my uid is {0}'.format(uid)
    # return 'my uid is %s' % uid
    # return 'center'


@app.route('/center4/<path:uid>')
def center4(uid):
    print(type(uid))
    return 'my uid is {0}'.format(uid)
    # return 'my uid is %s' % uid
    # return 'center'


# 自定义转换器
class MyConverter(BaseConverter):

    def __init__(self, map, regex):
        super().__init__(map)

        self.regex = regex


# 注册转换器
app.url_map.comverters['mc'] = MyConverter


@app.route('/phone/<mc("1[3456789]\d{9}"):pe>')
def phone(pe):
    print(type(pe))
    return 'my phone is {0}'.format(pe)
    # return 'my uid is %s' % uid
    # return 'center'


@app.route('/phone1/<mc("1[3456789]\d{9}"):pe>')
def phone1(pe):
    print(type(pe))
    return 'my phone is {0}'.format(pe)


@app.route('/phone2/<mc("1[3456789]\d{9}"):pe>')
def phone2(card):
    print(type(card))
    return 'my phone is {0}'.format(card)


if __name__ == '__main__':
    app.run(debug=True)

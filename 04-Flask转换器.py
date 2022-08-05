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
#
    def __init__(self, map, regex):
        super().__init__(map)

        self.regex = regex

    # 可以统一参数处理
    def to_python(self, value):
        return value

    # 重定向时用到
    def to_url(self, value):
        print(value, '----------------------------------')
        return value


# 注册转换器
app.url_map.converters['mc'] = MyConverter


@app.route('/phone/<mc("1[3456789]\d{9}"):pe>')
def phone(pe):
    print(type(pe))
    # return 'my phone is {0}'.format(pe)
    # return 'my uid is %s' % uid
    # return 'center'
    return redirect(url_for('phone1', pe=138123456789))

@app.route('/phone1/<mc("1[3456789]\d{9}"):pe>')
def phone1(pe):
    print(type(pe))
    return 'my phone is {0}'.format(pe)


@app.route(
    '/phone2/<mc("[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]"):pe>')
def phone2(card):
    print(type(card))
    return 'my phone is {0}'.format(card)


if __name__ == '__main__':
    app.run(debug=True)

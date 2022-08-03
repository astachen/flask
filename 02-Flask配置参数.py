from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    name = app.config.get('NAME')
    name = app.config['NAME']
    return 'name'


# 配置参数

# 用类的方式
# class Config(object):
#     DEBUG = True
#
#
# app.config.from_object(Config)


# 从文件读取
# app.config.from_pyfile('config.cfg')

# 直接配置
app.config['DEBUG'] = True

# 自定义参数

class Config(object):
    DEBUG = True
    NAME = 'laowang'

app.config.from_object(Config)

if __name__ == '__main__':
    app.run()

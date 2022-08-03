from flask import Flask

# 创建一个flask对象
# __name__表示以当前文件目录为Flask的家目录
# static_folder 指定静态目录
# template——folder 指定模板目录
# static——url——path 隐藏真实路径
# http://127.0.0.1:5000/1811/greem.jpeg
app = Flask(__name__, static_folder='static',
            template_folder='templates',
            static_url_path='/1811')


# 路由和视图
@app.route('/')
def index():
    return 'index'


# 0.0.0.0 只有任意IP找到这个网络设备即可
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

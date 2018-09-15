import random
import string

from flask import Flask, request, jsonify

# 创建app
from API.db import Database

app = Flask(__name__)

'''
    返回格式
    json
    {code=操作码，msg=错误信息，data=返回数据(可选)}
'''


# @app.route()是一种装饰器语法，装饰其下方的函数
@app.route('/api')  # 此处定义url，也是前台将要请求的接口地址
def api_index():  # 此处为收到请求时执行的操作
    return 'This is index page.'


@app.route('/api/test-request', methods=['GET', 'POST'])  # 可以定义支持的请求方式，如果不写则默认为GET
def test_request():
    # request用于处理各种请求
    if request.method == 'POST':
        # 下面是获取使用POST方式提交数据的方法
        text = request.form['text']
    elif request.method == 'GET':
        # 下面是获取使用GET方式提交数据的方法
        text = request.args.get('text', type=str)
    else:
        text = 'Can not receive anything.'
    return 'text = ' + text


@app.route('/api/check_server')
def check_server():
    """
    检查服务器是否可用
    :return: json status(1=正常)
    """
    return jsonify({'code': 1, 'msg': ''})


'''
    用户接口
'''


@app.route('/api/account/login', methods=['POST'])
def login():
    """
    用户登录
    :return: code(0=未知用户，-1=token初始化失败，1=成功)
    """
    username = request.form['username']
    password = request.form['password']
    db = Database()
    result = db.get({'username': username, 'password': password}, 'user')
    if result:
        result = db.update({'username': username, 'password': password}, {'token': new_token()}, 'user')
        if result:
            return jsonify({'code': 1, 'msg': 'success', 'data': {'token': result['token']}})
        return jsonify({'code': -1, 'msg': 'unable to update token'})
    return jsonify({'code': 0, 'msg': 'unexpected user'})


def new_token():
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 25))
    return ran_str


@app.route('/api/account/logout', methods=['POST'])
def logout():
    """
    用户退出
    :return: code(0=未知用户，1=成功)
    """
    token = request.form['token']
    db = Database()
    result = db.update({'token': token}, {'token': ''}, 'user')
    if result:
        return jsonify({'code': 1, 'msg': 'success'})
    return jsonify({'code': 0, 'msg': 'unexpected user'})


@app.route('/api/account/sign_up')
def sign_up():
    """
    用户注册
    :return:
    """
    pass


'''
    阅读接口
'''


@app.route('/api/reading/get_book_info')
def get_book_info():
    """
    获取书籍简介信息
    :return: code(0=未知书籍id，1=成功)
    """
    book_id = request.form['id']
    db = Database()
    result = db.get({'id': book_id}, 'article')
    if result:
        return jsonify({'code': 1, 'msg': 'success', 'data': result})
    return jsonify({'code': 0, 'msg': 'unexpected book id'})


if __name__ == '__main__':
    # 开启调试模式，修改代码后不需要重新启动服务即可生效
    # 请勿在生产环境下使用调试模式
    # Flask服务将默认运行在localhost的5000端口上
    app.run(debug=True)

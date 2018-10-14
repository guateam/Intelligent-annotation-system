import datetime
import os
import random
import string

from flask import Flask, request, jsonify

from API.db import Database, generate_password
from CollaborativeFiltering.cf import item_cf
from TextFeatureExtraction.WordSegmentation import pred

# 创建app

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
    return jsonify({'code': 1, 'msg': ''})  # 简单的返回值


'''
    账户接口(对用户个人操作) account
'''


@app.route('/api/account/login', methods=['POST'])  # 限制请求类型
def login():
    """
    用户登录
    :return: code(0=未知用户，-1=token初始化失败，1=成功)
    """
    username = request.form['username']
    password = request.form['password']
    db = Database()
    result = db.get({'username': username, 'password': generate_password(password)}, 'user')  # 获取数据
    if result:
        if result['is_del'] == 0:
            result = db.update({'username': username, 'password': generate_password(password)},
                               {'token': new_token()},
                               'user')  # 更新token
            if result:
                return jsonify(
                    {'code': 1, 'msg': 'success', 'data': {'token': result['token'], 'group': result['group']}}
                )  # 成功返回
            return jsonify({'code': -1, 'msg': 'unable to update token'})  # 失败返回
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回


def random_char():
    """
    获取随机25个字符的字符串
    :return: 字符串
    """
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 25))  # 获取随机25个字符
    return ran_str


def new_token():
    """
    获取一个不重复的token
    :return: token
    """
    db = Database()
    token = random_char()
    check = db.get({'token': token}, 'user')  # 检查token是否可用
    if check:
        return new_token()  # 递归调用
    return token


@app.route('/api/account/logout', methods=['POST'])
def logout():
    """
    用户退出
    :return: code(0=未知用户，1=成功)
    """
    token = request.form['token']
    db = Database()
    result = db.update({'token': token, 'is_del': 0}, {'token': ''}, 'user')  # 释放token
    if result:
        return jsonify({'code': 1, 'msg': 'success'})  # 成功返回
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 失败返回


@app.route('/api/account/signup', methods=['POST'])
def sign_up():
    """
    用户注册
    :return:
    """
    username = request.form['username']
    nickname = request.form['nickname']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
    group = request.form['group']
    db = Database()
    check_username = db.get({'username': username}, 'user')
    check_email = db.get({'email': email}, 'user')
    check_phone = db.get({'phone': phone}, 'user')
    if check_username:
        return jsonify({'code': 0, 'msg': 'username is already signed'})  # 用户名重复
    if check_email:
        return jsonify({'code': -1, 'msg': 'email is already signed'})  # 邮箱重复
    if check_phone:
        return jsonify({'code': -2, 'msg': 'phone is already signed'})  # 手机号重复
    flag = db.insert({
        'username': username,
        'password': generate_password(password),
        'group': group,
        'nickname': nickname,
        'phone': phone,
        'email': email,
    }, 'user')  # 添加新用户
    if flag:
        return jsonify({'code': 1, 'msg': 'success'})  # 成功返回
    return jsonify({'code': -3, 'msg': 'unknown'})  # 未知错误


@app.route('/api/account/check_username_available')
def check_username_available():
    """
    检查用户名是否可用
    :return: code 1 = 可用 0 = 不可用
    """
    username = request.form['username']
    db = Database()
    check_username = db.get({'username': username}, 'user')  # 查询
    if check_username:
        return jsonify({'code': 0, 'msg': 'username is already signed'})  # 不可用
    return jsonify({'code': 1, 'msg': 'username is available'})  # 可用


@app.route('/api/account/check_phone_available')
def check_phone_available():
    """
    检查手机号是否可用
    :return: code 1 = 可用 0 = 不可用
    """
    phone = request.form['phone']
    db = Database()
    check_phone = db.get({'phone': phone}, 'user')
    if check_phone:
        return jsonify({'code': 0, 'msg': 'phone is already signed'})
    return jsonify({'code': 1, 'msg': 'phone is available'})


@app.route('/api/account/check_email_available')
def check_email_available():
    """
    检查邮箱是否可用
    :return: code 1 = 可用 0 = 不可用
    """
    email = request.form['email']
    db = Database()
    check_email = db.get({'email': email}, 'user')
    if check_email:
        return jsonify({'code': 0, 'msg': 'email is already signed'})
    return jsonify({'code': 1, 'msg': 'email is available'})


'''
    阅读接口 reading
'''


@app.route('/api/reading/get_book_info/<book_id>')  # 通过路由传值
def get_book_info(book_id):
    """
    获取书籍简介信息
    :return: code(0=未知书籍id，1=成功)
    """
    # book_id = request.form['id'] 废弃调用方法
    db = Database()
    result = db.get({'id': book_id}, 'article')  # 获取书籍id
    if result:
        return jsonify({'code': 1, 'msg': 'success', 'data': result})
    return jsonify({'code': 0, 'msg': 'unexpected book id'})


@app.route('/api/reading/article_recommend')
def article_recommend():
    """
    根据用户模型推荐文章
    :return: code 1=成功 0=未知用户 data 数组
    """
    token = request.values.get('token')
    db = Database()
    result = []
    user = db.get({'token': token, 'is_del': 0}, 'user')  # 获取用户信息
    if user:
        article_list = []
        personas = db.get({'user_id': user['id']}, 'user_personas', 0)
        if personas:
            sorted(personas, key=lambda personas: personas['weight'], reverse=True)
            for value in personas:
                article_id = item_cf("../CollaborativeFiltering/item_simi.txt", value['article_id'] - 1)
                article_list.append(article_id + 1)
        for value in article_list:
            book = db.get({'id': value}, 'article')
            if book:
                book.update({'num_comment': 0, 'like': 0})  # 获取评论与收藏数（需要更改）
                flag = True
                for it in result:
                    if it['id'] == book['id']:
                        flag = False
                if flag:
                    result.append(book)
        return jsonify({'code': 1, 'msg': '', 'data': result})
    return jsonify({'code': 0, 'msg': 'unexpected user'})


@app.route('/api/reading/comment_recommend')
def comment_recommend():
    """
    根据用户模型推荐批注
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token, 'is_del': 0}, 'user')  # 获取用户信息
    if user:
        comment = db.get({'state': 0}, 'postil', 0)
        data = []
        for value in comment:
            if value['state'] == 0:
                article = db.get({'id': value['article_id']}, 'article')  # 获取批注所在文章
                if article:
                    uploader = db.get({'id': value['user_id'], 'is_del': 0}, 'user')  # 获取批注上传人
                    if uploader:
                        data.append({
                            'id': value['id'],
                            'book_id': article['id'],
                            'comment': value['content'],
                            'comment_uploader_id': value['user_id'],
                            'comment_uploader': uploader['nickname'],
                            'comment_start': value['start'],
                            'comment_end': value['end'],
                            'num_comment': db.count({'postil_id': value['id'], 'state': 0}, 'postil_comment'),
                            'like': 0  # 要改
                        })
        if data:
            return jsonify({'code': 1, 'msg': 'success', 'data': data})
        return jsonify({'code': -1, 'msg': 'empty data'})
    return jsonify({'code': 0, 'msg': 'unexpected user'})


@app.route('/api/reading/tag_recommend')
def tag_recommend():
    """
    根据用户模型推荐tag
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token, 'is_del': 0}, 'user')
    if user:
        pass


'''
    用户接口(用于用户对外，如 推荐教师等) user
'''


@app.route('/api/user/teacher_recommend')
def teacher_recommend():
    """
    根据用户模型推荐老师
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token, 'is_del': 0}, 'user')
    if user:
        pass


@app.route('/api/user/student_recommend')
def student_recommend():
    """
    根据用户模型推荐学生
    :return:
    """
    token = request.values.get('token')
    db = Database()
    user = db.get({'token': token, 'is_del': 0}, 'user')
    if user:
        pass


@app.route('/api/user/user_detail')
def user_detail():
    """
    获取用户详细信息
    :return: code 0=未知用户 1=成功 -1=未知错误
    """
    user_id = request.values.get('user_id')
    db = Database()
    user = db.get({'id': user_id}, 'user')
    if user:
        article = db.get({'user_id': user_id}, 'article', 0)  # 获取该用户的文章列表
        article_list = []
        for value in article:
            article_list.append({'id': value['id'], 'title': value['title']})  # 处理列表
        data = {
            'id': user['id'],
            'nickname': user['nickname'],
            'introduction': '',  # 因为没有简介字段所以现在是空的,
            'article': article_list
        }
        return jsonify({'code': 1, 'msg': 'success', 'data': data})  # 返回
    return jsonify({'code': 0, 'msg': 'unknown user'})  # 未知用户


'''
    上传接口
'''


@app.route('/api/upload/upload_article', methods=['POST'])
def upload_article():
    """
    上传接口
    :return: code 1=成功 0=未知用户 -1=未知错误
    """
    token = request.form['token']
    db = Database()
    user = db.get({'token': token}, 'user')  # 通过用户token获取用户信息
    if user:
        base_path = ''
        article = request.files['article']
        article_path = os.path.join(base_path, 'static', 'upload',
                                    str(datetime.datetime.now().timestamp() * 6) + article.filename)
        article.save(article_path)  # 上传文章

        image = request.files['image']
        image_path = os.path.join(base_path, 'static', 'upload',
                                  str(datetime.datetime.now().timestamp() * 6) + image.filename)
        image.save(image_path)  # 上传封面

        title = request.form['title']
        author = request.form['author']

        flag = db.insert({
            'file_path': change_route(article_path, 1),
            'image_path': change_route(image_path, 1),
            'title': title,
            'author': author,
            'uploader': int(user['id'])
        }, 'article')  # 添加记录
        if flag:
            with open(article_path, 'r') as file:
                result = pred(file.read())
                print(result)
                data = db.get({'file_path': change_route(article_path, 1)}, 'article')
                if data:
                    for value in result:
                        tag_flag = db.insert({
                            'article_id': data['id'],
                            'name': value['name'],
                            'weight': value['weight']
                        }, 'article_tag')
                        if not tag_flag:
                            return jsonify({'code': -1, 'msg': 'tag insert failed'})  # tag注入错误
                return jsonify({'code': 1, 'msg': 'success'})  # 成功返回
        return jsonify({'code': -1, 'msg': 'unknown error'})  # 未知错误
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 未知用户


@app.route('/api/message/get_message')
def get_message():
    token = request.form['token']
    db = Database()
    user = db.get({'token': token}, 'user')
    if user:
        pass
    return jsonify({'code': 0, 'msg': 'unexpected user'})  # 未知用户


def change_route(route, change_type=0):
    """
    改变route路径
    :param route: 原路径
    :param change_type: 转化种类 1=\\转/ 0=/转\\
    :return: 转换后的内容
    """
    if change_type == 0:
        return route.replace('/', '\\')
    else:
        return route.replace('\\', '/')


if __name__ == '__main__':
    # 开启调试模式，修改代码后不需要重新启动服务即可生效
    # 请勿在生产环境下使用调试模式
    # Flask服务将默认运行在localhost的5000端口上

    # with open('static\\upload\\36.txt', 'rb') as file:
    #     result = pred(file.read())
    #     print(result[0])
    app.run(debug=True)

from flask import Flask, request

# 创建app
app = Flask(__name__)


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


if __name__ == '__main__':
    # 开启调试模式，修改代码后不需要重新启动服务即可生效
    # 请勿在生产环境下使用调试模式
    # Flask服务将默认运行在localhost的5000端口上
    app.run(debug=True)

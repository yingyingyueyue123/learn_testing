from flask import Flask, request, json, abort

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'hello yueyue'


@app.route('/mock', methods=['POST', 'GET'])
def mock():
    if request.method == 'GET':
        abort(404)
    else:
        try:
            name = request.form['name']
            print(name)
            if name == 'yueyue':
                data = {"status": 200, "message": "True", "response": {"orderID": 100}}
            else:
                data = {"status": 400, "message": "False", "response": {}}
        except:
            data = {"status": 500, "message": "Server Error", "response": {}}
        return json.dumps(data)


if __name__ == '__main__':
    app.run()

"""
这段代码实现了这一功能：访问 http://127.0.0.1:5000，直接返回“hello world”。

直接使用 GET 方式访问http://127.0.0.1:5000/mock，会出现 404 错误。

如果使用 POST 方式，假设提交的数据中包括“name=yueyue”这个键值对，则返回如下结果：

{"status": 200, "message": "True", "response": {"orderID": 100}}
如果你提交的数据中不包括“name=yueyue”， 则返回如下结果：

{"status": 400, "message": "False", "response": {}}
如果代码在运行过程中发生了错误，则返回如下结果：
{"status": 500, "message": "Server Error", "response": {}}
"""

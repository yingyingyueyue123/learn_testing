from flask import jsonify, Flask

app = Flask(__name__)  # 创建flask实例，用来接收web请求

getMsg = {
    "code": 0,
    "msg": "OK",
}


@app.route('/mock', methods=['GET', 'POST'])  # get post
def get_mock():
    return jsonify(getMsg)


delMsg = {
    'code': 0,
    'msg': 'delete success'
}


@app.route('/mock/deleteMock', methods=['DELETE'])  # delete
def delete_mock():
    return jsonify(delMsg)


putMsg = {
    'code': 0,
    'msg': 'put success'
}


@app.route('/mock/putMock', methods=['PUT'])  # put
def put_mock():
    return jsonify(putMsg)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8888,
        debug=True
    )

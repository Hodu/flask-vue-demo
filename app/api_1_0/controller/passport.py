from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)

from app.api_1_0 import bp
from flask import request, jsonify


@bp.route('/register', methods=['POST'])
def register():
    # curl 127.0.0.1:5000/api/v1.0/register -X POST -d 'username=阿尔维奇' -d 'mobile=13108765051'
    # form_data = request.values
    # return '注册接收到 \n 姓名：%s \n 手机：%s \n' % (form_data['username'], form_data['mobile'])

    # curl 127.0.0.1:5000/api/v1.0/register -X POST -d '{"username":"阿尔维奇","mobile":"13108765051"}' -H 'Content-Type: application/json'
    # json_data = request.get_json()
    # return '注册接收到 \n 姓名：%s \n 手机：%s \n' % (json_data['username'], json_data['mobile'])

    file_date = request.files.get('logo')
    file_date.save(file_date.filename)
    return file_date.filename + ' \n'


# curl 127.0.0.1:8001/api/v1.0/login -X POST -H 'Content-Type: application/json' -d '{"username":"airvip"}'
@bp.route('/login', methods=['POST'])
def login():
    username = request.get_json()['username']
    # 验证自己做
    ret = {
        "access_token": create_access_token(identity=username),
        "refresh_token": create_refresh_token(identity=username)
    }
    return jsonify(ret)


# curl 127.0.0.1:8001/api/v1.0/protected -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNDMzMzEwNywianRpIjoiNTk2MWU4YTItNzVmYS00OGQ3LTgyOTYtNjRmMDEzY2QzOGZkIiwibmJmIjoxNjE0MzMzMTA3LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiYWlydmlwIiwiZXhwIjoxNjE0MzQwMzA3fQ.W8xu0RlPvdadJec5Bm4HoJvY94dBvZXTZx8NZBEMJa0'
@bp.route('/protected', methods=['GET'])
@jwt_required(fresh=True)
def protected():
    username = get_jwt_identity()
    print("=====> username: ", username)
    return jsonify(username=username)


# curl 127.0.0.1:8001/api/v1.0/refresh -X POST -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNDMzMjk1MywianRpIjoiOTg2MjRhZTEtMjU2MC00NGM2LWJhZmUtY2EzM2Q4NzI4NGFlIiwibmJmIjoxNjE0MzMyOTUzLCJ0eXBlIjoicmVmcmVzaCIsInN1YiI6ImFpcnZpcCIsImV4cCI6MTYxNjkyNDk1M30.3ZIj2VwrW7t7rX1KhWOkSaKqe6eNne3mcYRJQBR8wyE'

@bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    print("----> current_user: ", current_user)
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret)

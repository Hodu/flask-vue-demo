from flask import jsonify, render_template

from app.api_1_0 import bp
from app.api_1_0.model.user import UserModel
from app import db, cache


# curl 127.0.0.1:8001/api/v1.0/user -X post -d ''
@bp.route('/user', methods=['POST'])
def add_user():
    """
    新增数据分为三个步骤:
        1.创建对象
        2.添加到会话
        3.提交会话
    """
    user = UserModel()
    user.username = '阿尔维奇'
    user.mobile = '13303465052'
    user.password = '123456'

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return '添加失败'

    return '添加成功'


# curl 127.0.0.1:8001/api/v1.0/user -X get
@bp.route('/user', methods=['GET'])
def list_user():
    try:
        user_obj = UserModel.query.all()
    except Exception as e:
        return '查询失败'

    user_list = []
    for user in user_obj:
        user_list.append(user.to_dict())

    return jsonify(user_list)


# curl 127.0.0.1:8001/api/v1.0/user -X get
@bp.route('/user2', methods=['GET'])
def list_user_template():
    try:
        user_obj = UserModel.query.all()
    except Exception as e:
        return '查询失败'

    user_list = []
    for user in user_obj:
        user_list.append(user.to_dict())

    return render_template("api/users.html", users=user_list)


# curl 127.0.0.1:8001/api/v1.0/user/1 -X get
@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user_obj = UserModel.query.filter_by(id=id).all()
    except Exception as e:
        return '查询失败'

    user_list = []
    for user in user_obj:
        user_list.append(user.to_dict())

    return jsonify(user_list)


# curl 127.0.0.1:8001/api/v1.0/user/1 -X get
@bp.route('/user2/<int:id>', methods=['GET'])
@cache.cached(timeout=50)
def get_user_template(id):
    print("------------》get_user_template： ", id)
    try:
        print("user_" + str(id))
        user_list = cache.get("user_" + str(id))
        print("get user list from cache: ", user_list)
        if user_list is None:
            user_obj = UserModel.query.filter_by(id=id).all()
    except Exception as e:
        print("exp - ", e)
        return '查询失败'

    if user_list is None:
        user_list = []
        for user in user_obj:
            user_list.append(user.to_dict())
        cache.set("user_" + str(id), user_list)  # 缓存30s

    return render_template("api/user-detail.html", users=user_list)


"""
修改：
1.查询对象
2.修改数据
3.提交会话
"""


# curl 127.0.0.1:8001/api/v1.0/user/2 -X put
@bp.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        UserModel.query.filter_by(id=id).update({"username": "小可爱"})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return '更新失败'
    return '更新成功'


# curl 127.0.0.1:8001/api/v1.0/user-new/3 -X put
# 作用同上，只是先查询后提交
@bp.route('/user-new/<int:id>', methods=['PUT'])
def update_user_new(id):
    try:
        user_obj = UserModel.query.get(id)
        user_obj.username = 'airvip'
        user_obj.mobile = '13808765012'
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return '更新失败'
    return '更新成功'


"""
删除
"""


# curl 127.0.0.1:8001/api/v1.0/user/4 -X delete
@bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user_obj = UserModel.query.get(id)
        db.session.delete(user_obj)
        db.session.commit()
    except Exception as e:
        print("----delete exp -", e)
        db.session.rollback()
        return '删除失败'
    return '删除成功'

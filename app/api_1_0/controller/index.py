from app.api_1_0 import bp
from app.tasks.compute.tasks import mycomputer
from flask import render_template, current_app, jsonify


@bp.route('/', methods=['GET'])
def index():
    return render_template("api/index.html", data={'name': 'Flask', 'version': '1.1.2'})


@bp.route('/name/<obj_name>')
def hello(obj_name):
    obj_name = obj_name[0].upper()+obj_name[1:].lower()
    print("--> obj_name ", obj_name)
    return render_template("api/index.html", data={'name': obj_name, 'version': '1.1.2'})


@bp.route('/nameid/<int:_id>')
def hello1(_id):
    return 'hello %d \n' % _id


# "http://127.0.0.1:5000/api/v1.0/xixi/ ok
# "http://127.0.0.1:5000/api/v1.0/xixi ok
@bp.route('/xixi/')
def xixi():
    return 'xixi'


# "http://127.0.0.1:5000/api/v1.0/haha ok
# "http://127.0.0.1:5000/api/v1.0/haha/ not ok
@bp.route('/haha')
def haha():
    return 'haha'


@bp.route('/mymobile/<re(r"1[3-9]\d{9}"):mobile>')
def mymobile(mobile):
    return mobile

@bp.route('/mylog')
def logtest():
    current_app.logger.debug("我是 debug 级别")
    current_app.logger.info("我是 info 级别")
    current_app.logger.warning("我是 warning 级别")
    current_app.logger.error("我是 error 级别")
    current_app.logger.critical("我是 critical 级别")

    try:
        num = 1/0
    except ZeroDivisionError as e:
        current_app.logger.error("除数为 0")
    except Exception as e:
        current_app.logger("未知原因报错")

    return '愿世界一切安好，程序永无BUG！！！'


@bp.route('/jisuan')
def jisuan():
    mycomputer.delay(9)
    return 'ok \n'


@bp.route('/msg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)

from flask import Flask
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

import logging
from logging.handlers import RotatingFileHandler

from config import config_map
from app.utils.commons import ReConverter

# 创建数据库对象
db = SQLAlchemy()

# 创建 cache 对象
cache = Cache()

# 创建 jwt 对象
jwt = JWTManager()

# 设置日志的记录级别
logging.basicConfig(level=logging.DEBUG)  # 调试级别 debug
# 创建日志记录器，指明日志保存路径、每个日志文件的最大大小 100Kb、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录格式  日志等级 输入日志信息的文件名 行数  日志错误
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象 (flask app使用) 添加日志记录器
logging.getLogger().addHandler(file_log_handler)


# 工厂模式
def create_app(config_name):
    app = Flask(__name__)

    # 设置 flask 的配置信息
    config_class = config_map[config_name]
    app.config.from_object(config_class)

    # 使用 app 初始化 db
    db.init_app(app)

    # 使用 app 初始化 cache
    cache.init_app(app)

    # 使用 app 初始化 jwt
    jwt.init_app(app)

    # 为 flask 添加自定义的转换器
    app.url_map.converters["re"] = ReConverter

    # 注册蓝图
    from app import api_1_0
    app.register_blueprint(api_1_0.bp, url_prefix="/api/v1.0")

    # 如果只是接口，可以不注册 admin 模块
    # from app import admin
    # app.register_blueprint(admin.bp, url_prefix="/admin")

    # 注册提供静态文件的蓝图
    from app import html
    app.register_blueprint(html.html)

    return app

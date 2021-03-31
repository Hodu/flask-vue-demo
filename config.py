
class Config(object):
    SECRET_KEY = "AIRVip123456airvip"

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1:3306/test"
    # 如果设置成 True (默认),Flask-SQLAlchemy 将会追踪对象的修改并且发送信号,需要额外的内存。
    # 如果不必要，可以禁用。
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True  # 开发模式开启可以查看 sql 语句

    # cache
    CACHE_TYPE = "redis"
    CACHE_DEFAULT_TIMEOUT = 7200
    CACHE_KEY_PREFIX = 'dc_fl_'
    CACHE_REDIS_HOST = "127.0.0.1"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 1

    # 数据库、cache 配置省略
    # JWT
    JWT_ACCESS_TOKEN_EXPIRES = 7200


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config_map = {
    "dev": DevelopmentConfig,
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}


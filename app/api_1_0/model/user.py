from app import db
from . import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
import datetime, time


class UserModel(BaseModel, db.Model):
    __tablename__ = "base_user"

    id = db.Column(db.BigInteger, comment='pk', primary_key=True) # 用户id
    username = db.Column(db.String(50), nullable=False, default='') # 用户名
    mobile = db.Column(db.String(11), nullable=False, unique=True) # 手机号
    password_hash = db.Column(db.String(128), nullable=False) # 密码
    avatar_url = db.Column(db.String(255), nullable=False, default='') # 密码

    # 添加 property 装饰器之后，会把函数变为属性，属性名即为函数名
    @property
    def password(self):
        raise AttributeError("can't read")

    @password.setter
    def password(self, origin_password):
        self.password_hash = generate_password_hash(origin_password)

    def check_password(self, origin_password):
        return check_password_hash(self.password_hash, origin_password)

    def to_dict(self):
        return {
            "user_id": self.id,
            "username": self.username,
            "mobile": self.mobile,
            "avatar_url": self.avatar_url,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        }

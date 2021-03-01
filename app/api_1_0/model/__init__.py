from app import db
import datetime, time


class BaseModel(object):
    now_date_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    create_time = db.Column(db.DateTime, nullable=False, default=now_date_time, comment='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, default=now_date_time, onupdate=now_date_time, comment='更新时间')
    is_delete = db.Column(db.Integer, nullable=False, default=0, comment='是否删除，0否，1删除')

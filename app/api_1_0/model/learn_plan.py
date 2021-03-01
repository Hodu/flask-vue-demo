from app import db
from . import BaseModel
import datetime


class LearnPlanModel(BaseModel, db.Model):
    """
    学习计划表
    """
    __tablename__ = "learn_plan"

    now_date_time = datetime.datetime.now() + datetime.timedelta(hours=8)

    id = db.Column(db.BigInteger, comment='pk', primary_key=True)  # id
    title = db.Column(db.String(50), nullable=False, default='')  # 标题
    content = db.Column(db.String(255), nullable=False, default='')  # 内容
    expect_finish_time = db.Column(db.DateTime, nullable=False, default=now_date_time, comment='预计完成时间')  # 预计完成时间
    actual_finish_time = db.Column(db.DateTime, nullable=False, default=now_date_time, comment='实际完成时间')  # 实际完成时间
    author_id = db.Column(db.BigInteger, comment="作者id")  # 作者id

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "expect_finish_time": self.expect_finish_time.strftime("%Y-%m-%d %H:%M:%S"),
            "actual_finish_time": self.actual_finish_time.strftime("%Y-%m-%d %H:%M:%S") if self.actual_finish_time else "",
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        }


from celery import Celery
from app.tasks import config


# 定义 celery 对象
celery_app = Celery("tasks_app")

# 引入配置信息
celery_app.config_from_object(config)

# 自动搜寻异步任务
celery_app.autodiscover_tasks(["app.tasks.compute"])

from app.tasks import celery_app
import time


@celery_app.task
def mycomputer(num):
    time.sleep(5)
    return num ** 9

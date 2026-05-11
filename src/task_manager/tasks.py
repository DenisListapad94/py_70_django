from celery import shared_task


@shared_task
def add(x, y):
    import time
    time.sleep(60)
    return x + y


@shared_task
def mul(x, y):
    return x * y

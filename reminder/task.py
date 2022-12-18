from celery import shared_task


@shared_task
def test():
    print('들어옴')

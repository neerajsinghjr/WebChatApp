from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def get_sum(x,y):
    x = max(x,y)
    for i in range(x):
        print(f"i: {i}")
    return x+y
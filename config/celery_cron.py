from celery.schedules import crontab


# BEAT SCHEDULER;;
beat_schedule = {
    # everyday, midnight
    'TASK-GET-SUM-TWO-NUMBER': {
        'task': 'apps.home.task.get_sum',
        'schedule': crontab(hour='12', minute='44', day_of_week='*'),
        'kwargs': {'x': 100, 'y': 100},
    },
}
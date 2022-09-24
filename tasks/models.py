
from django.db import models
from django.utils import timezone


class Task(models.Model):
    DEFAULT = 'DEFAULT'
    HOBBY = 'HOBBY'
    DUTIES = 'DUTIES'
    WORK =' WORK'
    CATEGORIES = (
        (DEFAULT,DEFAULT),
        (HOBBY, HOBBY),
        (DUTIES,DUTIES),
        (WORK,WORK)
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    body =models.TextField(null=True, blank=True)
    due_date = models.DateField(default=timezone.now)
    deadline = models.DateField(default=timezone.now)
    task_finished = models.BooleanField(default=True)
    notification_send = models.BooleanField(default=True)
    category = models. CharField(max_length=20, choices=CATEGORIES, default=DEFAULT)

    def __str__(self):
        return f'{self.title}'

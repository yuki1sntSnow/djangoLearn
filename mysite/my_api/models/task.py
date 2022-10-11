from django.db import models
from my_api.models import BaseModel
from datetime import date


class Task(BaseModel):
    class Meta:
        db_table = 'task'
        verbose_name = verbose_name_plural = 'task' 

    PRIORITY_CHOICES = (
        (0, 'small'), 
        (1, 'mid'),
        (2, 'large'),
    )

    todo = models.CharField(
        verbose_name="do",
        max_length=255
    )

    priority = models.IntegerField(
        verbose_name="priority",
        choices=PRIORITY_CHOICES
    )

    complete_flag = models.BooleanField(
        verbose_name="flag",
        default=False
    )

    def __str__(self):
        return self.todo
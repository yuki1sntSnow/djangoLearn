from django.db import models


class BaseModel(models.Model):
    """
    common model
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name='login time', 
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='update time',
        auto_now=True
    )
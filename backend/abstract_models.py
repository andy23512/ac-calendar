import uuid
from django.db import models


class TimeStampedModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-create_time']


class UUIDModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )

    class Meta:
        abstract = True

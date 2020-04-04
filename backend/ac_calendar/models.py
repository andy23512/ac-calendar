from django.db import models

from abstract_models import TimeStampedModel, UUIDModel

# Create your models here.


class Category(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=10)
    order = models.IntegerField()


class Work(UUIDModel, TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='works')
    name = models.CharField(max_length=100)
    next_episode = models.IntegerField()
    notes = models.TextField(max_length=100)

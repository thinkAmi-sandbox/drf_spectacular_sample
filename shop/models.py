from django.db import models
from django.utils import timezone


class Shop(models.Model):
    name = models.CharField('名前', max_length=255)
    established_at = models.DateTimeField('設立日時', default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

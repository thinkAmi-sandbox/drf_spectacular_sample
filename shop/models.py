from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    class Size(models.IntegerChoices):
        SMALL = 1, _('小')
        MEDIUM = 2, _('中')
        LARGE = 3, _('大')

    name = models.CharField('名前', max_length=255)
    size = models.IntegerField('規模', choices=Size.choices, default=Size.MEDIUM)
    established_at = models.DateTimeField('設立日時', default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

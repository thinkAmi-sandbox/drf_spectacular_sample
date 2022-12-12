from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save


class Company(models.Model):
    name = models.CharField('名前', max_length=255)


class Shop(models.Model):
    class Size(models.IntegerChoices):
        SMALL = 1, _('小')
        MEDIUM = 2, _('中')
        LARGE = 3, _('大')

    name = models.CharField('名前', max_length=255)
    size = models.IntegerField('規模', choices=Size.choices, default=Size.MEDIUM)
    established_at = models.DateTimeField('設立日時', default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, verbose_name='会社', on_delete=models.PROTECT, default=1)


# auto_rowなupdated_atがfixtureだけでは設定できないため、signalを使ってfixtureのときだけ自分で設定
# https://stackoverflow.com/a/64984759
def fix_updated_at_by_fixture(sender, instance, **kwargs):
    if kwargs['raw']:
        instance.updated_at = timezone.now()


pre_save.connect(fix_updated_at_by_fixture, sender=Shop)


class Apple(models.Model):
    name = models.CharField('りんご名', max_length=255)
    shops = models.ManyToManyField(Shop, verbose_name='店')

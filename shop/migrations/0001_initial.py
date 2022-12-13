# Generated by Django 4.1.4 on 2022-12-11 01:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('established_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='設立日時')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

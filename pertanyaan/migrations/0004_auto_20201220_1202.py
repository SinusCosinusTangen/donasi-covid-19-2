# Generated by Django 3.1.2 on 2020-12-20 05:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pertanyaan', '0003_auto_20201113_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='name',
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

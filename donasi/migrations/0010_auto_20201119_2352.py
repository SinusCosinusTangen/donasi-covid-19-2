# Generated by Django 3.1.2 on 2020-11-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donasi', '0009_auto_20201119_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donasi',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='media/'),
        ),
    ]

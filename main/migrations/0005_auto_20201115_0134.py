# Generated by Django 3.1.2 on 2020-11-15 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201113_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendonor',
            name='method',
            field=models.CharField(choices=[('Transfer Bank', 'Transfer Bank'), ('Pepew Pay', 'Pepew Pay'), ('Go Pew', 'Go Pew'), ('OPEW', 'OPEW'), ('Pew Aja', 'Pew Aja')], default='1', max_length=100, null=True),
        ),
    ]

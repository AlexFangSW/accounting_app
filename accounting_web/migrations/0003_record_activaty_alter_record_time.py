# Generated by Django 4.0.3 on 2022-03-18 07:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_web', '0002_alter_record_id_alter_record_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='activaty',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 18, 7, 17, 48, 473410, tzinfo=utc)),
        ),
    ]
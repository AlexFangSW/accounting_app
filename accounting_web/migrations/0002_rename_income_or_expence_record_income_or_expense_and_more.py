# Generated by Django 4.0.3 on 2022-03-21 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='income_or_expence',
            new_name='income_or_expense',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='income_or_expence',
            new_name='income_or_expense',
        ),
    ]

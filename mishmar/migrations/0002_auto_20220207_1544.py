# Generated by Django 3.2.8 on 2022-02-07 13:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mishmar', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrganizationShifts',
            new_name='OrganizationShift',
        ),
        migrations.AlterField(
            model_name='week',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 7, 13, 44, 43, 77969, tzinfo=utc)),
        ),
    ]
